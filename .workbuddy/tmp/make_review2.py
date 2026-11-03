# -*- coding: utf-8 -*-
"""生成第二批插图的审查页。"""
import os, sys, html

sys.stdout.reconfigure(encoding="utf-8")
ROOT = r"D:\29469\Documents\notes\计算方法与优化"

CARDS = [
    dict(no="1", title="最小二乘的正交投影", file=r"第3章-最小二乘问题\figures\lsq-projection.svg",
         where="3.1 §3 法方程 · 推完 Aᵀ(Ax−b)=0 之后",
         had="列空间、投影、残差与每一列正交",
         new="把「正交」画成看得见的直角；另外 b 悬在平面上方这件事，文字只说了「通常不相容」，图上一眼就是「够不着」。",
         conf="高", why="最小二乘的几何本质就是垂足，这是全节唯一需要 3D 的地方。"),
    dict(no="2", title="Doolittle 的计算次序", file=r"第5章-解线性方程组的直接法\figures\lu-order.svg",
         where="5.3 §1.2 递推公式 · 「从左上角斜着一层层往右下推」之后",
         had="「斜着一层层往右下推」「每层只用到左边和上边已填好的数」",
         new="min(i,j) 这条规律文字里没有——原来只能靠 r=2、r=3 两步手算去体会；还有「对角元必须先算，否则同一列的除法没法做」这个顺序约束，图上一根绿箭头。",
         conf="高", why="这是手算时脑子里要有的那张表，纯文字写不出来。"),
    dict(no="4", title="Aitken 加速的序列图", file=r"第7章-非线性方程\figures\aitken-sequence.svg",
         where="7.2 §6.4 序列图与用法 · 正文原本写「板书画了一张图…」，而图已丢失",
         had="一段文字描述（上面一行、每三个数向下一行引箭头）+ §6.5 的数字表",
         new="把「震荡收敛」和「外推值一步贴到根上」摆在一起；表格里的 9 个数看不出这个形状。这是补回丢失的板书图，不是新增。",
         conf="高", why="正文在描述一张不存在的图，这是硬缺口。"),
    dict(no="6", title="条件数的椭圆解释", file=r"第5章-解线性方程组的直接法\figures\cond-ellipse.svg",
         where="5.5 §4 条件数 · 公式之后（原先这里那张平行线图已删）",
         had="cond 的定义、以及「两条近平行直线」的几何解释",
         new="第二种几何解释：圆被拉成椭圆，轴比就是 cond。平行线画法说不出「为什么求逆会放大误差」，椭圆能——短轴方向被放大 1/σmin 倍。",
         conf="中高", why="补的是被删那张图的位置，但换了更有信息量的几何；两张不是同一件事。"),
]


def read_svg(p):
    s = open(p, encoding="utf-8").read()
    i = s.find("<svg")
    return s[i:]


parts = []
for idx, c in enumerate(CARDS, 1):
    c["no"] = str(idx)
    svg = read_svg(os.path.join(ROOT, c["file"]))
    parts.append(f"""
    <section class="card">
      <div class="head">
        <span class="no">{c['no']}</span>
        <h2>{html.escape(c['title'])}</h2>
        <span class="conf c-{c['conf'].replace('中高','hi2')}">把握度 {c['conf']}</span>
      </div>
      <div class="where">插入位置 · {html.escape(c['where'])}</div>
      <div class="figwrap">{svg}</div>
      <div class="cmp">
        <div class="col had"><span class="tag">文字已经说了</span>{html.escape(c['had'])}</div>
        <div class="col new"><span class="tag">图新加了</span>{html.escape(c['new'])}</div>
      </div>
      <div class="why">{html.escape(c['why'])}</div>
    </section>""")

html_doc = """<!DOCTYPE html>
<html lang="zh-CN"><head><meta charset="utf-8">
<title>第二批插图 · 保留 4 张</title>
<style>
  *{box-sizing:border-box}
  body{margin:0;padding:36px 28px 64px;background:#f5f6f8;color:#1f2933;
       font-family:-apple-system,'Segoe UI','Microsoft YaHei',sans-serif;line-height:1.65}
  .wrap{max-width:980px;margin:0 auto}
  .lead{margin:0 0 6px;font-size:24px;font-weight:700;letter-spacing:.01em}
  .sub{margin:0 0 30px;color:#5a6572;font-size:13.5px}
  .card{background:#fff;border:1px solid #e2e6ec;border-radius:12px;padding:22px 24px 20px;
        margin-bottom:26px;box-shadow:0 1px 3px rgba(20,30,50,.05)}
  .head{display:flex;align-items:center;gap:10px;margin-bottom:4px}
  .no{display:inline-flex;width:26px;height:26px;border-radius:50%;background:#1f2933;color:#fff;
      font-size:13px;font-weight:700;align-items:center;justify-content:center;flex:0 0 auto}
  h2{font-size:16.5px;margin:0;font-weight:700;flex:1}
  .conf{font-size:11.5px;padding:2px 9px;border-radius:999px;border:1px solid;white-space:nowrap}
  .c-高{color:#047857;border-color:#b7ddd0;background:#effaf5}
  .c-中高,.c-hi2{color:#b45309;border-color:#f0d3a8;background:#fdf6e9}
  .c-中{color:#5a6572;border-color:#d5dae0;background:#f4f6f8}
  .where{font-size:12.5px;color:#6b7785;margin-bottom:16px;padding-left:36px}
  .figwrap{border:1px solid #eceff3;border-radius:8px;overflow:hidden;background:#fff;
           margin-bottom:16px}
  .figwrap svg{display:block;width:100%;height:auto}
  .cmp{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:12px}
  .col{font-size:13px;padding:12px 14px;border-radius:8px;background:#f8f9fb;border:1px solid #eceff3}
  .col.new{background:#f3f7ff;border-color:#dde7f8}
  .tag{display:block;font-size:11px;font-weight:700;letter-spacing:.04em;margin-bottom:5px;color:#8a94a0}
  .col.new .tag{color:#3b62b8}
  .why{font-size:13px;color:#3f4a56;padding-left:14px;border-left:2px solid #d5dae0}
  .foot{margin-top:8px;font-size:12.5px;color:#6b7785;text-align:center}
  @media (max-width:720px){.cmp{grid-template-columns:1fr}}
</style></head>
<body><div class="wrap">
  <p class="lead">第二批插图 · 保留 4 张</p>
  <p class="sub">全部按「结构 / 过程 / 几何映射」来画，不做静态示意。每张标明文字已经说过什么、图还多给了什么——
     如果某一栏「图新加了」读下来没有你原本不知道的东西，那张就该删。</p>
""" + "".join(parts) + """
  <p class="foot">说编号就行，比如「3 和 5 没用」，我把图和正文里依附它的说明一起撤掉。</p>
</div></body></html>"""

out = r"D:\29469\Documents\notes\.workbuddy\tmp\第二批插图审查.html"
open(out, "w", encoding="utf-8").write(html_doc)
print(out, "%.1f KB" % (os.path.getsize(out) / 1024))
