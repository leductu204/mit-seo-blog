# 🧠 SEO Blog — Memory & Tips

> Bài học thực chiến rút ra từ chiến dịch 26 bài Master Guide (04/2026).
> File này là quick reference — chi tiết đầy đủ xem `content-guide.md`.

---

## 1. Image Dedup — Vấn Đề Nghiêm Trọng Nhất

### Thực trạng phát hiện (06/04/2026):
- **218 ảnh tổng cộng, chỉ 143 unique → 75 file trùng lặp**
- **21 cross-post references** (cùng tên file dùng trong nhiều bài)
- Thủ phạm nặng nhất: `capture_kol_ai_ui.jpg` xuất hiện trong **10 bài**, `tst_model_select.png` trong **9 bài**

### Nguyên nhân gốc:
- Khi gen batch 26 bài, AI copy cùng 1 set ảnh (screenshot UI, YouTube thumbnail) sang nhiều folder draft
- Không có hệ thống tracking ảnh nào giữa các bài
- Tên file generic (`capture_kling_website.jpg`) khiến khó phát hiện trùng bằng mắt

### Cách phòng tránh:
```bash
# Chạy dedup TRƯỚC MỖI LẦN import
python generate_blog_post.py --dedup

# Nếu phát hiện trùng → thay bằng ảnh mới unique trước khi deploy
```

### Hàm check programmatic (dùng khi build auto-fetch):
```python
from generate_blog_post import check_image_duplicate

# Trước khi save ảnh mới vào draft folder:
dup = check_image_duplicate("drafts/new-post/image.jpg")
if dup:
    print(f"⚠ Trùng với: {dup} — cần ảnh khác!")
```

---

## 2. Encoding — Double UTF-8 Mojibake

### Triệu chứng:
`Cách Dùng` hiển thị thành `CÃ¡ch DÃ¹ng` trên production.

### Nguyên nhân:
File `.md` đã là UTF-8, nhưng script Python đọc rồi ghi lại bằng encoding sai → bytes UTF-8 bị encode lại thêm 1 lần nữa.

### Fix nhanh:
```python
import ftfy
content = ftfy.fix_text(broken_content)
```

### Phòng tránh:
```python
# LUÔN dùng pattern này khi đọc/ghi file .md
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()
with open(path, 'w', encoding='utf-8', newline='\n') as f:
    f.write(content)
```

---

## 3. YouTube Thumbnail — Local Only

### Rule:
- **KHÔNG dùng URL trực tiếp** `img.youtube.com` trong markdown
- `import_blog.py` sẽ upload ảnh lên R2 CDN → URL YouTube không được xử lý
- Phải tải thumbnail về local TRƯỚC khi reference

### Download nhanh:
```python
import urllib.request
video_id = "VIDEO_ID"
urllib.request.urlretrieve(
    f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg",
    f"./thumb_{video_id}.jpg"
)
```

### Lưu ý:
- `hqdefault.jpg` (480x360) — nhẹ, đủ dùng cho inline
- `maxresdefault.jpg` (1280x720) — chỉ dùng cho cover
- Kiểm tra file > 1KB (YouTube trả placeholder rỗng cho video không tồn tại)

---

## 4. Import Pipeline Tips

### Commands:
```bash
# Import bình thường (skip bài đã tồn tại)
python import_blog.py drafts

# Force update (ghi đè bài cũ — dùng sau khi fix encoding/ảnh)
python import_blog.py drafts --force
```

### Checklist trước import:
- [ ] `ADMIN_TOKEN` trong `.env` còn hạn
- [ ] `python generate_blog_post.py --dedup` → 0 duplicates
- [ ] Encoding audit: không có mojibake trong tiêu đề/meta
- [ ] Ảnh đã compress < 200KB

### Gotchas:
- Script dùng `PUT` để update khi `--force`, `POST` để tạo mới
- Nếu `401 Unauthorized` → token hết hạn, login admin panel lấy mới
- Ảnh bị `⚠ Image not found` trong log → ảnh thiếu trong folder draft, sẽ mất trên production

---

## 5. AI Image Generation — Anti-Duplicate Rules

### Prompt phải chứa yếu tố unique cho từng bài:
- ✅ Bài Kling → `"video editing timeline with Vietnamese text overlay"`
- ✅ Bài Veo 3 → `"Google AI studio showing landscape cinema preview"`
- ❌ Cả 2 dùng `"clean desk with laptop showing AI app"` → TRÙNG

### Naming convention:
```
cover.jpg           — ảnh bìa (1 per folder, unique content)
result_*.jpg        — ảnh output/showcase (VD: result_fashion_tiktok.jpg)
{topic}_concept.jpg — ảnh minh họa AI (VD: kling_pricing_concept.jpg)
thumb_{videoId}.jpg — YouTube thumbnail tải về local
```

### Style bắt buộc:
- **Clean & Minimalist** — pastel, soft morning light, lifestyle workspace
- **CẤM:** neon, cyberpunk, holographic, sci-fi effects
- Resize 800px width, JPEG quality 85, < 200KB

---

## 6. Content Guide Quick Ref

| Rule | Chi tiết |
| --- | --- |
| Ảnh/bài (Pillar) | 8 ảnh + 2 video |
| Nhịp media | 400 từ = 1 cụm media |
| Cover | Unique per bài, không bao giờ trùng |
| AI-gen ảnh | Mỗi ảnh chỉ cho 1 bài duy nhất |
| Video embed | Click-to-play thumbnail > iframe |
| Alt text | Mô tả cụ thể + keyword, không generic |
| File encoding | UTF-8 no BOM, LF line endings |

---

## 7. Tool Commands Cheat Sheet

```bash
# Gen bài mới
python generate_blog_post.py "keyword" --mode brave --format how-to --no-publish

# Gen batch
python generate_blog_post.py --batch keywords.txt --no-publish

# Dedup audit
python generate_blog_post.py --dedup

# Import to production
python import_blog.py drafts
python import_blog.py drafts --force

# Fix encoding
python -c "import ftfy, glob; [open(f,'w',encoding='utf-8').write(ftfy.fix_text(open(f,encoding='utf-8').read())) for f in glob.glob('drafts/*/index.md')]"
```

---

*Last updated: 2026-04-06 — sau chiến dịch remediation 26 bài Master Guide.*
