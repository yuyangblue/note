# 实验8：实现一个迷你 Shell（msh）

> 实验要求：写一个 shell 程序 `msh`，支持执行外部命令、`&` 后台运行、`timeout` 超时杀进程、SIGCHLD 防僵尸、Ctrl+C 不退出 shell。
> 源码位置（WSL）：`~/workspace/projects/shell/`（`msh.c` + `代码讲解.md` + `问答笔记.md`）

---

## 相关章节

- [[01_进程ECF]] —— fork / execve / waitpid 三部曲就是异常控制流（进程级）的核心应用
- [[02_信号与进程组_Signals]] —— SIGALRM / SIGCHLD / SIGINT 三个信号的处理贯穿整个实验

---

## 1. 程序骨架：Shell 的本质

Shell 就是一个**永不停止的"读命令 → 建进程 → 等结果"循环**：

```
┌──────── 主循环 main() ────────┐
│ 1. 打印提示符 "msh> "          │
│ 2. fgets 读一行输入            │
│ 3. parse_line 拆成 argv[]     │
│ 4. 内置命令 or 外部命令        │
│    exit    → 退出             │
│    timeout → builtin_timeout  │
│    其他    → execute_command  │
│ 5. 回到第 1 步                │
└───────────────────────────────┘
```

唯一的全局状态：`static pid_t fg_pid;`（当前前台作业 pid）——信号处理函数与主流程之间唯一的通信渠道（处理函数不能安全传普通参数）。

## 2. 五条要求 × 系统调用对照表

| 需求 | 实现位置 | 核心系统调用 |
| --- | --- | --- |
| 1. 执行外部命令 | `execute_command` | `fork` + `execvp` + `waitpid` |
| 2. `&` 后台运行 | `execute_command` 的 `bg` 分支 | fork 后**不 wait** |
| 3. `timeout` 超时 | `builtin_timeout` + `sigalrm_handler` | `alarm` + `kill` |
| 4. SIGCHLD 防僵尸 | `sigchld_handler` | `sigaction` + `waitpid(WNOHANG)` |
| 5. Ctrl+C 不退出 | `setup_signals` + 子进程恢复 | `SIG_IGN` / `SIG_DFL` |

## 3. 关键讲解

**fork / exec / wait 三部曲**：`fork` 一次调用两次返回（父拿子 pid、子拿 0）；`execvp` 用新程序整个替换当前进程映像（成功不返回，必须接 `exit(127)` 兜底；带 `p` 按 `PATH` 搜命令名）；`waitpid` 收尸——不收就是僵尸进程（`ps` 状态 `Z`，占进程表项）。

**`&` 后台 = 只是"不等"**：没有任何新系统调用，fork 后父进程直接回去显示提示符。但带来新问题——后台子进程退出时父进程没在 wait，谁来收尸？答案就是需求 4：让内核在子进程退出时**主动发 SIGCHLD 通知**。

**SIGCHLD 处理函数**（与 Tiny 服务器习题 11.8 同款）：

```c
while (waitpid(-1, NULL, WNOHANG) > 0)
    ;                       /* 循环：信号不排队，一次收完所有已终止子进程 */
```

**Ctrl+C 不退出**：shell 里 `SIGINT` 设 `SIG_IGN`（忽略），fork 后子进程里恢复 `SIG_DFL`——否则 Ctrl+C 连 ls 一起"免疫"了。忽略型处置会跨 fork 保留，所以子进程必须显式恢复默认。

**timeout**：`alarm(n)` 定时 + SIGALRM 处理函数里 `kill(fg_pid, SIGKILL)`；前台 pid 存全局变量，处理函数才知道杀谁。子进程被杀后 `waitpid` 返回，shell 打印 "timed out"。

## 4. 验证方法

```bash
msh> ls                      # 外部命令
msh> sleep 10 &              # 立即回提示符；sleep 结束后无僵尸（ps 查证）
msh> timeout 2 sleep 5       # 2 秒后打印 timed out 并杀掉 sleep
msh> Ctrl+C                  # shell 不退出；前台 ls 被 SIGINT 杀掉
```

## 5. 踩过的坑

- **`execvp` 后必须 `exit(127)`**：exec 失败（命令不存在）子进程不能继续跑 shell 的代码；
- **`waitpid` 循环 + `WNOHANG`**：信号不排队，多个后台任务同时退出只收到一个 SIGCHLD；
- **`sigaction` 而非 `signal()`**：行为可控（`SA_RESTART`、`sa_mask` 沿用），`signal()` 历史语义不一且可能被自动重置；
- **Ctrl+C 的"免疫"陷阱**：只在 shell 里 `SIG_IGN` 不够，子进程必须 `SIG_DFL` 恢复，否则命令行程序收不到中断。

## 6. 与后续实验的联系

本实验的 SIGCHLD 处理模式（while + WNOHANG + 保存恢复 errno）后来在 [[实验_TinyWeb服务器]] 的习题 11.8 里原样复用——CGI 子进程回收与后台命令收尸是同一个问题。
