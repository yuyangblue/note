# -*- coding: utf-8 -*-
import os, re, glob

base = r'D:\29469\Documents\notes\数据结构\原始材料'
subdir = os.path.join(base, '字幕')
outdir = os.path.join(base, '字幕_修正')
os.makedirs(outdir, exist_ok=True)

def clean(name):
    name = re.sub(r'[\\/:*?"<>|]', '_', name)
    return name.strip()

# 读清单（顺序 = 课程顺序）
order = []  # (cid, title)
for line in open(os.path.join(base, '视频清单.tsv'), encoding='utf-8'):
    parts = line.rstrip('\n').split('\t')
    if len(parts) == 2:
        order.append((parts[0], parts[1]))

# 标题 -> 文件名（当前下载目录）
files = glob.glob(os.path.join(subdir, '*.srt'))
by_title = {}
for f in files:
    b = os.path.basename(f)[:-4]
    idx, title_part = b.split('_', 1)
    by_title.setdefault(title_part, []).append(f)

# 检查重复标题
dup = {t: fs for t, fs in by_title.items() if len(fs) > 1}
if dup:
    print('重复标题警告:', {t: len(fs) for t, fs in dup})

# 重命名到新目录：按清单顺序 001-139
ok, miss = 0, []
for i, (cid, title) in enumerate(order, 1):
    tp = clean(title)
    cand = by_title.get(tp, [])
    if not cand:
        # 尝试宽容匹配（clean 后可能因括号/空格差异）
        cand = [f for f in files if clean(os.path.basename(f)[:-4].split('_', 1)[1]) == tp]
    if not cand:
        miss.append((cid, title))
        continue
    src = cand[0]
    dst = os.path.join(outdir, '%03d_%s.srt' % (i, tp))
    data = open(src, 'rb').read()
    open(dst, 'wb').write(data)
    ok += 1

print('重命名成功:', ok, '缺失:', len(miss))
for cid, t in miss:
    print(' MISS', cid, t)
