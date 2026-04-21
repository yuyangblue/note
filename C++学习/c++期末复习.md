### 0.小tip

1. %运算的符号只取决于第一个运算数的符号。
2. & > ^ > |（与>异或>或）
3. 逻辑运算符：先！然后<>,然后！=，然后&&后||
	例题：设变量int m,n,a,b的值均为0，则执行表达式(m=a>=b)||(n=a>=b)后，
	m、n的值分为1，0
4. 短路原则
5. int(z), (int)z, `static_cast<int> z` 完全等价，用于类型转换
6. 成员初始化顺序与它们在类定义中的出现顺序一致，而不是在初始化列表中出现的顺序！
7. 类的静态数据成员必须在类内声明，类外定义和初始化，用(::)来指明所属的类。静态成员函数只能引用属于该类的静态数据成员或静态成员函数
8. y=`*`px++ 相当于 y=`*`(px++)(`*`和++优先级相同，自右向左运算)，但是y的结果是`*`px，因为后缀++的含义是返回当前值并且自++
9. 形参是数组名时，编译系统将其转换为对应的指针类型
### 1.还没学
 C++ 文件流（fstream）中关于随机文件访问和 `seekg` 的相关知识点。

### 2.指针的注意事项
1. `MyClass *p[2]`：定义长度为 2 的**指针数组**（仅存储对象地址，不创建新对象），不会调用构造函数，无输出。
2. `*p++ = *str2++`

- 先执行 `*p = *str2`：将 `str2` 的第一个字符（'l'）复制到 `p` 当前位置（覆盖了原来的 `'\0'`）
- **然后** `p++` 和 `str2++`：指针后移
  因为 `*p++` 是**后缀 ++**，它的运算顺序是：
 
    1. 使用 p 的当前值进行解引用：`*p`
    2. 执行赋值：`*p = *str2`
    3. 然后 `p++`（后自增）
  如果是 `*++p = *str2++` 才会先移动指针再赋值，但这里不是。

### 3.vector要先规定大小在访问
如果可能，尽量提前预估 `vector` 的大小，使用 `reserve` 函数预先分配足够的内存，以减少内存重新分配的次数
```cpp
std::vector<int> vec; 
vec.reserve(100); // 预先分配100个元素的空间 
vec.resize(50); // 调整大小为50，此时不会重新分配内存
```
在使用矩阵之前，如果矩阵没有规定大小而越界访问会报错


### 4.神奇的char
1. `char`**可以存储整数**，它本身就是 1 字节的整数类型，只是默认常用来表示字符（基于 ASCII 码映射）。
2. 存储整数时要注意`char`的取值范围，超出范围会溢出，建议根据需求选择`signed char`或`unsigned char`。
3. 输出`char`时，默认会解析为 ASCII 字符，如需输出整数值，要强制转换为`int`。

### 5.初始化
基本数据类型的变量未被初始化，它的值由定义的位置决定。定义在函数之外的，默认初值为0，定义在函数之内的，则不被初始化！

###  6.volatile
volatile限定词：变量可能非明确说明的方式改变。一般情况下，编译程序认为没有出现在赋值语句左侧的变量不会改变。 volatile型的变量例外，因此编译系统会自动优化。
例如，变量保存 实时时钟值。

```cpp
#include <iostream>
#include <thread>
#include <unistd.h>

// 假设这是一个代表实时时钟的变量
volatile int realTimeClockValue = 0;

// 模拟实时时钟更新的函数（这里简单地递增）
void updateRealTimeClock() {
    for (int i = 0; i < 5; ++i) {
        realTimeClockValue++;
        sleep(1); // 模拟每秒更新一次
    }
}

int main() {
    // 在另一个线程中启动实时时钟更新
    std::thread clockThread(updateRealTimeClock);

    // 读取实时时钟的值
    for (int i = 0; i < 5; ++i) {
        std::cout << "实时时钟值: " << realTimeClockValue << std::endl;
        sleep(1); // 每秒读取一次
    }

    // 等待时钟更新线程结束
    clockThread.join();

    return 0;
}
```


### 7.左值与右值
#### 1. 定义与概念

**左值（lvalue）**：

