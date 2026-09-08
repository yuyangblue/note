# -*- coding: utf-8 -*-
import glob, os

d = r'D:\29469\Documents\notes\数据结构\原始材料\字幕_修正'

def srt_to_text(path):
    t = open(path, encoding='utf-8', errors='replace').read()
    out = []
    for ln in t.splitlines():
        ln = ln.strip()
        if not ln:
            continue
        if ln.isdigit():
            continue
        if '-->' in ln:
            continue
        out.append(ln)
    return ' '.join(out)

outdir = r'D:\29469\Documents\notes\数据结构\原始材料\纯文本_修正'
os.makedirs(outdir, exist_ok=True)
files = sorted(glob.glob(os.path.join(d, '*.srt')))
for f in files:
    name = os.path.basename(f).replace('.srt', '.txt')
    with open(os.path.join(outdir, name), 'w', encoding='utf-8') as w:
        w.write(srt_to_text(f))

# 按讲合并
def merge(start, end, label):
    parts = [os.path.join(outdir, os.path.basename(f).replace('.srt', '.txt'))
             for f in files[start-1:end]]
    merged = ''
    for p in parts:
        name = os.path.basename(p)
        merged += '\n\n===== %s =====\n\n' % name + open(p, encoding='utf-8').read()
    out = os.path.join(outdir, '_合并_%s.txt' % label)
    open(out, 'w', encoding='utf-8').write(merged)
    print(label, len(merged), '字符')

# 讲次边界（按清单）：第1讲=1-10, 第2讲=11-24, 第3讲=25-41...
# 先用编号推断：需要从标题判断。第1讲 1.x = 001-010
merge(1, 10, '第01讲')
merge(11, 24, '第02讲')
