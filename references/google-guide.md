# SEO Guide Summary — Google Search Starter Guide (Vi)

## 1. SEO là gì?
- SEO = tối ưu hoá để công cụ tìm kiếm hiểu nội dung + giúp người dùng tìm thấy site
- Không có bí quyết rank #1 tự động — chỉ có best practices
- Thay đổi SEO có thể mất vài tuần → vài tháng mới thấy hiệu quả

## 2. Google hoạt động như nào?
- Google dùng **crawler (bot)** tự động khám phá web qua links
- Khi tìm thấy trang → **index** vào cơ sở dữ liệu → **rank** khi user search
- Không cần làm gì nếu site đã public — Google tự tìm thấy theo thời gian
- Submit **sitemap.xml** giúp Google index nhanh hơn
- Dùng `site:domain.com` trên Google để kiểm tra đã index chưa

## 3. Cấu trúc URL
- URL cần mô tả nội dung: `/blog/huong-dan-tao-video-kling` ✅
- Tránh URL ngẫu nhiên: `/post/2f6a8c7d` ❌
- Nhóm bài cùng chủ đề vào folder: `/blog/ai-video/`, `/blog/huong-dan/`
- Tránh **duplicate content** — mỗi nội dung chỉ 1 URL duy nhất
- Dùng `canonical` tag hoặc redirect 301 nếu có URL trùng

## 4. On-page SEO
- **Title tag**: chứa keyword chính, ≤60 ký tự, unique mỗi trang
- **Meta description**: tóm tắt hấp dẫn, chứa keyword, ≤160 ký tự
- **Heading H1**: duy nhất/trang, chứa keyword chính
- **H2/H3**: keyword phụ, chia nhỏ nội dung dễ đọc
- **Content**: độc đáo, hữu ích, không copy, cập nhật thường xuyên
- **Internal links**: link tới các trang liên quan trong site
- **Keyword**: tự nhiên trong bài, không nhồi nhét

## 5. Technical SEO
- **Sitemap.xml**: liệt kê tất cả URL → submit lên Google Search Console
- **Robots.txt**: kiểm soát crawler được phép crawl trang nào
- **Canonical URL**: tránh duplicate content
- **HTTPS**: bắt buộc, Google ưu tiên HTTPS
- **Mobile-friendly**: responsive design
- **Page speed**: load nhanh, Google dùng Core Web Vitals
- **Structured Data (JSON-LD)**: giúp Google hiểu context (Article, Product, FAQ...)
- **CSS/JS không bị block**: Google cần render được đầy đủ

## 6. Content Quality
- Nội dung **độc đáo**, không copy từ nguồn khác
- **Hữu ích cho người đọc** — không chỉ viết cho SEO
- **Cập nhật thường xuyên** — bài cũ review lại, xoá nếu outdated
- Dự đoán **search intent**: user muốn gì khi search keyword đó?
- Tránh quảng cáo/popup gây gián đoạn đọc nội dung

## 7. Link Building (Off-page)
- Google tìm trang mới **qua links từ trang khác**
- **Backlinks** từ site uy tín = tín hiệu quality
- **Internal links** trong site giúp Google crawl và hiểu cấu trúc
- Quảng bá nội dung để có backlink tự nhiên (social, community, guest post)

## 8. Tools cần biết
- **Google Search Console**: monitor index, errors, click data
- **URL Inspection Tool**: xem Google thấy trang mày như nào
- **sitemap.xml + robots.txt**: submit/manage

## 9. Áp dụng cho tramsangtao.com (blog)

### Quick wins:
- Mỗi bài cần: title (keyword), meta desc, H1 unique, slug `/blog/keyword-slug`
- `sitemap.ts` trong Next.js → auto thêm slug mới → submit Search Console
- `generateMetadata()` per slug → dynamic SEO tags
- JSON-LD Article schema per post
- Internal links: bài → `/pricing`, `/tools`, bài liên quan

### Blog content strategy:
- Keywords: "tạo video AI", "Kling 2.5 review", "Freepik Pikaso", "hướng dẫn AI video VN"
- Bài dài 1500-2000 words ngon hơn cho SEO
- FAQ section ở cuối bài (người dùng hay hỏi gì về chủ đề đó)
- CTA cuối bài: link về trang tạo ảnh/video của tramsangtao
