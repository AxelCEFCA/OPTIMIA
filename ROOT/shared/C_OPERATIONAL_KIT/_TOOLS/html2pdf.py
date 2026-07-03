#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""html2pdf.py - render an HTML file to PDF with careful pagination.

Usage:
    python html2pdf.py input.html [output.pdf]

Pagination policy injected before rendering (generic, org-agnostic):
  - headings are kept with the text that follows them (no orphan headings at a page foot);
  - tables/figures avoid being split;
  - widows/orphans are limited.

Rendering backend is auto-detected, best first:
  1) Playwright (Chromium)   - highest fidelity     (pip install playwright; playwright install chromium)
  2) WeasyPrint              - pure-Python CSS->PDF  (pip install weasyprint)
If neither is installed, the script tells you what to install and exits non-zero
(it does NOT silently fail). Embed images first with embed_images.py for a portable input.
"""
import sys
from pathlib import Path

PAGINATION_CSS = """
@media print {
  h1,h2,h3,h4 { break-after: avoid-page; page-break-after: avoid; }
  h1,h2,h3,h4 { break-inside: avoid; }
  table, figure, pre, blockquote { break-inside: avoid; page-break-inside: avoid; }
  p { orphans: 3; widows: 3; }
  img { max-width: 100%; }
}
"""


def inject_css(html: str) -> str:
    style = f"<style>{PAGINATION_CSS}</style>"
    low = html.lower()
    if "</head>" in low:
        i = low.index("</head>")
        return html[:i] + style + html[i:]
    return style + html


def via_playwright(html: str, out: Path) -> bool:
    try:
        from playwright.sync_api import sync_playwright
    except Exception:
        return False
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page()
        pg.set_content(html, wait_until="load")
        pg.pdf(path=str(out), format="A4", print_background=True,
               margin={"top": "18mm", "bottom": "18mm", "left": "16mm", "right": "16mm"})
        b.close()
    return True


def via_weasyprint(html: str, out: Path, base_url: str) -> bool:
    try:
        from weasyprint import HTML
    except Exception:
        return False
    HTML(string=html, base_url=base_url).write_pdf(str(out))
    return True


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    src = Path(argv[1])
    if not src.is_file():
        print(f"error: not found: {src}")
        return 1
    out = Path(argv[2]) if len(argv) > 2 else src.with_suffix(".pdf")
    html = inject_css(src.read_text(encoding="utf-8"))
    if via_playwright(html, out):
        print(f"ok (playwright) -> {out}")
        return 0
    if via_weasyprint(html, out, base_url=str(src.parent)):
        print(f"ok (weasyprint) -> {out}")
        return 0
    print("error: no PDF backend available. Install ONE of:")
    print("   pip install playwright && playwright install chromium   (best fidelity)")
    print("   pip install weasyprint                                  (pure-Python)")
    return 3


if __name__ == "__main__":
    sys.exit(main(sys.argv))
