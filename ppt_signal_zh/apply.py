# -*- coding: utf-8 -*-
"""Generic: read translations JSON (same schema as B1), emit parts-<sid>.json."""
import io, os, re, json, sys
from xml.sax.saxutils import escape as sax_escape

os.chdir(r"D:\29469\Documents\notes\ppt_signal_zh")
SRC = io.open("source.xml", encoding="utf-8").read()
TR = json.load(io.open(sys.argv[1], encoding="utf-8"))

def escape(s):
    return sax_escape(s).replace('"', "&quot;").replace("'", "&apos;")

runs = json.load(io.open("runs.json", encoding="utf-8"))

def slide_xml(text, sid):
    m = re.search(r'<slide\b[^>]*\bid="%s"[^>]*>.*?</slide>' % re.escape(sid), text, re.S)
    return m.group(0) if m else None

def shape_xml(slide_text, bid):
    m = re.search(r'<shape\b[^>]*\bid="%s"[^>]*/>|<shape\b[^>]*\bid="%s"[^>]*>.*?</shape>' % (re.escape(bid), re.escape(bid)), slide_text, re.S)
    return m.group(0) if m else None

def seg_count_for_ps(ps):
    n = 0
    for ps_runs in ps:
        seg = 1
        for x in ps_runs:
            if x["tag"] == "br":
                seg += 1
        n += seg
    return n

def rebuild_ps(shape_text, ps, new_lines, fontsize=None):
    p_pat = re.compile(r'<p\b[^>]*/>|<p\b[^>]*>.*?</p>', re.S)
    pm = list(p_pat.finditer(shape_text))
    if len(pm) != len(ps):
        raise ValueError("p count mismatch: %d vs %d" % (len(pm), len(ps)))
    counts = []
    for ps_runs in ps:
        c = 1
        for x in ps_runs:
            if x["tag"] == "br":
                c += 1
        counts.append(c)
    segs_by_p = []
    idx = 0
    for c in counts:
        segs_by_p.append(new_lines[idx:idx + c])
        idx += c
    for pi in range(len(ps) - 1, -1, -1):
        m = pm[pi]
        new_p = rebuild_p(m.group(0), segs_by_p[pi], fontsize)
        out = shape_text[:m.start()] + new_p + shape_text[m.end():]
        shape_text = out
    return shape_text

def rebuild_p(p_xml, segs, fontsize=None):
    sm = re.match(r'<p\b[^>]*/>', p_xml)
    if sm:
        return sm.group(0)[:-2] + '></p>'
    m = re.match(r'<p\b[^>]*>', p_xml)
    p_open = m.group(0)
    inner = p_xml[m.end():]
    if inner.endswith('</p>'):
        inner = inner[:-len('</p>')]
    parts = re.split(r'<br\s*/>', inner)
    out = p_open
    for i, seg in enumerate(parts):
        if i > 0:
            out += '<br/>'
        t = segs[i] if i < len(segs) else ''
        if seg.strip() == '':
            continue
        sm2 = re.search(r'<span\b[^>]*>', seg)
        strong = bool(re.match(r'^\s*<strong[^>]*>', seg))
        if sm2:
            span_open = sm2.group(0)
            if fontsize:
                span_open = re.sub(r'fontSize="[^"]*"', 'fontSize="%s"' % fontsize, span_open)
            if strong:
                out += '<strong>' + span_open + escape(t) + '</span></strong>'
            else:
                out += span_open + escape(t) + '</span>'
        else:
            out += escape(t)
    out += '</p>'
    return out

def apply_sub(shape_text, pairs):
    for old, new in pairs:
        eold, enew = escape(old), escape(new)
        if eold not in shape_text:
            raise ValueError("sub not found: %r" % old[:60])
        shape_text = shape_text.replace(eold, enew)
    return shape_text

all_ok = True
for idx, page in enumerate(runs):
    sid = page["slide_id"]
    if sid not in TR:
        continue
    st = slide_xml(SRC, sid)
    if st is None:
        print("SLIDE MISS", sid); all_ok = False; continue
    olds = {b["id"]: b["ps"] for b in page["blocks"]}
    parts = []
    for bid, spec in TR[sid].items():
        if bid not in olds:
            print("BLOCK MISS", sid, bid); all_ok = False; continue
        ps = olds[bid]
        sh = shape_xml(st, bid)
        if sh is None:
            print("SHAPE MISS", sid, bid); all_ok = False; continue
        try:
            if spec["mode"] == "lines":
                nseg = seg_count_for_ps(ps)
                if nseg != len(spec["lines"]):
                    raise ValueError("segment mismatch %d vs %d" % (nseg, len(spec["lines"])))
                new_sh = rebuild_ps(sh, ps, spec["lines"], spec.get("fontSize"))
            else:
                new_sh = apply_sub(sh, spec["pairs"])
        except ValueError as e:
            print("FAIL", sid, bid, e); all_ok = False; continue
        parts.append({"action": "block_replace", "block_id": bid, "replacement": new_sh})
    if parts:
        with io.open("parts-%02d-%s.json" % (idx + 1, sid), "w", encoding="utf-8", newline="\n") as f:
            json.dump(parts, f, ensure_ascii=False)
        print("OK", sid, len(parts), "parts")
print("ALL_OK:", all_ok)
