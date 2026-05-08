# Verilog HDL 学习笔记

> 整理自Verilog HDL课件 | 武汉大学人工智能自强班FPGA课程

---

## 一、初识Verilog HDL

### 什么是硬件描述语言（HDL）？

想象一下，你是个城市规划师🎨，HDL就像是画设计图的语言。只不过这次你要设计的不是城市，而是**数字电路**！

HDL是一种具有特殊结构的编程语言，它能够：
- 描述电路元件之间的**连接关系**
- 描述电路的**功能行为**
- 在不同**抽象层次**上描述电路
- 描述电路的**时序特性**
- 表达**并行性**（这点和普通编程语言很不一样！）

目前最流行的HDL有两门语言：**Verilog**和**VHDL**。Verilog起源于C语言，所以语法上特别像C，容易上手；而VHDL起源于ADA语言，格式更严谨，学起来稍微费劲一些。

---

### Verilog的历史

Verilog是1983年由Phil Moorby创立的（那时候他还在GDA公司），后来这哥们儿还设计了第一个Verilog仿真器。再后来Cadence公司收购了GDA，1995年Verilog正式成为IEEE标准——IEEE 1364。从那以后，Verilog就成了硬件工程师们离不开的工具。

---

### Verilog能做什么？

Verilog的应用场景挺广的：

| 应用领域             | 说明                    |
| ---------------- | --------------------- |
| **ASIC/FPGA工程师** | 写可综合的RTL代码            |
| **系统仿真**         | 高抽象级仿真，进行系统架构开发       |
| **测试工程师**        | 编写各种层次的测试程序           |
| **模型开发**         | ASIC和FPGA单元或更高层次的模块建模 |

简单说，只要你跟数字电路打交道，Verilog基本是必学的技能！

---

### Verilog的五大特点

1. **支持多抽象层次** - 从行为级到门级都能描述
2. **设计测试语法统一** - 写设计和写测试用同一套语法
3. **与工艺无关** - 高层次描述不用关心具体芯片工艺
4. **类C语法** - if-else、for、while这些你熟悉的它都有
5. **丰富的运算符** - 算术、逻辑、位操作全支持

---

### 抽象层次：从高到低

Verilog支持5个抽象层次，理解这个很重要，因为不同层次描述的粒度完全不同：

| 层次 | 说明 | 类比 |
|-----|------|------|
| **系统级** | 用C等高级语言描述 | 画个方块说"这是CPU" |
| **行为级** | 描述模块的功能 | 说"CPU能做加减乘除" |
| **RTL级** | 寄存器与组合电路的逻辑 | 具体到哪些寄存器、哪些逻辑门 |
| **逻辑门级** | 基本逻辑门的组合 | 精确到and、or、not门 |
| **开关级** | 晶体管开关级别 | 精确到nmos、pmos管 |

对于FPGA开发来说，**RTL级**是最常用的抽象层次！我们写的代码最终要能综合成实际的电路。

---

### 三种描述风格

Verilog支持三种描述电路的方式，各有各的用武之地：

#### 1. 结构型描述（Structural）
```verilog
// 就像搭积木，用已知的元件拼出复杂电路
module mux2to1 (
    output out,
    input a, b, sel
);
    wire sel_;
    not u1(sel_, sel);           // 调用非门
    and u2(a1, a, sel_);         // 调用与门
    and u3(b1, b, sel);          // 调用与门
    or  u4(out, a1, b1);         // 调用或门
endmodule
```

#### 2. 数据流型描述（Dataflow）
```verilog
// 用assign连续赋值，描述数据是怎么"流动"的
assign out = (sel == 0) ? a : b;  // 三元运算符实现二选一
```

#### 3. 行为描述（Behavioral）
```verilog
// 用always块，描述"什么时候做什么"
always @(*) begin
    if (sel == 0)
        out = a;
    else
        out = b;
end
```

**小贴士**：实际工作中，这三种风格经常混用，取长补短。

---

### Verilog vs C语言：这些区别要牢记！

| 对比项 | C语言 | Verilog |
|-------|------|---------|
| **执行方式** | 顺序执行 | **并行执行**（所有模块同时工作）|
| **时序概念** | 无延迟概念 | **存在延迟**（可以加#延时）|
| **语法限制** | 相对灵活 | **限制严格**，需要数电知识 |

