# -*- coding: utf-8 -*-
"""补写 L04 多项分布小节"""
import io

p = r'D:\29469\Documents\notes\概率论MIT\笔记\L04 计数.md'
s = io.open(p, encoding='utf-8').read()

old = '### 2.5 子集数量'
new = """### 2.5 多项分布（多项概率，p048 L04.9）
$n$ 次独立试验，每次试验有 $r$ 类互斥结果，第 $i$ 类出现的概率为 $p_i$（$\\sum_i p_i = 1$），则"恰好 $n_1$ 次第 1 类、$n_2$ 次第 2 类、$\\dots$、$n_r$ 次第 $r$ 类"（$\\sum_i n_i = n$）的概率为：
$$P(n_1, n_2, \\dots, n_r) = \\frac{n!}{n_1! \\, n_2! \\cdots n_r!} \\, p_1^{n_1} p_2^{n_2} \\cdots p_r^{n_r}$$
- **推导两步**：① 任一特定序列（如"颜色一、一、三、一、二、二、一"）的概率由独立性得 $p_1^{n_1}p_2^{n_2}\\cdots p_r^{n_r}$（指数 = 该颜色出现次数，与顺序无关）；② 此类序列共有多少个？"在哪几次试验出现哪类颜色"就是集合 $\\{1,\\dots,n\\}$ 按大小 $n_1,\\dots,n_r$ 的划分，数量 = 分拆数 $\\frac{n!}{n_1!\\cdots n_r!}$（2.4 节）。两者相乘即得。
- **特例**：$r=2$ 时退化为二项概率 $\\binom{n}{n_1}p_1^{n_1}(1-p_1)^{n-n_1}$——把"两类颜色"换成"正面/反面"即可（老师原话：二项概率是多项概率的自然特例）。
- **用途**：多次试验中多类结果的计数概率，如骰子各点数出现次数、基因型计数、质检多等级分类。

### 2.6 子集数量"""

assert s.count(old) == 1, 'anchor count: ' + str(s.count(old))
s = s.replace(old, new)
io.open(p, 'w', encoding='utf-8', newline='').write(s)
print('OK L04 updated')
