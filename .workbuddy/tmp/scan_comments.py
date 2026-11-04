# -*- coding: utf-8 -*-
"""扫描 pptx 中代码块里的英文注释"""
import zipfile, re, sys, os

sys.stdout.reconfigure(encoding='utf-8')
BASE = r'C:/Users/29469/Desktop/大一下计算机科学导论/课件-CSAPP3e'

files = ['21-netprog1_中文.pptx']

for f in files:
    p = os.path.join(BASE, f)
    if not os.path.exists(p):
        print('缺失', f); continue
    z = zipfile.ZipFile(p)
    slides = sorted([n for n in z.namelist() if re.match(r'ppt/slides/slide\d+\.xml$', n)],
                    key=lambda x: int(re.search(r'(\d+)', x).group(1)))
    print('=' * 60)
    print(f, '页数', len(slides))
    total = 0
    for n in slides:
        x = z.read(n).decode('utf-8')
        # 按段落取文本
        paras = re.findall(r'<a:p>(.*?)</a:p>', x, flags=re.S)
        hits = []
        for para in paras:
            txt = ''.join(re.findall(r'<a:t[^>]*>(.*?)</a:t>', para, flags=re.S))
            txt = txt.strip()
            if not txt:
                continue
            # 含注释标记
            if '/*' in txt or '*/' in txt or txt.startswith('//') or '//' in txt:
                hits.append(txt)
        if hits:
            sid = re.search(r'(\d+)', n).group(1)
            print('--- slide %s (%d 段含注释) ---' % (sid, len(hits)))
            for h in hits:
                print('   ', h)
            total += len(hits)
    print('合计含注释段落', total)
