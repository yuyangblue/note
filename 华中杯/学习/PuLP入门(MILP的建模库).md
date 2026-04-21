PuPL是python中用于**混合整数线性规划（MILP**的建模库，适合处理带整数/二进制约束的优化问题
## 核心使用步骤 **创建问题示例

1. **创建问题实例**

    ```python
    prob = pulp.LpProblem("Production_Optimization", pulp.LpMaximize)
    ```

2. **定义决策变量**
    
    ```python
    x1 = pulp.LpVariable('x1', lowBound=0, cat='Integer')  # 整数变量
    x2 = pulp.LpVariable('x2', lowBound=0)                # 连续变量
    ```
    
3. **设置目标函数**

    ```python
    prob += 40*x1 + 30*x2, "Total_Profit"
    ```
    
4. **添加约束条件**
    
    ```python
    prob += 2*x1 + 4*x2 <= 200, "Resource1"
    prob += 3*x1 + 2*x2 <= 180, "Resource2"
    ```

约束条件和目标函数的顺序没有严格要求

4. **求解与输出**
    
    ```python
    prob.solve()
    print("Status:", pulp.LpStatus[prob.status])
    for v in prob.variables():
        print(v.name, "=", v.varValue)
    print("Optimal Profit =", pulp.value(prob.objective))
    ```