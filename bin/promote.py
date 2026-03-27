#!/usr/bin/env python3
"""
Promote a draft post to posts/ after validation.
Usage:
    python bin/promote.py drafts/my-post-slug
    python bin/promote.py my-post-slug          # auto-prepend drafts/
    python bin/promote.py --all                 # promote all ready drafts
"""
import sys, shutil, re, argparse
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DRAFTS_DIR = PROJECT_ROOT / "drafts"
POSTS_DIR = PROJECT_ROOT / "posts"

REQUIRED_FIELDS = ["title", "slug", "meta_title", "meta_description", "tags"]


def parse_frontmatter(md_path: Path) -> dict:
    """Parse YAML-like frontmatter from markdown file."""
    text = md_path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not match:
        return {}

    fm = {}
    for line in match.group(1).split("\n"):
        if ":" in line:
            key, val = line.split(":", 1)
            key = key.strip()
            val = val.strip().strip('"').strip("'")
            fm[key] = val
    return fm


def update_status(md_path: Path, new_status: str):
    """Update status field in frontmatter."""
    text = md_path.read_text(encoding="utf-8")
    text = re.sub(r'^(status:\s*)"?.*"?', f'\\1"{new_status}"', text, flags=re.MULTILINE)
    md_path.write_text(text, encoding="utf-8")


def validate_draft(draft_dir: Path) -> list[str]:
    """Validate a draft is ready for promotion. Returns list of issues."""
    issues = []
    md_path = draft_dir / "index.md"

    if not md_path.exists():
        issues.append(f"Missing index.md in {draft_dir.name}")
        return issues

    fm = parse_frontmatter(md_path)
    for field in REQUIRED_FIELDS:
        if field not in fm or not fm[field] or fm[field] in ("", "[]"):
            issues.append(f"Missing or empty field: {field}")

    # Check for cover image
    cover_files = list(draft_dir.glob("cover.*"))
    if not cover_files:
        issues.append("Missing cover image (cover.webp/jpg/png)")

    # Check content length
    text = md_path.read_text(encoding="utf-8")
    content = re.sub(r"^---\n.*?\n---\n?", "", text, flags=re.DOTALL)
    word_count = len(content.split())
    if word_count < 500:
        issues.append(f"Content too short: {word_count} words (min 500)")

    return issues


def promote(draft_dir: Path, force: bool = False) -> bool:
    """Promote draft to posts/."""
    slug = draft_dir.name
    dest = POSTS_DIR / slug

    print(f"📝 Validating: {slug}")
    issues = validate_draft(draft_dir)

    if issues and not force:
        print(f"  ❌ Cannot promote. Issues:")
        for i in issues:
            print(f"     - {i}")
        return False

    if issues and force:
        print(f"  ⚠️  Promoting with warnings:")
        for i in issues:
            print(f"     - {i}")

    # Update status
    md_path = draft_dir / "index.md"
    update_status(md_path, "ready")

    # Move
    if dest.exists():
        print(f"  ⚠️  Overwriting existing post: {dest}")
        shutil.rmtree(dest)

    shutil.move(str(draft_dir), str(dest))
    print(f"  ✅ Promoted: drafts/{slug} → posts/{slug}")
    return True


def main():
    parser = argparse.ArgumentParser(description="Promote draft posts to posts/")
    parser.add_argument("path", nargs="?", help="Draft folder path or slug name")
    parser.add_argument("--all", action="store_true", help="Promote all valid drafts")
    parser.add_argument("--force", action="store_true", help="Promote even with warnings")
    parser.add_argument("--check", action="store_true", help="Validate only, don't move")
    args = parser.parse_args()

    if args.all:
        drafts = [d for d in DRAFTS_DIR.iterdir() if d.is_dir() and d.name != ".gitkeep"]
        if not drafts:
            print("No drafts found.")
            return
        print(f"Found {len(drafts)} drafts\n")
        promoted = 0
        for d in sorted(drafts):
            if args.check:
                issues = validate_draft(d)
                status = "✅ Ready" if not issues else f"❌ {len(issues)} issue(s)"
                print(f"  {d.name}: {status}")
            else:
                if promote(d, args.force):
                    promoted += 1
            print()
        if not args.check:
            print(f"Promoted {promoted}/{len(drafts)} drafts")
    elif args.path:
        draft_path = Path(args.path)
        if not draft_path.is_absolute():
            # Try as slug name first
            if (DRAFTS_DIR / args.path).exists():
                draft_path = DRAFTS_DIR / args.path
            else:
                draft_path = PROJECT_ROOT / args.path

        if not draft_path.exists():
            print(f"❌ Not found: {draft_path}")
            sys.exit(1)

        if args.check:
            issues = validate_draft(draft_path)
            if issues:
                print(f"Issues for {draft_path.name}:")
                for i in issues:
                    print(f"  - {i}")
            else:
                print(f"✅ {draft_path.name} is ready to promote")
        else:
            promote(draft_path, args.force)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
