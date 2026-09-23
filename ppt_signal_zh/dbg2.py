# -*- coding: utf-8 -*-
import io, re
t = io.open(r"D:\29469\Documents\notes\ppt_signal_zh\source.xml", encoding="utf-8").read()
m = re.search(r'<slide\b[^>]*\bid="pVb"[^>]*>.*?</slide>', t, re.S)
st = m.group(0)
for bid in ("bFc", "bFr", "bFN", "bFO", "bFl", "bFH"):
    sm = re.search(r'<shape\b[^>]*\bid="%s"[^>]*>.*?</shape>' % bid, st, re.S)
    if sm:
        x = sm.group(0)
        w = re.search(r'width="([\d.]+)"', x).group(1)
        fs = set(re.findall(r'fontSize="([\d.]+)"', x))
        print(bid, "width=", w, "fontSizes=", fs)
