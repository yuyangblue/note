# -*- coding: utf-8 -*-
"""第二批插图 v2：只画「结构 / 过程 / 几何映射」。"""
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
FILL_PLANE = "#eef3fd"
FILL_U = "#e6edfb"
FILL_L = "#fbeade"
FONT = "'-apple-system','Segoe UI','Microsoft YaHei',sans-serif"


def head(w, h):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
        f'width="{w}" height="{h}" style="max-width:100%;height:auto" '
        f'font-family="{FONT}">'
        f'<rect width="{w}" height="{h}" fill="#ffffff"/>'
        '<defs>'
        f'<marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{INK}"/></marker>'
        f'<marker id="ar-b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{BLUE}"/></marker>'
        f'<marker id="ar-r" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{RED}"/></marker>'
        f'<marker id="ar-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{GREEN}"/></marker>'
        f'<marker id="ar-d" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{DIM}"/></marker>'
        '</defs>'
    )


def esc(s):
    s = str(s)
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def t(x, y, s, size=13, anchor="start", fill=INK, weight="400"):
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" fill="{fill}" '
            f'font-weight="{weight}" text-anchor="{anchor}">{esc(s)}</text>')


def tsup(x, y, parts, size=13, anchor="start", fill=INK, weight="400"):
    out = (f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" fill="{fill}" '
           f'font-weight="{weight}" text-anchor="{anchor}">')
    for s, sup in parts:
        if sup:
            out += (f'<tspan dy="{-size*0.36:.1f}" font-size="{size*0.72:.1f}">{esc(s)}</tspan>'
                    f'<tspan dy="{size*0.36:.1f}" font-size="{size}">\u200b</tspan>')
        else:
            out += f'<tspan>{esc(s)}</tspan>'
    return out + '</text>'


def save(rel, body):
    p = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w", encoding="utf-8").write(body + "</svg>")
    print("%-56s %6.1f KB" % (rel, os.path.getsize(p) / 1024))


