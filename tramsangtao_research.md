# Research: tramsangtao.com

> Ngày: 2026-03-27 | Stack: Next.js App Router | Hosting: Cloudflare

---

## 1. On-page SEO

| Tín hiệu | Giá trị | Đánh giá |
|---|---|---|
| `<title>` | `AI Studio` | ❌ **Quá ngắn, không có keyword, không có brand name** |
| `<meta description>` | `Tạo ảnh và video với AI nhanh chóng và hoàn toàn tự động.` | ⚠️ Ổn về ý nghĩa nhưng thiếu CTA và keyword chính |
| `lang` attribute | `en` | ❌ **Site tiếng Việt nhưng lang=en** |
| `canonical` | Không tìm thấy trong static HTML | ⚠️ Cần kiểm tra lại bằng browser |
| JSON-LD schema | Không tìm thấy trong SSR HTML | ⚠️ Có thể inject qua JS – cần browser render test |
| OpenGraph tags | Không có | ❌ Thiếu hoàn toàn |
| H1 | Render bằng JS (`HeroSection`) – không thể xác nhận qua static | ⚠️ Cần browser test |

**Blog page (`/blog`):** cùng title + meta description với homepage → **duplicate metadata nghiêm trọng**.

---

## 2. Technical SEO

### Sitemap (`/sitemap.xml`) ✅ Tốt
- Có sitemap, accessible
- **24 URLs** được khai báo
- Đã bao gồm: `/`, `/image`, `/video`, `/motion-control`, `/kol-ai`, `/pricing`, `/docs`, `/tools`, `/download`, `/about`, `/blog`, `/contact`, `/faq`, `/guide`, `/terms`, `/privacy`, `/refund`, + 6 guide sub-pages
- `lastmod` cập nhật theo realtime (2026-03-27) ✅
- **Vấn đề:** `/blog` có priority `0.6` nhưng không có slug blog nào trong sitemap → **nếu đã có bài đăng, cần thêm vào sitemap**

### Robots.txt ⚠️ Cần review
```
User-agent: *
Allow: /
Disallow: /admin/, /auth/, /login, /partner/, /referral, /account, /api/
```
- Cho phép Google crawl tất cả / ✅
- **Chặn Google-Extended, GPTBot, ClaudeBot, Bytespider** → OK về policy
- **Vấn đề:** Cloudflare Managed block `CloudflareBrowserRenderingCrawler` – có thể ảnh hưởng render test
- Sitemap reference ✅: `Sitemap: https://tramsangtao.com/sitemap.xml`

### Crawlability
- Site dùng Next.js CSR/RSC hybrid → **HTML tĩnh rất ít nội dung**
- Nội dung chính render qua React Suspense → Google cần render JS
- `Cloudflare Analytics` + `Google Analytics (G-XV0MTFTEYG)` ✅

---

## 3. Blog (`/blog`)

- Tồn tại trong sitemap với priority `0.6`
- `/blog` page hiện render bằng JS client — **không có bài viết nào được SSR**
- Title + meta desc = **giống hệt homepage** → duplicate
- **Chưa có bài blog nào** (hoặc nếu có thì không xuất hiện trong sitemap)

---

## 4. Nội dung & Sản phẩm

### Target audience (từ homepage content)
- **Affiliate Marketing:** 1 ảnh → 100 video review tự động (TikTok Shop, Shopee Affiliate)
- **Content Creator:** Ảnh/banner ads trong 2 phút, multi-platform
- **Automation Lovers:** 10,000+ prompts, batch processing, API, scheduled tasks

### AI Models hiện có
| Model | Type | Badge |
|---|---|---|
| Nano Banana Pro | Image | Mới |
| Kling 2.6 | Video | Hot |
| Veo3 | Video | Mới |
| Sora 2 Pro | Video | Hot |
| Fashional Style | Image | – |
| Upscale 4K | Tool | – |