⚠️ **最核心的区别**：C程序是一条条指令按顺序执行的，而Verilog描述的是硬件电路，所有"语句"是同时运行的！这也是新手最容易踩坑的地方。

---

## 二、Verilog语法基础

### 模块（Module）：Verilog程序的基本单位

Verilog代码是用**模块**组织的，一个模块可以代表：
- 一颗IC芯片
- 一个逻辑块（如ALU）
- 甚至整个系统

```verilog
module 模块名称(端口列表);
    // 输入输出端口声明
    input  clk;      // 输入端口
    output [7:0] data;  // 输出端口，8位宽
    inout  sda;      // 双向端口
    
    // 内部信号声明
    reg [7:0] counter;   // 寄存器
    wire enable;         // 线网
    
    // 功能描述...
    
endmodule
```

**模块的结构**：
```
module 模块名(端口1, 端口2, ...);
    [端口声明]
    [信号声明]
    [功能代码]
endmodule
```

---

### 基本语法规则

#### 注释：两种写法
```verilog
// 单行注释：到行末结束（和C++一样）

/* 多行注释
   中间的都是注释
   随便写多少行都行 */
```

#### 格式自由
Verilog对格式很随意，可以用空格、Tab、换行来让代码更美观——编译器会忽略多余的空白符。

---

### 数值表示：这些规则要知道

Verilog的常量有好几种表示方式：

```verilog
12           // 未定义位宽的十进制数（默认32位）
'H83a        // 未定义位宽的十六进制
8'b1100_0001 // 8位二进制（下划线忽略，便于阅读）
64'hff01     // 64位十六进制
9'O17        // 9位八进制
3'b1010_1101 // 高位被截断，只保留3位：3'b101
6.3          // 十进制浮点数
32e-4        // 科学计数法 = 0.0032
```

**注意事项**：
- 下划线`_`可以随意插入，增强可读性
- 没定义位宽默认32位
- 没定义进制默认十进制
- 当数值超出位宽时，**高位会被截断**

---

### 字符串：注意这些限制

```verilog
"This is a string"                   // 正常字符串
"This has \t tab and \n newline"     // 可以用转义符
"val = %b"                           // 格式符，类似printf
```

⚠️ **重要**：Verilog没有专门的字符串数据类型！字符串主要用于`$display`等系统任务的输出。

---

### 标识符（变量名）的命名规则

```verilog
// 合法的标识符
shift_reg_a     // 以字母开头，可以含下划线
_bus3            // 可以以下划线开头（但不推荐）
data123          // 可以含数字

// 非法的标识符
34net            // ❌ 不能以数字开头
a*b_net          // ❌ 不能含*
n@238            // ❌ 不能含@
```

**关键点**：
- 必须以**字母(a-z, A-Z)**或**下划线(_)**开头
- 后面可以是字母、数字、下划线、$
- **区分大小写**：`sel`和`SEL`是两个不同的东西！
- 关键字全小写：`module`、`input`、`reg`等

---

## 三、数据类型与逻辑系统

### 四值逻辑：Verilog的"世界观"

Verilog采用的是**四值逻辑系统**，这比只有0和1的纯二进制更有表现力：

| 值 | 含义 | 场景 |
|----|------|------|
| **0** | 逻辑低/假 | 低电平、接地 |
| **1** | 逻辑高/真 | 高电平、电源 |
| **x** | 未知态 | 冲突、初始化、仿真不确定 |
| **z** | 高阻态 | 三态门断开、上拉/下拉 |

**类比理解**：就像你问一个人"今天开心吗？"
- 0 = 不开心
- 1 = 开心  
- x = 不知道（可能开心也可能不开心）
- z = 不想回答（处于"高阻"状态）

---

### 线网类型（Net）：信号的"导线"

**Wire**是最常用的线网类型，代表信号连接——就像电路板上的导线。

```verilog
wire clk;              // 单比特线网
wire [7:0] data_bus;  // 8位宽的总线
tri [15:0] busa;      // 三态总线
```

**常见线网类型对比**：

