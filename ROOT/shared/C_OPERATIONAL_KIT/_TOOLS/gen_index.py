#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""gen_index.py - the P7 index generator: rebuild index.json (machine) and index.html
(human) for each content chamber from the live folder tree + each folder's README.

Usage:
    python gen_index.py            # regenerates A_REFERENCE and B_OPERATIONS indexes

Both indexes are GENERATED artefacts (governance P7): never hand-edit them; run this
after any structural change, configuration or promotion. The summary of each folder is
read from the first blockquote / heading-free line of its README (or the named CORE doc).
"""
import json
import re
from pathlib import Path

SHARED = Path(__file__).resolve().parents[2]          # .../shared
CORE_DOC = {"01_CORE_Schema": "SCHEMA.md", "02_CORE_Templates": "TEMPLATE.md",
            "03_CORE_Rules": "RULES.md", "04_CORE_Governance": "GOVERNANCE.md",
            "05_CORE_Glossary": "GLOSSARY.md", "07_CORE_Index": "INDEX_SPEC.md",
            "09_CORE_Flow": "FLOW.md"}
CSS = ("body{font:16px/1.5 -apple-system,Segoe UI,Roboto,Arial,sans-serif;color:#1d2733;"
       "background:#f7f9fc;max-width:1000px;margin:0 auto;padding:28px 20px 64px}"
       "h1{font-size:25px;margin:6px 0 2px}.sub{color:#5d6b7a;margin:0 0 22px}"
       ".fam h2{font-size:14px;letter-spacing:.04em;text-transform:uppercase;color:#2a6df0;"
       "border-bottom:1px solid #e3e8ee;padding-bottom:6px;margin:18px 0 8px}"
       ".grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:10px}"
       ".it{display:block;text-decoration:none;color:inherit;background:#fff;border:1px solid #e3e8ee;"
       "border-radius:9px;padding:11px 13px}.it .n{font-weight:600;font-size:14px}"
       ".it .s{color:#5d6b7a;font-size:12.5px;margin-top:3px}.it.core{border-left:3px solid #9b59b6}"
       ".it.base{border-left:3px solid #2a6df0}.it.reserved{opacity:.6}"
       "a.back{font-size:13px;color:#5d6b7a;text-decoration:none}")


def esc(s):
    return (s or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def summary_of(folder: Path, doc: str) -> str:
    f = folder / doc
    if not f.is_file():
        return ""
    in_fm = False
    for line in f.read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if s == "---":
            in_fm = not in_fm
            continue
        if in_fm or not s or s.startswith("#"):
            continue
        s = re.sub(r"^>\s*", "", s)
        s = re.sub(r"\*\*([^*]+)\*\*", r"\1", s)
        return s[:160]
    return ""


def classify(name: str):
    """Return (family, kind, doc) deriving the family from the name itself."""
    m = re.match(r"(\d+)_([A-Za-z]+)", name)
    if not m:
        fam = "OUTPUT" if name == "_OUTPUT" else "KIT"
        return fam, "kit", "README.md"
    num, fam = int(m.group(1)), m.group(2).upper()
    doc = CORE_DOC.get(name, "README.md") if fam == "CORE" else "README.md"
    if fam == "CORE":
        kind = "core"
    elif num % 10 == 0:
        kind = "base"
    elif "Reserved" in name:
        kind = "reserved"
    else:
        kind = "derivative"
    return fam, kind, doc


def build(chamber: str, side: str, accent: str):
    cdir = SHARED / chamber
    subs = sorted([p for p in cdir.iterdir() if p.is_dir()])
    entries, order, groups = [], [], {}
    for p in subs:
        name = p.name
        fam, kind, doc = classify(name)
        e = {"name": name, "kind": kind, "family": fam, "summary": summary_of(p, doc)}
        entries.append(e)
        if fam not in groups:
            groups[fam] = []; order.append(fam)
        groups[fam].append((e, doc))
    # index.json
    (cdir / "index.json").write_text(json.dumps(
        {"chamber": chamber, "generated_by": "07_CORE_Index / gen_index.py",
         "note": "Generated artefact (P7) - do not hand-edit.", "folders": entries},
        indent=2, ensure_ascii=False), encoding="utf-8")
    # index.html
    secs = []
    for fam in order:
        items = []
        for e, doc in groups[fam]:
            cls = {"core": "it core", "base": "it base", "reserved": "it reserved"}.get(e["kind"], "it")
            href = f'{e["name"]}/{doc}'
            items.append(f'<a class="{cls}" href="{href}"><div class="n">{esc(e["name"])}</div>'
                         f'<div class="s">{esc(e["summary"])}</div></a>')
        secs.append(f'<div class="fam"><h2>{esc(fam)}</h2><div class="grid">{"".join(items)}</div></div>')
    nav = " &nbsp;·&nbsp; ".join(
        (f"<b>{c}</b>" if c == chamber else f"<a href='../{c}/index.html'>{c}</a>")
        for c in ("A_REFERENCE", "B_OPERATIONS", "C_OPERATIONAL_KIT"))
    navcss = (".nav{font-size:13px;margin:6px 0 12px;color:#5d6b7a}"
              ".nav a{color:#2a6df0;text-decoration:none} .nav b{color:#1d2733}")
    html = (f"<!DOCTYPE html><html lang='en'><head><meta charset='utf-8'>"
            f"<meta name='viewport' content='width=device-width, initial-scale=1'>"
            f"<title>{chamber} - index</title><style>{CSS}{navcss} .fam h2{{color:{accent}}}</style></head>"
            f"<body><a class='back' href='../index.html'>&larr; landing</a><h1>{chamber}</h1>"
            f"<div class='nav'>Chambers: {nav} &nbsp;·&nbsp; "
            f"<a href='../C_OPERATIONAL_KIT/_SKILLS/skill_use_structure.md'>How to navigate &amp; manage this memory</a></div>"
            f"<p class='sub'>Generated from the folder tree (P7). Machine site-map: "
            f"<a href='index.json'>index.json</a>. The full folder tree is <a href='../../_TREE.txt'>_TREE.txt</a>.</p>"
            f"{''.join(secs)}</body></html>")
    (cdir / "index.html").write_text(html, encoding="utf-8")
    print(f"  {chamber}: {len(entries)} folders")


if __name__ == "__main__":
    print("Regenerating chamber indexes (P7)...")
    build("A_REFERENCE", "A", "#2a6df0")
    build("B_OPERATIONS", "B", "#0f9d6b")
    print("done.")
