# 第六章：并行处理器——从客户端到云端

---

## 一、并行计算导论

![[第六章1]]

**图示讲解**：
这张图是第六章的封面页，展示了章节主题"Parallel Processors from Client to Cloud"。页面采用学术演示的标准排版：
- **深蓝色标题栏**：章节编号"Chapter 6"与主题"Parallel Processors from Client to Cloud"醒目呈现
- **MK标识**：Morgan Kaufmann出版社的品牌印记，位于左下角
- **撞色设计**：红色星芒形徽章标注"RISC-V Edition"，与深灰蓝主色调形成视觉焦点

---

![[第六章2]]

**图示讲解**：
这张图展示了并行计算的核心目标与基本概念。内容分为三个层次：
- **浅米色一级条目**：
  - **Goal**：连接多个计算机以获得更高性能
  - **Task-level parallelism**：适用于独立作业的高吞吐量处理
  - **Parallel processing program**：单个程序在多个处理器上运行
  - **Multicore microprocessors**：芯片上集成多个处理器核心
- **灰色二级条目**补充说明：
  - **Scalability, availability, power efficiency**：多处理器的三大优势
  - **Single program run on multiple processors**：并行程序需分解任务协调执行

**核心概念**：
- **任务级并行（Task-level parallelism）**：多个独立作业可并行处理，提高系统吞吐量
- **多核处理器**：在单个芯片上集成多个处理器核心，是现代计算的主流

---

![[第六章3]]

**图示讲解**：
这张图从硬件和软件两个维度分析了并行计算的分类：
- **Hardware（硬件）**：
  - Serial（如Pentium 4）：串行处理器，一次执行一条指令流
  - Parallel（如quad-core Xeon e5345）：并行处理器，同时执行多条指令流
- **Software（软件）**：
  - Sequential（如matrix multiplication）：串行软件，按顺序执行
  - Concurrent（如operating system）：并发软件，可同时处理多任务
- **核心挑战**：如何有效利用并行硬件

**核心概念**：
- **软硬件组合**：串行/并发软件可在串行/并行硬件上运行
- **并行效率**：挑战在于让软件充分发挥并行硬件的性能潜力

---

![[第六章4]]

**图示讲解**：
这张图回顾了前几章中已涉及的并行相关主题，构建知识关联：
- **浅米色一级条目**：四个已学习章节
  - §2.11: 同步机制与指令级并行
  - §3.6: 算术运算中的并行性
  - §4.10: 超标量和乱序执行等高级ILP技术
  - §5.10: 缓存一致性协议
- **灰色二级条目**：每个主题的子内容
  - Synchronization（同步）
  - Subword Parallelism（子字并行）
  - Cache Coherence（缓存一致性）

**核心概念**：
- **指令级并行（ILP）**：第二章引入，后续各章深化
- **并行贯穿全书**：从指令级到系统级，并行是核心主题

---

![[第六章5]]

**图示讲解**：
这张图分析了并行编程的三大挑战，揭示并行软件为何难以开发：
- **核心观点**：
  - **Parallel software is the problem**：并行软件是主要难题
  - **Need to get significant performance improvement**：必须有足够的性能提升才值得
  - **Difficulties**：开发难度大
- **三大挑战（灰色二级条目）**：
  - **Partitioning（划分）**：将大问题分解为可并行的子任务
  - **Coordination（协调）**：多任务如何协同工作，共享数据和同步
  - **Communications overhead（通信开销）**：处理器间数据传输成本可能抵消并行收益

**核心概念**：
- **划分（Partitioning）**：识别可并行执行的部分，保持任务独立性
- **协调（Coordination）**：处理同步机制，最小化通信量
- **通信开销**：关键在于平衡并行收益与通信成本

---

## 二、阿姆达尔定律

![[第六章6]]

**图示讲解**：
这张图是阿姆达尔定律的核心公式与推导示例：
- **核心公式**：Speedup = 1 / ((1-F_parallelizable) + F_parallelizable/N)
- **公式变量**：
  - F_parallelizable：可并行部分的时间占比
  - N：处理器数量
  - T_new = T_parallelizable/100 + T_sequential
- **示例推导**：100个处理器获得90×加速比
  - 求解得 F_parallelizable = 0.999
  - **结论**：串行部分必须仅占原时间的0.1%！

**核心概念**：
- **串行瓶颈**：即使无限多处理器，串行部分仍限制加速比
- **极端要求**：90倍加速比需要99.9%的代码必须可并行化

---

![[第六章8]]

**图示讲解**：
这张图展示了扩展性对加速比影响的实际计算示例：
- **任务描述**：求和10个标量 + 100×100矩阵（共10010个加法）
- **单处理器**：Time = 10010 × t_add
- **10个处理器**：Time = 1010 × t_add，加速比 = 9.9（理论值的99%）
- **100个处理器**：Time = 110 × t_add，加速比 = 91（理论值的91%）
- **前提**：假设负载均衡

**核心概念**：
- **加速比计算**：T_new = T_sequential + T_parallelizable/N
- **规模效应**：问题规模越大，并行效率越高
- **实际意义**：大规模问题更适合并行处理

---

![[第六章9]]

**图示讲解**：
这张图对比了强扩展与弱扩展两种并行扩展模型：
- **Strong scaling（强扩展）**：
  - 问题规模固定
  - 增加处理器数量以减少执行时间
  - 10 processors, 10×10 matrix
- **Weak scaling（弱扩展）**：
  - 问题规模与处理器数量成比例
  - 每个处理器处理的数据量基本不变
  - 100 processors, 32×32 matrix
- **时间对比**：
  - 强扩展：Time = 20 × t_add
  - 弱扩展：Time = 10 × t_add + 1000/100 × t_add = 20 × t_add
  - **结论**：此例中性能保持恒定

**核心概念**：
- **强扩展**：固定问题规模，适合单机性能优化
- **弱扩展**：规模随处理器增长，更易实现良好扩展性

