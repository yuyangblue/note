# -*- coding: utf-8 -*-
"""按行号替换：消除第 7 章三篇笔记之间的重复。"""
import os, sys

sys.stdout.reconfigure(encoding="utf-8")
D = r"D:\29469\Documents\notes\计算方法与优化\第7章-非线性方程"
BS = chr(92)

F71 = os.path.join(D, "7.1-非线性方程求根-二分法与不动点迭代.md")
F72 = os.path.join(D, "7.2-收敛性判据收敛阶与迭代加速-牛顿法与割线法.md")
F73 = os.path.join(D, "7.3-非线性方程组-向量函数压缩映射与牛顿法.md")


def show(path, a, b):
    L = open(path, encoding="utf-8").read().split("\n")
    print("----", os.path.basename(path), a, b)
    for i in range(a, min(b, len(L))):
        print("  ", i, "|", L[i][:120])


def replace_block(path, start, end, new_lines, tag):
    """把 [start, end) 行替换成 new_lines（列表）。"""
    L = open(path, encoding="utf-8").read().split("\n")
    print("%-6s %s  行 %d-%d → %d 行" % (tag, os.path.basename(path)[:5], start, end - 1, len(new_lines)))
    show(path, start, end)
    L[start:end] = new_lines
    open(path, "w", encoding="utf-8").write("\n".join(L))


# ------------------------------------------------- 7.1 §11：删定义与证明思路，只留定理骨架
new71 = [
    "**定义（局部收敛）** 设 $g$ 在区间 $I$ 上有不动点 $x^*$。若存在 $" + BS + "delta>0$，使对任意 $x_0" + BS + "in U(x^*," + BS + "delta)" + BS + "subset I$，由迭代产生的序列满足",
    "",
    "$$",
    BS + "{x_k}" + BS + "}" + BS + "subset U(x^*," + BS + "delta),\\qquad " + BS + "lim_{k" + BS + "to" + BS + "infty}x_k=x^*",
    "$$",
    "",
    "则称该迭代在 $x^*$ 处**局部收敛**。换句话说：初值只在 $x^*$ 附近取，且序列**不许跑出**这个邻域——既要求收敛，也要求过程中不越界。",
    "",
    "**定理 3**（局部收敛定理）设 $x^*=g(x^*)$，$g$ 在 $x^*$ 的某个邻域内导数存在且连续，且 $|g'(x^*)|<1$，则迭代 $x_{k+1}=g(x_k)$ 在 $x^*$ 处局部收敛。",
    "",
    "收敛之后还要比较快慢。**收敛阶**说的是误差被压下去的速度：若 $|e_{k+1}|$ 与 $|e_k|^p$ 成正比（$e_k=x_k-x^*$），就说迭代是 $p$ 阶收敛的；$p=1$ 叫**线性收敛**，$p>1$ 叫**超线性收敛**，$p=2$ 叫**平方收敛**。精确的定义式（课本定义 2，含渐近误差常数 $C$）见 [7.2](7.2-收敛性判据收敛阶与迭代加速-牛顿法与割线法.md) §4.1。",
]
replace_block(F71, 283, 296, new71, "7.1")

# ------------------------------------------------- 7.2 §3.1：定义改为引用 7.1
new72 = [
    "**定义（局部收敛，课本定义 1）** 已在 [7.1](7.1-非线性方程求根-二分法与不动点迭代.md) §11 给出，这里不重抄。",
]
replace_block(F72, 121, 128, new72, "7.2")

# ------------------------------------------------- 7.3 §15：点明是标量版的向量版
new73a = [
    "这一节是 [7.1](7.1-非线性方程求根-二分法与不动点迭代.md) 定理 2 的**向量版**：区间 $[a,b]$ 换成区域 $D_0$，绝对值换成范数，Lipschitz 不等式照样成立，结论照样是「唯一不动点 + 任意初值收敛」。",
    "",
]
replace_block(F73, 367, 367, new73a, "7.3a")

# ------------------------------------------------- 7.3 §16：定义首句改为引用
old16 = "**定义（局部收敛）**：设 $x^*=" + BS + "Phi(x^*)$。若在 $x^*$ 附近存在邻域 $S$，使得对任意 $x^{(0)}" + BS + "in S$，迭代产生的序列满足"
new16 = ("**定义（局部收敛）**：与 [7.2](7.2-收敛性判据收敛阶与迭代加速-牛顿法与割线法.md) §3.1 相同，只是把邻域从 $U(x^*," + BS + "delta)$ 换成球 $S$：若在 $x^*$ 附近存在邻域 $S$，使得对任意 $x^{(0)}" + BS + "in S$，迭代产生的序列满足")
s = open(F73, encoding="utf-8").read()
print("7.3b  7.3 定义首句  count=%d" % s.count(old16))
s = s.replace(old16, new16)
open(F73, "w", encoding="utf-8").write(s)
