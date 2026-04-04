---
title: "Làm Video AI Không Lộ Mặt: Từ Script Đến Final Cut Trong 2 Giờ"
slug: "lam-video-ai-khong-lo-mat-tu-script-den-final-cut-trong-2-gio"
meta_title: "Làm Video AI Không Lộ Mặt Trong 2 Giờ | Workflow Thực Tế"
meta_description: "Học cách tạo video AI không lộ mặt đủ tự nhiên cho TikTok, Reels và affiliate content — từ script đến final cut chỉ trong 2 giờ với workflow thực tế."
tags:
  - video AI
  - không lộ mặt
  - affiliate marketing
  - tạo video tự động
  - AI content
status: draft
---

# Làm Video AI Không Lộ Mặt: Từ Script Đến Final Cut Trong 2 Giờ

---

## Intro

Có một câu hỏi mà nhiều người làm affiliate ngại nói thẳng: *"Tôi không muốn lộ mặt, nhưng tôi vẫn cần video có người thật để ra chuyển đổi — làm thế nào?"*

Câu trả lời không phải là dùng avatar hoạt hình trông như clip PowerPoint từ 2015. Cũng không phải thuê người mẫu với ngân sách vài triệu mỗi lần quay.

Bài này sẽ dạy bạn workflow thực tế để tạo video AI không lộ mặt — đủ tự nhiên để đặt lên TikTok, Reels, hoặc landing page mà không bị "lộ đồ AI" ngay 3 giây đầu.

**Bạn sẽ làm được gì sau bài này:**
- Tạo video nhân vật AI có chuyển động tự nhiên, không đơ
- Ghép voiceover hoặc text-on-screen để thay thế giọng nói thật
- Xuất video dùng được cho affiliate content, review sản phẩm, content giáo dục

**Mất bao lâu:** ~2 giờ lần đầu (bao gồm thời gian render). Sau khi quen workflow, khoảng 45 phút/video.

**Cần gì:**
- Tài khoản tramsangtao.com
- Script sẵn (kể cả 1 đoạn ngắn 150-200 chữ)
- Biết dùng Canva hoặc CapCut ở mức cơ bản

---

## Prerequisites — Chuẩn Bị Trước Khi Bắt Đầu

**1. Script trước, hình ảnh sau**
Đây là lỗi phổ biến nhất: mở tool ra tạo ảnh lung tung trước rồi mới nghĩ xem nói gì. Làm ngược lại. Script xong rồi mới tạo visual.

**2. Xác định "nhân vật"**
Không cần đặt tên hay backstory phức tạp. Chỉ cần quyết định:
- Giới tính, độ tuổi ước chừng
- Bối cảnh (trong nhà, ngoài trời, văn phòng, studio)
- Phong cách ăn mặc phù hợp niche của bạn

> Ví dụ: *"Nữ, 25-30 tuổi, mặc áo basic tông trắng/nude, background là góc làm việc gọn gàng"* — đủ rồi.

**3. Cài sẵn CapCut hoặc DaVinci Resolve**
Dùng để ghép video + audio cuối cùng.

**4. Chuẩn bị audio (chọn 1 trong 2):**
- Record giọng chính mình (chỉ giọng, không lộ mặt)
- Dùng text-to-speech như ElevenLabs hoặc FPT.AI nếu không muốn giọng thật

---

## Steps

### Bước 1 — Tạo Ảnh Nhân Vật Gốc Với FLUX hoặc Nano Banana Pro

**Làm gì:**
Vào tramsangtao.com, chọn model tạo ảnh. Nếu cần ảnh portrait người thật trông sắc nét, chọn **Nano Banana Pro**. Nếu cần phong cách linh hoạt hơn (commercial, lifestyle), dùng **FLUX**.

**Prompt mẫu cho Nano Banana Pro:**
```
A young Vietnamese woman, 25-30 years old, sitting at a minimal desk, 
wearing a white linen shirt, natural lighting from window, 
soft smile, looking slightly off-camera, photorealistic, 8k
```

**Tại sao nhìn hơi lệch camera?**
Vì nhân vật nhìn thẳng vào ống kính trông rất "posed" và dễ bị nhận ra là AI. Nhìn hơi lệch (~15 độ) tự nhiên hơn nhiều.

