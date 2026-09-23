# -*- coding: utf-8 -*-
"""Generate td block_replace parts for pVP signal table from readback.xml."""
import io, re, json

t = io.open(r"D:\29469\Documents\notes\ppt_signal_zh\readback.xml", encoding="utf-8").read()
m = re.search(r'<slide\b[^>]*\bid="pVP"[^>]*>.*?</slide>', t, re.S)
st = m.group(0)

TR = {
    "bwS": "编号", "bwn": "名称", "bwZ": "默认动作", "bwB": "对应事件",
    "bwq": "终止", "bwx": "用户键入 ctrl-c",
    "bwK": "终止", "bwP": "终止程序（无法覆盖或忽略）",
    "bwz": "终止", "bwQ": "段违规",
    "bwp": "终止", "bwr": "定时器信号",
    "bwW": "忽略", "bwd": "子进程停止或终止",
}

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;").replace("'", "&apos;")

parts = []
for td in re.finditer(r'<td\b[^>]*>.*?</td>', st, re.S):
    x = td.group(0)
    tidm = re.search(r'\bid="([^"]+)"', x)
    if not tidm:
        continue
    tid = tidm.group(1)
    if tid not in TR:
        continue
    new_txt = TR[tid]
    # rebuild td: keep opening tag, replace span text with translated
    # find first span open and content
    sm = re.search(r'(<td\b[^>]*>)(.*)(</td>)', x, re.S)
    open_tag, inner, close_tag = sm.group(1), sm.group(2), sm.group(3)
    # inside inner: <content><p><span ...>TEXT</span></p></content>
    def repl_span(mm):
        return mm.group(1) + esc(new_txt) + mm.group(2)
    new_inner = re.sub(r'(<span\b[^>]*>)([^<]*)(</span>)', repl_span, inner, count=1)
    parts.append({"action": "block_replace", "block_id": tid, "replacement": open_tag + new_inner + close_tag})

with io.open(r"D:\29469\Documents\notes\ppt_signal_zh\parts-pVP-td.json", "w", encoding="utf-8", newline="\n") as f:
    json.dump(parts, f, ensure_ascii=False)
print("parts:", len(parts))
for p in parts:
    print(p["block_id"], p["replacement"][:120])
