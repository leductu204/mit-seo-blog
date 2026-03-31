#!/usr/bin/env python3
"""
Blog post generator — multi-mode pipeline
Lấy tinh hoa từ content-pipeline (Affitor) + SEO-focused output

Usage:
  python3 generate_blog_post.py "keyword"
  python3 generate_blog_post.py "keyword" --mode brave              # Brave research (default)
  python3 generate_blog_post.py "keyword" --mode llm-only           # LLM only, no search
  python3 generate_blog_post.py "keyword" --format how-to           # seo|toplist|how-to|pov|case-study
  python3 generate_blog_post.py "keyword" --tone bold               # default|bold|educational|storytelling|analytical
  python3 generate_blog_post.py "keyword" --multi 3                 # gen 3 versions, auto-pick best
  python3 generate_blog_post.py --batch keywords.txt                # batch sequential
"""

import os, json, re, asyncio, aiohttp, argparse
from datetime import datetime
from typing import Literal

# ── Config ────────────────────────────────────────────────────────────────────
CLIPROXY_BASE = "http://localhost:8317/v1"
API_KEY       = os.getenv("CLIPROXY_API_KEY", "sk-leductu")
BLOG_API      = os.getenv("BLOG_API", "http://localhost:8000/api/blog/posts")
BRAVE_API_KEY = os.getenv("BRAVE_API_KEY", "")
MODEL         = os.getenv("BLOG_MODEL", "claude-sonnet-4-6")

ContentFormat = Literal["seo", "toplist", "how-to", "pov", "case-study"]
GenMode       = Literal["brave", "llm-only"]
Tone          = Literal["default", "bold", "educational", "storytelling", "analytical"]

# ── Brand Context ─────────────────────────────────────────────────────────────
BRAND_CONTEXT = """
Bạn đang viết nội dung cho tramsangtao.com — nền tảng tạo ảnh & video AI tại Việt Nam.
Target audience: người làm affiliate marketing, content creator, marketer VN.
Models có trên nền tảng: FLUX (ảnh), Kling 2.5/2.6/3.0 (video), Veo3 (video Google), Seedance 2.0 (video), Nano Banana Pro (ảnh portrait).
Tone: thực tế, hữu ích, không sáo rỗng. Viết như người trong nghề nói chuyện với đồng nghiệp.
Tuyệt đối KHÔNG dùng: "đẳng cấp", "chuyên nghiệp hàng đầu", "giải pháp toàn diện", "trong bối cảnh hiện nay".
""".strip()

# ── Tone Guide ────────────────────────────────────────────────────────────────
TONE_GUIDE = {
    "default":      "Tone: Thực tế, có dữ liệu, dễ đọc. Không học thuật, không hype.",
    "bold":         "Tone: Táo bạo, đôi khi counterintuitive. Có quan điểm rõ, dùng câu hỏi tu từ để kéo người đọc.",
    "educational":  "Tone: Giảng giải rõ ràng, dùng ví dụ và analogy. Framing kiểu 'đây là lý do tại sao cái này quan trọng'.",
    "storytelling": "Tone: Kể chuyện, bắt đầu bằng 1 tình huống/moment cụ thể. Build tension, reveal insight. Người đọc phải cảm thấy gì đó.",
    "analytical":   "Tone: Phân tích sâu, so sánh số liệu, tìm pattern. Viết như analyst cho smart audience.",
}

# ── Prompt Templates ──────────────────────────────────────────────────────────

def build_tone_section(tone: str) -> str:
    return f"## Tone\n{TONE_GUIDE.get(tone, TONE_GUIDE['default'])}"

def build_context_section(context: str, angle_note: str = "") -> str:
    parts = []
    if context:
        parts.append(f"## Research Context (dùng làm dẫn chứng nếu phù hợp)\n{context}")
    if angle_note:
        parts.append(f"## Góc tiếp cận\n{angle_note}")
    return "\n\n".join(parts)


