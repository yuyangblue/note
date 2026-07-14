![[Pasted image 20260714194828.png]]# **前**   **言**

Xilinx 7系列FPGA包括Spartan-7、Artix-7、Kintex-7、Virtex-7。它们基于ASMBL（AdvancedSilicon Modular Block）架构，ASMBL架构特点是资源按列排布，同一列的资源是相同的。

Xilinx FPGA由CLB（Configurable Logic Block，可编程逻辑单元）、BRAM（Block RAM，块RAM）、DSP48E1（专用数字处理单元）、可编程布线资源、可编程IO资源等部分组成，其中，CLB是实现逻辑功能的基础。

![](file:///C:\Users\29469\AppData\Local\Temp\ksohtml10544\wps1.jpg) 

图  ASMBL架构

下图是FPGA的内部结构图（XC7A100），如图下图所示，该FPGA分为8个区域（8个Clock Region）

![](file:///C:\Users\29469\AppData\Local\Temp\ksohtml10544\wps2.jpg) 

![](file:///C:\Users\29469\AppData\Local\Temp\ksohtml10544\wps3.jpg) 

![](file:///C:\Users\29469\AppData\Local\Temp\ksohtml10544\wps4.jpg) 

X0Y1区域放大后的图如图所示，图中最左侧蓝色部分为IO接口，面积最大灰色部分为slice（CLB），粉色部分为BRAM资源，绿色部分为DSP资源（DSP48E1）。

![](file:///C:\Users\29469\AppData\Local\Temp\ksohtml10544\wps5.jpg)