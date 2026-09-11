# FPGA与VIVADO设计流程笔记

> 整理自VIVADO设计流程课件+FPGA实验文档 | 武汉大学人工智能自强班FPGA课程

---

## 一、FPGA基础概念

### 什么是FPGA？

FPGA，全称**Field Programmable Gate Array**（现场可编程门阵列）。你可以把它想象成一片"数字电路乐高"——上面有成千上万个可以自由连接的逻辑块，你可以通过编程来定义它们之间的连接关系，从而实现各种数字电路功能。

**类比理解**：
- **ASIC**（专用芯片）：像定制家具，批量生产后功能固定
- **FPGA**：像乐高积木，可以反复搭建、修改、重新搭建

FPGA的核心优势在于：
- **灵活性高**：可以反复编程修改
- **开发周期短**：不需要流片
- **适合小批量**：成本可控
- **可以并行开发**：软硬件可以同时进行

---

### Xilinx Artix-7系列：我们的主角

课件和实验中用到的是**Artix-7 XC7A100T**芯片，封装是**CSG324**：

| 参数       | 值        | 说明                 |
| -------- | -------- | ------------------ |
| 芯片型号     | XC7A100T | Artix-7系列，100K逻辑单元 |
| 封装       | CSG324   | 324个引脚             |
| 速度等级     | -1       | 数字越大速度越快           |
| I/O Bank | 6个       | 每组Bank有不同的电压标准     |

**为什么选择Artix-7？**
- 性价比高，适合教学
- 资源够用（100K LUT + 126K FF）
- 功耗低
- 配套开发板多（如Nexys A7）

---

### VIVADO是什么？

Vivado是**Xilinx公司的新一代FPGA设计工具**，用来：
- 创建和管理工程
- 编写和编辑Verilog/VHDL代码
- 仿真验证功能
- 综合（把代码变成电路网表）
- 实现（布局布线）
- 生成比特流文件
- 烧写到FPGA开发板

**vivado版本**：课件用2016.2和2018.3实验用2018.3，界面略有差异但流程相同。

---

## 二、VIVADO设计流程总览

VIVADO的设计流程大致分为以下几个步骤：

```
┌─────────────────────────────────────────────────────────────────┐
│                        VIVADO设计流程                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ① 新建工程 ──→ ② 设计输入 ──→ ③ 功能仿真 ──→ ④ 设计综合             │
│        │                                        │               │
│        │                                        ↓               │
│  ⑦ 下载到板子 ←── ⑥ 位流生成 ←── ⑤ 工程实现                         │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

| 步骤       | 说明             | 产出        |
| -------- | -------------- | --------- |
| **新建工程** | 创建项目，配置芯片型号    | .xpr工程文件  |
| **设计输入** | 编写Verilog代码    | .v设计文件    |
| **功能仿真** | 用testbench验证功能 | 仿真波形      |
| **设计综合** | 代码→逻辑网表        | 综合后的原理图   |
| **工程实现** | 布局布线           | 门级网表      |
| **位流生成** | 生成配置文件         | .bit比特流文件 |
| **下载**   | 烧写到FPGA        | 运行在板子上    |

---

## 三、新建工程：一步一步来

### 步骤详解

**Step 1：打开Vivado**

双击桌面Vivado图标或在开始菜单找到：
```
Xilinx Design Tools → Vivado 2018.3 → Vivado 2018.3
```

看到欢迎界面后，点击 **"Create New Project"**。

---

**Step 2：工程名称和路径**

```
Project name: project_guessdigital
Project location: D:/cpu/NEXYSA7
☑ Create project subdirectory
```

⚠️ **注意事项**：
- 工程名称和路径**不能有中文和空格**！
- 建议用字母、数字、下划线组合
- 勾选创建子目录，便于管理

---

**Step 3：选择项目类型**

选择 **"RTL Project"**，并勾选 **"Do not specify sources at this time"**（暂时不添加源文件）。

| 项目类型 | 适用场景 |
|--------|----------|
| **RTL Project** | 大部分设计场景 |
| Post-synthesis Project | 已有综合网表 |
| I/O Planning Project | 只做引脚规划 |
| Imported Project | 从其他工具导入 |

---

**Step 4：选择FPGA芯片**

这是关键步骤！根据实验文档，需要选择：

```
Family: Artix-7
Subfamily: Artix-7
Package: CSG324
Speed: -1
Temp Grade: C
```

然后在器件列表中找到：**xc7a100tcsg324-1**

**或者直接搜索**，输入 `xc7a100tcsg324` 快速定位。

---

**Step 5：确认并完成**

检查Summary信息，确认无误后点击 **Finish**。

---

## 四、设计文件输入：写代码啦

### 创建Verilog文件

在Flow Navigator中：
1. 点击 **Project Manager → Add Sources**
2. 选择 **"Add or Create Design Sources"**
3. 点击 **"Create File"**
4. 输入文件名（如 `led.v`、`test.v`）
5. 选择文件类型：**Verilog**
6. 点击OK，然后Finish

---

### 编写模块代码

Vivado会自动生成模板：

```verilog
// 模板
module led(
    input [2:0] sw,
    output led
);
    // 在这里写你的代码
