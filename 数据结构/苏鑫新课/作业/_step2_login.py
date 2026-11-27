import requests, json, base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

BASE = "http://115.156.107.145"
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36"}
DIR = r"D:/29469/Documents/notes/数据结构/苏鑫新课/作业"

STID = "2025302191016"
PWD = STID  # 先按 账号=密码=学号 试
CAPTCHA = "sRaTn"

def enc(p):
    c = AES.new(b"Client8Sess!06ID", AES.MODE_ECB)
    return base64.b64encode(c.encrypt(pad(p.encode(), 16))).decode()

s = requests.Session()
s.headers.update(UA)
cookies = json.load(open(DIR + "/_cookies.json"))
s.cookies.update(cookies)

data = {
    "IndexStyle": "1",
    "stid": STID,
    "pwd": enc(PWD),
    "captchaCode": CAPTCHA,
}
r = s.post(BASE + "/login/loginproc.jsp", data=data,
           headers={"Referer": BASE + "/indexcs/simple.jsp"}, timeout=15, allow_redirects=True)
print("login POST:", r.status_code, "final url:", r.url)
body = r.text
print("len:", len(body))
for marker in ["学生登录", "loginErr", "密码", "验证码", "作业", "main.jsp", "欢迎"]:
    if marker in body:
        print("contains:", marker)

# follow-up: try main page
r2 = s.get(BASE + "/main.jsp", headers={"Referer": BASE + "/"}, timeout=15)
print("main.jsp:", r2.status_code, len(r2.text), "login" if "学生登录" in r2.text else "maybe-ok")
with open(DIR + "/_cookies.json", "w") as f:
    json.dump(s.cookies.get_dict(), f)
open(DIR + "/_main.html", "w", encoding="utf-8").write(r2.text)
