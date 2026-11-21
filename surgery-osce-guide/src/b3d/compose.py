"""Draw numbered red markers, dashed lines and arrows on the rendered 3D images -> images/<id>.png
usage: python3 compose.py RENDER_DIR OUT_DIR [ids...]"""
import sys, os, json, glob, math
from PIL import Image, ImageDraw, ImageFont
src, dst = sys.argv[1], sys.argv[2]
ids = sys.argv[3:] or sorted(os.path.basename(p)[:-5] for p in glob.glob(src + "/*.json") if "__" not in p)
FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
TEAL, RED = (22, 122, 139), (214, 47, 47)


def dashed(dr, a, b, w, dash=14, gap=9):
    L = math.dist(a, b); n = max(1, int(L / (dash + gap)))
    for i in range(n + 1):
        t0 = i * (dash + gap) / L; t1 = min(1, t0 + dash / L)
        if t0 >= 1: break
        dr.line([(a[0] + (b[0] - a[0]) * t0, a[1] + (b[1] - a[1]) * t0), (a[0] + (b[0] - a[0]) * t1, a[1] + (b[1] - a[1]) * t1)], fill=TEAL, width=w)


def arrow(dr, a, b, w):
    dr.line([a, b], fill=TEAL, width=w)
    ang = math.atan2(b[1] - a[1], b[0] - a[0]); h = 7 * w
    p1 = (b[0] - h * math.cos(ang - 0.45), b[1] - h * math.sin(ang - 0.45)); p2 = (b[0] - h * math.cos(ang + 0.45), b[1] - h * math.sin(ang + 0.45))
    dr.polygon([b, p1, p2], fill=TEAL)


for n in ids:
    im = Image.open(f"{src}/{n}.png").convert("RGB"); j = json.load(open(f"{src}/{n}.json"))
    W, H = im.size; S = W / 1200
    dr = ImageDraw.Draw(im); P = lambda q: (q[0] / 100 * W, q[1] / 100 * H)
    for o in j["over"]:
        pts = [P(q) for q in o["pts"]]
        if o["kind"] == "dash":
            dashed(dr, pts[0], pts[1], int(4 * S))
        elif o["kind"] == "arrow":
            arrow(dr, pts[0], pts[1], int(4 * S))
        elif o["kind"] == "arc":
            dashed(dr, pts[0], pts[1], int(4 * S)); dashed(dr, pts[0], pts[2], int(4 * S))
            r = 0.45 * min(math.dist(pts[0], pts[1]), math.dist(pts[0], pts[2]))
            a1 = math.degrees(math.atan2(pts[1][1] - pts[0][1], pts[1][0] - pts[0][0])); a2 = math.degrees(math.atan2(pts[2][1] - pts[0][1], pts[2][0] - pts[0][0]))
            lo, hi = sorted((a1, a2))
            if hi - lo > 180: lo, hi = hi, lo + 360
            dr.arc([pts[0][0] - r, pts[0][1] - r, pts[0][0] + r, pts[0][1] + r], lo, hi, fill=TEAL, width=int(4 * S))
    R = int(19 * S); F = ImageFont.truetype(FB, int(22 * S))
    for k, q in j["marks"].items():
        x, y = P(q)
        dr.ellipse((x - R - 2, y - R - 2, x + R + 2, y + R + 2), fill=(255, 255, 255))
        dr.ellipse((x - R, y - R, x + R, y + R), fill=RED)
        dr.text((x, y + 1), k, fill="white", font=F, anchor="mm")
    im.save(f"{dst}/{n}.png", optimize=True)
    print("composed", n)
