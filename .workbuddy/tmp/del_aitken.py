# -*- coding: utf-8 -*-
import os, sys
sys.stdout.reconfigure(encoding="utf-8")
D = r"D:\29469\Documents\notes\计算方法与优化\第7章-非线性方程"
F72 = os.path.join(D, "7.2-收敛性判据收敛阶与迭代加速-牛顿法与割线法.md")

s = open(F72, encoding="utf-8").read()

# 1) 标题与目录
pairs = [
    ("### 6.4 序列图与用法", "### 6.4 序列的构造与用法"),
    ("  - [[#6.4 序列图与用法]]", "  - [[#6.4 序列的构造与用法]]"),
]
for a, b in pairs:
    print("count=%d  %s" % (s.count(a), a[:40]))
    s = s.replace(a, b)

# 2) 正文：去掉图与依赖图的说法
old = (
    "加速的构造可以这样看：上面一行 $\\{x_k\\}$ 一直往前走，每三个数向下引一个箭头，得到下面一行 $\\{\\overline{x_k}\\}$ 的一个元素。用 $\\cos$ 迭代的实际数据画出来是这样：\n\n"
    "![Aitken 加速：上排原序列在根两侧震荡逼近，下排外推值几乎一次就贴到根上](figures/aitken-sequence.svg)\n\n"
    "上排每步只把误差压到 $0.67$ 倍左右，来回跳；下排几乎是一条水平线——因为每个 $\\overline{x_k}$ 都是按\"误差严格等比\"这个假设反推出来的极限位置，比原序列的直接值更靠近 $x^*$。"
)
new = (
    "加速的构造可以这样理解：$\\{x_k\\}$ 一直往前走，每三个连续值算出一个 $\\overline{x_k}$——取 $x_k,x_{k+1},x_{k+2}$，按\"误差严格等比\"这个假设外推出极限位置，作为 $\\overline{x_k}$。它比原序列的直接值更靠近 $x^*$：原序列每步只把误差压到 $0.67$ 倍左右、来回跳，而外推值一步就落到根上。"
)
print("count=%d  正文 6.4" % s.count(old))
s = s.replace(old, new)

# 3) 头部：不再提「重画 1 张 Aitken 序列图」
a = "正文保留 2 张实拍（牛顿切线、割线对照），另重画 1 张 Aitken 序列图"
b = "正文保留 2 张实拍（牛顿切线、割线对照）"
print("count=%d  头部" % s.count(a))
s = s.replace(a, b)

open(F72, "w", encoding="utf-8").write(s)
print("done")