endmodule
```

**实验代码示例**：猜数字游戏中检测特定开关组合

```verilog
module test(
    input clk,
    input rstn,
    input [15:0] sw_i,
    output [15:0] led_o
);
    reg ledstate;
    
    always@(*)
    begin
        if (sw_i[4:1] == 4'b1010) 
            ledstate = 1'b1;  // 开关5-8为1010时LED亮
        else 
            ledstate = 1'b0;
    end
    
    assign led_o[15] = ledstate;
endmodule
```

---

## 五、约束文件：告诉Vivado你的"接线图"

约束文件（XDC文件）告诉Vivado：
- **哪些引脚**连接哪些信号
- **时钟频率**是多少
- **电气标准**是什么

### 方法一：图形界面配置

**Step 1：先综合**

点击 **Run Synthesis**，等待综合完成。

**Step 2：打开综合设计**

点击 **Open Synthesized Design**。

**Step 3：配置引脚**

在layout中选择 **I/O Planning**，切换到 **I/O Ports** 标签。

设置每个端口的：
- **Package Pin**：引脚编号（如J15、L16）
- **I/O Std**：电气标准（如LVCMOS33）

---

### 方法二：手动编写XDC文件

**Step 1：创建约束文件**

Add Sources → Add or Create Constraints → Create File → 输入文件名（如`icf.xdc`）

**Step 2：编写约束内容**

```xdc
# ============================================================
# 猜数字游戏约束文件
# ============================================================

## 时钟约束
set_property PACKAGE_PIN L18 [get_ports clk]
set_property IOSTANDARD LVCMOS33 [get_ports clk]
create_clock -period 10.000 -name sys_clk_pin -waveform {0 5.000} -add [get_ports clk]

## 复位信号
set_property PACKAGE_PIN T18 [get_ports rstn]
set_property IOSTANDARD LVCMOS33 [get_ports rstn]

## 开关输入（16个）
set_property PACKAGE_PIN J15 [get_ports {sw_i[0]}]
set_property PACKAGE_PIN L16 [get_ports {sw_i[1]}]
set_property PACKAGE_PIN M13 [get_ports {sw_i[2]}]
set_property PACKAGE_PIN R15 [get_ports {sw_i[3]}]
set_property PACKAGE_PIN R17 [get_ports {sw_i[4]}]
set_property PACKAGE_PIN T18 [get_ports {sw_i[5]}]
set_property PACKAGE_PIN U18 [get_ports {sw_i[6]}]
set_property PACKAGE_PIN R13 [get_ports {sw_i[7]}]
set_property PACKAGE_PIN T8 [get_ports {sw_i[8]}]
set_property PACKAGE_PIN U8 [get_ports {sw_i[9]}]
set_property PACKAGE_PIN R16 [get_ports {sw_i[10]}]
set_property PACKAGE_PIN T13 [get_ports {sw_i[11]}]
set_property PACKAGE_PIN H6 [get_ports {sw_i[12]}]
# ... (其他开关类似)

## LED输出
set_property PACKAGE_PIN H17 [get_ports {led_o[0]}]
set_property PACKAGE_PIN K15 [get_ports {led_o[1]}]
set_property PACKAGE_PIN J13 [get_ports {led_o[2]}]
# ... (根据需要配置)

## 设置所有端口的IO标准
set_property IOSTANDARD LVCMOS33 [get_ports {sw_i[*]}]
set_property IOSTANDARD LVCMOS33 [get_ports {led_o[*]}]
```

---

### XDC约束语法速查

| 约束类型 | 语法 |
|---------|------|
| 引脚位置 | `set_property PACKAGE_PIN <引脚号> [get_ports <信号名>]` |
| IO标准 | `set_property IOSTANDARD <标准> [get_ports <信号>]` |
| 时钟约束 | `create_clock -period <周期> [get_ports <时钟信号>]` |
| IO Bank电压 | `set_property CFGBVS VCCO [current_design]` |

**常用IO标准**：
- **LVCMOS33**：3.3V CMOS，常用于按键、LED
- **LVCMOS18**：1.8V CMOS
- **LVDS**：差分信号

---

## 六、功能仿真：先"纸上谈兵"

在真正烧写到FPGA之前，先用仿真验证功能是否正确——这叫**功能仿真（Behavioral Simulation）**。

### 创建Testbench

**Step 1：添加仿真源文件**

Add Sources → Add or Create Simulation Sources → Create File → 输入名称（如`test_tb`）

**Step 2：编写Testbench**

```verilog
`timescale 1ns/1ps

module test_tb();
    // ==========================================
    // 1. 定义被测试模块的信号
    // ==========================================
    reg clk;
    reg rstn;
    reg [15:0] sw_i;
    wire [15:0] led_o;
    integer foutput;
    
    // ==========================================
    // 2. 例化被测试模块
    // ==========================================
    test u_test(
        .clk(clk),
        .rstn(rstn),
        .sw_i(sw_i),
        .led_o(led_o)
    );
    
    // ==========================================
    // 3. 复位信号生成
    // ==========================================
    initial begin
        clk = 1;
        rstn = 1;
        sw_i = 16'b0000_0000_0001_0100;  // 初始值
        
        foutput = $fopen("results.txt");
        
        #5;
        rstn = 0;   // 拉低复位
        #20;
        rstn = 1;   // 释放复位
    end
    
    // ==========================================
    // 4. 时钟信号生成
    // ==========================================
    always #5 clk = ~clk;  // 100MHz时钟
    
    // ==========================================
    // 5. 仿真过程中的信号变化
    // ==========================================
    always @(posedge clk) begin
        if (rstn == 1'b1) begin
            // 在时钟上升沿显示信号
            $display("sw_i = %h, led_o = %b", sw_i, led_o);
            $fdisplay(foutput, "sw_i = %h, led_o = %b", sw_i, led_o);
        end
    end
    
    // ==========================================
    // 6. 仿真结束
    // ==========================================
    initial begin
        #5000;   // 运行5000ns
        $fclose(foutput);
        $finish;
    end
    
endmodule
```

---

### 运行仿真

1. 点击 **Flow Navigator → Simulation → Run Simulation → Run Behavioral Simulation**
2. Vivado会打开仿真界面
3. 在 **Scopes** 中找到你的模块
4. 在 **Objects** 中选择信号，右键 **Add To Wave Window**
5. 点击 **Run** 运行仿真
6. 查看波形是否与预期一致

---

### 仿真波形查看

仿真波形工具栏功能：
| 按钮 | 功能 |
|-----|------|
| ⏪ | 复位（清空波形）|
| ▶️ | 运行仿真 |
| ⏸ | 暂停 |
| 🔀 | 单步运行 |
| ⏱ | 设置运行时间 |

---

## 七、设计综合：代码变电路

**综合（Synthesis）**是把Verilog代码转换成FPGA内部基本逻辑单元的过程。

### 运行综合

点击 **Run Synthesis**，Vivado会自动：
1. 检查语法错误
2. 优化逻辑
3. 映射到FPGA原语（LUT、FF、DSP等）
4. 生成综合网表

### 查看综合结果

综合完成后，点击 **Open Synthesized Design**：

| 查看内容 | 说明 |
|---------|------|
| **Schematic** | 查看综合后的电路原理图 |
| ** Utilization Report** | 资源使用率报告 |
| **Timing Summary** | 时序报告 |
| **DRC** | 设计规则检查 |

### 综合后的原理图解读

对于简单的组合逻辑，综合后可能会看到：
- **LUT**（查找表）：实现组合逻辑
- **IBUF**（输入缓冲器）：输入信号缓冲
- **OBUF**（输出缓冲器）：输出信号缓冲

对于时序逻辑，还会有：
- **FDRE**（触发器）：D触发器
- **BUFG**（全局时钟缓冲）：时钟信号专用走线

---

## 八、工程实现：布局布线

**实现（Implementation）**把综合后的网表映射到FPGA具体的物理资源上，包括：

| 阶段 | 说明 |
|-----|------|
| **Opt Design** | 优化设计 |
| **Place Design** | 布局（把逻辑放到具体资源上）|
| **Route Design** | 布线（连接各资源）|

### 运行实现

点击 **Run Implementation**，等待完成。

### 查看实现结果

点击 **Open Implemented Design**：

| 查看内容 | 说明 |
|---------|------|
| **Device视图** | 芯片内部资源使用情况 |
| **I/O Planning** | 引脚分配 |
| **Timing** | 时序分析 |

---

## 九、位流生成：生成"配置文件"

比特流（Bitstream）文件是FPGA的"程序"，包含了配置FPGA所有资源的信息。

### 生成位流

点击 **Generate Bitstream**，Vivado会：
1. 读取实现后的设计
2. 生成配置数据
3. 输出.bit文件

生成完成后，位流文件通常位于：
```
<工程目录>/<工程名>.runs/impl_1/<顶层模块>.bit
```

---

## 十、下载到FPGA：见证奇迹

### 连接硬件

1. 用USB线连接开发板和电脑
2. 打开开发板电源开关
3. 等待电脑识别设备

### 用Vivado下载

**Step 1：打开Hardware Manager**

点击 **Flow Navigator → Open Hardware Manager**

**Step 2：连接目标**

点击 **Open Target → Auto Connect**

**Step 3：编程设备**

1. 在 hardware 窗口中右键芯片
2. 选择 **Program Device**
3. 确认Bitstream文件路径
4. 点击 **Program**

---

### 验证结果

下载成功后，观察开发板：
- 如果是LED实验，对应LED应该按预期亮起
- 如果是数码管实验，显示应该正确
- 如果没反应，检查约束文件和代码逻辑

---

## 十一、实验案例：猜数字+跑马灯

### 实验目标

利用FPGA开发板的16个开关和16个LED实现：
- 通过开关输入特定组合（如1010）
- 检测到后点亮对应的LED
- 练习完整的Vivado设计流程

### 完整步骤回顾

| 步骤 | 操作 | 关键点 |
|-----|------|-------|
| 1 | 新建工程 | 选择正确的芯片型号 |
| 2 | 创建Verilog文件 | `test.v` |
| 3 | 编写代码 | 检测开关组合 |
| 4 | 创建XDC约束 | 配置引脚和时钟 |
| 5 | 功能仿真 | 验证逻辑正确性 |
| 6 | 设计综合 | 检查资源使用 |
| 7 | 工程实现 | 布局布线 |
| 8 | 位流生成 | 生成配置文件 |
| 9 | 下载验证 | 观察实际效果 |

---

### 代码实现

```verilog
module test(
    input clk,
    input rstn,
    input [15:0] sw_i,
    output [15:0] led_o
);
    reg ledstate;
    
    // 组合逻辑：检测开关5-8是否为1010
    always@(*)
    begin
        if (sw_i[4:1] == 4'b1010)
            ledstate = 1'b1;
        else
            ledstate = 1'b0;
    end
    
    // 输出连接到LED15
    assign led_o[15] = ledstate;
    
    // 其他LED保持熄灭
    assign led_o[14:0] = 15'b0;
    
endmodule
```

### 约束文件

```xdc
# 时钟约束（100MHz）
create_clock -period 10.000 -name sys_clk_pin -waveform {0 5.000} [get_ports clk]

# 复位约束
set_property PACKAGE_PIN T18 [get_ports rstn]
set_property IOSTANDARD LVCMOS33 [get_ports rstn]

# 开关约束（sw_i[0]到sw_i[7]）
set_property PACKAGE_PIN J15 [get_ports {sw_i[0]}]
set_property PACKAGE_PIN L16 [get_ports {sw_i[1]}]
set_property PACKAGE_PIN M13 [get_ports {sw_i[2]}]
set_property PACKAGE_PIN R15 [get_ports {sw_i[3]}]
set_property PACKAGE_PIN R17 [get_ports {sw_i[4]}]
set_property PACKAGE_PIN T18 [get_ports {sw_i[5]}]
set_property PACKAGE_PIN U18 [get_ports {sw_i[6]}]
set_property PACKAGE_PIN R13 [get_ports {sw_i[7]}]

# LED约束
set_property PACKAGE_PIN H17 [get_ports {led_o[15]}]
set_property IOSTANDARD LVCMOS33 [get_ports {led_o[*]}]
set_property IOSTANDARD LVCMOS33 [get_ports {sw_i[*]}]
```

---

## 附录：常见问题排查

| 问题 | 可能原因 | 解决方法 |
|-----|---------|---------|
| 综合报错 | 语法错误 | 检查代码，特别是分号、括号 |
| 仿真无波形 | 信号未定义或连接错误 | 检查testbench |
| 实现失败 | 时序不满足 | 优化代码或添加约束 |
| 下载后LED不亮 | 引脚约束错误 | 核对原理图和约束文件 |
| 资源不够 | 代码规模超过芯片 | 选择更大芯片或优化代码 |

---

## 附录：Nexys A7开发板资源

| 资源 | 数量/规格 | 备注 |
|-----|----------|------|
| FPGA芯片 | XC7A100T-CSG324 | 我们的目标芯片 |
| 开关 | 16个SW | 输入 |
| LED | 16个LED | 输出 |
| 按钮 | 5个BTN | 复位等 |
| 7段数码管 | 4位 | 显示 |
| 时钟 | 100MHz | 连接在特定引脚 |

---

## 附录：快捷键和技巧

| 操作 | 快捷键 | 说明 |
|-----|-------|------|
| 保存所有 | Ctrl+Shift+S | 保存所有文件 |
| 运行综合 | F6 | 快捷综合 |
| 添加到波形 | Ctrl+W | 在仿真中添加波形 |
| 搜索命令 | Ctrl+P | 快速搜索命令 |
| RTL分析 | Ctrl+Shift+E | 打开RTL分析 |

---

> 整理自VIVADO设计流程课件+FPGA实验文档 | 武汉大学人工智能自强班FPGA课程
>
> 动手实践是最好的学习方式！不要怕出错，多尝试多思考 💪
