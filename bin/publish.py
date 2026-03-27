#!/usr/bin/env python3
"""
Publish a post to the blog API.
Usage:
    python bin/publish.py posts/my-post-slug
    python bin/publish.py my-post-slug --status published
    python bin/publish.py my-post-slug --dry-run
"""
import os, sys, json, re, asyncio, aiohttp, argparse
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
POSTS_DIR = PROJECT_ROOT / "posts"

# Blog API — endpoint TBD, user will provide later
BLOG_API = os.getenv("BLOG_API", "https://api.tramsangtao.com/v1/blog/posts")
API_KEY = os.getenv("TST_API_KEY", "")
API_BASE = os.getenv("TST_API_BASE", "https://api.tramsangtao.com/v1")

IMAGE_EXTENSIONS = {".webp", ".jpg", ".jpeg", ".png", ".gif", ".avif"}


def parse_frontmatter(md_path: Path) -> tuple[dict, str]:
    """Parse frontmatter and content from markdown file."""
    text = md_path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n?(.*)", text, re.DOTALL)
    if not match:
        return {}, text

    fm = {}
    for line in match.group(1).split("\n"):
        if ":" in line:
            key, val = line.split(":", 1)
            key = key.strip()
            val = val.strip()
            # Parse JSON arrays
            if val.startswith("["):
                try:
                    val = json.loads(val)
                except json.JSONDecodeError:
                    pass
            else:
                val = val.strip('"').strip("'")
            fm[key] = val

    return fm, match.group(2).strip()


async def upload_image(file_path: Path, session: aiohttp.ClientSession) -> str:
    """Upload image to CDN via tramsangtao API. Returns URL."""
    headers = {"Authorization": f"Bearer {API_KEY}"}

    data = aiohttp.FormData()
    data.add_field("file", open(file_path, "rb"), filename=file_path.name,
                   content_type=f"image/{file_path.suffix.lstrip('.')}")

    async with session.post(f"{API_BASE}/files/upload/image", headers=headers, data=data) as resp:
        if resp.status == 200:
            result = await resp.json()
            return result.get("url", "")
        else:
            text = await resp.text()
            print(f"  ⚠️  Upload failed for {file_path.name}: {resp.status} {text}")
            return ""


async def upload_images_and_replace(post_dir: Path, content: str, session: aiohttp.ClientSession) -> tuple[str, dict]:
    """Upload local images and replace markdown refs with CDN URLs."""
    image_map = {}

    for img_file in post_dir.iterdir():
        if img_file.suffix.lower() in IMAGE_EXTENSIONS:
            print(f"  📤 Uploading: {img_file.name}")
            url = await upload_image(img_file, session)
            if url:
                image_map[img_file.name] = url
                # Replace relative refs in content
                content = content.replace(f"./{img_file.name}", url)
                content = content.replace(f"({img_file.name})", f"({url})")

    return content, image_map


async def publish(post_dir: Path, status: str = "draft", dry_run: bool = False):
    """Publish post: upload images → replace refs → POST to API."""
    md_path = post_dir / "index.md"
    if not md_path.exists():
        print(f"❌ No index.md in {post_dir}")
        return

    fm, content = parse_frontmatter(md_path)
    slug = fm.get("slug", post_dir.name)

    print(f"📰 Publishing: {slug} (status: {status})")

    async with aiohttp.ClientSession() as session:
        # Upload images & replace refs
        content, image_map = await upload_images_and_replace(post_dir, content, session)

        # Build payload
        payload = {
            "title": fm.get("title", ""),
            "slug": slug,
            "meta_title": fm.get("meta_title", fm.get("title", "")),
            "meta_description": fm.get("meta_description", ""),
            "description": fm.get("description", ""),
            "tags": fm.get("tags", []),
            "content": content,
            "status": status,
            "cover_image": image_map.get("cover.webp", image_map.get("cover.jpg", "")),
        }

        if dry_run:
            print(f"\n--- DRY RUN ---")
            print(f"Endpoint: POST {BLOG_API}")
            print(f"Payload preview:")
            preview = {k: (v[:100] + "..." if isinstance(v, str) and len(v) > 100 else v)
                      for k, v in payload.items()}
            print(json.dumps(preview, indent=2, ensure_ascii=False))
            print(f"Images uploaded: {len(image_map)}")
            for name, url in image_map.items():
                print(f"  {name} → {url}")
            return

        # POST to blog API
        headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
        async with session.post(BLOG_API, headers=headers, json=payload) as resp:
            if resp.status in (200, 201):
                result = await resp.json()
                print(f"  ✅ Published: /blog/{slug}")
                return result
            else:
                text = await resp.text()
                print(f"  ❌ Publish failed: {resp.status} {text}")
                return None


def main():
    parser = argparse.ArgumentParser(description="Publish blog post to site API")
    parser.add_argument("path", help="Post folder path or slug name")
    parser.add_argument("--status", default="draft", choices=["draft", "published"],
                       help="Publish status (default: draft)")
    parser.add_argument("--dry-run", action="store_true",
                       help="Preview payload without posting")
    args = parser.parse_args()

    post_path = Path(args.path)
    if not post_path.is_absolute():
        if (POSTS_DIR / args.path).exists():
            post_path = POSTS_DIR / args.path
        else:
            post_path = PROJECT_ROOT / args.path

    if not post_path.exists():
        print(f"❌ Not found: {post_path}")
        sys.exit(1)

    if not API_KEY and not args.dry_run:
        print("❌ TST_API_KEY not set. Use --dry-run or export TST_API_KEY")
        sys.exit(1)

    asyncio.run(publish(post_path, args.status, args.dry_run))


if __name__ == "__main__":
    main()