def seo_prompt(keyword: str, context: str, cta_page: str, tone: str = "default", angle: str = "") -> str:
    return f"""{BRAND_CONTEXT}

## Nhiệm vụ
Viết bài blog SEO tiếng Việt, dài 1500-2000 từ về: **{keyword}**

{build_tone_section(tone)}

## Cấu trúc bắt buộc
1. H1 — chứa keyword chính, tự nhiên
2. Intro (2-3 đoạn) — hook bằng vấn đề thực tế người đọc hay gặp
3. Body H2s — 4-6 section, mỗi section có ví dụ cụ thể
4. FAQ — 4-5 câu hỏi thường gặp, trả lời ngắn gọn
5. CTA — kêu gọi thử {cta_page} trên tramsangtao.com, tự nhiên

## Yêu cầu SEO
- Keyword density ~1-2%, xuất hiện tự nhiên
- Output: Markdown thuần

{build_context_section(context, angle)}"""


def toplist_prompt(keyword: str, context: str, cta_page: str, tone: str = "default", angle: str = "") -> str:
    return f"""{BRAND_CONTEXT}

## Nhiệm vụ
Viết bài "Top X..." về: **{keyword}**

{build_tone_section(tone)}

## Cấu trúc Toplist
1. HOOK (1-2 dòng) — con số ấn tượng hoặc tuyên bố táo bạo
2. CONTEXT (2-3 dòng) — tại sao topic này quan trọng lúc này
3. DANH SÁCH — mỗi item: Tên → điểm nổi bật → khi nào nên dùng
4. TAKEAWAY — pattern chung, bài học rút ra
5. CTA — gợi ý thử tool liên quan trên tramsangtao.com

## Rules
- Tối thiểu 5 items, tối đa 10, mỗi item phải có data/ví dụ cụ thể
- Output: Markdown

{build_context_section(context, angle)}"""


def howto_prompt(keyword: str, context: str, cta_page: str, tone: str = "default", angle: str = "") -> str:
    return f"""{BRAND_CONTEXT}

## Nhiệm vụ
Viết bài hướng dẫn step-by-step về: **{keyword}**

{build_tone_section(tone)}

## Cấu trúc How-to
1. Intro — bài này dạy được gì, mất bao lâu, cần gì
2. Prerequisites — cần chuẩn bị gì trước
3. Steps (đánh số) — mỗi bước: làm gì + tại sao + tip tránh lỗi
4. Kết quả mong đợi — trông như thế nào khi làm đúng
5. Troubleshooting — 2-3 lỗi phổ biến + cách fix
6. CTA — thử ngay trên tramsangtao.com

## Rules
- Bước phải cụ thể, làm theo được ngay
- Output: Markdown

{build_context_section(context, angle)}"""


def pov_prompt(keyword: str, context: str, cta_page: str, tone: str = "default", angle: str = "") -> str:
    return f"""{BRAND_CONTEXT}

## Nhiệm vụ
Viết bài góc nhìn/opinion về: **{keyword}**

{build_tone_section(tone)}

## Cấu trúc POV
1. HOOK — câu mở đầu counterintuitive hoặc gây tranh cãi
2. THESIS — quan điểm rõ ràng của bài
3. EVIDENCE — 3-4 dẫn chứng cụ thể ủng hộ quan điểm
4. COUNTERPOINT — thừa nhận 1 phản bác, rồi refute
5. CONCLUSION — tóm lại + implication
6. CTA — link tự nhiên đến tramsangtao.com

## Rules
- Phải có quan điểm rõ, không nước đôi
- Dùng ngôi thứ nhất
- Output: Markdown

{build_context_section(context, angle)}"""


