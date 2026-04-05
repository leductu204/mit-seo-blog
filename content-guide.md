# Content Guide — Trạm Sáng Tạo SEO Blog

Rút từ kinh nghiệm viết và augment 26 bài SEO (Phase 1→5). Dùng file này làm checklist mỗi khi viết/review bài mới.

---

## 1. Giọng Văn & Góc Nhìn

- **Trạm Sáng Tạo là nhân vật chính**, không phải Higgsfield hay tool khác
- Các tool khác chỉ làm nền so sánh — luôn highlight tramsangtao là giải pháp tốt nhất
- Nêu rõ USP: **UI tiếng Việt, support người Việt, video hướng dẫn YouTube, giá rẻ 2-4 lần, thanh toán Momo/ngân hàng VN**
- Không PR tool đối thủ — nếu nhắc tới thì phải kèm hạn chế rõ ràng

## 2. Thông Tin Đối Thủ — Phải Chính Xác

| Tool | Giá thực | Lưu ý |
|---|---|---|
| **Higgsfield** | Từ $15/tháng (~375k VND) | KHÔNG miễn phí, thanh toán Visa/Mastercard, chất lượng hên xui |
| **Kling trực tiếp** | Từ $6.99/tháng | Gói Free có credits nhưng KHÔNG dùng được — phải nạp sub. GD tiếng Anh/Trung |
| **Trạm Sáng Tạo** | Từ 99k/tháng | ~1K VND/video (Kling 2.5 Turbo), Momo/ngân hàng VN |

> **Quy tắc:** Luôn verify giá trước khi viết. Không đoán "miễn phí" nếu chưa chắc. Gói Free có credits không có nghĩa là dùng được.
> **Tính số video:** Đem credits chia cho khung 30-80 credits/video (tùy model) để ước tính.

## 3. Ảnh — Quy Tắc Ngón Tay Cái

### Số lượng ảnh theo loại bài:

| Loại bài | Số từ | Số ảnh lý tưởng |
|---|---|---|
| How-to ngắn | 1000-1500 từ | 3-4 ảnh |
| Review / Tutorial dài | 2000-3000 từ | 4-6 ảnh |
| Pillar content / Bài main | 3000+ từ | 5-8 ảnh |

**Quy tắc ngón tay cái:** Cứ khoảng **300-500 từ nên có 1 ảnh** để phá vỡ wall-of-text và giữ người đọc cuộn tiếp. Google đánh giá cao bài viết có ảnh minh họa đúng chỗ (đặc biệt khi ảnh có alt text keyword-rich).

### Kinh nghiệm SEO về ảnh:
- **Mỗi ảnh phải có mục đích rõ ràng** — minh họa 1 bước, 1 feature, hoặc 1 so sánh cụ thể. Không nhét ảnh "cho đẹp"
- **Alt text chứa keyword** — mỗi ảnh nên có alt text mô tả nội dung + keyword liên quan (VD: "Giao diện tạo video AI trên Trạm Sáng Tạo")
- **Ảnh đầu tiên (cover) cực kỳ quan trọng** — Google Image Search lấy ảnh này làm thumbnail, nên phải sạch text, đúng chủ đề, realistic
- **Đặt tên file có nghĩa** — `tst-video-workspace.png` tốt hơn `image_001.png` (Google đọc filename)
- **Tránh ảnh quá nặng** — resize về 600-800px width, dùng optimize=True khi save PNG. Ảnh >200KB sẽ kéo page speed xuống
- **Phân bố đều trong bài** — không dồn 5 ảnh ở đầu rồi để trống 2000 từ cuối. Rải đều theo tỉ lệ 300-500 từ/ảnh
- **Caption ảnh (chữ nghiêng dưới ảnh)** giúp tăng thời gian đọc. Format: `*Mô tả ngắn ảnh — nhấn mạnh USP hoặc pain point.*`

