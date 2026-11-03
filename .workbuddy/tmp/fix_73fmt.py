# -*- coding: utf-8 -*-
import sys, re
sys.stdout.reconfigure(encoding='utf-8')
p = r'D:\29469\Documents\notes\计算方法与优化\第7章-非线性方程\7.3-非线性方程组-向量函数压缩映射与牛顿法.md'
L = open(p, encoding='utf-8').read().split('\n')

i0 = next(i for i, l in enumerate(L) if l.startswith('**证明**（课堂四步'))
i1 = next(i for i, l in enumerate(L) if l.startswith('📌 **另一条路线：积分形式**'))
print('重写 L[%d:%d]' % (i0, i1))
print('被删首行:', L[i0][:60])
print('被删末行:', L[i1][:60])

new = r'''**证明**（课堂四步，只用 $F'$ 的连续性）。这条路要的结论比平方收敛**弱**——只到超线性，所以条件也弱：只要 $F'$ 连续，不要 Lipschitz。思路一句话：把误差写成「一个 Jacobian 的逆 × 一个二阶小量加一个一阶小量」，再证那个逆一致有界。

记 $e_k=x^{(k)}-x^*$，$\alpha=\big\|[F'(x^*)]^{-1}\big\|>0$。

1. **先用量把邻域压小。** 由 $F'$ 在 $x^*$ 处连续，对任意 $\varepsilon>0$ 存在 $\delta>0$，使 $x\in U(x^*,\delta)\subset S$ 时
   $$
   \big\|F'(x)-F'(x^*)\big\|<\varepsilon .
   $$
   后面会看到，要 $\varepsilon<\dfrac{1}{2\alpha}$ 才够用——这个量的用处要到第 3 步才显出来。
2. **把牛顿步的误差拆成两块。** 由 $F(x^*)=0$ 与 $x^{(k+1)}=x^{(k)}-[F'(x^{(k)})]^{-1}F(x^{(k)})$，
   $$
   e_{k+1}=\big[F'(x^{(k)})\big]^{-1}\Big\{F'(x^{(k)})e_k-\big[F(x^{(k)})-F(x^*)\big]\Big\}
   $$
   在花括号里加一项、减一项 $F'(x^*)e_k$，就凑成两块：
   $$
   F'(x^{(k)})e_k-F(x^{(k)})=\underbrace{-\big[F(x^{(k)})-F(x^*)-F'(x^*)e_k\big]}_{\text{二阶小量}}-\underbrace{\big[F'(x^{(k)})-F'(x^*)\big]e_k}_{\text{一阶小量}}
   $$
   取范数、用三角不等式：
   $$
   \|e_{k+1}\|\le\big\|[F'(x^{(k)})]^{-1}\big\|\Big\{\big\|F(x^{(k)})-F(x^*)-F'(x^*)e_k\big\|+\big\|\big[F'(x^{(k)})-F'(x^*)\big]e_k\big\|\Big\}
   $$
   第一块是 $F$ 在 $x^*$ 处一阶展开的余项，由可微性它是 $O(\|e_k\|^2)$；第二块由第 1 步不超过 $\varepsilon\|e_k\|$。
3. **证 Jacobian 的逆一致有界。** 这是全证明的技术核心——不先把这个逆控住，前面拆得再干净也没用。把 $[F'(x^{(k)})]^{-1}$ 用 $[F'(x^*)]^{-1}$ 表示出来：
   $$
   \big[F'(x^{(k)})\big]^{-1}=\big[F'(x^*)\big]^{-1}\Big(I-\underbrace{\big(I-[F'(x^*)]^{-1}F'(x^{(k)})\big)}_{=:T}\Big)^{-1}
   $$
   $T$ 的大小由第 1 步控制：$\|T\|\le\alpha\varepsilon<\frac12$。于是用 $\|(I-T)^{-1}\|\le\dfrac{1}{1-\|T\|}$，
   $$
   \big\|[F'(x^{(k)})]^{-1}\big\|\le\frac{\alpha}{1-\alpha\varepsilon}\le2\alpha=:M .
   $$
   顺带把定理的第一条结论也证出来了：邻域内每一点的 $F'$ 都可逆，因为上面这个构造本身就给出了逆。
4. **收尾：比值趋于零。** 把第 2、3 步合起来，
   $$
   \|e_{k+1}\|\le M\big(O(\|e_k\|^2)+\varepsilon\|e_k\|\big)
   \quad\Longrightarrow\quad
   \frac{\|e_{k+1}\|}{\|e_k\|}\le M\Big(\frac{O(\|e_k\|^2)}{\|e_k\|}+\varepsilon\Big)\xrightarrow[k\to\infty]{}0 .
   $$
   右端趋于 $M\varepsilon$，而 $\varepsilon$ 是任意给定的，所以比值的极限为零——**超线性收敛**。

这条证明有两处值得记住：一是它**没有**用 Lipschitz 条件，所以结论只到超线性；要平方收敛，得把第 2 步那块 $O(\|e_k\|^2)$ 收紧成「$\le C\|e_k\|^2$」，那就需要 $F'$ Lipschitz（正是定理 9 后半加的条件）。二是全证明**没有出现中值定理**——这不是疏漏，而是向量情形本来的样子，见下面。
'''.split('\n')

L[i0:i1] = new
open(p, 'w', encoding='utf-8', newline='').write('\n'.join(L))
print('完成，新行数', len(L))
M = '\n'.join(L).split('\n')
for k in range(i0, min(i0 + 8, len(M))):
    print(k, '|', M[k][:120])
print('...')
for k in range(i1 - 26, i1 + 4):
    print(k, '|', M[k][:120])
