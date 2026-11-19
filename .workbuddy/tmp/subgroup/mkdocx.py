import os, shutil
import docx
from docx.shared import Pt
from docx.oxml.ns import qn

base = r'D:\29469\Documents\notes\离散数学\原始材料\课堂录音稿\补充-子群判定与典型群'
os.makedirs(base, exist_ok=True)

shutil.copyfile(r'C:\Users\29469\Downloads\子群判定方法讲解_原文.docx', os.path.join(base, '原文.docx'))
shutil.copyfile(r'C:\Users\29469\Downloads\子群判定方法讲解_导读.docx', os.path.join(base, '导读.docx'))

src = r'D:\29469\Documents\notes\.workbuddy\tmp\subgroup\transcript.md'
lines = open(src, encoding='utf-8').read().split('\n')

d = docx.Document()
st = d.styles['Normal']
st.font.name = '等线'
st.font.size = Pt(10.5)
st.element.rPr.rFonts.set(qn('w:eastAsia'), '等线')

for ln in lines:
    s = ln.rstrip()
    if not s.strip():
        continue
    if s.startswith('## '):
        d.add_heading(s[3:].strip(), level=2)
    elif s.startswith('# '):
        d.add_heading(s[2:].strip(), level=1)
    else:
        d.add_paragraph(s)

d.save(os.path.join(base, '整理版逐字稿.docx'))
print('saved', os.path.join(base, '整理版逐字稿.docx'))
print('paras', len(docx.Document(os.path.join(base, '整理版逐字稿.docx')).paragraphs))
