# -*- coding: utf-8 -*-
"""高精度计算 Steffensen 迭代函数 phi(x)（g = cos），用于画图。"""
from decimal import Decimal as D, getcontext

getcontext().prec = 70

PI = D("3.14159265358979323846264338327950288419716939937510582097494459230781640628620899")


def cos(x):
    x = D(x)
    s = D(1)
    term = D(1)
    n = 0
    while True:
        n += 2
        term = -term * x * x / (n * (n - 1))
        if abs(term) < D("1e-65"):
            break
        s += term
    return s


def g(x):
    return cos(x)


def phi(x):
    """Steffensen: phi(x) = (x*g(g(x)) - g(x)^2) / (x - 2g(x) + g(g(x)))"""
    x = D(x)
    gx = g(x)
    ggx = g(gx)
    num = x * ggx - gx * gx
    den = x - 2 * gx + ggx
    if den == 0:
        return None
    return num / den


# 不动点
x = D("0.7")
for _ in range(80):
    x = g(x)
xs = x
print("x* =", xs)
print("g'(x*) = -sin(x*) ;  |g'| ≈", abs(g(xs) - xs) / abs(xs) if xs else 0)

# 验证 phi(x*) = x*, phi'(x*) = 0
print("phi(x*) =", phi(xs))
h = D("1e-8")
print("phi(x*+h) - phi(x*-h) ≈", (phi(xs + h) - phi(xs - h)) / (2 * h))

# 采样
print("\n采样：")
pts = []
for i in range(0, 31):
    xv = D("0.60") + D("0.28") * i / 30
    v = phi(xv)
    if v is None:
        continue
    pts.append((float(xv), float(v)))
    if i % 5 == 0:
        print("  x=%.4f  phi=%.6f" % (float(xv), float(v)))

with open(r"D:\29469\Documents\notes\.workbuddy\tmp\stef_data.txt", "w", encoding="utf-8") as f:
    for a, b in pts:
        f.write("%.6f %.9f\n" % (a, b))
print("\n写出 %d 个点" % len(pts))
