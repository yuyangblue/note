# -*- coding: utf-8 -*-
import os, sys

sys.stdout.reconfigure(encoding="utf-8")

ROOT = r"D:\29469\Documents\notes\计算方法与优化"
OUT = r"D:\29469\Documents\notes\.workbuddy\tmp\新增插图预览.html"

ITEMS = [
    dict(
        loc="5.4 向量范数与矩阵范数 · §1.2 常用的向量范数",
        file="第5章-解线性方程组的直接法/figures/norms-unit-balls.svg",
        why="原文只说了「曼哈顿距离」「欧氏距离」，三种范数的差别全靠想象。单位球一画，嵌套关系和等价性常数就有了实物。",
        text="把「长度为 1 的点」全部画出来，三种范数给出三种形状：‖·‖∞ 的是正方形，‖·‖₂ 的是圆，‖·‖₁ 的是菱形。三个球互相嵌套（B₁ ⊂ B₂ ⊂ B∞），嵌套的松紧正是下面那条等价性不等式里的常数。",
    ),
    dict(
        loc="5.5 线性方程组的性态与误差分析 · §4 条件数",
        file="第5章-解线性方程组的直接法/figures/ill-conditioned-lines.svg",
        why="条件数那一串推导全是范数不等式，读完不知道「病态」长什么样。放在定义前面先给几何，后面的公式才有落脚点。",
        text="先看几何：两条直线几乎平行时，右端项挪动一丁点，交点就会滑出去很远。条件数量化的正是这个「滑多远」。",
    ),
    dict(
        loc="6.4 共轭梯度法 · §10 CG 的收敛速度",
        file="第6章-解线性方程组的迭代法/figures/cg-vs-sd.svg",
        why="原文用「快一个数量级」一句话带过。半对数坐标下一画，两条直线的斜率差和 24 步处的差距都成了看得见的东西。",
        text="对数坐标下两条都是直线，斜率就是各自的压缩常数。SD 的线几乎是平的——κ=100 时每步只把误差压到 0.98 倍，四十几步下来仍有一半；CG 的线陡得多，因为它压的是 √κ 而不是 κ。",
    ),
    dict(
        loc="7.1 非线性方程求根 · §6 不动点迭代法：定义与几何",
        file="第7章-非线性方程/figures/fixed-point-cobweb.svg",
        why="原文用一整段话描述「折线阶梯」，还说「作为练习可以自行画出两种迭代的阶梯图」。直接把三种走向画出来，练习就不用做了。",
        text="三种走向的差别全在 g′ 的符号和大小上：0<g′<1 时每步都从同一侧靠近，折线是一级级收窄的阶梯；g′ 为负时左右横跳，折线绕成向内的螺旋；|g′|>1 时越折越远，几步就冲出画面。",
    ),
    dict(
        loc="7.3 非线性方程组 · §14 压缩映射",
        file="第7章-非线性方程/figures/contraction-map.svg",
        why="这一节原来一张图都没有，而压缩映射的两个条件（自映射、距离缩短）本来就是纯几何的。一张图把两个条件同时摆出来。",
        text="图上两件事同时发生：Φ 把整个 D₀ 映到它自己内部（自映射，条件 2），并且把 x,y 之间的距离从 ‖x−y‖ 缩到 ‖Φ(x)−Φ(y)‖（压缩条件，条件 1）。",
    ),
]

cards = []
for i, it in enumerate(ITEMS, 1):
    svg = open(os.path.join(ROOT, it["file"].replace("/", os.sep)), encoding="utf-8").read()
    # 不改 SVG 自带属性，交给外层 CSS 按 viewBox 缩放
    cards.append(f"""
  <section class="card">
    <div class="no">{i}</div>
    <div class="loc">{it['loc']}</div>
    <div class="why">{it['why']}</div>
    <div class="stage">{svg}</div>
    <div class="cap"><b>插图下方的正文</b>{it['text']}</div>
  </section>""")

html = f"""<!DOCTYPE html>
<html lang="zh-CN"><head><meta charset="utf-8">
<title>计算方法与优化 · 新增插图预览</title>
<style>
  :root {{ --ink:#1f2933; --dim:#6b7785; --line:#e4e7eb; --bg:#f7f8fa; --acc:#1d4ed8; }}
  * {{ box-sizing:border-box; }}
  body {{ margin:0; background:var(--bg); color:var(--ink);
         font:15px/1.75 -apple-system,"Segoe UI","Microsoft YaHei",sans-serif; }}
  header {{ padding:40px 40px 20px; max-width:1080px; margin:0 auto; }}
  h1 {{ font-size:22px; margin:0 0 8px; letter-spacing:.2px; }}
  .sub {{ color:var(--dim); font-size:13.5px; }}
  main {{ max-width:1080px; margin:0 auto; padding:8px 40px 80px; }}
  .card {{ background:#fff; border:1px solid var(--line); border-radius:10px;
           padding:26px 28px 22px; margin:22px 0; position:relative; }}
  .no {{ position:absolute; top:-12px; left:24px; background:var(--acc); color:#fff;
         width:26px; height:26px; border-radius:50%; display:flex; align-items:center;
         justify-content:center; font-size:13px; font-weight:600; }}
  .loc {{ font-size:13px; color:var(--acc); font-weight:600; margin:2px 0 10px; }}
  .why {{ color:var(--dim); font-size:13.5px; padding:10px 14px; background:#fafbfc;
          border-left:2px solid var(--line); border-radius:0 4px 4px 0; margin-bottom:18px; }}
  .stage {{ border:1px solid var(--line); border-radius:6px; overflow:hidden; background:#fff; }}
  .stage svg {{ display:block; width:100%; height:auto; }}
  .cap {{ margin-top:14px; font-size:13.5px; color:var(--ink); }}
  .cap b {{ display:block; color:var(--dim); font-size:12px; font-weight:600;
            letter-spacing:.4px; margin-bottom:4px; }}
</style></head>
<body>
<header>
  <h1>计算方法与优化 · 新增的 5 张插图</h1>
  <div class="sub">都是 SVG，矢量不失真，深色主题下也读得清。每张下面附了插进正文时新写的说明文字。</div>
</header>
<main>
{''.join(cards)}
</main>
</body></html>"""

open(OUT, "w", encoding="utf-8").write(html)
print("写出", OUT, "%.0f KB" % (os.path.getsize(OUT) / 1024))
