# -*- coding: utf-8 -*-
"""Build the Surgery OSCE study guide: SVG -> PNG, images.json, HTML -> PDF, page previews.

usage: python3 src/build.py [--no-render] [--pages]
"""
import json, os, re, subprocess, sys, html, urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "src")
sys.path.insert(0, SRC)
from checklists_a import TOPICS_A
from checklists_b import TOPICS_B
from checklists_c import TOPICS_C

TOPICS = TOPICS_A + TOPICS_B + TOPICS_C
from checklists_notes import NOTES, KEEP_STD


def merge_notes(t):
    """Checklists from the lecture notes replace the standard ones; uncovered standard ones stay, labelled."""
    old = t["checklists"]
    std = [(re.sub(r"^[A-Z]\. ", "", old[i][0]), old[i][1], "std") for i in KEEP_STD.get(t["id"], range(len(old)))]
    notes = [(c[0], c[1], "notes") for c in NOTES.get(t["id"], [])]
    hist = [c for c in std if "istory" in c[0]]
    rest = [c for c in std if "istory" not in c[0]]
    allc = hist + notes + rest
    t["checklists"] = [(f"{chr(65 + i)}. {c[0]}", c[1], c[2]) for i, c in enumerate(allc)]


for _t in TOPICS:
    merge_notes(_t)
IMG_DIR = os.path.join(ROOT, "images")
SVG_DIR = os.path.join(SRC, "svg")
BUILD = os.path.join(ROOT, "build")
PDF = os.path.join(ROOT, "Surgery_OSCE_Study_Guide.pdf")

STYLE = ("Clean digital medical line-art illustration for an OSCE clinical-skills textbook. "
         "Dark-brown outlines of varying thickness, flat skin colour with soft cel shading. "
         "Patient in a light-blue hospital gown on a dark-blue examination couch; examiner shown only as hands in "
         "light-blue nitrile gloves with white coat sleeves. Plain white background. Modest and professional, "
         "intimate areas covered or not shown. Anatomically accurate hands and body. No text, letters, labels or arrows.")


def strip(s):
    return html.unescape(re.sub("<[^>]+>", "", s))


# ---------------------------------------------------------------- images
def render_svgs():
    os.makedirs(IMG_DIR, exist_ok=True)
    todo = []
    for f in sorted(os.listdir(SVG_DIR)):
        if not f.endswith(".svg"):
            continue
        s, p = os.path.join(SVG_DIR, f), os.path.join(IMG_DIR, f[:-4] + ".png")
        if not os.path.exists(p) or os.path.getmtime(p) < os.path.getmtime(s):
            todo.append(s)
    if todo:
        subprocess.run(["node", os.path.join(SRC, "render_svg.js"), IMG_DIR, "2", *todo], check=True)


def topic_figures(t):
    """(image id, caption) for every checklist item that has an illustration, in order."""
    out = []
    for ck in t["checklists"]:
        for _, _, items in ck[1]:
            for it in items:
                if len(it) > 2 and it[2]:
                    out.append((it[2], f"{it[0]} — {it[1]}"))
    return out


def write_catalog():
    items = []
    for t in TOPICS:
        for img, cap in topic_figures(t):
            items.append(dict(id=img, topic=t["num"], kind="step", caption=strip(cap),
                              prompt=f"{STYLE} Scene: {strip(cap)}"))
        m = t["map"]
        items.append(dict(id=m["img"], topic=t["num"], kind="inspection-map", caption=strip(m["title"]),
                          prompt=f"{STYLE} Scene: {strip(m['title'])}; clear view of the whole area so numbered markers can be "
                                 f"added later at: " + "; ".join(strip(r[0]) for r in m["rows"]) + "."))
    for it in items:
        it["file"] = f"images/{it['id']}.png"
        it["status"] = "drawn" if os.path.exists(os.path.join(IMG_DIR, it["id"] + ".png")) else "pending"
    with open(os.path.join(ROOT, "images.json"), "w", encoding="utf-8") as f:
        json.dump(items, f, ensure_ascii=False, indent=2)
    return {i["id"]: i for i in items}


# ---------------------------------------------------------------- HTML
def esc_attr(s):
    return html.escape(s, quote=True)


def figure(img_id, caption, label, catalog, markers=None, cls="fig"):
    have = catalog.get(img_id, {}).get("status") == "drawn"
    if have:
        mk = ""
        for n, x, y in (markers or []):
            mk += f'<span class="mk" style="left:{x}%;top:{y}%">{n}</span>'
        inner = f'<div class="imgwrap"><img src="images/{img_id}.png" alt="{esc_attr(strip(caption))}">{mk}</div>'
    else:
        inner = (f'<div class="ph"><div class="ph-in"><b>Illustration pending</b>'
                 f'<span>{img_id}</span><small>drawn after the style of the first 3 images is approved</small></div></div>')
    return f'<figure class="{cls}">{inner}<figcaption><b>{label}</b> {caption}</figcaption></figure>'


