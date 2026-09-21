# -*- coding: utf-8 -*-
"""建立 Lecture N ↔ video_id 映射，重命名 transcript PDF 并转文本"""
import urllib.request
import re
import os
import sys
import time

BASE = 'https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013'
OUT = r'D:\29469\Documents\notes\概率论MIT\原始材料\OCW逐字稿'

def fetch(url, timeout=40):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    return urllib.request.urlopen(req, timeout=timeout).read().decode('utf-8', errors='replace')

# 1) Resource Index: (Lecture N) -> slug
idx = fetch(BASE + '/pages/resource-index/')
pairs = re.findall(r'href="(/resources/(lecture-\d+-video[^"]*))"[^>]*>\s*(?:<[^>]+>)*\s*(Lecture \d+[^<]*)', idx)
slug_to_lec = {}
for full, slug, lec in pairs:
    m = re.match(r'Lecture (\d+)', lec.strip())
    if m:
        slug_to_lec.setdefault(int(m.group(1)), set()).add('/' + full)
print('slugs found:', {k: sorted(v) for k, v in sorted(slug_to_lec.items())})

# 2) 每个 slug -> video_id (从页面 _transcript.pdf 提取)
lec_to_vid = {}
for n, slugs in sorted(slug_to_lec.items()):
    vid = None
    for s in slugs:
        try:
            html = fetch('https://ocw.mit.edu' + s)
            t = re.findall(r'href="([^"]*/([A-Za-z0-9_-]+)_transcript\.pdf)"', html)
            if t:
                vid = t[0][1]
                break
        except Exception as e:
            print('fail', s, e)
        time.sleep(0.2)
    lec_to_vid[n] = vid
    print('Lecture', n, '->', vid)

# 3) 重命名 + 转文本
try:
    import fitz  # PyMuPDF
    has_fitz = True
except Exception:
    has_fitz = False
print('fitz available:', has_fitz)

renamed = 0
for n, vid in sorted(lec_to_vid.items()):
    if not vid:
        print('Lecture', n, 'NO VIDEO ID - skip')
        continue
    src = os.path.join(OUT, vid + '_transcript.pdf')
    dst = os.path.join(OUT, 'lec%02d_transcript.pdf' % n)
    if os.path.exists(src):
        if not os.path.exists(dst):
            os.replace(src, dst)
        renamed += 1
    if has_fitz:
        try:
            doc = fitz.open(dst)
            text = '\n'.join(p.get_text() for p in doc)
            txt_dst = os.path.join(OUT, 'lec%02d_transcript.txt' % n)
            with open(txt_dst, 'w', encoding='utf-8') as f:
                f.write(text)
            print('txt', n, len(text))
        except Exception as e:
            print('txt fail', n, e)
    else:
        print('no fitz; skip txt', n)

print('renamed:', renamed)
