# -*- coding: utf-8 -*-
"""生成计算方法与优化笔记的 SVG 插图（v3）。"""
import math, os, sys

sys.stdout.reconfigure(encoding="utf-8")

ROOT = r"D:\29469\Documents\notes\计算方法与优化"
INK = "#1f2933"
DIM = "#6b7785"
LIGHT = "#9aa5b1"
GRID = "#e4e7eb"
RED = "#c2410c"
BLUE = "#1d4ed8"
GREEN = "#047857"
FONT = "'-apple-system','Segoe UI','Microsoft YaHei',sans-serif"


def head(w, h):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
        f'font-family="{FONT}">'
        f'<rect width="{w}" height="{h}" fill="#ffffff"/>'
        '<defs>'
        f'<marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
        f'<path d="M0,0 L10,5 L0,10 z" fill="{INK}"/></marker>'
        f'<marker id="ar-r" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
        f'<path d="M0,0 L10,5 L0,10 z" fill="{RED}"/></marker>'
        f'<marker id="ar-d" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">'
        f'<path d="M0,0 L10,5 L0,10 z" fill="{DIM}"/></marker>'
        '</defs>'
    )


def esc(s):
    """转义 & < >，但保护已经写好的实体。"""
    s = str(s)
    s = s.replace("&lt;", "\x00L").replace("&gt;", "\x00G").replace("&amp;", "\x00A")
    s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return s.replace("\x00L", "&lt;").replace("\x00G", "&gt;").replace("\x00A", "&amp;")


def t(x, y, s, size=13, anchor="start", fill=INK, weight="400"):
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" fill="{fill}" '
            f'font-weight="{weight}" text-anchor="{anchor}">{esc(s)}</text>')


def norms(x, y, which, size=13, anchor="start", fill=INK, weight="400"):
    """渲染 ‖x‖下标 = 1 形式。"""
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" fill="{fill}" font-weight="{weight}" '
            f'text-anchor="{anchor}">‖x‖<tspan dy="4" font-size="{size-3}">{which}</tspan>'
            f'<tspan dy="-4"> = 1</tspan></text>')


def save(rel, svg):
    p = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w", encoding="utf-8").write(svg)
    print("写出", rel, "%.1f KB" % (len(svg.encode("utf-8")) / 1024))


