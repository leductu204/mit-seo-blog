"""
Import blog posts from seo-blog/drafts/ folder → admin API.

Usage:
  cd backend
  python scripts/import_blog.py E:/seo-blog/drafts
  python scripts/import_blog.py E:/seo-blog/drafts/video-ai-nhay-tiktok

What it does:
  1. Scans each subfolder for index.md
  2. Parses YAML frontmatter (title, slug, tags, meta_*, etc.)
  3. Uploads images (cover.png + inline images) to R2 via admin API
  4. Replaces relative image paths (./cover.png) with R2 URLs in content
  5. Converts markdown → sends as content_raw + content_format=markdown
  6. Creates post via POST /api/admin/blog/posts
  7. Skips slugs that already exist

Requires:
  - Backend running (admin API)
  - Admin credentials (ADMIN_TOKEN env or hardcoded below)
"""

import os
import sys
import re
import json
import glob
import requests
from dotenv import load_dotenv

load_dotenv()

# ── Config ────────────────────────────────────────────────

# API_BASE = os.environ.get("API_BASE", "http://localhost:8000")
API_BASE = os.environ.get("API_BASE", "https://api.tramsangtao.com")
ADMIN_TOKEN = os.environ.get("ADMIN_TOKEN", "")

# Interactive: prompt for token if not set
if not ADMIN_TOKEN:
    ADMIN_TOKEN = input("Admin token (from admin panel login): ").strip()

# Pillar → category mapping
PILLAR_TO_CATEGORY = {
    "1": "tao-video-ai",
    "2": "tao-anh-ai",
    "3": "kiem-tien-online",
    "4": "tiktok",
    "5": "tao-video-ai",
    "how-to": "huong-dan",
    "how-to-gateway": "huong-dan",
    "brand-review": "mo-hinh-ai",
    "comparison-main": "mo-hinh-ai",
}

DEFAULT_CATEGORY = "huong-dan"
DEFAULT_AUTHOR = "Trạm Sáng Tạo"


def parse_frontmatter(content: str) -> tuple:
    """Parse YAML frontmatter from markdown file. Returns (metadata_dict, body_str)."""
    if not content.startswith("---"):
        return {}, content

    end = content.find("---", 3)
    if end == -1:
        return {}, content

    fm_text = content[3:end].strip()
    body = content[end + 3:].strip()

    meta = {}
    for line in fm_text.split("\n"):
        line = line.strip()
        if ":" not in line:
            continue
        key, _, val = line.partition(":")
        key = key.strip()
        val = val.strip().strip('"').strip("'")

        # Parse arrays: ["tag1", "tag2"]
        if val.startswith("[") and val.endswith("]"):
            try:
                val = json.loads(val.replace("'", '"'))
            except json.JSONDecodeError:
                val = [t.strip().strip('"').strip("'") for t in val[1:-1].split(",")]

        meta[key] = val

    return meta, body


def upload_image(filepath: str, session: requests.Session, prefix: str = "") -> str:
    """Upload image to R2 via admin API. Returns URL. prefix used to avoid filename collisions."""
    filename = os.path.basename(filepath)
    if prefix:
        filename = f"{prefix}_{filename}"
    with open(filepath, "rb") as f:
        resp = session.post(
            f"{API_BASE}/api/admin/blog/upload-image",
            files={"file": (filename, f, "image/png")},
        )
    if resp.status_code != 200:
        print(f"  ⚠ Upload failed for {filename}: {resp.status_code} {resp.text[:100]}")
        return ""
    return resp.json().get("url", "")


def replace_image_refs(content: str, folder: str, session: requests.Session, slug: str = "") -> tuple:
    """Find ./image.png refs in markdown, upload to R2, replace URLs. Returns (new_content, cover_url)."""
    cover_url = ""

    # Find all image references: ![alt](./file.png) or ![alt](file.png)
    img_pattern = re.compile(r'!\[([^\]]*)\]\(\.?/?([^)]+)\)')
    uploaded_cache = {}

    def replace_match(match):
        nonlocal cover_url
        alt = match.group(1)
        rel_path = match.group(2)

        # Skip external URLs
        if rel_path.startswith("http"):
            return match.group(0)

        filepath = os.path.join(folder, rel_path)
        if not os.path.exists(filepath):
            print(f"  ⚠ Image not found: {rel_path}")
            return match.group(0)

        if filepath in uploaded_cache:
            url = uploaded_cache[filepath]
        else:
            url = upload_image(filepath, session, prefix=slug)
            uploaded_cache[filepath] = url
            if url:
                print(f"  ✓ Uploaded: {rel_path} → {url[:60]}...")

        if url:
            return f"![{alt}]({url})"
        return match.group(0)

    new_content = img_pattern.sub(replace_match, content)

    # Upload cover.png separately if exists
    cover_path = os.path.join(folder, "cover.png")
    if not os.path.exists(cover_path):
        cover_path = os.path.join(folder, "cover.jpg")
    if os.path.exists(cover_path):
        if cover_path in uploaded_cache:
            cover_url = uploaded_cache[cover_path]
        else:
            cover_url = upload_image(cover_path, session, prefix=slug)

    return new_content, cover_url


