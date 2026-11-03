# -*- coding: utf-8 -*-
"""Steffensen 的迭代函数在不动点处是「平」的 —— 与一般不动点迭代的几何对照。"""
import math, os, sys

sys.stdout.reconfigure(encoding="utf-8")

ROOT = r"D:\29469\Documents\notes\计算方法与优化"
INK = "#1f2933"
DIM = "#6b7785"
LIGHT = "#9aa5b1"
RED = "#c2410c"
BLUE = "#1d4ed8"
GREEN = "#047857"
FILL_U = "#e6edfb"
FILL_G = "#e1f5ee"
FONT = "'-apple-system','Segoe UI','Microsoft YaHei',sans-serif"

XS = 0.7390851332151599      # cos 的不动点
LO, HI = 0.55, 0.92
PW = 240.0


def head(w, h):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
        f'width="{w}" height="{h}" style="max-width:100%;height:auto" '
        f'font-family="{FONT}">'
        f'<rect width="{w}" height="{h}" fill="#ffffff"/>'
        '<defs>'
        f'<marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{INK}"/></marker>'
        f'<marker id="ar-b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{BLUE}"/></marker>'
        f'<marker id="ar-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{GREEN}"/></marker>'
        f'<marker id="ar-r" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{RED}"/></marker>'
        '</defs>'
    )


def esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def t(x, y, s, size=13, anchor="start", fill=INK, weight="400"):
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" fill="{fill}" '
            f'font-weight="{weight}" text-anchor="{anchor}">{esc(s)}</text>')


def save(rel, body):
    p = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w", encoding="utf-8").write(body + "</svg>")
    print("%-56s %6.1f KB" % (rel, os.path.getsize(p) / 1024))


def make_panel(b, ox, oy, curve_pts, curve_color, title, sub, tang, demo_from, demo_to, demo_label):
    """画一个面板。ox/oy 为绘图区左上角。"""

    def PX(v):
        return ox + (v - LO) / (HI - LO) * PW

    def PY(v):
        return oy + PW - (v - LO) / (HI - LO) * PW

    # 对角线 y = x
    b.append(f'<line x1="{PX(LO):.1f}" y1="{PY(LO):.1f}" x2="{PX(HI):.1f}" y2="{PY(HI):.1f}" '
             f'stroke="{LIGHT}" stroke-width="1.4" stroke-dasharray="6 4"/>')
    b.append(t(PX(HI) - 2, PY(HI) + 18, "y = x", 12, "end", DIM))

    # 曲线
    d = "M " + " L ".join(f"{PX(a):.1f} {PY(c):.1f}" for a, c in curve_pts)
    b.append(f'<path d="{d}" fill="none" stroke="{curve_color}" stroke-width="2.4" stroke-linejoin="round"/>')

    # 不动点
    b.append(f'<circle cx="{PX(XS):.1f}" cy="{PY(XS):.1f}" r="5" fill="{INK}" stroke="#ffffff" stroke-width="1.6"/>')
    b.append(f'<line x1="{PX(XS):.1f}" y1="{PY(XS):.1f}" x2="{PX(XS):.1f}" y2="{PY(LO):.1f}" '
             f'stroke="{INK}" stroke-width="1" stroke-dasharray="3 4"/>')
    b.append(t(PX(XS) + 8, PY(LO) + 16, "x*", 12, "start", INK, "600"))

    # 交点处的切线
    if tang == "slope":
        m = -math.sin(XS)
        dx = 0.075
        b.append(f'<line x1="{PX(XS-dx):.1f}" y1="{PY(XS+m*dx):.1f}" x2="{PX(XS+dx):.1f}" y2="{PY(XS-m*dx):.1f}" '
                 f'stroke="{RED}" stroke-width="2"/>')
        b.append(t(PX(0.752), PY(0.612), "斜率 −0.674", 11.5, "start", RED, "600"))
    else:
        dx = 0.075
        b.append(f'<line x1="{PX(XS-dx):.1f}" y1="{PY(XS):.1f}" x2="{PX(XS+dx):.1f}" y2="{PY(XS):.1f}" '
                 f'stroke="{RED}" stroke-width="3"/>')
        b.append(t(PX(0.80), PY(0.706), "水平：斜率 0", 11.5, "start", RED, "600"))

    # 一步演示：x0 -> x1
    b.append(f'<circle cx="{PX(demo_from[0]):.1f}" cy="{PY(demo_from[1]):.1f}" r="4.2" fill="{DIM}"/>')
    b.append(f'<circle cx="{PX(demo_to[0]):.1f}" cy="{PY(demo_to[1]):.1f}" r="4.2" fill="{curve_color}"/>')
    b.append(f'<line x1="{PX(demo_from[0]):.1f}" y1="{PY(demo_from[1]):.1f}" x2="{PX(demo_to[0]):.1f}" y2="{PY(demo_to[1]):.1f}" '
             f'stroke="{INK}" stroke-width="1.3" marker-end="url(#ar)"/>')
    b.append(t(PX(demo_from[0]) - 8, PY(demo_from[1]) + 4, "x₀ = %.2f" % demo_from[0], 11, "end", DIM))
    b.append(t(PX(demo_from[0]) + 11, PY(0.672), demo_label, 11, "start", INK, "600"))

    b.append(t(ox, oy - 14, title, 13.5, "start", INK, "600"))
    b.append(t(ox, oy - 30, sub, 11.5, "start", DIM))