---

## 三、Flynn分类法

![[第六章10]]

**图示讲解**：
这张图展示了Flynn分类法的2×2矩阵分类体系：
- **SISD**（左上）：Single Instruction, Single Data
  - 单指令流处理单数据流
  - 示例：Intel Pentium 4
- **SIMD**（右上）：Single Instruction, Multiple Data
  - 单指令流处理多数据流
  - 示例：x86的SSE指令
- **MISD**（左下）：Multiple Instruction, Single Data
  - 多指令流处理单数据流
  - 示例：今天没有实际例子
- **MIMD**（右下）：Multiple Instruction, Multiple Data
  - 多指令流处理多数据流
  - 示例：Intel Xeon e5345
- **SPMD**：
  - Single Program Multiple Data
  - 在MIMD上运行的并行编程模式
  - 通过条件代码实现不同处理器执行不同分支

**核心概念**：
- **MIMD**：最灵活的并行架构，现代多核处理器主流
- **SPMD**：融合SIMD简单性与MIMD灵活性的编程模型
- **条件代码**：SPMD中不同处理器根据ID执行不同逻辑

---

## 四、向量处理器与SIMD架构

![[第六章11]]

**图示讲解**：
这张图介绍了向量处理器和RISC-V向量扩展的核心特性：
- **向量处理器的三个特征**：
  - **Highly pipelined function units**：高度流水线的功能单元
  - **Stream data from/to vector registers to units**：流式数据传输
  - **Significantly reduces instruction-fetch bandwidth**：减少指令获取带宽
- **RISC-V向量扩展**：
  - **v0 to v31**：32个向量寄存器
  - **64-element registers (64-bit elements)**：每个寄存器可存64个64位元素
  - **向量指令**：fld.v, fsd.v（加载/存储向量）、fadd.d.v（向量加法）、fadd.d.vs（标量加向量）

**核心概念**：
- **流水线执行**：多个指令同时处于不同执行阶段
- **向量寄存器**：提供大规模数据并行能力
- **流式传输**：减少访存延迟，提高吞吐量

---

![[第六章12]]

**图示讲解**：
这张图对比了DAXPY（Y = a×X + Y）的标量与向量实现：
- **Conventional RISC-V code（常规标量代码）**：
  - 循环执行，每次处理一个元素
  - 需显式循环控制和多次内存访问
  - 红色标注显示数据在f1和f2寄存器间流动
- **Vector RISC-V code（向量代码）**：
  - 仅需4条指令即可处理整个向量
  - fld.v：加载向量X
  - fmul.d.v：向量乘标量a
  - fadd.d.v：向量加Y
  - fsd.v：存储结果

**核心概念**：
- **循环消除**：向量代码消除显式循环，减少控制开销
- **指令减少**：4条指令替代n次循环迭代
- **数据并行**：一条向量指令处理多个数据元素

---

![[第六章13]]

**图示讲解**：
这张图对比了向量架构与多媒体扩展的优劣：
- **向量架构优势**：
  - **More general than ad-hoc media extensions**：比临时多媒体扩展（如MMX、SSE）更通用
  - **Simplify data-parallel programming**：简化数据并行编程
  - **Explicit statement of absence of loop-carried dependences**：显式声明无循环依赖
- **无循环依赖的意义**：
  - **Reduced checking in hardware**：硬件减少依赖检查
  - 编译器可安全优化
  - 硬件假设向量操作元素独立

**核心概念**：
- **灵活性**：向量架构支持可变向量宽度，适应不同数据规模
- **硬件简化**：显式声明使硬件减少依赖检查开销
- **编译器友好**：编译器可将循环自动转换为向量指令

---

![[第六章14]]

**图示讲解**：
这张图详细介绍了SIMD架构的工作原理与特点：
- **核心特征**：
  - **Operate elementwise on vectors of data**：在向量数据上逐元素操作
  - **All processors execute the same instruction at the same time**：所有处理器同一时刻执行相同指令
- **SIMD优势**：
  - **Simplifies synchronization**：简化同步（锁步执行）
  - **Reduced instruction control hardware**：减少指令控制硬件
  - **Works best for highly data-parallel applications**：适合高度数据并行应用
- **实现示例**：
  - MMX和SSE指令
  - 128位宽寄存器可存放多个数据元素

**核心概念**：
- **锁步执行**：SIMD处理器同步执行，无需复杂调度
- **控制简化**：单一控制单元驱动多个执行单元
- **适用场景**：图像处理、信号处理、多媒体应用

---

![[第六章15]]

**图示讲解**：
这张图对比了向量指令与多媒体扩展的关键差异：
- **三大差异**：
  - **Variable vs. Fixed width**：向量指令可变宽度，多媒体扩展固定宽度（如SSE固定128位）
  - **Strided access support**：向量指令支持跨步访问，多媒体扩展不支持
- **向量单元架构图示**：
  - 多个Lane并行工作
  - 每个Lane包含FP add pipe（浮点加法流水线）
  - 向量寄存器文件连接各功能单元
  - Vector load/store unit处理内存访问
- **跨步访问示意**：可访问非连续内存模式

**核心概念**：
- **向量宽度灵活性**：根据问题规模动态调整向量长度
- **跨步访问**：支持A[8], A[9]等非连续数据的灵活访问
- **流水线+阵列**：结合流水线吞吐量和阵列并行性

---

## 五、硬件多线程技术

![[第六章16]]

**图示讲解**：
这张图介绍了三种硬件多线程技术的基本概念：
- **核心定义**：Performing multiple threads of execution in parallel
  - 复制寄存器、PC等状态
  - 线程间快速切换
- **Fine-grain multithreading（细粒度多线程）**：
  - **Switch threads after each cycle**：每个周期后切换线程
  - **Interleave instruction execution**：交错执行指令
  - **If one thread stalls, others are executed**：一线程停顿时执行其他线程