**Tạo 4-6 ảnh khác nhau** với cùng prompt, chọn 1-2 cái ưng nhất. Lưu lại ảnh gốc — bạn sẽ cần nó ở bước sau.

> ⚠️ **Tip tránh lỗi:** Không dùng prompt có quá nhiều yếu tố cùng lúc (ví dụ: vừa muốn outdoor vừa indoor). Model sẽ cho ra kết quả nhập nhằng. Chọn 1 bối cảnh, stick với nó.

---

### Bước 2 — Biến Ảnh Tĩnh Thành Video Chuyển Động Với Kling

**Làm gì:**
Upload ảnh nhân vật vừa tạo vào **Kling 2.5** (ổn định, render nhanh) hoặc **Kling 2.6/3.0** (chuyển động tự nhiên hơn, chi tiết hơn).

**Prompt chuyển động gợi ý:**
```
Person gently nodding, slight shoulder movement, 
natural breathing motion, hair moves slightly, 
maintains eye contact with slight off-camera gaze, 
realistic subtle movement, no sudden gestures
```

**Tại sao không prompt cử chỉ tay mạnh?**
Kling vẫn có thể bị lỗi ở ngón tay khi chuyển động phức tạp. Cử chỉ nhẹ ở phần thân trên an toàn hơn nhiều.

**Settings nên dùng:**
- Duration: 5-8 giây (đủ để loop hoặc cắt ghép)
- Render 2-3 clip với cùng ảnh gốc để có options khi edit

> ⚠️ **Tip tránh lỗi:** Nếu khuôn mặt bị biến dạng sau vài giây, thêm vào prompt: `maintain consistent facial features throughout`. Đây là lỗi phổ biến nhất với video nhân vật AI.

---

### Bước 3 — Tạo B-roll Hỗ Trợ Với Veo3 Hoặc Seedance 2.0

**Làm gì:**
Video chỉ có 1 nhân vật đứng/ngồi nói suốt 60 giây sẽ nhàm. Cần B-roll để cắt xen kẽ.

Dùng **Veo3** (Google) hoặc **Seedance 2.0** để tạo các clip product/lifestyle:

**Ví dụ prompt B-roll cho video review sản phẩm skincare:**
```
Close-up of a white skincare serum bottle on marble surface, 
morning light, slow camera push-in, 
water droplets on bottle, minimal aesthetic
```

**Ví dụ prompt B-roll cho video tài chính/affiliate:**
```
Person's hands typing on laptop, coffee cup beside keyboard, 
cozy home office, warm afternoon light, 
shallow depth of field, 4K cinematic
```

**Tại sao cần B-roll?**
Không phải để "che" AI — mà vì đây là kỹ thuật edit cơ bản. Video review thật của creator triệu follow cũng dùng B-roll. Bạn dùng B-roll AI = tiết kiệm cả ngày quay.

> ⚠️ **Tip tránh lỗi:** Veo3 xử lý ánh sáng và vật thể cứng (chai lọ, thiết bị) rất tốt. Seedance 2.0 cho texture vải và chuyển động tự nhiên của con người ổn hơn. Dùng đúng tool cho đúng cảnh.

---

### Bước 4 — Chuẩn Bị Audio

**Làm gì:**
Đây là bước nhiều người bỏ qua rồi hỏi tại sao video không ra chuyển đổi.

**Option A — Voiceover của chính bạn (khuyên dùng):**
Record theo script, dùng điện thoại + microphone đơn giản. Không cần studio. Xử lý noise bằng Audacity (free) hoặc Adobe Podcast (free, AI-powered).

**Option B — Text-to-speech:**
- FPT.AI: Giọng Việt tự nhiên nhất hiện tại
- ElevenLabs: Tốt cho tiếng Anh hoặc nếu bạn cần clone giọng

**Bước phụ:** Sync audio với video nhân vật
Trong CapCut, kéo clip nhân vật và audio vào timeline. Không cần khớp môi (vì nhân vật không nói trực tiếp) — chỉ cần cảnh nhân vật xuất hiện khi bạn đang nói điểm quan trọng.

> ⚠️ **Tip tránh lỗi:** Nếu dùng TTS, đừng dùng tốc độ mặc định — thường quá nhanh và thiếu pause tự nhiên. Thêm dấu phẩy vào script để tạo nhịp thở.