- **概念**：“lvalue” 中的 “l” 最初代表 “left”，意味着它通常出现在赋值语句的左边（但并非绝对）。左值是指那些具有持久内存地址的表达式，也就是可以取地址的表达式。它可以是变量、函数调用返回的左值引用，或者是通过解引用指针得到的结果等。
**右值（rvalue）**：

- **概念**：“rvalue” 中的 “r” 代表 “right”，通常出现在赋值语句的右边。右值是临时性的，它们没有持久的内存地址。右值包括字面常量（如 `10`、`"hello"`）、函数返回的非引用类型、算术表达式的结果等
#### 2. 左值和右值在代码中的特性
- **可寻址性**：
- **左值**：可以使用 `&` 运算符获取其地址。
- **右值**：通常不能取地址（C++ 17 引入了对某些右值的地址获取方式，但这是特殊情况）。例如：

- **持久性**：
- **左值**：具有持久性，在其作用域内保持其值，除非被显式修改。
- **右值**：是临时的，生命周期只在表达式求值期间存在。一旦包含右值的表达式求值完成，右值所代表的临时对象就会被销毁。例如：
####  3. 左值引用和右值引用

- **左值引用（lvalue reference）**：
 **定义**：左值引用是对左值的别名，通过 `&` 符号声明。左值引用必须绑定到左值。
 
```cpp
int value = 42;
int& ref = value; // 'ref' 是对 'value' 这个左值的左值引用
ref = 43; // 通过引用修改 'value' 的值
```

- **右值引用（rvalue reference）**：
    **定义**：右值引用是 C++ 11 引入的新特性，通过 `&&` 符号声明，它允许绑定到右值。右值引用主要用于实现移动语义和完美转发。
    **示例**：

```cpp
int&& rref = 10; // 'rref' 是对右值 '10' 的右值引用
```

**右值的应用场景**：

- **临时对象处理**：在实现移动语义时，右值引用可以避免不必要的对象拷贝，提高性能。
```cpp
// 移动构造函数
    MyString(MyString&& other) noexcept : data(other.data) {
        other.data = nullptr;
    }
    MyString getString() {
    return MyString("Hello");
}
	int main() {
    MyString s = getString();
    // 使用移动构造函数，避免了对临时 MyString 对象的拷贝
    return 0;
}

```
- **函数返回值优化**：编译器可以利用右值的临时性进行返回值优化（RVO），减少不必要的对象拷贝。
```cpp
MyString createString() {
    MyString temp("World");
    return temp;
}
MyString result = createString();
// 编译器可能会直接将临时的 'temp' 对象构造为'result'，避免额外的拷贝
```

### 8.register
**`register` 关键字的基本概念**

- 在 C 和 C++ 中，`register` 关键字用于提示编译器将变量存储在寄存器中，而不是内存中。寄存器是 CPU 内部的高速存储单元，访问寄存器中的数据比访问内存中的数据要快得多。通过将频繁使用的变量声明为 `register`，可以潜在地提高程序的执行效率，因为对寄存器变量的访问速度更快，减少了 CPU 从内存中读取数据的时间开销。

### 9.extern关键字和static关键字

1. **`extern`关键字**

- **作用**：`extern`关键字用于声明一个变量或函数，表明这个变量或函数在其他地方已经定义。它的主要目的是让编译器知道该对象具有外部链接，即可以在多个源文件之间共享访问。
- **对变量的要求**：被 `extern` 说明的对象必须是静态生存期的变量。静态生存期意味着变量在程序启动时创建，在程序结束时销毁。全局变量就是典型的具有静态生存期的变量。这是因为只有静态生存期的变量在整个程序执行期间都存在，才能保证在不同源文件中通过 `extern` 访问时的一致性。

2. **`static`关键字**

- **静态全局变量**：
  **特点**：当一个全局变量（文件作用域内）被声明为 `static` 时，它具有内部链接。这意味着该变量只能在定义它的源文件内被访问，其他源文件无法访问。
```cpp
// file1.cpp
static int staticGlobal = 5;
void printStaticGlobal() {
    std::cout << "Static global in file1: " << staticGlobal << std::endl;
}
```

```cpp
// file2.cpp
// 这里不能访问file1中的staticGlobal变量
// 即使尝试声明extern int staticGlobal;也不行
```