# ------------------------------------------------------------ 1 单位球
def fig_norm_balls():
    W, H = 720, 430
    cx, cy, R = 250, 240, 106
    b = [head(W, H)]
    b.append(t(48, 44, "三种范数各自的「单位球」", 16, "start", INK, "600"))
    b.append(t(48, 68, "同样要求长度为 1，形状却不同；嵌套的宽窄就是范数等价常数", 12, "start", DIM))

    b.append(f'<line x1="{cx-R-46}" y1="{cy}" x2="{cx+R+52}" y2="{cy}" stroke="{LIGHT}" stroke-width="1.2" marker-end="url(#ar)"/>')
    b.append(f'<line x1="{cx}" y1="{cy+R+44}" x2="{cx}" y2="{cy-R-46}" stroke="{LIGHT}" stroke-width="1.2" marker-end="url(#ar)"/>')
    b.append(t(cx + R + 44, cy + 18, "x₁", 12, "end", DIM))
    b.append(t(cx + 14, cy - R - 38, "x₂", 12, "start", DIM))

    b.append(f'<rect x="{cx-R}" y="{cy-R}" width="{2*R}" height="{2*R}" fill="none" stroke="{GREEN}" stroke-width="2.2"/>')
    b.append(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="{INK}" stroke-width="2.2"/>')
    b.append(f'<polygon points="{cx-R},{cy} {cx},{cy-R} {cx+R},{cy} {cx},{cy+R}" fill="none" stroke="{BLUE}" stroke-width="2.2"/>')
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        b.append(f'<circle cx="{cx+dx*R}" cy="{cy+dy*R}" r="3.2" fill="{INK}"/>')

    lx, ly = 480, 126
    items = [(GREEN, "正方形", "∞", "最外层：每边到 ±1"),
             (INK, "单位圆", "2", "中间：欧氏长度"),
             (BLUE, "菱形", "1", "最内层：顶点落在坐标轴上")]
    for i, (c, name, sub, desc) in enumerate(items):
        yy = ly + i * 70
        if name == "正方形":
            b.append(f'<rect x="{lx}" y="{yy-12}" width="24" height="24" fill="none" stroke="{c}" stroke-width="2.2"/>')
        elif name == "单位圆":
            b.append(f'<circle cx="{lx+12}" cy="{yy}" r="12" fill="none" stroke="{c}" stroke-width="2.2"/>')
        else:
            b.append(f'<polygon points="{lx},{yy} {lx+12},{yy-12} {lx+24},{yy} {lx+12},{yy+12}" fill="none" stroke="{c}" stroke-width="2.2"/>')
        b.append(t(lx + 38, yy - 4, name, 13, "start", INK, "600"))
        b.append(norms(lx + 38, yy + 15, sub, 12, "start", c, "600"))
        b.append(t(lx + 38, yy + 33, desc, 11, "start", DIM))

    b.append(f'<line x1="480" y1="338" x2="688" y2="338" stroke="{GRID}" stroke-width="1" stroke-dasharray="3 3"/>')
    b.append(t(480, 364, "包含关系", 12, "start", DIM, "600"))
    b.append(f'<text x="480" y="390" font-size="14" fill="{INK}">B<tspan dy="4" font-size="10">1</tspan>'
             f'<tspan dy="-4"> ⊂ B</tspan><tspan dy="4" font-size="10">2</tspan><tspan dy="-4"> ⊂ B</tspan>'
             f'<tspan dy="4" font-size="10">∞</tspan></text>')
    b.append(f'<text x="480" y="416" font-size="13.5" fill="{INK}">‖x‖<tspan dy="4" font-size="10">∞</tspan>'
             f'<tspan dy="-4"> ≤ ‖x‖</tspan><tspan dy="4" font-size="10">2</tspan>'
             f'<tspan dy="-4"> ≤ ‖x‖</tspan><tspan dy="4" font-size="10">1</tspan></text>')
    b.append("</svg>")
    return "".join(b)


# ------------------------------------------------------------ 2 病态
def fig_ill_cond():
    W, H = 720, 430
    xmin, xmax, ymin, ymax = 0.0, 5.0, 0.0, 4.2
    ox, oy = 82, 356
    sw, sh = 590, 272
    sx, sy = sw / (xmax - xmin), sh / (ymax - ymin)

    def P(x, y):
        return (ox + (x - xmin) * sx, oy - (y - ymin) * sy)

    b = [head(W, H)]
    b.append(t(48, 44, "两条几乎平行的直线：右端动一点，交点跑很远", 16, "start", INK, "600"))
    b.append(t(48, 68, "夹角越小，同样的 δb 引起的 δx 越大——条件数大就是这个意思", 12, "start", DIM))

    b.append(f'<line x1="{ox}" y1="{oy}" x2="{ox+sw+30}" y2="{oy}" stroke="{LIGHT}" stroke-width="1.2" marker-end="url(#ar)"/>')
    b.append(f'<line x1="{ox}" y1="{oy}" x2="{ox}" y2="{oy-sh-26}" stroke="{LIGHT}" stroke-width="1.2" marker-end="url(#ar)"/>')
    b.append(t(ox + sw + 24, oy + 18, "x₁", 12, "end", DIM))
    b.append(t(ox - 12, oy - sh - 16, "x₂", 12, "end", DIM))

    l1a, l1b = P(0, 0.15), P(4.7, 4.85)
    l2a, l2b = P(0, 0.55), P(4.3, 4.205)
    l3a, l3b = P(0, 0.67), P(4.15, 4.195)
    b.append(f'<line x1="{l1a[0]:.1f}" y1="{l1a[1]:.1f}" x2="{l1b[0]:.1f}" y2="{l1b[1]:.1f}" stroke="{INK}" stroke-width="2.2"/>')
    b.append(f'<line x1="{l2a[0]:.1f}" y1="{l2a[1]:.1f}" x2="{l2b[0]:.1f}" y2="{l2b[1]:.1f}" stroke="{INK}" stroke-width="2.2"/>')
    b.append(f'<line x1="{l3a[0]:.1f}" y1="{l3a[1]:.1f}" x2="{l3b[0]:.1f}" y2="{l3b[1]:.1f}" stroke="{RED}" stroke-width="2" stroke-dasharray="7 5"/>')

    pA, pB = P(2.667, 2.817), P(3.467, 3.617)
    b.append(f'<circle cx="{pA[0]:.1f}" cy="{pA[1]:.1f}" r="5" fill="{INK}" stroke="#ffffff" stroke-width="1.6"/>')
    b.append(f'<circle cx="{pB[0]:.1f}" cy="{pB[1]:.1f}" r="5" fill="{RED}" stroke="#ffffff" stroke-width="1.6"/>')
    b.append(t(pA[0] - 14, pA[1] + 30, "x*", 13.5, "end", INK, "600"))
    b.append(t(pB[0] + 16, pB[1] + 30, "x* + δx", 13.5, "start", RED, "600"))
    b.append(f'<line x1="{pA[0]+7:.1f}" y1="{pA[1]-7:.1f}" x2="{pB[0]-8:.1f}" y2="{pB[1]+8:.1f}" stroke="{RED}" stroke-width="1.8" marker-end="url(#ar-r)"/>')

    q1, q2 = P(0, 0.55), P(0, 0.67)
    b.append(f'<line x1="{q1[0]-24:.1f}" y1="{q1[1]:.1f}" x2="{q2[0]-24:.1f}" y2="{q2[1]-3:.1f}" stroke="{RED}" stroke-width="1.8" marker-end="url(#ar-r)"/>')
    b.append(t(q1[0] - 32, q1[1] + 16, "δb₂", 12, "end", RED, "600"))

    b.append(t(P(4.62, 4.77)[0], P(4.62, 4.77)[1] - 14, "F₁ = 0", 12.5, "end", INK, "600"))
    b.append(t(P(4.24, 4.154)[0] + 10, P(4.24, 4.154)[1] + 18, "F₂ = 0", 12.5, "start", INK, "600"))
    b.append(t(P(4.08, 4.138)[0] + 10, P(4.08, 4.138)[1] + 38, "F₂ = δb₂", 12, "start", RED, "600"))

    b.append(t(48, 404, "δb₂ 只挪了 0.12，交点从 (2.67, 2.82) 跳到 (3.47, 3.62)", 12, "start", DIM))
    b.append("</svg>")
    return "".join(b)


# ------------------------------------------------------------ 3 收敛速度
def fig_cg():
    W, H = 720, 440
    L, Rr, T, B = 104, 646, 116, 356
    kmax = 40
    ymin, ymax = -3.6, 0.1

    def P(k, v):
        return (L + (k / kmax) * (Rr - L), B - (v - ymin) / (ymax - ymin) * (B - T))

    b = [head(W, H)]
    b.append(t(48, 44, "同一个 κ = 100，两条误差界衰减得有多快", 16, "start", INK, "600"))
    b.append(t(48, 68, "竖轴取对数：画成直线表示按固定比例缩小，越陡越快", 12, "start", DIM))

    for v, lab in [(0, "1"), (-1, "10⁻¹"), (-2, "10⁻²"), (-3, "10⁻³")]:
        y = P(0, v)[1]
        b.append(f'<line x1="{L}" y1="{y:.1f}" x2="{Rr}" y2="{y:.1f}" stroke="{GRID}" stroke-width="1"/>')
        b.append(t(L - 14, y + 4, lab, 11.5, "end", DIM))
    for k in range(0, kmax + 1, 10):
        x = P(k, 0)[0]
        b.append(f'<line x1="{x:.1f}" y1="{T}" x2="{x:.1f}" y2="{B}" stroke="{GRID}" stroke-width="1" stroke-dasharray="2 4"/>')
        b.append(t(x, B + 24, str(k), 11.5, "middle", DIM))

    b.append(f'<line x1="{L}" y1="{B}" x2="{Rr+18}" y2="{B}" stroke="{LIGHT}" stroke-width="1.3" marker-end="url(#ar)"/>')
    b.append(f'<line x1="{L}" y1="{B}" x2="{L}" y2="{T-20}" stroke="{LIGHT}" stroke-width="1.3" marker-end="url(#ar)"/>')
    b.append(t(Rr + 16, B + 46, "k", 12.5, "end", DIM))
    b.append(t(L - 14, T - 26, "相对误差", 11.5, "end", DIM))

    kap = 100.0
    sd = [P(k, k * math.log10((kap - 1) / (kap + 1))) for k in range(kmax + 1)]
    cg = []
    for k in range(kmax + 1):
        v = 0.301 + k * math.log10((math.sqrt(kap) - 1) / (math.sqrt(kap) + 1))
        cg.append(P(k, max(v, ymin - 0.2)))

    b.append('<polyline points="' + " ".join(f"{x:.1f},{y:.1f}" for x, y in sd) +
             f'" fill="none" stroke="{BLUE}" stroke-width="2.4"/>')
    b.append('<polyline points="' + " ".join(f"{x:.1f},{y:.1f}" for x, y in cg) +
             f'" fill="none" stroke="{RED}" stroke-width="2.4"/>')

    b.append(t(P(26, -0.06)[0], P(26, -0.06)[1], "最速下降", 12.5, "middle", BLUE, "600"))
    b.append(t(P(31, -1.35)[0], P(31, -1.35)[1], "共轭梯度", 12.5, "middle", RED, "600"))

    k0 = 24
    x24 = P(k0, 0)[0]
    b.append(f'<line x1="{x24:.1f}" y1="{T}" x2="{x24:.1f}" y2="{B}" stroke="{DIM}" stroke-width="1" stroke-dasharray="4 3"/>')
    b.append(f'<circle cx="{x24:.1f}" cy="{P(k0, k0*math.log10(0.9802))[1]:.1f}" r="3.6" fill="{BLUE}"/>')
    b.append(f'<circle cx="{x24:.1f}" cy="{P(k0, 0.301+k0*math.log10((math.sqrt(kap)-1)/(math.sqrt(kap)+1)))[1]:.1f}" r="3.6" fill="{RED}"/>')

    b.append(t(48, 400, "24 步时：最速下降还剩 0.62，共轭梯度已经到 1.6 × 10⁻²", 12.5, "start", INK))
    b.append(t(48, 424, "两式分别是 ((κ−1)/(κ+1))^k 与 2((√κ−1)/(√κ+1))^k，κ = 100", 11.5, "start", DIM))
    b.append("</svg>")
    return "".join(b)


# ------------------------------------------------------------ 4 蛛网
def cobweb(px, py, w, h, g, x0, lo, hi, steps, color, title):
    sx, sy = w / (hi - lo), h / (hi - lo)

    def P(x, y):
        return (px + (x - lo) * sx, py + h - (y - lo) * sy)

    b = [f'<rect x="{px}" y="{py}" width="{w}" height="{h}" fill="#fcfcfd" stroke="#e4e7eb" stroke-width="1" rx="4"/>']
    a1, a2 = P(lo, lo), P(hi, hi)
    b.append(f'<line x1="{a1[0]:.1f}" y1="{a1[1]:.1f}" x2="{a2[0]:.1f}" y2="{a2[1]:.1f}" stroke="{LIGHT}" stroke-width="1.2"/>')
    b.append(t(a2[0] - 4, a2[1] - 8, "y = x", 10, "end", LIGHT))

    pts, n = [], 200
    for i in range(n + 1):
        xx = lo + (hi - lo) * i / n
        try:
            yy = g(xx)
        except Exception:
            continue
        if yy is None or yy < lo - 0.4 or yy > hi + 0.4:
            continue
        pts.append(f"{P(xx, yy)[0]:.1f},{P(xx, yy)[1]:.1f}")
    b.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{INK}" stroke-width="1.8"/>')

    seq = [x0]
    for _ in range(steps):
        try:
            yy = g(seq[-1])
        except Exception:
            break
        if yy is None:
            break
        seq.append(yy)
        if abs(yy) > 1e4:
            break

    cur = x0
    for i in range(len(seq) - 1):
        nxt = seq[i + 1]
        if nxt > hi:
            p1, p2 = P(cur, cur), P(cur, hi)
            b.append(f'<line x1="{p1[0]:.1f}" y1="{p1[1]:.1f}" x2="{p2[0]:.1f}" y2="{p2[1]-6:.1f}" stroke="{color}" stroke-width="1.6" marker-end="url(#ar)"/>')
            break
        p1, p2, p3 = P(cur, cur), P(cur, nxt), P(nxt, nxt)
        b.append(f'<line x1="{p1[0]:.1f}" y1="{p1[1]:.1f}" x2="{p2[0]:.1f}" y2="{p2[1]:.1f}" stroke="{color}" stroke-width="1.6"/>')
        b.append(f'<line x1="{p2[0]:.1f}" y1="{p2[1]:.1f}" x2="{p3[0]:.1f}" y2="{p3[1]:.1f}" stroke="{color}" stroke-width="1.6"/>')
        cur = nxt

    p0 = P(x0, x0)
    b.append(f'<circle cx="{p0[0]:.1f}" cy="{p0[1]:.1f}" r="3.2" fill="{color}"/>')
    b.append(t(px + 6, py - 9, title, 12, "start", INK, "600"))
    return "".join(b)


def fig_cobweb():
    W, H = 780, 372
    b = [head(W, H)]
    b.append(t(44, 42, "蛛网迭代：在 y = g(x) 与 y = x 之间来回折", 16, "start", INK, "600"))
    b.append(t(44, 66, "先竖直走到曲线上，再水平走到 y = x；折线往里收就是收敛，往外散就是发散", 12, "start", DIM))

    b.append(cobweb(52, 96, 208, 208, lambda x: (x + 1) ** (1 / 3) if x > -1 else 0,
                    1.50, 0.95, 1.72, 6, BLUE, "(a)  0 < g′ < 1"))
    b.append(cobweb(292, 96, 208, 208, math.cos, 1.05, 0.15, 1.15, 8, RED, "(b)  −1 < g′ < 0"))
    b.append(cobweb(532, 96, 208, 208, lambda x: x ** 3 - 1, 1.50, 0.9, 3.1, 3, "#6d28d9", "(c)  |g′| > 1"))

    b.append(t(156, 332, "单调收敛，从一侧逼近", 11.5, "middle", DIM))
    b.append(t(396, 332, "振荡收敛，绕成螺旋", 11.5, "middle", DIM))
    b.append(t(636, 332, "越折越远，冲出去", 11.5, "middle", DIM))
    b.append(t(52, 354, "g(x) = ∛(x+1)", 11, "start", BLUE))
    b.append(t(292, 354, "g(x) = cos x", 11, "start", RED))
    b.append(t(532, 354, "g(x) = x³ − 1", 11, "start", "#6d28d9"))
    b.append("</svg>")
    return "".join(b)


# ------------------------------------------------------------ 5 压缩映射
def fig_contraction():
    W, H = 720, 430
    b = [head(W, H)]
    b.append(t(48, 44, "压缩映射：任意两点的像，距离被同一个 L 倍缩短", 16, "start", INK, "600"))
    b.append(t(48, 68, "L < 1 时反复迭代必然挤到同一点——这就是压缩映射原理", 12, "start", DIM))

    c1, r1 = (296, 252), 132
    c2, r2 = (348, 278), 68
    Lr = r2 / r1

    b.append(f'<circle cx="{c1[0]}" cy="{c1[1]}" r="{r1}" fill="#f8fafc" stroke="{BLUE}" stroke-width="1.8" stroke-dasharray="7 5"/>')
    b.append(f'<circle cx="{c2[0]}" cy="{c2[1]}" r="{r2}" fill="#fdf2ee" stroke="{RED}" stroke-width="1.8"/>')
    b.append(t(c1[0] - r1 + 4, c1[1] - r1 - 10, "D₀", 13.5, "start", BLUE, "600"))
    b.append(t(c2[0] + r2 + 8, c2[1] + 22, "Φ(D₀)", 13.5, "start", RED, "600"))

    x = (200, 175)
    y = (250, 352)
    fx = (c2[0] + (x[0] - c1[0]) * Lr, c2[1] + (x[1] - c1[1]) * Lr)
    fy = (c2[0] + (y[0] - c1[0]) * Lr, c2[1] + (y[1] - c1[1]) * Lr)

    for p, q, name in [(x, fx, "x"), (y, fy, "y")]:
        b.append(f'<line x1="{p[0]}" y1="{p[1]}" x2="{q[0]:.1f}" y2="{q[1]:.1f}" stroke="{LIGHT}" stroke-width="1.2" stroke-dasharray="4 3" marker-end="url(#ar-d)"/>')
        b.append(f'<circle cx="{p[0]}" cy="{p[1]}" r="4.5" fill="{INK}"/>')
        b.append(f'<circle cx="{q[0]:.1f}" cy="{q[1]:.1f}" r="4.2" fill="{RED}"/>')
        b.append(t(p[0] - 12, p[1] - 8, name, 12.5, "end", INK, "600"))
        b.append(t(q[0] + 9, q[1] + 4, "Φ(" + name + ")", 11.5, "start", RED))

    b.append(f'<line x1="{x[0]}" y1="{x[1]}" x2="{y[0]}" y2="{y[1]}" stroke="{INK}" stroke-width="1.7"/>')
    b.append(f'<line x1="{fx[0]:.1f}" y1="{fx[1]:.1f}" x2="{fy[0]:.1f}" y2="{fy[1]:.1f}" stroke="{RED}" stroke-width="1.7"/>')
    b.append(t(212, 272, "‖x − y‖", 11.5, "end", INK))
    # 像的距离：引出到小圆下方
    b.append(f'<line x1="{(fx[0]+fy[0])/2:.1f}" y1="{(fx[1]+fy[1])/2:.1f}" x2="346" y2="374" stroke="{RED}" stroke-width="0.9" stroke-dasharray="3 3"/>')
    b.append(t(352, 390, "‖Φ(x) − Φ(y)‖", 11.5, "start", RED))

    b.append(f'<circle cx="{c2[0]-16}" cy="{c2[1]-16}" r="4.5" fill="{GREEN}"/>')
    b.append(t(c2[0] - 6, c2[1] - 22, "x*", 12.5, "start", GREEN, "600"))

    b.append(t(48, 406, "像落在 D₀ 里面（自映射），距离又缩到 L 倍——所以不动点唯一，且任意初值都收敛", 12, "start", DIM))
    b.append("</svg>")
    return "".join(b)


save(os.path.join("第5章-解线性方程组的直接法", "figures", "norms-unit-balls.svg"), fig_norm_balls())
save(os.path.join("第5章-解线性方程组的直接法", "figures", "ill-conditioned-lines.svg"), fig_ill_cond())
save(os.path.join("第6章-解线性方程组的迭代法", "figures", "cg-vs-sd.svg"), fig_cg())
save(os.path.join("第7章-非线性方程", "figures", "fixed-point-cobweb.svg"), fig_cobweb())
save(os.path.join("第7章-非线性方程", "figures", "contraction-map.svg"), fig_contraction())
