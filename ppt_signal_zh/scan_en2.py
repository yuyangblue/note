# -*- coding: utf-8 -*-
"""Scan readback2.xml for remaining English text; classify by block."""
import io, re

t = io.open(r"D:\29469\Documents\notes\ppt_signal_zh\readback2.xml", encoding="utf-8").read()
slides = re.findall(r'<slide\b[^>]*>.*?</slide>', t, re.S)
pat = re.compile(r"[A-Za-z]{3,}")
CODE_OK = {"int", "char", "void", "main", "while", "if", "else", "return", "for", "exit",
           "printf", "Fgets", "eval", "fork", "Fork", "waitpid", "wait", "sleep", "Sleep",
           "kill", "signal", "Signal", "sigprocmask", "Sigprocmask", "sigemptyset",
           "sigaddset", "sigfillset", "sigdelset", "sigaction", "setjmp", "longjmp",
           "sigsetjmp", "siglongjmp", "sigsuspend", "Sigsuspend", "pause", "execve",
           "Execve", "unix_error", "Sio_error", "Sio_puts", "Sio_putl", "fflush", "stdout",
           "SIGINT", "SIGKILL", "SIGSEGV", "SIGALRM", "SIGCHLD", "SIGTSTP", "SIGCONT",
           "SIG_ERR", "SIG_IGN", "SIG_DFL", "SA_RESTART", "SIG_BLOCK", "SIG_SETMASK",
           "ECHILD", "WIFEXITED", "WEXITSTATUS", "NULL", "pid", "pid_t", "wpid", "argc",
           "argv", "cmdline", "MAXLINE", "MAXARGS", "environ", "status", "buf", "sig",
           "olderrno", "errno", "ccount", "mask", "prev", "prev_mask", "mask_all",
           "mask_one", "prev_one", "prev_all", "old_action", "action", "handler",
           "handler_t", "jmp_buf", "sigset_t", "sigjmp_buf", "struct", "child_handler",
           "child_handler2", "sigint_handler", "sigchld_handler", "foo", "bar", "error1",
           "error2", "p1", "p2", "p3", "P1", "P2", "P3", "env", "i", "j", "x", "y", "z",
           "pid", "main", "return", "case", "default", "break", "switch", "error",
           "reaped", "child", "starting", "restarting", "processing", "Handler", "Child",
           "Parent", "Terminate", "Kill", "Ignore", "Timer", "User", "typed", "ctrl",
           "Segmentation", "violation", "stopped", "terminated", "SIGKILL", "SIGSEGV",
           "SIGALRM", "SIGCHLD", "SIGINT", "sleep", "wait", "Waitpid", "Fork", "Execve",
           "Sigprocmask", "Sigfillset", "Sigaddset", "Sigemptyset", "Signal", "exit",
           "Detected", "Unknown", "condition", "greatwhite", "whaleshark", "linux",
           "bluefish", "forks", "ps", "gcc", "kill", "bin", "OK", "Well", "bomb",
           "ctrl", "stop", "you", "think", "with", "do", "So", "Sio", "Pid", "File",
           "Pgrp", "Ps", "infinite", "Infinite", "Loop", "Killing", "process", "wpid",
           "Sigchld", "Sigint", "Initjobs", "Addjob", "Deletejob", "initjobs", "addjob",
           "deletejob", "parseline", "builtin", "command", "status", "waitfg", "sh",
           "tcsh", "csh", "bash", "Bourne", "Again", "Stephen", "Bell", "Labs", "httpd",
           "pstree", "init", "Perl", "python", "Randal", "Bryant", "David", "O", "Hallaron",
           "Carnegie", "Mellon", "Computer", "Systems", "Programmer", "Perspective",
           "Pers", "Click", "add", "text", "ECF", "Unix", "Linux", "execve", "execve",
           "cmdline", "MAXLINE", "Fgets", "feof", "eval", "parseline", "argv", "environ",
           "maxargs", "shellex", "procmask", "waitforsignal", "sigsuspend", "sigint",
           "sigchld", "sigaction", "restart", "csapp", "app", "h", "include", "define",
           "ifdef", "endif", "sio", "error", "exit", "status", "Waitpid", "Sigsuspend",
           "Sigprocmask", "Sigemptyset", "Sigaddset", "Sigfillset", "Signal", "Fork",
           "Execve", "Sleep", "Pause", "Sio_puts", "Sio_putl", "Sio_error", "unix_error",
           "errno", "EINTR", "ECHILD", "SA_RESTART", "SIG", "BLOCK", "SETMASK", "IGN",
           "DFL", "ERR", "default", "switch", "case", "break", "longjmp", "setjmp",
           "buf", "sigjmp", "restart", "starting", "restarting", "processing", "reaped",
           "Killing", "terminated", "exit", "status", "child", "Child", "Parent",
           "whaleshark", "greatwhite", "forks", "restart", "Handler", "reaped",
           "condition", "foo", "error1", "error2", "Unknown", "Detected", "Ctrl", "ID",
           "Name", "Action", "Corresponding", "Event", "编号", "名称", "默认动作", "对应事件",
           "Getpgrp", "Setpgid", "getpgrp", "setpgid", "sigemptyset", "sigfillset",
           "sigaddset", "sigdelset", "Sio_error", "Sio_puts", "Sio_putl", "sleep",
           "kill", "wait", "waitpid", "write", "exit", "malloc", "sprintf", "printf",
           "ppid", "pgid", "pid", "pid", "Pid", "pgrp", "stat", "time", "cmd", "TTY",
           "CMD", "pts", "tcsh", "forks", "ps", "linux", "bluefish", "whaleshark",
           "greatwhite", "restart", "Handler", "reaped", "child", "starting",
           "restarting", "processing", "Ctrl", "procmask1", "procmask2", "sigsuspend",
           "waitforsignal", "sigint", "sigintsafe", "restart", "fork14", "fork12",
           "forks", "c", "C", "Sio", "Puts", "Putl", "Error", "wait", "error", "signal",
           "Signal", "Installing", "Default", "Actions", "SIG", "Handlers", "Handling",
           "Receiving", "Sending", "Blocking", "Unblocking", "Temporarily", "Safe",
           "Safety", "Async", "Correct", "Portable", "Nested", "Concurrent", "Flows",
           "Explicitly", "Waiting", "sigsuspend", "Synchronizing", "Avoid", "Races",
           "Nonlocal", "Jumps", "setjmp", "longjmp", "Summary", "Additional", "slides",
           "Today", "Shells", "Signals", "Nonlocal", "jumps", "Consult", "your",
           "textbook", "and", "additional", "slides", "putting", "together", "program",
           "restarts", "itself", "ctrl", "pressing", "Putting", "Together", "Program",
           "Restarts", "Itself", "When", "Limitations", "Long", "Jumps", "Works",
           "within", "stack", "discipline", "can", "only", "long", "jump", "environment",
           "function", "that", "has", "been", "called", "but", "not", "yet", "completed",
           "At", "setjmp", "longjmp", "P2", "returns", "Before", "After", "Meaning",
           "return", "from", "the", "remembered", "by", "jump", "buffer", "again",
           "this", "time", "returning", "instead", "of", "Called", "once", "but", "never",
           "returns", "Restore", "register", "context", "stack", "pointer", "base",
           "PC", "value", "from", "Set", "eax", "the", "to", "Jump", "location",
           "indicated", "stored", "in", "Powerful", "dangerous", "user", "level",
           "mechanism", "for", "transferring", "control", "arbitrary", "Controlled",
           "way", "break", "procedure", "call", "return", "discipline", "Useful",
           "error", "recovery", "signal", "handling", "int", "Must", "before",
           "Identifies", "site", "subsequent", "one", "more", "times", "Implementation",
           "Remember", "where", "you", "are", "storing", "current", "and", "Goal",
           "directly", "original", "caller", "deeply", "nested", "function", "Deeply",
           "Putting", "All", "Together", "Great", "white", "restarting", "processing",
           "sigsuspend", "Equivalent", "atomic", "uninterruptable", "version", "Program",
           "correct", "wasteful", "Other", "options", "Solution", "Similar", "shell",
           "waiting", "foreground", "job", "terminate", "Corrected", "Shell", "without",
           "Race", "Simple", "subtle", "synchronization", "assumes", "runs", "first",
           "Guidelines", "Writing", "Safe", "Keep", "handlers", "simple", "possible",
           "Set", "global", "flag", "Call", "only", "async", "functions", "are", "not",
           "Save", "restore", "entry", "exit", "So", "other", "don", "overwrite",
           "value", "Protect", "accesses", "shared", "data", "structures", "temporarily",
           "blocking", "all", "To", "prevent", "possible", "corruption", "Declare",
           "volatile", "compiler", "storing", "them", "register", "flags", "sig_atomic_t",
           "variable", "read", "written", "e.g.", "Flag", "declared", "this", "way",
           "does", "need", "protected", "like", "globals", "Function", "reentrant",
           "stored", "stack", "frame", "Posix", "guarantees", "functions", "Source",
           "man", "Popular", "list", "Unfortunate", "fact", "only", "output",
           "Safely", "Generating", "Formatted", "Output", "reentrant", "SIO", "library",
           "from", "your", "Put", "string", "msg", "Pending", "queued", "For", "each",
           "type", "bit", "indicates", "whether", "signal", "thus", "at", "most",
           "particular", "You", "use", "count", "events", "such", "children",
           "terminating", "Correct", "Must", "all", "terminated", "child", "processes",
           "loop", "reap", "Ugh", "Different", "versions", "can", "different",
           "handling", "semantics", "older", "systems", "restore", "action", "default",
           "after", "catching", "interrupted", "syscalls", "with", "EINTR", "don",
           "block", "type", "being", "handled", "Solution", "Implicit", "mechanism",
           "Kernel", "pending", "currently", "E.g.", "interrupted", "another",
           "Explicit", "unblocking", "sigprocmask", "Supporting", "Create", "empty",
           "set", "Add", "every", "number", "Delete", "from", "Code", "region", "will",
           "interrupt", "Restore", "previous", "unblocking", "tricky", "concurrent",
           "main", "program", "share", "same", "global", "corrupted", "ll", "explore",
           "concurrency", "issues", "later", "term", "here", "some", "help", "avoid",
           "trouble", "假设内核正从异常处理程序返回，准备把控制权交给进程 p",
           "内核计算 pnb = pending &amp; ~blocked", "正在被处理的信号类型", "进程组",
           "显式", "辅助", "列表中的常用函数", "不在列表中的常用函数", "处理程序", "子进程",
           "被接收", "回收", "解除", "主程序", "当前", "下一", "上下文切换", "内核代码",
           "用户代码", "嵌套", "捕获", "返回", "等待", "阻塞", "信号", "默认", "动作",
           "接收", "发送", "递送", "已到达", "集合", "编号", "名称", "事件", "终止",
           "忽略", "定时器", "段违规", "用户键入", "对应", "SIGINT", "SIGKILL", "SIGSEGV",
           "SIGALRM", "SIGCHLD"}

keep = []
for s in slides:
    sid = re.search(r'\bid="([^"]+)"', s).group(1)
    for sm in re.finditer(r'<span\b[^>]*>([^<]*)</span>', s):
        txt = sm.group(1)
        if not pat.search(txt):
            continue
        head = s[:sm.start()]
        bidm = re.findall(r'<shape\b[^>]*\bid="([^"]+)"', head)
        bid = bidm[-1] if bidm else "?"
        # check if mostly code-ish: split words, all known
        words = set(re.findall(r"[A-Za-z0-9_\.]+", txt))
        unknown = {w for w in words if w not in CODE_OK}
        if unknown:
            keep.append((sid, bid, txt[:70], sorted(unknown)[:5]))

seen = set()
for sid, bid, txt, unk in keep:
    k = (sid, bid, txt)
    if k in seen:
        continue
    seen.add(k)
    print(sid, bid, repr(txt), "UNK:", unk)