# ---------------------------------------------------------------- 1 正交投影
def fig_projection():
    W, H = 780, 440
    b = [head(W, H)]
    b.append(t(40, 44, "最小二乘就是把 b 投影到列空间上", 16, "start", INK, "600"))
    b.append(t(40, 68, "残差 r 垂直于整个平面——这就是法方程 AᵀAx = Aᵀb 的几何含义", 12, "start", DIM))

    O = (175.0, 318.0)
    e1 = (238.0, 66.0)
    e2 = (92.0, -86.0)
    P1 = (O[0] + e1[0], O[1] + e1[1])
    P12 = (P1[0] + e2[0], P1[1] + e2[1])
    P2 = (O[0] + e2[0], O[1] + e2[1])

    b.append(f'<polygon points="{O[0]:.1f},{O[1]:.1f} {P1[0]:.1f},{P1[1]:.1f} '
             f'{P12[0]:.1f},{P12[1]:.1f} {P2[0]:.1f},{P2[1]:.1f}" '
             f'fill="{FILL_PLANE}" stroke="{LIGHT}" stroke-width="1.4"/>')

    p = (O[0] + 0.46 * e1[0] + 0.40 * e2[0], O[1] + 0.46 * e1[1] + 0.40 * e2[1])
    bb = (p[0], p[1] - 158.0)

    b.append(f'<line x1="{bb[0]:.1f}" y1="{bb[1]:.1f}" x2="{p[0]:.1f}" y2="{p[1]:.1f}" '
             f'stroke="{RED}" stroke-width="2" stroke-dasharray="7 5"/>')
    b.append(f'<circle cx="{bb[0]:.1f}" cy="{bb[1]:.1f}" r="4.5" fill="{INK}"/>')
    b.append(f'<line x1="{O[0]:.1f}" y1="{O[1]:.1f}" x2="{bb[0]:.1f}" y2="{bb[1]:.1f}" '
             f'stroke="{INK}" stroke-width="2" marker-end="url(#ar)"/>')
    b.append(f'<line x1="{O[0]:.1f}" y1="{O[1]:.1f}" x2="{p[0]:.1f}" y2="{p[1]:.1f}" '
             f'stroke="{BLUE}" stroke-width="2" marker-end="url(#ar-b)"/>')

    # 直角标记（沿 e1 方向 与 残差方向）
    ux, uy = 16.0, 16.0 * 66.0 / 238.0
    b.append(f'<path d="M {p[0]+ux:.1f} {p[1]+uy:.1f} L {p[0]+ux:.1f} {p[1]+uy-16:.1f} '
             f'L {p[0]:.1f} {p[1]-16:.1f}" fill="none" stroke="{RED}" stroke-width="1.4"/>')

    b.append(f'<circle cx="{p[0]:.1f}" cy="{p[1]:.1f}" r="4.5" fill="{BLUE}"/>')
    b.append(f'<circle cx="{O[0]:.1f}" cy="{O[1]:.1f}" r="4" fill="{INK}"/>')

    b.append(t(O[0] - 10, O[1] + 6, "O", 13, "end", INK, "600"))
    b.append(t(bb[0] + 10, bb[1] + 2, "b", 15, "start", INK, "600"))
    b.append(t(p[0] + 10, p[1] + 22, "Ax̂", 14, "start", BLUE, "600"))
    b.append(t(p[0] + 14, (p[1] + bb[1]) / 2, "r = b − Ax̂", 13, "start", RED, "600"))
    b.append(t(432, 300, "col(A)", 14, "start", BLUE, "600"))

    x0 = 545
    b.append(t(x0, 152, "r ⊥ col(A)", 15, "start", RED, "600"))
    b.append(t(x0, 184, "r 与 A 的每一列都正交：", 12.5, "start", INK))
    b.append(t(x0, 206, "aᵢᵀ(b − Ax̂) = 0,  i = 1…n", 12.5, "start", INK))
    b.append(t(x0, 244, "合起来就是法方程：", 12.5, "start", INK))
    b.append(tsup(x0, 270, [("A", 0), ("T", 1), ("A", 0), ("x", 0), (" = A", 0), ("T", 1), ("b", 0)],
                  14, "start", BLUE, "600"))
    b.append(t(x0, 312, "Ax̂ 是 b 在列空间上的投影，", 12, "start", DIM))
    b.append(t(x0, 330, "b − Ax̂ 是垂直的那部分。", 12, "start", DIM))
    b.append(t(x0, 362, "A 不满秩时投影点仍唯一，", 12, "start", DIM))
    b.append(t(x0, 380, "但写成列组合的方式不唯一。", 12, "start", DIM))
    save(os.path.join("第3章-最小二乘问题", "figures", "lsq-projection.svg"), "\n".join(b))


