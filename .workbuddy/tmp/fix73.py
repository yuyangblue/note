# -*- coding: utf-8 -*-
import os, re, sys
sys.stdout.reconfigure(encoding="utf-8")
D = r"D:\29469\Documents\notes\计算方法与优化\第7章-非线性方程"
BS = chr(92)

# --- 修 7.3 §15 的空行
F73 = os.path.join(D, "7.3-非线性方程组-向量函数压缩映射与牛顿法.md")
L = open(F73, encoding="utf-8").read().split("\n")
i = L.index("## 15. 全局收敛：压缩映射原理（定理 7）")
print("7.3 标题行索引", i, "| 下一行:", repr(L[i + 1][:40]), "| 后两行:", repr(L[i + 2]), repr(L[i + 3]))
if L[i + 1].strip() and not L[i + 1].startswith("这"):
    L.insert(i + 1, "")
    print("  → 已在标题后插入空行")
# 清掉连续三空
out = []
for x in L:
    if x == "" and len(out) >= 2 and out[-1] == "" and out[-2] == "":
        continue
    out.append(x)
print("  → 行数 %d → %d" % (len(L), len(out)))
open(F73, "w", encoding="utf-8").write("\n".join(out))

# --- 机检：三篇里的定理/定义/推论清单
print("\n===== 三篇的定理与定义清单 =====")
for fn in sorted(os.listdir(D)):
    if not fn.endswith(".md"):
        continue
    print("\n###", fn[:4])
    for n, line in enumerate(open(os.path.join(D, fn), encoding="utf-8").read().split("\n"), 1):
        m = re.match(r"^\*\*(定理|定义|推论|命题)", line)
        if m:
            t = re.sub(r"[*$\\]", "", line)
            print("  %4d  %s" % (n, t[:96]))