def case_study_prompt(keyword: str, context: str, cta_page: str, tone: str = "default", angle: str = "") -> str:
    return f"""{BRAND_CONTEXT}

## Nhiệm vụ
Viết bài case study về: **{keyword}**

{build_tone_section(tone)}

## Cấu trúc Case Study
1. HOOK (1-2 dòng) — metric/kết quả ấn tượng nhất lên đầu
2. CONTEXT — vấn đề tồn tại là gì, thị trường trông như thế nào
3. HỌ ĐÃ LÀM GÌ — chiến lược cụ thể, tool dùng, bước thực hiện
4. KẾT QUẢ — số liệu cụ thể, outcome đo được
5. BÀI HỌC — takeaway không hiển nhiên, người đọc có thể áp dụng ngay
6. CTA — kêu gọi thử {cta_page} trên tramsangtao.com

## Rules
- Focus vào 1 case/nhân vật cụ thể, không lan man
- Problem → Action → Result → Lesson arc
- Số liệu cụ thể ở mọi điểm có thể
- Output: Markdown

{build_context_section(context, angle)}"""


PROMPT_FNS = {
    "seo":        seo_prompt,
    "toplist":    toplist_prompt,
    "how-to":     howto_prompt,
    "pov":        pov_prompt,
    "case-study": case_study_prompt,
}

# ── Angle variations cho multi-gen ───────────────────────────────────────────
ANGLE_VARIANTS = [
    "Góc độ người mới bắt đầu: focus vào việc setup lần đầu, tránh lỗi thường gặp.",
    "Góc độ chuyên gia/power user: tips nâng cao, optimize workflow, hidden features.",
    "Góc độ so sánh: đặt trong bối cảnh cạnh tranh với các tool khác, lý do chọn cái này.",
    "Góc độ business/ROI: focus vào kết quả đo được, tiết kiệm thời gian, tăng doanh thu.",
    "Góc độ use case cụ thể: chọn 1 ngành/scenario cụ thể (e.g., TikTok affiliate, ecom).",
]

SEO_SCORER_PROMPT = """Đánh giá 3 bài blog dưới đây theo tiêu chí SEO và chất lượng content.

Keyword mục tiêu: {keyword}

{versions}

Chấm điểm mỗi bài (0-10) theo:
- SEO potential (keyword usage, structure, search intent match)
- Content quality (depth, examples, uniqueness)
- Engagement (hook, readability, CTA)

Output JSON:
{{
  "winner": 1,  // index 1-based của bài tốt nhất
  "scores": [
    {{"version": 1, "seo": 8, "quality": 7, "engagement": 8, "total": 23, "reason": "..."}},
    {{"version": 2, "seo": 6, "quality": 8, "engagement": 7, "total": 21, "reason": "..."}},
    {{"version": 3, "seo": 7, "quality": 6, "engagement": 6, "total": 19, "reason": "..."}}
  ]
}}
"""

SEO_FIELDS_PROMPT = """Từ bài blog dưới đây, extract các trường SEO.

Bài blog:
{content}

Output JSON (chỉ JSON, không có text khác):
{{
  "title": "...",
  "slug": "...",
  "meta_title": "...",
  "meta_description": "...",
  "tags": ["...", "..."],
  "description": "..."
}}

Rules:
- title: H1 của bài, ≤60 chars
- slug: lowercase, hyphen, ≤60 chars, tiếng Việt không dấu
- meta_title: ≤60 chars
- meta_description: ≤160 chars, hấp dẫn, chứa keyword chính
- tags: 3-5 tags tiếng Việt
- description: 1-2 câu tóm tắt
"""


# ── Brave Research ────────────────────────────────────────────────────────────

async def research_keyword(keyword: str, session: aiohttp.ClientSession) -> str:
    if not BRAVE_API_KEY:
        return ""

    url = "https://api.search.brave.com/res/v1/web/search"
    headers = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip",
        "X-Subscription-Token": BRAVE_API_KEY,
    }
    params = {"q": keyword, "count": 10, "freshness": "pm", "text_decorations": "false"}

    try:
        async with session.get(url, headers=headers, params=params) as resp:
            data = await resp.json()
            results = data.get("web", {}).get("results", [])

        await asyncio.sleep(1.1)  # Brave free plan rate limit
        async with session.get(
            "https://api.search.brave.com/res/v1/news/search",
            headers=headers,
            params={"q": keyword, "count": 5, "freshness": "pw"},
        ) as resp2:
            news_data = await resp2.json()
            news = news_data.get("results", [])

        lines = []
        for r in (news[:3] + results[:5])[:8]:
            title = r.get("title", "")
            desc  = r.get("description", "") or ""
            if title:
                lines.append(f"- {title}: {desc[:200]}")

        return "\n".join(lines)

    except Exception as e:
        print(f"  ⚠️ Research failed: {e}")
        return ""


