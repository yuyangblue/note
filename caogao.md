$$\frac{d}{dx}\arcsin x = \frac{1}{\sqrt{1-x^2}}$$

---

## 推导

设 $y = \arcsin x$，则 $x = \sin y$，其中 $y \in \left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$。

两边对 $x$ 求导：
$$1 = \cos y \cdot \frac{dy}{dx}$$

所以：
$$\frac{dy}{dx} = \frac{1}{\cos y}$$

利用 $\sin^2 y + \cos^2 y = 1$，得：
$$\cos y = \sqrt{1 - \sin^2 y} = \sqrt{1 - x^2}$$

（取正根是因为 $y \in \left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$ 时 $\cos y \geq 0$）

因此：
$$\frac{d}{dx}\arcsin x = \frac{1}{\sqrt{1-x^2}}$$

---

## 定义域

- $x \in (-1, 1)$
- 端点 $x = \pm 1$ 处导数趋于无穷（切线垂直）