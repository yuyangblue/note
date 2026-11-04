# -*- coding: utf-8 -*-
"""生成 CM+Opt_非线性.pdf 的图形候选 + 逐页对照审查页。"""
import os, sys, base64
sys.stdout.reconfigure(encoding='utf-8')

TMP = r'D:\29469\Documents\notes\.workbuddy\tmp'
FIG = os.path.join(TMP, 'figprev4')
OUT = os.path.join(TMP, '非线性手写讲义-图形审查.html')

CARDS = [
 ('a-二分法区间收缩.png', 'p01', '二分法：多根区间怎么收缩',
  '7.1 §2 的区间更新规则、§3 的误差界 $\\varepsilon\\le L/2^{k+1}$',
  '多根函数在区间里最终锁定哪一个根',
  '不建议', '一层意思一句话能补，且手写红笔潦草。属于「把规则重画一遍」。'),
 ('b-二分法折半示意.png', 'p01', '二分法：两种折半情形',
  '$a^{k+1}$ 或 $b^{k+1}$ 取 $(a^k+b^k)/2$',
  '无 —— 纯文字直译',
  '不建议', '公式已经写全，图只是给公式配括号。'),
 ('c-局部收敛邻域.png', 'p03', "$g'$ 曲线与水平线 $L<1$",
  '7.2 §3.2 四步证明、§3.3「附近到底有多近」',
  '本可给出 $\\delta$ 的量化，但手写版只标到 $L<1$',
  '已有更好替代', '笔记里的 <code>local-neighborhood.svg</code> 带 $|g\u2032(x^*)|=0.40$、$L=0.60$、$\\delta=(1-|g\u2032|)/2$，信息更多、字迹清楚。保留 SVG，不截手写版。'),
 ('d-Aitken序列构造.png', 'p05', 'Aitken：上排三值换下排一值',
  '7.2 §6.4「$\\{x_k\\}$ 每三个连续值算出一个 $\\overline{x_k}$」',
  '只有箭头的分组关系',
  '不建议', 'Aitken 是纯代数构造（二阶差商），没有天然几何结构。这正是上次删掉的 <code>aitken-sequence.svg</code> 同类。'),
 ('e-牛顿法切线.png', 'p07', '牛顿法的切线几何',
  '7.2 §11 的几何读法',
  '切线与 x 轴的交点',
  '已有更好替代', '笔记已有板书实拍 <code>newton-tangent.jpg</code>，更清晰；手写版是同一张图的简略版。'),
 ('f-切线转割线.png', 'p09', '切线 → 割线',
  '7.2 §14.3 割线法推导',
  '两张并排的控制',
  '已有更好替代', '笔记已有 <code>secant-method.jpg</code>（左切线右割线对照），结构相同且更完整。'),
 ('g-曲线交点.png', 'p12', '三次曲线与圆的交点',
  '7.3 §20 两个方程与两个交点数值',
  '静态示意，无路径、无量级',
  '不建议', '图本身不进正文；但这一页给出 §20 的方程、初值与 $F(x^{(0)})=(0,1)^T$，据此重算了数值。常数是否等于课上原题，无第二来源可确认。'),
]

ROWS = [
 ('p01', '二分法（介值定理）、区间收缩、误差 $L/2^{k+1}$、$x^3-x^2-1$ 例题', '7.1 §2–§5', ''),
 ('p02', '误差推导、不动点存在唯一性、Lipschitz、$x^2+x-10$ 三种改写', '7.1 §3、§8；7.2 §1', ''),
 ('p03', '全局/局部收敛性、局部收敛定理及证明、发散推论', '7.2 §2–§3', ''),
 ('p04', '收敛阶定义、有效位数翻倍、判定定理与泰勒证明', '7.2 §4–§5', ''),
 ('p05', 'Aitken $\\Delta^2$ 推导、外推公式、加速定理', '7.2 §6', ''),
 ('p06', 'Steffensen 迭代、$\\varphi$ 与 $g$ 不动点等价（含 $0/0$ 分支）', '7.2 §7–§8', ''),
 ('p07', 'Steffensen 收敛速度、牛顿法推导、平方收敛定理与证明', '7.2 §9、§11–§12', '补 $2p-1$ 定理的条件与出处'),
 ('p08', '证明续（$C^*$、$\\delta^*$、归纳）、$\\sqrt2$ 与 $\\sqrt0$ 两例', '7.2 §12–§13.2', ''),
 ('p09', '$x^N=0$、拟牛顿、割线法与黄金分割阶、三阶构造开端', '7.2 §13.3–§15；7.3 §4', ''),
 ('p10', '三阶格式、Halley 对照、$\\sqrt[n]{a}$ 两种写法与误差常数', '7.3 §5–§10', ''),
 ('p11', '向量函数连续性、Fréchet 导数、Jacobian、压缩映射', '7.3 §12–§14', ''),
 ('p12', '定理 1/2、方程组牛顿法、三次曲线与圆的例题', '7.3 §15–§20', '补 §20 一组自洽常数并重算'),
 ('p13', '牛顿法局部收敛性（超线性）完整证明', '7.3 §19', ''),
 ('p14', '拟牛顿方程、秩一修正引理与两条性质', '7.4 §2–§3', ''),
 ('p15', 'Broyden 秩一方法、Sherman–Morrison、逆 Broyden', '7.4 §4–§5', ''),
]


def b64(name):
    with open(os.path.join(FIG, name), 'rb') as f:
        return base64.b64encode(f.read()).decode()


