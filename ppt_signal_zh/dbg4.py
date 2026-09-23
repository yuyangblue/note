# -*- coding: utf-8 -*-
import io, re, xml.etree.ElementTree as ET

t = io.open(r"D:\29469\Documents\notes\ppt_signal_zh\readback.xml", encoding="utf-8").read()
m = re.search(r'<slide\b[^>]*\bid="pVP"[^>]*>.*?</slide>', t, re.S)
st = m.group(0)
slide_el = ET.fromstring(st)
tags = {}
for el in slide_el.iter():
    tags[el.tag] = tags.get(el.tag, 0) + 1
for k in sorted(tags):
    print(k, tags[k])
