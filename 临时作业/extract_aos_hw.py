# -*- coding: utf-8 -*-
"""抽取 13 套 Homework 首页文字 + 校验所有 PDF 完整性。"""
import os
import pymupdf

BASE = r"C:\Users\29469\Desktop\All of Statistics 统计部分"
HW = os.path.join(BASE, "01_主线_Wasserman_36-705_Fall2020", "Homework")

print("=== HOMEWORK HEADS ===")
for n in range(1, 14):
    p = os.path.join(HW, "HW%02d.pdf" % n)
    try:
        doc = pymupdf.open(p)
        head = [l.strip() for l in doc[0].get_text().strip().splitlines() if l.strip()][:6]
        print("HW%02d | %s" % (n, " / ".join(head)))
        doc.close()
    except Exception as e:
        print("HW%02d | ERROR %s" % (n, e))

print("=== PDF INTEGRITY ===")
bad = []
count = 0
for root, _, files in os.walk(BASE):
    for fn in files:
        if not fn.lower().endswith(".pdf"):
            continue
        count += 1
        fp = os.path.join(root, fn)
        try:
            with open(fp, "rb") as f:
                if f.read(4) != b"%PDF":
                    bad.append((fp, "bad header"))
            d = pymupdf.open(fp)
            if len(d) < 1:
                bad.append((fp, "no pages"))
            d.close()
        except Exception as e:
            bad.append((fp, str(e)[:80]))
print("checked=%d bad=%d" % (count, len(bad)))
for b in bad:
    print("  BAD:", b[0], "|", b[1])