def build():
    W, H = 780, 470
    b = [head(W, H)]
    b.append(t(40, 42, "Steffensen 的加速：换了个迭代函数，让它在不动点处变平", 16, "start", INK, "600"))
    b.append(t(40, 66, "同一根对角线 y = x，同样的不动点 x* ≈ 0.7391 —— 差别只在曲线穿过 x* 时的姿态", 12, "start", DIM))

    oy = 128.0
    # 左：一般不动点迭代
    cospts = []
    i = 0
    while True:
        xv = LO + (HI - LO) * i / 120.0
        cospts.append((xv, math.cos(xv)))
        i += 1
        if i > 120:
            break
    make_panel(b, 60.0, oy, cospts, BLUE,
               "一般不动点迭代：y = g(x)", "交点处斜着穿过，迭代像沿斜坡往根挪",
               "slope", (0.60, 0.60), (0.60, math.cos(0.60)), "一步到 0.8253，还差 0.086")

    # 右：Steffensen
    phipts = []
    with open(r"D:\29469\Documents\notes\.workbuddy\tmp\stef_data.txt", encoding="utf-8") as f:
        for line in f:
            a, c = line.split()
            phipts.append((float(a), float(c)))
    make_panel(b, 420.0, oy, phipts, GREEN,
               "Steffensen：y = φ(x)", "整条曲线几乎是平的，穿过 x* 时也是平的",
               "flat", (0.60, 0.60), (0.60, phipts[0][1]), "一步到 0.7364，只差 0.0027")

    b.append(t(40, 398, "φ 是用 g 现算出来的：φ(x) = (x·g(g(x)) − g(x)²) / (x − 2g(x) + g(g(x)))。", 12.5, "start", INK))
    b.append(t(40, 420, "它在 x* 处满足 φ(x*) = x* 且 φ′(x*) = 0 —— 迭代函数在不动点处变平，于是 xₖ₊₁ = φ(xₖ) 一步就落到根附近，收敛阶升到 2。", 12, "start", DIM))
    b.append(t(40, 442, "这与 Aitken 完全不同：Aitken 改造的是「算出来的序列」，Steffensen 改造的是「迭代函数本身」。", 12, "start", DIM))
    save(os.path.join("第7章-非线性方程", "figures", "stefensen-tangent.svg"), "\n".join(b))


build()