def get_existing_posts(session: requests.Session) -> dict:
    """Fetch all existing posts from admin API. Returns {slug: id} map."""
    try:
        resp = session.get(f"{API_BASE}/api/admin/blog/posts")
        if resp.status_code == 200:
            return {p["slug"]: p["id"] for p in resp.json().get("posts", [])}
    except Exception as e:
        print(f"⚠ Failed to fetch existing posts: {e}")
    return {}


def import_folder(drafts_dir: str, force: bool = False):
    if not ADMIN_TOKEN:
        print("ERROR: Set ADMIN_TOKEN env variable or edit the script.")
        print("  Get token: login to admin panel, check localStorage/cookie for admin token")
        sys.exit(1)

    session = requests.Session()
    session.headers["Authorization"] = f"Bearer {ADMIN_TOKEN}"

    existing_posts = get_existing_posts(session)
    print(f"Found {len(existing_posts)} existing posts in DB")
    if force:
        print("⚡ FORCE mode: existing posts will be UPDATED\n")
    else:
        print()

    # Support both: single post folder (has index.md) or parent folder with subfolders
    single_index = os.path.join(drafts_dir, "index.md")
    if os.path.exists(single_index):
        folders = [single_index]
    else:
        folders = sorted(glob.glob(os.path.join(drafts_dir, "*/index.md")))
    if not folders:
        print(f"No index.md found in {drafts_dir}/ or {drafts_dir}/*/")
        return

    imported = 0
    updated = 0
    skipped = 0

    for index_path in folders:
        folder = os.path.dirname(index_path)
        folder_name = os.path.basename(folder)

        with open(index_path, "r", encoding="utf-8") as f:
            raw = f.read()

        meta, body = parse_frontmatter(raw)
        slug = meta.get("slug", folder_name)
        title = meta.get("title", folder_name.replace("-", " ").title())

        is_update = slug in existing_posts
        if is_update and not force:
            print(f"⏭ Skip (exists): {slug}")
            skipped += 1
            continue

        action = "🔄 Updating" if is_update else "📝 Importing"
        print(f"{action}: {slug}")

        # Upload images and replace refs
        body, cover_url = replace_image_refs(body, folder, session, slug=slug)

        # Map pillar → category
        pillar = str(meta.get("pillar", ""))
        category = PILLAR_TO_CATEGORY.get(pillar, DEFAULT_CATEGORY)

        # Parse tags
        tags = meta.get("tags", [])
        if isinstance(tags, str):
            tags = [t.strip() for t in tags.split(",")]

        # Estimate read time (~200 words/min Vietnamese)
        word_count = len(body.split())
        read_time = max(3, round(word_count / 200))

        # Build post data
        post_data = {
            "title": title,
            "slug": slug,
            "category": category,
            "content_raw": body,
            "content_format": "markdown",
            "excerpt": meta.get("meta_description", "")[:500] or None,
            "cover_image": cover_url or None,
            "author_name": meta.get("author", DEFAULT_AUTHOR),
            "read_time": read_time,
            "is_published": 1 if meta.get("status") == "published" else 0,
            "meta_title": meta.get("meta_title"),
            "meta_description": meta.get("meta_description"),
            "tags": tags if tags else None,
        }

        # Remove None values
        post_data = {k: v for k, v in post_data.items() if v is not None}

        if is_update:
            post_id = existing_posts[slug]
            resp = session.put(
                f"{API_BASE}/api/admin/blog/posts/{post_id}",
                json=post_data,
            )
            if resp.status_code == 200:
                print(f"  ✓ Updated: id={post_id}, category={category}")
                updated += 1
            else:
                print(f"  ✗ Update failed: {resp.status_code} {resp.text[:200]}")
        else:
            resp = session.post(
                f"{API_BASE}/api/admin/blog/posts",
                json=post_data,
            )
            if resp.status_code == 200:
                post_id = resp.json().get("id", "?")
                print(f"  ✓ Created: id={post_id}, category={category}, read_time={read_time}min")
                imported += 1
            else:
                print(f"  ✗ Failed: {resp.status_code} {resp.text[:200]}")

    print(f"\n{'='*40}")
    print(f"Done: {imported} imported, {updated} updated, {skipped} skipped")


if __name__ == "__main__":
    force = "--force" in sys.argv
    args = [a for a in sys.argv[1:] if not a.startswith("--")]

    if args:
        path = args[0]
    else:
        path = input("Folder path (single post or parent folder): ").strip()
        if not path:
            print("No path provided.")
            sys.exit(1)

    if not os.path.isdir(path):
        print(f"ERROR: '{path}' is not a valid directory.")
        sys.exit(1)

    import_folder(path, force=force)