def table_html(tb):
    n = len(tb["rows"])
    cls = "tbl keep" if n <= 12 else "tbl"
    h = "".join(f"<th>{c}</th>" for c in tb["head"])
    rows = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in tb["rows"])
    note = f'<p class="note">{tb["note"]}</p>' if tb.get("note") else ""
    return (f'<div class="{cls}"><h4>{tb["title"]}</h4><table><thead><tr>{h}</tr></thead>'
            f'<tbody>{rows}</tbody></table>{note}</div>')


def topic_html(t, catalog):
    n = t["num"]
    out = [f'<section class="topic" id="t{n}">',
           f'<header class="thead"><div class="kicker">TOPIC {n:02d}</div><h1>{t["title"]}</h1>'
           f'<p class="sub">{t["subtitle"]}</p></header>',
           f'<div class="ar-box" dir="rtl" lang="ar"><div class="ar-h">ملخص سريع</div><p>{t["ar"]}</p></div>',
           '<h2><span>1</span>OSCE checklist</h2>']
    figno = 0
    cols = ('<colgroup><col class="c-n"><col class="c-s"><col class="c-h"><col class="c-b"><col class="c-b"><col class="c-b"></colgroup>')
    for ck in t["checklists"]:
        ctitle, phases = ck[0], ck[1]
        src = ck[2] if len(ck) > 2 else "std"
        tag = ('<span class="src notes">from your lecture notes</span>' if src == "notes"
               else '<span class="src std">standard version — not in your notes</span>')
        out.append(f'<div class="ck {src}"><h3 class="ck-t">{ctitle} {tag}</h3>')
        step = 0
        for pi, (phase, pnote, items) in enumerate(phases):
            count = "" if phase in ("HELP", "End of station") or len(items) < 2 else f' <em>{len(items)} things</em>'
            pn = f' <span class="pnote">· {pnote}</span>' if pnote else ""
            rows, figs = "", []
            for it in items:
                step += 1
                ref = ""
                if len(it) > 2 and it[2]:
                    figno += 1
                    figs.append((it[2], it[0], it[1], step, figno))
                    ref = f' <span class="figref">→ Fig {n}.{figno}</span>'
                rows += (f'<tr><td class="num">{step}</td><td class="st">{it[0]}</td><td class="how">{it[1]}{ref}</td>'
                         f'<td class="bx"><span></span></td><td class="bx"><span></span></td><td class="bx"><span></span></td></tr>')
            head = ('<thead><tr><th>#</th><th>Step</th><th>How / what you may find</th><th>P</th><th>MP</th><th>F</th></tr></thead>'
                    if pi == 0 else "")
            cls = "phase-block" + (" end" if phase == "End of station" else "") + (" help" if phase == "HELP" else "")
            out.append(f'<div class="{cls}"><table class="cktbl">{cols}{head}<tbody>'
                       f'<tr class="phase"><td colspan="6">{phase}{count}{pn}</td></tr>{rows}</tbody></table>')
            if figs:
                out.append('<div class="figrow">')
                for img, st, how, sn, fn in figs:
                    out.append(figure(img, f"<b>{st}</b> — {how}", f"Fig {n}.{fn} · step {sn}", catalog))
                out.append('</div>')
            out.append('</div>')
        out.append('</div>')
    # inspection map
    m = t["map"]
    wide = False
    pth = os.path.join(IMG_DIR, m["img"] + ".png")
    if os.path.exists(pth):
        from PIL import Image
        w, h = Image.open(pth).size
        wide = w > h * 1.1
    rows = "".join(f'<tr><td class="num"><span class="mk-s">{i}</span></td><td>{w}</td><td>{f}</td></tr>'
                   for i, (w, f) in enumerate(m["rows"], 1))
    out.append(f'<div class="mapblock"><h2><span>2</span>Inspection map</h2><div class="map{" wide" if wide else ""}">'
               f'{figure(m["img"], m["title"], "Map", catalog, m["markers"], "fig mapfig")}'
               f'<table class="maptbl"><thead><tr><th>#</th><th>Where to look</th><th>What you may find</th></tr></thead>'
               f'<tbody>{rows}</tbody></table></div></div>')
    out.append('<h2><span>3</span>Key tables</h2>')
    out += [table_html(tb) for tb in t["tables"]]
    lis = " · ".join(f'<a href="https://www.youtube.com/results?search_query={urllib.parse.quote_plus(q)}">▶ {lab}</a>'
                     for lab, q in t["links"])
    out.append(f'<div class="links1"><b>Videos (YouTube search):</b> {lis}</div>')
    out.append('</section>')
    return "\n".join(out)