- **静态局部变量**：
- **特点**：静态局部变量在函数内部声明，但是它具有静态生存期。与普通局部变量不同，普通局部变量在函数调用时创建，函数结束时销毁；而静态局部变量在程序第一次执行到其声明处时创建，并且在程序的整个执行期间都存在，不过其作用域仍然局限于声明它的函数内部。

3. **全局变量**：全局变量默认具有 `extern` 类别，这意味着它们具有外部链接，可以在多个源文件中访问。

所以总结来说，静态全局变量和静态局部变量都不能被外部访问，全局变量可以被外部访问，而普通局部变量不能被外部访问

### 10.thread_local和mutable

**`thread_local`关键字**

- **线程存储生存期**：`thread_local`关键字用于声明变量具有线程存储生存期。这意味着每个线程都有该变量的独立副本。在多线程编程中，不同线程对 `thread_local` 变量的修改不会相互影响，每个线程都可以独立地读写自己的那份变量副本。

**`mutable`关键字**

- **适用范围与限制**：`mutable` 关键字只能用于类的数据成员，并且不能与 `const` 或者 `static` 同时使用，也不能用来修饰引用变量。
- **突破 `const` 限制**：在类中，`const` 成员函数通常不能修改类的数据成员，因为 `const` 成员函数承诺不会改变对象的状态。但是，当某个数据成员被 `mutable` 修饰时，即使在 `const` 成员函数中也可以修改它。

### 11.const和constexpr

**`constexpr` 变量的常量属性**

- 当一个变量被 `constexpr` 修饰时，它确实暗含 `const` 属性，这意味着一旦初始化后，其值就不能再改变。这是因为 `constexpr` 的主要目的之一是用于表示常量表达式，在编译时就确定其值。

**与 `const` 的细微区别**

- **初始化时机**：`const` 变量可以在运行时初始化，只要在其作用域内尽早初始化即可。而 `constexpr` 变量要求其初始化表达式必须是常量表达式，即在编译时就能确定值。
 ```cpp
int getValue() {
    return 20;
}
const int a = getValue(); // 合法，const变量可以在运行时初始化
// constexpr int b = getValue(); // 不合法，constexpr变量要求编译时确定值
```
- **使用场景**：`constexpr` 变量更侧重于用于需要在编译期就确定值的场景，比如作为数组的维度、模板参数等。而 `const` 变量则更通用，用于表示一般意义上的不可变值，运行时初始化的情况也很常见。例如
```cpp
constexpr int size = 5;
int arr[size]; // 合法，constexpr变量可用于确定数组维度
const int anotherSize = 10;
// int anotherArr[anotherSize]; // C++ 标准中，普通const变量不能直接用于确定数组维度（C99 及以后的C标准支持这种做法）
```

### 12.指针、常量和类型别名

如果某个类型别名指代的是复合类型或常量，那么把它用到声明语句里就会产生意想不到的后果。

例如下面的声明语句用到了类型`pstring`，它实际上是类型`char＊`的别名：

```cpp
typedef char * pstring;
const pstring cstr = 0;
const pstring *ps;
```

上述两条声明语句的基本数据类型都是`const pstring`，和过去一样，`const`是对给定类型的修饰。
`pstring`实际上是指向char的指针，因此，`const pstring`就是指向`char`的常量指针，而非指向常量字符的指针。

### 13.构造组合类对象时的初始化次序

- 当一个类的构造函数被调用时，首先会处理构造函数初始化列表。在这个阶段，类的成员（包括基本类型成员和对象成员）会按照它们在类体中定义的顺序进行初始化。
- 对于对象成员，其构造函数的调用顺序也是按照它们在类中声明的顺序，先声明的对象成员先构造。如果某个对象成员在初始化列表中没有显式初始化，那么它会调用默认构造函数（即没有参数的构造函数）进行初始化。
- 完成初始化列表的处理后，才会执行构造函数的函数体。
 ```cpp
#include <iostream>

class SubClass {
public:
    SubClass() {
        std::cout << "SubClass default constructor called" << std::endl;
    }

    SubClass(int value) : data(value) {
        std::cout << "SubClass constructor with int called" << std::endl;
    }

    ~SubClass() {
        std::cout << "SubClass destructor called" << std::endl;
    }

private:
    int data;
};

class MainClass {
    SubClass sub1;
    int num;
    SubClass sub2;

public:
    MainClass() : num(10), sub2(20) {
        std::cout << "MainClass constructor body" << std::endl;
    }
};

int main() {
    MainClass obj;
    return 0;
}
```
- 所以初始化顺序为：
    - 首先调用 `sub1` 的默认构造函数，输出 `SubClass default constructor called`。
    - 接着初始化 `num`，将其赋值为 `10`（虽然这里基本类型的初始化在输出上没有体现额外信息）。
    - 然后调用 `sub2` 的带参数构造函数，输出 `SubClass constructor with int called`。
