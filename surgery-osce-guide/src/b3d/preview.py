"""Draw pins/overlays on rendered PNGs and tile them: python3 preview.py DIR OUT.png [names...]"""
import sys, os, json, glob, math
from PIL import Image, ImageDraw, ImageFont
d, outp = sys.argv[1], sys.argv[2]; names = sys.argv[3:] or sorted(os.path.basename(p)[:-5] for p in glob.glob(d + "/*.json"))
F = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 15)
tiles = []
for n in names:
    im = Image.open(f"{d}/{n}.png").convert("RGB"); j = json.load(open(f"{d}/{n}.json")); W, H = im.size
    dr = ImageDraw.Draw(im); P = lambda q: (q[0] / 100 * W, q[1] / 100 * H)
    for o in j["over"]:
        pts = [P(q) for q in o["pts"]]
        if o["kind"] in ("dash", "line", "arrow"):
            dr.line(pts, fill=(22, 122, 139), width=3)
        if o["kind"] == "arc":
            dr.line([pts[0], pts[1]], fill=(22, 122, 139), width=2); dr.line([pts[0], pts[2]], fill=(22, 122, 139), width=2)
    for k, q in j["marks"].items():
        x, y = P(q); dr.ellipse((x - 11, y - 11, x + 11, y + 11), fill=(214, 47, 47), outline="white", width=2)
        dr.text((x, y), k, fill="white", font=F, anchor="mm")
    dr.text((8, 8), n, fill=(0, 0, 0), font=F)
    tiles.append(im)
w = max(t.width for t in tiles); h = max(t.height for t in tiles); cols = 3
sheet = Image.new("RGB", (cols * w, math.ceil(len(tiles) / cols) * h), "white")
for i, t in enumerate(tiles):
    sheet.paste(t, ((i % cols) * w, (i // cols) * h))
sheet.save(outp)
