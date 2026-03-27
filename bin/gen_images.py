#!/usr/bin/env python3
"""
Generate blog cover/step images via tramsangtao API.
Usage:
    python bin/gen_images.py                              # Process all rows in queue/images.csv
    python bin/gen_images.py --slug my-post --prompt "..." --type cover
    python bin/gen_images.py --auto-from-csv --slug my-post  # Only rows matching slug
"""
import os, sys, csv, asyncio, aiohttp, argparse, time
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DRAFTS_DIR = PROJECT_ROOT / "drafts"
POSTS_DIR = PROJECT_ROOT / "posts"
QUEUE_DIR = PROJECT_ROOT / "queue"

API_BASE = os.getenv("TST_API_BASE", "https://api.tramsangtao.com/v1")
API_KEY = os.getenv("TST_API_KEY", "")
DEFAULT_MODEL = "nano-banana-pro"
POLL_INTERVAL = 3  # seconds
MAX_POLL = 120  # max seconds to wait


async def generate_image(prompt: str, model: str, session: aiohttp.ClientSession) -> str:
    """Submit image generation job and poll until done. Returns CDN URL."""
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    payload = {"prompt": prompt, "model": model}

    # Submit job
    async with session.post(f"{API_BASE}/image/generate", headers=headers, json=payload) as resp:
        if resp.status != 200:
            text = await resp.text()
            raise Exception(f"Generate failed ({resp.status}): {text}")
        data = await resp.json()
        job_id = data["job_id"]
        print(f"    Job {job_id} submitted (cost: {data.get('cost', '?')} credits)")

    # Poll for result
    elapsed = 0
    while elapsed < MAX_POLL:
        await asyncio.sleep(POLL_INTERVAL)
        elapsed += POLL_INTERVAL
        async with session.get(f"{API_BASE}/jobs/{job_id}", headers=headers) as resp:
            data = await resp.json()
            status = data.get("status", "unknown")
            if status == "completed":
                return data["result"]
            elif status in ("failed", "error"):
                raise Exception(f"Job {job_id} failed: {data}")
            # Still processing...

    raise Exception(f"Job {job_id} timed out after {MAX_POLL}s")


async def download_image(url: str, save_path: Path, session: aiohttp.ClientSession):
    """Download image from CDN URL and save locally."""
    async with session.get(url) as resp:
        if resp.status == 200:
            save_path.parent.mkdir(parents=True, exist_ok=True)
            save_path.write_bytes(await resp.read())
            print(f"    ✅ Saved: {save_path}")
        else:
            print(f"    ❌ Download failed: {resp.status}")


async def process_row(row: dict, session: aiohttp.ClientSession):
    """Process one CSV row: generate + download."""
    slug = row["slug"]
    prompt = row["prompt"]
    img_type = row.get("type", "cover")
    model = row.get("model", DEFAULT_MODEL)

    # Determine save location (drafts first, then posts)
    draft_dir = DRAFTS_DIR / slug
    post_dir = POSTS_DIR / slug
    save_dir = draft_dir if draft_dir.exists() else post_dir
    save_dir.mkdir(parents=True, exist_ok=True)

    save_path = save_dir / f"{img_type}.webp"
    if save_path.exists():
        print(f"  ⏭️  Skip {slug}/{img_type}.webp (already exists)")
        return

    print(f"  🎨 Generating {slug}/{img_type} with {model}...")
    try:
        url = await generate_image(prompt, model, session)
        await download_image(url, save_path, session)
    except Exception as e:
        print(f"  ❌ Error for {slug}/{img_type}: {e}")


async def process_csv(csv_path: Path, filter_slug: str = None):
    """Process all rows in images.csv."""
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    if filter_slug:
        rows = [r for r in rows if r["slug"] == filter_slug]

    if not rows:
        print("No rows to process.")
        return

    print(f"Processing {len(rows)} image(s)...\n")
    async with aiohttp.ClientSession() as session:
        for row in rows:
            await process_row(row, session)

    print(f"\nDone!")


async def single_generate(slug: str, prompt: str, img_type: str, model: str):
    """Generate a single image from CLI args."""
    async with aiohttp.ClientSession() as session:
        row = {"slug": slug, "prompt": prompt, "type": img_type, "model": model}
        await process_row(row, session)


def main():
    parser = argparse.ArgumentParser(description="Generate blog images via tramsangtao API")
    parser.add_argument("--slug", type=str, help="Post slug")
    parser.add_argument("--prompt", type=str, help="Image prompt")
    parser.add_argument("--type", type=str, default="cover", help="Image type: cover, step, etc.")
    parser.add_argument("--model", type=str, default=DEFAULT_MODEL, help=f"Model (default: {DEFAULT_MODEL})")
    parser.add_argument("--csv", type=str, default="queue/images.csv", help="CSV file path")
    parser.add_argument("--auto-from-csv", action="store_true", help="Process images.csv (optionally filter by --slug)")
    args = parser.parse_args()

    if not API_KEY:
        print("❌ TST_API_KEY not set. Export it first:")
        print('   export TST_API_KEY="your-api-key"')
        sys.exit(1)

    if args.prompt and args.slug:
        # Single image mode
        asyncio.run(single_generate(args.slug, args.prompt, args.type, args.model))
    else:
        # CSV batch mode
        csv_path = Path(args.csv)
        if not csv_path.is_absolute():
            csv_path = PROJECT_ROOT / csv_path
        asyncio.run(process_csv(csv_path, filter_slug=args.slug))


if __name__ == "__main__":
    main()
