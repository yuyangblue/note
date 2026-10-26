# -*- coding: utf-8 -*-
import io, os, re

base = r'D:\29469\Documents\notes'
p05 = os.path.join(base, '统计学完全教程', '第2章 随机变量',
                   'p05 第2章 随机变量（三）重要的连续分布.md')
M = '概率论MIT/笔记'

s = io.open(p05, encoding='utf-8').read()

# 1) 拆掉之前单独加的「配套笔记 / 延伸阅读」块
lines = s.split('\n')
out = []
for l in lines:
    if l.startswith('> **配套笔记**') or l.startswith('> **延伸阅读**'):
        if out and out[-1] == '':
            out.pop()
        continue
    out.append(l)
s = '\n'.join(out)


def sub1(text, old, new):
    if text.count(old) != 1:
        raise SystemExit('ANCHOR x%d: %s' % (text.count(old), old[:50]))
    return text.replace(old, new)


def append_before(text, marker, add):
    """把 add 接到 marker 之前最后一个非空行末尾（自然嵌进原段）"""
    i = text.index(marker)
    j = i
    while j > 0 and text[j - 1] in '\n \t':
        j -= 1
    k = text.rfind('\n', 0, j)
    line = text[k + 1:j]
    if not line:
        raise SystemExit('EMPTY LINE for marker %r' % marker)
    return text[:j] + add + text[j:]


# 2) 嵌进正文的括注
s = sub1(s,
         '概率由积分给出（$P(a < X < b) = \\int_a^b f(x)dx$）。',
         '概率由积分给出（$P(a < X < b) = \\int_a^b f(x)dx$；PDF 与 CDF 的一般理论见 `%s/03-一般随机变量/L08 连续随机变量与PDF.md` §1）。' % M)

s = sub1(s,
         '统计推断几乎都围绕它展开。',
         '统计推断几乎都围绕它展开（CLT 详见 `%s/05-极限定理/L19 中心极限定理.md` §1）。' % M)

s = sub1(s,
         '（见 p08 变换）。',
         '（见 p08 变换；逆变换采样的具体做法见 `%s/04-随机变量进一步专题/L11 导出分布.md` §5；均匀"等长区间等概率"的严格说法见 `%s/03-一般随机变量/L08 连续随机变量与PDF.md` §2.1）。' % (M, M))

s = sub1(s,
         '许多自然现象可以用正态分布近似；后面将看到**中心极限定理**表明随机变量和的分布可以用正态分布近似。',
         '许多自然现象可以用正态分布近似；后面将看到**中心极限定理**表明随机变量和的分布可以用正态分布近似（详见 `%s/05-极限定理/L19 中心极限定理.md` §1）。' % M)

s = append_before(s, '\n### 3.2 概率计算（标准化）',
                  '（同一结论的另一份配平方推导见 `%s/04-随机变量进一步专题/L12 独立随机变量之和与协方差.md` §2.1。）' % M)

s = append_before(s, '\n---\n\n## 4. 指数分布',
                  '（$1/\\sqrt{2\\pi}$ 与 $1/\\sigma$ 因子的来历、查表演算见 `%s/03-一般随机变量/L08 连续随机变量与PDF.md` §2.2–2.3。）' % M)

s = sub1(s,
         '（可用生存函数 $S(x)$ 严格证明：无记忆性 $S(s+t) = S(s)S(t)$ 的函数方程的解只有指数函数 $S(t) = e^{-t/\\beta}$）。',
         '（可用生存函数 $S(x)$ 严格证明：无记忆性 $S(s+t) = S(s)S(t)$ 的函数方程的解只有指数函数 $S(t) = e^{-t/\\beta}$；完整证明见 `%s/03-一般随机变量/L08 连续随机变量与PDF.md` §3.1）。' % M)

s = sub1(s,
         '（见概率论MIT 笔记 06 文件夹）。',
         '（见 `%s/06-伯努利和泊松过程/L22 泊松过程.md` §2.2–2.3；几何分布的 fresh start 与连续化见 `%s/06-伯努利和泊松过程/L21 伯努利过程.md`）。' % (M, M))

s = append_before(s, '\n---\n\n## 6. 贝塔分布',
                  '（"第 $k$ 次到达 = Erlang" 的完整推导见 `%s/06-伯努利和泊松过程/L22 泊松过程.md` §2.3。）' % M)

s = sub1(s,
         '（见 p21 第11章）。',
         '（见 p21 第11章；归一化常数与均值 $a/(a+b)$ 的推导见 `%s/08-贝叶斯统计推断/L14 贝叶斯推断导论.md` §2.2）。' % M)

s = append_before(s, '\n---\n\n## 8. χ² 分布',
                  '（为什么要引入它——$\\sigma$ 未知改用样本标准差 $s$ 的动机见 `%s/09-经典统计推断/L20-9.1-经典估计与置信区间.md` §2.5；"两个变量之比"这类导出分布的通用做法见 `%s/04-随机变量进一步专题/L11 导出分布.md` §2.4、例 4。）' % (M, M))

s = append_before(s, '\n---\n\n## 9. 例题',
                  '（拟合优度检验里的分箱卡方用法见 `%s/09-经典统计推断/L20-9.3-9.4-假设检验与显著性检验.md` 例 4、例 5。）' % M)

io.open(p05, 'w', encoding='utf-8', newline='').write(s)
print('p05 woven')
