# -*- coding: utf-8 -*-
"""幂法转向：两组 |λ2/λ1| 的真实迭代角度，用于决定插图数据。"""
import math, sys
sys.stdout.reconfigure(encoding="utf-8")

def run(l1, l2, steps):
    """对称矩阵 [[a,b],[b,a]]，特征值 a+b=l1, a-b=l2；x1=(1,1)/√2, x2=(1,-1)/√2。
    v0 = (1,0) = (x1+x2)/√2，即 α1=α2=1/√2。"""
    out = []
    for k in range(steps + 1):
        a = l1 ** k
        b = l2 ** k
        v = (a + b, a - b)              # 正比于 v^(k)
        ang = math.degrees(math.atan2(v[1], v[0]))
        out.append((k, ang))
    return out

for l1, l2 in [(2.0, 0.4), (2.0, 1.6)]:
    seq = run(l1, l2, 5)
    print("λ1=%.1f λ2=%.1f  比值=%.2f" % (l1, l2, abs(l2 / l1)))
    print("  角度:", "  ".join("%d:%.2f°" % (k, a) for k, a in seq))
    err = [45 - a for k, a in seq]
    print("  角度差:", "  ".join("%.2f" % e for e in err))
    print("  相邻比值:", "  ".join("%.3f" % (err[i + 1] / err[i]) for i in range(len(err) - 1)))
    a_, b_ = l1 + 0 + (l2), 0
    print("  对应矩阵 [[%.2f, %.2f],[%.2f, %.2f]]" % ((l1 + l2) / 2, (l1 - l2) / 2, (l1 - l2) / 2, (l1 + l2) / 2))
    print()
