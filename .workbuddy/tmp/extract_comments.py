# -*- coding: utf-8 -*-
"""提取三份中译课件里所有 /* */ 注释内容，去重后输出"""
import zipfile, re, sys, os, json

sys.stdout.reconfigure(encoding='utf-8')
BASE = r'C:/Users/29469/Desktop/大一下计算机科学导论/课件-CSAPP3e'
FILES = ['21-netprog1_中文.pptx', '16-io_中文.pptx', '22-netprog2-中文翻译.pptx']

uniq = {}
per_file = {}

for f in FILES:
    p = os.path.join(BASE, f)
    if not os.path.exists(p):
        print('缺失', f); continue
    z = zipfile.ZipFile(p)
    slides = [n for n in z.namelist() if re.match(r'ppt/slides/slide\d+\.xml$', n)]
    cnt = 0
    for n in slides:
        x = z.read(n).decode('utf-8')
        for para in re.findall(r'<a:p>(.*?)</a:p>', x, flags=re.S):
            txt = ''.join(re.findall(r'<a:t[^>]*>(.*?)</a:t>', para, flags=re.S))
            if not txt.strip():
                continue
            for m in re.finditer(r'/\*(.+?)\*/', txt, flags=re.S):
                c = m.group(1).strip()
                if not c:
                    continue
                if re.search(r'[A-Za-z]{2,}', c) and not re.search(r'[\u4e00-\u9fff]', c):
                    uniq[c] = uniq.get(c, 0) + 1
                    cnt += 1
    per_file[f] = cnt
    print(f, '英文注释片段', cnt)

print()
print('唯一注释', len(uniq))
print('-' * 70)
for c in sorted(uniq, key=lambda s: (-uniq[s], s)):
    print('%2d×  %s' % (uniq[c], c))

json.dump(uniq, open(r'D:/29469/Documents/notes/.workbuddy/tmp/comments.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
