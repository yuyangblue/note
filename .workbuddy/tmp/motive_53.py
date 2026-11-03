# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
p = r'D:\29469\Documents\notes\计算方法与优化\第5章-解线性方程组的直接法\5.3-矩阵三角分解法.md'
L = open(p, encoding='utf-8').read().split('\n')

i0 = next(i for i, l in enumerate(L) if l.startswith('**证明梗概**：'))
i1 = next(i for i in range(i0, len(L)) if L[i].startswith('5. $D$ 对角元全正'))
print('替换 L[%d:%d]' % (i0, i1 + 1))
for l in L[i0:i1 + 1]:
    print('  -', l[:80])

new = r'''**证明梗概**。整条路只干一件事：把 $A=LDL^T$ 里的 $D$ 拆成 $D^{1/2}D^{1/2}$，从而合并进 $L$。难点只有一个——**$D$ 的对角元必须为正，开方才有意义**。所以前 3 步全在证这件事，第 4、5 步才真正做分解。

1. **先拿到 LU 分解。** $A$ 正定 ⇒ 各阶顺序主子式 $\det(A_p)>0$ ⇒ 由定理 3（LU 存在唯一性）分解已存在，不用再构造。
2. **把对角元写成行列式之比。** 取顺序主子块 $A_p=L_pU_p$，两边取行列式（$\det(L_p)=1$）得 $\det(A_p)=\det(U_p)=u_{11}u_{22}\cdots u_{pp}>0$。这一步本身不产生结论，只是把「未知的 $u_{pp}$」换成「已知的 $A_p$ 的行列式」。
3. **确认每个对角元都为正。** 由 $p=1,2,\dots,n$ 递推：$u_{11}=\det(A_1)>0$，而 $u_{pp}=\det(A_p)/\det(A_{p-1})$ 是正数除正数，故**$u_{pp}>0$**。这是全证明的关键一步——它说明开方处处合法，而这句话之所以成立，全靠 $A$ 正定。
4. **用对称性把上三角换成转置。** 由 $A=A^T$ 与 LU 分解的唯一性得 $U=DL^T$（$D=\operatorname{diag}(u_{pp})$），即 $A=LDL^T$。对称性在这里的作用是把第二因子整个省掉。
5. **开平方合并。** $D$ 的对角元全正 ⇒ $D^{1/2}$ 是实矩阵，于是
   $A=LD^{1/2}D^{1/2}L^T=(LD^{1/2})(LD^{1/2})^T$，取 $\tilde L=LD^{1/2}$ 即得 $A=\tilde L\tilde L^T$。限定对角元为正时，$\tilde L$ 由 $L$、$D$ 唯一确定，唯一性得证。'''.split('\n')

L[i0:i1 + 1] = new
open(p, 'w', encoding='utf-8', newline='').write('\n'.join(L))
print('--- 替换后 ---')
M = '\n'.join(L).split('\n')
for k in range(i0 - 2, min(i0 + 22, len(M))):
    print(k, '|', M[k][:130])
