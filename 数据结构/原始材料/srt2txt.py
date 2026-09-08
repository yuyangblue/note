# -*- coding: utf-8 -*-
import os, re, glob

def srt_to_text(path):
    t = open(path, encoding='utf-8', errors='replace').read()
    lines = t.splitlines()
    out = []
    for ln in lines:
        ln = ln.strip()
        if not ln:
            continue
        if re.fullmatch(r'\d+', ln):
            continue
        if '-->' in ln:
            continue
        out.append(ln)
    return ' '.join(out)

base = r'D:\29469\Documents\notes\数据结构\原始材料\字幕'
files = sorted(glob.glob(os.path.join(base, '*.srt')))

# 按视频编号分组输出纯文本
for f in files:
    name = os.path.basename(f)
    num = name.split('_')[0]
    txt = srt_to_text(f)
    outpath = os.path.join(r'D:\29469\Documents\notes\数据结构\原始材料\纯文本', name.replace('.srt', '.txt'))
    os.makedirs(os.path.dirname(outpath), exist_ok=True)
    with open(outpath, 'w', encoding='utf-8') as w:
        w.write(txt)

print('转换完成', len(files))
