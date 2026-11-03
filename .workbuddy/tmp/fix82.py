# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
p = r'D:\29469\Documents\notes\计算方法与优化\第8章-矩阵特征值\8.2-幂法与反幂法.md'
s = open(p, encoding='utf-8').read()

pairs = [
    ('> 对应课本：李庆扬《数值分析（第五版）》**§8.2 幂法及反幂法**——§8.2.1 幂法（p.245）、§8.2.2 加速方法（p.248）、§8.2.3 反幂法（p.251）',
     '> 对应课本：李庆扬《数值分析（第五版）》**§8.2 幂法及反幂法**——§8.2.1 幂法（p.245，定理 7 未规范化、定理 8 规范化）、§8.2.2 加速方法（p.248，原点平移法）、§8.2.3 反幂法（p.251）。**课本的规范化写法与板书不同但等价**，见 §3.2'),
    # 假设里补"主特征值为实根"
    ('2. **$\\lambda_1$ 是按模最大的单特征值**：',
     '2. **$\\lambda_1$ 是按模最大的单特征值**（课本还要求它是**实根**，否则规范化后的符号会来回震荡）：'),
]
for a, b in pairs:
    n = s.count(a)
    print(('OK  ' if n == 1 else '!! %d ' % n) + a[:50].replace('\n', '|'))
    s = s.replace(a, b)

# 在「符号函数到底在防什么」之后补课本写法的对照
anchor = '乘上 $\\operatorname{sgn}(\\varphi)$、强制最大分量为 $+1$，读出来的符号才是 $\\lambda_1$ 真实的符号（$\\lambda_1$ 本身当然可能是负的，那是它的真符号，不是规范化造成的假象）。'
assert s.count(anchor) == 1, s.count(anchor)
add = anchor + r'''

**课本的写法更省一步**：课本把「$\vec z$ 的**带符号**最大分量」直接记成 $\max\{\vec z\}$——定义是「若有 $|z_{i_0}|=\max_i|z_i|$，则 $\max\{\vec z\}=z_{i_0}$」，注意右端**带符号**，不是绝对值。于是规范化写成

$$
\vec v^{(k+1)}=\frac{\vec z^{(k+1)}}{\max\{\vec z^{(k+1)}\}},
$$

一步就把长度和符号同时处理了。对照一下就知道两者是一回事：

$$
\operatorname{sgn}(\varphi)\cdot\|\vec z\|_\infty=\operatorname{sgn}(\varphi)\,|\varphi|=\varphi=\max\{\vec z\} .
$$

课上把它拆成"除绝对值、再乘符号函数"两步，写法啰嗦，但把"为什么需要符号"这件事暴露得更清楚——课本那个 $\max\{\cdot\}$ 的定义容易看漏"带符号"三个字。'''
s = s.replace(anchor, add, 1)

# 在 📌 瑞利商那条之前补原点平移法
anchor2 = '📌 再往下还有**瑞利商迭代**'
assert s.count(anchor2) == 1
add2 = r'''📌 课本 §8.2.2 的加速方法是**原点平移法**：取 $B=A-pI$（$p$ 是选定的参数）。$B$ 的特征值是 $\lambda_i-p$，特征向量与 $A$ 相同，所以对 $B$ 用幂法，收敛因子变成

$$
\frac{|\lambda_2-p|}{|\lambda_1-p|},
$$

选合适的 $p$ 可以让这个比值比原来的 $|\lambda_2/\lambda_1|$ 小得多——这就是"加速"的全部内容。代价是 $p$ 得靠对特征值分布的估计来选（圆盘定理正好能给），选坏了反而更慢。课上没有展开这一层，只提了瑞利商。

'''
s = s.replace(anchor2, add2 + anchor2, 1)

open(p, 'w', encoding='utf-8', newline='').write(s)
print('已改 8.2')
