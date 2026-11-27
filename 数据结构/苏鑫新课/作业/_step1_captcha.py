import requests, sys, io

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36"}
BASE = "http://115.156.107.145"

s = requests.Session()
s.headers.update(UA)

# 1. login page -> session cookie
r = s.get(BASE + "/indexcs/simple.jsp", headers={"Referer": BASE + "/"}, timeout=15)
print("login page:", r.status_code, len(r.text), "student-login" if "学生登录" in r.text else "?")
open(r"D:/29469/Documents/notes/数据结构/苏鑫新课/作业/_login_page.html", "w", encoding="utf-8").write(r.text)

# 2. captcha image (same session)
r2 = s.get(BASE + "/cgjiaoyan", headers={"Referer": BASE + "/indexcs/simple.jsp"}, timeout=15)
print("captcha:", r2.status_code, r2.headers.get("Content-Type"), len(r2.content))
open(r"D:/29469/Documents/notes/数据结构/苏鑫新课/作业/_captcha.png", "wb").write(r2.content)

# save cookies for next step
import json
with open(r"D:/29469/Documents/notes/数据结构/苏鑫新课/作业/_cookies.json", "w") as f:
    json.dump(s.cookies.get_dict(), f)
print("cookies:", s.cookies.get_dict())
