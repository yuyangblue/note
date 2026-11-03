# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
p = r'D:\29469\Documents\notes\计算方法与优化\第7章-非线性方程\7.2-收敛性判据收敛阶与迭代加速-牛顿法与割线法.md'
L = open(p, encoding='utf-8').read().split('\n')

# 定位四步证明：从「**证明**（四步）：」到第 4 步那一行
i0 = next(i for i, l in enumerate(L) if l.startswith('**证明**（四步）：'))
i1 = next(i for i in range(i0, len(L)) if L[i].startswith('4. 有了「映进自身」'))
print('替换 L[%d:%d]' % (i0, i1 + 1))
for l in L[i0:i1 + 1]:
    print('  -', l[:80])

new = r'''**证明**（四步）。目标很明确：§2 的全局定理只要两样东西——一个**不变的闭区间**，和区间上**小于 1 的压缩常数**。四步分别是：把单点信息 $|g'(x^*)|<1$ 换成整段上的常数 $L$、把 $L$ 换成 Lipschitz 条件、验证区间不变、然后交给全局定理。

1. **先划一条安全线。** 手上只有一个数 $|g'(x^*)|<1$，要它管住整段区间，就得留余量：取 $\varepsilon>0$ 使 $L:=|g'(x^*)|+\varepsilon<1$。再由 $g'$ 连续，把这根水平线压到 $x^*$ 附近——存在 $\delta>0$，使 $x\in U(x^*,\delta)$ 时 $|g'(x)|\le L$。（具体取 $\delta=\dfrac{1-|g'(x^*)|}{2}$ 就够，此时 $L=(1+|g'(x^*)|)/2<1$。）
2. **换成 Lipschitz 条件。** 中值定理把「导数有界」翻译成 §2 认得的语言：对 $x\in U(x^*,\delta)$，
   $|g(x)-g(x^*)|=|g(x)-x^*|\le L|x-x^*|$。
   注意这里用的是区间上**每一点**的导数有界，而不是只在 $x^*$ 一点——第 1 步把条件铺到整段，正是为这一步服务的。
3. **让区间自成一体。** 全局定理还要求 $g$ 把区间映进自己，否则迭代可能跑出去，§2 的自映射条件就断了。由 $|x-x^*|\le\delta$ 得
   $|g(x)-x^*|\le L\delta<\delta$，即
   $g\big(U(x^*,\delta)\big)\subset U(x^*,\delta)=[x^*-\delta,\,x^*+\delta]$
   ——**$g$ 把这个小闭区间映进自身**。
4. **交给全局定理。** 到这里 $U(x^*,\delta)$ 上两个条件都齐了（自映射 + Lipschitz 常数 $L<1$），直接套 §2 的定理，即得对任意 $x_0\in U(x^*,\delta)$ 收敛。整个证明没有用到 $g$ 在区间外的任何信息，这正是「局部」二字的来源。'''.split('\n')

L[i0:i1 + 1] = new
open(p, 'w', encoding='utf-8', newline='').write('\n'.join(L))
print('--- 替换后 ---')
M = '\n'.join(L).split('\n')
for i in range(i0 - 2, i0 + 26):
    print(i, '|', M[i][:150])
