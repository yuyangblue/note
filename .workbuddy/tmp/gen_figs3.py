# -*- coding: utf-8 -*-
"""第三批插图：局部收敛的邻域构造 + Cholesky 省一半。只画「结构 / 几何约束」。"""
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
FILL_U = "#e6edfb"
FILL_L = "#fbeade"
FILL_GREY = "#f4f6f8"
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


def save(rel, body):
    p = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w", encoding="utf-8").write(body + "</svg>")
    print("%-58s %6.1f KB" % (rel, os.path.getsize(p) / 1024))


# ------------------------------------------------- 1 局部收敛的邻域构造
def fig_neighborhood():
    W, H = 780, 440
    b = [head(W, H)]
    b.append(t(40, 44, "局部收敛：把单点上的 |g′(x*)| < 1 换成一个邻域", 16, "start", INK, "600"))
    b.append(t(40, 68, "第一步就是给 |g′| 画一条水平线 L，要求整段邻域都被压在下面", 12, "start", DIM))

    # 坐标系：x -> px, |g'| -> py
    X0, X1 = 96.0, 700.0
    Y0, Y1 = 116.0, 322.0          # 画布内的绘图区（y 轴向上）
    VMIN, VMAX = 0.0, 1.15

    def PX(x):
        return X0 + (x - 0.0) / 10.0 * (X1 - X0)

    def PY(v):
        return Y1 - (v - VMIN) / (VMAX - VMIN) * (Y1 - Y0)

    # 轴
    b.append(f'<line x1="{X0:.1f}" y1="{Y1:.1f}" x2="{X1:.1f}" y2="{Y1:.1f}" stroke="{LIGHT}" stroke-width="1.2"/>')
    b.append(f'<line x1="{X0:.1f}" y1="{Y0:.1f}" x2="{X0:.1f}" y2="{Y1:.1f}" stroke="{LIGHT}" stroke-width="1.2"/>')
    b.append(t(X1, Y1 + 22, "x", 12, "end", DIM))
    b.append(t(X0 - 12, PY(1.0) + 4, "1", 11.5, "end", DIM))
    b.append(t(X0 - 14, Y0 - 8, "|g′(x)|", 11.5, "end", DIM))

    # y = 1 这条「安全线」
    b.append(f'<line x1="{X0:.1f}" y1="{PY(1.0):.1f}" x2="{X1:.1f}" y2="{PY(1.0):.1f}" '
             f'stroke="{LIGHT}" stroke-width="1" stroke-dasharray="3 4"/>')
    b.append(t(X1 - 4, PY(1.0) - 8, "1（不能碰）", 11, "end", DIM))

    # |g'| 曲线（示意）：连续、起伏
    pts = [(0.0, 0.92), (1.6, 0.74), (3.0, 0.55), (4.2, 0.44), (5.0, 0.40),
           (5.8, 0.43), (7.0, 0.52), (8.4, 0.67), (10.0, 0.88)]
    # 用二次贝塞尔做平滑
    d = f'M {PX(pts[0][0]):.1f} {PY(pts[0][1]):.1f}'
    for i in range(len(pts) - 1):
        x0, y0 = pts[i]
        x1, y1 = pts[i + 1]
        mx = (x0 + x1) / 2
        my = (y0 + y1) / 2
        d += (f' Q {PX(mx):.1f} {PY(my):.1f} {PX(x1):.1f} {PY(y1):.1f}')
    b.append(f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="2.2" stroke-linejoin="round"/>')

    # 邻域 [3, 7]
    XS, XE = 3.0, 7.0
    L = 0.60
    # 邻域内曲线下方的填色
    b.append(f'<rect x="{PX(XS):.1f}" y="{PY(L):.1f}" width="{PX(XE)-PX(XS):.1f}" '
             f'height="{Y1-PY(L):.1f}" fill="{FILL_U}" opacity="0.85"/>')
    # 水平线 L
    b.append(f'<line x1="{X0:.1f}" y1="{PY(L):.1f}" x2="{X1:.1f}" y2="{PY(L):.1f}" '
             f'stroke="{RED}" stroke-width="1.8" stroke-dasharray="7 5"/>')
    b.append(t(X1 - 2, PY(L) + 18, "L = |g′(x*)| + ε = 0.60", 11.5, "end", RED, "600"))

    # 竖线
    for x, lab in [(XS, "x* − δ"), (5.0, "x*"), (XE, "x* + δ")]:
        c = RED if x == 5.0 else DIM
        b.append(f'<line x1="{PX(x):.1f}" y1="{PY(L):.1f}" x2="{PX(x):.1f}" y2="{Y1:.1f}" '
                 f'stroke="{c}" stroke-width="1.3" stroke-dasharray="4 4"/>')
    b.append(t(PX(3.0), Y1 + 20, "x* − δ", 11.5, "middle", DIM))
    b.append(t(PX(5.0), Y1 + 20, "x*", 11.5, "middle", RED, "600"))
    b.append(t(PX(7.0), Y1 + 20, "x* + δ", 11.5, "middle", DIM))

    # |g'(x*)| 的点与短线
    b.append(f'<circle cx="{PX(5.0):.1f}" cy="{PY(0.40):.1f}" r="4.6" fill="{INK}"/>')
    b.append(f'<line x1="{PX(5.0):.1f}" y1="{PY(0.40):.1f}" x2="{PX(5.0):.1f}" y2="{PY(L):.1f}" '
             f'stroke="{INK}" stroke-width="1.2" stroke-dasharray="2 3"/>')
    b.append(t(PX(5.0) + 10, PY(0.40) + 4, "|g′(x*)| = 0.40", 11.5, "start", INK, "600"))

    # δ 的双向箭头（画在轴下方）
    ay = Y1 + 42
    b.append(f'<line x1="{PX(XS):.1f}" y1="{ay:.1f}" x2="{PX(XE):.1f}" y2="{ay:.1f}" '
             f'stroke="{BLUE}" stroke-width="1.4" marker-start="url(#ar-b)" marker-end="url(#ar-b)"/>')
    b.append(t(PX(5.0), ay - 8, "2δ = 1 − |g′(x*)|", 11.5, "middle", BLUE, "600"))

    # 说明
    b.append(t(40, 386, "曲线的具体形状无所谓，只要连续——这就是「由连续性存在 δ」：", 12, "start", DIM))
    b.append(t(40, 406, "邻域里整段被水平线 L 压住，而 L < 1，于是全局定理的两个条件在这个小闭区间上都成立。", 12, "start", DIM))
    b.append(t(40, 426, "δ 不能随便取：|g′(x*)| 必须离 1 留出距离，δ 才有可能存在。", 12, "start", DIM))
    save(os.path.join("第7章-非线性方程", "figures", "local-neighborhood.svg"), "\n".join(b))


# ------------------------------------------------- 2 Cholesky 省一半
def fig_cholesky():
    W, H = 780, 470
    b = [head(W, H)]
    b.append(t(40, 44, "对称性让上三角白算：Cholesky 的工作量正好是 LU 的一半", 16, "start", INK, "600"))
    b.append(t(40, 68, "A = LU 要填满上下两个三角；A = LLᵀ 只需下三角，上三角是转置", 12, "start", DIM))

    cell = 40.0
    N = 5

    def grid(cx, top, mode):
        """mode: 'lu' 填满；'chol' 上三角留空"""
        x0 = cx - N * cell / 2
        # 格子
        for i in range(N):
            for j in range(N):
                x = x0 + j * cell
                y = top + i * cell
                if mode == 'lu':
                    if i == j:
                        fill = "#dbe4fb"
                    elif i > j:
                        fill = FILL_L
                    else:
                        fill = FILL_U
                else:
                    if i == j:
                        fill = "#dbe4fb"
                    elif i > j:
                        fill = FILL_L
                    else:
                        fill = FILL_GREY
                b.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{cell:.1f}" height="{cell:.1f}" '
                         f'fill="{fill}" stroke="#d5dae0" stroke-width="1"/>')
        # 对角线
        b.append(f'<line x1="{x0:.1f}" y1="{top:.1f}" x2="{x0+N*cell:.1f}" y2="{top+N*cell:.1f}" '
                 f'stroke="{INK}" stroke-width="1.6"/>')
        if mode == 'chol':
            # 上三角标「不用算」
            for j in range(N):
                for i in range(j):
                    x = x0 + j * cell
                    y = top + i * cell
                    b.append(f'<line x1="{x+9:.1f}" y1="{y+cell-9:.1f}" x2="{x+cell-9:.1f}" y2="{y+9:.1f}" '
                             f'stroke="{LIGHT}" stroke-width="1.4"/>')
        return x0, top

    top = 118.0
    xl, _ = grid(190.0, top, 'lu')
    xr, _ = grid(560.0, top, 'chol')

    b.append(t(190.0, 104, "LU：上下三角都要算", 13, "middle", INK, "600"))
    b.append(t(560.0, 104, "Cholesky：只算下三角", 13, "middle", INK, "600"))

    # 左图下三角/上三角标注
    b.append(t(xl + cell * 1.5, top + N * cell + 22, "L 在下三角", 11.5, "middle", DIM))
    b.append(t(xl + cell * 3.5, top + N * cell + 22, "U 在上三角", 11.5, "middle", DIM))
    b.append(t(xr + cell * 2.5, top + N * cell + 22, "上三角 = 下三角转置，不用算", 11.5, "middle", DIM))

    # 中间箭头
    my_ = top + N * cell / 2
    xa, xb = xl + N * cell + 22, xr - 22
    b.append(f'<line x1="{xa:.1f}" y1="{my_:.1f}" x2="{xb-11:.1f}" y2="{my_:.1f}" '
             f'stroke="{BLUE}" stroke-width="2"/>')
    b.append(f'<path d="M {xb:.1f} {my_:.1f} L {xb-13:.1f} {my_-6.5:.1f} L {xb-13:.1f} {my_+6.5:.1f} z" '
             f'fill="{BLUE}"/>')
    b.append(t((xl + N * cell + xr) / 2, top + N * cell / 2 - 14, "对称", 12.5, "middle", BLUE, "600"))
    b.append(t((xl + N * cell + xr) / 2, top + N * cell / 2 + 26, "省一半", 12.5, "middle", BLUE, "600"))

    # 数字对比
    y0 = top + N * cell + 56
    b.append(t(40, y0, "存储量", 12, "start", DIM, "600"))
    b.append(t(120, y0, "LU 存 n² 个元素", 12, "start", INK))
    b.append(t(300, y0, "→", 13, "middle", LIGHT))
    b.append(t(330, y0, "Cholesky 只存 n(n+1)/2 个（L 的下三角含对角）", 12, "start", INK))

    b.append(t(40, y0 + 24, "运算量", 12, "start", DIM, "600"))
    b.append(t(120, y0 + 24, "n³/3 次乘除", 12, "start", INK))
    b.append(t(300, y0 + 24, "→", 13, "middle", LIGHT))
    b.append(t(330, y0 + 24, "n³/6 次乘除，正好一半", 12, "start", INK))

    b.append(t(40, y0 + 48, "代价", 12, "start", DIM, "600"))
    b.append(t(120, y0 + 48, "每步要开一次方（共 n 次）", 12, "start", INK))
    b.append(t(300, y0 + 48, "→", 13, "middle", LIGHT))
    b.append(t(330, y0 + 48, "改进平方根法 LDLᵀ 把开方消掉，见 §2.4", 12, "start", INK))

    b.append(t(40, y0 + 80, "n = 5 时：LU 要处理 25 个位置，Cholesky 只处理 15 个 —— 省掉的正是那 10 个上三角。", 12, "start", DIM))
    save(os.path.join("第5章-解线性方程组的直接法", "figures", "cholesky-half.svg"), "\n".join(b))


if __name__ == "__main__":
    fig_neighborhood()
    fig_cholesky()