| 类型            | 功能    | 何时用        |
| ------------- | ----- | ---------- |
| **wire**      | 标准连接线 | 最常用，用于组合逻辑 |
| **tri**       | 三态总线  | 需要高阻态时     |
| **wor**       | 线或    | 多驱动器"或"在一起 |
| **wand**      | 线与    | 多驱动器"与"在一起 |
| **supply0/1** | 电源/地  | 表示常量0或1    |

**记忆技巧**：wire就像普通导线，tri是"带开关"的导线（高阻态时断开）。

---

### 寄存器类型（Register）：会"记住"的变量

**Reg**是最常用的寄存器类型，能够保存赋值直到下一次赋值：

```verilog
reg a;                 // 1位寄存器
reg [3:0] counter;    // 4位寄存器
reg [7:0] mem [0:255]; // 存储器：256个8位字
```

**四种寄存器类型对比**：

| 类型          | 说明           | 典型用途      |
| ----------- | ------------ | --------- |
| **reg**     | 有符号整数，可标量或矢量 | 最常用，保存数据  |
| **integer** | 32位有符号整数     | 算法计算、循环计数 |
| **real**    | 双精度浮点        | 科学计算      |
| **time**    | 64位无符号整数     | 保存仿真时间    |

**关于负数**：reg是无符号的，integer是有符号的
```verilog
reg [3:0] a;
integer b;
a = -1;  // 结果是4'b1111（二进制补码）
b = -1;  // 结果是-1（带符号）
```

---

### 参数（Parameter）：模块的"配置项"

参数就像C语言的const或宏定义，用于定义模块的常量：

```verilog
module uart #(
    parameter CLK_FREQ = 50_000_000,  // 50MHz时钟
    parameter BAUD_RATE = 9600        // 波特率
)(
    input clk,
    output tx
);
    // 在模块内部，参数就像常量一样使用
    localparam BIT_TIME = CLK_FREQ / BAUD_RATE;
    
    // ...
endmodule
```

**参数可以重载**：实例化模块时可以传入新值
```verilog
uart #(.BAUD_RATE(115200)) uart_inst (...);  // 覆盖默认的9600
```

---

### 变量类型选择：实战经验

这是新手最容易出错的地方！记住这个规则：

| 场景 | 正确类型 | 说明 |
|-----|---------|------|
| assign赋值 | **wire** | 过程块外的连续赋值 |
| always块赋值 | **reg** | 过程块内的赋值目标 |
| 模块输入端口 | **wire** | 输入只能是net类型 |
| 模块输出端口 | wire或reg | 取决于如何赋值 |

⚠️ **常见错误**：
```verilog
// 错误示例
wire clk;
always @(posedge clk)
    clk = ~clk;  // ❌ 不能再always块中给wire赋值
```

---

## 四、运算符：硬件世界的"魔法棒"

### 运算符一览表（按优先级）

| 优先级 | 运算符类型 | 符号 |
|-------|-----------|------|
| 最高 | 连接与复制 | `{ }`, `{{ }}` |
| ↓ | 算术运算 | `*`, `/`, `%`, `+`, `-` |
| ↓ | 逻辑移位 | `<<`, `>>` |
| ↓ | 关系运算 | `>`, `<`, `>=`, `<=` |
| ↓ | 相等运算 | `==`, `!=`, `===`, `!==` |
| ↓ | 按位运算 | `~`, `&`, `|`, `^`, `~^` |
| ↓ | 逻辑运算 | `!`, `&&`, `||` |
| 最低 | 条件运算 | `? :` |

**建议**：复杂的表达式多用括号，别依赖优先级！

---

### 算术运算符：加减乘除

```verilog
a = 5 + 3;   // 加法：8
b = 5 - 3;   // 减法：2
c = 5 * 3;   // 乘法：15
d = 5 / 3;   // 除法：1（整数除法）
e = 5 % 3;   // 取模：2
```

**重要特性**：
- 整数除法**会舍去小数部分**
- 取模运算的符号与**第一个操作数**相同
- 如果操作数含`x`或`z`，结果为`x`

---

### 按位运算符 vs 逻辑运算符：别搞混！

这是两个特别容易混淆的运算符家族：