- **Coarse-grain multithreading（粗粒度多线程）**：
  - **Only switch on long stall**：仅在长延迟停顿时切换
  - **Simplifies hardware**：简化硬件
  - **Doesn't hide short stalls**：无法隐藏短停顿（如数据hazard）

**核心概念**：
- **状态复制**：多线程需要复制寄存器文件等状态信息
- **停顿隐藏**：多线程的主要目标是隐藏内存访问延迟
- **粒度权衡**：细粒度切换频繁但延迟隐藏好，粗粒度反之

---

![[第六章17]]

**图示讲解**：
这张图详细介绍了同时多线程（SMT）技术：
- **SMT定义**：In multiple-issue dynamically scheduled processor
- **Intel Pentium-4 HT示例**：
  - 从多线程调度指令
  - 功能单元可用时执行不同线程的指令
  - 线程内依赖由调度和寄存器重命名处理
- **Hyper-Threading特点**：
  - **Duplicated registers**：复制寄存器
  - **Shared function units and caches**：共享功能单元和缓存

**核心概念**：
- **指令级并行**：SMT充分利用超标量处理器的发射能力
- **资源共享**：复制寄存器但共享执行单元，平衡面积与性能
- **动态调度**：调度器从多个线程选择指令同时发射

---

![[第六章18]]

**图示讲解**：
这张图通过时序图对比了三种多线程技术的执行模式：
- **上方模块（独立线程执行）**：
  - Thread A、B、C、D顺序执行
  - 各线程在不同时间段运行，无重叠
- **下方模块（三种技术对比）**：
  - **Coarse MT**：粗粒度切换，线程执行时段较长
  - **Fine MT**：细粒度切换，不同颜色密集交替
  - **SMT**：同一发射槽内混合多种颜色
  - **关键差异**：SMT同一周期可发射来自多个线程的指令

**核心概念**：
- **发射槽利用率**：SMT > Fine MT > Coarse MT
- **并发度**：SMT实现真正的指令级并行
- **效率对比**：SMT充分利用所有执行资源

---

![[第六章19]]

**图示讲解**：
这张图讨论了多线程技术的未来发展趋势：
- **核心问题**：Will it survive? In what form?
- **功耗约束**：
  - **Power considerations**：功耗成为设计主要约束
  - **Simplified microarchitectures**：推动微架构简化
  - **Simpler forms of multithreading**：更简单的多线程形式可能取代复杂SMT
- **发展方向**：
  - **Tolerating cache-miss latency**：继续用于容忍缓存未命中延迟
  - **Multiple simple cores might share resources more effectively**：多个简单核心可能更有效共享资源

**核心概念**：
- **功耗墙**：功耗约束推动设计权衡
- **多核化**：简单核心组合可能优于复杂单核
- **延迟容忍**：多线程的核心价值在于隐藏内存延迟

---

## 六、共享内存多处理器

![[第六章20]]

**图示讲解**：
这张图介绍了共享内存多处理器（SMP）的基本架构：
- **SMP定义**：Shared Memory Multiprocessor
  - 硬件提供单一物理地址空间
  - 使用锁同步共享变量
  - 内存访问时间特性决定类型
- **UMA vs. NUMA**：
  - **UMA**：Uniform Memory Access，统一内存访问
  - **NUMA**：Non-Uniform Memory Access，非均匀内存访问
- **架构示意图**：
  - 多个Processor通过Cache连接Interconnection Network
  - Network连接共享Memory和I/O

**核心概念**：
- **单一地址空间**：所有处理器共享物理内存
- **一致性挑战**：需要缓存一致性协议
- **NUMA特性**：远端内存访问延迟高于本地

---

![[第六章21]]

**图示讲解**：
这张图展示了在UMA多处理器上求和归约的并行化策略：
- **任务**：在64处理器UMA上求和64000个数
- **第一阶段（分区）**：
  - Each processor has ID: 0 ≤ Pn ≤ 63
  - Partition 1000 numbers per processor
  - 每处理器计算局部和：sum[Pn] += A[i]
- **第二阶段（归约）**：
  - **Reduction**：分治法
  - Half the processors add pairs
  - Then quarter, then eighth...
  - **需要同步**：归约步骤间必须同步

**核心概念**：
- **两阶段策略**：分区计算局部和 → 归约合并
- **树形归约**：log₂N步完成N个数求和
- **同步必要性**：归约步骤间必须等待所有处理器完成

---

![[第六章22]]

**图示讲解**：
这张图给出了归约求和的完整代码与树形执行图：
- **代码示例**：
  - `half = 64`
  - `synch()`：红色高亮，同步操作
  - `if (half%2 != 0 && Pn == 0) sum[0] += sum[half-1]`：奇数处理
  - `if (Pn < half) sum[Pn] += sum[Pn + half]`：配对加法
- **树形归约图示**：
  - half = 1：2个处理器合并
  - half = 2：4个处理器合并
  - half = 4：8个处理器合并
  - 最终所有处理器参与归约

**核心概念**：
- **配对同步**：处理器与其配对伙伴同步交换数据
- **奇数处理**：当half为奇数时，处理器0处理最后一个元素
- **对数复杂度**：log₂N轮完成全局归约

---

## 七、GPU架构

![[第六章23]]

**图示讲解**：
这张图回顾了GPU从图形处理器到通用计算的演进历程：
- **Early video cards（早期显卡）**：
  - Frame buffer memory with address generation for video output
  - 简单帧缓冲，功能单一
- **3D graphics processing（3D图形处理）**：
  - Originally high-end computers（如SGI）
  - Moore's Law ⇒ lower cost, higher density
  - 3D graphics cards for PCs and game consoles
- **Graphics Processing Units（GPU）**：
  - Processors oriented to 3D graphics tasks
  - Vertex/pixel processing, shading, texture mapping, rasterization
  - 功能不断增强

