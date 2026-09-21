# -*- coding: utf-8 -*-
"""建立 Lecture N ↔ video_id 映射（v2）：直接抓 25 个 lecture 视频页，从页面标题取编号"""
import urllib.request
import re
import os
import time

BASE = 'https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013'
OUT = r'D:\29469\Documents\notes\概率论MIT\原始材料\OCW逐字稿'

def fetch(url, timeout=40):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    return urllib.request.urlopen(req, timeout=timeout).read().decode('utf-8', errors='replace')

idx = fetch(BASE + '/pages/resource-index/')
slugs = sorted(set(re.findall(r'/resources/(lecture-\d+-video[^"/]*)', idx)))
print('slugs:', len(slugs))

lec_to_vid = {}
for slug in slugs:
    url = BASE + '/resources/' + slug + '/'
    try:
        html = fetch(url)
    except Exception as e:
        print('FAIL', slug, e)
        continue
    m = re.search(r'<title>\s*Lecture (\d+)', html, re.I)
    if not m:
        m = re.search(r'Lecture (\d+):', html[:4000])
    n = int(m.group(1)) if m else None
    t = re.findall(r'href="[^"]*/([A-Za-z0-9_-]+)_transcript\.pdf"', html)
    vid = t[0] if t else None
    print(slug, '-> Lecture', n, '->', vid)
    if n is not None:
        lec_to_vid[n] = vid
    time.sleep(0.2)

# 保存映射
with open(os.path.join(OUT, '_lec_map.txt'), 'w', encoding='utf-8') as f:
    for n in sorted(lec_to_vid):
        f.write('%d %s\n' % (n, lec_to_vid[n]))
print('map saved:', len(lec_to_vid))

# 重命名 + 转文本
import fitz  # PyMuPDF
renamed = 0
for n, vid in sorted(lec_to_vid.items()):
    if not vid:
        continue
    src = os.path.join(OUT, vid + '_transcript.pdf')
    dst = os.path.join(OUT, 'lec%02d_transcript.pdf' % n)
    if os.path.exists(src) and not os.path.exists(dst):
        os.replace(src, dst)
        renamed += 1
    try:
        doc = fitz.open(dst)
        text = '\n'.join(p.get_text() for p in doc)
        with open(os.path.join(OUT, 'lec%02d_transcript.txt' % n), 'w', encoding='utf-8') as f:
            f.write(text)
        print('converted lec%02d len=%d' % (n, len(text)))
    except Exception as e:
        print('convert fail', n, e)
print('renamed:', renamed)