### Chiến Thuật Mix Ảnh & Media (Rule Chốt Kỷ Tị 2026):
Để tránh bài viết bị "nhàm chán" hay "giả trân", rổ tài nguyên cho 1 bài viết Seo sẽ áp dụng theo chiến thuật Mix sau:
1. **1 Cover Image (Ảnh bìa):** Ưu tiên sử dụng YouTube HD Thumbnail thực tế (vi text giật tít tốt, đảm bảo CTR rất cao).
2. **1 Video Iframe:** Nhúng video YouTube (hướng dẫn/review) ngay trong phần đầu hoặc bước quan trọng để tối đa hóa Dwell Time (thời gian ở lại trang).
3. **2 Ảnh Inline Cào Từ Web/Youtube:** Screenshot giao diện thực tế hoặc bòn rút từ YouTube Thumbnails tạo góc nhìn thân thiện cho người dùng.
4. **1-2 Ảnh AI-Generated:** Cực kì cẩn trọng trong Prompting. Phải bám sát checklist bên dưới.
5. **Shuffle Tự Nhiên:** Khi nhúng vào framework markdown, sử dụng `random.shuffle()` hoặc xếp đan xen ngẫu nhiên để ảnh do AI sinh ra không bị tập trung chỉ vào 1 chỗ.

**💎 Tỷ lệ Vàng "8 Ảnh + 2 Video" chuyên biệt cho Master Guide (Bài Pillar 3000+ từ):**
- 1 Ảnh Cover thu hút Traffic.
- 2 Videos (1 Video overview ở đầu bài, 1 Video hướng dẫn ngách ở các section kỹ thuật sâu).
- 2 Ảnh AI-Generated (Minimalist) đặt ở các đoạn "lý thuyết chữ chay" mệt người (như đoạn Viết Prompt, Báo giá tính toán) để tạo khoảng nghỉ thị giác (visual breathing space).
- 3-4 Ảnh Web UI / Screenshot thực tế phân bổ ở các phần hướng dẫn thực hành/workflow.
- Công thức lõi: Giữ đúng nhịp "Trung bình 400 từ = 1 cụm Media" để phá hoàn toàn bức tường chữ (Wall of Text) và đè bẹp Bounce Rate.

### Checklist Cốt Lõi Khi Tạo Ảnh AI (AI Generated Images):
- **BẮT BUỘC:** Phong cách **"Clean & Minimalist"** — tông màu pastel thanh lịch (trắng, beige/kem). Ánh sáng thiên về ban mai tự nhiên (soft morning light). Motif thường là: lifestyle bàn làm việc gọn gàng, sảnh văn phòng thoáng đãng, thiết bị tối giản. Định hướng phải trông sang trọng như các công ty công nghệ / Tech Blog lớn (The Verge, TechCrunch).
- **CẤM KỴ:** Tuyệt đối KHÔNG prompt thêm hiệu ứng "công nghệ viễn tưởng", "neon lights", màu mè "xanh đỏ tím vàng", cyberpunk, holographic. Ảnh "công nghệ quá đà" mang lại tác dụng ngược ở thị trường Việt Nam năm 2026.

### Kỹ Thuật Tối Ưu (Technical SEO):
- **Luôn resize/compress ảnh:** width dao động 600-800px. Nén Save for Web (JPEG/WebP) thay vì ảnh PNG AI > 2MB khổng lồ! Trọng lượng ảnh ép < 200KB.
- **Tên file thân thiện:** Tên file chứa keyword theo chuẩn slug `ten-tool-tao-video.jpg`. Thay thế hoàn toàn tên rác kiểu `image_001.png`.
- **Alt text:** Ảnh luôn có Alt text đúng ngữ nghĩa của đoạn văn, thay thế cho từ khóa nhồi nhét.

## 3.5. Video Embed — Tăng Dwell Time & Rich Snippet

### Tại sao phải embed video?
- **Tăng dwell time** — Google coi thời gian ở trang là tín hiệu chất lượng. Bài có video người đọc ở lâu hơn 2-3 phút
- **Rich snippet trên SERP** — bài có video có thể hiển thị thumbnail video trên kết quả tìm kiếm, tăng CTR 15-30%
- **Google Video tab** — bài có embed YouTube xuất hiện ở tab Video của Google Search (traffic miễn phí)
- **Giảm bounce rate** — người đọc dừng lại xem video thay vì thoát ngay

### Số lượng video theo loại bài:

| Loại bài | Số video lý tưởng |
|---|---|
| How-to ngắn | 1 video (demo hoặc hướng dẫn) |
| Review / Tutorial dài | 1-2 video |
| Pillar content / Bài main | 2-3 video |

### Nguồn video (ưu tiên từ trên xuống):
1. **Video từ trang chính thức** — Kling, Veo, Seedance thường có showcase/demo video trên kênh YouTube chính thức, authoritative nhất
2. **YouTube Trạm Sáng Tạo** — video hướng dẫn từ kênh chính thức, embed để tăng view kênh
3. **YouTube reviewer** — review từ creator khác, dùng kèm credit
4. **TikTok / Reels viral** — video demo trending, embed bằng link hoặc screenshot
5. **Video tự tạo** — record screen demo trên TST, upload YouTube rồi embed