- 最后执行构造函数的函数体，输出 `MainClass constructor body`。

### 14.**析构函数调用顺序**

- 析构函数的调用顺序与构造函数的调用顺序相反。当一个对象被销毁时，首先执行该对象构造函数函数体中最后一条语句之后的部分，然后按照对象成员在类中声明的相反顺序调用对象成员的析构函数，最后调用类自身的析构函数。
- 如果涉及继承，析构顺序会更加复杂。当一个派生类对象被销毁时，首先调用派生类的析构函数，然后按照继承层次从下往上（即先调用直接基类的析构函数，再调用间接基类的析构函数）调用基类的析构函数。

### 15.在面向对象编程和设计中，常见的关系

#### 1. 关联（Association）

- **定义**：关联表示两个或多个类之间存在某种语义上的连接，它描述了对象之间的结构关系。
- **特点**：关联可以是单向的或双向的。例如，“学生” 和 “课程” 之间存在关联，学生可以选修课程，课程也可以被学生选修，这是双向关联；若只考虑学生选修课程，不考虑课程反过来对学生的关联，就是单向关联。
- **重数**：通过重数来描述类之间对象数量的对应关系。如 “1” 表示一对一，“1..” 表示一对多，“0..1” 表示零对一或一对一，“0..” 表示零对多或一对多。例如，一个班级有多个学生（一对多），一个人可能有零个或一个护照（零对一或一对一）。
- **重数 A**：表示类 B 的每个对象与类 A 的对象发生作用的数量。
- **重数 B**：决定了类 A 的每个对象与类 B 的对象发生作用的数量。
 ![[Pasted image 20260102125446.png]]

#### 2. 聚合（Aggregation）

- **定义**：聚合是一种特殊的关联关系，它表示整体与部分的关系，其中部分可以脱离整体而独立存在。
- **特点**：整体和部分之间具有 “拥有” 关系，但部分的生命周期可以独立于整体。例如，“图书馆” 和 “书籍”，图书馆拥有书籍，但书籍可以从一个图书馆转移到另一个图书馆，甚至在没有图书馆的情况下（比如私人藏书）也能存在。
- **表示**：在 UML 图中，聚合关系用空心菱形表示，菱形指向整体。
- 
 ![[Pasted image 20260102125514.png]]

#### 3. 组合（Composition）
 
- **定义**：组合也是整体与部分的关系，但部分不能脱离整体而存在，整体的生命周期决定部分的生命周期。
- **特点**：与聚合相比，组合的关系更为紧密。例如，“汽车” 和 “发动机”，发动机是汽车的一部分，当汽车报废时，发动机通常也随之报废，发动机不能独立于汽车而存在。
- **表示**：在 UML 图中，组合关系用实心菱形表示，菱形指向整体。

#### 4. 继承（Inheritance）

- **定义**：继承是指一个类（子类）可以继承另一个类（父类）的属性和行为。子类可以复用父类的代码，并可以在此基础上添加新的属性和方法。
- **特点**：它体现了 “is - a” 的关系，即子类是父类的一种特殊类型。例如，“轿车” 是 “汽车” 的一种，“轿车” 类可以继承 “汽车” 类的属性（如车轮数量、颜色等）和方法（如启动、停止等），并可以添加自己特有的属性（如座位数量）和方法（如自动驾驶）。
- **表示**：在 UML 图中，继承关系用带空心三角箭头的实线表示，箭头指向父类。

#### 5. 依赖（Dependency）

