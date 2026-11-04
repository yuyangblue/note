# -*- coding: utf-8 -*-
import os, re, sys
from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

sys.stdout.reconfigure(encoding='utf-8')
TMP = r'D:\29469\Documents\notes\.workbuddy\tmp'
OUT = r'D://29469//Documents//notes//计算方法与优化//原始材料//课堂录音稿//11.04-幂法加速与收缩方法//原点位移加速方法-整理稿.docx'

txt = ''
for f in ['zhengli1104.md']:
    txt += open(os.path.join(TMP, f), encoding='utf-8').read() + '\n'

doc = Document()
st = doc.styles['Normal']
st.font.name = 'Consolas'
st.font.size = Pt(10.5)

lines = txt.split('\n')
i = 0
n_par = 0
while i < len(lines):
    l = lines[i].rstrip()
    s = l.strip()
    if not s:
        i += 1
        continue
    if s.startswith('# '):
        doc.add_heading(s[2:].strip(), level=0)
    elif s.startswith('## '):
        doc.add_heading(s[3:].strip(), level=1)
    elif s.startswith('### '):
        doc.add_heading(s[4:].strip(), level=2)
    elif s.startswith('$$'):
        # 显示公式块：原样收纳
        buf = [s]
        if s == '$$':
            i += 1
            while i < len(lines) and lines[i].strip() != '$$':
                buf.append(lines[i].rstrip())
                i += 1
            if i < len(lines):
                buf.append('$$')
            else:
                i -= 1
        body = '\n'.join(buf).replace('$$', '').strip()
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(body)
        r.font.name = 'Cambria Math'
        r.italic = False
    elif s.startswith('> '):
        p = doc.add_paragraph()
        p.paragraph_format.left_indent = Pt(18)
        r = p.add_run(s[2:].strip())
        r.italic = True
        r.font.color.rgb = RGBColor(0x55, 0x55, 0x55)
    elif s.startswith('|'):
        # 表格：收集连续行
        rows = []
        while i < len(lines) and lines[i].strip().startswith('|'):
            rows.append(lines[i].strip())
            i += 1
        i -= 1
        cells = [[c.strip() for c in r.strip('|').split('|')] for r in rows]
        cells = [r for r in cells if not all(re.fullmatch(r':?-{2,}:?', c or '') for c in r)]
        if cells:
            ncol = max(len(r) for r in cells)
            t = doc.add_table(rows=len(cells), cols=ncol)
            t.style = 'Table Grid'
            for ri, row in enumerate(cells):
                for ci in range(ncol):
                    t.cell(ri, ci).text = row[ci] if ci < len(row) else ''
    elif s.startswith('- '):
        p = doc.add_paragraph(s[2:].strip(), style='List Bullet')
    elif re.match(r'^\d+\.\s', s):
        p = doc.add_paragraph(re.sub(r'^\d+\.\s', '', s), style='List Number')
    else:
        doc.add_paragraph(s)
        n_par += 1
    i += 1

doc.save(OUT)
print('已生成', OUT)
print('大小 %.1f KB' % (os.path.getsize(OUT) / 1024))
print('正文段落', n_par)
print('字数约', len(re.sub(r'\s', '', txt)))