### Format embed trong Markdown:

**YouTube (khuyến nghị nhất):**
```markdown
[![Tên video mô tả](https://img.youtube.com/vi/VIDEO_ID/maxresdefault.jpg)](https://www.youtube.com/watch?v=VIDEO_ID)
*Xem video hướng dẫn chi tiết trên YouTube.*
```

**Hoặc iframe trực tiếp (nếu platform hỗ trợ):**
```html
<iframe width="100%" height="400" src="https://www.youtube.com/embed/VIDEO_ID" frameborder="0" allowfullscreen></iframe>
```

### Quy tắc đặt video:
- **Video đầu tiên** đặt gần đầu bài (sau intro hoặc sau section 1) — above the fold tăng engagement
- **Không đặt 2 video liền nhau** — phải có ít nhất 300-500 từ text giữa 2 video
- **Mỗi video phải có caption** giải thích nội dung: `*Xem video hướng dẫn tạo video AI trên Trạm Sáng Tạo.*`
- **Ưu tiên click-to-play thumbnail** hơn auto-embed iframe — giữ page speed nhanh
- **Luôn ghi credit** nếu dùng video của người khác: `*Nguồn: Tên kênh YouTube*`

### Video KHÔNG nên dùng:
- Video quá dài (>15 phút) — người đọc blog không xem hết, thêm timestamp nếu bắt buộc
- Video không liên quan trực tiếp đến bài viết — nhét cho có sẽ tăng bounce rate
- Video tự host (mp4 trực tiếp) — nặng bandwidth, không được Google index như YouTube

## 4. Cấu Trúc Bài SEO

```
Frontmatter (YAML)
H1: Tiêu đề chứa keyword chính + năm
├── Cover image 
├── Intro 2-3 câu (hook + promise)
├── H2: Giải thích concept (keyword definition)
├── H2: Cách 1 (tool 1 — nêu hạn chế)
├── H2: Cách 2 (tool 2 — nêu hạn chế)  
├── H2: Cách 3 (Trạm Sáng Tạo — HERO section, dài nhất)
│   ├── H3: Bảng so sánh
│   ├── H3: Hướng dẫn step-by-step + screenshot UI
│   ├── H3: Lưu ý input
│   └── H3: Bảng giá
├── H2: Video hướng dẫn (YouTube embed)
├── H2: So sánh tổng hợp (1 bảng duy nhất, không trùng)
├── H2: Tips viral/mẹo
├── H2: FAQ (5-6 câu, lấy từ People Also Ask)
└── H2: Kết luận + CTA
```

### Tránh:
- Không có 2 bảng so sánh trùng nội dung
- Không có section "Lưu ý" trùng với section "Tips"
- Heading không chứa emoji (❌ `### ⚠️ Lưu Ý` → ✅ `### Lưu Ý`)

## 5. SEO Checklist

### Frontmatter:
- [ ] `title` chứa keyword chính + năm
- [ ] `meta_title` có thêm "| Trạm Sáng Tạo"
- [ ] `meta_description` < 160 ký tự, có keyword + brand
- [ ] `slug` ngắn gọn, có keyword, dùng dấu `-`
- [ ] `tags` 5-6 từ khóa liên quan
- [ ] `cta_page` trỏ đúng trang sản phẩm

### Nội dung:
- [ ] H1 = title, xuất hiện 1 lần duy nhất
- [ ] Keyword chính xuất hiện trong 100 từ đầu
- [ ] Heading hierarchy đúng: H1 > H2 > H3 (không nhảy cấp)
- [ ] Ảnh có alt text mô tả keyword-rich
- [ ] Internal link → trang sản phẩm tramsangtao (ít nhất 2-3 lần)
- [ ] FAQ section với câu hỏi thật từ SERP
- [ ] Kết luận có CTA link rõ ràng
- [ ] ~2000-3000 từ cho pillar content

### Thông tin:
- [ ] Giá đối thủ chính xác (double check)
- [ ] Mọi claim về "miễn phí" / "rẻ hơn X lần" phải đúng thực tế
- [ ] Kết luận không recommend tool đối thủ là lựa chọn chính

## 6. Quy Trình Ảnh

