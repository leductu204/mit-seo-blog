#!/usr/bin/env python3
"""
Blog post generator: keyword → research → write → SEO fields → save as draft
Usage:
    python bin/generate.py "hướng dẫn tạo video AI nhảy TikTok"
    python bin/generate.py --batch queue/keywords.txt --workers 3
    python bin/generate.py --batch queue/keywords.txt --gen-images
"""
import os, sys, json, re, asyncio, aiohttp, argparse
from pathlib import Path
from datetime import datetime

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DRAFTS_DIR = PROJECT_ROOT / "drafts"
QUEUE_DIR = PROJECT_ROOT / "queue"

CLIPROXY_BASE = os.getenv("CLIPROXY_BASE", "http://localhost:8317/v1")
CLIPROXY_KEY = os.getenv("CLIPROXY_API_KEY", "sk-leductu")
BRAVE_API_KEY = os.getenv("BRAVE_API_KEY", "")
MODEL = os.getenv("WRITER_MODEL", "claude-sonnet-4-5")

WRITER_PROMPT = """Viết bài blog SEO tiếng Việt về: {keyword}

Yêu cầu:
- Độ dài: 1500-2000 từ
- Cấu trúc: H1 (keyword chính) → H2 (subtopics) → FAQ (4-5 câu hỏi) → CTA
- Tone: chuyên nghiệp nhưng dễ đọc, phù hợp người Việt
- CTA cuối bài: link về {cta_page} trên tramsangtao.com
- Keyword xuất hiện tự nhiên ~1-2%, không nhồi nhét
- Output: Markdown thuần, KHÔNG frontmatter, bắt đầu bằng # H1

Context về tramsangtao.com:
- Platform tạo ảnh/video AI cho thị trường VN
- Models: FLUX, Kling 2.6, Veo3, Sora 2 Pro, Nano Banana Pro
- Features: motion control, KOL AI, upscale 4K, remove BG
- Target: content creators, affiliate marketers, automation lovers

Outline gợi ý từ research:
{outline}
"""

SEO_PROMPT = """Từ bài blog sau, tạo các trường SEO. Output JSON thuần (chỉ JSON, không markdown):
{{
  "title": "...",              // H1, ≤60 chars
  "slug": "...",               // URL slug, lowercase, hyphen, ≤60 chars, tiếng Việt không dấu
  "meta_title": "...",         // SEO title ≤60 chars
  "meta_description": "...",   // ≤160 chars, hấp dẫn, chứa keyword
  "tags": ["...", "..."],      // 3-5 tags
  "description": "...",        // 1-2 câu tóm tắt
  "cta_page": "..."            // Trang CTA phù hợp nhất: /pricing, /video, /image, /motion-control, /kol-ai
}}

Bài blog:
{content}
"""


async def research_keyword(keyword: str, session: aiohttp.ClientSession) -> str:
    """Search web for keyword context via Brave API."""
    if not BRAVE_API_KEY:
        return f"(Không có Brave API key, skip research cho: {keyword})"

    url = "https://api.search.brave.com/res/v1/web/search"
    headers = {"Accept": "application/json", "X-Subscription-Token": BRAVE_API_KEY}
    params = {"q": keyword, "count": 5, "lang": "vi"}

    try:
        async with session.get(url, headers=headers, params=params) as resp:
            data = await resp.json()
            results = data.get("web", {}).get("results", [])
            return "\n".join([f"- {r['title']}: {r.get('description', '')}" for r in results[:5]])
    except Exception as e:
        return f"(Research failed: {e})"


async def call_llm(prompt: str, session: aiohttp.ClientSession) -> str:
    """Call Claude via CLIProxy."""
    payload = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 4096,
    }
    headers = {"Authorization": f"Bearer {CLIPROXY_KEY}", "Content-Type": "application/json"}

    async with session.post(f"{CLIPROXY_BASE}/messages", headers=headers, json=payload) as resp:
        data = await resp.json()
        return data["content"][0]["text"]