# ── LLM Call ──────────────────────────────────────────────────────────────────

async def call_claude(prompt: str, session: aiohttp.ClientSession) -> str:
    payload = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 4096,
    }
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    async with session.post(
        f"{CLIPROXY_BASE}/chat/completions", headers=headers, json=payload
    ) as resp:
        data = await resp.json()
        return data["choices"][0]["message"]["content"]


# ── Multi-version + Auto-scorer ───────────────────────────────────────────────

async def gen_multi_versions(
    keyword: str,
    context: str,
    fmt: ContentFormat,
    tone: str,
    cta_page: str,
    n: int,
    session: aiohttp.ClientSession,
) -> tuple[str, list[dict]]:
    """Gen n versions với angles khác nhau, LLM tự chọn best. Return (best_content, scores)."""
    import random
    angles = random.sample(ANGLE_VARIANTS, min(n, len(ANGLE_VARIANTS)))
    prompt_fn = PROMPT_FNS.get(fmt, seo_prompt)

    print(f"  Generating {n} versions...")
    versions = []
    for i, angle in enumerate(angles, 1):
        print(f"    Version {i}/{n} (angle: {angle[:50]}...)")
        content = await call_claude(
            prompt_fn(keyword, context, cta_page, tone, angle), session
        )
        versions.append(content)

    # Auto-score + pick best
    print(f"  Scoring {n} versions...")
    versions_block = "\n\n---\n\n".join(
        [f"## Version {i+1}\n{v[:800]}..." for i, v in enumerate(versions)]
    )
    score_raw = await call_claude(
        SEO_SCORER_PROMPT.format(keyword=keyword, versions=versions_block), session
    )
    try:
        score_data = json.loads(re.search(r'\{.*\}', score_raw, re.DOTALL).group())
        winner_idx = score_data.get("winner", 1) - 1
        scores = score_data.get("scores", [])
    except Exception:
        winner_idx = 0
        scores = []

    winner_idx = max(0, min(winner_idx, len(versions) - 1))
    print(f"  → Winner: Version {winner_idx + 1}")
    if scores:
        for s in scores:
            marker = "✓" if s.get("version") == winner_idx + 1 else " "
            print(f"    [{marker}] v{s.get('version')} total={s.get('total')} — {s.get('reason','')[:60]}")

    return versions[winner_idx], scores


# ── Publish ───────────────────────────────────────────────────────────────────

async def publish_post(post: dict, session: aiohttp.ClientSession) -> dict:
    async with session.post(
        BLOG_API, json=post, headers={"Content-Type": "application/json"}
    ) as resp:
        if resp.status in (200, 201):
            return await resp.json()
        else:
            text = await resp.text()
            print(f"  ❌ Publish failed {resp.status}: {text[:200]}")
            return post


# ── Main Pipeline ─────────────────────────────────────────────────────────────