```verilog
// 按位运算：每一位单独操作，结果位宽不变
a = 4'b1001 & 4'b1010;  // 4'b1000（对应位相与）
a = 4'b1001 | 4'b1010;  // 4'b1011（对应位相或）
a = ~4'b1001;           // 4'b0110（逐位取反）

// 逻辑运算：整体判断，结果只有1位
a = (4'b1001 != 0);     // 1'b1（全0才为0）
a = (4'b1001 == 4'b0000);  // 1'b0
a = !4'b0000;           // 1'b1（非零变零，零变一）
```

**记忆口诀**：
- **按位**（`~ & |`）→ 逐位操作，位数不变
- **逻辑**（`! && ||`）→ 整体判断，结果1位

---

### 移位运算符：左移右移

```verilog
a = 8'b00001100 << 2;   // 8'b00110000（左移2位，低位补0）
a = 8'b00001100 >> 2;   // 8'b00000011（右移2位，高位补0）
```

⚠️ **注意**：右移时高位补0（逻辑移位），这意味着负数的右移结果会改变！

---

### 相等运算符：`==` vs `===`

这两个家伙看起来差不多，但行为完全不同：

```verilog
// 逻辑相等：x和z参与比较时结果可能是x
2'b1x == 2'b1x   // 结果是 x（可能相等也可能不等）
2'b1x == 2'b0x   // 结果是 x

//  case相等：严格比较，x只能等于x，z只能等于z
2'b1x === 2'b1x  // 结果是 1（完全相同）
2'b1x === 2'b0x  // 结果是 0（不相同）
```

**实战建议**：
- RTL代码中用`==`和`!=`
- testbench中可以用`===`做精确匹配
- `===`和`!==`**不可综合**，只能用于仿真

---

### 条件运算符：`? :` 三元表达式

```verilog
// 基本用法
out = (sel == 0) ? a : b;

// 嵌套用法：实现四选一
out = (sel == 2'b00) ? a :
      (sel == 2'b01) ? b :
      (sel == 2'b10) ? c : d;
```

⚠️ **注意**：如果条件值为x或z，且true和false分支值不同，结果不确定！

---

### 连接与复制：`{ }` 和 `{{ }}`

```verilog
// 连接：把多个信号拼成一个向量
{a, b, c} = 8'b10110011;  // a=1, b=0, c=110011（按顺序对应）

// 复制：把一个信号重复多次
a = {4{2'b10}};           // 8'b10101010（重复4次）

// 组合使用
result = {a, 2'b00, b[7:4]};  // 灵活拼接
```

---

## 五、结构描述：用元件"搭积木"

### 基本门级原语：Verilog的"乐高积木"

Verilog预定义了一些基本门电路，可以直接调用：

| 原语 | 功能 | 符号 |
|-----|------|------|
| **and** | 与门 | 多输入，单输出 |
| **or** | 或门 | 多输入，单输出 |
| **not** | 非门 | 单输入，单输出 |
| **xor** | 异或门 | 多输入，单输出 |
| **nand** | 与非门 | 多输入，单输出 |
| **nor** | 或非门 | 多输入，单输出 |
| **buf** | 缓冲器 | 单输入，多输出 |

```verilog
// 基本调用格式
and (out, in1, in2, in3);  // 三输入与门
not (out, in);              // 非门
xor (out, in1, in2);       // 异或门
```

---

### 条件门：三态门的表达

```verilog
// bufif1：使能高时通过，否则高阻
bufif1 (data_out, data_in, enable);

// bufif0：使能低时通过，否则高阻
bufif0 (data_out, data_in, enable);

// notif1/notif0：带反相的条件缓冲器
notif1 (data_out, data_in, enable);
```

---

### 模块实例化：复用你的设计

**实例化**就是把你写的模块"复制"到别的地方用：

```verilog
// 定义一个D触发器模块
module dff (
    input d, clk,
    output q, qb
);
    always @(posedge clk) begin
        q <= d;
        qb <= ~d;
    end
endmodule

// 在另一个模块中实例化它
module reg4 (
    input [3:0] d,
    input clk, clr,
    output [3:0] q
);
    // 位置映射：按顺序连接
    dff d0 (d[0], clk, clr, q[0], );
    dff d1 (d[1], clk, clr, q[1], );
    dff d2 (d[2], clk, clr, q[2], );
    dff d3 (d[3], clk, clr, q[3], );
    
    // 名称映射：更清晰，不易出错
    dff d0 (.d(d[0]), .clk(clk), .clr(clr), .q(q[0]), .qb());
endmodule
```

