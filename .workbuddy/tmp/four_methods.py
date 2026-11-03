# -*- coding: utf-8 -*-
"""同题四法：x^3-x-1=0，根 1.3247179572447460，x0=1.5"""
import sys
from decimal import Decimal, getcontext
getcontext().prec = 40
sys.stdout.reconfigure(encoding='utf-8')

XS = 1.3247179572447460259609088544780973407
TOL = 1e-6


def f(x):
    return x ** 3 - x - 1


def fp(x):
    return 3 * x ** 2 - 1


def g(x):  # cbrt(x+1)
    return (x + 1) ** (1 / 3)


print('根 =', XS)
print('g\'(x*) =', 1 / (3 * (XS + 1) ** (2 / 3)))


def run_fixed(x0, n=12):
    xs = [x0]
    for _ in range(n):
        xs.append(g(xs[-1]))
    return xs


def aitken(xs):
    """对序列前若干项做 Aitken 外推"""
    out = []
    for k in range(len(xs) - 2):
        d1 = xs[k + 1] - xs[k]
        d2 = xs[k + 2] - 2 * xs[k + 1] + xs[k]
        out.append(xs[k] - d1 * d1 / d2)
    return out


def run_stef(x0, n=8):
    xs = [x0]
    for _ in range(n):
        x = xs[-1]
        y = g(x)
        z = g(y)
        den = z - 2 * y + x
        if den == 0:
            break
        xs.append(x - (y - x) ** 2 / den)
    return xs


def run_newton(x0, n=8):
    xs = [x0]
    for _ in range(n):
        x = xs[-1]
        xs.append(x - f(x) / fp(x))
    return xs


def run_secant(x0, x1, n=8):
    xs = [x0, x1]
    for _ in range(n):
        a, b = xs[-1], xs[-2]
        den = f(b) - f(a)
        if den == 0:
            break
        xs.append(b - f(b) * (b - a) / den)
    return xs


def steps_to(xs, tol=TOL):
    for i, x in enumerate(xs):
        if abs(x - XS) < tol:
            return i
    return None


fixed = run_fixed(1.5)
print('\n--- 不动点 g=cbrt(x+1) ---')
for i, x in enumerate(fixed[:6]):
    print(' x%d = %.10f  e=%.2e' % (i, x, abs(x - XS)))

ai = aitken(fixed)
print('\n--- Aitken ---')
for i, x in enumerate(ai[:5]):
    print(' xbar%d = %.10f  e=%.2e' % (i, x, abs(x - XS)))

st = run_stef(1.5)
print('\n--- Steffensen ---')
for i, x in enumerate(st[:6]):
    print(' x%d = %.10f  e=%.2e' % (i, x, abs(x - XS)))

nw = run_newton(1.5)
print('\n--- Newton ---')
for i, x in enumerate(nw[:6]):
    print(' x%d = %.10f  e=%.2e' % (i, x, abs(x - XS)))

sc = run_secant(1.5, 1.4)
print('\n--- Secant (1.5, 1.4) ---')
for i, x in enumerate(sc[:7]):
    print(' x%d = %.10f  e=%.2e' % (i, x, abs(x - XS)))

print('\n--- 到 1e-6 需要几步 ---')
print(' 不动点', steps_to(fixed))
print(' Aitken（以 xbar_k 计，k 为外推序号）', steps_to(ai))
print(' Steffensen', steps_to(st))
print(' Newton', steps_to(nw))
print(' Secant', steps_to(sc))
