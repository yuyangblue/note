# 实验：Tiny Web 服务器（CS:APP 第 11 章）

> 实验内容：在教材 Tiny 服务器基础上完成一组扩展——请求行/报头回显（11.6 A）、MPG/MP4 视频、SIGCHLD 回收 CGI 子进程（11.8）、`serve_static` 改 malloc 版、HEAD 方法、POST 动态内容、优雅处理 SIGPIPE/EPIPE。
> 源码位置（WSL）：`~/workspace/projects/tiny/`（`tiny.c` + `cgi-bin/adder.c` + `csapp.c/h` + 测试页面与媒体文件；教材习题答案在 `作业/` 子目录）
> 全部改动均有中文详细注释，浏览器实测 + curl/telnet 实测通过。

---

## 相关章节

- [[01_网络编程_从以太网到套接字]] —— 套接字 API：`socket → bind → listen → accept`，Tiny 的 main 就这四步循环
- [[02_Web服务器]] —— HTTP 协议、静态/动态内容、CGI 约定，本实验是这章的完整落地
- [[01_系统级IO_UnixIO]] —— RIO 包（`Rio_readlineb/Rio_readnb/Rio_writen`）与文件描述符是整台服务器的地基

---

## 1. 完成的习题一览

| 习题 | 改动 | 验证 |
| --- | --- | --- |
| 11.6 A 回显 | `doit` 发 text/plain 头后逐行 `Rio_writen` 回显请求行+报头（已注释停用，可一键启用） | curl/浏览器 |
| MPG/MP4 | `get_filetype` 加 `video/mpeg`、`video/mp4` | `cmp` 逐字节一致 |
| 11.8 SIGCHLD | `sigchld_handler`（while+waitpid+WNOHANG+存取 errno），删 `Wait(NULL)` | 30 个 CGI 请求零僵尸 |
| malloc 版静态发送 | `mmap` 换成 `Malloc + Rio_readn + Rio_writen + Free` | 7 个文件逐字节一致 |
| HEAD | 方法白名单加 HEAD；`is_head` 置位后发完头即 return（`Content-length` 仍报真实大小） | curl -I 与 telnet |
| POST | `read_requesthdrs` 解析 Content-Length/Type → `Rio_readnb` 读请求体 → **管道**送 CGI stdin + 三个 CGI 环境变量 | post.html 表单浏览器实测 |
| SIGPIPE/EPIPE | `Signal(SIGPIPE, SIG_IGN)` + 宏重映射 `Rio_writen → safe_writen`（底层 `rio_writen`，出错不 exit） | 25 个提前关闭客户端，服务器存活 |

## 2. 三个最有讲解价值的点

**① POST 的管道桥**：请求体已被 Tiny 读进内存，套接字上没有数据可再读，而 CGI 约定从 stdin 取参数——`serve_dynamic` 里 `pipe` 建管 → fork 继承两端 → 子进程把读端 `Dup2` 成 stdin，父进程把请求体 `Rio_writen` 进写端再关闭（**EOF 靠关写端产生，不是写出来的**）。相当于手工搭了一条 `echo "x=3&y=4" | adder`。

**② SIGPIPE 会死两次**：客户端提前关闭后 write → 内核递送 SIGPIPE（默认终止进程）；即使忽略它，write 变成 `EPIPE` 错误，csapp 的 `Rio_writen` 包装又会 `unix_error → exit()`。所以必须**既忽略信号、又换掉会退出的写包装**两层都做。

**③ 哨兵思想贯穿全部习题**：HEAD 只发头不发体但报真实 `Content-length`；SIGCHLD 处理函数要 while 循环（信号不排队）并保存恢复 errno；`safe_writen` 出错不 return 也不 exit，后续写入安静失败、事务自然结束。

## 3. 调试/实验技巧沉淀

- **telnet 当裸 HTTP 客户端**：`telnet localhost 18080` 后手敲 `GET /home.html HTTP/1.0` + 空行，最直观地看到"请求行 + 报头"原样；敲错不能退格，只能重连；
- **curl 组合拳**：`curl -si`（看头+体）、`curl -I`（HEAD）、`curl -X POST -d "x=3&y=4"`（表单请求）；
- **F12 Network**：浏览器端看 `Request Method`、`Content-Length`、Payload，服务器端日志看同一事务的请求侧——两端对照理解 HTTP 事务；
- **制造 EPIPE**：Python `socket` 连上发完请求立刻 `close()`，配合 8MB 大文件制造部分写，日志里出现 44 条 EPIPE 而服务器存活。

## 4. 容易忘的细节

- `home.html` 里 `<img src="godzilla.gif">` 会让浏览器自动补发第二个请求——一张网页 = 1 次文档请求 + N 次资源请求，各自独立事务；
- `Content-Length: 7` 正好是 `"x=3&y=4"` 的字节数——POST 头部靠它界定请求体长度，`Rio_readnb` 必须从 rio 缓冲区读（裸 `read(fd)` 会漏掉 RIO 已预读的部分）；
- 官方 `adder.c` 直接 `atoi` 参数，教材式 `?x=3&y=4` 会得 0+0=0，需裸数字 `?3&4`（或像本项目一样改 adder 解析）。
