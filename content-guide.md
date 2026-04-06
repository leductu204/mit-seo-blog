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

### 🚨 Quy Tắc Chống Trùng Lặp Ảnh Cross-Post (Rút từ Incident 04/2026):

**Bối cảnh:** Trong chiến dịch 26 bài Master Guide, hơn 15 bài bị dùng chung cùng 1 ảnh cover YouTube thumbnail và cùng 1 bộ screenshot UI → Google Image Search coi đây là near-duplicate content, giảm khả năng index ảnh và ảnh hưởng tiêu cực đến SEO.

**Nguyên tắc vàng: MỖI BÀI VIẾT PHẢI CÓ BỘ ẢNH RIÊNG BIỆT 100%.**

**Quy tắc cụ thể:**

1. **Cover Image — KHÔNG BAO GIỜ trùng giữa 2 bài.**
   - Mỗi bài phải có ảnh cover duy nhất, tạo riêng cho chủ đề đó.
   - Nếu dùng YouTube thumbnail làm cover → mỗi bài phải dùng thumbnail từ video KHÁC nhau.
   - Nếu dùng AI-generated cover → prompt phải khác nhau rõ rệt (khác composition, khác subject, khác màu chủ đạo).

2. **Ảnh Inline (UI screenshot, product demo) — Giới hạn tái sử dụng tối đa 1 ảnh/3 bài.**
   - Ảnh screenshot giao diện Trạm Sáng Tạo có thể dùng lại nếu context phù hợp, nhưng KHÔNG quá 1 lần dùng trong mỗi 3 bài liền kề.
   - Ưu tiên crop/highlight vùng khác nhau của cùng UI nếu cần dùng lại (VD: bài A crop thanh sidebar, bài B crop khu vực chính).

3. **Ảnh AI-Generated — Mỗi ảnh chỉ dùng cho ĐÚNG 1 bài.**
   - Không bao giờ copy ảnh AI từ thư mục bài A sang bài B.
   - Nếu 2 bài cùng topic (VD: Kling review + Kling tutorial), vẫn phải gen 2 ảnh riêng với prompt khác nhau.

4. **YouTube Thumbnails — Ánh xạ 1:1 giữa video và bài.**
   - Mỗi bài chỉ dùng thumbnail của video liên quan trực tiếp đến bài đó.
   - KHÔNG dùng thumbnail của video "tổng hợp" cho tất cả bài trong cùng series.

### Quy Trình Tìm/Tạo Ảnh Cho Mỗi Bài Viết Mới:

**Bước 1 — Kiểm tra kho ảnh hiện có:**
```bash
# Liệt kê TẤT CẢ ảnh đang dùng trong toàn bộ drafts
python -c "
import os, re, glob, collections
refs = collections.Counter()
for f in glob.glob('drafts/*/index.md'):
    with open(f, 'r', encoding='utf-8') as fh:
        for m in re.findall(r'!\[[^\]]*\]\(\.?/?([^)]+)\)', fh.read()):
            if not m.startswith('http'):
                refs[m] += 1
for name, count in refs.most_common():
    if count > 1:
        print(f'⚠ TRÙNG {count}x: {name}')
"
```

**Bước 2 — Xác định loại ảnh cần cho bài mới:**

| Slot | Nguồn ưu tiên | Fallback |
| --- | --- | --- |
| Cover | YouTube thumbnail riêng cho bài | AI-generated cover (prompt unique) |
| Screenshot UI | Chụp trực tiếp tramsangtao.com vùng liên quan | Crop vùng khác từ screenshot chung |
| Ảnh minh họa concept | Tải từ Unsplash/Pexels (free, commercial license) | AI-generated (Clean & Minimalist) |
| Ảnh output/showcase | Tạo video/ảnh thật trên platform rồi screenshot | AI-generated showcase (`result_*.jpg`) |
| Ảnh so sánh | Ghép 2-4 screenshot side-by-side | Infographic đơn giản bằng design tool |

**Bước 3 — Tạo ảnh AI (nếu cần):**

Khi dùng tool `generate_image` hoặc API tạo ảnh, PHẢI tuân thủ:

