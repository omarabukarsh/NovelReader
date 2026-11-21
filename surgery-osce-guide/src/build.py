# -*- coding: utf-8 -*-
"""Build the Surgery OSCE study guide: SVG -> PNG, images.json, HTML -> PDF, page previews.

usage: python3 src/build.py [--no-render] [--pages]
"""
import json, os, re, subprocess, sys, html, urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "src")
sys.path.insert(0, SRC)
from channel_content import TOPICS, HISTORY_TITLES
from photos3d import PHOTOS, PLACE
HISTORIES = json.load(open(os.path.join(SRC, "channel_histories.json"), encoding="utf-8"))
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
    for pid, (cap, legend) in PHOTOS.items():
        items.append(dict(id=pid, topic=None, kind="3d-photo", caption=strip(cap), legend=[strip(x) for x in legend],
                          prompt="Blender Cycles render of a MakeHuman (CC0) body and WebXR generic hand (MIT); see src/b3d"))
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


def history_html(pid):
    """Render a channel history script (Arabic) compactly: sections with questions run together."""
    txt = HISTORIES[pid]
    lines = [l.strip() for l in txt.splitlines() if l.strip()]
    secs, cur, title = [], [], "الافتتاح"
    for l in lines:
        if "🐥" in l:
            if cur:
                secs.append((title, cur))
            title, cur = l.replace("🐥", "").strip(" :"), []
        else:
            cur.append(html.escape(l))
    if cur:
        secs.append((title, cur))
    body = "".join(f'<p><b>{html.escape(t)}:</b> {" ◦ ".join(q)}</p>' for t, q in secs)
    return (f'<div class="hist"><h3 class="ck-t">{HISTORY_TITLES[pid]} <span class="src notes">channel script</span></h3>'
            f'<div class="hist-b" dir="rtl" lang="ar">{body}</div></div>')


def topic_html(t, catalog):
    n = t["num"]
    sec = 0
    def h2(title):
        nonlocal sec
        sec += 1
        return f'<h2><span>{sec}</span>{title}</h2>'
    out = [f'<section class="topic" id="t{n}">',
           f'<header class="thead"><div class="kicker">TOPIC {n:02d}</div><h1>{t["title"]}</h1>'
           f'<p class="sub">{t["subtitle"]}</p></header>',
           f'<div class="ar-box" dir="rtl" lang="ar"><div class="ar-h">ملخص سريع</div><p>{t["ar"]}</p></div>',
           h2("OSCE checklists")]
    figno = 0
    cols = ('<colgroup><col class="c-n"><col class="c-s"><col class="c-h"><col class="c-b"><col class="c-b"><col class="c-b"></colgroup>')
    for ci, ck in enumerate(t["checklists"]):
        ctitle, phases, points = ck[0], ck[1], ck[2]
        out.append(f'<div class="ck"><h3 class="ck-t">{chr(65 + ci)}. {ctitle}</h3>')
        step = 0
        for pi, (phase, pnote, items) in enumerate(phases):
            count = "" if phase in ("Introduction", "Completion", "Closure", "Preparation") or len(items) < 2 else f' <em>{len(items)} things</em>'
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
            cls = "phase-block" + (" end" if phase in ("Completion", "Closure") else "") + (" help" if phase in ("Introduction", "Preparation") else "")
            out.append(f'<div class="{cls}"><table class="cktbl">{cols}{head}<tbody>'
                       f'<tr class="phase"><td colspan="6">{phase}{count}{pn}</td></tr>{rows}</tbody></table>')
            if figs:
                out.append('<div class="figrow">')
                for img, st, how, sn, fn in figs:
                    out.append(figure(img, f"<b>{st}</b> — {how}", f"Fig {n}.{fn} · step {sn}", catalog))
                out.append('</div>')
            ph3 = PLACE.get((t["id"], ci, phase), [])
            if ph3:
                out.append('<div class="row3d">')
                for pid in ph3:
                    figno += 1
                    cap, legend = PHOTOS[pid]
                    lg = "".join(f'<li><span class="mk-s">{i}</span>{x}</li>' for i, x in enumerate(legend, 1))
                    out.append(f'<figure class="fig3d"><div class="imgwrap"><img src="images/{pid}.png" alt=""></div>'
                               f'<figcaption><b>3D · Fig {n}.{figno}</b> {cap}</figcaption>'
                               + (f'<ol class="lg3d">{lg}</ol>' if lg else '') + '</figure>')
                out.append('</div>')
            out.append('</div>')
        if points:
            out.append('<div class="pts"><b>★ Important OSCE points the examiner looks for:</b> ' +
                       " · ".join(points) + '</div>')
        out.append('</div>')
    if t["tables"]:
        out += [table_html(tb) for tb in t["tables"]]
    if t["tips"]:
        out.append('<div class="tipbox"><b>Exam tips from the channel</b><ul>' + "".join(f"<li>{x}</li>" for x in t["tips"]) + '</ul></div>')
    if t["histories"]:
        out.append(h2("History taking — channel scripts"))
        out += [history_html(pid) for pid in t["histories"]]
    if t["quiz"]:
        rows = "".join(f'<tr><td class="num">{i}</td><td>{q}</td><td>{a or "—"}</td></tr>' for i, (q, a) in enumerate(t["quiz"], 1))
        out.append(f'<div class="tbl">{h2("Previous quiz questions")}<table><thead><tr><th>#</th><th>Question</th><th>Answer (as given in the channel)</th></tr></thead>'
                   f'<tbody>{rows}</tbody></table></div>')
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
             f'<p class="cv-s">Every station from the Competenze Cliniche channel: checklists, examiner points, history scripts and previous quiz questions</p>'
             f'<p class="cv-ar" dir="rtl" lang="ar">دليل المذاكرة لامتحان المهارات الإكلينيكية – الجراحة</p>'
             f'<img class="cv-img" src="images/{cover_img}.png" alt="">'
             f'<ol class="cv-list">' + "".join(f"<li>{t['title']}</li>" for t in TOPICS) + '</ol></div></section>')
    tocs = (f'<section class="toc"><h1>Contents</h1><ol>{toc}</ol>'
            f'<div class="howto"><h3>How every topic is organised</h3><ol>'
            f'<li><b>ملخص</b> – short Arabic summary</li>'
            f'<li><b>OSCE checklists</b> – every station of the topic, step by step in the channel’s order. Each phase says how many things '
            f'to do; drawings sit under the phase they show; ★ box = the points the examiner looks for. Tick P / MP / F while you practise.</li>'
            f'<li><b>History taking</b> – the channel’s Arabic question scripts. Not everything is asked: read the parts most related to your case.</li>'
            f'<li><b>Previous quiz questions</b> – from earlier groups, with the channel’s answers where given.</li></ol>'
            f'<p class="note">Source: Telegram channel “Competenze Cliniche 313” (summaries written from the doctors’ voice notes). '
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
