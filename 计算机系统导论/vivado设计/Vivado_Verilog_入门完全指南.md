# Vivado + Verilog 入门完全指南

> 本文档基于 Nexys A7 开发板，面向 FPGA 初学者，系统梳理 Vivado 与 Verilog 的核心概念、文件关系与实战技巧。

---

## 目录

1. [三种文件的关系](#一三种文件的关系)
2. [RTL 设计图是什么](#二rtl-设计图是什么)
3. [核心概念大白话](#三核心概念大白话)
4. [parameter：仿真时 vs 编程时](#四parameter仿真时-vs-编程时)
5. [完整项目实战：分频器 + 跑马灯](#五完整项目实战分频器--跑马灯)
6. [学习路径与推荐资源](#六学习路径与推荐资源)
7. [初学者常见坑](#七初学者常见坑)

---

## 一、三种文件的关系

用"装修房子"来比喻：

| 文件 | 比喻 | 核心作用 |
|------|------|----------|
| **.v 设计文件** | **建筑图纸** | 描述"电路长什么样、怎么工作"（逻辑功能） |
| **.xdc 约束文件** | **施工说明书** | 告诉工人"门装在哪面墙、水管接哪个口"（物理引脚映射） |
| **Testbench 测试文件** | **虚拟验收测试** | 在真正动工前，用软件模拟"按开关看灯亮不亮"（验证逻辑对不对） |

### 1.1 .v 设计文件（建筑图纸）

```verilog
module led_button(
    input  wire btn,
    output wire led
);
    assign led = btn;  // 逻辑：按键按下，LED就亮
endmodule
```

它只关心逻辑：`led = btn`，完全不关心按键和 LED 在电路板上的哪个位置。

### 1.2 Testbench 测试文件（虚拟验收）

```verilog
module tb_led_button;
    reg  btn;
    wire led;

    led_button uut(
        .btn(btn),
        .led(led)
    );

    initial begin
        btn = 0; #10;
        btn = 1; #10;
        btn = 0; #10;
        $finish;
    end
endmodule
```

**关键理解**：Testbench 是**纯软件模拟**，在电脑里跑，**不需要知道 FPGA 的物理引脚**。它只验证你的逻辑设计是否正确。

### 1.3 .xdc 约束文件（施工说明书）

```xdc
set_property PACKAGE_PIN V17 [get_ports {led}]
set_property IOSTANDARD LVCMOS33 [get_ports {led}]

set_property PACKAGE_PIN W5 [get_ports {btn}]
set_property IOSTANDARD LVCMOS33 [get_ports {btn}]
```

约束文件是**给 Vivado 的"物理施工指南"**。它告诉工具：
- 你代码里的 `led` 端口 → 实际连接到 FPGA 芯片的 **V17 引脚**
- 你代码里的 `btn` 端口 → 实际连接到 FPGA 芯片的 **W5 引脚**

没有约束文件，Vivado 不知道你的按键和 LED 接在哪里，就无法生成可以下载到板子上的比特流文件。

### 1.4 一句话总结

> **.v 文件说"做什么"，Testbench 说"对不对"，.xdc 文件说"接哪里"。**

---

## 二、RTL 设计图是什么

**RTL = Register Transfer Level（寄存器传输级）**

RTL 设计图，就是 **Vivado 把你写的 Verilog 代码"翻译"成电路原理图后的可视化结果**。它展示的是：你的代码综合后，到底变成了什么样的逻辑门、触发器、多路选择器等真实电路元件。

### 2.1 一句话理解

> **Verilog 代码是"文字描述"，RTL 图是"电路照片"。**

### 2.2 示例

你写了这段代码：

```verilog
module example(
    input  wire a, b,
    output wire y
);
    assign y = a & b;
endmodule
```

**RTL 设计图会显示：**

```
        a ───┐
              ├──[ AND2 ]─── y
        b ───┘
```

就是一个 **2 输入与门（AND2）**。你的代码被综合成了一个实实在在的硬件电路。

### 2.3 在 Vivado 中怎么看 RTL 图？

1. **打开综合后的设计**：Flow Navigator → **Open Synthesized Design** → **Schematic**
2. 或者直接点击 **RTL Analysis** → **Open Elaborated Design** → **Schematic**

你会看到一张由各种小方块（逻辑门、触发器、LUT、加法器等）和连线组成的图。

### 2.4 为什么初学者一定要看 RTL 图？

这是培养**硬件思维**的最佳方式：

| 你写的代码 | RTL 图显示 | 你的感悟 |
|-----------|-----------|---------|
| `assign y = a & b;` | 一个 AND 门 | 哦，这是组合逻辑 |
| `always @(posedge clk)` | 一堆 D 触发器 | 哦，这是时序逻辑，会存值 |
| `if (a) y = b; else y = c;` | 一个 2 选 1 多路选择器（MUX） | 原来 if-else 综合成 MUX |
| `case` 语句不完整 | 出现了一个 Latch（锁存器） | 糟糕！我漏了 default，生成了不想要的锁存器 |

> **看 RTL 图，能帮你验证"你写的代码"和"你想象的电路"是否一致。** 如果不一致，说明你的理解有偏差，需要修改代码。

---

## 三、核心概念大白话

### 3.1 rstn 是什么？要它干嘛？

`rstn` 是 **复位信号（Reset）**，字母 `n` 表示 **低电平有效**（negative）。就是 FPGA 的**"重启按钮"**。

**为什么必须需要它？**
FPGA 上电后，所有寄存器里的值是**不确定的**（可能是 0，可能是 1，是随机的）。就像电脑开机后内存里是乱码，必须有一个"重启/初始化"过程，把电路设置到一个**已知的初始状态**。

```verilog
input rstn   // rstn = 0 时复位，rstn = 1 时正常工作
```

**代码里怎么用？**

```verilog
always @(posedge clk or negedge rstn) begin
    if (!rstn)           // 如果 rstn 是低电平（0）
        led_tmp <= 0;    // 全部清零，回到初始状态
    else
        led_tmp <= ...;  // 正常工作
end
```

**生活比喻**：`rstn` 就像你玩游戏的**"重新开始"按钮**。不按的时候游戏正常运行，一按下去（变成 0），所有分数、位置全部归零。

**什么时候用？**

| 场景 | rstn 从哪来 | 你要做什么 |
|------|-----------|-----------|
| **仿真（Testbench）** | 你自己在 Testbench 里生成 | 写代码让 `rstn` 先变 0 保持一段时间，再变 1 |
| **上板（真实FPGA）** | 板子上的**复位按键**或**上电复位电路** | 在 .xdc 约束文件里把 `rstn` 绑定到板子的复位引脚 |

**仿真时写法：**

```verilog
initial begin
    rstn = 0;      // 一开始复位（低电平）
    #100;          // 等 100ns
    rstn = 1;      // 释放复位，电路开始工作
end
```

### 3.2 assign 连续赋值是什么意思？

`assign` 就是**拉一根电线**，左边的输出永远等于右边的输入，输入一变，输出立刻跟着变。

```verilog
assign y = a & b;   // y 这根线，永远等于 a 和 b 的与
```

**生活比喻**：就像你家里的**电灯开关**。开关 `a` 和 `b` 都闭合 → 灯 `y` 立刻亮；任意一个断开 → 灯 `y` 立刻灭。

**没有记忆功能**，不会"记住"之前的状态，purely 是物理连线。

**什么时候用 `assign`？**
描述**组合逻辑**（没有时钟参与，像与门、或门、多路选择器）：

```verilog
assign clk_div29 = clk_cnt[div_num];  // 取一根线，连到计数器的某一位
assign led_o = led_tmp;               // 把内部信号连到输出端口
```

**assign 两边分别是什么？**

```verilog
assign 左边 = 右边;
```

| 位置 | 类型 | 例子 |
|------|------|------|
| **左边** | `wire` 类型 | `clk_div29`, `led_o` |
| **右边** | 任意表达式 | `clk_cnt[div_num]`, `a & b`, `1'b1` |

**wire 赋值后去哪了？**

`wire` 被 `assign` 赋值后，信号就像电流一样沿着导线走，有三个去向：

1. **被模块内部的其他逻辑"使用"**：`clk_div29` 流到了 `always @(posedge clk_div29)` 里当时钟用
2. **直接输出到模块外部**：`led_o` 流到了 FPGA 芯片的物理引脚上，点亮 LED
3. **悬空**：拉好了线但没人用（比如你代码里的 `clk_div2`），Vivado 会**自动优化掉**

### 3.3 always 块是干嘛的？

`always` 块是 Verilog 的**"当...发生时，执行..."**结构。它描述的是**电路的行为**，而不是像 C 语言那样一行行顺序执行。

**两种最常见的 `always` 块：**

| 写法 | 含义 | 综合成什么电路 |
|------|------|--------------|
| `always @(posedge clk)` | 当时钟上升沿时触发 | **触发器/寄存器**（时序逻辑） |
| `always @(*)` | 当任意输入变化时触发 | **组合逻辑**（门电路） |

**生活比喻**：`always` 块就像一个**自动感应门**：
- `@(posedge clk)` → "每当有人靠近（时钟跳变），门就打开一次"
- `@(*)` → "只要有人站在门口（任何输入变化），门就一直保持对应状态"

**always 就是 C++ 的 if 吗？**

**完全不是！**

| | C++ `if` | Verilog `always` |
|--|---------|------------------|
| **执行方式** | 顺序执行，从上到下 | **并行执行**，所有 always 块同时跑 |
| **触发条件** | 程序跑到这行就执行 | 只有敏感列表里的信号变化才执行 |
| **综合结果** | 只是一段 CPU 指令 | 综合成**真实硬件电路**（门、触发器） |
| **次数** | 执行一次就结束 | 只要信号变，就**反复触发** |

**C++ 代码：**

```cpp
if (a == 1) {      // 程序跑到这里，判断一次
    b = c;
}
// 继续往下执行其他代码
```

**Verilog 代码：**

```verilog
always @(posedge clk) begin   // 每当 clk 上升沿，就执行一次
    if (a == 1)
        b <= c;
end
// 这个 always 块永远"活着"，clk 每跳一次就执行一次
```

### 3.4 为什么在 always 里赋值就必须声明 reg？

这是 Verilog 的**语法规定**，不是因为它一定变成寄存器！

```verilog
reg led_tmp;   // 声明为 reg

always @(posedge clk) begin
    led_tmp <= ...;  // 在 always 里赋值，左边必须是 reg 类型
end
```

**关键区分：**

| 赋值方式 | 左边类型 | 说明 |
|---------|---------|------|
| `assign y = ...;` | `wire` | 连续赋值，描述连线 |
| `always ... y <= ...;` | `reg` | 过程赋值，语法要求 |

**⚠️ 重要误区**：`reg` **不**等于"硬件寄存器"！
- 如果 `always @(*)` 里用 `reg`，综合出来可能是**组合逻辑**（门电路）
- 如果 `always @(posedge clk)` 里用 `reg`，综合出来才是**触发器**（真正的寄存器）

> Verilog 规定：`always` 块内赋值的左边，必须声明为 `reg` 类型。这是历史遗留的语法设计，初学者记住"规则"就行。

### 3.5 阻塞赋值 vs 非阻塞赋值

| 符号 | 名称 | 执行方式 | 用在哪 |
|------|------|---------|--------|
| `=` | 阻塞赋值 | 先算右边，立刻更新左边，下一条才能执行 | **组合逻辑** `always @(*)` |
| `<=` | 非阻塞赋值 | 先记住右边值，等所有语句评估完，同时更新左边 | **时序逻辑** `always @(posedge clk)` |

**为什么时序逻辑必须用 `<=`？**

假设有两个寄存器：

```verilog
always @(posedge clk) begin
    a <= b;  // 非阻塞：把此刻的 b 值存到 a
    b <= a;  // 非阻塞：把此刻的 a 值存到 b
end
// 效果：a 和 b 的值互换！（同时交换）
```

如果用阻塞赋值：

```verilog
always @(posedge clk) begin
    a = b;   // 立刻执行：a 变成 b 的值
    b = a;   // 再执行：b 变成 a 的新值（也就是 b 原来的值）
end
// 效果：a = b，b 不变！（不是交换，是复制）
```

**生活比喻**：
- `=`（阻塞）：老师**一个一个**收作业，先收小明的，再收小红的
- `<=`（非阻塞）：老师**同时**给全班发卷子，所有人同时拿到

> **铁律**：时钟触发的 `always` 块里，**必须用 `<=`**，否则仿真和实际硬件可能不一致！

### 3.6 posedge clk or negedge rstn 在干嘛？

这是 `always` 块的**敏感列表（Sensitivity List）**，告诉电路："当以下事件发生时，叫醒我执行代码"。

| 关键字 | 含义 |
|--------|------|
| `posedge clk` | `clk` 的**上升沿**（从 0 变 1） |
| `negedge rstn` | `rstn` 的**下降沿**（从 1 变 0） |
| `or` | 两者任意一个发生，都触发 |

**为什么要把 `rstn` 也写进敏感列表？**

这是**异步复位**的经典写法：
- 正常情况下：等 `clk` 上升沿，电路才工作
- 复位时：**不管 clk 在干嘛**，只要 `rstn` 变低（0），立刻复位

```verilog
always @(posedge clk or negedge rstn) begin
    if (!rstn)          // 如果 rstn 是 0
        ... // 复位
    else
        ... // 等时钟上升沿再工作
end
```

**生活比喻**：
- `posedge clk` → "每天早上 8 点闹钟响，我才起床工作"
- `negedge rstn` → "但如果有火灾警报（rstn=0），**不管几点**，我立刻跳下床逃生"

---

## 四、parameter：仿真时 vs 编程时

### 4.1 核心概念

同一个 `parameter`，不同场景下改值：

| 场景 | `div_num` 设为 | 原因 |
|------|---------------|--------|
| **仿真时** | `3` | 电脑仿真跑得快，3 就能出效果，不用等太久 |
| **编程时（上板）** | `24` | 真实 FPGA 时钟太快（100MHz），需要更大的分频才能肉眼看到 |

### 4.2 分频原理

```verilog
assign clk_div29 = clk_cnt[div_num];   // 取第 div_num 位
```

`clk_cnt` 是一个 32 位计数器，每个时钟周期 `+1`。取 `clk_cnt` 的第 `div_num` 位作为输出，**翻转周期 = 2^(div_num+1)**：

| `div_num` | 取第几位 | 翻转周期 | 分频比 |
|-----------|---------|---------|--------|
| 3 | 第3位 | 2⁴ = 16 个时钟 | **8分频** |
| 24 | 第24位 | 2²⁵ 个时钟 | **约 1677 万分频** |

### 4.3 为什么仿真时要设小？

假设 FPGA 板子时钟是 **100MHz**（周期 10ns）：

**如果 `div_num = 24`：**
```
分频后时钟周期 = 10ns × 2^25 ≈ 0.335 秒
跑马灯移动一次要等 0.335 秒
```
仿真跑 1 秒 = 100,000,000 个时钟周期，电脑要算很久才能看到 LED 移动一次。

**如果 `div_num = 3`：**
```
分频后时钟周期 = 10ns × 2^4 = 160ns
```
仿真很快就能跑完几个周期，验证逻辑是否正确。

### 4.4 怎么在 Vivado 里切换这个值？

**方法1：直接改代码（最常用）**

```verilog
// 仿真时：
parameter div_num = 3;

// 上板前，手动改成：
parameter div_num = 24;
```

**方法2：在 Vivado 里覆盖参数值（不用改代码）**

```tcl
# 仿真时
set_property generic {div_num=3} [get_filesets sim_1]

# 综合时（上板）
set_property generic {div_num=24} [get_filesets sources_1]
```

**方法3：用 `ifdef` 条件编译（进阶）**

```verilog
`ifdef SIMULATION
    parameter div_num = 3;
`else
    parameter div_num = 24;
`endif
```

### 4.5 完整流程对比

```
写代码 / 调试阶段
  parameter div_num = 3;  ← 仿真值
  1. 写 Testbench
  2. 运行行为仿真（Behavioral Simulation）
  3. 看波形，确认跑马灯逻辑正确
     （clk_div29 翻转很快，很快看到效果）
              ↓
      【仿真通过？逻辑正确？】
              ↓
上板验证阶段
  parameter div_num = 24;  ← 上板值
  4. 修改 div_num 为 24
  5. 写 .xdc 约束文件（管脚分配）
  6. 综合 → 实现 → 生成比特流
  7. 下载到 FPGA 板子
     （LED 肉眼可见地流动）
```

---

## 五、完整项目实战：分频器 + 跑马灯

### 5.1 整体架构

```
┌─────────────────────────────────────────┐
│              顶层模块 test               │
├─────────────────────────────────────────┤
│  输入: clk(100MHz)  rstn(复位)  sw_i    │
│  输出: led_o[15:0]                     │
├─────────────────────────────────────────┤
│  ┌─────────┐   ┌─────────────────┐     │
│  │ 2分频器  │   │  div_num分频器   │     │
│  │(T触发器) │   │(32位计数器取位) │     │
│  └────┬────┘   └────────┬────────┘     │
│       │                 │              │
│       └────┬────────────┘              │
│            ▼                            │
│      ┌─────────────┐                   │
│      │  跑马灯状态机 │ ← 用分频后的慢时钟 │
│      │  (16位循环)  │                   │
│      └──────┬──────┘                   │
│             ▼                           │
│        led_o[15:0]                     │
└─────────────────────────────────────────┘
```

### 5.2 逐行编写

#### 第1步：搭模块框架（声明端口）

```verilog
module test(
    input        clk,      // 系统时钟，100MHz
    input        rstn,     // 复位，低电平有效（n表示negative）
    input  [15:0] sw_i,    // 16位拨码开关输入
    output [15:0] led_o    // 16位LED输出
);
```

**编写要点：**
- `rstn` 带 `n` 后缀表示**低电平有效**（0复位，1正常工作），这是行业惯例
- `sw_i` 的 `[15:0]` 表示**16位总线**，高位在前
- 模块名用 `test` 可以，但建议用有意义的名字如 `led_marquee`

#### 第2步：定义参数和内部信号

```verilog
    // 参数：分频系数，仿真时设3，上板时设24
    parameter div_num = 3;

    // 内部信号声明
    reg  [15:0] led_tmp;      // LED状态寄存器（时序逻辑输出）
    reg         ledset_flag;  // 标志位：1=未初始化，0=已开始跑马
    wire        clk_div2;     // 2分频输出（备用）
    wire        clk_div29;    // div_num分频输出（给跑马灯用）
```

**编写要点：**

| 信号 | 类型 | 为什么 |
|------|------|--------|
| `led_tmp` | `reg` | 在 `always` 块里赋值，必须声明为 `reg` |
| `ledset_flag` | `reg` | 同上，时序逻辑输出 |
| `clk_div2` | `wire` | 用 `assign` 连续赋值，声明为 `wire` |
| `clk_div29` | `wire` | 同上 |

> **关键规则**：`always` 块内赋值 → 用 `reg`；`assign` 赋值 → 用 `wire`。

#### 第3步：写2分频器（T触发器）

```verilog
    //========== 2分频器 ==========
    reg clk_div2_tmp;  // 中间寄存器

    always @(posedge clk or negedge rstn) begin
        if (!rstn)
            clk_div2_tmp = 1'b0;   // 复位清零
        else
            clk_div2_tmp = ~clk_div2_tmp;  // 每个时钟翻转一次
    end

    assign clk_div2 = clk_div2_tmp;  // 输出
```

**编写思路：**
- 每个时钟上升沿，把值取反 → 输出周期是输入的2倍 → **2分频**
- `1'b0` 表示 **1位二进制数0**
- 这里用了 `=`（阻塞赋值），因为只有一个赋值语句，用 `=` 或 `<=` 效果一样

**RTL图对应：** 一个 D 触发器，把 **Q非** 接回 **D 端**，这就是经典的 **T 触发器**。

#### 第4步：写 div_num 分频器（核心技巧）

```verilog
    //========== div_num 分频器 ==========
    reg [31:0] clk_cnt;  // 32位计数器

    always @(posedge clk or negedge rstn) begin
        if (!rstn)
            clk_cnt <= 32'b0;   // 复位清零
        else
            clk_cnt <= clk_cnt + 1'b1;  // 每个时钟+1
    end

    assign clk_div29 = clk_cnt[div_num];  // 取第div_num位
```

**这是最关键的一段，详细解释：**

`clk_cnt` 是一个二进制计数器，从 0 开始递增：

```
clk_cnt[0] : 0 1 0 1 0 1 0 1 ...  (每1个时钟翻转，周期=2)
clk_cnt[1] : 0 0 1 1 0 0 1 1 ...  (每2个时钟翻转，周期=4)
clk_cnt[2] : 0 0 0 0 1 1 1 1 ...  (每4个时钟翻转，周期=8)
clk_cnt[3] : 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 ... (每8个时钟翻转，周期=16)
```

**第 n 位的翻转周期 = 2^(n+1)**，所以：
- `div_num = 3` → 取第3位 → 周期 = 16 → **8分频**
- `div_num = 24` → 取第24位 → 周期 = 2^25 → **约 1677 万分频**

> 💡 **这就是"用取位实现分频"的巧妙之处**——不用除法器，只用计数器 + 一根线！

**为什么用 `<=`（非阻塞赋值）？**
- 计数器是典型的**时序逻辑**，必须用 `<=`
- 如果用 `=`，仿真和综合可能不一致

#### 第5步：写跑马灯状态机（最复杂部分）

```verilog
    //========== 跑马灯逻辑 ==========
    always @(posedge clk_div29 or negedge rstn) begin
        if (!rstn) begin
            // 复位状态：全部熄灭，标志位置1
            ledset_flag <= 1'b1;
            led_tmp     <= 16'b0000_0000_0000_0000;
        end
        else if ((ledset_flag == 1'b1) && (sw_i[4:1] == 4'b1010)) begin
            // 初始化：当开关匹配4'b1010时，点亮最高位LED
            ledset_flag <= 1'b0;
            led_tmp     <= 16'b1000_0000_0000_0000;
        end
        else if (sw_i[4:1] == 4'b1010) begin
            // 正常运行：开关保持1010，LED循环右移
            led_tmp <= {led_tmp[14:0], led_tmp[15]};
        end
        else begin
            // 开关不匹配：熄灭，回到等待状态
            led_tmp     <= 16'b0000_0000_0000_0000;
            ledset_flag <= 1'b1;
        end
    end

    // 输出赋值
    assign led_o[15:0] = led_tmp;
```

**编写思路拆解：**

这是一个**三段式状态机的简化版**，有3个状态：

| 状态 | 条件 | 动作 |
|------|------|------|
| **复位/等待** | `rstn=0` 或开关不匹配 | `ledset_flag=1`, LED全灭 |
| **初始化** | `ledset_flag=1` 且 `sw_i[4:1]=1010` | 点亮最高位，标志位清零 |
| **循环移位** | `sw_i[4:1]=1010` 且已开始 | LED右移一位 |

**关键语法解释：**

```verilog
led_tmp <= {led_tmp[14:0], led_tmp[15]};
```

这是 **位拼接运算符 `{}`**，实现**循环右移**：

```
假设 led_tmp = 1000_0000_0000_0000 (只有最高位亮)
led_tmp[14:0] = 000_0000_0000_0000  (低15位)
led_tmp[15]   = 1                    (最高位)

拼接后：{000_0000_0000_0000, 1} = 0100_0000_0000_0000
→ 亮灯从最高位移到了次高位！
```

**为什么用 `sw_i[4:1]` 而不是 `sw_i` 全部16位？**
- 设计者只用开关的 **第1~4位** 作为控制信号（`4'b1010` 是特定密码）
- 其他位可能用于其他功能，或不用

### 5.3 完整代码（整理优化版）

```verilog
`timescale 1ns / 1ps

module test(
    input        clk,
    input        rstn,
    input  [15:0] sw_i,
    output [15:0] led_o
);

    parameter div_num = 3;  // 仿真=3，上板=24

    reg  [15:0] led_tmp;
    reg         ledset_flag;
    wire        clk_div29;

    // 32位计数器分频
    reg [31:0] clk_cnt;

    always @(posedge clk or negedge rstn) begin
        if (!rstn)
            clk_cnt <= 32'b0;
        else
            clk_cnt <= clk_cnt + 1'b1;
    end

    assign clk_div29 = clk_cnt[div_num];

    // 跑马灯状态机（用时钟clk_div29）
    always @(posedge clk_div29 or negedge rstn) begin
        if (!rstn) begin
            ledset_flag <= 1'b1;
            led_tmp     <= 16'b0;
        end
        else if (ledset_flag && (sw_i[4:1] == 4'b1010)) begin
            ledset_flag <= 1'b0;
            led_tmp     <= 16'b1000_0000_0000_0000;
        end
        else if (sw_i[4:1] == 4'b1010) begin
            led_tmp <= {led_tmp[14:0], led_tmp[15]};
        end
        else begin
            ledset_flag <= 1'b1;
            led_tmp     <= 16'b0;
        end
    end

    assign led_o = led_tmp;

endmodule
```

### 5.4 Testbench 框架

```verilog
`timescale 1ns / 1ps

module tb_test;
    reg         clk;
    reg         rstn;
    reg  [15:0] sw_i;
    wire [15:0] led_o;

    // 实例化被测模块
    test uut(
        .clk(clk),
        .rstn(rstn),
        .sw_i(sw_i),
        .led_o(led_o)
    );

    // 时钟生成：100MHz = 10ns周期
    initial clk = 0;
    always #5 clk = ~clk;

    // 测试激励
    initial begin
        // 初始化
        rstn = 0;
        sw_i = 16'b0;
        #100;

        // 释放复位
        rstn = 1;
        #100;

        // 设置开关匹配条件 sw_i[4:1] = 1010
        sw_i = 16'b0000_0000_0001_0100;  // 第2位=1,第4位=1 → [4:1]=1010
        #5000;  // 观察跑马灯效果

        $finish;
    end
endmodule
```

---

## 六、学习路径与推荐资源

### 6.1 学习路线

```
阶段1：数字电路基础（1-2周）
  └─ 基本逻辑门、组合逻辑 vs 时序逻辑、触发器、状态机

阶段2：Verilog 核心语法（2-4周）
  └─ module、wire/reg、assign、always、parameter
  └─ 阻塞/非阻塞赋值、三段式状态机
  └─ 练习平台：HDLbits（硬件版 LeetCode）

阶段3：Vivado 开发流程（2-3周）
  └─ 创建工程 → 添加源文件 → 仿真 → 综合 → 实现 → 生成比特流 → 下载

阶段4：项目实战（持续）
  └─ 流水灯 → 按键消抖 → 数码管 → 计数器 → UART → 简单 CPU
```

### 6.2 推荐资源

| 类型 | 推荐 |
|------|------|
| **官方文档** | Vivado UG901（可综合 Verilog 语法指南） |
| **在线练习** | HDLbits（hdlbits.01xz.net） |
| **书籍** | 《Verilog HDL 数字设计与综合》（夏宇闻） |
| **实验平台** | 清华大学数字逻辑实验课程资料 |

### 6.3 Vivado 完整开发流程

```
设计输入（RTL代码） → 功能仿真 → 综合（Synthesis） → 实现（Implementation）
→ 生成比特流（Bitstream） → 下载到FPGA硬件
```

**推荐入门实验（按顺序）：**
1. 流水灯（LED 闪烁）—— 熟悉工程创建和下载流程
2. 按键消抖 + 数码管译码器 —— 学习组合逻辑和约束文件
3. 计数器 + 分频器 —— 学习时序逻辑
4. 交通灯状态机 —— 学习三段式状态机

---

## 七、初学者常见坑

### 坑1：把 Verilog 当 C 语言写

这是最大的误区。`always` 块里的代码是**并行执行**的，不是顺序执行。

### 坑2：混淆 `wire` 和 `reg`

- `wire` 用于 `assign`
- `reg` 用于 `always` 块（但不一定综合成寄存器）

### 坑3：阻塞赋值与非阻塞赋值混用

- **组合逻辑**用 `=`（`always @(*)`）
- **时序逻辑**用 `<=`（`always @(posedge clk)`）
- 混用会导致仿真与综合不一致

### 坑4：忘记写 `default` 分支

`case` 或 `if-else` 不完整会综合出 **latch（锁存器）**，通常不是你想用的。

### 坑5：不做仿真直接上板

仿真能发现 80% 的问题，养成先仿真的习惯。

### 坑6：悬空信号

`wire` 赋值后如果没有任何逻辑使用它，Vivado 会**自动优化掉**，RTL 图里可能找不到。

---

> **最后的话**：FPGA 开发的核心是**硬件思维**。每写一行代码，都要问自己"这综合出来是什么电路？"养成"写一段代码 → 看 RTL 图 → 确认电路"的习惯，是成为优秀 FPGA 工程师的关键一步。

---

*文档整理时间：2026-07-14*
*适用板卡：Nexys A7（xc7a35t）*