- **Prompt phải chứa ít nhất 1 yếu tố unique** liên quan trực tiếp đến bài viết. VD:
  - ✅ Bài về Kling → prompt chứa "video editing timeline with Vietnamese interface"
  - ✅ Bài về Veo 3 → prompt chứa "Google AI studio with landscape preview"
  - ❌ Cả 2 bài cùng dùng prompt "clean desk with laptop showing AI app" → trùng!

- **Sau khi gen xong, đặt tên file theo pattern:**
  - Cover: `cover.jpg` (unique per folder)
  - AI concept: `{topic_keyword}_concept.jpg` (VD: `kling_pricing_concept.jpg`)
  - Showcase: `result_{loai_output}.jpg` (VD: `result_fashion_tiktok.jpg`)

- **Luôn compress ngay sau khi gen:** AI tool thường output PNG 2-5MB. Resize về 800px width, save JPEG quality 85 → dưới 200KB.

**Bước 4 — Audit trước khi commit:**
```bash
# Chạy dedup check trước mỗi lần import
python -c "
import os, hashlib, glob
hashes = {}
for img in glob.glob('drafts/*/*.jpg') + glob.glob('drafts/*/*.png'):
    h = hashlib.md5(open(img,'rb').read()).hexdigest()
    if h in hashes:
        print(f'⚠ DUPLICATE FILE: {img} == {hashes[h]}')
    else:
        hashes[h] = img
print(f'Checked {len(hashes)} unique images')
"
```
Nếu audit phát hiện duplicate → phải thay thế 1 trong 2 bằng ảnh mới trước khi chạy `import_blog.py`.

### Nguồn Ảnh Miễn Phí Khuyến Nghị (Commercial License):

| Nguồn | Loại ảnh | Lưu ý |
| --- | --- | --- |
| **Unsplash** | Lifestyle, workspace, tech | Miễn phí thương mại, không cần credit |
| **Pexels** | Tương tự Unsplash | Miễn phí, search tiếng Anh cho kết quả tốt hơn |
| **YouTube Thumbnails** | Screenshot video demo | Chỉ dùng thumbnail từ video official hoặc thuộc kênh mình |
| **Trạm Sáng Tạo Platform** | Screenshot giao diện thực | Chụp trực tiếp, crop vùng liên quan, blur thông tin user |
| **AI Generation** | Concept, abstract, infographic | Dùng `generate_image` tool — tuân thủ checklist phía trên |

> **⛔ KHÔNG dùng:** Google Image Search random, Pinterest, ảnh có watermark, ảnh từ blog đối thủ (vi phạm copyright + Google phạt duplicate).

### Kỹ Thuật Tối Ưu (Technical SEO):
- **Luôn resize/compress ảnh:** width dao động 600-800px. Nén Save for Web (JPEG/WebP) thay vì ảnh PNG AI > 2MB khổng lồ! Trọng lượng ảnh ép < 200KB.
- **Tên file thân thiện:** Tên file chứa keyword theo chuẩn slug `ten-tool-tao-video.jpg`. Thay thế hoàn toàn tên rác kiểu `image_001.png`.
- **Alt text:** Ảnh luôn có Alt text đúng ngữ nghĩa của đoạn văn, thay thế cho từ khóa nhồi nhét.

### ⚠️ Quy Tắc Embed Ảnh Trong Markdown (Rút từ Incident 04/2026):

**Format chuẩn duy nhất:**
```markdown
![Alt text mô tả nội dung ảnh](./ten-file.jpg)
*Caption mô tả — nhấn mạnh USP hoặc pain point.*
```

**Quy tắc bắt buộc:**
1. **Mọi ảnh reference phải tồn tại trong thư mục draft.** Trước khi commit, chạy audit script kiểm tra broken refs. Import script (`import_blog.py`) sẽ log `⚠ Image not found` nếu ảnh thiếu → ảnh bị mất trên production.
2. **Không bao giờ reference ảnh chưa tải về.** Nếu cần thumbnail YouTube, tải về local trước (`thumb_{videoId}.jpg`), không dùng URL trực tiếp `img.youtube.com` trong markdown vì import script sẽ upload lên R2 CDN.
3. **Mỗi ảnh trong bài phải unique.** Không dùng cùng 1 file ảnh cho 2 vị trí khác nhau trong cùng bài (gây confuse cho reader và lãng phí bandwidth).
4. **Tên file không chứa ký tự đặc biệt.** Chỉ dùng `a-z`, `0-9`, `_`, `-`. Tránh dấu cách, dấu tiếng Việt trong tên file.

