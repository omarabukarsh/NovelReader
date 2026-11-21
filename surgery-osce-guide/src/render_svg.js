// Render SVG files to PNG with headless Chromium (Playwright).
// usage: node src/render_svg.js out_dir scale file1.svg [file2.svg ...]
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
(async () => {
  const [outDir, scale, ...files] = process.argv.slice(2);
  const browser = await chromium.launch();
  const page = await browser.newPage({ deviceScaleFactor: Number(scale) || 1 });
  for (const f of files) {
    const svg = fs.readFileSync(f, 'utf8');
    const m = svg.match(/viewBox="([\d.\s-]+)"/);
    const [, , w, h] = m[1].trim().split(/\s+/).map(Number);
    await page.setViewportSize({ width: Math.round(w), height: Math.round(h) });
    await page.setContent(`<html><body style="margin:0;background:#fff">${svg.replace(/<svg /, `<svg width="${w}" height="${h}" `)}</body></html>`);
    const out = path.join(outDir, path.basename(f).replace(/\.svg$/, '.png'));
    await page.screenshot({ path: out, clip: { x: 0, y: 0, width: w, height: h } });
    console.log('wrote', out);
  }
  await browser.close();
})();