### Pricing
| Gói | Giá | Credits | Ảnh/tháng | Video/tháng |
|---|---|---|---|---|
| Trải Nghiệm | 99.000 VND | 2.000 | 400 | 100 |
| Tiết Kiệm ⭐ PHỔ BIẾN | 199.000 VND | 4.500 | 900 | 250 |
| Sáng Tạo | 499.000 VND | 13.000 | 2.600 | 700 |
| UNLIMITED | INCOMING | Không giới hạn | – | – |

Thanh toán: Momo, Bank | Hoàn tiền 7 ngày | Hủy bất cứ lúc nào

---

## 5. Vấn đề SEO Ưu Tiên (Priority)

### 🔴 Critical
1. **Title tag homepage** = `"AI Studio"` — không có brand, không có keyword VN → Google sẽ rewrite
2. **`lang="en"` trên site tiếng Việt** — sai signal ngôn ngữ, ảnh hưởng Vietnamese SERP
3. **Blog `/blog` không có bài nào trong sitemap** — mất cơ hội index content

### 🟠 High Impact
4. **Duplicate title + meta desc** giữa homepage và `/blog`
5. **Thiếu OpenGraph tags** — share lên social media không có preview
6. **Không có JSON-LD Article schema** trên blog posts (cần verify qua browser)
7. **Canonical tags** — chưa xác nhận presence, cần test

### 🟡 Medium
8. **Blog content = zero** — không có bài viết nào → không có organic traffic từ long-tail keywords
9. **Sitemap không include `/blog/[slug]`** — cần implement khi có content
10. **Internal linking** từ homepage/pricing → blog chưa tồn tại

---

## 6. Quick Wins

| Action | Effort | Impact |
|---|---|---|
| Sửa `<title>` homepage → `"Tạo Ảnh & Video AI \| Trạm Sáng Tạo"` | 5 phút | Cao |
| Thêm `lang="vi"` vào `<html>` | 1 phút | Cao |
| Thêm `generateMetadata()` unique cho `/blog` | 30 phút | Cao |
| Thêm OpenGraph meta | 1 giờ | Trung bình |
| Publish 5-10 bài blog đầu tiên | 1-2 ngày | Rất cao |
| Thêm JSON-LD Article schema | 2 giờ | Trung bình |

---

## 7. Keyword Opportunities — Deep Research

> 0 bài blog hiện tại = mọi keyword đều là cơ hội xanh. Competition tiếng Việt còn rất thấp.

---

### 🟣 Pillar 1: AI Video Generator — Core Platform Keywords

#### SERP Landscape
- **Đang rank top:** gearvn.com, xtmobile.vn, cellphones.com.vn, slimcrm.vn, mona.media
- **Dạng content top:** Listicle "Top 10 công cụ tạo video AI" — toàn review tool nước ngoài (Pictory, Lumen5, InVideo)
- **Gap:** Hầu hết bài viết VN chỉ list tool, **KHÔNG** có hướng dẫn thực chiến step-by-step dùng Kling/Veo3/Sora
- **Sora update:** OpenAI đã ngừng Sora consumer app (3/2026) — cơ hội viết bài "Sora đã chết, đây là lựa chọn thay thế"