**两种映射方式对比**：

| 方式 | 语法 | 优点 | 缺点 |
|-----|------|------|------|
| 位置映射 | `mod inst(a, b, c)` | 简洁 | 顺序容易错 |
| 名称映射 | `mod inst(.out(a), .in(b))` | 清晰，不易错 | 写起来长 |

---

### 参数化模块实例化

```verilog
// 实例化时修改参数
uart #(
    .CLK_FREQ(100_000_000),  // 100MHz
    .BAUD_RATE(115200)       // 高波特率
) uart_high_speed (...);
```

---

## 六、数据流描述：assign的魔法

### 连续赋值：组合逻辑的利器

`assign`是数据流描述的核心，用于描述**组合逻辑**：

```verilog
// 基本语法
assign out = a & b;           // 与运算
assign out = (sel == 0) ? a : b;  // 条件选择

// 显式 vs 隐式
wire out1 = a & b;            // 隐式赋值（简洁）
assign out2 = a & b;          // 显式赋值（清晰）
```

**特点**：
- 持续监控右侧表达式
- 右侧任意信号变化，左侧立即更新
- 只能用于**wire类型**

---

### 组合逻辑的数据流实现

```verilog
// 实现一个2:1选择器
module mux2to1 (
    input a, b, sel,
    output out
);
    assign out = (sel == 0) ? a : b;
endmodule

// 实现一个全加器
module full_adder (
    input a, b, cin,
    output sum, cout
);
    assign sum = a ^ b ^ cin;
    assign cout = (a & b) | (cin & (a ^ b));
endmodule
```

---

## 七、行为描述：always块的艺术

### 过程块：initial和always

```verilog
// initial：仿真开始时执行一次，常用于testbench
initial begin
    clk = 0;
    rst = 1;
    #100 rst = 0;
end

// always：循环执行，硬件的灵魂
always #5 clk = ~clk;  // 生成时钟信号
```

**两者的本质区别**：
- `initial`像"一次性事件"
- `always`像"永不停止的进程"

---

### 敏感信号列表：@()

**组合逻辑**：电平敏感
```verilog
always @(*) begin   // @(*) 自动包含所有输入
    out = a & b;
end

// 等价于
always @(a or b) begin
    out = a & b;
end
```

**时序逻辑**：边沿敏感
```verilog
always @(posedge clk) begin        // 上升沿触发
    q <= d;
end

always @(negedge clk) begin       // 下降沿触发
    q <= d;
end

always @(posedge clk or negedge rst) begin  // 异步复位
    if (!rst)
        q <= 0;
    else
        q <= d;
end
```

---

### 阻塞赋值 vs 非阻塞赋值：这是重点！

这是Verilog中最容易出错的概念，也是区分新手和老手的分水岭！

#### 阻塞赋值 `=`
```verilog
// "顺序执行"的感觉
always @(posedge clk) begin
    a = b;    // 先执行
    c = a;    // 然后用新的a
end
// 结果：c = b（新值）
```

#### 非阻塞赋值 `<=`
```verilog
// "同时赋值"的感觉
always @(posedge clk) begin
    a <= b;   // 同时采样
    c <= a;   // 用的是旧值
end
// 结果：c = 旧的a
```

**实战规则**：

| 场景 | 用哪种赋值 | 原因 |
|-----|----------|------|
| **时序逻辑（寄存器）** | **非阻塞`<=`** | 避免竞争冒险 |
| **组合逻辑** | **阻塞`=`** | 组合逻辑本应立即计算 |
| **同一always块内** | **统一用一种** | 混用容易出错 |

**经典错误示例**：
```verilog
// 错误：用阻塞赋值实现寄存器
always @(posedge clk) begin
    q = d;    // ❌ 应该用 <=
    qb = ~d;  // 此时q已是新值！
end

// 正确：用非阻塞赋值
always @(posedge clk) begin
    q <= d;    // ✓
    qb <= ~d;  // ✓ 用的是d的旧值
end
```

