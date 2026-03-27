---
name: seo-blog
description: SEO audit, optimization, and AI-powered blog content pipeline. Use when the user wants to audit SEO issues, optimize pages/posts for search engines, generate SEO-optimized blog posts, build a blog content pipeline, plan keyword strategy, add structured data (JSON-LD), or asks about "why isn't my site ranking", "SEO check", "optimize this page", "write SEO blog post", "content pipeline", "sitemap", "meta tags", "keyword research", or "Google ranking".
---

# SEO Blog Skill

Specialized SEO knowledge for auditing sites and generating SEO-optimized blog content.

## Modes

- **Audit** — analyze a URL or codebase for SEO issues
- **Optimize** — improve existing pages/posts
- **Generate** — write a new SEO-optimized blog post
- **Pipeline** — plan or implement an AI content generation pipeline

---

## SEO Fundamentals

Google: crawl → index → rank. SEO = help bots understand + give users what they search for.

**3 pillars:**
1. **On-page** — title, meta, headings, content, internal links, URL slug
2. **Technical** — sitemap, robots.txt, canonical, HTTPS, speed, structured data
3. **Off-page** — backlinks (long-term, organic)

---

## Audit Framework

Priority order:
1. Crawlability & indexation (can Google find it?)
2. Technical foundations (fast, HTTPS, mobile)
3. On-page (content optimized?)
4. Content quality (deserves to rank?)

See `references/audit-checklist.md` for full checklist.

---

## SEO-Optimized Post Structure

```
Title (H1)           ← primary keyword, ≤60 chars
Meta description     ← keyword + CTA, ≤160 chars
Slug                 ← /blog/keyword-slug (short, hyphenated)
─────────────────────
Intro (150-200w)     ← hook + state what article covers
H2: [subtopic 1]     ← secondary keyword
H2: [subtopic 2]
H2: [subtopic 3]
H2: FAQ              ← answer common questions (boosts rich results)
  H3: Q1?
  H3: Q2?
CTA                  ← link to /pricing or relevant tool
─────────────────────
Word count: 1500-2000w
Keyword density: ~1-2% (natural, not stuffed)
Images: alt text with keyword
Internal links: 2-4 links to other pages on site
JSON-LD: Article schema (see references/structured-data.md)
```

---

## Next.js Implementation (tramsangtao stack)

```typescript
// app/blog/[slug]/page.tsx
export async function generateMetadata({ params }) {
  const post = await getPost(params.slug)
  return {
    title: post.meta_title || post.title,
    description: post.meta_description || post.description,
    openGraph: { title: post.title, description: post.description, images: [post.cover_image] }
  }
}
```

Key files to implement:
- `app/sitemap.ts` — auto-include all published slugs
- `app/robots.ts` — allow /blog, disallow /api
- `app/blog/[slug]/page.tsx` — JSON-LD Article schema injection
- `lib/blog.ts` — DB queries for posts

See `references/nextjs-seo.md` for full code patterns.

---

## AI Content Pipeline

```
Keyword → [Research] → [Write] → [SEO Optimize] → [Publish]
```

Steps:
1. **Research**: web_search top 10 results, extract outline + FAQs competitors cover
2. **Write**: Claude Sonnet, 1500-2000w, Vietnamese, Markdown format
3. **SEO**: gen slug, meta_title, meta_description, tags from content
4. **Media**: optional — gen cover image via FLUX
5. **Publish**: POST /api/blog/posts with status=draft (review) or published

For batch generation (50-100 posts), use parallel workers (5 concurrent max).
See `references/content-pipeline.md` for full implementation.

---

## Writer Prompt Template

```
Viết bài blog SEO tiếng Việt về: {keyword}

Yêu cầu:
- Độ dài: 1500-2000 từ
- Cấu trúc: H1 (keyword chính) → H2 (subtopics) → FAQ → CTA
- Tone: chuyên nghiệp nhưng dễ đọc, phù hợp người Việt
- CTA cuối bài: link về {cta_page} (ví dụ: /pricing, /tools/kling)
- Kết thúc bằng section FAQ với 3-5 câu hỏi thường gặp
- Không nhồi nhét keyword, viết tự nhiên
- Output: Markdown thuần, không có frontmatter

Context về tramsangtao.com:
- Platform tạo ảnh/video AI cho thị trường VN
- Dùng FLUX, Kling, Veo3, Sora 2 Pro...
- Target: content creators, affiliate marketers
```

---

## Key Tools

- `site:domain.com` — check indexed pages
- Google Search Console — monitor indexation + clicks
- PageSpeed Insights — Core Web Vitals
- Google Rich Results Test — validate JSON-LD