**核心概念**：
- **Moore定律驱动**：成本降低、密度提升推动GPU普及
- **图形管线**：顶点处理、像素着色、纹理映射、光栅化
- **通用化前奏**：GPU架构日益强大，为后续GPGPU奠定基础

---

![[第六章24]]

**图示讲解**：
这张图展示了GPU在系统中的三种集成架构演变：
- **早期架构（左侧）**：
  - CPU → Front Side Bus → North Bridge
  - North Bridge连接Memory、VGA Controller
  - VGA Controller → Framebuffer Memory → Display
  - 图形通过专用VGA控制器处理
- **中期架构（中部）**：
  - Intel CPU + North Bridge
  - 128-bit DDR2 Memory (667 MT/s)
  - x16 PCI-Express连接GPU
  - GPU独立显存
- **现代架构（右侧）**：
  - AMD集成方案
  - CPU core集成North Bridge
  - HyperTransport连接Chipset
  - GPU通过PCIe连接

**核心概念**：
- **CPU-GPU分离**：传统架构中GPU是独立设备
- **集成趋势**：现代处理器将更多功能集成到芯片上
- **带宽提升**：从FSB到PCIe，互联带宽持续增加

---

![[第六章25]]

**图示讲解**：
这张图概述了GPU架构的核心特征与编程环境：
- **GPU处理特点**：
  - **Highly data-parallel**：高度数据并行
  - **Highly multithreaded**：高度多线程化
  - **Use thread switching to hide memory latency**：用线程切换隐藏内存延迟
  - **Less reliance on multi-level caches**：减少对多级缓存的依赖
  - **Graphics memory is wide and high-bandwidth**：图形内存宽且带宽高
- **异构趋势**：
  - **Heterogeneous CPU/GPU systems**：CPU处理串行代码，GPU处理并行代码
- **编程语言/API**：
  - DirectX, OpenGL
  - Cg, HLSL
  - **CUDA**：Compute Unified Device Architecture

**核心概念**：
- **CPU-GPU分工**：串行代码CPU执行，并行代码GPU执行
- **线程切换**：GPU通过大量线程切换隐藏内存访问延迟
- **CUDA统一计算**：NVIDIA推出的通用并行计算平台

---

![[第六章26]]

**图示讲解**：
这张图是NVIDIA Fermi架构的详细结构图：
- **顶部**：Instruction register发出指令
- **16组SIMD Lanes（线程处理器）**：
  - 每个Lane有Registers (1K×32)
  - Load/Store unit处理内存访问
  - 16条并行数据通路
- **地址合并单元（Address coalescing unit）**：
  - 合并多个内存访问请求
  - 优化内存带宽利用
- **互连网络（Interconnection network）**：
  - 连接各处理单元
  - 连接本地存储与全局存储
- **本地存储（Local Memory 64 KiB）**：
  - 每个SIMD处理器私有的高速存储

**核心概念**：
- **SIMD并行**：16个并行通道处理数据
- **地址合并**：合并相邻线程的内存访问为合并访问
- **层次存储**：寄存器→本地存储→全局存储

---

![[第六章27]]

**图示讲解**：
这张图详细说明了Fermi架构SIMD处理器的规格参数：
- **SIMD Processor配置**：
  - **16 SIMD lanes**：16条并行通道
  - **SIMD instruction**：单指令驱动16通道
  - **32K × 32-bit registers spread across lanes**：跨Lane分布的寄存器文件
- **执行特性**：
  - **Operates on 32 element wide threads**：每个线程操作32元素宽度
  - **Dynamically scheduled on 16-wide processor over 2 cycles**：16宽处理器上动态调度，2周期完成
  - **64 registers per thread context**：每线程上下文64个寄存器

**核心概念**：
- **Warp概念**：32元素线程在16宽处理器上分2周期执行
- **寄存器分布**：大量寄存器支持多线程上下文
- **动态调度**：硬件调度器管理线程执行

---

![[第六章28]]

**图示讲解**：
这张图展示了GPU的内存层次结构与数据流：
- **CUDA Thread（单线程）**：
  - Per-CUDA Thread Private Memory
  - 每个线程私有的临时数据
- **Thread block（线程块）**：
  - Per-Block Local Memory
  - 线程块内线程共享的本地存储
- **Grid（网格）**：
  - Grid 0 → Grid 1（执行顺序）
  - 多个线程块可顺序执行
- **GPU Memory（全局显存）**：
  - 所有线程可访问的全局存储
  - 带宽高但延迟大
- **Inter-Grid Synchronization**：网格间同步（通过软件）

**核心概念**：
- **私有→本地→全局**：从线程私有到全局的内存层次
- **线程块协作**：块内线程通过本地存储通信
- **网格执行**：多个线程块顺序执行组成完整程序

---

![[第六章29]]

**图示讲解**：
这张图分析了GPU在SIMD/MIMD分类中的特殊地位：
- **核心观点**：Don't fit nicely into SIMD/MIMD model
  - 条件执行允许MIMD的假象
  - 但会导致性能下降
- **分类对比表**：
  - **ILP vs. DLP**：指令级并行 vs. 数据级并行
  - **Static vs. Dynamic**：静态发现 vs. 动态发现
  - Tesla Multiprocessor：动态发现数据级并行
- **编程注意**：Need to write general purpose code with care

**核心概念**：
- **GPU特殊性**：不完全符合传统SIMD/MIMD分类
- **条件执行代价**：分支导致执行路径串行化
- **性能权衡**：灵活性与性能的取舍

---

![[第六章30]]

**图示讲解**：
这张对比表详细对比了多核+SIMD与GPU的架构差异：