| Keyword | Intent | SERP Top 3 hiện tại | Content Gap | Góc viết cho tramsangtao |
|---|---|---|---|---|
| tạo video AI miễn phí | Commercial | gearvn (listicle), xtmobile (listicle), mona.media | Toàn list tool nước ngoài, không hướng dẫn thực tế | **"Top 5 cách tạo video AI miễn phí 2026 + Demo thực tế"** — embed video output từ tramsangtao |
| AI video generator Việt Nam | Commercial | Chưa có bài nào target chính xác | Không ai own keyword này | **Own keyword ngay** — "AI Video Generator Việt Nam: Tại sao tramsangtao là lựa chọn #1" |
| hướng dẫn tạo video AI 2026 | Informational | cellphones (generic), slimcrm | Surface-level, không kèm demo | **Tutorial video + text** — gom Kling + Veo3 + motion control vào 1 bài master |
| Kling AI tiếng Việt | Navigational | aifacefy.com (review EN), 1office.vn | Chưa có bài VN chuyên sâu nào | **"Kling AI Tiếng Việt: Hướng dẫn đầy đủ từ A-Z"** — tính năng, pricing, so sánh |
| Kling 2.6 review | Informational | aifacefy (EN-first), flux-ai.io | Zero bài review VN chuyên về 2.6 | **Review chuyên sâu:** tính năng mới (audio sync, aspect ratio, 1080p), benchmark với 2.5 Turbo |
| Veo3 là gì cách dùng | Informational | cellphones, dienmaycholon, vnreview, dantri | Toàn bài tin tức, **không** có hướng dẫn thực chiến | **How-to:** cách đăng ký (cần VPN → US), dùng qua Gemini/Flow, tạo video có tiếng Việt |
| Sora 2 Pro review | Informational | 24h.com.vn (tin tức ngừng hoạt động) | Sora consumer app đã đóng → opportunity viết "thay thế" | **"Sora đã dừng — 3 AI video thay thế tốt hơn (Kling, Veo3, Motion Control)"** |
| so sánh AI video generator 2026 | Informational | Chưa ai target chính xác năm 2026 | Listicle cũ chỉ so sánh tool EN | **Bảng so sánh chi tiết:** Kling 2.6 vs Veo3 vs Sora 2 (RIP) — giá, chất lượng, tốc độ, tiếng Việt |
| motion control AI video | Informational | Không bài VN nào target | Near-zero VN content | **First-mover:** "Motion Control AI là gì? Biến nhân vật tĩnh thành video nhảy/nói" |

**People Also Ask (dự đoán):**
- Tạo video AI bao nhiêu tiền?
- Kling AI có hỗ trợ tiếng Việt không?
- Video AI tạo ra có bị dính watermark không?
- Veo3 có miễn phí không?
- Nên dùng Kling hay Veo3?

---

### 👗 Pillar 2: Tạo Ảnh Mẫu Thời Trang AI

#### SERP Landscape
- **Đang rank top:** Shopee.vn (hướng dẫn built-in), riomedia.vn, WeShop AI, fptshop.com.vn
- **Dạng content:** Hướng dẫn dùng Shopee AI + giới thiệu WeShop AI
- **Gap:** Không ai so sánh chất lượng các tool (Shopee AI vs WeShop vs FLUX vs Midjourney), không ai từ góc platform VN
- **Shopee trend:** Shopee đã tích hợp "thử đồ trên người mẫu ảo" + "tối ưu hình ảnh AI" miễn phí trong Kênh Người Bán

| Keyword | SERP Top 3 | Content Gap | Góc viết | CTA |
|---|---|---|---|---|
| tạo ảnh model AI thời trang | WeShop AI (EN), riomedia.vn | Không ai benchmark chất lượng | **So sánh output:** Shopee AI vs WeShop vs FLUX (qua tramsangtao) — kèm ảnh thật | `/image` |
| người mẫu AI thời trang VN | giaiphapmoipro.vn, congdongai.vn | Bài ngắn, không thực chiến | **Case study:** 1 shop quần áo VN dùng AI → tiết kiệm bao nhiêu tiền chụp ảnh | `/image` |
| tạo ảnh mặc quần áo AI | Shopee.vn (built-in feature) | Shopee AI chỉ basic, không premium | **"Vượt xa Shopee AI"** — tạo lookbook pro bằng FLUX/Seedream trên tramsangtao | `/image` |
| AI lookbook thời trang | Gần như zero VN | Chưa ai viết keyword này bằng tiếng VN | **First-mover:** "AI Lookbook: Thay photoshoot bằng AI — chi phí 0 đồng" | `/image` |
| ảnh model AI cho shop online | riomedia.vn, shopee.vn | Toàn nói về Shopee Video AI | **Tutorial:** step-by-step tạo 20 ảnh model/ngày cho Shopee/TikTok | `/pricing` |
| thay nền ảnh sản phẩm AI | penci.vn, photoroom.com | Mostly intro tool, ít hướng dẫn VN | **"Thay nền ảnh sản phẩm AI trong 30 giây"** — dùng remove BG + tạo nền mới bằng FLUX | `/tools` |
| FLUX tạo ảnh model | Chưa ai target VN | Zero content VN | **Hướng dẫn prompt FLUX:** tạo ảnh model thời trang VN style, kèm prompt library | `/image` |

