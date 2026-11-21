#!/bin/bash
# render given svg names to build/check and make a montage sheet: check.sh sheetname name1 name2 ...
cd "$(dirname "$0")/.."
sheet=$1; shift
files=(); for n in "$@"; do files+=("src/svg/$n.svg"); done
node src/render_svg.js build/check 1 "${files[@]}" >/dev/null
pngs=(); for n in "$@"; do pngs+=("build/check/$n.png"); done
montage "${pngs[@]}" -tile 2x -geometry 640x480+6+6 -background '#888' build/$sheet.png
