# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
p = r'D:\29469\Documents\notes\计算方法与优化\第7章-非线性方程\7.2-收敛性判据收敛阶与迭代加速-牛顿法与割线法.md'
L = open(p, encoding='utf-8').read().split('\n')

# 定位导航表区块：从「整节的路线可以按这三问查表」到「那就是 7.3。」
i0 = next(i for i, l in enumerate(L) if l.startswith('整节的路线可以按这三问查表'))
i1 = next(i for i, l in enumerate(L) if l.startswith('牛顿法和割线法都是「第三问」的答案'))
print('删除区间 L[%d:%d]' % (i0, i1 + 1))
for l in L[i0:i1 + 1]:
    print('  -', l[:70])

# 连同前面的一个空行一起删，保留后面那个空行
start = i0
if L[start - 1].strip() == '':
    start -= 1
del L[start:i1 + 1]

open(p, 'w', encoding='utf-8', newline='').write('\n'.join(L))
print('--- 删除后 ---')
for i in range(94, 104):
    print(i, '|', L[i][:120])
