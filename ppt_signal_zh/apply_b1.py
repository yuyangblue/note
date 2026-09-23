# -*- coding: utf-8 -*-
"""Apply batch translations. Modes: lines (rebuild br-separated segments, keep first span style per segment) / sub (substring pairs, keep all spans)."""
import io, os, re, json
from xml.sax.saxutils import escape as sax_escape

os.chdir(r"D:\29469\Documents\notes\ppt_signal_zh")
SRC = io.open("source.xml", encoding="utf-8").read()

def escape(s):
    # PPT XML escapes quotes as &quot; inside text nodes; mimic that
    return sax_escape(s).replace('"', "&quot;").replace("'", "&apos;")

B1 = {
 "pVR": {
   "bet": {"mode": "lines", "lines": ["异常控制流：", "信号与非本地跳转", "", "15-213：计算机系统导论", "第 15 讲，2015 年 10 月 20 日"]},
   "beX": {"mode": "lines", "lines": ["授课教师：", "Randal E. Bryant and David R. O’Hallaron"]},
 },
 "pVi": {
   "beY": {"mode": "lines", "lines": ["ECF 存在于系统的各个层次"]},
   "beu": {"mode": "lines", "lines": ["异常", "硬件和操作系统内核软件", "进程上下文切换", "硬件定时器和内核软件", "信号", "内核软件和应用程序软件", "非本地跳转", "应用程序代码"]},
   "beA": {"mode": "lines", "lines": [" "]},
   "bev": {"mode": "lines", "lines": ["上一讲"]},
   "ber": {"mode": "lines", "lines": [" "]},
   "beK": {"mode": "lines", "lines": ["本讲"]},
   "beB": {"mode": "lines", "lines": ["课本和 ", "补充幻灯片"]},
   "beU": {"mode": "lines", "lines": [" "]},
 },
 "pVm": {
   "beI": {"mode": "lines", "lines": ["今日内容"]},
   "beF": {"mode": "lines", "lines": ["外壳 Shell", "信号 Signals", "非本地跳转 Nonlocal jumps"]},
 },
 "pVd": {
   "ben": {"mode": "lines", "lines": ["Linux 进程层次结构"]},
   "beQ": {"mode": "lines", "lines": ["登录外壳"]},
   "beq": {"mode": "lines", "lines": ["子进程"]},
   "bej": {"mode": "lines", "lines": ["子进程"]},
   "beS": {"mode": "lines", "lines": ["孙进程"]},
   "bel": {"mode": "lines", "lines": ["孙进程"]},
   "beH": {"mode": "lines", "lines": ["[0]"]},
   "beW": {"mode": "lines", "lines": ["守护进程", "例如 httpd"]},
   "bef": {"mode": "lines", "lines": ["init [1]"]},
   "beV": {"mode": "lines", "lines": ["登录外壳"]},
   "beh": {"mode": "lines", "lines": ["子进程"]},
   "beM": {"mode": "lines", "lines": ["…"]},
   "beE": {"mode": "lines", "lines": ["…"]},
   "beZ": {"mode": "lines", "lines": ["…"]},
   "beP": {"mode": "lines", "lines": ["注意：可使用 Linux 的 pstree 命令查看该层次"]},
 },
 "pVe": {
   "bww": {"mode": "lines", "lines": ["外壳程序"]},
   "bwi": {"mode": "lines", "lines": ["外壳（shell）是一种应用程序，代表用户运行其他程序。",
           "sh 最初的 Unix 外壳（Stephen Bourne，AT&T 贝尔实验室，1977）",
           "csh/tcsh BSD Unix 的 C 外壳",
           "bash “Bourne-Again” 外壳（Linux 默认外壳）"]},
   "bem": {"mode": "sub", "pairs": [["/* command line */", "/* 命令行 */"],
           ["/* read */", "/* 读取 */"], ["/* evaluate */", "/* 求值 */"]]},
   "beL": {"mode": "lines", "lines": ["执行过程是一系列读取/求值步骤"]},
   "beJ": {"mode": "lines", "lines": ["shellex.c"]},
 },
 "pVf": {
   "beD": {"mode": "lines", "lines": ["简单外壳的 eval 函数"]},
   "beG": {"mode": "sub", "pairs": [
           ["/* Argument list execve() */", "/* 供 execve() 使用的参数列表 */"],
           ["/* Holds modified command line */", "/* 存放修改后的命令行 */"],
           ["/* Should the job run in bg or fg? */", "/* 作业应在后台还是前台运行？ */"],
           ["/* Process id */", "/* 进程 ID */"],
           ["/* Ignore empty lines */", "/* 忽略空行 */"],
           ["/* Child runs user job */", "/* 子进程运行用户作业 */"],
           ["/* Parent waits for foreground job to terminate */", "/* 父进程等待前台作业终止 */"],
           ['"%s: Command not found.\\n"', '"%s：找不到命令。\\n"'],
           ['"waitfg: waitpid error"', '"waitfg：waitpid 错误"']]},
   "bea": {"mode": "lines", "lines": ["shellex.c"]},
 },
 "pVq": {
   "bwC": {"mode": "lines", "lines": ["简单外壳示例的问题"]},
   "bwI": {"mode": "lines", "lines": ["我们的示例外壳能正确等待并回收前台作业", "",
           "但后台作业呢？", "它们终止时会变成僵尸进程",
           "永远不会被回收，因为外壳（通常）不会终止",
           "会造成内存泄漏，可能耗尽内核内存"]},
 },
 "pVx": {
   "bws": {"mode": "lines", "lines": ["ECF 来救场！"]},
   "bwt": {"mode": "lines", "lines": ["解决办法：异常控制流",
           "当后台进程完成时，内核会中断常规处理来提醒我们",
           "在 Unix 中，这种提醒机制称为信号（signal）"]},
 },
 "pVY": {
   "bwh": {"mode": "lines", "lines": ["今日内容"]},
   "bwj": {"mode": "lines", "lines": ["外壳 Shell", "信号 Signals", "非本地跳转 Nonlocal jumps"]},
 },
}

