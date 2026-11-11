# 第十一章 网络编程（续）：Web 服务器与 HTTP

> 依据：CMU 15-213 第 22 讲（Network Programming Part 2，`22-netprog2-中文翻译.pptx` p30–p63）+ 《深入理解计算机系统》第 3 版第 11 章 §11.5–§11.6 + 课堂录音《网络框架设计相关讲解》整理稿（2026-11-11，见 `原始材料/课堂录音稿/2026-11-11-网络框架设计与并发/整理稿.md`）。
> 上一篇笔记讲到 echo 服务器——客户端发什么，服务器原样回什么。这是最简单的网络应用。这一篇把它换成真实场景：浏览器作为客户端，Web 服务器作为服务器，两者之间用 HTTP 协议对话。套接字框架完全一样，变的只是消息处理那一层。

---

## 目录

- [[#目录]]
- [[#1. Web 服务器在做什么]]
- [[#2. MIME 类型：服务器告诉浏览器"这是什么"]]
- [[#3. 静态内容与动态内容]]
- [[#4. URL：互联网上的资源地址]]
- [[#5. HTTP 请求格式]]
- [[#6. HTTP 响应格式]]
- [[#7. 一次完整的 HTTP 事务]]
- [[#8. Tiny Web 服务器：教材的完整示例]]
  - [[#8.1 整体工作流程]]
  - [[#8.2 静态响应：serve_static]]
  - [[#8.3 动态响应与 CGI]]
  - [[#8.4 GET 传参与 QUERY_STRING]]
- [[#9. HTTP/1.0 与 HTTP/1.1]]
- [[#10. 代理与缓存]]
- [[#11. C/S 与 B/S：两种客户端形态]]
- [[#12. 小结]]

---

## 1. Web 服务器在做什么

浏览器和 Web 服务器之间的通信规则叫 **HTTP（HyperText Transfer Protocol，超文本传输协议）**。"超文本"指的是网页不再只是纯文字——它包含图像、音频、视频，以及最关键的**超链接**，点击就跳到另一个页面。

HTTP 是应用层协议。它建立在 TCP 连接之上：浏览器先和服务器完成三次握手、建立一条 TCP 连接，然后在这条连接上发送 HTTP 请求、接收 HTTP 响应。一个最基本的 Web 事务就是——浏览器发一个请求行（"我要 `/index.html`"），服务器回一个响应行（"200 OK，这是内容"）。

网络是分层的。实际使用的是 TCP/IP 四层模型：应用层、传输层、网络层、链路层。理论上还有 OSI 七层模型，分得更细。HTTP 在最上面的应用层，同层还有 FTP（文件传输）、SMTP（发邮件）、POP3（收邮件）。游戏厂商自己定义的"命令 1 代表移动、命令 2 代表攻击"也是应用层协议，不过是私有的；HTTP 是国际公开标准。

---

## 2. MIME 类型：服务器告诉浏览器"这是什么"

服务器返回的内容不只是 HTML 网页，还可能是图片、音频、纯文本。服务器在响应头里用 **MIME（Multipurpose Internet Mail Extensions）类型**告诉浏览器："我发回来的这段数据是什么格式，你按什么方式渲染。"

| MIME 类型 | 内容 |
|---|---|
| `text/html` | HTML 文档 |
| `text/plain` | 纯文本，没有标签 |
| `image/gif` | GIF 图像 |
| `image/png` | PNG 图像 |

现在 JSON 也成了事实标准——`application/json`。它比早期 XML 轻很多：XML 每个字段都要成对的开闭标签（`<name>张三</name>`），传输的字节里大部分是标签开销；JSON 只用 `"name":"张三"`，有效信息占比高。HTML 其实可以看作 XML 的一个特例——标签名固定是 `<html>`、`<body>`、`<p>`，而 XML 的标签名可以自定义。

---

## 3. 静态内容与动态内容

HTTP 响应返回的内容分两大类：

- **静态内容**：服务器上现成的文件，请求来了直接读出来发回去。HTML 文件、图片、音频片段都是静态的。
- **动态内容**：响应时实时生成的。服务器收到请求后 fork 一个子进程、执行一个程序（查数据库、跑计算），把程序的输出作为响应发回去。

静态响应快——服务器只要 `open` 文件、`mmap` 映射到内存、`write` 出去。动态响应慢——要跑业务逻辑、查数据库，一台机器能扛的并发数差一个量级。工程上常用的优化是**动态页面静态化**：把那些很多人查、但结果不常变的动态查询，定时预先生成成静态页面存着，用户来查时直接发静态文件。

---

## 4. URL：互联网上的资源地址

**URL（Uniform Resource Locator，统一资源定位符）**唯一标识互联网上的一个资源。以 `http://www.example.com:8080/index.html` 为例：

| 部分 | 含义 | 可否省略 |
|---|---|---|
| `http://` | 协议类型（HTTPS 是加密的 HTTP） | 不能省 |
| `www.example.com` | 域名 | 不能省 |
| `:8080` | 端口号 | HTTP 默认 80，可以省略 |
| `/index.html` | 服务器上的文件路径 | 请求 `/` 时默认返回 index.html，也可省略 |

所以 `http://www.example.com` 和 `http://www.example.com:80/index.html` 访问的是同一个页面。客户端从 URL 的前缀推断三件事：用什么协议联系服务器、服务器在哪、服务器监听哪个端口；服务器从后缀取出要返回的文件路径。

---

## 5. HTTP 请求格式

HTTP 请求由一条请求行开头，后面跟零个或多个请求头，再跟一个空行（`\r\n`），空行之后才是请求体（GET 请求一般没有 body）。

请求行的格式是：

```
<方法> <URI> <版本>
```

**方法**告诉服务器要对这个资源做什么：

| 方法 | 作用 |
|---|---|
| GET | 获取资源 |
| POST | 提交数据（如登录表单） |
| HEAD | 类似 GET，但只返回响应头、不返回内容 |
| OPTIONS | 测试资源是否可用 |
| PUT | 上传/更新资源 |
| DELETE | 删除资源 |
| TRACE | 跟踪请求经过的路径 |

标准里方法很多，但实际工程中建议只用 GET 和 POST。很多防火墙会把 PUT、DELETE 等方法拦掉——实验室里就遇到过：按 RESTful 风格设计，删除用 DELETE、更新用 PUT，结果线上服务器外面的防火墙把这些方法全拦了，客户端发不到后端。最后只能把所有操作都改成 POST。

`<URI>` 对服务器来说是 URL 的后缀部分（如 `/index.html`）；对代理来说通常是完整 URL。`<版本>` 是请求使用的 HTTP 版本，`HTTP/1.0` 或 `HTTP/1.1`。

---

## 6. HTTP 响应格式

HTTP 响应由一条响应行开头，后面跟零个或多个响应头，再跟一个空行，空行之后是响应体。

响应行的格式是：

```
<版本> <状态码> <状态消息>
```

状态码是三位数字，告诉客户端请求的结果：

| 状态码 | 含义 |
|---|---|
| 200 | OK，请求成功 |
| 301 | 资源永久重定向 |
| 404 | Not Found，资源不存在 |
| 500 | 服务器内部错误（如动态处理时数据库出错） |

状态消息是对应的英文文本，和数字重复，但方便人读。

---

## 7. 一次完整的 HTTP 事务

用 `telnet` 命令可以手动发 HTTP 请求来观察整个过程：

```bash
$ telnet www.cmu.edu 80
Trying 128.2.42.52...
Connected to WWW-CMU-PROD-VIP.ANDREW.cmu.edu.
Escape character is '^]'.

GET / HTTP/1.1
Host: www.cmu.edu

```

最后两个空行（`\r\n\r\n`）结束请求头。服务器收到后返回：

```
HTTP/1.1 200 OK
Date: Fri, 29 Oct 2010 19:48:32 GMT
Server: Apache/2.2.14
Content-Length: 479
Content-Type: text/html
Connection: Keep-Alive

<html>...页面内容...</html>
```

注意 `Host` 头在 HTTP/1.1 里是必填的——一台服务器可能同时托管多个域名（虚拟主机），服务器靠 `Host` 头知道该返回哪个站点的内容。

---

## 8. Tiny Web 服务器：教材的完整示例

教材里的 Tiny Web 服务器只有 239 行带注释的 C 代码，是一个**迭代型** Web 服务器——同一时刻只服务一个客户端。它能返回静态内容（HTML、GIF、PNG、JPEG），也能通过 CGI 返回动态内容。它不像真实服务器那样健壮：用不规范的请求（比如行结束用 `\n` 而不是 `\r\n`）就能把它弄崩。

### 8.1 整体工作流程

```c
int main(int argc, char **argv) {
    int listenfd, connfd;
    struct sockaddr_storage clientaddr;
    listenfd = Open_listenfd(argv[1]);
    while (1) {
        connfd = Accept(listenfd, (SA *)&clientaddr, &clientlen);
        doit(connfd);      // 处理这个客户端
        Close(connfd);
    }
}
```

`doit` 函数做的事情：

1. 从 connfd 读一行请求，拆成 `<方法> <URI> <版本>`；
2. 如果方法不是 GET，返回错误；
3. 如果 URI 里包含 `cgi-bin`，走动态内容（`serve_dynamic`）；否则走静态内容（`serve_static`）。

### 8.2 静态响应：serve_static

静态响应分两次 `write`：先写响应头，再写文件内容。

```c
void serve_static(int fd, char *filename, int filesize) {
    int srcfd;
    char *srcp, filetype[MAXLINE], buf[MAXBUF];

    get_filetype(filename, filetype);          // 根据后缀判断 MIME 类型
    sprintf(buf, "HTTP/1.0 200 OK\r\n");
    sprintf(buf, "%sServer: Tiny Web Server\r\n", buf);
    sprintf(buf, "%sContent-length: %d\r\n", buf, filesize);
    sprintf(buf, "%sContent-type: %s\r\n\r\n", buf, filetype);
    Rio_writen(fd, buf, strlen(buf));          // 第一次写：响应头

    srcfd = Open(filename, O_RDONLY, 0);
    srcp = Mmap(0, filesize, PROT_READ, MAP_PRIVATE, srcfd, 0);
    Close(srcfd);
    Rio_writen(fd, srcp, filesize);             // 第二次写：文件内容
    Munmap(srcp, filesize);
}
```

这里用 `mmap` 把文件内容直接映射到进程地址空间——比 `read` 一个个字节读快得多，因为省去了内核空间到用户空间的拷贝。`srcp` 指向映射好的文件内容，直接 `write` 出去就行。

### 8.3 动态响应与 CGI

如果请求的 URI 里包含 `/cgi-bin`，Tiny 认为这是动态内容请求。它 fork 一个子进程，在子进程里 `execve` 执行 URI 指定的程序；子进程的标准输出被服务器捕获，不做修改地转发回客户端。

```c
void serve_dynamic(int fd, char *filename, char *cgiargs) {
    char buf[MAXLINE], *emptylist[] = { NULL };

    sprintf(buf, "HTTP/1.0 200 OK\r\n");
    Rio_writen(fd, buf, strlen(buf));
    sprintf(buf, "Server: Tiny Web Server\r\n");
    Rio_writen(fd, buf, strlen(buf));

    if (Fork() == 0) {              // 子进程
        setenv("QUERY_STRING", cgiargs, 1);   // 把参数放进环境变量
        Dup2(fd, STDOUT_FILENO);               // 把 stdout 重定向到 connfd
        Execve(filename, emptylist, environ);  // 执行 CGI 程序
    }
    Wait(NULL);                     // 父进程等待子进程结束
}
```

这里有两个关键操作：

- `setenv("QUERY_STRING", ...)`：客户端传的参数通过环境变量传给子进程；
- `Dup2(fd, STDOUT_FILENO)`：把子进程的标准输出重定向到 connfd——这样 CGI 程序 `printf` 的内容就直接写到客户端了，不需要 CGI 程序自己知道怎么写网络套接字。

**CGI（Common Gateway Interface，通用网关接口）** 是最早的动态内容生成标准。它规定了客户端、Web 服务器、外部程序三者之间怎么传信息。CGI 的缺点是每次请求都 fork 一个新进程，开销大、速度慢。现在基本被 FastCGI、Apache 模块、Java Servlet、Rails 控制器等技术取代——这些技术让外部程序常驻内存，不用每次重新创建进程。

### 8.4 GET 传参与 QUERY_STRING

客户端怎么把参数传给 CGI 程序？答案是把参数附加在 URI 后面，用 `?` 开头，多个参数用 `&` 分隔：

```
http://add.com/cgi-bin/adder?15213&18213
```

服务器从 URI 里取出 `?` 后面的部分（`15213&18213`），放进环境变量 `QUERY_STRING`。CGI 程序用 `getenv("QUERY_STRING")` 读出来，自己解析参数：

```c
if ((buf = getenv("QUERY_STRING")) != NULL) {
    p = strchr(buf, '&');
    *p = '\0';
    n1 = atoi(buf);
    n2 = atoi(p+1);
}
```

然后 CGI 程序 `printf` 输出结果——因为 stdout 已经被重定向到 connfd，这段输出就直接成为 HTTP 响应体。

---

## 9. HTTP/1.0 与 HTTP/1.1

HTTP/1.1 和 HTTP/1.0 的主要区别：

| | HTTP/1.0 | HTTP/1.1 |
|---|---|---|
| 连接 | 每个事务结束就关闭 TCP 连接 | 支持持久连接（Keep-Alive），同一条 TCP 上跑多个事务 |
| Host 头 | 不要求 | 必填（虚拟主机需要） |

持久连接省掉了每次请求都重新三次握手的开销。但连接不能一直占着——服务器会定时发探测消息问客户端"你还在吗"，客户端回应"我在"，这叫**心跳保活**。游戏服务器尤其需要这个：客户端异常掉线（网络断了、电脑死机）时，服务器不知道连接已死，这个连接资源就一直占着。有了心跳机制，几个心跳没收到就认为客户端不在了，直接释放资源。

---

## 10. 代理与缓存

**代理（proxy）**是客户端和源服务器之间的中介。对客户端来说，代理就像一台服务器；对服务器来说，代理就像一个客户端。

```
客户端 → 代理 → 源服务器
```

代理能做的事情：

- **缓存**：把经常访问的资源缓存在代理上，下次别人来要同样的内容直接从代理发，不用回源站。国内的开源软件镜像源（清华、中科、阿里的 PyPI、Docker Hub 镜像）就是这个原理。
- **南北运营商互通**：南方以电信为主，北方以联通为主，跨运营商访问要绕路。在北方部署代理节点，北方用户直接访问北方节点，节点通过专线访问南方源站，两边都快。
- **日志记录、匿名化、过滤、转码**。

---

## 11. C/S 与 B/S：两种客户端形态

Web 服务器的客户端是浏览器，这种模式叫 **B/S（Browser/Server）**；对应的传统模式叫 **C/S（Client/Server）**——客户端是自己写的应用程序。但 B/S 底层仍然是 C/S，只不过客户端固定成了浏览器这个通用程序。

| | C/S | B/S |
|---|---|---|
| 客户端 | 自己写的应用程序 | 浏览器 |
| 渲染能力 | 强，可以做复杂 3D 游戏 | 弱，只能做简单渲染 |
| 更新 | 服务器端更新没用，客户端必须跟着更新 | 所有东西在服务器端，客户端不用更新 |
| 典型场景 | 重型游戏、专业客户端 | OA 办公系统、网页应用 |

C/S 的好处是客户端可以做很复杂的事情——大型 3D 游戏必须用 C/S，浏览器渲染能力有限。缺点是版本管理麻烦：服务器更新了，客户端版本不对就连不上，必须强制更新。B/S 的好处是所有东西都在服务器端，要更新就是厂商自己更新一下，跟用户的浏览器没关系。

---

## 12. 小结

- Web 服务器本质上还是套接字编程——`socket` / `bind` / `listen` / `accept` / `read` / `write`，和 echo 服务器一模一样；
- 区别在于消息处理：echo 是原样返回，Web 服务器是解析 HTTP 请求行、根据 URI 返回静态文件或执行 CGI 程序返回动态内容；
- HTTP 请求 = 请求行（方法 URI 版本）+ 请求头 + 空行 + body；HTTP 响应 = 响应行（版本 状态码 状态消息）+ 响应头 + 空行 + body；
- 静态内容直接 `mmap` 文件后 `write` 两次（先头后内容）；动态内容 `fork` 子进程执行 CGI 程序，参数通过 `QUERY_STRING` 环境变量传递，stdout 重定向到 connfd；
- HTTP/1.1 的 Keep-Alive 让一条 TCP 连接跑多个事务；代理可以做缓存和跨运营商加速。

---

> **本节重点**：
> - Web 服务器 = 套接字框架 + HTTP 消息解析，不是什么新东西；
> - 静态响应两次 write（头 + 文件内容），动态响应 fork + execve + dup2(stdout→connfd)；
> - CGI 参数走 `QUERY_STRING` 环境变量，不是命令行参数；
> - HTTP/1.1 持久连接 + Host 头是和 1.0 的核心区别；
> - **常见坑**：响应头和响应体之间必须有一个空行（`\r\n\r\n`），少了浏览器不认。
