import requests, json, time, re

BASE = "http://115.156.107.145"
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36"}
DIR = r"D:/29469/Documents/notes/数据结构/苏鑫新课/作业"
RAW = DIR + "/_raw"

s = requests.Session()
s.headers.update(UA)
s.cookies.update(json.load(open(DIR + "/_cookies.json")))

pids = {"26884": "prog_1", "26883": "prog_2", "26882": "prog_3", "25837": "prog_4", "25167": "prog_5"}
for pid, tag in pids.items():
    h = open(f"{RAW}/{tag}.html", encoding="utf-8").read()
    m = re.search(r"cgRenderMarkdown\('([^']+)'", h)
    if not m:
        print(pid, "no key"); continue
    key = m.group(1)
    r = s.get(f"{BASE}/downMarkdown?mkdoc={key}",
              headers={"Referer": BASE + "/assignment/index.jsp?courseID=186&assignID=3675"}, timeout=20)
    body = r.text
    open(f"{RAW}/md_{pid}.md", "w", encoding="utf-8").write(body)
    print(pid, r.status_code, len(body), "|", body[:120].replace("\n", " "))
    time.sleep(0.3)