parts = ['''<!DOCTYPE html>
<html lang="zh-CN"><head><meta charset="utf-8">
<title>CM+Opt_非线性.pdf · 图形与内容审查</title>
<style>
:root{--ink:#1c2430;--dim:#5c6875;--line:#e2e6ea;--bg:#f5f7f9;--card:#fff;
--ok:#1a7f5a;--warn:#b06a12;--no:#8a939d;}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);
font:15px/1.75 -apple-system,"Segoe UI","Microsoft YaHei",sans-serif}
.wrap{max-width:1000px;margin:0 auto;padding:36px 24px 60px}
h1{font-size:25px;margin:0 0 6px;letter-spacing:-.3px}
.sub{color:var(--dim);font-size:13.5px;margin-bottom:26px}
.lead{background:#eef4f8;border-left:4px solid #4a7fa5;padding:16px 20px;
border-radius:0 8px 8px 0;margin-bottom:30px}
.lead b{color:#2b5f85}
h2{font-size:18px;margin:34px 0 14px;padding-bottom:8px;border-bottom:1px solid var(--line)}
.card{background:var(--card);border:1px solid var(--line);border-radius:10px;
padding:18px 20px;margin-bottom:16px;display:flex;gap:22px;align-items:flex-start}
.card .shot{flex:0 0 330px;background:#fafbfc;border:1px solid var(--line);
border-radius:6px;padding:8px;text-align:center}
.card .shot img{max-width:100%;height:auto;display:block}
.card .shot .pg{font-size:11.5px;color:var(--no);margin-top:6px}
.card .body{flex:1;min-width:0}
.card h3{margin:0 0 4px;font-size:16px}
.badge{display:inline-block;font-size:11.5px;padding:2px 9px;border-radius:20px;
background:#f0f2f4;color:var(--no);margin-bottom:10px}
.badge.alt{background:#eaf3ff;color:#2b6cb0}
.kv{font-size:13.5px;color:var(--dim);margin:5px 0}
.kv b{color:var(--ink);font-weight:600}
.verdict{font-size:13.5px;margin-top:10px;padding-top:10px;border-top:1px dashed var(--line)}
table{width:100%;border-collapse:collapse;background:var(--card);
border:1px solid var(--line);border-radius:8px;overflow:hidden;font-size:13.5px}
th,td{padding:9px 12px;text-align:left;border-bottom:1px solid var(--line);vertical-align:top}
th{background:#eef1f4;font-weight:600;color:var(--dim);font-size:12.5px}
tr:last-child td{border-bottom:none}
td.hit{color:var(--ok);font-weight:600}
code{background:#f0f2f4;padding:1px 5px;border-radius:4px;font-size:12.5px}
.foot{margin-top:26px;color:var(--dim);font-size:12.5px}
</style></head><body><div class="wrap">
<h1>CM+Opt_非线性.pdf · 图形与内容审查</h1>
<div class="sub">15 页 iPad 手写课堂笔记 · 逐页对照 7.1 / 7.2 / 7.3 / 7.4</div>
<div class="lead">
<b>结论：内容几乎全覆盖，图一张都不建议进正文。</b><br>
15 页从头到尾对下来，讲义里的每块内容都能在笔记里找到对应，而且笔记多半更详细（有算例、动机、数值验证）。
真正补进正文的是两处：<b>7.2 §9</b> 的 $2p-1$ 定理条件与出处、<b>7.3 §20</b> 按手写笔记里一组自洽常数重算全部数值。<br>
<b>证据等级要分清：</b>7.2 那条在手写笔记里有完整定理陈述，可核；7.3 那组常数只有手写笔记一个来源，课堂录音转写正好把常数丢了，<b>无从交叉核对，不能断言等于老师口述的原题</b>，笔记内已把推断依据与不确定性写明。<br>
下面 7 张是讲义里全部成形的图形，按「有没有携带文字给不出的信息」逐张判过。<b>p12 那页虽然图不值得留，却给出了 §20 的方程与自洽性线索。</b>
</div>
<h2>一、图形候选（7 张）</h2>
''']

for fn, pg, title, said, extra, verdict, note in CARDS:
    cls = 'badge alt' if '替代' in verdict else 'badge'
    parts.append(f'''<div class="card">
<div class="shot"><img src="data:image/png;base64,{b64(fn)}" alt="{title}"><div class="pg">讲义 {pg}</div></div>
<div class="body"><h3>{title}</h3><div class="{cls}">{verdict}</div>
<div class="kv"><b>文字已说：</b>{said}</div>
<div class="kv"><b>图能多给：</b>{extra}</div>
<div class="verdict">{note}</div>
</div></div>''')

parts.append('''<h2>二、15 页 → 笔记对照</h2>
<table><thead><tr><th style="width:52px">页</th><th>讲义内容</th><th style="width:190px">笔记位置</th>
<th style="width:170px">缺口</th></tr></thead><tbody>''')
for pg, what, where, gap in ROWS:
    g = f'<td class="hit">{gap}</td>' if gap else '<td style="color:#8a939d">—</td>'
    parts.append(f'<tr><td>{pg}</td><td>{what}</td><td>{where}</td>{g}</tr>')
parts.append('''</tbody></table>
<div class="foot">
判断依据沿用项目约定：图只画「路径 / 结构 / 真实数据 / 量级」，不画文字直译、教材标配、公式已写全只补一句对应、按公式拟的曲线。
手写讲义的图多是随手示意，且笔记里已有三张更清楚的替代品（<code>local-neighborhood.svg</code>、<code>newton-tangent.jpg</code>、<code>secant-method.jpg</code>）。
</div></div></body></html>''')

open(OUT, 'w', encoding='utf-8').write(''.join(parts))
print('生成', OUT, '%.0f KB' % (os.path.getsize(OUT)/1024))
print('卡片', len(CARDS), '对照行', len(ROWS))
