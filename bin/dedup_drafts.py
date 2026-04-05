#!/usr/bin/env python3
"""
dedup_drafts.py — Deduplicate draft posts by keyword cluster.

Scoring (higher = better):
  1. Word count      — proportional, normalized to 0-40 pts
  2. Frontmatter     — title(10) + meta_description(10) + tags(10) = 30 pts
  3. Header count    — H2/H3 headings, normalized to 0-30 pts

Usage:
  python bin/dedup_drafts.py          # dry-run, show report
  python bin/dedup_drafts.py --apply  # delete losers
  python bin/dedup_drafts.py --apply --verbose  # show all details
"""

import argparse
import re
import shutil
import sys
from collections import defaultdict
from pathlib import Path

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
DRAFTS_DIR = Path(__file__).parent.parent / "drafts"

# Keyword → canonical cluster label.
# Groups are defined by shared root "keyword tokens".
# We auto-cluster by extracting slug tokens (see cluster_key()).
# Manual overrides can be added here if needed.
PROTECTED_SLUGS: set[str] = set()  # never delete these slugs
SKIP_DIRS: set[str] = {"STATUS.md", ".gitkeep"}

# Scoring weights
SCORE_WORDS_MAX = 40    # points for word count (scaled)
SCORE_FM_MAX = 30       # points for frontmatter
SCORE_HEADERS_MAX = 30  # points for H2/H3 count


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def read_file(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except Exception:
        return ""


def parse_frontmatter(content: str) -> dict:
    """Extract YAML frontmatter fields as raw strings."""
    fm: dict = {}
    match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return fm
    block = match.group(1)
    for line in block.splitlines():
        m = re.match(r"^\s*(\w+)\s*:\s*(.*)", line)
        if m:
            key, val = m.group(1).strip(), m.group(2).strip()
            if key not in fm:
                fm[key] = val
    return fm


def strip_frontmatter(content: str) -> str:
    return re.sub(r"^---\s*\n.*?\n---\s*\n", "", content, flags=re.DOTALL)


def word_count(content: str) -> int:
    body = strip_frontmatter(content)
    # Remove markdown syntax noise
    body = re.sub(r"!\[.*?\]\(.*?\)", "", body)
    body = re.sub(r"\[.*?\]\(.*?\)", "", body)
    body = re.sub(r"```.*?```", "", body, flags=re.DOTALL)
    body = re.sub(r"`[^`]+`", "", body)
    body = re.sub(r"[#*_>|~\-]+", " ", body)
    return len(body.split())


def header_count(content: str) -> int:
    body = strip_frontmatter(content)
    return len(re.findall(r"^#{2,3}\s+\S", body, re.MULTILINE))


def fm_score(fm: dict) -> int:
    """Return 0-30 based on frontmatter completeness."""
    score = 0
    if fm.get("title", "").strip():
        score += 10
    desc = fm.get("meta_description", "").strip()
    if desc and len(desc) > 40:
        score += 10
    tags_raw = fm.get("tags", "").strip()
    if tags_raw and tags_raw not in ("-", "[]", ""):
        score += 10
    return score


def score_post(content: str, all_words: list[int]) -> dict:
    """Compute composite score for a post."""
    fm = parse_frontmatter(content)
    words = word_count(content)
    headers = header_count(content)

    # Normalize word count: scale relative to max in cluster group
    max_words = max(all_words) if all_words else 1
    word_pts = round((words / max_words) * SCORE_WORDS_MAX) if max_words else 0

    # Header score: cap at 10 headers = full marks
    header_pts = min(headers, 10) / 10 * SCORE_HEADERS_MAX
    header_pts = round(header_pts)

    fm_pts = fm_score(fm)
    total = word_pts + fm_pts + header_pts

    return {
        "words": words,
        "headers": headers,
        "fm_pts": fm_pts,
        "word_pts": word_pts,
        "header_pts": header_pts,
        "total": total,
    }


# ---------------------------------------------------------------------------
# Clustering — brand-centric approach
# ---------------------------------------------------------------------------

# Brands and platforms — anchor of the cluster key
BRANDS = {
    "kling", "veo", "sora", "flux", "seedance", "higgsfield", "vidu",
    "stable", "diffusion", "midjourney",
    "tiktok", "youtube", "reels", "shorts",
}

# Intent/topic bigrams: replace BEFORE splitting so both halves collapse
# Keep ONLY bigrams that define a truly distinct content intent.
# Removed: so-sanh, khong-can, tu-dong (too generic/cause false splits)
SLUG_BIGRAMS = {
    "la-gi":    "lagi",      # what-is — informational
    "mien-phi": "mienPhi",   # free plan
    "gia-bao":  "giaBao",    # pricing
    "dang-ky":  "dangKy",    # register tutorial
    "lo-mat":   "loMat",     # no-face / anonymous video
    "tu-anh":   "tuAnh",     # from-image (image→video)
    "so-voi":   "soVoi",     # X vs other tools (comparison)
    "so-sanh":  "soSanh",    # compare/comparison
}

# Non-brand tokens that can narrow a cluster key
TOPIC_TOKENS = {
    # intent bigram outputs
    "lagi", "mienPhi", "giaBao", "dangKy", "loMat", "tuAnh",
    "soVoi", "soSanh",
    # content format
    "ngan",     # short-form video
    "vs",       # comparison slug starting with vs
}


def cluster_key(slug: str) -> str:
    """
    Build a cluster key that collapses near-duplicate slugs.

    Rules:
    1. Collapse known compound bigrams first (la-gi → lagi, etc.)
    2. Walk tokens in order — collect brands and topic tokens.
    3. Version digits are ONLY kept when they appear immediately after
       a brand name (e.g. veo-3, kling-2-5) — prevents '1-tuan', '2-gio'
       from polluting keys.
    4. 'review' is treated as a brand-level differentiator ONLY when it
       starts the slug (position 0 in original slug).
    5. Sort collected tokens, cap at 4, join as key.
    6. Fallback to full slug when no brand/topic signal found.
    """
    # Step 1: collapse bigrams
    processed = slug
    for bigram, token in SLUG_BIGRAMS.items():
        processed = processed.replace(bigram, token)

    parts = processed.split("-")
    orig_parts = slug.split("-")  # original for positional checks

    kept = set()

    # Step 2: 'review' only significant when it opens the slug
    if orig_parts and orig_parts[0] == "review":
        kept.add("review")

    # Step 3: walk tokens
    for i, t in enumerate(parts):
        if t in BRANDS:
            kept.add(t)
            # Brand-adjacent version digits only (up to 2 digits after brand)
            for offset in (1, 2):
                if i + offset < len(parts) and parts[i + offset].isdigit():
                    kept.add(parts[i + offset])
                else:
                    break  # stop at first non-digit
        elif t in TOPIC_TOKENS:
            kept.add(t)

    # Step 4: build key
    key_tokens = sorted(kept)[:4]
    if not key_tokens:
        return slug  # truly unique slug, treated as singleton

    return " ".join(key_tokens)





def find_draft_posts() -> list[Path]:
    posts = []
    for d in sorted(DRAFTS_DIR.iterdir()):
        if not d.is_dir():
            continue
        if d.name in SKIP_DIRS:
            continue
        idx = d / "index.md"
        if idx.exists():
            posts.append(idx)
    return posts


# ---------------------------------------------------------------------------
# Main logic
# ---------------------------------------------------------------------------

def build_clusters(posts: list[Path]) -> dict[str, list[Path]]:
    clusters: dict[str, list[Path]] = defaultdict(list)
    for p in posts:
        slug = p.parent.name
        key = cluster_key(slug)
        clusters[key].append(p)
    return clusters


def analyse(clusters: dict[str, list[Path]], verbose: bool = False):
    """
    Returns:
      winners: dict[cluster_key → Path]
      losers:  list[Path]
      report:  list[str]
    """
    winners: dict[str, Path] = {}
    losers: list[Path] = []
    report: list[str] = []

    solo_count = 0
    dedup_count = 0

    for key, paths in sorted(clusters.items()):
        if len(paths) == 1:
            solo_count += 1
            winners[key] = paths[0]
            if verbose:
                report.append(f"  [solo] {paths[0].parent.name}")
            continue

        dedup_count += 1
        # Read all and compute word counts first (needed for normalisation)
        contents = [read_file(p) for p in paths]
        all_words = [word_count(c) for c in contents]

        scored = []
        for p, c in zip(paths, contents):
            s = score_post(c, all_words)
            s["path"] = p
            scored.append(s)

        scored.sort(key=lambda x: x["total"], reverse=True)
        winner = scored[0]
        cluster_losers = scored[1:]

        winners[key] = winner["path"]
        losers.extend(l["path"] for l in cluster_losers)

        report.append(
            f"\n[CLUSTER] [{key[:60]}] ({len(paths)} posts)"
        )
        for i, s in enumerate(scored):
            marker = ">> KEEP  " if i == 0 else "   DELETE"
            report.append(
                f"   {marker}  {s['path'].parent.name}\n"
                f"          score={s['total']:>3}  "
                f"words={s['words']:>4}({s['word_pts']}pts)  "
                f"fm={s['fm_pts']}pts  "
                f"h2/h3={s['headers']}({s['header_pts']}pts)"
            )

    total_drafts = sum(len(v) for v in clusters.values())
    report.insert(0, (
        f"\n{'='*60}\n"
        f"  DEDUP REPORT\n"
        f"  Total drafts : {total_drafts}\n"
        f"  Solo clusters: {solo_count}\n"
        f"  Dedup groups : {dedup_count}\n"
        f"  Will DELETE  : {len(losers)}\n"
        f"{'='*60}"
    ))

    return winners, losers, report


def delete_loser(path: Path, dry_run: bool = True) -> str:
    folder = path.parent
    if folder.name in PROTECTED_SLUGS:
        return f"  [PROTECTED] skip: {folder.name}"
    if dry_run:
        return f"  [dry-run] would delete: {folder}"
    shutil.rmtree(folder)
    return f"  [DELETED]: {folder}"


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Dedup draft blog posts.")
    parser.add_argument("--apply", action="store_true",
                        help="Actually delete loser folders (default: dry-run)")
    parser.add_argument("--verbose", action="store_true",
                        help="Show solo clusters too")
    args = parser.parse_args()

    # Force UTF-8 output so Vietnamese slugs don't crash on Windows cp1252
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    posts = find_draft_posts()
    if not posts:
        print("No draft posts found.")
        sys.exit(0)

    clusters = build_clusters(posts)
    winners, losers, report = analyse(clusters, verbose=args.verbose)

    print("\n".join(report))

    if not losers:
        print("\nOK: Nothing to delete -- all clusters are unique.")
        return

    print(f"\n{'-'*60}")
    print(f"Action: {'APPLY (deleting)' if args.apply else 'DRY-RUN (no changes)'}")
    print(f"{'-'*60}")

    for p in losers:
        msg = delete_loser(p, dry_run=not args.apply)
        print(msg)

    if not args.apply:
        print(
            f"\nTIP: Run with --apply to actually delete {len(losers)} folder(s)."
        )
    else:
        print(f"\nDone. Deleted {len(losers)} loser folder(s).")


if __name__ == "__main__":
    main()
