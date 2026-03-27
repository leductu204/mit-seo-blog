# AI Content Pipeline — Implementation

## Script: generate_blog_post.py

```python
#!/usr/bin/env python3
"""
Blog post generator: keyword → research → write → SEO → publish
Usage: python3 generate_blog_post.py "hướng dẫn tạo video AI bằng Kling 2.5"
       python3 generate_blog_post.py --batch keywords.txt --workers 5
"""
import os, json, re, asyncio, aiohttp
from datetime import datetime

CLIPROXY_BASE = "http://localhost:8317/v1"
API_KEY = os.getenv("CLIPROXY_API_KEY", "sk-leductu")
BLOG_API = os.getenv("BLOG_API", "http://localhost:8000/api/blog/posts")
BRAVE_API_KEY = os.getenv("BRAVE_API_KEY", "")

WRITER_PROMPT = """Viết bài blog SEO tiếng Việt về: {keyword}

Yêu cầu:
- Độ dài: 1500-2000 từ
- Cấu trúc: H1 (keyword chính) → H2 (subtopics) → FAQ → CTA
- Tone: chuyên nghiên cứu, chuyên nghiệp nhưng dễ đọc
- CTA cuối bài: đề xuất thử {cta_page} trên tramsangtao.com
- FAQ section với 4-5 câu hỏi thường gặp
- Keyword xuất hiện tự nhiên ~1-2%, không nhồi nhét
- Output: Markdown thuần

Context: tramsangtao.com là platform tạo ảnh/video AI cho thị trường VN, dùng FLUX, Kling, Veo3, Sora 2 Pro.

Outline gợi ý từ research:
{outline}
"""

SEO_PROMPT = """Từ bài blog sau, tạo các trường SEO:

Bài blog:
{content}

Output JSON (chỉ JSON, không có text khác):
{{
  "title": "...",           // H1 của bài, ≤60 chars
  "slug": "...",            // URL slug, lowercase, hyphen, ≤60 chars
  "meta_title": "...",      // SEO title tag ≤60 chars (có thể khác title)
  "meta_description": "...", // ≤160 chars, hấp dẫn, chứa keyword
  "tags": ["...", "..."],   // 3-5 tags tiếng Việt
  "description": "..."      // 1-2 câu tóm tắt bài
}}
"""

async def research_keyword(keyword: str, session: aiohttp.ClientSession) -> str:
    """Search web for keyword, extract outline"""
    if not BRAVE_API_KEY:
        return f"Không có Brave API key, bỏ qua research bước này cho keyword: {keyword}"
    
    url = "https://api.search.brave.com/res/v1/web/search"
    headers = {"Accept": "application/json", "X-Subscription-Token": BRAVE_API_KEY}
    params = {"q": keyword, "count": 5, "lang": "vi"}
    
    try:
        async with session.get(url, headers=headers, params=params) as resp:
            data = await resp.json()
            results = data.get("web", {}).get("results", [])
            outline = "\n".join([f"- {r['title']}: {r['description']}" for r in results[:5]])
            return outline
    except Exception as e:
        return f"Research failed: {e}"


async def call_claude(prompt: str, session: aiohttp.ClientSession, model: str = "claude-sonnet-4-6") -> str:
    """Call Claude via cliproxy"""
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 4000,
    }
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    
    async with session.post(f"{CLIPROXY_BASE}/messages", headers=headers, json=payload) as resp:
        data = await resp.json()
        return data["content"][0]["text"]


async def generate_post(keyword: str, cta_page: str = "/pricing", status: str = "draft") -> dict:
    async with aiohttp.ClientSession() as session:
        # 1. Research
        print(f"[1/4] Researching: {keyword}")
        outline = await research_keyword(keyword, session)
        
        # 2. Write
        print(f"[2/4] Writing...")
        content = await call_claude(
            WRITER_PROMPT.format(keyword=keyword, cta_page=cta_page, outline=outline),
            session
        )
        
        # 3. SEO fields
        print(f"[3/4] Generating SEO fields...")
        seo_raw = await call_claude(SEO_PROMPT.format(content=content[:3000]), session)
        seo = json.loads(re.search(r'\{.*\}', seo_raw, re.DOTALL).group())
        
        # 4. Publish
        print(f"[4/4] Publishing...")
        post = {
            **seo,
            "content": content,
            "status": status,
            "published_at": datetime.utcnow().isoformat() if status == "published" else None,
        }
        
        async with session.post(BLOG_API, json=post, headers={"Content-Type": "application/json"}) as resp:
            if resp.status in (200, 201):
                result = await resp.json()
                print(f"✅ Created: /blog/{seo['slug']}")
                return result
            else:
                text = await resp.text()
                print(f"❌ Publish failed: {resp.status} {text}")
                return post


async def batch_generate(keywords: list[str], workers: int = 5):
    semaphore = asyncio.Semaphore(workers)
    
    async def bounded(kw):
        async with semaphore:
            return await generate_post(kw)
    
    tasks = [bounded(kw) for kw in keywords]
    return await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == "__main__":
    import sys
    if "--batch" in sys.argv:
        idx = sys.argv.index("--batch")
        with open(sys.argv[idx + 1]) as f:
            keywords = [line.strip() for line in f if line.strip()]
        workers = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 5
        print(f"Batch generating {len(keywords)} posts with {workers} workers...")
        asyncio.run(batch_generate(keywords, workers))
    else:
        keyword = " ".join(sys.argv[1:]) or "hướng dẫn tạo video AI"
        asyncio.run(generate_post(keyword))
```

## keywords.txt example

```
hướng dẫn tạo video AI bằng Kling 2.5
Freepik Pikaso là gì và cách dùng
tạo ảnh AI với FLUX miễn phí
Sora 2 Pro review tiếng Việt
Veo3 Google video AI hướng dẫn
AI video generator tốt nhất 2026
cách tạo video TikTok bằng AI
motion control AI video tutorial
tạo thumbnail YouTube bằng AI
AI image generator so sánh 2026
```

## Run batch

```bash
# Single post
python3 bin/generate_blog_post.py "hướng dẫn tạo video AI bằng Kling 2.5"

# Batch (50-100 keywords, 5 workers)
python3 bin/generate_blog_post.py --batch keywords.txt --workers 5
```
