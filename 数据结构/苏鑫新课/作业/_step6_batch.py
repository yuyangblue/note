import requests, json, re, time, os

BASE = "http://115.156.107.145"
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36"}
DIR = r"D:/29469/Documents/notes/数据结构/苏鑫新课/作业"
RAW = os.path.join(DIR, "_raw")
os.makedirs(RAW, exist_ok=True)
AID = 3675

s = requests.Session()
s.headers.update(UA)
s.cookies.update(json.load(open(DIR + "/_cookies.json")))

def get(url, referer=None):
    h = {"Referer": referer or (BASE + f"/assignment/index.jsp?courseID=186&assignID={AID}")}
    r = s.get(url, headers=h, timeout=20)
    return r

sections = [
    ("multi", "optionList", range(1, 7)),
    ("cloze", "clozeList", range(1, 3)),
    ("brief", "briefAnswerList", range(1, 4)),
    ("prog", "programList", range(1, 6)),
]

problem_ids = {}
for tag, page, rng in sections:
    for n in rng:
        url = f"{BASE}/assignment/{page}.jsp?proNum={n}&assignID={AID}"
        r = get(url)
        fn = f"{RAW}/{tag}_{n}.html"
        open(fn, "w", encoding="utf-8").write(r.text)
        pids = re.findall(r"problemID=(\d+)", r.text)
        problem_ids[f"{tag}_{n}"] = sorted(set(pids))
        print(tag, n, r.status_code, len(r.text), "pids:", sorted(set(pids)))
        time.sleep(0.3)

json.dump(problem_ids, open(RAW + "/problem_ids.json", "w"))

# fetch problemContent for each unique problemID
allpids = sorted({p for v in problem_ids.values() for p in v}, key=int)
print("all pids:", allpids)
for pid in allpids:
    r = get(f"{BASE}/assignment/problemContent.jsp?problemID={pid}")
    open(f"{RAW}/content_{pid}.html", "w", encoding="utf-8").write(r.text)
    print("content", pid, r.status_code, len(r.text))
    time.sleep(0.3)
