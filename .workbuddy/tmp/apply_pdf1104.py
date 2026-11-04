# -*- coding: utf-8 -*-
"""把 CM+Opt_非线性.pdf（手写笔记）里真正的增量写进第 7 章笔记。"""
import os, sys
sys.stdout.reconfigure(encoding='utf-8')

BASE = r'D:\29469\Documents\notes\计算方法与优化'
CH7 = os.path.join(BASE, '第7章-非线性方程')
LINK = '[CM+Opt_ch4-非线性手写笔记](../原始材料/CM+Opt_ch4-非线性手写笔记.pdf)'

# ---------- 1) 四篇头部各加一行来源 ----------
heads = [
    ('7.1-非线性方程求根-二分法与不动点迭代.md',
     '> ' + LINK + ' §1 二分法、§2.1 不动点及其迭代策略、§2.2 迭代法收敛性质'),
    ('7.2-收敛性判据收敛阶与迭代加速-牛顿法与割线法.md',
     '> ' + LINK + ' §2.2 收敛性质、§2.3 迭代加速、§3 牛顿法'),
    ('7.3-非线性方程组-向量函数压缩映射与牛顿法.md',
     '> ' + LINK + ' §4.1 向量函数导数、§4.2 压缩映射、§4.3 方程组牛顿法'),
    ('7.4-非线性方程组的拟牛顿法.md',
     '> ' + LINK + ' §4.4 拟牛顿法'),
]
for fn, line in heads:
    p = os.path.join(CH7, fn)
    s = open(p, encoding='utf-8').read()
    if LINK in s:
        print('SKIP 已挂来源', fn)
        continue
    anchor = '> [返回总览]'
    assert s.count(anchor) >= 1, fn
    i = s.index(anchor)
    s = s[:i] + line + '\n' + s[i:]
    open(p, 'w', encoding='utf-8', newline='').write(s)
    print('OK   头部加来源', fn)

# ---------- 2) 7.2 头部：修正「课本体系」→「课件体系」 ----------
p = os.path.join(CH7, '7.2-收敛性判据收敛阶与迭代加速-牛顿法与割线法.md')
s = open(p, encoding='utf-8').read()
old = ('> 板书的节号是课本体系里的 **2.2 迭代法收敛性质**、'
       '**2.3 迭代加速收敛的方法**，与笔记的小节号不对应，按内容对齐即可')
new = ('> 板书与手写笔记用的是课件自己的节号：**1. 二分法**、**2. 不动点迭代法**'
       '（2.1 不动点与策略、2.2 收敛性质、2.3 迭代加速）、**3. 牛顿法**、'
       '**4. 非线性方程组**（4.1 导数、4.2 压缩映射、4.3 牛顿法、4.4 拟牛顿法）。'
       '这套编号不属于课本第七章，与笔记的 7.x 小节按内容对齐即可')
print('7.2 节号行命中', s.count(old))
assert s.count(old) == 1
s = s.replace(old, new)

# ---------- 3) 7.2 §9：补 2p-1 定理的出处与条件 ----------
old9 = '''Steffensen 的收敛阶有两条：

- 若 $g$ 是**线性**收敛（$p=1$）且 $g'(x^*)\\ne1$，则 Steffensen 迭代是 **$2$ 阶**收敛；
- 若 $g$ 是 $p$ 阶收敛（$p>1$），则 Steffensen 迭代是 **$2p-1$ 阶**收敛。

第一条是课本定理 5 的后半；第二条课本没有，课上补的。注意 $2p-1$ 只用于 $p>1$：$p=1$ 时 $2\\cdot1-1=1$ 与结论矛盾，线性收敛是单独一条。'''
new9 = '''Steffensen 的收敛阶有两条：

- 若 $g$ 是**线性**收敛（$p=1$）且 $g'(x^*)\\ne1$，则 Steffensen 迭代至少 **$2$ 阶**收敛；
- 若 $g$ 是 $p$ 阶收敛（$p>1$，超线性），则 Steffensen 迭代是 **$2p-1$ 阶**收敛。

**定理（手写笔记 §2.3）** 设 $x^*=g(x^*)$，且存在 $\\delta>0$ 使 $g$ 在 $U(x^*,\\delta)$ 内直到 $p-1$ 阶导数存在且连续，则上面两条成立。第一条即课本定理 5 的后半；第二条课本没有，是配套手写笔记 §2.3 记下的定理，课上照讲。

注意 $2p-1$ 只用于 $p>1$：$p=1$ 时 $2\\cdot1-1=1$ 与结论矛盾。要分成两条，根源在 $g'(x^*)$：线性收敛时 $g'(x^*)=\\lambda\\ne0$（只要求 $|\\lambda|<1$），超线性时 $g'(x^*)=0$，$\\varphi$ 在 $x^*$ 处的展开从不同的阶起步。'''
print('7.2 §9 段落命中', s.count(old9))
assert s.count(old9) == 1
s = s.replace(old9, new9)

pairs = [
    ('与课堂讲的 $2p-1$ 不一致', '与手写笔记 §2.3 的 $2p-1$ 不一致'),
    ('所以**课堂的 $2p-1$ 是对的**，笔记按课堂记。',
     '所以 **$2p-1$ 是对的**，笔记按手写笔记记。'),
]
for a, b in pairs:
    print('  §9 替换', s.count(a), a[:28])
    assert s.count(a) == 1
    s = s.replace(a, b)
open(p, 'w', encoding='utf-8', newline='').write(s)
print('7.2 完成')

# ---------- 4) 索引：手写笔记段落补一条 ----------
p = os.path.join(BASE, '00-索引.md')
s = open(p, encoding='utf-8').read()
anchor = ('  同一批里还有第 5 份 `cm+opt_05_lecture3-2_期望不等式与集中不等式`，'
          '实为**《工科概率论与数理统计》（刘常钰）Lecture 3-2** 的讲义转录'
          '（Markov／Chebyshev／Cauchy–Schwarz／Hoeffding），前缀 `cm+opt` 只是同一 OCR 服务的批量编号，'
          '不属本课程，已移入 `统计学完全教程/原始材料/`。')
add = '''
- 同批另有 [CM+Opt_ch4-非线性手写笔记](原始材料/CM+Opt_ch4-非线性手写笔记.pdf)（15 页，覆盖课件第四章全章：二分法 → 拟牛顿法，对应 7.1–7.4）。**尚未 OCR**，工作区内是 2.7 MB 压缩扫描版，14 MB 原件在 `桌面\\计算方法与优化\\课堂笔记\\CM+Opt_非线性.pdf`。逐页核对下来，内容与课堂录音稿互为印证，正文没有缺块；唯一补进笔记的是 7.2 §9 的 $2p-1$ 定理条件与出处。'''
print('索引锚点命中', s.count(anchor))
assert s.count(anchor) == 1
s = s.replace(anchor, anchor + '\n' + add)
open(p, 'w', encoding='utf-8', newline='').write(s)
print('索引完成')