- **定义**：依赖关系表示一个类的变化可能会影响到另一个类。这种影响通常是因为一个类使用了另一个类，比如一个类的方法参数、局部变量或返回值是另一个类的类型。
- **特点**：依赖是一种比较弱的关系。例如，“订单” 类的计算总价方法可能依赖 “商品” 类获取商品价格，“订单” 类并不拥有 “商品” 类的对象，但在执行计算操作时需要使用 “商品” 类的信息。
- **表示**：在 UML 图中，依赖关系用带箭头的虚线表示，箭头指向被依赖的类。
 ![[Pasted image 20260102125417.png]]

### 16.在类的继承中对象的调用方法

#### 1. 通过派生类对象调用

- **直接调用**：直接创建派生类对象，可直接调用派生类自身定义的方法以及从基类继承而来的可访问方法。例如：

```cpp
class Base {
public:
    void baseMethod() {
        std::cout << "Base method" << std::endl;
    }
};

class Derived : public Base {
public:
    void derivedMethod() {
        std::cout << "Derived method" << std::endl;
    }
};

int main() {
    Derived d;
    d.baseMethod(); // 调用从基类继承的方法
    d.derivedMethod(); // 调用派生类自身的方法
    return 0;
}
```

- **通过派生类指针或引用调用**：创建派生类指针或引用并指向 / 绑定派生类对象，同样能调用派生类自身及从基类继承的可访问方法。例如：

```cpp
int main() {
    Derived d;
    Derived* ptr = &d;
    ptr->baseMethod();
    ptr->derivedMethod();

    Derived& ref = d;
    ref.baseMethod();
    ref.derivedMethod();
    return 0;
}
```

#### 2. 通过基类对象、指针或引用调用

- **基类对象调用**：创建基类对象只能调用基类中定义的方法，无法调用派生类特有的方法，即便实际对象是派生类对象经隐式转换而来。例如：

```cpp
int main() {
    Derived d;
    Base b = d; // 派生类对象隐式转换为基类对象
    b.baseMethod();
    // b.derivedMethod(); // 编译错误，基类对象无法访问派生类特有的方法
    return 0;
}
```

- **基类指针或引用调用**：若基类指针或引用指向 / 绑定派生类对象，在编译时，只能调用基类中定义的方法。但如果基类方法是虚函数且派生类重写了该虚函数，在运行时会根据实际对象类型（即派生类类型）调用派生类重写的版本，这就是多态性。例如：

```cpp
class Base {
public:
    virtual void virtualMethod() {
        std::cout << "Base virtual method" << std::endl;
    }
};

class Derived : public Base {
public:
    void virtualMethod() override {
        std::cout << "Derived virtual method" << std::endl;
    }
    void derivedMethod() {
        std::cout << "Derived method" << std::endl;
    }
};

int main() {
    Derived d;
    Base* ptr = &d;
    ptr->virtualMethod(); // 运行时调用派生类重写的虚函数
    // ptr->derivedMethod(); // 编译错误，通过基类指针无法直接访问派生类特有的方法

    Base& ref = d;
    ref.virtualMethod(); // 运行时调用派生类重写的虚函数
    // ref.derivedMethod(); // 编译错误，通过基类引用无法直接访问派生类特有的方法
    return 0;
}
```

#### 3. 通过类型转换调用

- **`static_cast`**：在已知实际对象是派生类类型的情况下，可使用 `static_cast` 将基类指针或引用转换为派生类指针或引用，进而访问派生类特有的方法。但这种转换不进行运行时类型检查，如果实际对象不是派生类类型，会导致未定义行为。例如：

```cpp
int main() {
    Base* basePtr = new Derived();
    Derived* derivedPtr = static_cast<Derived*>(basePtr);
    derivedPtr->virtualMethod();
    derivedPtr->derivedMethod();
    delete basePtr;
    return 0;
}
```

- **`dynamic_cast`**：用于在有虚函数的情况下进行安全的类型转换。它在运行时检查类型转换是否合法，对于指针类型，如果转换失败返回 `nullptr`；对于引用类型，如果转换失败抛出 `std::bad_cast` 异常。例如：