**记忆口诀**："时序用<=，组合用=，永远不要在时序逻辑里用="

---

### 条件语句：if和case

#### if-else语句
```verilog
always @(*) begin
    if (en == 1) begin
        out = data;
    end else begin
        out = 0;
    end
end

// 嵌套if：注意优先级
if (cond1)
    if (cond2)
        result = a;
    else
        result = b;
else
    result = c;
```

⚠️ **建议**：多层嵌套时用`begin...end`明确代码块，避免else匹配错误！

#### case语句
```verilog
case (opcode)
    3'b000: result = a + b;
    3'b001: result = a - b;
    3'b010,
    3'b100: result = a / b;  // 多个值共用一组操作
    default: result = 0;       // 别忘了default！
endcase
```

**三种case变体**：

| 类型 | 忽略的值 | 用途 |
|-----|---------|------|
| `case` | 无 | 精确匹配 |
| `casez` | `?`和`z` | don't care匹配 |
| `casex` | `?`、`z`、`x` | 更宽松的匹配 |

```verilog
// casez示例：实现优先编码器
casez (irq)
    4'b???1: priority = 0;   // 最高位优先
    4'b??1?: priority = 1;
    4'b?1??: priority = 2;
    4'b1???: priority = 3;
    default: priority = 0;
endcase
```

---

### 循环语句

#### repeat：重复固定次数
```verilog
// 延时n个时钟周期
repeat(10) @(posedge clk);
```

#### while：条件为真时循环
```verilog
// 统计二进制中1的个数
count = 0;
while (data != 0) begin
    if (data[0] == 1)
        count = count + 1;
    data = data >> 1;
end
```

#### for：最常用的循环
```verilog
// 8位到32位扩展
for (i = 0; i < 8; i = i + 1)
    extended[32-8+i] = data[i];  // 符号扩展
```

#### forever：永不停止
⚠️ 主要用于testbench生成时钟，**不可综合**
```verilog
// 生成50MHz时钟
always begin
    #10 clk = ~clk;  // 永不停止！
end
```

---

### 时序控制：#和@

```verilog
// #延时：等多少时间单位
#10 data = 8'hFF;    // 等10个时间单位

// @(边沿)：等信号变化
@(posedge clk) data = 8'h00;  // 等时钟上升沿
@(negedge clk) data = 8'h00; // 等时钟下降沿

// wait：电平敏感
wait (enable) #5 data = 8'h00;  // enable为真时执行
```

---

## 八、任务与函数

### 任务（Task）：带时序的"子程序"

Task可以包含时序控制，可以有多个输入输出：

```verilog
task delayed_write;
    input [7:0] data;
    input [3:0] delay_cycles;
    begin
        repeat(delay_cycles) @(posedge clk);
        write_data(data);
    end
endtask

// 调用
initial begin
    delayed_write(8'hA5, 4);
end
```

**Task特点**：
- ✅ 可以有时序控制（`#`、`@`、`wait`）
- ✅ 可以有input、output、inout
- ✅ 可以调用其他task或function
- ❌ 不能综合（主要用于testbench）

---

### 函数（Function）：纯组合逻辑

Function用于纯组合逻辑计算，不能包含时序：

```verilog
// 计算奇偶校验位
function parity;
    input [7:0] data;
    integer i;
    begin
        parity = 0;
        for (i = 0; i < 8; i = i + 1)
            parity = parity ^ data[i];
    end
endfunction

// 调用
wire p = parity(8'hA5);
```

**Function特点**：
- ✅ 只能有input
- ✅ 隐含返回return值（函数名就是返回值）
- ✅ 调用快，仿真时间0
- ❌ 不能有时序控制
- ❌ 不能调用task

**task vs function对比**：

| 特性 | task | function |
|-----|------|---------|
| 时序控制 | ✅ 可以 | ❌ 不行 |
| 输入参数 | input/output/inout | 只能input |
| 调用其他function | ✅ | ✅ |
| 调用其他task | ✅ | ❌ |
| 返回值 | 多个output | 函数名隐含返回 |
| 可综合 | ❌ | ✅（组合部分） |