**People Also Ask:**
- Tạo ảnh model AI có vi phạm bản quyền không?
- Shopee có cho đăng ảnh AI không?
- Chi phí tạo ảnh model AI bao nhiêu?
- Ảnh model AI trông có giả không?
- Nên dùng tool nào tạo ảnh thời trang AI?

---

### 🛍️ Pillar 3: Ảnh & Video AI cho Affiliate (TikTok Shop / Shopee)

#### SERP Landscape
- **Đang rank top:** YouTube (Kaloclip, TopView Board AI tutorials), zenodigital.vn, tiktok.com seller center
- **Dạng content:** Chủ yếu video YouTube hướng dẫn, rất ít bài blog text
- **Gap lớn nhất:** **Không blog VN nào** hướng dẫn chi tiết workflow "từ 1 ảnh → 100 video affiliate" bằng text
- **Tool landscape:** Kaloclip (5 phút/video), HeyGen (avatar AI), SceneCraft AI (ảnh → clip motion), FastMoss AI (research + script)
- **TikTok native:** TikTok Shop có Image-to-Video tool built-in (AI Fashion Video Maker) — nhưng chất lượng thấp

| Keyword | SERP Top 3 | Content Gap | Góc viết | CTA |
|---|---|---|---|---|
| tạo video review sản phẩm AI | YouTube (Kaloclip tutorial) | Zero blog text chuyên sâu | **Bài pillar:** "Hướng dẫn tạo video review sản phẩm AI cho TikTok Shop — 5 phương pháp" | `/video` |
| 1 ảnh tạo 100 video review TikTok | Không ai target chính xác | Zero — keyword viral nhưng không ai viết blog | **First-mover:** workflow step-by-step dùng batch processing tramsangtao, kèm output demo | `/video` |
| tạo video affiliate TikTok Shop bằng AI | YouTube videos, zenodigital.vn | Blog text = zero, toàn video format | **SEO text advantage:** bài 2000w kèm screenshots step-by-step, link thẳng tới studio | `/pricing` |
| ảnh sản phẩm AI TikTok Shop | tiktok.com seller center, shopee.vn | Hướng dẫn của TikTok quá chung chung | **"Ảnh sản phẩm AI chuẩn TikTok Shop"** — kích thước, aspect ratio, background tips | `/image` |
| tạo video bán hàng AI tự động | fastcare.vn, fptshop.com.vn | Generic, không nói về scale/batch | **Batch workflow:** 1 prompt template → 50 videos/ngày → schedule đăng tự động | `/video` |
| hướng dẫn làm affiliate AI TikTok | YouTube dominant | Blog = gap khổng lồ | **Bài A-Z 3000w:** đăng ký affiliate → chọn sản phẩm → tạo content AI → tối ưu → scale | `/pricing` |
| remove background AI miễn phí | penci.vn, photoroom.com | So sánh tool nước ngoài, không VN | **"Xóa nền ảnh sản phẩm AI — 5 tool miễn phí + 1 cách nhanh nhất"** (hint: tramsangtao/tools) | `/tools` |
| upscale ảnh sản phẩm 4K AI | Gần zero VN | Chưa ai viết bằng tiếng Việt | **Tutorial ngắn:** "Nâng ảnh sản phẩm lên 4K trong 1 click" — dùng Upscale 4K trên tramsangtao | `/tools` |

