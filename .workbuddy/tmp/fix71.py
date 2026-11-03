# -*- coding: utf-8 -*-
import os, sys
sys.stdout.reconfigure(encoding="utf-8")
F = r"D:\29469\Documents\notes\计算方法与优化\第7章-非线性方程\7.1-非线性方程求根-二分法与不动点迭代.md"
BS = chr(92)
old = BS + "{x_k}" + BS + "}" + BS + "subset U(x^*," + BS + "delta)," + BS + "qquad " + BS + "lim_{k" + BS + "to" + BS + "infty}x_k=x^*"
new = BS + "{x_k" + BS + "}" + BS + "subset U(x^*," + BS + "delta)," + BS + "qquad " + BS + "lim_{k" + BS + "to" + BS + "infty}x_k=x^*"
s = open(F, encoding="utf-8").read()
print("count =", s.count(old))
s = s.replace(old, new)
open(F, "w", encoding="utf-8").write(s)
print(repr([l for l in s.split("\n") if "x_k" in l and "subset U" in l][0]))
