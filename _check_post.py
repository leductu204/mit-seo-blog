import os, requests, json
from dotenv import load_dotenv
load_dotenv()

token = os.environ.get('ADMIN_TOKEN','')
s = requests.Session()
s.headers['Authorization'] = f'Bearer {token}'
r = s.get('https://api.tramsangtao.com/api/admin/blog/posts')
posts = r.json().get('posts', [])

lines = []
lines.append(f"S | {'raw':>6s} | {'html':>6s} | slug")
lines.append("-" * 70)

for p in posts:
    pid = p['id']
    r2 = s.get(f'https://api.tramsangtao.com/api/admin/blog/posts/{pid}')
    data = r2.json()
    cr = len(data.get('content_raw', '') or '')
    c = len(data.get('content', '') or '')
    pub = 'P' if p.get('is_published') else 'D'
    lines.append(f"{pub} | {cr:6d} | {c:6d} | {p['slug']}")

with open('_content_report.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

print(f"Checked {len(posts)} posts. Report saved to _content_report.txt")