1. Có YouTube video liên quan? → Dùng thumbnail làm cover
2. User cung cấp ảnh? → **Resize (PIL, width 600-800px)** → đặt tên rõ ràng (không để "image copy.png")
3. Cần ảnh đối thủ? → Vào website chính thức chụp screenshot (browser subagent)
4. Cần ảnh minh họa UI? → Screenshot thật từ site (copy vào folder draft)
5. Cần ảnh bổ sung? → `generate_image` với style **photorealistic**, người thật, nền studio
6. **Luôn resize ảnh trước khi embed:** `python -c "from PIL import Image; ..."` → width 800px (ngang) hoặc 600px (đứng)
7. Review: đếm ảnh, bài review dài OK 4-6, bài ngắn 3-4
8. Kiểm tra: không có ảnh nào trùng nội dung với text đã viết

## 7. Common Mistakes (Tránh Lặp Lại)

| Sai | Đúng |
|---|---|
| Gọi Higgsfield là "miễn phí" | Từ $15/tháng, thanh toán Visa/MC |
| Kling Free = dùng được | Có credits nhưng KHÔNG dùng được, phải nạp sub |
| Ảnh cover style cyberpunk/neon | Photorealistic, người thật, nền sạch |
| 7-8 ảnh/bài | 3-6 ảnh tùy loại bài |
| Ảnh gốc 3000px không resize | Resize 600-800px bằng PIL trước khi embed |
| Link logo SVG từ site ngoài | Chụp screenshot, save local |
| Infographic AI trùng nội dung text | Bỏ ảnh, giữ text |
| 2 bảng so sánh trùng | 1 bảng tổng hợp duy nhất |
| Kết luận "thử Higgsfield miễn phí" | "CapCut thử nhanh miễn phí" |
| Heading có emoji ⚠️ | Heading text thuần |
| PR tool đối thủ quá nhiều | Focus tramsangtao, đối thủ chỉ làm nền |
| Kling giá $9.9/tháng | $6.99 Standard, $25.99 Pro (verify trên klingai.com) |
| Tính video = credits / giá cố định | Chia theo khung 30-80 credits/video |
| Tính toán Aff sai | 1 video ~1k VND. Đơn Affiliate hoa hồng mốc: 10k-20k/đơn |
| Tạo URL nội bộ ảo (vd /blog/tts) | Link về trang gốc có thật (vd `/video`) |

## 8. Case Study — Công Thức Đã Chạy Tốt

Mỗi bài nên có 1 section **Case Study** trước khi vào FAQ/Kết luận. Đây là section có engagement cao nhất vì biến kiến thức thành câu chuyện.

**Format chuẩn (3 phần, tổng 150-250 từ):**

```
## 📈 Case Study: [Ai] Dùng [Tool Gì] Để [Đạt Kết Quả Gì]

[1 dòng giới thiệu nhân vật + ngữ cảnh]
- **Pain Point:** [Vấn đề cụ thể, có số liệu chi phí/thời gian]
- **Giải Pháp:** [Workflow cụ thể trên tramsangtao.com, mention model + prompt mẫu nếu có]
- **Kết Quả & ROI:** [Số liệu before/after, chi phí tiết kiệm, tăng trưởng]
```

**Các persona đã dùng (đừng lặp lại):**

| Persona | Dùng cho bài | ROI chính |
|---------|-------------|-----------|
| Tiệm trà sữa Đà Nẵng | kling-2-5 | 15 clip từ 5 ảnh smartphone |
| Freelancer Shopee creative | review-kling-ai | Giảm 3-4h → 30 phút/bộ |
| Shop thời trang 200+ SKU | tao-anh-ai-mien-phi | Giảm 15tr → 500k/tháng |
| Admin TikTok tâm lý | khong-can-lo-mat | 200k followers, 20k/video |
| Agency 3 người TMĐT | lam-video-tu-dong | 15 → 50 video/tuần |
| Marketer chạy FB ads | khong-can-quay | 30 video/tuần, ROAS +35% |
| Startup D2C Hà Nội | cach-dung-ai-tao-video-tiktok | 3 triệu view TikTok/tháng |
| Photographer chuyển AI | cach-tao-video-ai-tu-anh | 40% doanh thu mới từ video |

**Quy tắc viết Case Study:**
- **Nhân vật phải cụ thể** — "1 freelancer" tốt hơn "người dùng". Thêm địa danh VN (Đà Nẵng, TP.HCM) tăng relatability
- **Pain Point chứa số liệu** — "tốn 3 triệu/buổi quay" cụ thể hơn "tốn nhiều tiền"
- **Giải Pháp phải mention tramsangtao.com** — đây là CTA ngầm, không cần push mạnh
- **ROI = before vs after** — luôn có 2 con số so sánh (chi phí cũ vs chi phí mới, thời gian cũ vs mới)
- **Không dùng lại persona đã dùng** — check bảng trên trước khi viết