def page_html(catalog, pages=None):
    css = open(os.path.join(SRC, "style.css"), encoding="utf-8").read()
    toc = ""
    for t in TOPICS:
        pg = pages.get(t["num"], "") if pages else ""
        toc += (f'<li><a href="#t{t["num"]}"><span class="tn">{t["num"]}</span><span class="tt">{t["title"]}'
                f'<small>{t["subtitle"]}</small></span><span class="dots"></span><span class="pg">{pg}</span></a></li>')
    cover_img = "pvd_popliteal_pulse"
    cover = (f'<section class="cover"><div class="cv-band"></div><div class="cv-in">'
             f'<div class="cv-k">Surgery · Clinical Skills</div><h1>OSCE Study Guide</h1>'
             f'<p class="cv-s">One marking-order checklist per station, with drawings, inspection maps and must-know tables — 9 syllabus topics</p>'
             f'<p class="cv-ar" dir="rtl" lang="ar">دليل المذاكرة لامتحان المهارات الإكلينيكية – الجراحة</p>'
             f'<img class="cv-img" src="images/{cover_img}.png" alt="">'
             f'<ol class="cv-list">' + "".join(f"<li>{t['title']}</li>" for t in TOPICS) + '</ol></div></section>')
    tocs = (f'<section class="toc"><h1>Contents</h1><ol>{toc}</ol>'
            f'<div class="howto"><h3>How every topic is organised</h3><ol>'
            f'<li><b>ملخص</b> – short Arabic summary</li>'
            f'<li><b>OSCE checklist</b> – the station in the order your doctors taught it. Each phase says how many things to do; '
            f'each step says how and what you may find; the drawings sit right under the phase they show. Tick P / MP / F while you practise. '
            f'<span class="src notes">from your lecture notes</span> = written only from what the doctor said · '
            f'<span class="src std">standard version</span> = topic not covered in your notes.</li>'
            f'<li><b>Inspection map</b> – numbered red markers + table</li><li><b>Key tables</b> – only the must-know ones</li></ol>'
            f'<p class="note">HELP = Hello (introduction &amp; consent) · Exposure · Lighting · Position (and ask about pain), then wash hands. '
            f'P = performed · MP = partially performed · F = failed.</p></div></section>')
    body = cover + tocs + "\n".join(topic_html(t, catalog) for t in TOPICS)
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Surgery OSCE Study Guide</title>'
            f'<style>{css}</style></head><body>{body}</body></html>')


# ---------------------------------------------------------------- PDF
FOOTER = ('<div style="width:100%;font-family:Inter,Arial,sans-serif;font-size:7.5px;color:#6b7a8c;'
          'padding:0 13mm;display:flex;justify-content:space-between">'
          '<span>Surgery Clinical Skills · OSCE Study Guide</span>'
          '<span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>')


def to_pdf(html_path, pdf_path):
    js = f"""
const {{ chromium }} = require('playwright');
(async () => {{
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto('file://{html_path}', {{ waitUntil: 'networkidle' }});
  await p.evaluate(() => document.fonts.ready);
  await p.pdf({{ path: '{pdf_path}', format: 'A4', printBackground: true, preferCSSPageSize: true,
    displayHeaderFooter: true, headerTemplate: '<span></span>', footerTemplate: {json.dumps(FOOTER)},
    margin: {{ top: '13mm', bottom: '15mm', left: '13mm', right: '13mm' }} }});
  await b.close();
}})();"""
    jsf = os.path.join(BUILD, "_pdf.js")
    open(jsf, "w").write(js)
    subprocess.run(["node", jsf], check=True)


def topic_pages(pdf_path):
    n = int(re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", pdf_path], capture_output=True, text=True).stdout).group(1))
    pages = {}
    for i in range(1, n + 1):
        txt = subprocess.run(["pdftotext", "-f", str(i), "-l", str(i), pdf_path, "-"], capture_output=True, text=True).stdout
        for m in re.finditer(r"T\s*O\s*P\s*I\s*C\s+(\d)\s*(\d)", txt.replace("\u200b", "")):
            pages.setdefault(int(m.group(1) + m.group(2)), i)
    return pages, n


def main():
    os.makedirs(BUILD, exist_ok=True)
    if "--no-render" not in sys.argv:
        render_svgs()
    catalog = write_catalog()
    html_path = os.path.join(ROOT, "Surgery_OSCE_Study_Guide.html")
    open(html_path, "w", encoding="utf-8").write(page_html(catalog))
    to_pdf(html_path, PDF)
    pages, n = topic_pages(PDF)
    open(html_path, "w", encoding="utf-8").write(page_html(catalog, pages))
    to_pdf(html_path, PDF)
    pages2, n = topic_pages(PDF)
    if pages2 != pages:
        print("warning: TOC page numbers shifted", pages, pages2)
    print(f"PDF: {PDF} ({n} pages); topic pages: {pages2}")
    drawn = sum(1 for v in catalog.values() if v["status"] == "drawn")
    print(f"images drawn: {drawn}/{len(catalog)}")
    if "--pages" in sys.argv:
        out = os.path.join(BUILD, "pages")
        os.makedirs(out, exist_ok=True)
        for f in os.listdir(out):
            os.remove(os.path.join(out, f))
        subprocess.run(["pdftoppm", "-r", "60", "-png", PDF, os.path.join(out, "p")], check=True)


if __name__ == "__main__":
    main()
