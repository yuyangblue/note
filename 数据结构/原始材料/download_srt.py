# -*- coding: utf-8 -*-
import json, urllib.request, os, re, time

base = r'D:\29469\Documents\notes\数据结构\原始材料'
srt_map = json.load(open(os.path.join(base, 'srt_map.json'), encoding='utf-8'))
outdir = os.path.join(base, '字幕')
os.makedirs(outdir, exist_ok=True)

titles = {}
for line in open(os.path.join(base, '视频清单.tsv'), encoding='utf-8'):
    parts = line.rstrip('\n').split('\t')
    if len(parts) == 2:
        titles[parts[0]] = parts[1]

def clean(name):
    name = re.sub(r'[\\/:*?"<>|]', '_', name)
    return name.strip()

ok, fail = 0, []
for i, (cid, info) in enumerate(srt_map.items(), 1):
    srt_url = info.get('srt', '')
    if not srt_url:
        fail.append((cid, 'no-srt-url'))
        continue
    title = titles.get(cid, cid)
    fname = clean('%03d_%s.srt' % (i, title))
    fpath = os.path.join(outdir, fname)
    if os.path.exists(fpath) and os.path.getsize(fpath) > 100:
        ok += 1
        continue
    try:
        req = urllib.request.Request(srt_url, headers={'User-Agent': 'Mozilla/5.0'})
        data = urllib.request.urlopen(req, timeout=30).read()
        if len(data) < 100:
            fail.append((cid, 'tiny'))
            continue
        with open(fpath, 'wb') as f:
            f.write(data)
        ok += 1
    except Exception as e:
        fail.append((cid, str(e)[:60]))
    if i % 30 == 0:
        print('...%d/%d ok=%d' % (i, len(srt_map), ok))
    time.sleep(0.2)

print('下载完成 ok=', ok, 'fail=', len(fail))
for cid, why in fail[:15]:
    print(' FAIL', cid, why)
