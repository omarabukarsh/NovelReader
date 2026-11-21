"""Option A: generate every illustration in images.json with an image-generation API.

Runs only if IMAGE_API_KEY is set. Default model: OpenAI gpt-image-1 (override with IMAGE_MODEL).
Skips images that already exist in images/.   usage: python3 src/gen_images.py [--only id1,id2]
"""
import base64, json, os, sys, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KEY = os.environ.get("IMAGE_API_KEY")
MODEL = os.environ.get("IMAGE_MODEL", "gpt-image-1")
if not KEY:
    sys.exit("IMAGE_API_KEY is not set - use the hand-drawn SVG pipeline (src/draw_*.py) instead.")
only = set(sys.argv[sys.argv.index("--only") + 1].split(",")) if "--only" in sys.argv else None
items = json.load(open(os.path.join(ROOT, "images.json"), encoding="utf-8"))
os.makedirs(os.path.join(ROOT, "images"), exist_ok=True)
for it in items:
    out = os.path.join(ROOT, it["file"])
    if os.path.exists(out) or (only and it["id"] not in only):
        continue
    size = "1024x1536" if it["kind"] == "inspection-map" else "1536x1024"
    body = json.dumps({"model": MODEL, "prompt": it["prompt"], "size": size, "n": 1}).encode()
    req = urllib.request.Request("https://api.openai.com/v1/images/generations", data=body,
                                 headers={"Authorization": f"Bearer {KEY}", "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=300) as r:
            data = json.load(r)["data"][0]["b64_json"]
        open(out, "wb").write(base64.b64decode(data))
        print("saved", out)
    except Exception as e:  # keep going; re-run later to fill gaps
        print("FAILED", it["id"], e)