async def generate_post(
    keyword: str,
    mode: GenMode = "brave",
    fmt: ContentFormat = "seo",
    tone: str = "default",
    cta_page: str = "/pricing",
    status: str = "draft",
    publish: bool = True,
    multi: int = 1,
) -> dict:
    async with aiohttp.ClientSession() as session:

        # Step 1: Research
        context = ""
        if mode == "brave":
            print(f"  [1/4] Researching: {keyword}")
            context = await research_keyword(keyword, session)
            if context:
                print(f"        {len(context.splitlines())} sources found")
        else:
            print(f"  [1/4] Skipping research (llm-only)")

        # Step 2: Write (single or multi-version)
        print(f"  [2/4] Writing (format={fmt}, tone={tone}, versions={multi})...")
        if multi > 1:
            content, scores = await gen_multi_versions(
                keyword, context, fmt, tone, cta_page, multi, session
            )
        else:
            prompt_fn = PROMPT_FNS.get(fmt, seo_prompt)
            content = await call_claude(
                prompt_fn(keyword, context, cta_page, tone), session
            )

        # Step 3: SEO fields
        print(f"  [3/4] Extracting SEO fields...")
        seo_raw = await call_claude(
            SEO_FIELDS_PROMPT.format(content=content[:3000]), session
        )
        try:
            seo = json.loads(re.search(r'\{.*\}', seo_raw, re.DOTALL).group())
        except Exception:
            seo = {
                "title": keyword,
                "slug": re.sub(r'[^a-z0-9-]', '-', keyword.lower())[:60],
                "meta_title": keyword[:60],
                "meta_description": keyword[:160],
                "tags": [],
                "description": keyword,
            }

        post = {
            **seo,
            "content": content,
            "status": status,
            "published_at": datetime.utcnow().isoformat() if status == "published" else None,
        }

        # Step 4: Publish
        if publish:
            print(f"  [4/4] Publishing...")
            result = await publish_post(post, session)
            print(f"  ✅ /blog/{seo.get('slug')}")
            return result
        else:
            print(f"  ✅ Done (no publish): {seo.get('slug')}")
            return post


# ── Batch (sequential) ────────────────────────────────────────────────────────

async def batch_generate(
    keywords: list[str],
    mode: GenMode = "brave",
    fmt: ContentFormat = "seo",
    tone: str = "default",
    status: str = "draft",
    publish: bool = True,
    multi: int = 1,
):
    print(f"Batch: {len(keywords)} keywords | mode={mode} | format={fmt} | tone={tone} | versions={multi}\n")
    results = []
    for i, kw in enumerate(keywords, 1):
        print(f"[{i}/{len(keywords)}] {kw}")
        try:
            result = await generate_post(
                kw, mode=mode, fmt=fmt, tone=tone,
                status=status, publish=publish, multi=multi
            )
            results.append({"keyword": kw, "status": "ok", "slug": result.get("slug")})
        except Exception as e:
            print(f"  ❌ Error: {e}")
            results.append({"keyword": kw, "status": "error", "error": str(e)})
        print()

    ok = sum(1 for r in results if r["status"] == "ok")
    print(f"Done: {ok}/{len(keywords)} succeeded")
    return results


# ── CLI ───────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Blog post generator")
    parser.add_argument("keyword", nargs="?", help="Keyword to write about")
    parser.add_argument("--batch",  metavar="FILE", help="File with keywords (one per line)")
    parser.add_argument("--mode",   choices=["brave", "llm-only"], default="brave")
    parser.add_argument("--format", dest="fmt",
                        choices=["seo", "toplist", "how-to", "pov", "case-study"], default="seo")
    parser.add_argument("--tone",   choices=list(TONE_GUIDE.keys()), default="default")
    parser.add_argument("--multi",  type=int, default=1, metavar="N",
                        help="Gen N versions, auto-pick best (default: 1)")
    parser.add_argument("--status", choices=["draft", "published"], default="draft")
    parser.add_argument("--no-publish", action="store_true",
                        help="Gen only, don't push to blog API")
    parser.add_argument("--cta",    default="/pricing", help="CTA page path")
    args = parser.parse_args()

    publish = not args.no_publish

    if args.batch:
        with open(args.batch) as f:
            keywords = [l.strip() for l in f if l.strip() and not l.startswith("#")]
        asyncio.run(batch_generate(
            keywords, mode=args.mode, fmt=args.fmt, tone=args.tone,
            status=args.status, publish=publish, multi=args.multi
        ))
    elif args.keyword:
        asyncio.run(generate_post(
            args.keyword, mode=args.mode, fmt=args.fmt, tone=args.tone,
            cta_page=args.cta, status=args.status, publish=publish, multi=args.multi
        ))
    else:
        parser.print_help()
