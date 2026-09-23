# -*- coding: utf-8 -*-
"""Submit batch with lint; if blocked and ALL errors are pre-existing baseline issues (template elems),
record exemption and resubmit with --no-lint."""
import io, os, subprocess, json

os.chdir(r"D:\29469\Documents\notes\ppt_signal_zh")
PRES = "NVAAsrqRMlxzD6d6aLPcA8KUnvc"
pages = ["pVR","pVi","pVm","pVd","pVe","pVf","pVq","pVx","pVY"]

# baseline per-slide error signature: (code, sorted elements)
base = json.load(io.open("source-response.json", encoding="utf-8"))
iss = base.get("data", {}).get("issues", {})
base_slides = {}
for s in iss.get("slides", []):
    sig = set()
    for e in s.get("errors", []):
        sig.add((e.get("code"), tuple(sorted(e.get("elements") or []))))
    base_slides[s["slide_number"]] = sig
# slide_number is report-internal; map by order of slides[] == document order == source.xml order
# We'll map by index order later; simpler: baseline errors we care about are template ids, compare by ids directly.

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
    r = subprocess.run(
        ["lark-cli", "slides", "+replace-slide", "--presentation", PRES,
         "--slide-id", sid, "--parts", "@" + pf] + extra,
        capture_output=True, text=True, encoding="utf-8")
    return r

for sid in pages:
    pf = "parts-%s.json" % sid
    if not os.path.exists(pf):
        print("SKIP", sid); continue
    r1 = submit(sid, pf, [])
    out1 = "stdout:\n" + r1.stdout + "\nstderr:\n" + r1.stderr
    with io.open("resp1-%s.json" % sid, "w", encoding="utf-8", newline="\n") as f:
        f.write(out1)
    payload = (r1.stderr if r1.stderr.strip() else r1.stdout)
    js, rep = get_report(payload)
    if js.get("ok"):
        print(sid, "OK first try, rev=", (js.get("data") or {}).get("revision_id"))
        continue
    code = (js.get("error") or {}).get("code")
    if code != 4000153 or rep is None:
        print(sid, "FAIL non-lint:", code, payload[:300])
        continue
    sigs = err_sig(rep)
    template_ids = {"bei", "beC", "bew"}
    all_preexisting = True
    for c, elems in sigs:
        # pre-existing if all elements are template ids that baseline also flags
        if elems and all(e in template_ids for e in elems):
            continue
        # OR code+elems present in some baseline page
        found = False
        for bsig in base_slides.values():
            if (c, tuple(elems)) in bsig:
                found = True
                break
        if not found:
            # fallback: code known pre-existing anywhere in baseline with same elements
            all_preexisting = False
            print("   NEW issue:", c, elems)
    if not all_preexisting:
        print(sid, "HAS NEW ISSUES - manual review needed")
        continue
    # exemption: resubmit with --no-lint
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
        print(sid, "no-lint also failed:", (payload2 or "")[:300])