```cpp
int main() {
    Base* basePtr = new Derived();
    Derived* derivedPtr = dynamic_cast<Derived*>(basePtr);
    if (derivedPtr) {
        derivedPtr->virtualMethod();
        derivedPtr->derivedMethod();
    }
    delete basePtr;

    Base* wrongPtr = new Base();
    Derived* wrongCastPtr = dynamic_cast<Derived*>(wrongPtr);
    if (!wrongCastPtr) {
        std::cout << "Dynamic cast failed" << std::endl;
    }
    delete wrongPtr;
    return 0;
}
```

### 17.函数调用运算符 `()` 在类中的重载
1. **概念**：在 C++ 中，函数调用运算符 `()` 可在类中重载，使得类的对象能像函数一样被调用 。当对象 `x` 属于类 `X` 且 `()` 被重载后，`x(arg1, arg2)` 会被解析为 `x.operator()(arg1, arg2)`。
2. **重载方式**：
    - 在类定义内部，像定义成员函数一样定义 `operator()`。其参数列表和返回类型可根据具体需求灵活设定，能有多个重载版本，通过不同参数列表来区分。
    - 例如：
```cpp
#include <iostream>
#include <string>

class MathOperations {
public:
    // 重载函数调用运算符，实现两个整数相加
    int operator()(int a, int b) {
        return a + b;
    }

    // 重载函数调用运算符，实现字符串拼接
    std::string operator()(const std::string& str1, const std::string& str2) {
        return str1 + str2;
    }
    
    //实现字符串打印
    void operator()(const std::string str1){
	    std::cout << str1 << std::endl;
    }
};

int main() {
    MathOperations mathOp;
    int sum = mathOp(3, 5);
    std::cout << "Sum of 3 and 5 is: " << sum << std::endl;

    std::string result = mathOp("Hello, ", "world!");
    std::cout << "Concatenated string: " << result << std::endl;

    return 0;
}
```

3. **使用场景**：
    
    - **函数对象**：常用于创建函数对象，这种对象可像普通函数一样使用，在算法库（如 `std::sort` 的自定义比较函数）中广泛应用，提供更灵活的操作逻辑。
    - **实现特定功能封装**：将复杂的操作封装在类中，并通过重载 `()` 来执行，让代码结构更清晰，便于复用和维护。例如，一个图像处理类可通过重载 `()` 来执行不同的图像操作。

### 18.下标运算符 `[]` 在类中进行的重载
1. **重载下标运算符的概念**
    
    - 在 C++ 中，下标运算符 `[]` 可以在类中进行重载。它是一个二元运算符，`x[y]` 的形式会被解释为 `x.operator[](y)`，其中 `x` 是类 `X` 的对象，`y` 是传递给重载函数 `operator[]` 的参数。
    
2. **重载规则**
    
    - **参数声明**：重载 `operator[]` 函数时，只能显式地声明一个参数。这个参数通常用于表示下标值。例如，如果是对数组类进行重载，参数可能是数组的索引。
    - **返回类型**：返回类型根据实际需求确定。如果是模拟数组访问，可能返回数组元素的引用，以便对元素进行读写操作；如果是用于映射关系，可能返回与下标对应的映射值。
    
3. **示例代码 - 模拟数组访问**

```cpp
#include <iostream>
#include <stdexcept>

class MyArray {
private:
    int data[10];
public:
    MyArray() {
        for (int i = 0; i < 10; ++i) {
            data[i] = i * 2;
        }
    }
    // 重载下标运算符，返回元素引用，可用于读写
    int& operator[](int index) {
        if (index < 0 || index >= 10) {
            throw std::out_of_range("Index out of range");
        }
        return data[index];
    }
};

int main() {
    MyArray arr;
    // 使用重载的下标运算符读取元素
    std::cout << "Element at index 3: " << arr[3] << std::endl;
    // 使用重载的下标运算符修改元素
    arr[5] = 100;
    std::cout << "Element at index 5 after modification: " << arr[5] << std::endl;
      
try {  
    arr[11];  
} catch (const std::out_of_range& e) {  
    std::cout << "异常捕获：" << e.what() << std::endl;  
}
    return 0;
}
```

### 19.虚析构函数

1. **通过基类指针删除派生类对象的场景**
    
    - 在 C++ 的多态编程中，经常会使用基类指针来操作派生类对象。例如：
    
