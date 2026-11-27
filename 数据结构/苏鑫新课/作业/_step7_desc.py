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
    r = s.get(f"{BASE}/assignment/showProcessMsg.jsp?problemID={pid}&assignID=3675",
              headers={"Referer": BASE + "/assignment/index.jsp?courseID=186&assignID=3675"}, timeout=20)
    open(f"{RAW}/desc_{pid}.html", "w", encoding="utf-8").write(r.text)
    t = re.sub(r"<script.*?</script>", "", r.text, flags=re.S)
    t = re.sub(r"<[^>]+>", " ", t)
    t = re.sub(r"\s+", " ", t)
    print(pid, r.status_code, len(r.text), "|", t[:200])
    time.sleep(0.3)
