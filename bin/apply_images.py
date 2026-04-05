import os
import glob
import shutil
import re
import json
import requests
from pathlib import Path

brain_dir = Path("C:/Users/leduc/.gemini/antigravity/brain/fb4a12b8-8a7e-4c62-9a6a-2ead628f7b2c")
drafts_dir = Path("e:/seo-blog/drafts")

# Find all media in brain
media_files = []
for ext in ["*.png", "*.jpg", "*.webp"]:
    media_files.extend(brain_dir.glob(ext))

def find_media(keyword: str):
    # Returns first media file that contains keyword in its name
    for m in media_files:
        if keyword.lower() in m.name.lower():
            return m
    return None

# Map slug keywords to lists of artifacts to use.
# First item will be used as cover.png (if available)
# Subsequent items will be inserted into the markdown body
mapping = {
    "kling-2-5": ["kling_brand", "kling_screenshot"],
    "kling-2-6-vs-kling-3-0-7-diem": ["kling_specs_table", "cover_kling_compare"],
    "kling-3-0": ["kling_brand", "kling_specs_table"],
    "kling-ai-co-mien-phi": ["tramsangtao_credits_pricing", "tramsangtao_pricing"],
    "kling-ai-gia-bao-nhieu": ["tramsangtao_pricing", "tramsangtao_credits_pricing"],
    "kling-ai-vs-veo-3": ["cover_kling_compare", "cover_veo3_review"],
    "kling-vs-sora": ["cover_kling_compare", "cover_so_sanh"],
    "kling-ai-la-gi": ["kling_screenshot", "kling_brand", "kling_homepage"],
    "kling-ai-so-voi": ["cover_kling_compare"],
    "review-kling-ai": ["kling_review_cover", "capture_kling_website"],
    "cach-dang-ky-kling": ["kling_homepage"],
    "huong-dan-dung-kling": ["kling_review_cover", "kling_usecase"],
    
    "veo-3-la-gi": ["cover_veo3_review", "close_browser_veo3"],
    
    "tao-anh-ai-mien-phi": ["cover_image_ai", "product_photo_ai", "prompt_structure_image"],
    "flux-vs-stable-diffusion": ["cover_compare_clean", "capture_flux_ui"],
    
    "cach-dung-ai-tao-video-tiktok": ["tiktok_ai_content", "thumbnail_motion", "thumb_bot_dance"],
    "cach-tao-video-ngan": ["cover_seedance", "seedance_character", "seedance_jimeng"],
    
    "6-app-tao-video-ai": ["cover_so_sanh_video", "homepage_ui"],
    "top-7-tool-tao-video": ["cover_so_sanh_video", "media__"],
    "cach-dung-sora": ["sora", "cover_so_sanh"],
    "sora-2-la-gi": ["sora", "cover_so_sanh"],
    
    "cach-tao-video-ai-tu-anh": ["cover_video_from_photo", "so_sanh_before_after", "before_after_video"],
    
    "lam-video-ai-khong-can-lo-mat": ["affiliate_no_face", "kol_ai_avatar", "kol_podcast"],
    "lam-video-ai-tu-dong": ["chaining_workflow", "character_sheet"],
    "tao-video-ai-khong-can-quay": ["cover_video_dai", "luu_y_video_anh"],
    "tao-video-ai-huong-dan-toan-dien": ["cover_video_dai", "kling_specs_table", "cover_so_sanh_video", "cover_image_ai"],
}

generated_map = {
    "cach-dang-ky-kling": "kling_registration_concept",
    "tiktok": "tiktok_ai_viral_concept",
    "6-app-tao-video": "top_video_ai_apps",
    "cach-dung-sora": "sora_ai_concept",
    "cach-tao-video-ai-tu-anh": "photo_to_video_magic",
}

youtube_mappings_file = Path("e:/seo-blog/bin/youtube_mappings.json")
youtube_search_results = {}
if youtube_mappings_file.exists():
    youtube_search_results = json.loads(youtube_mappings_file.read_text(encoding="utf-8"))

