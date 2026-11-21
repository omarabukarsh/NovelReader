# -*- coding: utf-8 -*-
"""Build the Surgery OSCE study guide: SVG -> PNG, images.json, HTML -> PDF, page previews.

usage: python3 src/build.py [--no-render] [--pages]
"""
import json, os, re, subprocess, sys, html, urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "src")
sys.path.insert(0, SRC)
from content_1 import TOPICS_A
from content_2 import TOPICS_B
from content_3 import TOPICS_C

TOPICS = TOPICS_A + TOPICS_B + TOPICS_C
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


def write_catalog():
    items = []
    for t in TOPICS:
        for img, cap in t["figures"]:
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
           f'<p class="sub">{t["subtitle"]}</p></header>']
    # 1 Arabic summary
    out.append(f'<div class="ar-box" dir="rtl" lang="ar"><div class="ar-h">ملخص سريع</div><p>{t["ar"]}</p></div>')
    # 2 look for
    out.append('<h2><span>1</span>Number of things to look for</h2><div class="look">')
    for title, items in t["lookfor"]:
        lis = "".join(f"<li>{i}</li>" for i in items)
        out.append(f'<div class="lcard"><h3>{title} — <em>{len(items)} things</em></h3><ol>{lis}</ol></div>')
    out.append('</div>')
    # 3 procedure
    out.append('<h2><span>2</span>Step-by-step procedure</h2>')
    for title, steps in t["procedures"]:
        lis = ""
        for kind, txt in steps:
            c = f' class="{kind}"' if kind else ""
            lis += f"<li{c}>{txt}</li>"
        out.append(f'<div class="proc"><h3>{title}</h3><ol class="steps">{lis}</ol></div>')
    # 4 figures
    out.append('<h2 class="brk"><span>3</span>Step illustrations</h2><div class="figs">')
    for k, (img, cap) in enumerate(t["figures"], 1):
        out.append(figure(img, cap, f"Fig {n}.{k}", catalog))
    out.append('</div>')
    # 5 inspection map
    m = t["map"]
    rows = "".join(f'<tr><td class="num"><span class="mk-s">{i}</span></td><td>{w}</td><td>{f}</td></tr>'
                   for i, (w, f) in enumerate(m["rows"], 1))
    out.append(f'<div class="mapblock"><h2><span>4</span>Inspection map</h2><div class="map">'
               f'{figure(m["img"], m["title"], "Map", catalog, m["markers"], "fig mapfig")}'
               f'<table class="maptbl"><thead><tr><th>#</th><th>Where to look</th><th>What you may find</th></tr></thead>'
               f'<tbody>{rows}</tbody></table></div></div>')
    # 6 tables
    out.append('<h2><span>5</span>Key tables</h2>')
    out += [table_html(tb) for tb in t["tables"]]
    # 7 checklist
    rows = "".join(f'<tr><td class="num">{i}</td><td>{s}</td><td class="box"><span></span></td></tr>'
                   for i, s in enumerate(t["checklist"], 1))
    out.append(f'<div class="cl"><h2><span>6</span>OSCE checklist</h2><table class="check"><thead><tr><th>#</th>'
               f'<th>Step</th><th>✓</th></tr></thead><tbody>{rows}</tbody></table></div>')
    # 8 links
    lis = "".join(f'<li><a href="https://www.youtube.com/results?search_query={urllib.parse.quote_plus(q)}">▶ {lab}</a>'
                  f'<span class="q">YouTube search: “{q}”</span></li>' for lab, q in t["links"])
    out.append(f'<div class="links"><h2><span>7</span>Video links</h2><ul>{lis}</ul></div>')
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
             f'<p class="cv-s">Examination routines, inspection maps, key tables and checklists for 9 syllabus topics</p>'
             f'<p class="cv-ar" dir="rtl" lang="ar">دليل المذاكرة لامتحان المهارات الإكلينيكية – الجراحة</p>'
             f'<img class="cv-img" src="images/{cover_img}.png" alt="">'
             f'<ol class="cv-list">' + "".join(f"<li>{t['title']}</li>" for t in TOPICS) + '</ol></div></section>')
    tocs = (f'<section class="toc"><h1>Contents</h1><ol>{toc}</ol>'
            f'<div class="howto"><h3>How every topic is organised</h3><ol>'
            f'<li><b>ملخص</b> – short Arabic summary</li><li>Number of things to look for</li>'
            f'<li>Step-by-step procedure – in the order examiners mark it</li><li>Step illustrations</li>'
            f'<li>Inspection map – numbered red markers + table</li><li>Key tables</li>'
            f'<li>OSCE checklist – tick the boxes while you practise</li><li>Video links</li></ol>'
            f'<p class="note">Bookends of every examination are highlighted: <span class="tag open">start – WIPER</span> '
            f'<span class="tag close">finish – thank, cover, wash, summarise, differential, complete, investigations</span></p></div></section>')
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