runs = json.load(io.open("runs.json", encoding="utf-8"))

def slide_xml(text, sid):
    m = re.search(r'<slide\b[^>]*\bid="%s"[^>]*>.*?</slide>' % re.escape(sid), text, re.S)
    return m.group(0) if m else None

def shape_xml(slide_text, bid):
    m = re.search(r'<shape\b[^>]*\bid="%s"[^>]*/>|<shape\b[^>]*\bid="%s"[^>]*>.*?</shape>' % (re.escape(bid), re.escape(bid)), slide_text, re.S)
    return m.group(0) if m else None

def seg_count_for_ps(ps):
    """number of br-separated segments across ps"""
    n = 0
    for ps_runs in ps:
        # split by br within this p
        seg = 1
        for x in ps_runs:
            if x["tag"] == "br":
                seg += 1
        n += seg
    return n

def rebuild_ps(shape_text, ps, new_lines):
    """replace each <p> inner text; new_lines flat over segments (br-split, all ps concatenated)."""
    out = shape_text
    # find all <p>...</p> in shape (also self-closing <p .../>)
    p_pat = re.compile(r'<p\b[^>]*/>|<p\b[^>]*>.*?</p>', re.S)
    pm = list(p_pat.finditer(shape_text))
    if len(pm) != len(ps):
        raise ValueError("p count mismatch: %d vs %d" % (len(pm), len(ps)))
    # build per-p segment counts
    counts = []
    for ps_runs in ps:
        c = 1
        for x in ps_runs:
            if x["tag"] == "br":
                c += 1
        counts.append(c)
    # slice translated segments per p in order, then apply from END to START
    segs_by_p = []
    idx = 0
    for c in counts:
        segs_by_p.append(new_lines[idx:idx + c])
        idx += c
    for pi in range(len(ps) - 1, -1, -1):
        m = pm[pi]
        new_p = rebuild_p(m.group(0), segs_by_p[pi])
        out = out[:m.start()] + new_p + out[m.end():]
    return out

def rebuild_p(p_xml, segs):
    sm = re.match(r'<p\b[^>]*/>', p_xml)
    if sm:
        # self-closing empty paragraph -> keep as empty <p attrs></p>
        return sm.group(0)[:-2] + '></p>'
    m = re.match(r'<p\b[^>]*>', p_xml)
    p_open = m.group(0)
    inner = p_xml[m.end():]
    if inner.endswith('</p>'):
        inner = inner[:-len('</p>')]
    parts = re.split(r'<br\s*/>', inner)
    out = p_open
    for i, seg in enumerate(parts):
        if i > 0:
            out += '<br/>'
        t = segs[i] if i < len(segs) else ''
        if seg.strip() == '':
            continue
        sm = re.search(r'<span\b[^>]*>', seg)
        strong = bool(re.match(r'^\s*<strong[^>]*>', seg))
        if sm:
            span_open = sm.group(0)
            if strong:
                out += '<strong>' + span_open + escape(t) + '</span></strong>'
            else:
                out += span_open + escape(t) + '</span>'
        else:
            out += escape(t)
    out += '</p>'
    return out

def apply_sub(shape_text, pairs):
    for old, new in pairs:
        eold, enew = escape(old), escape(new)
        if eold not in shape_text:
            raise ValueError("sub not found: %r" % old[:60])
        shape_text = shape_text.replace(eold, enew)
    return shape_text

all_ok = True
for page in runs:
    sid = page["slide_id"]
    if sid not in B1:
        continue
    st = slide_xml(SRC, sid)
    if st is None:
        print("SLIDE MISS", sid); all_ok = False; continue
    olds = {b["id"]: b["ps"] for b in page["blocks"]}
    parts = []
    for bid, spec in B1[sid].items():
        if bid not in olds:
            print("BLOCK MISS", sid, bid); all_ok = False; continue
        ps = olds[bid]
        sh = shape_xml(st, bid)
        if sh is None:
            print("SHAPE MISS", sid, bid); all_ok = False; continue
        try:
            if spec["mode"] == "lines":
                nseg = seg_count_for_ps(ps)
                if nseg != len(spec["lines"]):
                    raise ValueError("segment mismatch %d vs %d" % (nseg, len(spec["lines"])))
                new_sh = rebuild_ps(sh, ps, spec["lines"])
            else:
                new_sh = apply_sub(sh, spec["pairs"])
        except ValueError as e:
            print("FAIL", sid, bid, e); all_ok = False; continue
        parts.append({"action": "block_replace", "block_id": bid, "replacement": new_sh})
    if parts:
        with io.open("parts-%s.json" % sid, "w", encoding="utf-8", newline="\n") as f:
            json.dump(parts, f, ensure_ascii=False)
        print("OK", sid, len(parts), "parts")
print("ALL_OK:", all_ok)
