# MNIST手写数字识别详解

> **一句话总结**：用PyTorch训练一个神经网络，让它学会"看"手写数字图片，判断是0-9中的哪个数字。

---

## 一、这个代码在干什么？有什么用？

### 1.1 实际应用场景

| 应用领域 | 怎么用 |
|---------|-------|
| **银行支票识别** | 自动读取支票上的手写金额 |
| **邮政编码识别** | 自动分拣信件到不同地区 |
| **车牌识别** | 识别车牌上的数字和字母 |
| **表单数字化** | 将手写表单转为电子数据 |

**MNIST是什么**：一个包含6万张手写数字图片的训练集 + 1万张测试集，每张图片是28×28像素的灰度图。

![MNIST数据集示例](https://s.coze.cn/image/xVhVn6VwHic/)

### 1.2 核心工作流程

```
图片输入 → 神经网络处理 → 输出概率 → 预测数字
  28×28    →    黑盒子    →  10个数  →  最大概率
```

---

## 二、模块1：导入库

```python
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter
import matplotlib.pyplot as plt
import numpy as np
```

### 各个库的作用

| 库 | 干什么用 | 打个比方 |
|---|---------|---------|
| `torch` | PyTorch核心，张量运算 | 算盘（计算工具） |
| `torch.nn` | 神经网络模块 | 盖房子的砖头和水泥 |
| `torch.optim` | 优化器，更新参数 | 指导学习的老师 |
| `torchvision` | 图像处理工具 | 图片加工厂 |
| `DataLoader` | 批量加载数据 | 传送带，一批批喂给模型 |
| `SummaryWriter` | TensorBoard可视化 | 监控训练过程的仪表盘 |

---

## 三、模块2：设置超参数

```python
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
INPUT_SIZE = 784     # 28x28 像素展平后的长度
HIDDEN_SIZE = 500    # 隐藏层神经元数
NUM_CLASSES = 10     # 输出为 0-9 十个数字
NUM_EPOCHS = 10      # 训练轮数
BATCH_SIZE = 100     # 每次喂给模型多少张图片
LEARNING_RATE = 0.001 # 初始学习率
```

### 参数详解

| 参数 | 值 | 为什么是这个值？ |
|-----|---|----------------|
| `INPUT_SIZE` | 784 | 28×28图片，展平成1维向量 |
| `HIDDEN_SIZE` | 500 | 模型"脑容量"，越大越聪明但越慢 |
| `NUM_CLASSES` | 10 | 0-9共10个数字 |
| `NUM_EPOCHS` | 10 | 看数据集10遍，多了会过拟合 |
| `BATCH_SIZE` | 100 | 一次喂100张，平衡速度和稳定性 |
| `LEARNING_RATE` | 0.001 | 步子大小，太大震荡，太小收敛慢 |

**device是什么**：自动检测有没有GPU，有就用GPU加速，没有就用CPU。

---

## 四、模块3：数据加载与预处理

### 4.1 归一化：为什么要做？

```python
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,)) 
])
```

**归一化的作用**：把像素值从[0, 255]缩放到接近0的范围。

| 不归一化 | 归一化后 |
|---------|---------|
| 损失函数像"狭长深谷" | 损失函数像"圆碗" |
| 梯度下降会震荡 | 梯度直指中心 |
| 收敛慢 | 收敛快 |

**0.1307和0.3081是什么**：MNIST数据集的均值和标准差，是统计出来的固定值。

$$x_{new} = \frac{x - 0.1307}{0.3081}$$

### 4.2 数据加载

```python
train_dataset = MNIST(root='./data', train=True, transform=transform, download=True)
test_dataset = MNIST(root='./data', train=False, transform=transform)

train_loader = DataLoader(dataset=train_dataset, batch_size=BATCH_SIZE, shuffle=True)
test_loader = DataLoader(dataset=test_dataset, batch_size=BATCH_SIZE, shuffle=False)
```

**DataLoader的作用**：

| 参数 | 作用 |
|-----|-----|
| `shuffle=True` | 训练集打乱顺序，防止模型记住顺序 |
| `shuffle=False` | 测试集不打乱，方便评估 |

**打个比方**：DataLoader就像传送带，每次抓100张图片（一个batch）喂给模型。

---

## 五、模块4：搭建神经网络

### 5.1 网络结构

```python
class NeuralNet(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(NeuralNet, self).__init__()
        self.fc_stack = nn.Sequential(
            nn.Linear(input_size, hidden_size), # 784 → 500
            nn.ReLU(),                          # 激活函数
            nn.Linear(hidden_size, num_classes) # 500 → 10
        )
    
    def forward(self, x):
        x = x.view(-1, 28*28)  # 把28×28压扁成784
        return self.fc_stack(x)
```

### 5.2 结构详解

**第一层（输入层→隐藏层）**：
- 输入：784个数字（28×28图片压扁）
- 输出：500个数字
- 数学操作：$y = Wx + b$

**激活函数ReLU**：

![ReLU函数](https://s.coze.cn/image/MOqCaW7GB6o/)

$$ReLU(x) = \max(0, x)$$

| 输入 | 输出 |
|-----|-----|
| 正数 | 保持不变 |
| 负数 | 变成0 |

**为什么要用ReLU**：
1. 计算快（就是比大小）
2. 解决梯度消失问题
3. 让网络能学习非线性关系

**第二层（隐藏层→输出层）**：
- 输入：500个数字
- 输出：10个数字（每个数字的概率）

### 5.3 forward函数：数据如何流动

```python
def forward(self, x):
    x = x.view(-1, 28*28)  # 压扁
    return self.fc_stack(x)
```

**view的作用**：把28×28的2维图片压扁成784的1维向量。

**例子**：
```python
# 输入形状：(batch_size, 1, 28, 28)
# view后：(batch_size, 784)
```

---

## 六、模块5：损失函数、优化器、学习率调度器

### 6.1 损失函数

```python
criterion = nn.CrossEntropyLoss()
```

**CrossEntropyLoss是什么**：衡量预测值和真实标签的差距。

$$Loss = -\sum y_{true} \log(y_{pred})$$

**直观理解**：
- 预测对且自信 → loss小
- 预测错或不确定 → loss大

### 6.2 优化器

```python
optimizer = optim.Adam(model.parameters(), lr=LEARNING_RATE)
```

**Adam优化器**：一种自适应学习率优化算法。

![梯度下降](https://s.coze.cn/image/KlSeJ4Gq7E8/)

| 特点 | 说明 |
|-----|-----|
| 自适应学习率 | 每个参数有自己的学习率 |
| 动量机制 | 记住之前的方向，减少震荡 |
| 收敛快 | 比普通SGD快 |

### 6.3 学习率调度器

```python
scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=3, gamma=0.7)
```

**作用**：每3个epoch，学习率变成原来的70%。

| Epoch | 学习率 |
|-------|-------|
| 1-3 | 0.001 |
| 4-6 | 0.0007 |
| 7-9 | 0.00049 |
| 10 | 0.000343 |

**为什么要衰减**：
- 开始时：大步子快速接近最优解
- 后期：小步子精细调整，避免震荡

---

## 七、模块6：训练与验证循环

### 7.1 训练流程

```python
for epoch in range(NUM_EPOCHS):
    model.train()  # 训练模式
    for images, labels in train_loader:
        # 1. 前向传播
        outputs = model(images)
        loss = criterion(outputs, labels)
        
        # 2. 反向传播
        optimizer.zero_grad()  # 清空旧梯度
        loss.backward()        # 计算梯度
        optimizer.step()       # 更新参数
```

### 7.2 四步训练法

| 步骤 | 代码 | 做什么 |
|-----|------|-------|
| 1 | `outputs = model(images)` | 让模型预测 |
| 2 | `loss = criterion(outputs, labels)` | 计算错得有多离谱 |
| 3 | `loss.backward()` | 算出每层该怎么改 |
| 4 | `optimizer.step()` | 真正更新参数 |

**optimizer.zero_grad()为什么重要**：
- PyTorch会累加梯度
- 不清零的话，当前batch的梯度会加上上一个batch的梯度
- 结果就是参数更新方向错误

### 7.3 验证流程

```python
model.eval()  # 评估模式
with torch.no_grad():  # 不计算梯度
    correct = 0
    total = 0
    for images, labels in test_loader:
        outputs = model(images)
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()
    
    accuracy = 100 * correct / total
```

**model.eval()的作用**：
- 关闭Dropout（如果有的话）
- 使用训练好的BatchNorm参数

**torch.no_grad()的作用**：
- 不计算梯度，节省内存
- 测试时不需要反向传播

**torch.max(outputs, 1)的意思**：
- outputs是一个(batch_size, 10)的矩阵
- 每行10个数字，代表预测是0-9的概率
- torch.max找出每行最大的那个索引

---

## 八、模块7：TensorBoard可视化

### 8.1 记录内容

```python
writer = SummaryWriter('runs/mnist_final_experiment')
writer.add_scalar('Loss/Batch_Train', loss.item(), global_step)
writer.add_scalar('Accuracy/Test', accuracy, epoch)
writer.add_graph(model, dummy_input)
```

### 8.2 如何查看TensorBoard

**步骤**：

```bash
# 在终端运行
tensorboard --logdir=runs
```

然后在浏览器打开 `http://localhost:6006`

**能看到什么**：
- Loss随训练轮次下降的曲线
- 准确率随训练轮次上升的曲线
- 学习率的变化
- 模型结构图

---

## 九、训练结果分析

```
Epoch [1/10], Avg Loss: 0.2177, Test Accuracy: 96.81%
Epoch [2/10], Avg Loss: 0.0857, Test Accuracy: 97.43%
Epoch [3/10], Avg Loss: 0.0567, Test Accuracy: 97.76%
...
Epoch [10/10], Avg Loss: 0.0028, Test Accuracy: 98.28%
```

### 9.1 结果解读

| 指标 | 变化趋势 | 说明 |
|-----|---------|-----|
| Avg Loss | 0.2177 → 0.0028 | 下降了99%，模型在学习 |
| Test Accuracy | 96.81% → 98.28% | 准确率提升1.5个百分点 |
| Learning Rate | 0.001 → 0.000343 | 按计划衰减 |

### 9.2 为什么Loss几乎为0但准确率不是100%

**原因**：
1. 有些手写数字确实难以辨认（人也不一定能认对）
2. 模型对某些样本"很自信但错了"
3. 数据集本身的噪声和歧义

---

## 十、模型保存与加载

### 10.1 保存模型

```python
torch.save(model.state_dict(), 'mnist_model.pth')
```

**state_dict是什么**：模型所有参数的字典，包含每层的权重和偏置。

### 10.2 加载模型

```python
model.load_state_dict(torch.load('mnist_model.pth'))
model.eval()  # 切换到评估模式
```

---

## 十一、预测可视化

```python
def visualize_predictions():
    model.load_state_dict(torch.load('mnist_model.pth'))
    model.eval()
    
    images, labels = next(iter(DataLoader(test_dataset, batch_size=8, shuffle=True)))
    
    with torch.no_grad():
        outputs = model(images.to(device))
        _, preds = torch.max(outputs, 1)
    
    for i in range(8):
        color = 'green' if preds[i] == labels[i] else 'red'
        plt.title(f"P: {preds[i]} | A: {labels[i]}", color=color)
```

**输出说明**：
- P: Prediction（预测值）
- A: Actual（真实值）
- 绿色 = 预测对
- 红色 = 预测错

---

## 十二、常见问题

### Q1: 为什么准确率卡在98%上不去？

**A**: 全连接网络（MLP）的能力有限。要想更高，可以：
1. 用卷积神经网络（CNN）
2. 增加网络深度
3. 使用数据增强
4. 换更强的模型（如ResNet）

### Q2: 为什么要用view压扁图片？

**A**: 全连接层只能处理1维向量。如果想保留图片的2维结构，要用卷积层。

### Q3: GPU和CPU训练速度差多少？

**A**: 
- MNIST这种小数据集：差别不大
- 大模型大数据集：GPU快10-100倍

### Q4: 为什么测试时shuffle=False？

**A**: 测试集的顺序不影响评估结果，打乱反而可能让结果难以复现。

---

## 十三、代码速查表

### 完整流程

```python
# 1. 准备数据
transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize(...)])
train_loader = DataLoader(MNIST(..., train=True), batch_size=100, shuffle=True)

# 2. 搭建模型
class NeuralNet(nn.Module):
    def __init__(self): ...
    def forward(self, x): ...

# 3. 定义损失函数和优化器
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# 4. 训练循环
for epoch in range(10):
    for images, labels in train_loader:
        outputs = model(images)
        loss = criterion(outputs, labels)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

# 5. 测试评估
model.eval()
with torch.no_grad():
    # 计算准确率...

# 6. 保存模型
torch.save(model.state_dict(), 'model.pth')
```

---

## 十四、总结

| 模块 | 核心功能 | 关键点 |
|-----|---------|-------|
| 数据加载 | 加载并预处理图片 | 归一化很重要 |
| 模型定义 | 搭建神经网络 | view压扁 + ReLU激活 |
| 训练循环 | 更新模型参数 | 四步：前向→算loss→反向→更新 |
| 验证循环 | 评估模型效果 | no_grad节省内存 |
| 可视化 | 监控训练过程 | TensorBoard很直观 |

**这个代码的核心价值**：
- 是深度学习入门的标准案例
- 理解了这个，其他图像分类任务原理一样
- 可以扩展到更复杂的数据集和模型
