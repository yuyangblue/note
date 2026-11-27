import requests, json, re

BASE = "http://115.156.107.145"
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36"}
DIR = r"D:/29469/Documents/notes/数据结构/苏鑫新课/作业"

s = requests.Session()
s.headers.update(UA)
s.cookies.update(json.load(open(DIR + "/_cookies.json")))

def get(url, referer=BASE + "/"):
    r = s.get(url, headers={"Referer":referer}, timeout=15)
    return r

r = get(BASE + "/includes/redirect.jsp?tab=-2")
print("tab -2:", r.status_code, len(r.text))
open(DIR + "/_assignlist.html", "w", encoding="utf-8").write(r.text)

# all assignment links
links = re.findall(r'href="([^"]*assignID[^"]*)"', r.text)
for l in sorted(set(links)):
    print(l)

# also course list page: choose course 数据结构与算法
r2 = get(BASE + "/courselist.jsp?urid=10564")
m = re.findall(r'href="([^"]*course[^"]*)"[^>]*>([^<]*数据结构[^<]*)', r2.text)
print("course match:", m)
for mm in re.findall(r'<a[^>]+href="([^"]+)"[^>]*>\s*数据结构[^<]*', r2.text):
    print("course link:", mm)