**People Also Ask:**
- Làm affiliate TikTok Shop có cần vốn không?
- Dùng video AI bán hàng TikTok có bị khóa tài khoản không?
- 1 video affiliate AI tạo mất bao lâu?
- Hoa hồng affiliate TikTok Shop bao nhiêu?
- Video AI review có tăng tỷ lệ chuyển đổi không?

---

### 🕺 Pillar 4: Video Nhảy AI & Lip Sync TikTok ⭐ PRIORITY

#### SERP Landscape
- **Đang rank top:** cellphones.com.vn, phucanh.vn, anonyviet.com, thegioididong.com
- **Dạng content:** Hướng dẫn dùng Higgsfield, CapCut AI — surface-level (500-800w, ít chi tiết)
- **Tool ecosystem:** Higgsfield.ai (free dance), Kling AI Motion Control (premium), VideoWeb AI, CapCut AI
- **Gap lớn nhất:** Không bài VN nào hướng dẫn **Kling Motion Control cho nhảy/lip sync** — tất cả chỉ nói Higgsfield
- **Viral potential:** Keyword "video AI nhảy TikTok triệu view" có search intent cực rõ và evergreen

| Keyword | SERP Top 3 | Content Gap | Góc viết | CTA |
|---|---|---|---|---|
| cách tạo video AI nhảy TikTok | cellphones (Higgsfield guide), phucanh | Chỉ nói Higgsfield, không nói Kling MC | **"3 cách tạo video AI nhảy TikTok (Free → Pro)"** — Higgsfield (free) → CapCut → Kling MC (pro) | `/motion-control` |
| video AI nhảy triệu view | cellphones.com.vn, thegioididong | Tips chung chung, không có case study | **Case study thật:** "Tạo video AI nhảy 1M+ view — từng bước + analytics" → kèm ảnh chứng minh | `/motion-control` |
| hướng dẫn làm video nhảy AI | phucanh (Higgsfield), anonyviet | 500-800w, thiếu tips optimize | **Bài 2000w chi tiết:** chọn ảnh, chọn video mẫu, cài đặt, optimize cho viral, nhạc trending | `/motion-control` |
| tạo video hát nhép AI TikTok | cellphones (basic guide) | Không ai hướng dẫn lip sync chuyên sâu | **"Lip Sync AI: Biến ảnh tĩnh thành video hát nhép siêu thật"** — Kling lip sync + KOL AI | `/kol-ai` |
| lip sync AI video tạo thế nào | aiappvn.com, toolify.ai | Toàn tool EN, không hướng dẫn VN | **Tutorial VN đầu tiên:** lip sync bằng Runway ML vs Kling Avatars, so sánh chất lượng | `/kol-ai` |
| tạo video nhảy từ 1 ảnh AI | phucanh (Higgsfield) | Chỉ 1 tool, chỉ free option | **"Từ 1 ảnh → video nhảy pro"** — so sánh Higgsfield (free, basic) vs Kling MC (pro, mượt hơn) | `/motion-control` |
| Kling motion control lip sync | ZERO kết quả VN | **Không ai viết** | **First-mover opportunity:** owner keyword hoàn toàn, hướng dẫn chi tiết Kling MC trên tramsangtao | `/motion-control` |

