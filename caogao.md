在空间直角坐标系中，分两种情况：

---

## 情况一：空间曲线的切线

设曲线参数方程为：
$$x=x(t),\quad y=y(t),\quad z=z(t)$$

某点处**切向量**为：
$$\boldsymbol{T} = \bigl(x'(t),\; y'(t),\; z'(t)\bigr)$$

切线与 $x$ 轴正方向夹角 $\alpha$ 满足：

$$\boxed{\cos\alpha = \frac{x'(t)}{\|\boldsymbol{T}\|} = \frac{x'(t)}{\sqrt{[x'(t)]^2 + [y'(t)]^2 + [z'(t)]^2}}}$$

因此：
$$\alpha = \arccos\left(\frac{x'(t)}{\|\boldsymbol{T}\|}\right)$$

---

## 情况二：方向导数的方向向量

若方向 $\boldsymbol{l}$ 用于求方向导数，且已知其**方向余弦**表示：
$$\boldsymbol{l} = (\cos\alpha,\; \cos\beta,\; \cos\gamma)$$

则 $\alpha$ 就是与 $x$ 轴正方向的夹角，直接由方向向量的第一个分量给出：

$$\boxed{\cos\alpha = l_1}$$

即 $\alpha = \arccos(l_1)$，其中 $l_1$ 是单位方向向量在 $x$ 轴上的投影。

---

## 统一公式

无论哪种情况，核心都是：

$$\cos\alpha = \frac{\text{方向向量的 } x \text{ 分量}}{\text{方向向量的模长}}$$

---

**你是做具体的题目吗？** 如果有曲线的方程或方向向量的具体表达式，我可以直接帮你算出 $\alpha$。