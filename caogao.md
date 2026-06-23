这是**保守场/有势场的等价条件**表，我来补全完整版本：

---

## 单连通区域上的等价命题

| 命题              | 向量表述                                                                                                   |
| :-------------- | :----------------------------------------------------------------------------------------------------- |
| **(1) 闭路环量为零**  | $\displaystyle\oint_{(C)}\boldsymbol A\cdot\mathrm d\boldsymbol s=0$，对任意分段光滑闭曲线 $(C)$                  |
| **(2) 积分与路径无关** | $\displaystyle\int_{(C)}\boldsymbol A\cdot\mathrm d\boldsymbol s$ 只与起点、终点有关，即 $\boldsymbol A$ 为**保守场** |
| **(3) 存在势函数**   | 存在可微函数 $u$，使 $\nabla u=\boldsymbol A$，即 $\boldsymbol A$ 为**有势场**，$u$ 称为**势函数**（或原函数）                   |
| **(4) 旋度为零**    | $\nabla\times\boldsymbol A=\boldsymbol 0$，即 $\boldsymbol A$ 为**无旋场**                                   |

---

## 等价关系

$$\text{(1)} \Leftrightarrow \text{(2)} \Leftrightarrow \text{(3)} \Leftrightarrow \text{(4)}$$

> **前提**：区域必须是**单连通**的（没有"洞"）。如果区域有洞，(4) 推不出前三条。

---

## 势函数的求法

若 $\boldsymbol A=(P,Q,R)$ 是有势场，则势函数 $u$ 满足：

$$\frac{\partial u}{\partial x}=P,\quad \frac{\partial u}{\partial y}=Q,\quad \frac{\partial u}{\partial z}=R$$

通过**逐次积分**或**折线积分**求出：

$$u(x,y,z)=\int_{(x_0,y_0,z_0)}^{(x,y,z)}P\,\mathrm dx+Q\,\mathrm dy+R\,\mathrm dz$$

---

## 一句话总结

> **保守场 = 有势场 = 无旋场 = 闭路环量为零 = 积分与路径无关**

这是场论中最重要的等价关系之一，与复变函数中的**解析函数**、物理学中的**保守力**（重力、静电力）直接对应。

---

需要我把这个表和之前的 Green/Gauss/Stokes 表合并，导出成一份完整的场论公式速查？