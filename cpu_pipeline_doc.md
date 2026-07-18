# RISC-V 五级流水线 CPU 详解

> 项目路径：`/home/yuyang/workspace/vivado/cpu_pipeline/`
> 目标平台：Nexys A7-100T (xc7a100tcsg324-1)
> 指令集：RISC-V RV32I 子集

---

## 总览：五级流水线架构

```
 ┌──────┐    ┌──────┐    ┌──────┐    ┌──────┐    ┌──────┐
 │  IF  │───→│  ID  │───→│  EX  │───→│ MEM  │───→│  WB  │
 │ 取指  │    │ 译码  │    │ 执行  │    │ 访存  │    │ 写回  │
 └──────┘    └──────┘    └──────┘    └──────┘    └──────┘
    │           │           │           │           │
    │   IF_ID   │  ID_EX    │  EX_MEM   │  MEM_WB   │
    │  寄存器    │  寄存器    │  寄存器    │  寄存器    │
    └───────────┘           └───────────┘           └────────
```

每条指令走过 5 个阶段，每个阶段之间由**流水线寄存器**隔开，存放该阶段的中间结果。

---

## 一、顶层模块（`cpu_pipeline.v`）

`SCPU_PIPELINE_TOP` —— 整个 CPU 的顶层连线模块，负责：
1. **时钟分频**：把 100MHz 板载时钟分到肉眼可见的速度
2. **指令存储器**：用 `$readmemh` 从 `.dat` 文件加载指令到 ROM
3. **5 级流水线各模块的实例化与连线**
4. **跳转处理**：ID 阶段直接计算 JAL/JALR 目标，不等 EX
5. **分支处理**：EX 阶段判断分支条件，分支命中后冲刷 IF/ID 和 ID/EX
6. **调试显示**：拨码开关选看 PC、指令、寄存器、ALU、DMEM

### 关键机制

**（一）时钟分频**

```
sw[15]=1 → 计数到 67,108,863 翻转 → ~0.75 Hz（慢速，看信号）
sw[15]=0 → 计数到 16,777,215 翻转 → ~3 Hz（快速）
```

仿真模式（`SIM` 定义）下 `clk_cpu` 每拍翻转一次，跑满速。

**（二）指令存储器**

用 `reg [31:0] imem [0:63]` 存 64 条指令（纯 Verilog ROM，不是 IP 核）。
`pc_cur[7:2]` 把 32 位字节地址转成 6 位字地址索引 ROM。
上电时 `$readmemh(MEM_FILE, imem)` 从 `.dat` 文件加载，其余位置填 NOP（`addi x0, x0, 0`）。

**（三）跳转处理 —— 最核心的设计**

流水线 CPU 最大的问题是 JAL 在 ID 译出来，但 PC 更新要到下个周期。
这里的解法是**在 ID 阶段就算出跳转目标，直接改 pc_next**，不等 EX 阶段：

```
ID 阶段识别出 JAL    → 立即计算出 jump_target_id = if_id_PC + id_imm
                      → pc_next 直接选 jump_target_id（旁路 NPC 输出）
ID 阶段识别出 JALR   → 通过前递拿到 rs1（EX/MEM/WB 的最新值）
                      → 算出 jalr_target_id = (rs1 + imm) & ~1
                      → pc_next 选 jalr_target_id
```

**同时**设置 `jump_handled` 标记：
```
jump_handled <= id_isJump;   // 下一周期为 1
// 跳转后的下一周期强制 NPC 输出 PCPLUS4：
.NPCOp(jump_handled ? 3'b000 : id_ex_NPCOp)
```

这样 JAL 指令到达 EX 阶段时，NPC 看到的 NPCOp 已被强制为 000（顺序执行），
不会再用 EX 阶段的 PC 算出第二次跳转，避免双跳。

**（四）分支处理**

分支条件由 EX 阶段的 ALU 计算结果判断（`beq_taken` / `bne_taken` / ...）。
分支命中时：
```
branch_taken = 1 → pc_next = branch_target_ex = id_ex_PC + id_ex_imm
                  → flush_ID = 1（冲刷 IF/ID，丢掉预取的下一条）
                  → flush_EX = 1（冲刷 ID/EX，丢掉分支后的指令）
```

**（五）冒险控制**