**Content viết nên kèm:**
- Video demo output thật (embed YouTube/TikTok hoặc GIF)
- Ảnh trước/sau so sánh
- List nhạc trending TikTok phù hợp để nhảy AI
- Hashtag strategy (#AITikTok, #VideoAI, #KlingAI, #MotionControl)
- Tips chọn ảnh input tốt nhất (toàn thân, nền trơn, tay chân rõ)

**People Also Ask:**
- Video AI nhảy có bị TikTok hạn chế không?
- Tạo video nhảy AI mất bao lâu?
- Dùng ảnh người thật hay ảnh AI nhảy tốt hơn?
- Video nhảy AI có cần credit không?
- Higgsfield vs Kling motion control cái nào tốt hơn?

---

### 🎭 Pillar 5: KOL AI / Avatar AI

#### SERP Landscape
- **Đang rank top:** giaiphapmoipro.vn (bài chuyên sâu nhất VN hiện tại), thanhnien.vn, cleverads.vn
- **Thị trường:** VN influencer marketing $150-200M by 2025, TikTok 70M monthly active users VN
- **TikTok tools:** Symphony Avatars (tạo avatar AI từ creator thật), Smart+ (tự động hóa ads)
- **Gap:** Chỉ có giaiphapmoipro viết bài dài — phần lớn là tin tức xu hướng, **KHÔNG** hướng dẫn thực chiến tạo KOL AI
- **Monetization angles:** Affiliate, booking quảng cáo, bán hàng TikTok Shop, tạo persona không lộ mặt

| Keyword | SERP Top 3 | Content Gap | Góc viết | CTA |
|---|---|---|---|---|
| KOL AI là gì | giaiphapmoipro (overview), cleverads | Bài overview, không action steps | **"KOL AI là gì? + Hướng dẫn tạo KOL AI TikTok kiếm tiền từ tuần 1"** — educate + action | `/kol-ai` |
| cách tạo KOL AI TikTok | YouTube (tool tutorials) | Blog text = gap | **Step-by-step:** tạo avatar AI → tạo video nói → đăng TikTok → monetize qua affiliate | `/kol-ai` |
| avatar AI TikTok tạo thế nào | mobilecity.vn (Lensa AI), dienthoaivui | Chỉ nói avatar ảnh tĩnh, không video | **"Avatar AI TikTok 2026"** — bao gồm video avatar (Kling Avatars 2.0) không chỉ ảnh | `/kol-ai` |
| virtual influencer AI VN | Bài EN dominant (twimbit.com) | Near-zero VN blog | **"Virtual Influencer VN: Xu hướng tỷ đô và cách bắt đầu"** — case study VN + global | `/kol-ai` |
| tạo người ảo AI bán hàng | giaiphapmoipro (1 bài) | Chỉ theory, không practical | **Practical guide:** tạo persona → tạo voice → tạo video intro → chạy content → chốt đơn | `/kol-ai` |
| cách làm KOL AI kiếm tiền | YouTube tutorials | Blog = zero | **"5 cách kiếm tiền từ KOL AI"** — affiliate, booking ads, TikTok Shop, brand deals, nội dung không lộ mặt | `/pricing` |
| TikTok Symphony Avatar | thanhnien.vn (tin tức) | Tin tức nhưng không hướng dẫn | **Tutorial:** cách đăng ký + dùng Symphony Avatar cho ads TikTok, so sánh với Kling Avatars | `/kol-ai` |

**People Also Ask:**
- KOL AI có bị coi là lừa đảo không?
- TikTok có cho phép dùng avatar AI bán hàng không?
- Chi phí tạo 1 KOL AI bao nhiêu?
- KOL AI có thể livestream không?
- Dùng KOL AI có cần kỹ năng gì đặc biệt?

---

### 🖼️ Pillar 6: Tạo Ảnh AI — Công Cụ & How-to

#### SERP Landscape
- **Đang rank top:** congdongai.vn, ecpmedia.vn, vinalink.edu.vn (listicle tools)
- **Dạng content:** "Top 10 tool tạo ảnh AI" — listicle nước ngoài (Midjourney, DALL-E, Canva AI)
- **Gap:** Không ai viết hướng dẫn FLUX, Nano Banana, Seedream — đều là model mới, VN near-zero content

| Keyword | SERP Top 3 | Content Gap | Góc viết | CTA |
|---|---|---|---|---|
| tạo ảnh AI miễn phí 2026 | congdongai, ecpmedia (listicle) | List tool cũ, không cập nhật 2026 | **"Tạo ảnh AI miễn phí 2026: 7 công cụ mới nhất (bao gồm Imagen 4, Grok Image)"** | `/image` |
| FLUX tạo ảnh hướng dẫn | Zero VN | **Không ai viết** | **First-mover:** "FLUX 2 Pro: Hướng dẫn tạo ảnh AI chất lượng studio" — prompt tips, settings | `/image` |
| Nano Banana Pro là gì | Zero VN (proprietary model) | **Brand keyword mình phải own** | **Product page + blog:** "Nano Banana Pro — model AI tạo ảnh exclusive chỉ có trên tramsangtao" | `/image` |
| tạo ảnh AI từ mô tả tiếng Việt | vinalink (generic) | Không ai test prompt tiếng Việt | **Test thực tế:** nhập prompt VN vào FLUX, Imagen 4, Nano Banana — so sánh output | `/image` |
| upscale ảnh 4K bằng AI | Rất ít VN | Tool nước ngoài dominates | **"Upscale ảnh 4K bằng AI trong 1 click"** — dùng tramsangtao Upscale 4K tool, kèm before/after | `/tools` |
| xóa nền ảnh AI tự động | penci.vn, photoroom.com | Hướng dẫn chụp nhưng không VN tool | **"3 cách xóa nền ảnh AI tự động"** — remove.bg vs Canva vs tramsangtao (so sánh tốc độ, chất lượng) | `/tools` |
| prompt AI tạo ảnh đẹp | Rất ít VN chuyên sâu | Bài ngắn, prompt EN | **Bài resource:** "50 prompt AI tạo ảnh đẹp — tiếng Việt thực dụng" — categorized by style | `/image` |
| Midjourney thay thế miễn phí | ecpmedia (listicle) | List chung, không demo | **"5 thay thế Midjourney miễn phí"** — FLUX, Imagen 4, Nano Banana, Playground, Leonardo — có ảnh demo thật | `/image` |

**People Also Ask:**
- Tạo ảnh AI có vi phạm bản quyền không?
- Prompt tiếng Việt hay tiếng Anh tạo ảnh AI đẹp hơn?
- Tạo 1 ảnh AI mất bao lâu?
- Ảnh AI tạo ra có bán thương mại được không?

---

### 📋 Content Calendar Gợi Ý (20 bài đầu tiên)

Thứ tự **ưu tiên theo traffic potential** (Pillar 4 → 3 → 1 → 5 → 2 → 6):

| # | Tiêu đề bài | Pillar | Keyword Target | Độ dài | Ảnh cần |
|---|---|---|---|---|---|
| 1 | Hướng dẫn tạo video AI nhảy TikTok triệu view 2026 | 4 | video AI nhảy TikTok | 2000w | cover + 5 step screenshots |
| 2 | 1 ảnh tạo 100 video review sản phẩm TikTok Shop tự động | 3 | tạo video affiliate TikTok | 2000w | cover + workflow diagram |
| 3 | Kling 2.6: Review đầy đủ tính năng, giá, cách dùng 2026 | 1 | Kling AI tiếng Việt | 2500w | cover + UI screenshots + output samples |
| 4 | Cách tạo video hát nhép AI TikTok cực dễ (Lip Sync) | 4 | lip sync AI TikTok | 1800w | cover + before/after |
| 5 | Tạo ảnh sản phẩm AI cho Shopee TikTok Shop: Hướng dẫn A-Z | 3 | ảnh sản phẩm AI TikTok Shop | 2000w | cover + 3 product demos |
| 6 | KOL AI là gì? Cách tạo virtual influencer TikTok từ đầu | 5 | KOL AI là gì | 2500w | cover + avatar examples |
| 7 | Veo3 là gì? Google AI video mạnh nhất 2026 | 1 | Veo3 là gì | 2000w | cover + output comparison |
| 8 | Tạo ảnh model thời trang AI: Hết thời thuê người mẫu thật | 2 | ảnh model AI thời trang | 2000w | cover + fashion AI gallery |
| 9 | Motion Control AI: Làm nhân vật chuyển động theo ý muốn | 1 | motion control AI | 1800w | cover + GIF demos |
| 10 | Cách làm KOL AI kiếm tiền TikTok: Hướng dẫn thực chiến | 5 | cách làm KOL AI | 2000w | cover + income proof |
| 11 | FLUX vs Midjourney: So sánh AI tạo ảnh tốt nhất 2026 | 6 | Midjourney thay thế | 2000w | comparison gallery (6+ pairs) |
| 12 | Tạo ảnh AI miễn phí: Top 7 công cụ tốt nhất 2026 | 6 | tạo ảnh AI miễn phí | 2500w | tool screenshots + output |
| 13 | Hướng dẫn làm affiliate TikTok Shop bằng AI từ A-Z 2026 | 3 | làm affiliate AI TikTok | 3000w | cover + workflow + screenshots |
| 14 | Sora đã dừng — 3 AI video thay thế tốt hơn | 1 | Sora 2 Pro review | 1500w | cover + comparison table |
| 15 | Prompt AI tạo ảnh đẹp: 50 công thức tiếng Việt thực dụng | 6 | prompt AI tạo ảnh | 2500w | 20+ output images |
| 16 | Tạo video bán hàng TikTok bằng AI: Từ idea đến 100 video/ngày | 3 | video bán hàng AI | 2000w | cover + batch demo |
| 17 | Avatar AI TikTok: Cách tạo và xu hướng 2026 | 5 | avatar AI TikTok | 1800w | cover + avatar gallery |
| 18 | AI lookbook thời trang: Thay thế photoshoot với chi phí 0 đồng | 2 | AI lookbook thời trang | 2000w | lookbook gallery (10+ images) |
| 19 | Upscale ảnh 4K bằng AI: Nâng chất lượng ảnh cũ trong 1 click | 6 | upscale ảnh 4K AI | 1200w | before/after pairs |
| 20 | Xóa nền ảnh sản phẩm AI: Top 3 công cụ nhanh nhất | 6 | xóa nền ảnh AI | 1200w | comparison demo |

---

### 💡 Insight Cạnh Tranh Chi Tiết

| Competitor | Strengths | Weaknesses | Opportunity cho tramsangtao |
|---|---|---|---|
| cellphones.com.vn | Domain authority cao, bài 800-1500w | Generic, không có tool thật, copypaste | Bài sâu hơn + demo output thật từ platform |
| congdongai.vn | Niche AI, audience đúng | Cập nhật chậm, thiếu tool hands-on | Tốc độ publish + keyword fresh (2026) |
| fptshop.com.vn | DA rất cao | Tin tức surface, không tutorial | Deep tutorial > news recap |
| YouTube VN channels | Video format chiếm lĩnh | Không có SEO text blog | Blog text sẽ rank trên Google SERP |
| giaiphapmoipro.vn | Bài KOL AI dài nhất VN | Chỉ 1-2 bài, không update | Consistent publishing sẽ dominate |

**First-mover keywords (chưa ai viết VN):**
1. "Kling motion control lip sync"
2. "AI lookbook thời trang"
3. "FLUX tạo ảnh model"
4. "Nano Banana Pro là gì"
5. "AI video generator Việt Nam"
6. "bulk video AI affiliate"
7. "motion control AI video hướng dẫn"

**Chiến lược publish:**
1. **Tuần 1-2:** Pillar 4 (nhảy/lip sync) — viral bait, traffic nhanh nhất
2. **Tuần 3-4:** Pillar 3 (affiliate) — monetization, audience chính
3. **Tháng 2:** Pillar 1 (Kling/Veo3 review) — evergreen SEO
4. **Tháng 3:** Pillar 5 + 2 (KOL AI + fashion) — niche depth
5. **Ongoing:** Pillar 6 vào giữa — tool content, easy wins