### YouTube Thumbnail Management:

Khi bài viết reference video YouTube (dạng click-to-play), thumbnail phải được tải về local:

```python
# Tải thumbnail YouTube về thư mục draft
import urllib.request
video_id = "VIDEO_ID"
url = f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg"
urllib.request.urlretrieve(url, f"./thumb_{video_id}.jpg")
```

**Lưu ý:**
- Dùng `hqdefault.jpg` (480x360) — nhẹ, đủ chất lượng cho blog.
- `maxresdefault.jpg` (1280x720) nặng hơn nhưng sắc nét hơn — chỉ dùng cho cover.
- Luôn kiểm tra file size > 1KB sau khi tải (YouTube trả placeholder rỗng cho video không tồn tại).

### Showcase Image (Ảnh Output/Kết Quả):

Mỗi bài viết hướng dẫn/review **nên có 1 ảnh showcase** ở phần đầu (sau H2 đầu tiên hoặc cuối intro) để demo kết quả thực tế mà AI tool tạo ra. Quy tắc:

- **Tên file bắt đầu bằng `result_`** để phân biệt với ảnh hướng dẫn: `result_cinematic_scene.jpg`, `result_product_video.jpg`.
- **Alt text mô tả output cụ thể**, không generic: ✅ `"Phong cảnh Việt Nam qua AI — Veo 3 tạo chất lượng cinematic chuẩn phim"` — ❌ `"AI generated image"`.
- **Không dùng chung 1 ảnh showcase cho nhiều bài.** Mỗi bài cần ảnh showcase riêng để tránh duplicate content signal từ Google Image Search.
- Nếu không có ảnh output thực tế, dùng `generate_image` tool tạo ảnh minh họa theo phong cách Clean & Minimalist (xem checklist ở trên).

### Encoding Safety (QUAN TRỌNG):

File `.md` trong `drafts/` **BẮT BUỘC phải là UTF-8 (no BOM)**. Các lỗi encoding thường gặp:

| Triệu chứng | Nguyên nhân | Fix |
|---|---|---|
| `CÃ¡ch DÃ¹ng` thay vì `Cách Dùng` | Double-encoded UTF-8 (UTF-8 bytes được encode lại thành UTF-8) | `pip install ftfy` rồi `ftfy.fix_text(content)` |
| `C?ch D?ng` | File saved as ASCII/Latin-1 | Mở bằng editor, Save As → UTF-8 |
| Tiêu đề hiển thị đúng local nhưng sai trên server | CRLF vs LF line ending conflict | `newline='\n'` khi write file bằng Python |

**Phòng ngừa:** Khi viết script Python xử lý batch file `.md`, LUÔN dùng:
```python
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()
# ... process ...
with open(path, 'w', encoding='utf-8', newline='\n') as f:
    f.write(content)
```

**KHÔNG BAO GIỜ** dùng regex replace trên byte stream hoặc `os.system()` để thao tác nội dung file — dễ gây mất newline, vỡ encoding.

### Import Pipeline (`import_blog.py`):

```bash
# Import mới (skip bài đã tồn tại)
python import_blog.py drafts

# Force update tất cả (ghi đè bài đã import — dùng khi sửa lỗi encoding/ảnh)
python import_blog.py drafts --force

# Import 1 bài cụ thể
python import_blog.py drafts/ten-bai-viet
```

**Checklist trước khi chạy import:**
- [ ] `ADMIN_TOKEN` trong `.env` còn hạn (login admin panel lấy token mới nếu hết)
- [ ] Chạy encoding audit: `python -c "import ftfy; ..."` để fix mojibake
- [ ] Chạy image audit: kiểm tra 0 broken refs trước deploy
- [ ] Ảnh đã compress < 200KB (script sẽ upload tất cả ảnh lên R2 CDN)

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