## 9. Pro-Tips — Công Thức "Mẹo Người Trong Nghề"

Mỗi bài nên có 1 section **Pro-Tips** với 2-3 mẹo cụ thể. Đây là section có share cao nhất vì reader bookmark/screenshot để dùng sau.

**Format chuẩn:**

```
## 💎 Pro-Tips: [Tiêu đề hấp dẫn, kiểu "Bí kíp..." hoặc "Mẹo..."]

1. **[Tên mẹo ngắn gọn]:** [Giải thích 2-3 câu, kèm ví dụ prompt hoặc workflow cụ thể]
2. **[Tên mẹo ngắn gọn]:** [Giải thích 2-3 câu]
```

**Các chủ đề Pro-Tips đã dùng (đừng lặp lại):**

| Chủ đề | Dùng trong bài |
|--------|---------------|
| Test rẻ (2.5) → Render đắt (3.0) | kling-2-5 |
| "Product photography style" keyword | kling-2-5 |
| Chê Kling đúng chỗ, chọn đúng tool | review-kling-ai |
| Character consistency bằng ảnh reference | review-kling-ai |
| Combo Gemini brainstorm + FLUX render | tao-anh-ai-mien-phi |
| "shot on Canon 5D..." keyword | tao-anh-ai-mien-phi |
| Visual Signature cố định | khong-can-lo-mat |
| Giọng thật tốt hơn TTS | khong-can-lo-mat |
| Template Prompt Library (Google Sheet) | lam-video-tu-dong |
| "3 giây đầu quyết định" | lam-video-tu-dong |
| Batch generate rồi review hàng loạt | khong-can-quay |
| "Last 2 seconds rule" - cắt 2 giây cuối | khong-can-quay |
| Negative Prompt trick | kling-ai-vs-veo-3, kling-3-0 |

**Quy tắc viết Pro-Tips:**
- **Mẹo phải actionable ngay** — reader đọc xong phải apply được trong 5 phút
- **Kèm prompt mẫu nếu liên quan** — viết bằng tiếng Anh, in nghiêng trong dấu *...*
- **Mỗi mẹo tối đa 3 câu** — ngắn gọn, dễ screenshot
- **Không trùng với nội dung chính bài** — Pro-Tips là "bonus", không phải tóm tắt bài

## 10. Internal Linking — Bản Đồ Liên Kết Nội Bộ

Đây là điểm yếu nhất hiện tại. Mỗi bài nên link sang 2-3 bài liên quan. Dưới đây là mapping đã xác nhận:

**Cluster 1: Kling (8 bài)**

```
cach-dang-ky-kling-ai (entry point)
  → kling-ai-la-gi (overview)
  → kling-ai-gia-bao-nhieu (pricing)
  → kling-ai-co-mien-phi (free tier)
  → kling-2-5-la-gi (v2.5 deep dive)
  → kling-2-6-vs-kling-3-0 (version compare)
  → kling-3-0-la-gi (v3.0 deep dive)
  → review-kling-ai-tieng-viet (review tổng hợp)
  → huong-dan-dung-kling-ai-tieng-viet (tutorial)
```

**Cluster 2: So sánh tools (5 bài)**

```
top-7-tool-tao-video-ai (pillar)
  → kling-ai-so-voi-cac-tool
  → kling-vs-sora-2025
  → kling-ai-vs-veo-3
  → 6-app-tao-video-ai
  → so-sanh-video-ai (nếu có)
```

**Cluster 3: Workflow/How-to (6 bài)**

```
cach-tao-video-ngan-bang-ai (entry point)
  → lam-video-ai-tu-dong
  → lam-video-ai-khong-can-lo-mat
  → tao-video-ai-khong-can-quay
  → cach-dung-ai-tao-video-tiktok
  → cach-tao-video-ai-tu-anh
```

**Cluster 4: Model-specific (4 bài)**

```
veo-3-la-gi
sora-2-la-gi
sora-2-danh-gia-tu-goc-nhin
seedance (trong bài kling-ai-vs-veo-3)
```

**Cluster 5: Ảnh AI (2 bài)**

```
tao-anh-ai-mien-phi
flux-vs-stable-diffusion
```

