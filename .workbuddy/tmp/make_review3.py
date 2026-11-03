# -*- coding: utf-8 -*-
import os, sys, html

sys.stdout.reconfigure(encoding="utf-8")
ROOT = r"D:\29469\Documents\notes\计算方法与优化"

CARDS = [
    dict(no="1", title="局部收敛的邻域构造", file=r"第7章-非线性方程\figures\local-neighborhood.svg",
         where="7.2 §3.2 局部收敛定理 · 证明四步之后",
         had="证明第 1 步说：取 ε 使 L=|g′(x*)|+ε<1，由连续性存在 δ 使邻域内 |g′|≤L；第 3 步说 g 把这个闭区间映进自身。",
         new="① |g′| 的曲线怎么起伏都行（只要连续），只要被一条水平线压住；② 可用邻域的宽度受制于 |g′(x*)| 离 1 还有多远——越接近 1，区间越窄。",
         why="这两点文字都没明说。特别是第二点：它解释了定理为什么只承诺「局部」，以及初值到底要取得多近。图里 δ 的长度就是 1−|g′(x*)| 的一半。",
         conf="中高"),
    dict(no="2", title="对称性让上三角白算", file=r"第5章-解线性方程组的直接法\figures\cholesky-half.svg",
         where="5.3 §2.1 平方根法 · 定理 10 证明梗概之后",
         had="正文给了 A=LDLᵀ 的推导和定理 10，但「运算量正好是一半」只是 §2.3 里的一句话提过。",
         new="① 格子图直接显示省掉的是哪一半（打斜杠的上三角）；② 代价那行：Cholesky 每步要开方（共 n 次），LU 不用。",
         why="「省一半」的来源是结构性的——A 对称 ⇒ a_ij = a_ji，上三角是下三角的转置拷贝。文字要绕几句才说得清，格子图一眼看出省掉的是哪一块，也顺带把开方代价摆出来了。",
         conf="中"),
]

HEAD = """<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8">
<title>第三批插图 · 2 张</title><style>
*{box-sizing:border-box}
body{margin:0;padding:28px 30px 60px;background:#0f1419;color:#e6edf3;
 font-family:-apple-system,'Segoe UI','Microsoft YaHei',sans-serif;line-height:1.65}
h1{font-size:21px;margin:0 0 6px;font-weight:600}
.sub{color:#8b98a5;font-size:13px;margin-bottom:26px}
.card{background:#161c23;border:1px solid #232c36;border-radius:12px;padding:20px 22px;margin-bottom:22px}
.head{display:flex;align-items:baseline;gap:12px;flex-wrap:wrap}
.no{background:#2563eb;color:#fff;border-radius:6px;padding:1px 9px;font-size:13px;font-weight:600}
h2{font-size:17px;margin:0;font-weight:600}
.conf{margin-left:auto;font-size:12px;color:#8b98a5;border:1px solid #2c3742;border-radius:20px;padding:2px 11px}
.where{color:#7fb3ff;font-size:13px;margin:8px 0 14px}
.figwrap{background:#ffffff;border-radius:8px;padding:10px;overflow:auto}
.figwrap svg{max-width:100%;height:auto;display:block}
.cmp{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:14px}
.col{background:#11171d;border:1px solid #222b35;border-radius:8px;padding:12px 14px;font-size:13.5px;color:#c8d3dd}
.tag{display:inline-block;font-size:11px;color:#0f1419;border-radius:4px;padding:1px 7px;margin-bottom:7px}
.had .tag{background:#5b6472;color:#eef2f6}
.new .tag{background:#2f7d4f;color:#eefaf1}
.why{margin-top:12px;font-size:13.5px;color:#a8b5c1;border-left:3px solid #2c3742;padding-left:12px}
@media(max-width:760px){.cmp{grid-template-columns:1fr}}
</style></head><body>
<h1>第三批插图 · 2 张</h1>
<div class="sub">画法：只画「结构 / 几何约束」，不做静态示意，也不把公式重画成曲线</div>
"""


def read_svg(rel):
    p = os.path.join(ROOT, rel)
    s = open(p, encoding="utf-8").read()
    s = s.replace("<?xml version=\"1.0\" encoding=\"utf-8\"?>", "")
    return s


parts = [HEAD]
for c in CARDS:
    parts.append(f"""
<section class="card">
  <div class="head"><span class="no">{c['no']}</span><h2>{html.escape(c['title'])}</h2>
  <span class="conf">把握度 {c['conf']}</span></div>
  <div class="where">插入位置 · {html.escape(c['where'])}</div>
  <div class="figwrap">{read_svg(c['file'])}</div>
  <div class="cmp">
    <div class="col had"><span class="tag">文字已经说了</span>{html.escape(c['had'])}</div>
    <div class="col new"><span class="tag">图新加了</span>{html.escape(c['new'])}</div>
  </div>
  <div class="why">{html.escape(c['why'])}</div>
</section>""")

out = r"D:\29469\Documents\notes\.workbuddy\tmp\第三批插图审查.html"
open(out, "w", encoding="utf-8").write("\n".join(parts) + "</body></html>")
print(out, os.path.getsize(out) / 1024, "KB")
