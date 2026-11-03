# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
p = r'D:\29469\Documents\notes\计算方法与优化\第7章-非线性方程\7.3-非线性方程组-向量函数压缩映射与牛顿法.md'
L = open(p, encoding='utf-8').read().split('\n')

i0 = next(i for i, l in enumerate(L) if l.startswith('📌 **平方收敛的证明思路**'))
i1 = next(i for i, l in enumerate(L) if l.startswith('**关键在 $\\big[F\'(x^{(k)})\\big]^{-1}$ 有界**'))
print('替换 L[%d:%d]' % (i0, i1 + 1))
for l in L[i0:i1 + 1]:
    print('  -', l[:90])

new = r'''📌 **平方收敛的证明思路**（课本只给结论，这里补出来）。一元的证明（7.2 §12）是把 $f(x^*)$ 在 $x_k$ 处泰勒展开；这里不能照抄，因为**向量函数没有中值定理**——写成 $F(x^{(k)})-F(x^*)=F'(\xi)\,e_k$ 的那个 $\xi$，各分量一般各不相同，凑不出一个公共的 $\xi$。补上这个缺口的办法是改用**积分形式的中值定理**，它对向量函数照样成立。所以三步：把牛顿步写成误差的式子、用积分把 $F(x^{(k)})$ 换成 $x^*$ 处的值、再估计剩下的 Jacobian 之差。

记 $e_k=x^{(k)}-x^*$。

1. **先把牛顿步写成误差。** 由 $F(x^{(k)})+F'(x^{(k)})\Delta x=0$ 与 $x^{(k+1)}=x^{(k)}+\Delta x$，

$$
e_{k+1}=e_k-\big[F'(x^{(k)})\big]^{-1}F(x^{(k)})
=\big[F'(x^{(k)})\big]^{-1}\Big\{F'(x^{(k)})e_k-F(x^{(k)})\Big\}
$$

这一步只是把牛顿步里的 $F$ 换成 $-[F']^{-1}F$，还没有做任何估计；它的用处是把式子整理成「一个 Jacobian 的逆 × 一对要相比较的量」。

2. **用积分把 $F(x^{(k)})$ 挪到 $x^*$ 去。** 因为 $F(x^*)=0$，

$$
F\big(x^{(k)}\big)-F(x^*)=\int_0^1F'\big(x^*+t\,e_k\big)e_k\,dt
$$

这里 $e_k$ 是常向量，可以整个提到积分号外——正是这一点让积分形式的公式和一维长得完全一样。代回去，

$$
e_{k+1}=\big[F'(x^{(k)})\big]^{-1}\int_0^1\Big\{F'(x^{(k)})-F'\big(x^*+te_k\big)\Big\}e_k\,dt
$$

现在括号里只剩两个 Jacobian 之差，而它们都在 $x^*$ 附近取值，这才轮到用 Lipschitz 条件。

3. **括号里的差是 $O(\|e_k\|)$。** 由 $\big\|F'(x)-F'(x^*)\big\|\le L\|x-x^*\|$，被积的那一项一致地小，于是

$$
\|e_{k+1}\|\le\big\|[F'(x^{(k)})]^{-1}\big\|\cdot L\|e_k\|\cdot\|e_k\|=O\big(\|e_k\|^2\big)
$$'''.split('\n')

L[i0:i1 + 1] = new
open(p, 'w', encoding='utf-8', newline='').write('\n'.join(L))
print('--- 替换后 ---')
M = '\n'.join(L).split('\n')
for i in range(i0 - 2, i0 + 40):
    print(i, '|', M[i][:130])