---

## 九、系统任务与函数

### 显示输出：$display和$write

```verilog
initial begin
    $display("Hello, FPGA!");                    // 输出并换行
    $write("No newline here"); $write("!\n");    // 不换行
    
    // 格式化输出
    $display("a=%b, hex=%h, dec=%d", a, a, a);
end
```

**常用格式符**：

| 格式符 | 含义 |
|-------|------|
| `%b` | 二进制 |
| `%h` | 十六进制 |
| `%d` | 十进制 |
| `%o` | 八进制 |
| `%s` | 字符串 |
| `%t` | 时间 |
| `%m` | 模块名 |

---

### 监控：$monitor

```verilog
initial begin
    $monitor("%t: clk=%b rst=%b cnt=%d", 
             $time, clk, rst, cnt);
end
```

⚠️ `$monitor`会在**信号变化时**自动输出，很适合观察波形。

---

### 文件操作

```verilog
integer f;

// 打开文件
f = $fopen("result.txt", "w");  // "r"读/"w"写/"a"追加

// 写入
$fdisplay(f, "Simulation time: %t", $time);
$fwrite(f, "Data: %h\n", data);

// 关闭
$fclose(f);

// 读取存储器
reg [7:0] mem [0:255];
initial $readmemh("mem_init.txt", mem);
```

---

### 仿真控制

```verilog
#100 $display("Time: %t", $time);  // 显示仿真时间
$finish;    // 终止仿真
$stop;      // 暂停仿真（可继续）
```

---

## 十、代码风格与实践建议

### 命名规范

```verilog
// 推荐：清晰有意义
input clk;                    // 时钟
input rst_n;                  // 低有效复位
output [7:0] data_out;        // 输出数据
reg [15:0] counter;           // 计数器

// 不推荐：糊名
input a, b, c, d, e, f, g, h;
output o1, o2, o3;
reg x, y, z;
```

---

### 同步复位 vs 异步复位

```verilog
// 异步复位：复位信号独立于时钟
always @(posedge clk or negedge rst_n) begin
    if (!rst_n)
        q <= 0;
    else
        q <= d;
end

// 同步复位：复位信号受时钟控制
always @(posedge clk) begin
    if (!rst_n)
        q <= 0;
    else
        q <= d;
end
```

**选择建议**：
- 异步复位：响应快，但易受毛刺影响
- 同步复位：更稳定，资源稍多

---

### 常见错误避免

1. **不要在过程块中给wire赋值**
2. **时序逻辑用非阻塞`<=`**
3. **组合逻辑敏感列表要完整**
4. **不要忘记default分支**
5. **不要在多个always块驱动同一信号**

---

### 可综合风格检查

| 可综合 | 不可综合 |
|-------|---------|
| always @(posedge clk) | initial块 |
| assign | for/while循环（仅限testbench）|
| wire/reg | force/release |
| case/if-else | wait语句 |
| 运算符（大部分）| 命名事件 |

---

## 附录：常用代码模板

### 基础D触发器
```verilog
module dff (
    input d, clk, rst_n,
    output reg q
);
    always @(posedge clk or negedge rst_n)
        if (!rst_n)
            q <= 0;
        else
            q <= d;
endmodule
```

### 计数器
```verilog
module counter #(
    parameter MAX = 255
)(
    input clk, rst_n,
    output reg [7:0] cnt
);
    always @(posedge clk or negedge rst_n)
        if (!rst_n)
            cnt <= 0;
        else if (cnt == MAX)
            cnt <= 0;
        else
            cnt <= cnt + 1;
endmodule
```

### 状态机模板
```verilog
localparam IDLE = 2'b00;
localparam READ = 2'b01;
localparam WRITE = 2'b10;

always @(posedge clk or negedge rst_n)
    if (!rst_n)
        state <= IDLE;
    else
        case (state)
            IDLE:   if (start) state <= READ;
            READ:   if (done)  state <= WRITE;
            WRITE:  state <= IDLE;
            default: state <= IDLE;
        endcase
```

---

> 整理自Verilog HDL课件 | 武汉大学人工智能自强班FPGA课程
> 
> 祝学习愉快！有问题多仿真，波形是最好的老师 🚀