# ---------------------------------------------------------------- 2 LU 逐层推进
def fig_lu_order():
    W, H = 780, 500
    b = [head(W, H)]
    b.append(t(40, 44, "Doolittle 分解：每个元素在第几步被算出来", 16, "start", INK, "600"))
    b.append(t(40, 68, "格中数字 = min(i, j)：同一数字的格子在同一步算出，沿左上→右下的 L 形推进", 12, "start", DIM))

    n, cell = 5, 58
    X0, Y0 = 56, 108

    def cx(j):
        return X0 + (j - 1) * cell + cell / 2

    def cy(i):
        return Y0 + (i - 1) * cell + cell / 2

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            r = min(i, j)
            fill = FILL_U if j >= i else FILL_L
            b.append(f'<rect x="{X0+(j-1)*cell}" y="{Y0+(i-1)*cell}" width="{cell}" height="{cell}" '
                     f'fill="{fill}" stroke="#ffffff" stroke-width="1.6"/>')
            col = BLUE if j >= i else RED
            b.append(t(cx(j), cy(i) + 7, str(r), 18, "middle", col, "600"))

    b.append(f'<rect x="{X0}" y="{Y0}" width="{n*cell}" height="{n*cell}" fill="none" '
             f'stroke="{LIGHT}" stroke-width="1.4"/>')

    step = 3
    for j in range(step, n + 1):
        b.append(f'<rect x="{X0+(j-1)*cell+1}" y="{Y0+(step-1)*cell+1}" width="{cell-2}" height="{cell-2}" '
                 f'fill="none" stroke="{RED}" stroke-width="2.4"/>')
    for i in range(step + 1, n + 1):
        b.append(f'<rect x="{X0+(step-1)*cell+1}" y="{Y0+(i-1)*cell+1}" width="{cell-2}" height="{cell-2}" '
                 f'fill="none" stroke="{RED}" stroke-width="2.4"/>')

    dx, dy = cx(step), cy(step)
    b.append(f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="21" fill="none" stroke="{GREEN}" stroke-width="2.2"/>')
    b.append(f'<line x1="{dx:.1f}" y1="{dy+23:.1f}" x2="{dx:.1f}" y2="{cy(step+1)-cell/2+18:.1f}" '
             f'stroke="{GREEN}" stroke-width="1.6" stroke-dasharray="3 3" marker-end="url(#ar-g)"/>')

    x0 = 386
    b.append(t(x0, 122, "第 r 步做两件事", 13.5, "start", INK, "600"))
    b.append(t(x0, 148, "· U 第 r 行：j = r … n", 12.5, "start", BLUE))
    b.append(t(x0, 170, "· L 第 r 列：i = r+1 … n", 12.5, "start", RED))
    b.append(t(x0, 202, "两件事拼成一个 L 形，手算", 12, "start", DIM))
    b.append(t(x0, 220, "就是斜着一层层往右下推。", 12, "start", DIM))

    b.append(t(x0, 256, "顺序不能颠倒", 13.5, "start", RED, "600"))
    b.append(t(x0, 280, "l_ir 要除以 u_rr，所以同一步里", 12, "start", INK))
    b.append(t(x0, 298, "对角元 u_rr 必须先算，再往", 12, "start", INK))
    b.append(t(x0, 316, "下算这一列（绿圈 → 下方）。", 12, "start", INK))

    b.append(t(x0, 352, "浅蓝格属 U（j ≥ i）", 12, "start", BLUE))
    b.append(t(x0, 372, "浅橙格属 L（i > j）", 12, "start", RED))
    b.append(t(x0, 404, "对角线上 l_ii = 1 不存。", 12, "start", DIM))

    b.append(t(56, 452, "A = LU 的每个位置只被用到一次，所以 L、U 可以直接覆盖 A 的存储。", 12.5, "start", INK))
    b.append(t(56, 476, "数字相同的格子共享同一批已算好的数据，这正是它比先做消去再记乘数更省的原因。", 12, "start", DIM))
    save(os.path.join("第5章-解线性方程组的直接法", "figures", "lu-order.svg"), "\n".join(b))


# ---------------------------------------------------------------- 3 三对角结构
def fig_tridiag():
    W, H = 720, 580
    b = [head(W, H)]
    b.append(t(40, 44, "差分离散化：网格点怎么变成三对角矩阵", 16, "start", INK, "600"))
    b.append(t(40, 68, "每个内点对应一行；一个点只与左右邻居耦合，所以每行只有三个非零元", 12, "start", DIM))

    N, cell = 5, 62
    MX, MY = 250, 196
    gy = 112.0

    def colx(j):
        return MX + (j - 1) * cell + cell / 2

    def nodex(i):
        if i == 0:
            return colx(1) - cell
        if i == N:
            return colx(4) + cell
        return colx(i)

    b.append(f'<line x1="{nodex(0)-24:.1f}" y1="{gy}" x2="{nodex(N)+24:.1f}" y2="{gy}" '
             f'stroke="{LIGHT}" stroke-width="1.6"/>')
    for i in range(N + 1):
        x = nodex(i)
        if i in (0, N):
            b.append(f'<circle cx="{x:.1f}" cy="{gy}" r="6" fill="#ffffff" stroke="{DIM}" stroke-width="1.8"/>')
        else:
            b.append(f'<circle cx="{x:.1f}" cy="{gy}" r="5.5" fill="{INK}"/>')
        b.append(t(x, gy - 16, f"x{i}", 12.5, "middle", INK if i not in (0, N) else DIM, "600"))
    b.append(t(nodex(0), gy + 26, "0", 12, "middle", DIM))
    b.append(t(nodex(N), gy + 26, "0", 12, "middle", DIM))
    b.append(t((nodex(0) + nodex(1)) / 2, gy + 26, "h", 12, "middle", DIM))

    for j in range(1, 5):
        x = colx(j)
        b.append(f'<line x1="{x:.1f}" y1="{gy+10}" x2="{x:.1f}" y2="{MY-20}" stroke="{BLUE}" '
                 f'stroke-width="1.1" stroke-dasharray="3 4" opacity="0.5"/>')
        b.append(t(x, MY - 24, f"u{j}", 12, "middle", BLUE, "600"))

    for i in range(1, 5):
        for j in range(1, 5):
            x = MX + (j - 1) * cell
            y = MY + (i - 1) * cell
            # 先铺一层空格底纹，保证整张矩阵的网格看得见
            b.append(f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" fill="#fbfcfd" '
                     f'stroke="#d5dae0" stroke-width="1"/>')
            if abs(i - j) <= 1:
                val = "2" if i == j else "−1"
                fill = FILL_U if i == j else "#f4f6f8"
                b.append(f'<rect x="{x+1}" y="{y+1}" width="{cell-2}" height="{cell-2}" fill="{fill}" '
                         f'stroke="#cfd6dd" stroke-width="1"/>')
                b.append(t(colx(j), y + cell / 2 + 5, val, 13, "middle",
                           INK if i == j else DIM, "600" if i == j else "400"))

    hi = 2
    y = MY + (hi - 1) * cell
    b.append(f'<rect x="{MX+1}" y="{y+1}" width="{4*cell-2}" height="{cell-2}" fill="none" '
             f'stroke="{RED}" stroke-width="2.4"/>')
    for i in range(1, 5):
        b.append(t(MX - 14, MY + (i - 1) * cell + cell / 2 + 5, f"{i}", 12, "end", DIM))

    b.append(t(40, 500, "稀疏性不是偶然：差分格式只涉及 xᵢ₋₁、xᵢ、xᵢ₊₁ 三个未知量，矩阵就只在这三列上有非零元。", 12.5, "start", INK))
    b.append(t(40, 522, "第 1 行与最后一行只剩两个非零元——边界值 u₀ = u_N = 0 被移到右端，不进矩阵。", 12, "start", DIM))
    b.append(t(40, 544, "节点再多，每行的非零元还是三个；这正是追赶法 O(N)、迭代法每轮 O(N) 的来源。", 12, "start", DIM))
    save(os.path.join("第6章-解线性方程组的迭代法", "figures", "tridiag-structure.svg"), "\n".join(b))


# ---------------------------------------------------------------- 4 Aitken 序列
def fig_aitken():
    W, H = 820, 556
    b = [head(W, H)]
    b.append(t(40, 44, "Aitken 加速：三个原迭代值，换一个几乎落在根上的值", 16, "start", INK, "600"))
    b.append(t(40, 68, "cos 迭代 x₀ = 1 的真实数据。上排是原序列（震荡逼近），下排是逐组外推的结果", 12, "start", DIM))

    xs = [1.00000, 0.54030, 0.85755, 0.65429, 0.79348, 0.70137, 0.76396, 0.72210, 0.75042]
    xbar = [0.72800, 0.73367, 0.73690, 0.73805, 0.73864, 0.738875, 0.738992]
    xstar = 0.7390851
    vmin, vmax = 0.50, 1.02
    TOP, BOT = 118.0, 302.0
    DROP = 175.0

    def KX(k):
        return 118.0 + k * 78.0

    def VY(v):
        return BOT - (v - vmin) / (vmax - vmin) * (BOT - TOP)

    b.append(f'<line x1="{KX(0)-38:.1f}" y1="{BOT+18:.1f}" x2="{KX(8)+26:.1f}" y2="{BOT+18:.1f}" '
             f'stroke="{LIGHT}" stroke-width="1.2"/>')
    for k in range(9):
        b.append(t(KX(k), BOT + 40, str(k), 11.5, "middle", DIM))
    b.append(t(KX(8) + 22, BOT + 40, "k", 11.5, "middle", DIM))

    ystar = VY(xstar)
    b.append(f'<line x1="{KX(0)-38:.1f}" y1="{ystar:.1f}" x2="{KX(8)+30:.1f}" y2="{ystar:.1f}" '
             f'stroke="{GREEN}" stroke-width="1.5" stroke-dasharray="6 4"/>')
    b.append(t(KX(0) - 42, ystar + 4, "x* = 0.73909", 11.5, "end", GREEN, "600"))

    pts = [(KX(k), VY(v)) for k, v in enumerate(xs)]
    d = "M " + " L ".join(f"{x:.1f} {y:.1f}" for x, y in pts)
    b.append(f'<path d="{d}" fill="none" stroke="{BLUE}" stroke-width="2.1"/>')
    for (x, y) in pts:
        b.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4.2" fill="{BLUE}"/>')

    b.append(t(KX(0) + 12, VY(1.0) - 4, "x₀", 11.5, "start", BLUE))
    b.append(t(KX(1) + 10, VY(0.5403) + 6, "x₁", 11.5, "start", BLUE))

    # 下排：加速值
    ylow = ystar + DROP
    b.append(f'<line x1="{KX(0)-38:.1f}" y1="{ylow:.1f}" x2="{KX(8)+30:.1f}" y2="{ylow:.1f}" '
             f'stroke="{GREEN}" stroke-width="1.2" stroke-dasharray="4 4" opacity="0.6"/>')
    b.append(t(KX(0) - 42, ylow + 4, "x*（同高）", 11, "end", GREEN))

    bpts = []
    for k, v in enumerate(xbar):
        x = KX(k) + 39
        y = VY(v) + DROP
        bpts.append((x, y))
    d2 = "M " + " L ".join(f"{x:.1f} {y:.1f}" for x, y in bpts)
    b.append(f'<path d="{d2}" fill="none" stroke="{RED}" stroke-width="1.8" stroke-dasharray="5 3"/>')
    for x, y in bpts:
        b.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.8" fill="{RED}"/>')

    # 两处示范：三点 -> 一点
    for k, lab in [(0, "x̄₀")]:
        gx = [KX(k), KX(k + 1), KX(k + 2)]
        gy_ = max(VY(xs[k]), VY(xs[k + 1]), VY(xs[k + 2])) + 18
        b.append(f'<path d="M {gx[0]:.1f} {gy_-8:.1f} L {gx[0]:.1f} {gy_:.1f} L {gx[2]:.1f} {gy_:.1f} L {gx[2]:.1f} {gy_-8:.1f}" '
                 f'fill="none" stroke="{RED}" stroke-width="1.2" opacity="0.75"/>')
        b.append(f'<line x1="{(gx[0]+gx[2])/2:.1f}" y1="{gy_:.1f}" x2="{KX(k)+39:.1f}" y2="{ylow-10:.1f}" '
                 f'stroke="{RED}" stroke-width="1.2" opacity="0.75" marker-end="url(#ar-r)"/>')
        b.append(t(KX(k) + 39, ylow + 22, lab, 11.5, "middle", RED, "600"))
    # 第 7 组只保留下方数值标签

    b.append(t(KX(6) + 39, ylow + 40, "x̄₆ = 0.73899", 11.5, "middle", RED, "600"))

    b.append(t(40, 476, "上排每个 xₖ 都在 x* 两侧来回跳，收敛比例稳定在 0.67 左右；下排的外推值几乎一次就贴到 x*。", 12.5, "start", INK))
    b.append(t(40, 500, "三个数换十二步：误差从 1.13×10⁻² 直接到 9.3×10⁻⁵。下排点之间没有递推关系，各自独立由上面相邻三个算出。", 12, "start", DIM))
    b.append(t(40, 524, "纵轴尺度与上排相同（整体下移），所以下排看起来几乎是一条水平线，这本身就是加速的效果。", 12, "start", DIM))
    save(os.path.join("第7章-非线性方程", "figures", "aitken-sequence.svg"), "\n".join(b))


# ---------------------------------------------------------------- 5 谱半径圆盘
def fig_spectral():
    W, H = 720, 470
    b = [head(W, H)]
    b.append(t(40, 44, "ρ(B) < 1：所有特征值都落在单位圆内", 16, "start", INK, "600"))
    b.append(t(40, 68, "ρ 是「离圆心最远的那个模」，决定收敛的是它，不是某个范数", 12, "start", DIM))

    C = (372.0, 252.0)
    S = 72.0

    def P(re, im):
        return (C[0] + re * S, C[1] - im * S)

    b.append(f'<line x1="{C[0]-196:.1f}" y1="{C[1]}" x2="{C[0]+196:.1f}" y2="{C[1]}" stroke="{LIGHT}" stroke-width="1.2"/>')
    b.append(f'<line x1="{C[0]}" y1="{C[1]-150:.1f}" x2="{C[0]}" y2="{C[1]+150:.1f}" stroke="{LIGHT}" stroke-width="1.2"/>')
    b.append(t(C[0] + 192, C[1] + 20, "Re", 11.5, "end", DIM))
    b.append(t(C[0] + 10, C[1] - 140, "Im", 11.5, "start", DIM))

    b.append(f'<circle cx="{C[0]:.1f}" cy="{C[1]:.1f}" r="{S:.1f}" fill="none" stroke="{DIM}" '
             f'stroke-width="1.6" stroke-dasharray="7 5"/>')
    b.append(t(C[0] - 0.74 * S, C[1] - 0.68 * S, "|λ| = 1", 12, "end", DIM))

    px, py = P(0.3592, 0)
    b.append(f'<line x1="{C[0]}" y1="{C[1]}" x2="{px:.1f}" y2="{py:.1f}" stroke="{BLUE}" stroke-width="1.6" opacity="0.55"/>')

    def dot(re, im, col, r=5.5):
        x, y = P(re, im)
        b.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{col}"/>')

    for re, im in [(0.3592, 0.0), (-0.15, 0.20), (-0.15, -0.20)]:
        dot(re, im, BLUE)
    b.append(t(px, py + 34, "ρ ≈ 0.36", 12, "middle", BLUE, "600"))

    for re in (2.449, -2.449):
        dot(re, 0, RED)
    b.append(t(P(2.449, 0)[0] - 2, C[1] - 14, "ρ = √6 ≈ 2.45", 12, "middle", RED, "600"))

    for re, im in [(0.97, 0.0), (0.60, 0.75), (0.60, -0.75)]:
        dot(re, im, "#aab3bd", 4.5)
    b.append(t(P(0.60, 0.75)[0] + 10, P(0.60, 0.75)[1] + 4, "ρ → 1", 11.5, "start", DIM, "600"))

    b.append(t(36, 150, "收敛（定理 5）", 12.5, "start", BLUE, "600"))
    b.append(t(36, 170, "全部特征值在圆内", 11.5, "start", DIM))
    b.append(t(36, 206, "发散", 12.5, "start", RED, "600"))
    b.append(t(36, 226, "有一个在圆外，Bᵏ 不趋于零", 11.5, "start", DIM))
    b.append(t(36, 262, "收敛但极慢", 12.5, "start", DIM, "600"))
    b.append(t(36, 282, "贴着圆周，误差几乎不缩", 11.5, "start", DIM))
    b.append(t(36, 330, "ρ(B) = max|λᵢ|。判据只看这颗", 11.5, "start", DIM))
    b.append(t(36, 348, "最远的点，不看 ‖B‖。", 11.5, "start", DIM))

    b.append(t(40, 452, "ρ < 1 ⇔ Bᵏ → 0 ⇔ 任意初值都收敛；只要有一个特征值跑到圆外，迭代就发散。", 12, "start", INK))
    save(os.path.join("第6章-解线性方程组的迭代法", "figures", "spectral-radius.svg"), "\n".join(b))


def fig_cond():
    W, H = 760, 400
    b = [head(W, H)]
    b.append(t(40, 44, "条件数就是「单位圆被拉成多扁的椭圆」", 16, "start", INK, "600"))
    b.append(t(40, 68, "同一个 A 作用在圆周上：最长方向拉 3 倍，最短方向拉 1 倍", 12, "start", DIM))

    C1 = (186.0, 208.0)
    R = 84.0
    b.append(f'<circle cx="{C1[0]}" cy="{C1[1]}" r="{R}" fill="{FILL_PLANE}" stroke="{DIM}" '
             f'stroke-width="1.8" stroke-dasharray="6 4"/>')
    b.append(f'<line x1="{C1[0]-R-14}" y1="{C1[1]}" x2="{C1[0]+R+14}" y2="{C1[1]}" stroke="{LIGHT}" stroke-width="1"/>')
    b.append(f'<line x1="{C1[0]}" y1="{C1[1]-R-14}" x2="{C1[0]}" y2="{C1[1]+R+14}" stroke="{LIGHT}" stroke-width="1"/>')
    b.append(t(C1[0], C1[1] - R - 18, "‖x‖₂ = 1", 12.5, "middle", DIM, "600"))

    b.append(f'<line x1="{C1[0]+R+20:.1f}" y1="{C1[1]:.1f}" x2="{C1[0]+R+100:.1f}" y2="{C1[1]:.1f}" '
             f'stroke="{INK}" stroke-width="2" marker-end="url(#ar)"/>')
    b.append(t(C1[0] + R + 60, C1[1] - 12, "A", 15, "middle", INK, "600"))

    C2 = (512.0, 208.0)
    a, bb2 = 116.0, 38.0
    b.append(f'<ellipse cx="{C2[0]}" cy="{C2[1]}" rx="{a}" ry="{bb2}" fill="{FILL_U}" stroke="{BLUE}" stroke-width="2"/>')

    b.append(f'<line x1="{C2[0]-a:.1f}" y1="{C2[1]:.1f}" x2="{C2[0]+a:.1f}" y2="{C2[1]:.1f}" '
             f'stroke="{RED}" stroke-width="1.6" marker-start="url(#ar-r)" marker-end="url(#ar-r)"/>')
    b.append(f'<line x1="{C2[0]:.1f}" y1="{C2[1]-bb2:.1f}" x2="{C2[0]:.1f}" y2="{C2[1]+bb2:.1f}" '
             f'stroke="{GREEN}" stroke-width="1.6" marker-start="url(#ar-g)" marker-end="url(#ar-g)"/>')

    b.append(t(C2[0], C2[1] + bb2 + 32, "σmax = 3（长半轴）", 12, "middle", RED, "600"))
    b.append(t(C2[0], C2[1] - bb2 - 14, "σmin = 1（短半轴）", 12, "middle", GREEN, "600"))

    b.append(t(40, 320, "cond₂(A) = σmax / σmin = 长短轴比 = 3", 14, "start", INK, "600"))
    b.append(t(40, 346, "椭圆越扁，cond 越大。求逆相当于把椭圆缩回圆，短轴方向被放大 1/σmin 倍——", 12, "start", DIM))
    b.append(t(40, 368, "于是 b 上一点小扰动，在短轴方向上就被成倍放大到解里去。", 12, "start", DIM))
    save(os.path.join("第5章-解线性方程组的直接法", "figures", "cond-ellipse.svg"), "\n".join(b))


if __name__ == "__main__":
    fig_projection()
    fig_lu_order()
    fig_tridiag()
    fig_aitken()
    fig_spectral()
    fig_cond()