---

### Bước 5 — Ghép Và Edit Final

**Làm gì:**
Mở CapCut hoặc DaVinci, build timeline theo cấu trúc:

```
[Hook - Nhân vật AI 3-5 giây]
[B-roll + Voiceover nêu vấn đề - 10-15 giây]  
[Nhân vật AI - nói solution - 10-15 giây]
[B-roll sản phẩm/minh họa - 10-15 giây]
[Nhân vật AI - CTA - 5-8 giây]
```

**Thêm text-on-screen:**
Không phải để phụ đề kiểu karaoke — mà để highlight key points. Ví dụ: khi nói *"tiết kiệm 3 giờ mỗi ngày"*, text đó xuất hiện to trên màn hình. Làm tăng retention rõ rệt.

**Color grading đơn giản:**
Trong CapCut, dùng filter "Film" hoặc "Natural" ở 40-50% intensity. Mục tiêu: làm clip B-roll AI và clip nhân vật AI trông có cùng màu sắc tông.

> ⚠️ **Tip tránh lỗi:** Nếu clip nhân vật và B-roll trông khác nhiệt độ màu (một cái vàng ấm, một cái trắng lạnh), người xem sẽ cảm thấy "lạ" dù không biết tại sao. Fix bằng cách kéo White Balance về cùng tông trước khi apply filter.

---

## Kết Quả Mong Đợi

Khi làm đúng, video cuối của bạn sẽ trông như thế này:

- **Nhân vật:** Có chuyển động nhẹ, không đơ cứng, không bị biến dạng mặt
- **Flow:** Không có cảnh nào kéo dài quá 8-10 giây mà không cắt
- **Audio:** Nghe rõ, có nhịp điệu, không bị robotic
- **Tổng thể:** Ai xem lần đầu không confirm ngay "clip này AI 100%" — họ có thể nghĩ là bạn thuê người quay hoặc dùng stock video high-end

Đây không phải bar thấp. Đây chính xác là mức bạn cần để affiliate content hoạt động.

---

## Troubleshooting

### Lỗi 1: Khuôn mặt nhân vật bị biến dạng giữa chừng trong video Kling

**Triệu chứng:** Đầu video trông ổn, cuối video mặt bị nhòe hoặc méo.

**Fix:**
- Dùng clip ngắn hơn (5 giây thay vì 10 giây)
- Thêm vào prompt: `consistent facial features, stable face, no morphing`
- Nếu vẫn lỗi, thử lại với ảnh nguồn có độ phân giải cao hơn và background ít chi tiết hơn

---

### Lỗi 2: B-roll AI trông quá khác biệt so với clip nhân vật

**Triệu chứng:** Video cảm giác bị vá víu, thiếu coherence.

**Fix:**
- Đảm bảo ánh sáng trong tất cả prompt đều dùng cùng mô tả (ví dụ: tất cả đều "natural morning light" hoặc tất cả đều "warm afternoon light")
- Apply cùng 1 LUT hoặc filter trong CapCut cho toàn bộ clip
- Thêm transition đơn giản (J-cut hoặc L-cut) thay vì hard cut

---

### Lỗi 3: Video render xong nhưng motion blur quá nhiều, trông mờ

**Triệu chứng:** Clip nhân vật chuyển động nhưng bị mờ kiểu slow-motion không mong muốn.

**Fix:**
- Khi prompt Kling, tránh dùng từ "slow motion" hoặc "cinematic slow"
- Dùng: `natural speed movement, real-time motion`
- Nếu đã render xong, trong CapCut có thể dùng "Motion deblur" trong phần enhance video

---

## Thử Ngay

Workflow này không yêu cầu bạn học design, học quay phim, hay mua thiết bị. Yêu cầu duy nhất là bạn có script và sẵn sàng iterate 2-3 lần đầu.

**Tất cả model trong bài này — FLUX, Nano Banana Pro, Kling 2.5/2.6/3.0, Veo3, Seedance 2.0 — đều có trên [tramsangtao.com](https://tramsangtao.com).**

Bắt đầu từ Bước 1: tạo ảnh nhân vật. Cả workflow sẽ rõ hơn khi bạn có ảnh trong