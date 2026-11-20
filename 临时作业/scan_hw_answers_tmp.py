# -*- coding: utf-8 -*-
import io, re, glob, os

D = r'D:/29469/Documents/notes/统计学完全教程/作业'
for p in sorted(glob.glob(os.path.join(D, '*.md'))):
    lines = io.open(p, encoding='utf-8').read().splitlines()
    # 找每个 [!note]- 块，记录标题行号、长度、之前的题目行
    blocks = []
    i = 0
    while i < len(lines):
        if '[!note]-' in lines[i]:
            title = lines[i].strip()
            j = i + 1
            body = []
            while j < len(lines) and (lines[j].strip().startswith('>') or lines[j].strip() == ''):
                body.append(lines[j].strip())
                j += 1
            chars = sum(len(b) for b in body)
            # 往上找最近的题目/小节标题
            q = ''
            for k in range(i-1, max(-1, i-30), -1):
                if lines[k].strip().startswith('## ') or lines[k].strip().startswith('**题目'):
                    q = lines[k].strip().lstrip('#* ').strip()
                    break
            blocks.append((i+1, chars, q[:34], title.split(']')[-1].strip()[:20]))
            i = j
        else:
            i += 1
    print('\n===== %s (%d blocks) =====' % (os.path.basename(p), len(blocks)))
    for ln, chars, q, t in blocks:
        flag = '  <<< 短' if chars < 160 else ''
        print('  L%-4d %5d字  %-36s %s' % (ln, chars, q, flag))
