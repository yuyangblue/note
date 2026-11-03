# -*- coding: utf-8 -*-
import os, sys
sys.stdout.reconfigure(encoding="utf-8")
D = r"D:\29469\Documents\notes\计算方法与优化\第7章-非线性方程"
F71 = os.path.join(D, "7.1-非线性方程求根-二分法与不动点迭代.md")
F72 = os.path.join(D, "7.2-收敛性判据收敛阶与迭代加速-牛顿法与割线法.md")

# 7.2 §2：删掉重抄的证明后，后面的「证明写到这里收住」失去了指代
s = open(F72, encoding="utf-8").read()
old = "证明写到这里收住，顺带说了一句：从数学分析的角度还可以再讨论不动点的唯一性、误差估计等一系列性质，课上不展开（唯一性和误差估计在 7.1 §8–§9 已经写过）。"
new = "课堂上的证明写到这里就停住，顺带说了一句：从数学分析的角度还可以再讨论不动点的唯一性、误差估计等一系列性质，课上不展开（唯一性和误差估计在 7.1 §8–§9 已经写过）。"
print("7.2 §2 收尾  count=%d" % s.count(old))
s = s.replace(old, new)
open(F72, "w", encoding="utf-8").write(s)

# 7.1 §13：把「本节末尾提到的」改成明确指向 §11
s = open(F71, encoding="utf-8").read()
old = "下一讲 [7.2 收敛性判据、收敛阶与迭代加速](7.2-收敛性判据收敛阶与迭代加速-牛顿法与割线法.md) 会先把本节末尾提到的局部收敛性、收敛阶两条定理补上完整证明，再讲加速与牛顿法："
new = "下一讲 [7.2 收敛性判据、收敛阶与迭代加速](7.2-收敛性判据收敛阶与迭代加速-牛顿法与割线法.md) 会把 §11 那两条定理的证明补上，再讲加速与牛顿法："
print("7.1 §13  count=%d" % s.count(old))
s = s.replace(old, new)
open(F71, "w", encoding="utf-8").write(s)
print("done")
