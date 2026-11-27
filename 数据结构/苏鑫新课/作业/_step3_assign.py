import requests, json, re, time

BASE = "http://115.156.107.145"
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36"}
DIR = r"D:/29469/Documents/notes/数据结构/苏鑫新课/作业"

s = requests.Session()
s.headers.update(UA)
s.cookies.update(json.load(open(DIR + "/_cookies.json")))

def get(url, **kw):
    r = s.get(url, headers={"Referer": BASE + "/"}, timeout=15, **kw)
    return r

# assignment page
r = get(BASE + "/assignment/index.jsp?assignID=3675")
print("assign page:", r.status_code, len(r.text))
html = r.text
open(DIR + "/_assign3675.html", "w", encoding="utf-8").write(html)

# strip tags for quick view
text = re.sub(r"<script.*?</script>", "", html, flags=re.S)
text = re.sub(r"<style.*?</style>", "", text, flags=re.S)
text = re.sub(r"<[^>]+>", " ", text)
text = re.sub(r"\s+", " ", text)
print(text[:3000])

# find problemIDs referenced
ids = re.findall(r"problemID=(\d+)", html)
print("problemIDs:", sorted(set(ids)))
