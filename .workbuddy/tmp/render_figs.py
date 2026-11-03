import os, sys
import pymupdf

sys.stdout.reconfigure(encoding="utf-8")
root = r"D:\29469\Documents\notes\计算方法与优化"
out = r"D:\29469\Documents\notes\.workbuddy\tmp\figprev"
os.makedirs(out, exist_ok=True)

files = [
    ("第5章-解线性方程组的直接法/figures/norms-unit-balls.svg", "1-norms.png"),
    ("第5章-解线性方程组的直接法/figures/ill-conditioned-lines.svg", "2-illcond.png"),
    ("第6章-解线性方程组的迭代法/figures/cg-vs-sd.svg", "3-cg.png"),
    ("第7章-非线性方程/figures/fixed-point-cobweb.svg", "4-cobweb.png"),
    ("第7章-非线性方程/figures/contraction-map.svg", "5-contraction.png"),
]

for rel, name in files:
    p = os.path.join(root, rel.replace("/", os.sep))
    try:
        doc = pymupdf.open(p)
        page = doc[0]
        pix = page.get_pixmap(dpi=150)
        pix.save(os.path.join(out, name))
        print("OK", name, pix.width, "x", pix.height)
    except Exception as e:
        print("FAIL", name, type(e).__name__, e)