```
PCEn = ~hazard_stall_IF         // Load-use 停顿：PC 不更新
if_id_stall  = hazard_stall_ID  // IF/ID 保持当前值
if_id_flush  = hazard_flush_ID | (id_isJump && ~hazard_stall_ID)
id_ex_flush  = hazard_flush_EX  | (id_isJump && ~hazard_stall_ID)
```

跳转时同时冲刷 IF/ID 和 ID/EX，把 JAL 后面那条取错的指令清掉。

---

## 二、各模块详解

### 1. `PC.v` — 程序计数器

```
输入：clk, rst, NPC[31:0], PCEn
输出：PC[31:0]
```

最简单的模块：
- 复位时 PC = 0
- 每个时钟上升沿，如果 PCEn=1，PC <= NPC
- PCEn=0 时保持不动（用于 Load-use 停顿）

### 2. `NPC.v` — 下一条 PC 计算

```
输入：pc_cur, pc_ex, imm_ext, rs1_val, NPCOp[2:0]
输出：NPC[31:0]
```

组合逻辑，根据 NPCOp 选择：

| NPCOp | 类型 | NPC 计算公式 |
|-------|------|-------------|
| 000 | 顺序执行 | `pc_cur + 4` |
| 001 | 分支 | `pc_ex + imm_ext`（EX 阶段 PC + 偏移） |
| 010 | JAL | `pc_ex + imm_ext` |
| 100 | JALR | `(rs1_val + imm_ext) & ~1`（末位清零保证对齐） |

流水线版本比单周期多了 `pc_cur`（当前取指 PC）和 `pc_ex`（EX 阶段 PC）两个输入——
顺序执行用 `pc_cur` 算（紧跟取指地址），分支/跳转用 `pc_ex` 算（基于 EX 阶段的 PC）。

### 3. 流水线寄存器（4 组）

#### `IF_ID.v` — 取指→译码

```
保存：指令机器码(instr) + PC
控制：stall（保持）/ flush（插入 NOP）
flush 时 → instr_out = 32'h00000013（addi x0, x0, 0，等效 NOP）
stall 时 → 输出保持不变（气泡卡在 IF/ID 里）
```

典型用途：Load-use 检测到冒险时，stall IF 和 IF/ID，同时 flush ID/EX，
被堵住的 load 指令继续前进，而后面跟着的指令被插入气泡。

#### `ID_EX.v` — 译码→执行

```
保存：所有控制信号(RegWrite, MemWrite, ALUSrc, WDSel, ALUOp, NPCOp 等)
      + 操作数(RD1, RD2, imm) + 寄存器编号(rs1, rs2, rd) + PC
flush 时 → 所有控制信号清零（相当于插入气泡指令）
```

这是最胖的流水线寄存器——装了几乎所有译码结果。
flush 后控制信号全 0 → ALU 做 NOP、不写寄存器、不写内存。

#### `EX_MEM.v` — 执行→访存

```
保存：ALU 结果(alu_out) + 写数据(write_data=RD2) + rd + PC
      + 控制信号(RegWrite, MemWrite, WDSel, DMType)
```

ALU 结果传给 DM 做地址，RD2 传给 DM 做写入数据。

**特殊处理**（在顶层中）：
```
.RegWrite_in(id_ex_RegWrite & ~(id_ex_isJump & (id_ex_rd == 5'd0)))
```
JAL 写 x0 时不使能写——x0 永远是 0，没必要写。

#### `MEM_WB.v` — 访存→写回

```
保存：alu_out + mem_data(内存读出) + rd + PC
      + 控制信号(RegWrite, WDSel)
```

写回阶段用 WDSel 从 ALU 结果/内存数据/PC+4 中选一个写入 RF。

### 4. `ctrl.v` — 控制单元（译码器）

输入 Op + Funct7 + Funct3，输出所有控制信号。

**指令识别方式**：先用 Opcode 判断指令大类（R/I/S/SB/U/J 型），
再用 Funct7 + Funct3 细分具体指令。

支持指令（RV32I 子集）：

| 分类 | 指令 |
|------|------|
| R-type | add, sub, sll, srl, sra, slt, sltu, and, or, xor |
| I-type (load) | lb, lh, lw |
| I-type (ALU) | addi, slli, srli, srai, slti, sltiu, andi, ori, xori |
| S-type | sb, sh, sw |
| SB-type | beq, bne, blt, bge, bltu, bgeu |
| U-type | lui, auipc |
| J-type | jal, jalr |