def save_draft(slug: str, content: str, seo: dict, source: str = "auto"):
    """Save content + frontmatter as draft markdown file."""
    draft_dir = DRAFTS_DIR / slug
    draft_dir.mkdir(parents=True, exist_ok=True)

    frontmatter = {
        **seo,
        "status": "draft",
        "source": source,
        "images_status": "pending",
        "created": datetime.now().strftime("%Y-%m-%d"),
    }

    fm_lines = ["---"]
    for k, v in frontmatter.items():
        if isinstance(v, list):
            fm_lines.append(f'{k}: {json.dumps(v, ensure_ascii=False)}')
        elif v is None:
            fm_lines.append(f"{k}: ")
        else:
            fm_lines.append(f'{k}: "{v}"' if isinstance(v, str) else f"{k}: {v}")
    fm_lines.append("---\n")

    md_path = draft_dir / "index.md"
    md_path.write_text("\n".join(fm_lines) + "\n" + content, encoding="utf-8")
    return md_path


async def generate_post(keyword: str, cta_page: str = "/pricing") -> dict:
    """Full pipeline: research → write → SEO → save draft."""
    async with aiohttp.ClientSession() as session:
        # 1. Research
        print(f"  [1/3] Researching: {keyword}")
        outline = await research_keyword(keyword, session)

        # 2. Write
        print(f"  [2/3] Writing ({MODEL})...")
        content = await call_llm(
            WRITER_PROMPT.format(keyword=keyword, cta_page=cta_page, outline=outline),
            session,
        )

        # 3. SEO fields
        print(f"  [3/3] Generating SEO fields...")
        seo_raw = await call_llm(SEO_PROMPT.format(content=content[:3000]), session)
        # Extract JSON from response
        json_match = re.search(r"\{.*\}", seo_raw, re.DOTALL)
        if not json_match:
            print(f"  ⚠️  Could not parse SEO JSON, using defaults")
            slug = re.sub(r"[^a-z0-9]+", "-", keyword.lower())[:60].strip("-")
            seo = {"title": keyword, "slug": slug, "meta_title": keyword,
                   "meta_description": keyword, "tags": [], "description": keyword,
                   "cta_page": cta_page}
        else:
            seo = json.loads(json_match.group())

        # 4. Save
        md_path = save_draft(seo.get("slug", "untitled"), content, seo)
        print(f"  ✅ Saved: {md_path}")
        return {"slug": seo["slug"], "path": str(md_path)}


async def batch_generate(keywords: list[str], workers: int = 3, gen_images: bool = False):
    """Generate multiple posts concurrently."""
    semaphore = asyncio.Semaphore(workers)

    async def bounded(kw):
        async with semaphore:
            return await generate_post(kw)

    print(f"Generating {len(keywords)} posts with {workers} workers...\n")
    tasks = [bounded(kw.strip()) for kw in keywords if kw.strip()]
    results = await asyncio.gather(*tasks, return_exceptions=True)

    success = [r for r in results if isinstance(r, dict)]
    failed = [r for r in results if isinstance(r, Exception)]
    print(f"\n{'='*40}")
    print(f"Done: {len(success)} success, {len(failed)} failed")

    if gen_images and success:
        print(f"\nGenerating images for {len(success)} posts...")
        # Import and call gen_images for each slug
        gen_script = PROJECT_ROOT / "bin" / "gen_images.py"
        for r in success:
            os.system(f'python "{gen_script}" --slug {r["slug"]} --auto-from-csv')

    return results


def main():
    parser = argparse.ArgumentParser(description="Generate SEO blog posts via AI")
    parser.add_argument("keyword", nargs="?", help="Single keyword to write about")
    parser.add_argument("--batch", type=str, help="Path to keywords.txt file")
    parser.add_argument("--workers", type=int, default=3, help="Concurrent workers (default: 3)")
    parser.add_argument("--gen-images", action="store_true", help="Also generate cover images")
    parser.add_argument("--cta", type=str, default="/pricing", help="CTA page (default: /pricing)")
    parser.add_argument("--model", type=str, help="Override LLM model")
    args = parser.parse_args()

    if args.model:
        global MODEL
        MODEL = args.model

    if args.batch:
        batch_path = Path(args.batch)
        if not batch_path.exists():
            batch_path = QUEUE_DIR / args.batch
        with open(batch_path) as f:
            keywords = [line.strip() for line in f if line.strip()]
        asyncio.run(batch_generate(keywords, args.workers, args.gen_images))
    elif args.keyword:
        print(f"Generating post for: {args.keyword}\n")
        asyncio.run(generate_post(args.keyword, args.cta))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
