# -*- coding: utf-8 -*-
import os, sys
import pymupdf

sys.stdout.reconfigure(encoding="utf-8")
ROOT = r"D:\29469\Documents\notes\计算方法与优化"
OUT = r"D:\29469\Documents\notes\.workbuddy\tmp\figprev2"
os.makedirs(OUT, exist_ok=True)

items = [
    (r"第3章-最小二乘问题\figures\lsq-projection.svg", "1-projection.png"),
    (r"第5章-解线性方程组的直接法\figures\lu-order.svg", "2-lu.png"),
    (r"第6章-解线性方程组的迭代法\figures\tridiag-structure.svg", "3-tridiag.png"),
    (r"第7章-非线性方程\figures\aitken-sequence.svg", "4-aitken.png"),
    (r"第6章-解线性方程组的迭代法\figures\spectral-radius.svg", "5-spectral.png"),
    (r"第5章-解线性方程组的直接法\figures\cond-ellipse.svg", "6-cond.png"),
]

for src, dst in items:
    p = os.path.join(ROOT, src)
    try:
        doc = pymupdf.open(p)
        page = doc[0]
        pix = page.get_pixmap(dpi=132, alpha=False)
        out = os.path.join(OUT, dst)
        pix.save(out)
        print("%-18s %dx%d  %.0f KB" % (dst, pix.width, pix.height, os.path.getsize(out) / 1024))
    except Exception as e:
        print("FAIL", src, type(e).__name__, e)