**控制信号输出**：

| 信号 | 说明 |
|------|------|
| RegWrite | 是否写寄存器 |
| MemWrite | 是否写内存 |
| ALUSrc | ALU B 端选立即数(1) 或 RD2(0) |
| WDSel[1:0] | 写回数据来源：00=ALU, 01=MEM, 10=PC+4 |
| NPCOp[2:0] | 下一条 PC 选择 |
| ALUOp[4:0] | ALU 运算类型 |
| EXTOp[5:0] | 立即数扩展类型（独热码） |
| DMType[2:0] | 内存访问宽度 |
| isBranch | 是否为分支指令（流水线冒险用） |
| isJump | 是否为跳转指令（流水线冒险用） |

**详细信号生成表**：

| 指令 | RegWrite | MemWrite | ALUSrc | WDSel | NPCOp | ALUOp |
|------|----------|----------|--------|-------|-------|-------|
| add/sub | 1 | 0 | 0 | 00 | 000 | add/sub |
| addi | 1 | 0 | 1 | 00 | 000 | add |
| lw/lb/lh | 1 | 0 | 1 | 01 | 000 | add |
| sw/sb/sh | 0 | 1 | 1 | 00 | 000 | add |
| beq/bne/... | 0 | 0 | 0 | 00 | 001 | 对应比较 |
| jal | 1 | 0 | 1 | 10 | 010 | add |
| jalr | 1 | 0 | 1 | 10 | 100 | add |
| lui | 1 | 0 | 1 | 00 | 000 | lui |
| auipc | 1 | 0 | 1 | 00 | 000 | auipc |

### 5. `ALU.v` — 算术逻辑单元

```
输入：A[31:0], B[31:0], PC[31:0], ALUOp[4:0]
输出：C[31:0], Zero
```

32 位 ALU，支持：