def get_youtube_iframe(yt_id: str):
    iframe = f'<iframe width="100%" class="aspect-video mt-4 mb-8 rounded-lg shadow-lg" src="https://www.youtube.com/embed/{yt_id}" frameborder="0" allowfullscreen></iframe>'
    return iframe

def fetch_youtube_thumbnail(yt_id: str, out_path: Path):
    url = f"https://img.youtube.com/vi/{yt_id}/maxresdefault.jpg"
    r = requests.get(url)
    if r.status_code == 404:
        # Fallback to hqdefault
        url = f"https://img.youtube.com/vi/{yt_id}/hqdefault.jpg"
        r = requests.get(url)
    
    if r.status_code == 200:
        out_path.write_bytes(r.content)
        return True
    return False

def insert_inline_images(content: str, images: list, yt_iframe: str):
    """Inserts markdown image tags randomly under different H2 headings"""
    lines = content.split('\n')
    new_lines = []
    img_idx = 0
    iframe_inserted = False
    for line in lines:
        new_lines.append(line)
        if line.startswith("## "):
            if not iframe_inserted:
                new_lines.append(f"\n{yt_iframe}\n")
                iframe_inserted = True
            elif img_idx < len(images):
                # Insert an image right after subsequent H2
                img_name = images[img_idx]
                new_lines.append(f"\n![Minh họa {img_idx}](./{img_name})\n")
                img_idx += 1
    
    if not iframe_inserted:
        new_lines.append(f"\n{yt_iframe}\n")

    # If there are still images uninserted, append to the end
    while img_idx < len(images):
        img_name = images[img_idx]
        new_lines.append(f"\n![Minh họa {img_idx}](./{img_name})\n")
        img_idx += 1
        
    return "\n".join(new_lines)

for draft in [d for d in drafts_dir.iterdir() if d.is_dir() and d.name != "archive"]:
    if draft.name == ".gitkeep":
        continue
        
    slug = draft.name
    index_md = draft / "index.md"
    if not index_md.exists():
        continue
        
    # Fetch dynamic Youtube IDs and thumbnails
    yt_ids = youtube_search_results.get(slug, [])
    if not yt_ids:
        print(f"[{slug}] No YouTube data found, skipping new media.")
        continue
        
    main_yt_id = yt_ids[0]
    
    # Setup Cover from the first YouTube thumbnail
    cover_img_name = "cover.jpg"
    out_cover = draft / cover_img_name
    
    # We remove old cover.png if it exists so there's no confusion
    if (draft / "cover.png").exists():
        (draft / "cover.png").unlink()
    if (draft / "cover.webp").exists():
        (draft / "cover.webp").unlink()

    if not out_cover.exists():
        fetch_youtube_thumbnail(main_yt_id, out_cover)
    print(f"[{slug}] Cover: {cover_img_name}")
    
    # Inline images from remaining youtube thumbnails
    inline_images = []
    
    # Check if there is a generated AI image for this draft
    matched_gen_keys = [k for k in generated_map.keys() if k in slug]
    if matched_gen_keys:
        gen_kw = generated_map[matched_gen_keys[0]]
        m = find_media(gen_kw)
        if m:
            inline_images.append(m.name)
            shutil.copy2(m, draft / m.name)
            
    for v_id in yt_ids[1:]:
        img_name = f"thumb_{v_id}.jpg"
        out_path = draft / img_name
        if not out_path.exists():
            if fetch_youtube_thumbnail(v_id, out_path):
                inline_images.append(img_name)
        else:
            inline_images.append(img_name)
            
        if len(inline_images) >= 4:
            break

    if inline_images:
        content = index_md.read_text(encoding="utf-8")
        
        # Strip existing image and iframe tags
        content = re.sub(r'\n!\[Minh họa.*?\]\(.*?\)\n', '', content)
        content = re.sub(r'\n<iframe.*?</iframe>\n', '', content)

        yt_iframe = get_youtube_iframe(main_yt_id)
        
        import random
        random.shuffle(inline_images)
        
        new_content = insert_inline_images(content, inline_images, yt_iframe)
        index_md.write_text(new_content, encoding="utf-8")
    print(f"[{slug}] Finished processing.")
