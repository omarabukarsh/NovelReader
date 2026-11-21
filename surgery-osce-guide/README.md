# Surgery Clinical Skills — OSCE Study Guide

* `Surgery_OSCE_Study_Guide.pdf` – the guide (A4). `Surgery_OSCE_Study_Guide.html` – its source page.
* `images/` – illustrations (PNG). `images.json` – catalogue of every illustration (caption, prompt, status).
* `src/channel_content.py` – all station checklists, examiner points, quiz questions and tips, taken from the Telegram channel “Competenze Cliniche 313”; `src/channel_histories.json` – its Arabic history-taking scripts.
* `src/draw_*.py` + `src/art.py` – hand-drawn illustrations (single Bézier outline per body part, reusable hand-pose library) → `src/svg/` → `images/*.png` (2×). `src/check.sh` renders a contact sheet for review.
* `src/gen_images.py` – Option A: AI generation when `IMAGE_API_KEY` is set (skips existing files).
* Build: `python3 src/build.py --pages` (renders SVG → PNG, two-pass PDF so the contents page numbers are right, page previews in `build/pages`).