| ALUOp | 运算 | C 输出 |
|-------|------|--------|
| 00000 | NOP | 0 |
| 00001 | LUI | B |
| 00010 | AUIPC | PC + B |
| 00011 | ADD | A + B |
| 00100 | SUB | A - B |
| 00101 | BEQ | A - B（Zero=1 当 A==B） |
| 00110 | BNE | {31'b0, (A!=B)} |
| 00111 | BLT | {31'b0, (A<B) 有符号} |
| 01000 | BGE | {31'b0, (A>=B) 有符号} |
| 01001 | BLTU | {31'b0, (A<B) 无符号} |
| 01010 | BGEU | {31'b0, (A>=B) 无符号} |
| 10001 | SLL | A << B[4:0] |
| 10010 | SRL | A >> B[4:0] |
| 10100 | SRA | $signed(A) >>> B[4:0] |
| 11000 | SLT | {31'b0, $signed(A)<$signed(B)} |
| 11001 | SLTU | {31'b0, A < B} |
| 01100 | AND | A & B |
| 01110 | OR | A | B |
| 01101 | XOR | A ^ B |

`Zero` = (C == 0)，分支指令用 Zero 判断条件是否成立。

分支指令的 Zero 语义：
- BEQ: C = A-B, Zero=1 表示 A==B → 跳转
- BNE: C = {31'b0, A!=B}, Zero=1 表示 A!=B → 跳转
- BLT: C = {31'b0, A<B}, Zero=1 表示 A<B → 跳转

### 6. `RF.v` — 寄存器堆

```
32 个 32 位寄存器（x0~x31）
输入：A1(读1), A2(读2), A3(写), WD(写数据), RFWr(写使能)
输出：RD1, RD2
```

**重要特性**：

1. **异步读**：组合逻辑输出寄存器的值，不用等时钟
2. **同步写**：时钟上升沿写入
3. **写透传（Write-Through）**：同一拍内，如果读地址 == 写地址（且 RFWr=1），
   读端口直接返回当前正在写入的数据（WD），而不是旧的寄存器值
4. **x0 硬连线为 0**：读 A1/A2=0 返回 0；写 A3=0 忽略；复位后全 0
5. **调试端口**：`A_display` / `RD_display` 独立于正常读写，供数码管显示

**写透传的作用**：WB 阶段写回 RF 的同时，后面指令的 ID 阶段可能正在读同一个寄存器。
有了写透传，ID 阶段读到 RD1/RD2 时如果发现 WB 正在写同一个寄存器，
会直接拿到最新值——这就是最后一道"前递"防线。

### 7. `ext.v` — 立即数扩展

| EXTOp | 类型 | 扩展方式 | 指令例子 |
|-------|------|----------|---------|
| 100000 | shift | 零扩展 5 位 | slli, srli, srai |
| 010000 | I-type | 符号扩展 12 位 | addi, lw, lb, lh, jalr |
| 001000 | S-type | 符号扩展 12 位 | sw, sb, sh |
| 000100 | B-type | 符号扩展 + 左移 1 位 | beq, bne, ... |
| 000010 | U-type | 高 20 位，低 12 位补 0 | lui, auipc |
| 000001 | J-type | 符号扩展 + 左移 1 位 | jal |

B 型和 J 型左移 1 位：RISC-V 分支/跳转偏移量以 2 字节为单位，左移 1 位 = 乘 2。

### 8. `dm.v` — 数据存储器

```
128 字节（地址 0~127），按字节组织
支持：字(32-bit)、半字(16-bit)、字节(8-bit) 读写
小端序（RISC-V 标准）
```

**写操作**（同步，时钟上升沿）：

| DMType | 写入方式 | 地址限制 |
|--------|---------|---------|
| 000 (word) | 分 4 字节写：addr+0~addr+3 | addr <= 124 |
| 001 (halfword) | 分 2 字节写：addr+0~addr+1 | addr <= 126 |
| 011 (byte) | 写 1 字节：addr | addr <= 127 |

字写入（`addr=8, din=0x12345678`）：
```
dmem[8]  <= 0x78    // din[7:0]
dmem[9]  <= 0x56    // din[15:8]
dmem[10] <= 0x34    // din[23:16]
dmem[11] <= 0x12    // din[31:24]
```

**读操作**（组合逻辑，半字/字节带符号扩展）。

**调试端口**：`disp_addr[6:0]` + `disp_data[7:0]` 独立读端口，
sw[10]=1 时选地址查看内存内容（sw[6:0] 选地址）。

### 9. `HazardUnit.v` — 冒险检测单元

处理三种冒险：

**（一）数据前递（Forwarding）**

```
EX 阶段的加法需要 rs1 的值
但 rs1 的源是上一条 lw 的结果（还在 MEM 阶段）
→ 不从 ID/EX 寄存器读旧值
→ 直接从 EX/MEM 寄存器拿 ALU 结果
```

前递优先级：`00=ID/EX默认 → 01=MEM前递(alu_out) → 10=WB前递(wb_wd)`

前递条件：
```
// MEM → EX
if (mem_RegWrite && mem_rd != 0 && mem_rd == ex_rs1)
    forwardA = 2'b01
// WB → EX（且 MEM 没有抢先）
if (wb_RegWrite && wb_rd != 0 && wb_rd == ex_rs1
    && !(mem_RegWrite && mem_rd == ex_rs1 && mem_rd != 0))
    forwardA = 2'b10
```

**（二）Load-Use 停顿（Stall）**

EX 阶段 load 指令要从内存读值写回寄存器，
下一条指令（ID）立刻要用同一个寄存器的值 —— 前递来不及，必须停 1 周期：

```
load_use_hazard = ex_MemtoReg && ex_rd != 0
                  && (ex_rd == id_rs1 || ex_rd == id_rs2)

stall_IF = 1  → PC 不更新
stall_ID = 1  → IF/ID 保持
flush_EX = 1  → ID/EX 插入气泡（load 进 MEM，空出 EX）
```

时序效果：
```
Cycle  :  1       2       3       4
lw     :  IF      ID      EX      MEM → WB
add    :  IF      ID(stall) (flush) ID → EX
              ↑ 气泡插入 →
```

**（三）分支冲刷（Branch Flush）**

分支预测策略：**默认不跳转**（predict not taken）。
EX 阶段发现 `branch_taken=1` → IF 和 ID 的指令预取错了 → 冲刷：

```
flush_ID = 1  → IF/ID 插入气泡（丢掉取错的指令）
flush_EX = 1  → ID/EX 插入气泡（丢掉译错的那条）
```

JAL/JALR 由 ID 阶段的 `id_isJump` 在顶层直接冲刷（不等 HazardUnit），
所以 HazardUnit 里 `ex_isJump` 不触发额外冲刷（注释标注了这一点）。

### 10. 宏定义文件

| 文件 | 内容 |
|------|------|
| `alu_defines.v` | ALUOp 各操作编码 |
| `ext_defines.v` | EXTOp 各扩展类型编码（6 位独热码） |
| `dm_defines.v` | DMType 各访问模式编码 |
| `mux_defines.v` | WDSel 写回选择 + NPCOp 下一条 PC 选择 |

---

## 三、数据通路完整流程

以 `add x3, x1, x2` 为例（x1=5, x2=3）：

```
Cycle 1 — IF
  PC <= 0x00
  ROM读出指令 0x002081B3 (add x3, x1, x2)
  时钟上升沿 → IF/ID 保存指令+PC

Cycle 2 — ID
  ctrl 译出：RegWrite=1, ALUSrc=0, ALUOp=add, NPCOp=000
  RF读出：RD1=5(x1), RD2=3(x2)
  时钟上升沿 → ID/EX 保存控制信号+操作数

Cycle 3 — EX
  ALU: A=5, B=3, ALUOp=add → C=8
  时钟上升沿 → EX/MEM 保存 alu_out=8, rd=3, RegWrite=1

Cycle 4 — MEM
  add 不写内存
  时钟上升沿 → MEM/WB 保存 alu_out=8, rd=3

Cycle 5 — WB
  WDSel=00 → wb_wd = alu_out = 8
  RFWr=1 → rf[3] <= 8
```

理想吞吐率 = 1 IPC（无冒险时每周期完成一条指令）。

---

## 四、跳转流程详解

### JAL x1, label

```
Cycle N (IF)   : 取到 JAL 指令
Cycle N (ID)   : ctrl → isJump=1
                 计算 jump_target_id = PC + imm
                 pc_next = jump_target_id（旁路 NPC）
                 jump_handled <= 1
                 flush IF/ID + ID/EX
Cycle N+1 (IF) : PC = 跳转目标 → 取目标指令
                 jump_handled=1 → NPC 强制 PCPLUS4
                 （JAL 到 EX，但 NPC 不理它的 NPCOp）
Cycle N+5 (WB) : JAL 写回 ra = 原 PC + 4
```

### JALR x1, 0(x2)

跳转目标来自寄存器 x2：
```
jump_target_id = (前递后的 x2 + imm) & 0xFFFFFFFE
```

JALR 前递链路（比普通指令多一层）：
```
jalr_rs1 = EX 阶段正在算 ? alu_C :
           MEM 的 load 结果 ? mem_dout :
           MEM 的 ALU 结果 ? ex_mem_alu_out :
           RF 默认值
```

---

## 五、调试功能

通过 Nexys A7 拨码开关（SW）和 8 位数码管查看内部状态：

| 开关 | 功能 |
|------|------|
| SW[15] | 时钟速度：1=慢速(~0.75Hz)，0=快速(~3Hz) |
| SW[14] | 显示当前指令机器码 |
| SW[13] | 显示写回数据(wb_wd) |
| SW[12] | 显示 ALU 内部（轮流 A/B/C/Zero） |
| SW[11] | 显示当前 PC |
| SW[10] | 显示内存字节（SW[6:0] 选地址 0~127） |
| SW[9] | 显示寄存器（SW[4:0] 选编号 0~31） |
| 默认 | 显示当前指令机器码 |

---

## 六、仿真与运行

### 测试文件

| 文件 | 内容 |
|------|------|
| `sim_1/new/tb_pipeline.v` | 基础流水线测试 |
| `sim_1/new/tb_sim1.v` ~ `tb_sim3.v` | 无/有数据依赖测试 |
| `sim_1/new/tb_fib.v` | Fibonacci 汇编测试 |
| `sim_1/new/tb_fib_sim.v` | Fibonacci 仿真（带 $display） |
| `sim_1/new/tb_bubble.v` | 冒泡排序测试 |
| `sim_1/new/tb_branch.v` | 分支指令测试 |
| `sim_1/new/tb_min.v` | 最小化测试 |

### 运行脚本

| 脚本 | 用途 |
|------|------|
| `run_sort_sim.tcl` | 运行排序仿真 |
| `run_bubble.tcl` | 运行冒泡测试仿真 |
| `board_tests/` | 存放板级测试 `.dat` 文件 |

运行方式（Vivado Tcl Console）：
```tcl
source run_sort_sim.tcl
```