| 特性 | Multicore with SIMD | GPU |
|------|---------------------|-----|
| SIMD处理器数量 | 4-8 | 8-16 |
| 每处理器SIMD通道数 | 2-4 | 8-16 |
| SIMD线程多线程支持 | 2-4 | 16-32 |
| 单/双精度比率 | 2:1 | 2:1 |
| 最大缓存大小 | 8 MB | 0.75 MB |
| 内存地址大小 | 64-bit | 64-bit |
| 主存大小 | 8-256 GB | 4-6 GB |
| 页级内存保护 | Yes | Yes |
| 请求分页 | Yes | **No** |
| 集成标量处理器 | Yes | **No** |
| 缓存一致性 | Yes | **No** |

**核心概念**：
- **GPU线程更多**：支持大量并发线程
- **缓存更小**：GPU减少缓存依赖，依赖线程切换
- **无分页/无一致性**：GPU设计优先吞吐量而非灵活性

---

![[第六章31]]

**图示讲解**：
这张术语对照表统一了GPU相关概念与传统并行计算术语：

| 类型 | 更具描述性名称 | 最接近旧术语 | CUDA/NVIDIA术语 | 本书定义 |
|------|--------------|-------------|----------------|---------|
| 程序抽象 | Vectorizable Loop | 向量化循环 | **Grid** | GPU上执行的向量化循环 |
| 程序抽象 | Body of Vectorized Loop | 循环体 | **Thread Block** | SIMD处理器上执行的循环体 |
| 程序抽象 | One iteration | 标量循环迭代 | **CUDA Thread** | 单SIMD通道执行的一个元素 |
| 机器对象 | Thread of SIMD Instructions | 向量指令序列 | **Warp** | SIMD指令线程（32元素） |
| 机器对象 | SIMD Instruction | 向量指令 | **PTX Instruction** | 所有通道执行的单条指令 |
| 处理硬件 | Multithreaded SIMD Processor | 多线程向量处理器 | **SM (Streaming Multiprocessor)** | 执行Warp的硬件单元 |

**核心概念**：
- **Grid→Thread Block→Warp→Thread**：四级层次结构
- **硬件映射**：Grid对应整体程序，Thread对应基本执行单元
- **术语统一**：帮助理解GPU与传统并行架构的对应关系

---

## 八、消息传递与集群

![[第六章32]]

**图示讲解**：
这张图展示了消息传递架构的基本特征：
- **核心特征**：
  - **Each processor has private physical address space**：每个处理器有私有物理地址空间
  - **Hardware sends/receives messages between processors**：硬件提供发送/接收消息机制
- **架构示意图**：
  - 多个独立Processor-Cache-Memory组
  - 通过Interconnection Network互联
  - 每组有独立的内存地址空间
  - 消息传递替代共享地址空间

**核心概念**：
- **私有地址空间**：处理器间内存不共享
- **消息传递通信**：通过send/receive原语交换数据
- **可扩展性**：松耦合，易于构建大规模系统

---

![[第六章33]]

**图示讲解**：
这张图介绍了松耦合集群的特性与应用场景：
- **Network of independent computers**：
  - Each has private memory and OS
  - Connected using I/O system（如Ethernet/switch, Internet）
- **适用场景**：
  - **Suitable for applications with independent tasks**
  - E.g., Web servers, databases, simulations
- **核心优势**：
  - **High availability**：高可用性
  - **Scalable**：可扩展
  - **Affordable**：成本可控
- **存在问题**：
  - Administration cost（偏好虚拟机）
  - Low interconnect bandwidth（相比SMP处理器/内存带宽）

**核心概念**：
- **独立计算机网络**：每个节点完整独立
- **适合独立任务**：高吞吐量计算的理想选择
- **带宽瓶颈**：集群间互联带宽远低于SMP

---

![[第六章34]]

**图示讲解**：
这张图展示了消息传递架构下求和归约的并行化方法：
- **第一阶段：数据分发**：
  - Sum 64,000 on 64 processors
  - First distribute 1000 numbers to each
  - 每处理器计算局部和
- **第二阶段：归约**：
  - Half the processors send
  - Other half receive and add
  - The quarter send, quarter receive and add
  - 逐步合并直到完成

**核心概念**：
- **数据分发**：初始将数据均匀分配到各处理器
- **树形归约**：消息传递版归约需要显式通信
- **分治策略**：与共享内存类似，但需显式send/receive

---

![[第六章35]]

**图示讲解**：
这张图给出了消息传递归约的代码实现：
- **基础操作**：
  - Given send() and receive() operations
  - 假设send/receive时间与加法相近
- **关键代码**：
  - `synch()`：同步操作（红色高亮）
  - `send(Pn - half, sum)`：发送数据给配对处理器
  - `sum += receive()`：接收并累加数据
- **同步机制**：
  - Send/receive also provide synchronization
  - Assumes send/receive take similar time to addition

**核心概念**：
- **显式通信**：消息传递需要程序员管理数据移动
- **同步语义**：send/receive隐含同步点
- **时间模型**：假设通信时间可预测

---

![[第六章36]]

**图示讲解**：
这张图介绍了网格计算的概念与特点：
- **定义**：Separate computers interconnected by long-haul networks
  - E.g., Internet connections
  - Work units farmed out, results sent back
- **闲置时间利用**：
  - **Can make use of idle time on PCs**
  - E.g., SETI@home, World Community Grid
- **特点**：
  - 志愿者计算资源
  - 极低成本
  - 适合计算密集型、容错性强的任务

**核心概念**：
- **长距离网络互联**：通过互联网连接全球计算机
- **志愿者计算**：利用公共闲置算力
- **分布式任务**：任务分解下发，结果汇总

---

## 九、互连网络

![[第六章37]]

**图示讲解**：
这张图展示了五种常见的互连网络拓扑结构：
- **Bus（总线）**：
  - 所有节点共享单一通信介质
  - 简单但扩展性差
- **Ring（环形）**：
  - 总线首尾相连形成环
  - 更好支持并发传输
- **2D Mesh（二维网格）**：
  - 4×4规整网格结构
  - 每个节点与相邻节点直连
