#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""md2pdf.py - render a Markdown file to PDF (Markdown -> HTML -> html2pdf.py).

Usage:
    python md2pdf.py input.md [output.pdf]

Markdown is converted with the `markdown` package if available (pip install markdown),
otherwise a minimal built-in converter handles headings, lists, code and paragraphs.
The intermediate HTML is wrapped in a neutral stylesheet and handed to html2pdf.py.
"""
import html as _html
import re
import subprocess
import sys
from pathlib import Path

DOC_CSS = """
body{font:15px/1.55 -apple-system,Segoe UI,Roboto,Arial,sans-serif;color:#1d2733;max-width:820px;margin:0 auto;padding:24px;}
h1,h2,h3{line-height:1.25} code{background:#eef2f7;padding:1px 5px;border-radius:4px}
pre{background:#0f1722;color:#e6edf3;padding:12px;border-radius:8px;overflow:auto}
table{border-collapse:collapse} td,th{border:1px solid #d8dee6;padding:6px 10px}
blockquote{border-left:3px solid #c7d2e0;margin:0;padding-left:14px;color:#48566a}
"""


def minimal_md(md: str) -> str:
    out, in_ul, in_code = [], False, False
    for line in md.splitlines():
        if line.strip().startswith("```"):
            in_code = not in_code
            out.append("<pre>" if in_code else "</pre>")
            continue
        if in_code:
            out.append(_html.escape(line))
            continue
        m = re.match(r"(#{1,6})\s+(.*)", line)
        if m:
            if in_ul:
                out.append("</ul>"); in_ul = False
            lvl = len(m.group(1))
            out.append(f"<h{lvl}>{_html.escape(m.group(2))}</h{lvl}>")
            continue
        if re.match(r"\s*[-*]\s+", line):
            if not in_ul:
                out.append("<ul>"); in_ul = True
            out.append(f"<li>{_html.escape(re.sub(r'^\s*[-*]\s+', '', line))}</li>")
            continue
        if in_ul:
            out.append("</ul>"); in_ul = False
        out.append(f"<p>{_html.escape(line)}</p>" if line.strip() else "")
    if in_ul:
        out.append("</ul>")
    return "\n".join(out)


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    src = Path(argv[1])
    if not src.is_file():
        print(f"error: not found: {src}")
        return 1
    out = Path(argv[2]) if len(argv) > 2 else src.with_suffix(".pdf")
    md = src.read_text(encoding="utf-8")
    try:
        import markdown
        body = markdown.markdown(md, extensions=["tables", "fenced_code"])
    except Exception:
        body = minimal_md(md)
    doc = f"<!DOCTYPE html><html><head><meta charset='utf-8'><style>{DOC_CSS}</style></head><body>{body}</body></html>"
    tmp = src.with_suffix(".md.html")
    tmp.write_text(doc, encoding="utf-8")
    here = Path(__file__).parent / "html2pdf.py"
    rc = subprocess.call([sys.executable, str(here), str(tmp), str(out)])
    try:
        tmp.unlink()
    except OSError:
        pass
    return rc


if __name__ == "__main__":
    sys.exit(main(sys.argv))