```cpp
class Base {
public:
    Base() {
        std::cout << "Base constructor" << std::endl;
    }
    ~Base() {
        std::cout << "Base destructor" << std::endl;
    }
};

class Derived : public Base {
private:
    int *data;
public:
    Derived() {
        data = new int(10);
        std::cout << "Derived constructor" << std::endl;
    }
    ~Derived() {
        delete data;
        std::cout << "Derived destructor" << std::endl;
    }
};
```

- 然后在 `main` 函数中，可能会这样写：

```cpp
int main() {
    Base *ptr = new Derived();
    delete ptr;
    return 0;
}
```

- 在这个例子中，`ptr` 是一个基类指针，它指向一个派生类对象。当执行 `delete ptr;` 时，如果基类的析构函数不是虚函数，就会出现问题。

2. **非虚析构函数的问题**
    
    - 当基类析构函数不是虚函数时，`delete ptr;` 只会调用基类的析构函数，而不会调用派生类的析构函数。在上面的 `Derived` 类中，`Derived` 类的析构函数负责释放动态分配的内存（`delete data;`）。如果不调用 `Derived` 类的析构函数，就会导致内存泄漏，因为 `data` 所指向的内存没有被释放。
    - 输出结果会是：
```cpp
Base constructor
Derived constructor
Base destructor
```

- 可以看到，`Derived` 类的析构函数没有被调用。

3. **虚析构函数的作用**
    
    - 当把基类的析构函数声明为虚函数时，如：
    
```cpp
class Base {
public:
    Base() {
        std::cout << "Base constructor" << std::endl;
    }
    virtual ~Base() {
        std::cout << "Base destructor" << std::endl;
    }
};
```

- 此时再执行 `delete ptr;`，会首先调用派生类的析构函数，然后调用基类的析构函数。这是因为虚函数机制在运行时会根据对象的实际类型（这里是 `Derived` 类）来确定调用哪个析构函数。
- 输出结果会是：

plaintext

```
Base constructor
Derived constructor
Derived destructor
Base destructor
```

- 这样就确保了派生类中动态分配的资源（如 `data`）能够被正确释放，避免了内存泄漏。

4. **总结**
    - 当可能通过基类指针删除派生类对象时，为了保证派生类的析构函数能够被正确调用，从而正确释放派生类对象所占用的资源，需要将基类的析构函数声明为虚函数。否则，执行 `delete` 操作时，只会调用基类析构函数，而派生类析构函数不会被调用，导致不确定的结果，最常见的就是内存泄漏。所以，如果允许其他人通过基类指针调用对象的析构函数（通过 `delete`），就一定要让基类的析构函数成为虚函数。

### 20.简单的模板

1. **类模板声明基础**
    
    - **模板参数表**：模板参数表可以包含零个或多个模板参数。模板参数可以是类型参数（用 `class` 或 `typename` 关键字声明），也可以是非类型参数（如整数、枚举等）。例如：
    
```cpp
template <typename T>
class MyClass {
    T data;
public:
    MyClass(T value) : data(value) {}
    T getData() {
        return data;
    }
};
```

这里 `typename T` 就是一个类型参数，`T` 可以代表任何类型。在实例化 `MyClass` 时，需要指定具体的类型来替换 `T`。

- **类成员声明**：在类模板内部，可以像普通类一样声明成员变量和成员函数。这些成员可以使用模板参数。如上述例子中，成员变量 `data` 的类型是模板参数 `T`，构造函数 `MyClass(T value)` 和成员函数 `T getData()` 也都使用了 `T`。

2. **类模板成员函数在类外定义**
    
    - **模板参数表重复**：当在类模板外部定义成员函数时，需要再次声明模板参数表。例如：
    
```cpp
template <typename T>
class MyClass {
    T data;
public:
    MyClass(T value);
    T getData();
};

template <typename T>
MyClass<T>::MyClass(T value) : data(value) {}

template <typename T>
T MyClass<T>::getData() {
    return data;
}
```

这里在类外定义 `MyClass` 的构造函数和 `getData` 函数时，都重新声明了 `template <typename T>`。

- **类名与模板参数标识符列表**：类名后面要紧跟 `<模板参数标识符列表>`，这里的模板参数标识符要与模板参数表中的一致。如 `MyClass<T>::MyClass(T value)` 和 `T MyClass<T>::getData()` 中的 `<T>` 要与前面声明的模板参数 `typename T` 相对应。