- **N-cube (N=3)（三维立方体）**：
  - 8顶点通过3维互连
  - 适合高维通信模式
- **Fully Connected（全连接）**：
  - 每对节点直接相连
  - 带宽最大但成本最高

**核心概念**：
- **拓扑权衡**：直径、度、成本、可扩展性
- **Mesh流行**：实现简单，扩展性好
- **全连接最优**：任意两点一跳可达

---

![[第六章38]]

**图示讲解**：
这张图详细展示了两种多级互连网络：
- **Crossbar（交叉开关）**：
  - P₀-P₇ 8个输入端口
  - 8×8交叉点矩阵
  - 每个交叉点可独立开关
  - 任意输入可无冲突连接到任意输出
- **Omega Network（Omega网络）**：
  - 同样8输入8输出
  - 三层开关单元（log₂N层）
  - 单元间交叉连接
  - 通过设置开关状态建立路径
- **Switch Box（交换盒）**：
  - Omega网络基础单元
  - 两种状态：直连或交叉

**核心概念**：
- **Crossbar无阻塞**：可同时建立所有输入到输出的连接
- **Omega网络**：递归构建，适合规模扩展
- **开关设置**：根据路由算法动态配置

---

![[第六章39]]

**图示讲解**：
这张图分析了评估互连网络的四个关键指标：
- **Performance（性能）**：
  - Latency per message (unloaded network)：空载网络延迟
  - Throughput：吞吐量
    - Link bandwidth：链路带宽
    - Total network bandwidth：总网络带宽
    - Bisection bandwidth：二分带宽
  - Congestion delays (depending on traffic)：拥塞延迟
- **Cost（成本）**：交换机、链路、端口数
- **Power（功耗）**：能源效率
- **Routability in silicon（硅片可布线性）**：物理实现难度

**核心概念**：
- **延迟vs吞吐量**：延迟关注单次传输，吞吐量关注持续带宽
- **二分带宽**：将网络分成两半后能传输的数据量
- **拥塞影响**：流量负载高时性能急剧下降

---

## 十、多处理器基准测试与性能模型

![[第六章40]]

**图示讲解**：
这张图介绍了主流并行处理器基准测试套件：
- **Linpack**：
  - 矩阵线性代数
  - 经典HPL基准
- **SPECrate**：
  - Job-level parallelism
  - SPEC CPU程序的并行运行
- **SPLASH**：
  - Stanford Parallel Applications for Shared Memory
  - 强扩展测试
  - computational fluid dynamics kernels
- **NAS (NASA Advanced Supercomputing)**：
  - NASA开发的基准套件
- **PARSEC**：
  - Princeton Application Repository for Shared Memory Computers
  - 使用Pthreads和OpenMP
  - 多线程应用基准

**核心概念**：
- **HPL**：Linpack是TOP500排名的基准
- **强扩展测试**：SPLASH等衡量固定问题下的并行效率
- **真实应用**：PARSEC使用实际多线程应用

---

![[第六章41]]

**图示讲解**：
这张图讨论了并行基准测试的演进方向：
- **传统基准**：
  - Fixed code and data sets
  - 固定代码和数据集
- **并行编程演进**：
  - Should algorithms, programming languages, and tools be part of the system?
  - Compare systems, provided they implement a given application
  - E.g., Linpack, Berkeley Design Patterns
- **创新驱动**：
  - Would foster innovation in approaches to parallelism
  - 促进并行方法的创新

**核心概念**：
- **固定vs应用**：传统固定代码 vs 真实应用对比
- **系统完整性**：算法、语言、工具应纳入系统评估
- **创新激励**：基准测试设计影响发展方向

---

![[第六章42]]

**图示讲解**：
这张图介绍了性能建模的基本概念与指标：
- **性能指标**：Achievable GFLOPs/sec（可达GFLOPS）
- **Arithmetic intensity（算术强度）**：
  - FLOPs per byte of memory accessed
  - 每字节内存访问的浮点运算数
  - 使用Berkeley Design Patterns的计算内核测量
- **给定计算机的参数**：
  - **Peak GFLOPS**：来自数据手册的峰值浮点性能
  - **Peak memory bytes/sec**：使用Stream基准测试

**核心概念**：
- **算术强度**：衡量计算密度与内存访问的比值
- **性能上限**：Peak GFLOPS是理论最大值
- **带宽限制**：内存带宽决定算术强度低时的性能

---

![[第六章43]]

**图示讲解**：
这张图是Roofline性能模型的核心——屋顶线图：
- **图表结构**：
  - **横轴**：Arithmetic Intensity (FLOPs/Byte)
  - **纵轴**：Attainable GFLOPs/second
- **两条性能边界**：
  - **蓝色斜线**：Peak memory bandwidth
    - 斜率 = 内存带宽
    - 算术强度低时受内存带宽限制
  - **水平线**：Peak floating-point performance
    - 算术强度高时受计算能力限制
- **内核分类**：
  - **Kernel 1**：Memory Bandwidth limited（内存带宽受限）
  - **Kernel 2**：Computation limited（计算受限）
- **核心公式**：
  - Attainable = Min(Peak_MemBW × AI, Peak_FP)

**核心概念**：
- **性能屋顶**：实际性能不会超过任一边界
- **算术强度决定**：低AI受内存限制，高AI受计算限制
- **优化方向**：根据当前位置选择优化策略

---

![[第六章44]]

**图示讲解**：
这张图用Roofline模型对比了Opteron X2与X4的性能：
- **系统配置对比**：
  - Opteron X2：2核，2× FP performance/core，2.2GHz
  - Opteron X4：4核，2× FP performance/core，2.3GHz
  - Same memory system（相同内存系统）
- **性能曲线**：
  - 黑色实线：X2性能
  - 蓝色虚线：X4性能
  - X4在低AI时与X2相近，高AI时显著优于X2
