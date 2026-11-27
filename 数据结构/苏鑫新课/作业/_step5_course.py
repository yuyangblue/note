import requests, json, re

BASE = "http://115.156.107.145"
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36"}
DIR = r"D:/29469/Documents/notes/数据结构/苏鑫新课/作业"

s = requests.Session()
s.headers.update(UA)
s.cookies.update(json.load(open(DIR + "/_cookies.json")))

def get(url, referer=BASE + "/"):
    r = s.get(url, headers={"Referer": referer}, timeout=15)
    return r

# select course first (sets session course context)
r = get(BASE + "/courselist.jsp?courseID=186", referer=BASE + "/courselist.jsp?urid=10564")
print("select course:", r.status_code, len(r.text))

# assignment list for course 186
r = get(BASE + "/includes/redirect.jsp?tab=-2", referer=BASE + "/main.jsp")
open(DIR + "/_assignlist.html", "w", encoding="utf-8").write(r.text)
links = sorted(set(re.findall(r'(?:href=")?[^"\']*assignID=(\d+)[^"\']*', r.text)))
print("assignIDs on list:", links)
for m in re.findall(r'<a[^>]+href="([^"]*assignID=\d+[^"]*)"[^>]*>(.*?)</a>', r.text, re.S):
    txt = re.sub(r'<[^>]+>', ' ', m[1])
    txt = re.sub(r'\s+', ' ', txt).strip()
    print(m[0], '->', txt[:60])

# the target assignment page
r = get(BASE + "/assignment/index.jsp?courseID=186&assignID=3675", referer=BASE + "/includes/redirect.jsp?tab=-2")
print("assign3675:", r.status_code, len(r.text))
open(DIR + "/_assign3675.html", "w", encoding="utf-8").write(r.text)
t = re.sub(r'<script.*?</script>', '', r.text, flags=re.S)
t = re.sub(r'<[^>]+>', ' ', t)
t = re.sub(r'\s+', ' ', t)
print(t[:1500])
print('PIDS:', sorted(set(re.findall(r'problemID=(\d+)', r.text))))
