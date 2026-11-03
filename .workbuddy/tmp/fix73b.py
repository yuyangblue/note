# -*- coding: utf-8 -*-
import os, re, sys
sys.stdout.reconfigure(encoding="utf-8")
D = r"D:\29469\Documents\notes\计算方法与优化\第7章-非线性方程"
BS = chr(92)

F71 = os.path.join(D, "7.1-非线性方程求根-二分法与不动点迭代.md")
F73 = os.path.join(D, "7.3-非线性方程组-向量函数压缩映射与牛顿法.md")

# ---- 7.3 §15 标题后补空行
L = open(F73, encoding="utf-8").read().split("\n")
i = L.index("## 15. 全局收敛：压缩映射原理（定理 7）")
if L[i + 1].strip():
    L.insert(i + 1, "")
    print("7.3 标题后已插入空行")
# 连续空行压成一个
out = []
for x in L:
    if x == "" and out and out[-1] == "":
        continue
    out.append(x)
print("7.3 行数 %d → %d" % (len(L), len(out)))
open(F73, "w", encoding="utf-8").write("\n".join(out))

# ---- 7.1 定理 4 补上「p 为整数」，并指向 7.2
s = open(F71, encoding="utf-8").read()
old = ("**定理 4**（收敛阶判定）对迭代 $x_{k+1}=g(x_k)$，若 $g^{(p)}$ 在根 $x^*$ 邻近连续，且")
new = ("**定理 4**（收敛阶判定）对迭代 $x_{k+1}=g(x_k)$，若 $p" + BS + "ge1$ 为**整数**、$g^{(p)}$ 在根 $x^*$ 邻近连续，且")
print("7.1 定理 4  count=%d" % s.count(old))
s = s.replace(old, new)
open(F71, "w", encoding="utf-8").write(s)

# ---- 7.3 定理 7 条件 1 指向 §14 的压缩定义
s = open(F73, encoding="utf-8").read()
old = ("1. 存在闭集 $D_0" + BS + "subset D$ 与常数 $L" + BS + "in(0,1)$，使 $" + BS + BS + "Phi(x)-" + BS + "Phi(y)" + BS + BS + "le L" + BS + BS + "x-y" + BS + BS + "$，$" + BS + "forall x,y" + BS + "in D_0$；")
if old not in s:
    # 用更宽松的定位：找到含 "存在闭集 $D_0" 的行
    for n, line in enumerate(s.split("\n"), 1):
        if "存在闭集 $D_0" in line:
            print("7.3 定理 7 条件 1 实际行 %d: %s" % (n, line))
            old = line
            break
new = ("1. 存在闭集 $D_0" + BS + "subset D$ 与常数 $L" + BS + "in(0,1)$，使 $" + BS + "Phi$ 在 $D_0$ 上是**压缩**的（即对任意 $x,y" + BS + "in D_0$ 有 $" + BS + BS + "Phi(x)-" + BS + "Phi(y)" + BS + BS + "le L" + BS + BS + "x-y" + BS + BS + "$，压缩的定义见 §14）；")
s = s.replace(old, new)
open(F73, "w", encoding="utf-8").write(s)
print("7.3 定理 7 条件 1 已改写")
