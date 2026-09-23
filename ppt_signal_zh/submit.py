# -*- coding: utf-8 -*-
"""Generic submit: pages from argv, lint first, --no-lint only when all errors pre-exist."""
import io, os, subprocess, json, sys

os.chdir(r"D:\29469\Documents\notes\ppt_signal_zh")
PRES = "NVAAsrqRMlxzD6d6aLPcA8KUnvc"
pages = [(int(x.split(":")[0]), x.split(":")[1]) for x in sys.argv[1].split(",")]

base = json.load(io.open("source-response.json", encoding="utf-8"))
iss = base.get("data", {}).get("issues", {})
base_slides = []
for s in iss.get("slides", []):
    sig = set()
    for e in s.get("errors", []):
        sig.add((e.get("code"), tuple(sorted(e.get("elements") or []))))
    base_slides.append(sig)

def err_sig(report):
    sig = []
    for s in report.get("slides", []):
        for e in s.get("errors", []):
            sig.append((e.get("code"), sorted(e.get("elements") or [])))
    return sig

def get_report(resp_text):
    start = resp_text.find("{")
    js = json.loads(resp_text[start:])
    if js.get("ok"):
        return js, None
    msg = (js.get("error") or {}).get("message")
    try:
        rep = json.loads(msg)
    except Exception:
        rep = None
    return js, rep

def submit(sid, pf, extra):
    return subprocess.run(
        ["lark-cli", "slides", "+replace-slide", "--presentation", PRES,
         "--slide-id", sid, "--parts", "@" + pf] + extra,
        capture_output=True, text=True, encoding="utf-8")

for nidx, sid in pages:
    pf = "parts-%02d-%s.json" % (nidx, sid)
    if not os.path.exists(pf):
        print("SKIP", sid); continue
    r1 = submit(sid, pf, [])
    out1 = "stdout:\n" + r1.stdout + "\nstderr:\n" + r1.stderr
    with io.open("resp1-%s.json" % sid, "w", encoding="utf-8", newline="\n") as f:
        f.write(out1)
    payload = (r1.stderr if r1.stderr.strip() else r1.stdout)
    try:
        js, rep = get_report(payload)
    except Exception:
        print(sid, "PARSE FAIL", payload[:200]); continue
    if js.get("ok"):
        print(sid, "OK first try, rev=", (js.get("data") or {}).get("revision_id"))
        continue
    code = (js.get("error") or {}).get("code")
    if code != 4000153 or rep is None:
        print(sid, "FAIL non-lint:", code, payload[:200]); continue
    sigs = err_sig(rep)
    template_ids = {"bei", "beC", "bew"}
    new_issues = []
    for c, elems in sigs:
        if elems and all(e in template_ids for e in elems):
            continue
        found = any((c, tuple(elems)) in bs for bs in base_slides)
        if not found:
            new_issues.append((c, elems))
    if new_issues:
        print(sid, "HAS NEW ISSUES:", new_issues)
        continue
    r2 = submit(sid, pf, ["--no-lint"])
    out2 = "stdout:\n" + r2.stdout + "\nstderr:\n" + r2.stderr
    with io.open("resp2-%s.json" % sid, "w", encoding="utf-8", newline="\n") as f:
        f.write(out2)
    payload2 = (r2.stderr if r2.stderr.strip() else r2.stdout)
    try:
        js2 = json.loads(payload2[payload2.find("{"):])
    except Exception:
        js2 = None
    if js2 and js2.get("ok"):
        print(sid, "OK via no-lint (preexisting only), rev=", (js2.get("data") or {}).get("revision_id"))
    else:
        print(sid, "no-lint failed:", (payload2 or "")[:300])
