#!/usr/bin/env python3
"""Inline css/ and js/ back into a single dist/nmms-portal.html."""
from pathlib import Path

root = Path(__file__).parent
html = (root / "index.html").read_text(encoding="utf-8")
css = (root / "css/styles.css").read_text(encoding="utf-8")
js = "\n".join((root / p).read_text(encoding="utf-8")
               for p in ["js/i18n.js", "js/data/hero.js", "js/data/bank.js", "js/app.js"])

html = html.replace('<link rel="stylesheet" href="css/styles.css">',
                    f"<style>\n{css}\n</style>")
for tag in ['<script src="js/i18n.js"></script>',
            '<script src="js/data/hero.js"></script>',
            '<script src="js/data/bank.js"></script>']:
    html = html.replace(tag, "")
html = html.replace('<script src="js/app.js"></script>',
                    f"<script>\n{js}\n</script>")

out = root / "dist/nmms-portal.html"
out.parent.mkdir(exist_ok=True)
out.write_text(html, encoding="utf-8")
print(f"built {out} ({len(html):,} chars)")
