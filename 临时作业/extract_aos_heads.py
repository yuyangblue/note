# -*- coding: utf-8 -*-
"""抽取主线 27 份 Lecture Notes 首页文字，用于生成章节对照表。"""
import os
import pymupdf

D = r"C:\Users\29469\Desktop\All of Statistics 统计部分\01_主线_Wasserman_36-705_Fall2020\LectureNotes"
OUT = r"D:\29469\Documents\notes\临时作业\aos_lecture_heads.txt"

lines = []
for n in range(1, 28):
    p = os.path.join(D, "L%02d.pdf" % n)
    try:
        doc = pymupdf.open(p)
        text = doc[0].get_text().strip()
        pages = len(doc)
        # 取前若干行非空内容
        head = [l.strip() for l in text.splitlines() if l.strip()][:8]
        lines.append("L%02d | pages=%d | %s" % (n, pages, " / ".join(head)))
        doc.close()
    except Exception as e:
        lines.append("L%02d | ERROR %s" % (n, e))

open(OUT, "w", encoding="utf-8").write("\n".join(lines))
print("\n".join(lines))