- **优化建议**：
  - Need high arithmetic intensity
  - Or working set must fit in X4's 2MB L-3 cache

**核心概念**：
- **核数翻倍**：X4有2倍核心，性能非2倍
- **缓存作用**：L3缓存使高AI工作集可在片上处理
- **优化策略**：增加算术强度或优化缓存局部性

---

![[第六章45]]

**图示讲解**：
这张图展示了针对AMD Opteron的多步性能优化：
- **优化维度**：
  - **Optimize FP performance**：平衡加法与乘法
  - **Optimize memory usage**：避免加载停顿、非局部访问
- **优化步骤**：
  1. **Fl. Pt. imbalance**：浮点运算不平衡
  2. **Without ILP or SIMD**：无指令级并行或SIMD
  3. **w/out SW prefetching**：无软件预取
  4. **w/out Memory Affinity**：无内存亲和性
- **性能改进**：
  - 每步优化逐步提升性能
  - Roofline曲线显示各阶段性能天花板

**核心概念**：
- **平衡优化**：FP性能、ILP/SIMD、预取、内存亲和性
- **累积效果**：多步优化叠加显著提升性能
- **诊断定位**：Roofline帮助识别性能瓶颈

---

![[第六章46]]

**图示讲解**：
这张图讨论了优化策略与算术强度的关系：
- **关键洞察**：
  - **Choice of optimization depends on arithmetic intensity of code**
  - **Arithmetic intensity is not always fixed**
- **动态特性**：
  - **May scale with problem size**：随问题规模变化
  - **Caching reduces memory accesses**：缓存减少内存访问
  - **Increases arithmetic intensity**：提高算术强度
- **优化对应**：
  - 低AI：优化内存访问模式
  - 高AI：优化计算吞吐量

**核心概念**：
- **非固定AI**：算术强度可随执行状态变化
- **缓存效应**：缓存命中有助于提高有效算术强度
- **因地制宜**：根据当前瓶颈选择优化重点

---

![[第六章47]]

**图示讲解**：
这张详细对比表比较了Intel i7-960与NVIDIA Tesla GPU：
| 参数 | Core i7-960 | GTX 280 | GTX 480 | 280/i7 | 480/i7 |
|------|------------|---------|---------|--------|--------|
| 处理单元数 | 4 | 30 | 15 | 7.5× | 3.8× |
| 时钟频率 | 3.2GHz | 1.3GHz | 1.4GHz | 0.41× | 0.44× |
| 晶体管数 | 700M | 1400M | 3100M | 2× | 4.4× |
| 内存带宽 | 32 GB/s | 141 GB/s | 177 GB/s | 4.4× | 5.5× |
| 单精度SIMD宽度 | 4 | 8 | 32 | 2× | 8× |
| 峰值单精度FLOPS | 102 GFLOPS | 311-933 GFLOPS | 515-1344 GFLOPS | 3-9× | 5-13× |

**核心概念**：
- **GPU并行优势**：更多处理单元和更高带宽
- **频率权衡**：GPU低频但高并行
- **精度差异**：GPU单精度能力强，双精度较弱

---

![[第六章48]]

**图示讲解**：
这张图展示了Core i7-960与GTX 280的Roofline对比图：
- **Core i7 960 (Nehalem)**：
  - 双精度峰值：51.2 GFLOPS
  - 单精度峰值：102.4 GFLOPS
  - 内存带宽：16.4 GB/s
  - 在AI=4处达到双精度峰值
- **NVIDIA GTX 280**：
  - 双精度峰值：78 GFLOPS
  - 单精度峰值：624 GFLOPS
  - 内存带宽：127 GB/s
  - 在AI=1处达到双精度峰值
- **关键差异**：
  - GTX 280内存带宽是i7的7.7倍
  - i7双精度能力更强

**核心概念**：
- **屋顶位置**：确定各处理器的性能上限
- **斜率差异**：内存带宽差异决定低AI区域性能
- **精度平衡**：不同应用选择不同处理器

---

![[第六章49]]

**图示讲解**：
这张性能对比表展示了14种计算内核在i7-960与GTX 280上的表现：

| Kernel | i7-960 | GTX 280 | 加速比 |
|--------|--------|---------|--------|
| SGEMM | 94 | 364 | 3.9× |
| MC | 0.8 | 1.4 | 1.8× |
| Conv | 1250 | 3500 | 2.8× |
| FFT | 71.4 | 213 | 3.0× |
| SAXPY | 16.8 | 88.8 | 5.3× |
| LBM | 85 | 426 | 5.0× |
| GJK | 67 | 1020 | **15.2×** |
| Bilat | 83 | 475 | **5.7×** |
| SpMV | 4.9 | 9.1 | 1.9× |
| Solv | 103 | 52 | **0.5×** |
| Sort | 250 | 198 | 0.8× |

**核心概念**：
- **GPU优势明显**：高并行内核（GJK、Bilat）GPU显著领先
- **GPU劣势场景**：Solv、Sort等不规则访问应用
- **选择依据**：根据内核特性选择执行平台

---

![[第六章50]]

**图示讲解**：
这张图总结了i7与GPU的性能对比要点：
- **GPU内存带宽优势**：GPU (480) has 4.4× the memory bandwidth
  - Benefits memory bound kernels
- **吞吐量对比**：
  - GPU has 13.1× single precision throughput
  - 2.5× double precision throughput
  - Benefits FP compute bound kernels
- **CPU缓存优势**：
  - CPU cache prevents some kernels from becoming memory bound
  - 某些内核在CPU上不会成为内存受限
- **GPU特殊能力**：
  - GPUs offer scatter-gather：支持非连续内存访问
  - Assists with kernels with strided data
- **GPU局限**：
  - Lack of synchronization and memory consistency support
  - Limits performance for some kernels

