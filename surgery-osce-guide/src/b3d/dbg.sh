#!/bin/bash
# dbg.sh scene -> /tmp/claude-0/r3d/dbg_<scene>.png (main view with pins + top/side/end views)
cd "$(dirname "$0")"; mkdir -p /tmp/claude-0/r3d/dbg
/tmp/claude-0/bpyenv/bin/python run.py /tmp/claude-0/r3d/dbg --preview --debug "$@" 2>&1 | grep -E "^[a-z0-9_]+: |rror|Trace"
for n in "$@"; do
python3 - "$n" <<'P'
import sys, json; from PIL import Image, ImageDraw, ImageFont
n=sys.argv[1]; d="/tmp/claude-0/r3d/dbg"; im=Image.open(f"{d}/{n}.png").convert("RGB"); j=json.load(open(f"{d}/{n}.json"))
W,H=im.size; dr=ImageDraw.Draw(im); F=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",14)
for k,q in j["marks"].items():
    x,y=q[0]/100*W,q[1]/100*H; dr.ellipse((x-10,y-10,x+10,y+10),fill=(214,47,47),outline="white",width=2); dr.text((x,y),k,fill="white",font=F,anchor="mm")
sheet=Image.new("RGB",(W+420,max(H,960)),"white"); sheet.paste(im,(0,0))
for i,t in enumerate(("top","side","end")):
    v=Image.open(f"{d}/{n}__{t}.png").convert("RGB"); sheet.paste(v,(W,i*320)); ImageDraw.Draw(sheet).text((W+6,i*320+4),t,fill="black",font=F)
sheet.save(f"/tmp/claude-0/r3d/dbg_{n}.png")
P
done
