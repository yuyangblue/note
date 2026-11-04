# -*- coding: utf-8 -*-
"""幂法的方向转向：两组 |λ2/λ1| 的真实迭代轨迹。v2：精简标注、加步数刻度。"""
import math, os, sys
sys.stdout.reconfigure(encoding="utf-8")

ROOT = r"D:\29469\Documents\notes\计算方法与优化"
INK, DIM, LIGHT, GRID = "#1f2933", "#6b7785", "#9aa5b1", "#e4e7eb"
RED, BLUE, GREEN = "#c2410c", "#1d4ed8", "#047857"
FONT = "'-apple-system','Segoe UI','Microsoft YaHei',sans-serif"


def head(w, h):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
        f'width="{w}" height="{h}" style="max-width:100%;height:auto" '
        f'font-family="{FONT}">'
        f'<rect width="{w}" height="{h}" fill="#ffffff"/>'
        '<defs>'
        f'<marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{INK}"/></marker>'
        f'<marker id="ar-d" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{DIM}"/></marker>'
        '</defs>'
    )


def esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def t(x, y, s, size=13, anchor="start", fill=INK, weight="400"):
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" fill="{fill}" '
            f'font-weight="{weight}" text-anchor="{anchor}">{esc(s)}</text>')


def build():
    W, H = 780, 486
    b = [head(W, H)]
    CX, CY = 194.0, 262.0
    R0, DR = 56.0, 33.0

    def P(k, deg):
        r = R0 + k * DR
        a = math.radians(deg)
        return (CX + r * math.cos(a), CY - r * math.sin(a))

    # ---- 参考射线 ----
    for deg, ln, lab in [(45, 214, "x₁"), (-45, 146, "x₂")]:
        a = math.radians(deg)
        x2, y2 = CX + ln * math.cos(a), CY - ln * math.sin(a)
        b.append(f'<line x1="{CX}" y1="{CY}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{LIGHT}" '
                 f'stroke-width="1.4" stroke-dasharray="6 5"/>')
        b.append(t(CX + (ln + 10) * math.cos(a), CY - (ln + 10) * math.sin(a) + 4,
                   lab, 13, "start", DIM, "600"))

    b.append(t(CX - 12, CY + 5, "O", 12, "end", DIM))
    b.append(t(CX - 14, CY + 44, "半径向外 = 步数增加", 10.5, "end", LIGHT))

    # ---- 两组轨迹 ----
    series = [(0.4, BLUE), (1.6, RED)]
    for l2, col in series:
        pts = []
        for k in range(5):
            a, c = 2.0 ** k, l2 ** k
            ang = math.degrees(math.atan2(a - c, a + c))
            pts.append(P(k, ang))
        d = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
        b.append(f'<polyline points="{d}" fill="none" stroke="{col}" stroke-width="1.6" opacity="0.42"/>')
        for i, (x, y) in enumerate(pts):
            r = 7.0 if i == 0 else 5.0
            b.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{col}"/>')

    # 起点标注（共用）
    b.append(t(CX + R0 - 12, CY - 16, "v⁽⁰⁾", 11.5, "middle", INK, "600"))
    # 两个终点
    bx, by = P(4, 44.91)
    b.append(t(bx + 10, by + 13, "v⁽⁴⁾", 11.5, "start", BLUE, "600"))
    rx, ry = P(4, 22.73)
    b.append(t(rx + 13, ry + 4, "v⁽⁴⁾", 11.5, "start", RED, "600"))

    # ---- 右栏 ----
    X0 = 496
    b.append(t(X0, 88, "两种比值，同一个初值", 14.5, "start", INK, "600"))
    b.append(t(X0, 111, "都从 (1, 0) 出发，λ₁ = 2，各走四步", 11.5, "start", DIM))

    rows = [
        (BLUE, "|λ₂/λ₁| = 0.20", "45° → 11.3° → 2.3° → 0.46°", "三步就贴到 x₁"),
        (RED, "|λ₂/λ₁| = 0.80", "45° → 38.7° → 32.6° → 27.1°", "二十步才够"),
    ]
    y = 152
    for col, name, seq, tail in rows:
        b.append(f'<rect x="{X0}" y="{y - 13}" width="3.5" height="50" fill="{col}"/>')
        b.append(t(X0 + 13, y, name, 12.5, "start", col, "600"))
        b.append(t(X0 + 13, y + 20, seq, 10.8, "start", DIM))
        b.append(t(X0 + 13, y + 37, tail, 11, "start", DIM))
        y += 78

    b.append(t(X0, 330, "角度差每步都乘同一个比值", 12, "start", INK, "600"))
    b.append(t(X0, 350, "这就是「指数收敛」的几何样子：", 11.5, "start", DIM))
    b.append(t(X0, 368, "不是匀速转，是越近越慢。", 11.5, "start", DIM))
    b.append(t(X0, 400, "转到多近算停，取决于要几位有效数字——", 11.5, "start", DIM))
    b.append(t(X0, 418, "0.8²⁰ ≈ 0.012，二十步才把 45° 压到半度。", 11.5, "start", DIM))

    # ---- 底部 ----
    b.append(t(40, 440, "半径只代表步数，不代表向量长度：幂法的长度每步乘 |λ₁|，先归一化，图上才只剩方向。", 12, "start", INK))
    b.append(t(40, 462, "所以「收敛」说的是方向；λ₁ 的模由长度给出，符号由 §3.2 的符号函数给出。", 12, "start", DIM))

    out = os.path.join(ROOT, "第8章-矩阵特征值", "figures", "power-rotation.svg")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w", encoding="utf-8").write("\n".join(b) + "\n</svg>")
    print("已写", out, os.path.getsize(out), "B")


build()