3. **示例完整代码及解释**

```cpp
#include <iostream>

// 类模板声明
template <typename T>
class MyClass {
    T data;
public:
    MyClass(T value);
    T getData();
};

// 构造函数在类外定义
template <typename T>
MyClass<T>::MyClass(T value) : data(value) {}

// getData函数在类外定义
template <typename T>
T MyClass<T>::getData() {
    return data;
}

int main() {
    MyClass<int> intObj(10);
    std::cout << "Integer data: " << intObj.getData() << std::endl;

    MyClass<double> doubleObj(3.14);
    std::cout << "Double data: " << doubleObj.getData() << std::endl;

    return 0;
}
```

在 `main` 函数中，首先实例化了 `MyClass<int>`，创建了一个 `int` 类型的 `MyClass` 对象 `intObj`，并调用 `getData` 函数输出数据。然后又实例化了 `MyClass<double>`，创建了一个 `double` 类型的 `MyClass` 对象 `doubleObj`，同样调用 `getData` 函数输出数据。通过类模板，可以用相同的代码结构处理不同类型的数据，提高了代码的复用性。

### 21.虚拟表
在 C++ 编程语境中，“虚拟表”（Virtual Table，常简称为 VTable）是实现多态性的一个关键机制。下面详细为你解释：

#### 1. 基本概念

- **定义**：虚拟表是一个存储类的虚函数地址的数组。每个包含虚函数的类都有一个与之关联的虚拟表。当一个类中声明了虚函数时，编译器会为该类创建一个虚拟表。
- **作用**：虚拟表的主要作用是在运行时确定应该调用哪个函数版本，从而实现动态绑定（多态性的一种实现方式）。当通过基类指针或引用调用虚函数时，程序能够根据对象的实际类型（而不是指针或引用的类型）来调用正确的虚函数版本。

#### 2. 工作原理

- **对象布局**：对于包含虚函数的类对象，其内存布局中会有一个指向虚拟表的指针（通常称为 vptr，virtual pointer）。这个指针位于对象的起始位置（在大多数编译器实现中）。例如，假设有一个类 `Base` 包含虚函数：

```c
class Base {
public:
    virtual void virtualFunction() {
        std::cout << "Base::virtualFunction" << std::endl;
    }
};
```

当创建 `Base` 类的对象 `b` 时，`b` 对象的内存中会有一个 `vptr` 指针，它指向 `Base` 类的虚拟表。

- **虚拟表填充**：编译器为 `Base` 类创建虚拟表，并将虚函数 `virtualFunction` 的地址填充到虚拟表中。如果 `Base` 类有多个虚函数，虚拟表中会按顺序存储这些虚函数的地址。
- **派生类情况**：当有派生类继承自包含虚函数的基类时，派生类会继承基类的虚拟表，并根据自身对虚函数的重写情况修改虚拟表。例如：

```cpp
class Derived : public Base {
public:
    void virtualFunction() override {
        std::cout << "Derived::virtualFunction" << std::endl;
    }
};
```

在 `Derived` 类中重写了 `virtualFunction` 函数。此时，`Derived` 类对象的 `vptr` 指针指向的虚拟表中，`virtualFunction` 对应的地址是 `Derived::virtualFunction` 的地址，而不是 `Base::virtualFunction` 的地址。

- **函数调用**：当通过基类指针或引用调用虚函数时，程序会首先通过对象的 `vptr` 找到对应的虚拟表，然后根据虚拟表中存储的函数地址调用相应的虚函数版本。例如：

```cpp
int main() {
    Base *ptr = new Derived();
    ptr->virtualFunction(); // 实际调用的是Derived::virtualFunction
    delete ptr;
    return 0;
}
```

在这个例子中，虽然 `ptr` 是 `Base` 类型的指针，但它指向的是 `Derived` 类对象。通过 `ptr` 调用 `virtualFunction` 时，程序会根据 `Derived` 类对象的 `vptr` 找到 `Derived` 类的虚拟表，并调用 `Derived::virtualFunction`，实现了多态性。
#### 3. 注意事项
类的多个实例对象可以共享本类的虚拟表