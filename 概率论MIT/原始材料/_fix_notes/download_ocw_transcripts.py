# -*- coding: utf-8 -*-
"""抓取 OCW 6.041SC 全部 Lecture 官方逐字稿 PDF"""
import urllib.request
import re
import os
import sys
import time

BASE = 'https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013'
OUT = r'D:\29469\Documents\notes\概率论MIT\原始材料\OCW逐字稿'
os.makedirs(OUT, exist_ok=True)

def fetch(url, timeout=40):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    return urllib.request.urlopen(req, timeout=timeout).read()

# 1) 抓 Resource Index，收集所有 lecture 视频资源页链接
idx_html = fetch(BASE + '/pages/resource-index/').decode('utf-8', errors='replace')
links = set(re.findall(r'href="(/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/resources/[^"]*)"', idx_html))
video_pages = sorted(l for l in links if re.search(r'lecture-\d+-video', l))
print('found', len(video_pages), 'lecture video pages')

# 2) 对每个视频页提取 _transcript.pdf 链接
transcripts = {}
for page in video_pages:
    url = 'https://ocw.mit.edu' + page
    try:
        html = fetch(url).decode('utf-8', errors='replace')
    except Exception as e:
        print('FETCH FAIL', page, e)
        continue
    t = re.findall(r'href="([^"]*_transcript\.pdf)"', html)
    if t:
        transcripts[page] = t[0]
        print('  transcript:', t[0])
    else:
        print('  NO transcript on', page)
    time.sleep(0.3)

# 3) 下载全部 transcript
for page, tp in sorted(transcripts.items()):
    name = tp.split('/')[-1]  # e.g. TluTv5V0RmE_transcript.pdf
    dst = os.path.join(OUT, name)
    if os.path.exists(dst) and os.path.getsize(dst) > 1000:
        print('skip existing', name)
        continue
    try:
        data = fetch('https://ocw.mit.edu' + tp)
        with open(dst, 'wb') as f:
            f.write(data)
        print('downloaded', name, len(data), 'bytes')
    except Exception as e:
        print('DL FAIL', tp, e)
    time.sleep(0.3)

print('total transcripts:', len(transcripts))
