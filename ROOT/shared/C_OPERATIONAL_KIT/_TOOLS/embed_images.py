#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""embed_images.py - turn a lightweight HTML (referenced images) into a self-contained
HTML (images inlined as base64 data URIs). Pure standard library; no dependencies.

Usage:
    python embed_images.py input.html [output.html]

If output is omitted, writes <input>_embed.html next to the input. Local <img src> and
CSS url(...) references are inlined; http(s) and data: URIs are left untouched. This is
the first step of the production pipeline (see ../_SKILLS/skill_official_documents.md):
    work (referenced) -> embed_images -> self-contained -> html2pdf -> _OUTPUT/
"""
import base64
import mimetypes
import re
import sys
from pathlib import Path

ASSET_RE = re.compile(r'(src|href)\s*=\s*(["\'])([^"\']+)\2', re.IGNORECASE)
CSS_URL_RE = re.compile(r'url\(\s*["\']?([^"\')]+)["\']?\s*\)', re.IGNORECASE)
SKIP = ("http://", "https://", "data:", "mailto:", "#")


def to_data_uri(path: Path) -> str | None:
    if not path.is_file():
        return None
    mime, _ = mimetypes.guess_type(str(path))
    mime = mime or "application/octet-stream"
    b64 = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime};base64,{b64}"


def inline(html: str, base_dir: Path) -> tuple[str, int, int]:
    done = miss = 0

    def is_image(target: str) -> bool:
        return target.lower().rsplit(".", 1)[-1] in {
            "png", "jpg", "jpeg", "gif", "svg", "webp", "ico", "bmp"}

    def repl_attr(m):
        nonlocal done, miss
        attr, quote, target = m.group(1), m.group(2), m.group(3)
        if target.startswith(SKIP) or (attr.lower() == "href" and not is_image(target)):
            return m.group(0)
        uri = to_data_uri((base_dir / target).resolve())
        if uri:
            done += 1
            return f'{attr}={quote}{uri}{quote}'
        miss += 1
        return m.group(0)

    def repl_css(m):
        nonlocal done, miss
        target = m.group(1)
        if target.startswith(SKIP):
            return m.group(0)
        uri = to_data_uri((base_dir / target).resolve())
        if uri:
            done += 1
            return f'url("{uri}")'
        miss += 1
        return m.group(0)

    html = ASSET_RE.sub(repl_attr, html)
    html = CSS_URL_RE.sub(repl_css, html)
    return html, done, miss


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    src = Path(argv[1])
    if not src.is_file():
        print(f"error: not found: {src}")
        return 1
    out = Path(argv[2]) if len(argv) > 2 else src.with_name(src.stem + "_embed.html")
    html, done, miss = inline(src.read_text(encoding="utf-8"), src.parent)
    out.write_text(html, encoding="utf-8")
    print(f"embedded {done} asset(s){' , ' + str(miss) + ' missing' if miss else ''} -> {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
