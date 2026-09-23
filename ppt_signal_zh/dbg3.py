# -*- coding: utf-8 -*-
import io, re
t = io.open(r"D:\29469\Documents\notes\ppt_signal_zh\readback.xml", encoding="utf-8").read()
m = re.search(r'<slide\b[^>]*\bid="pVP"[^>]*>.*?</slide>', t, re.S)
st = m.group(0)
for td in re.finditer(r'<td\b[^>]*>.*?</td>', st, re.S):
    x = td.group(0)
    tid = re.search(r'\bid="([^"]+)"', x)
    texts = re.findall(r'<span\b[^>]*>([^<]*)</span>', x)
    print(tid.group(1) if tid else "?", "|", texts)