**Cách link tự nhiên trong bài:**
- "Nếu bạn chưa có tài khoản, xem [hướng dẫn đăng ký Kling AI từng bước](/blog/cach-dang-ky-kling-ai)."
- "So sánh chi tiết hơn giữa Kling 2.6 và 3.0 tại [bài viết chuyên sâu](/blog/kling-2-6-vs-kling-3-0)."
- Đặt internal link trong flow tự nhiên, không dồn hết vào cuối bài

## 11. Prompt Mẫu Trong Bài — Quy Tắc Vàng

Prompt mẫu là phần được copy-paste nhiều nhất. Viết đúng = reader quay lại.

**Format chuẩn:**
- Viết prompt bằng **tiếng Anh** (AI models xử lý tiếng Anh tốt hơn)
- In nghiêng trong dấu *...*
- Kèm giải thích tiếng Việt ngay dưới, từng phần

**Ví dụ tốt:**
> *"Close-up of a bubble tea cup, condensation drops sliding down the glass, straw slowly being pulled up, soft café background, warm afternoon light, shallow depth of field."*
>
> Phân tích: `Close-up` = góc cận, `condensation drops` = giọt nước đọng (chi tiết nhỏ tạo realism), `shallow depth of field` = xóa phông nhẹ.

**Các keyword "ma thuật" đã test hiệu quả:**
- Camera: `cinematic`, `slow dolly`, `push in`, `aerial descending`
- Ánh sáng: `golden hour`, `warm afternoon light`, `soft studio lighting`
- Chất lượng: `film grain`, `natural skin texture`, `shot on Canon 5D`
- Style: `product photography`, `lifestyle mockup`, `minimalist`
- Tránh: `4K`, `ultra HD`, `masterpiece` (không thực sự cải thiện output)

## 12. Domain & URL — Bẫy Đã Gặp

Các lỗi domain/URL cần check định kỳ:

| Sai | Đúng | Lý do |
|-----|------|-------|
| klingai.com | kling.ai | Kling đã migrate domain (2025) |
| tramsangtao.com/blog/xyz | /blog/[slug] | Verify slug tồn tại trước khi link |
| Link đến pricing page cũ | tramsangtao.com/pricing | Pricing page hay thay đổi, check link sống |
| sora.com | openai.com/sora | Sora không có domain riêng |

**Quy tắc URL:**
- Mỗi khi nhắc đến tool bên ngoài, **verify URL bằng cách mở thử** trước khi viết
- Nếu tool thay đổi domain → grep toàn bộ drafts để sửa hàng loạt: `grep -rl "domain_cu" drafts/`
- Internal link dùng relative path (`/blog/slug`) thay vì absolute (`https://tramsangtao.com/blog/slug`)

## 13. Anti-Truncation — Tránh Bài Bị Cụt

Qua 26 bài, có 3 bài bị truncated (file kết thúc giữa chừng). Nguyên nhân: AI generate nội dung quá dài, bị cắt khi save.

**Checklist sau khi viết bài:**
- [ ] File kết thúc bằng section hoàn chỉnh (CTA hoặc Kết luận)
- [ ] Dòng cuối cùng không bị cắt giữa chừng (không kết thúc bằng "đ", "và", "nhưng"...)
- [ ] Section cuối có ít nhất 2-3 câu hoàn chỉnh
- [ ] Mở file, scroll xuống cuối cùng để verify bằng mắt

**Nếu phát hiện bài bị cụt:**
1. Xác định section cuối đang viết dở
2. Hoàn thành section đó
3. Thêm Case Study + Pro-Tips nếu chưa có
4. Thêm CTA/Kết luận

## 14. Cập Nhật Giá & Model Mới

AI tools thay đổi rất nhanh. Cứ 2-4 tuần nên review lại:

**Check list cập nhật:**
- [ ] Kling có version mới không? (hiện tại: 2.5, 2.6, 3.0)
- [ ] Veo có update không? (hiện tại: Veo 3)
- [ ] Sora có mở rộng access không? (hiện tại: Plus $20/tháng)
- [ ] Giá tramsangtao có thay đổi không?
- [ ] Có tool mới nào đáng viết bài không?
- [ ] Domain nào đã thay đổi? (dùng `grep -rl` để tìm)

**Model đang có trên tramsangtao (tính đến 04/2026):**
- Video: Kling 2.5, Kling 2.6, Kling 3.0, Veo 3, Seedance 1.0
- Ảnh: FLUX, Nano Banana Pro, Stable Diffusion
- Đặc biệt: Virtual Try-On (Nano Banana), Image-to-Video (Kling)

