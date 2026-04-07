#!/usr/bin/env python3
import os, re, sys, unicodedata, subprocess
from pathlib import Path
from datetime import datetime

def load_env(env_path: Path):
    if not env_path.exists():
        return
    for line in env_path.read_text(encoding='utf-8').splitlines():
        line=line.strip()
        if not line or line.startswith('#') or '=' not in line:
            continue
        k,v = line.split('=',1)
        k=k.strip(); v=v.strip().strip('"').strip("'")
        os.environ.setdefault(k, v)

def slugify_vi(s: str, max_len: int = 60) -> str:
    s = s.strip().lower()
    s = unicodedata.normalize('NFKD', s)
    s = ''.join(ch for ch in s if not unicodedata.combining(ch))
    s = re.sub(r'[^a-z0-9\s-]', ' ', s)
    s = re.sub(r'\s+', '-', s)
    s = re.sub(r'-{2,}', '-', s).strip('-')
    return s[:max_len] or 'untitled'

def read_keywords(path: Path) -> list[str]:
    kws=[]
    for line in path.read_text(encoding='utf-8').splitlines():
        line=line.strip()
        if not line or line.startswith('#'):
            continue
        kws.append(line)
    return kws

def existing_slugs(drafts_dir: Path) -> set[str]:
    if not drafts_dir.exists():
        return set()
    return {p.name for p in drafts_dir.iterdir() if p.is_dir()}

def now_str():
    return datetime.now().strftime('%Y-%m-%d %H:%M')

def append_log(log_path: Path, text: str):
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open('a', encoding='utf-8') as f:
        f.write(text)
        if not text.endswith('\n'):
            f.write('\n')

def run_one(keyword: str) -> tuple[bool, str, str]:
    """Return (ok, slug_or_empty, err_or_empty)."""
    cmd = [sys.executable, 'generate_blog_post.py', keyword, '--mode', 'brave', '--no-publish']
    p = subprocess.run(cmd, cwd=str(Path(__file__).parent), capture_output=True, text=True)
    out = (p.stdout or '') + (p.stderr or '')
    if p.returncode != 0:
        return False, '', out.strip()[-500:]
    m = re.search(r"Done \(saved\): drafts/([^/]+)/index\.md", out)
    slug = m.group(1) if m else slugify_vi(keyword)
    return True, slug, ''

def main():
    base = Path(__file__).parent
    load_env(base/'.env')
    kw_path = base/'queue'/'keywords.txt'
    drafts_dir = base/'drafts'
    log_path = base/'gen_log.txt'

    kws = read_keywords(kw_path)
    slugs = existing_slugs(drafts_dir)
    ready=[]
    for kw in kws:
        if slugify_vi(kw) in slugs:
            continue
        ready.append(kw)

    total_ok=0
    errors=[]

    batch_size=5
    batches=[ready[i:i+batch_size] for i in range(0, len(ready), batch_size)]
    for bi, batch in enumerate(batches, 1):
        append_log(log_path, f"[BATCH {bi}] {now_str()}")
        for kw in batch:
            ok, slug, err = run_one(kw)
            if ok:
                total_ok += 1
                slugs.add(slug)
                append_log(log_path, f"  ✅ {kw} → drafts/{slug}/")
            else:
                errors.append((kw, err))
                append_log(log_path, f"  ❌ {kw} → ERROR: {err.replace(chr(10),' | ')[:300]}")
        append_log(log_path, "")

    append_log(log_path, f"[SUMMARY] {now_str()}")
    append_log(log_path, f"  Success: {total_ok}")
    append_log(log_path, f"  Errors: {len(errors)}")
    if errors:
        append_log(log_path, "  Error list:")
        for kw, err in errors:
            append_log(log_path, f"    - {kw}: {err.replace(chr(10),' | ')[:300]}")

if __name__ == '__main__':
    main()