**核心概念**：
- **平台互补**：CPU与GPU各有优势场景
- **内存vs计算**：内存带宽和计算吞吐量决定瓶颈
- **功能差异**：同步和一致性支持影响应用范围

---

## 十一、多线程DGEMM

![[第六章51]]

**图示讲解**：
这张图展示了使用OpenMP并行化DGEMM的代码：
- **OpenMP并行化**：
  - `#pragma omp parallel for`指令
  - 自动并行化循环
- **三层嵌套循环**：
  - 外层循环遍历C矩阵块
  - 内层调用`do_block()`执行矩阵乘法
  - 自动分配迭代到各线程
- **块矩阵乘法**：
  - 分块提高缓存局部性
  - 每线程处理矩阵的一个子块

**核心概念**：
- **OpenMP简化**：编译器指令自动并行化
- **数据局部性**：分块策略优化缓存重用
- **隐式同步**：OpenMP运行时处理同步

---

![[第六章52]]

**图示讲解**：
这张加速比曲线图展示了多线程DGEMM的性能：
- **横轴**：Threads（线程数1-16）
- **纵轴**：Speedup relative to 1 core（相对单核加速比）
- **曲线对比**：
  - **960×960**：近乎线性加速，16线程达13.5×
  - **480×480**：接近线性加速，16线程达13×
  - **160×160**：8线程后趋于平缓，约4.7×
  - **32×32**：基本无加速，甚至下降
- **关键观察**：
  - 大矩阵多线程效率高
  - 小矩阵受同步开销影响大

**核心概念**：
- **Amdahl定律**：小部分串行代码限制加速比
- **规模效应**：大矩阵并行效率更高
- **线程开销**：小问题多线程开销超过收益

---

![[第六章53]]

**图示讲解**：
这张柱状图更直观地展示了各配置的绝对性能：
- **纵轴**：GFLOPS（实际计算性能）
- **配置对比**：
  - **960×960**：16线程达174 GFLOPS
  - **480×480**：16线程达169 GFLOPS
  - **160×160**：16线程约60 GFLOPS
  - **32×32**：基本保持在10-15 GFLOPS
- **增长趋势**：
  - 大矩阵随线程数增加接近峰值
  - 小矩阵增长有限

**核心概念**：
- **峰值对比**：大矩阵配置接近GPU峰值
- **并行效率**：大矩阵配置效率>90%
- **小问题局限**：32×32规模不适合并行化

---

## 十二、Fallacies and Pitfalls

![[第六章54]]

**图示讲解**：
这张图指出了关于并行性能的两个常见谬误：
- **谬误1**：Amdahl's Law doesn't apply to parallel computers
  - SINCE we can achieve linear speedup
  - BUT only on applications with weak scaling
- **谬误2**：Peak performance tracks observed performance
  - Marketers like this approach!
  - But compare Xeon with others in example
  - Need to be aware of bottlenecks
  - 峰值性能≠实际性能

**核心概念**：
- **线性加速特例**：弱扩展下才可能接近线性加速
- **峰值陷阱**：市场营销常用峰值，但实际差异大
- **瓶颈意识**：需关注内存带宽、互连带宽等瓶颈

---

![[第六章55]]

**图示讲解**：
这张图指出了一个常见的并行编程陷阱：
- **陷阱**：Not developing the software to take account of a multiprocessor architecture
- **示例**：Using a single lock for a shared composite resource
- **后果**：
  - **Serializes accesses**：串行化访问
  - Even if they could be done in parallel
  - 即使可并行也被迫串行
- **解决**：
  - **Use finer-granularity locking**
  - 细粒度锁保护资源不同部分

**核心概念**：
- **粗粒度锁**：单一锁限制并发
- **细粒度优化**：分离锁提高并行度
- **设计前置**：软件架构需考虑并行特性

---

## 十三、Concluding Remarks

![[第六章56]]

**图示讲解**：
这张图总结了第六章的核心结论：
- **Goal**：higher performance by using multiple processors
  - 通过多处理器获得更高性能
- **Difficulties（挑战）**：
  - Developing parallel software：开发并行软件
  - Devising appropriate architectures：设计合适的架构
- **发展趋势**：
  - SaaS importance is growing
  - Clusters are a good match
  - 集群与SaaS趋势契合
- **驱动力**：
  - Performance per dollar
  - Performance per Joule
  - 性能和成本、能效共同驱动

**核心概念**：
- **并行价值**：多处理器是性能提升的关键途径
- **双重挑战**：软件和硬件都需要适配并行
- **实用导向**：成本和能效是重要考量

---

![[第六章57]]

**图示讲解**：
这张图展示了并行加速比的历史演进与未来趋势：
- **核心观点**：SIMD and vector operations match multimedia applications and are easy to program
- **加速比演进图**：
  - **MIMD**：稳定增长，2023年约100倍
  - **MIMD×SIMD (64b)**：最高，2023年接近1000倍
  - **MIMD×SIMD (32b)**：次高，约500倍
  - **SIMD (32b/64b)**：增长平缓
- **关键趋势**：
  - MIMD与SIMD结合获得最高性能
  - 向量化是性能提升重要手段
  - 软硬件协同设计是关键

**核心概念**：
- **MIMD×SIMD融合**：结合任务级和指令级并行
- **向量指令价值**：匹配多媒体应用，易于编程
- **演进路线**：从单一技术到融合架构

---

## 附录：GPU术语速查

| CUDA术语 | 传统并行计算对应 | 含义 |
|----------|----------------|------|
| Grid | 向量化循环 | GPU上执行的完整程序 |
| Thread Block | 循环体 | SIMD处理器上执行的子任务 |
| Warp | 向量指令序列 | 32元素的SIMD线程 |
| SM (Streaming Multiprocessor) | 向量处理器 | 执行Warp的硬件单元 |
| PTX Instruction | 向量指令 | 单条SIMD指令 |
| CUDA Thread | 循环迭代 | SIMD通道执行的单个元素 |
