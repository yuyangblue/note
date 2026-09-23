# -*- coding: utf-8 -*-
import io, re
SRC = io.open(r"D:\29469\Documents\notes\ppt_signal_zh\source.xml", encoding="utf-8").read()
m = re.search(r'<slide\b[^>]*\bid="pVf"[^>]*>.*?</slide>', SRC, re.S)
st = m.group(0)
shm = re.search(r'<shape\b[^>]*\bid="beG"[^>]*>.*?</shape>', st, re.S)
sh = shm.group(0)
old = '"%s: Command not found.\\n"'
eold = old  # no escape needed: only & < > are escaped
print("old repr:", repr(old))
print("in shape:", eold in sh)
i = sh.find("Command")
print("ctx:", repr(sh[i-100:i+120]))
