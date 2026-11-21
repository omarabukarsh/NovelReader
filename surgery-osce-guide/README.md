# Surgery Clinical Skills — OSCE Study Guide

* `Surgery_OSCE_Study_Guide.pdf` – the guide (A4). `Surgery_OSCE_Study_Guide.html` – its source page.
* `images/` – illustrations (PNG). `images.json` – catalogue of every illustration (caption, prompt, status).
* `src/content_*.py` – all text, steps, tables, checklists, map markers.
* `src/draw_*.py` + `src/art.py` – hand-drawn illustrations (single Bézier outlines per body part) → `src/svg/`.
* `src/gen_images.py` – Option A: AI generation when `IMAGE_API_KEY` is set (skips existing files).
* Build: `python3 src/build.py --pages` (renders SVG → PNG, two-pass PDF so the contents page numbers are right, page previews in `build/pages`).
