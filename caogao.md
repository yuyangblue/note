这是整理好的 **Green、Gauss、Stokes 三大公式对比表**：

| 公式 | 必要条件 | 几何 / 物理意义 |
|:---|:---|:---|
| **Green** (8.1) | $P,Q\in C^{(1)}$，区域 $(\sigma)$ 由分段光滑闭曲线围成 | 平面 2D：$\displaystyle\iint_{(\sigma)}\left(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\right)\mathrm d\sigma=\oint_{(C)}P\,\mathrm dx+Q\,\mathrm dy$ |
| **Gauss** (8.7) | $P,Q,R\in C^{(1)}$，体 $(V)$ 由分片光滑闭曲面围成（取外侧） | 通量守恒：$\displaystyle\iiint_{(V)}\nabla\!\cdot\!\boldsymbol A\,\mathrm dV=\oiint_{(S)}\boldsymbol A\cdot\mathrm d\boldsymbol S$ |
| **Stokes** (8.18) | $P,Q,R\in C^{(1)}$，曲面 $(S)$ 光滑，$(C)$ 是其边界（右手定则） | 环量 = 旋度通量：$\displaystyle\oint_{(C)}\boldsymbol A\cdot\mathrm d\boldsymbol s=\iint_{(S)}(\nabla\times\boldsymbol A)\cdot\mathrm d\boldsymbol S$ |

---

### 三句话串记

- **Green**：平面区域上的"旋度"（面积分） = 边界上的环量（线积分）
- **Gauss**：体域上的"散度"（体积分） = 边界上的通量（面积分）
- **Stokes**：曲面上的"旋度"（面积分） = 边界上的环量（线积分）

> **统一规律**：都是 **"内部某种微分量的积分" = "边界上对应积分"**，是微积分基本定理在高维的推广。

---

需要我把它导出成文件（Markdown / PDF）方便你打印或插入笔记吗？