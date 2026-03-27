# Content Guide — Trạm Sáng Tạo SEO Blog

Rút từ kinh nghiệm viết bài #1 "Video AI Nhảy TikTok" và #2 "Kling AI Review". Dùng file này làm checklist mỗi khi viết/review bài mới.

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

## 3. Ảnh — Ít Nhưng Chất

### Nguyên tắc:
- **3-4 ảnh/bài** là đủ cho bài how-to ngắn. **4-6 ảnh** OK cho bài review/tutorial dài (nếu mỗi ảnh minh họa 1 bước/feature cụ thể)
- Ưu tiên ảnh thật (screenshot UI, thumbnail YouTube) hơn ảnh AI-generated
- Ảnh AI-generated phải **realistic, người giống thật** — không ảo/cyberpunk/neon
- Ảnh trùng (cover = YouTube thumbnail) → OK, tăng brand consistency
- **Luôn resize ảnh cho hợp lý:** width 600-800px (dùng PIL/Pillow). Ảnh gốc lớn > 1000px phải resize xuống

### Loại ảnh nên dùng:
1. **Cover/thumbnail:** Dùng thumbnail YouTube thật nếu có, hoặc ảnh từ site/user cung cấp
2. **Screenshot UI:** Chụp thật từ tramsangtao.com — menu, settings, model selector, kết quả
3. **Screenshot đối thủ:** Lấy từ website chính thức (vào trang chụp/browser screenshot)
4. **YouTube embed:** Thumbnail click-to-play, không auto-embed video

### Loại ảnh KHÔNG nên dùng:
- Ảnh AI kiểu holographic/neon/fantasy → người Việt không chuộng
- Infographic AI-generated → nội dung thường trùng với text, thừa
- Logo SVG link ngoài → hay bị lỗi, chụp screenshot thay thế

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
