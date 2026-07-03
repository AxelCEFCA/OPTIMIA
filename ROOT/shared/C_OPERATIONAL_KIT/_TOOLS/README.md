# _TOOLS — production utilities (detailed reference)

**What goes here:** the **tools** (scripts, usually Python) an agent runs at specific moments to
**transform and produce** documents and to **maintain** the memory. Reusable utilities with **no business
state**.

**What does NOT go here:** the agents' decision logic (that is `39_HOW_Automations`), the documents
themselves, the generated output (`B_OPERATIONS/_OUTPUT/`), or external capabilities/MCP servers (those
are catalogued in [`../_SERVICES/`](../_SERVICES/README.md)).

---

## 1. Software architecture

The toolkit is a small set of **single-purpose, composable command-line filters**. They are designed to be
run by an agent (or a human) one after another; each reads a file, transforms it, and writes a file. There
is no shared runtime, no daemon, no global state — every tool is a pure function of its inputs.

**Design principles**

1. **Single responsibility + composability.** Each tool does one thing and emits a file the next tool can
   consume. Complex outputs are produced by *chaining* tools, not by one mega-tool.
2. **Pure, idempotent, side-effect-local.** A tool only reads its inputs and writes its declared output.
   Re-running with the same inputs yields the same result. No tool mutates the working memory except the
   index generator, which only rewrites the two generated index files (P7).
3. **Standard library first.** `embed_images.py` and `gen_index.py` need only Python's standard library
   (zero install). `html2pdf.py`/`md2pdf.py` need a PDF backend and **detect it at runtime**, failing with
   a clear "install X" message instead of a stack trace — they never fail silently.
4. **UTF-8, no BOM, everywhere.** All tools read and write `encoding="utf-8"`. They never use a
   platform-default codec (this is a hard rule for the whole memory).
5. **Text in, text out.** Inputs and outputs are plain files (HTML, MD, JSON, images). This keeps the tools
   debuggable, diffable and pipe-friendly.
6. **No business knowledge.** A tool knows nothing about the organisation. Anything org-specific (logo
   placement, naming, output layout) comes from `08_CORE_Profile`, not from a tool.

**The production pipeline** (how the tools compose)

```
            working document                    (lightweight HTML, images REFERENCED to _RESOURCES)
                   │
   embed_images.py │  inline every local <img>/url() as a base64 data: URI
                   ▼
            self-contained HTML                 (one portable file — good for chat/email)
                   │
      html2pdf.py  │  render with pagination rules (Playwright or WeasyPrint)
                   ▼
                  PDF  ───────────────────────►  B_OPERATIONS/_OUTPUT/   (the heavy deliverable)
                                                        │
                                                        └─ if evidence → stub + pointer in 03_WORK_Flow

   md2pdf.py   = Markdown ─► HTML ─► html2pdf.py        (a convenience wrapper over the chain)
   gen_index.py = folder tree ─► index.json + index.html  (the P7 index generator; runs independently)
```

`embed_images.py` and `html2pdf.py` are the two atoms of the document pipeline; `md2pdf.py` is sugar that
chains them from Markdown; `gen_index.py` is a separate maintenance tool that keeps the navigable and
machine indexes in sync with the tree.

---

## 2. Tool catalogue

| Tool | One line | Stdlib only? |
|------|----------|--------------|
| `embed_images.py` | referenced-image HTML → self-contained HTML (base64) | ✅ yes |
| `html2pdf.py` | HTML → PDF with careful pagination | needs a PDF backend |
| `md2pdf.py` | Markdown → PDF (MD→HTML→`html2pdf.py`) | needs a PDF backend |
| `gen_index.py` | folder tree → `index.json` + `index.html` (P7 generator) | ✅ yes |

Run any tool with **no arguments** to print its usage header.

---

## 3. Tool reference (detailed)

### `embed_images.py`
- **What it does.** Rewrites an HTML file so every **local** image referenced by `<img src>`, `<… href>`
  (for image files) or CSS `url(...)` is inlined as a `data:<mime>;base64,…` URI. The result is a single,
  dependency-free HTML file. `http(s):` and existing `data:` URIs are left untouched; both single and
  double quotes are handled.
- **When to use it.** Right before sending a document by chat/email, or before `html2pdf.py`, so the output
  is portable and self-contained. (Working documents stay *light* with referenced images; embedding is only
  for output.)
- **Usage.**
  ```
  python embed_images.py input.html [output.html]
  ```
  If `output` is omitted, writes `<input>_embed.html` next to the input.
- **Inputs.** One HTML file plus the local image files it references (resolved relative to the HTML).
- **Outputs.** One self-contained HTML file. Prints `embedded N asset(s) [, M missing]`.
- **Dependencies.** None (standard library only).
- **How it works.** Two regexes scan for `src=/href=` attributes and CSS `url()`; each local target is read,
  MIME-typed via `mimetypes`, base64-encoded and substituted in place, preserving the original quote style.
- **Exit codes.** `0` success · `1` input not found · `2` no/over-few arguments (prints usage).

### `html2pdf.py`
- **What it does.** Renders an HTML file to PDF and **injects a print stylesheet** first so that: headings
  are not orphaned at a page foot (`break-after: avoid`), tables/figures/blockquotes are not split, and
  paragraphs keep ≥3 orphan/widow lines.
- **When to use it.** To produce the printable/archival deliverable, after `embed_images.py`.
- **Usage.**
  ```
  python html2pdf.py input.html [output.pdf]
  ```
  If `output` is omitted, writes `<input>.pdf`.
- **Inputs.** One HTML file (ideally already self-contained).
- **Outputs.** One PDF (A4, sensible margins, backgrounds printed).
- **Dependencies.** A PDF backend, auto-detected best-first: **Playwright** (`pip install playwright &&
  playwright install chromium`, highest fidelity) or **WeasyPrint** (`pip install weasyprint`, pure-Python).
  If neither is present it prints exactly what to install and exits non-zero — it does **not** fail silently.
- **How it works.** Injects `PAGINATION_CSS` before `</head>`, then tries Playwright, then WeasyPrint.
- **Exit codes.** `0` success · `1` input not found · `2` usage · `3` no backend available.

### `md2pdf.py`
- **What it does.** Converts Markdown to HTML (using the `markdown` package if installed, otherwise a
  minimal built-in converter for headings/lists/code/paragraphs), wraps it in a neutral stylesheet, and
  hands it to `html2pdf.py`.
- **When to use it.** For reports/notes/minutes authored in Markdown that need a PDF.
- **Usage.** `python md2pdf.py input.md [output.pdf]`
- **Inputs / Outputs.** One `.md` → one `.pdf` (intermediate `.md.html` is created and removed).
- **Dependencies.** Optional `markdown`; the same PDF backend as `html2pdf.py` (it shells out to it).
- **Exit codes.** Propagates `html2pdf.py`'s codes (`0/1/2/3`).

### `gen_index.py`
- **What it does.** The **P7 index generator**. Scans each content chamber (`A_REFERENCE`, `B_OPERATIONS`),
  derives every folder's family/kind from its name, reads a one-line summary from each folder's README (or
  the named CORE doc), and regenerates that chamber's `index.json` (machine) and `index.html` (human).
- **When to use it.** After **any** structural change, configuration step or promotion — the indexes are
  generated artefacts and must never be hand-edited (governance P7).
- **Usage.** `python gen_index.py` (no arguments; it locates `shared/` from its own path).
- **Inputs.** The live folder tree under `shared/A_REFERENCE` and `shared/B_OPERATIONS`.
- **Outputs.** `A_REFERENCE/{index.json,index.html}` and `B_OPERATIONS/{index.json,index.html}`.
- **Dependencies.** None (standard library only).
- **Exit codes.** `0` on success.

---

## 4. Conventions for every tool

- **UTF-8, no BOM**, read and write. Never a platform default codec.
- **No business state.** Org-specifics come from `08_CORE_Profile`, never hard-coded in a tool.
- **Self-documenting.** Running a tool with no arguments prints its usage header.
- **Local side effects only.** A tool writes its declared output and nothing else (except `gen_index.py`,
  which regenerates the two index files by design).

## 5. How to add a new tool

1. Confirm it does not already exist here (this is the canonical home of production scripts).
2. One responsibility; read a file → write a file; standard library first; detect optional deps at runtime
   with a clear install message.
3. Add a top docstring usable as `--help`/no-arg output, then a **detailed card in §3 above** (what / when /
   usage / inputs / outputs / dependencies / how it works / exit codes).
4. If it transforms documents, slot it into the pipeline diagram in §1.
5. If it exposes a capability other agents should discover, also register it in
   [`../_SERVICES/`](../_SERVICES/README.md).

> Relationship to the rest of the kit: **`_TOOLS`** = local scripts you *run*; **`_SKILLS`** = instructions
> you *follow*; **`_SERVICES`** = external/available capabilities (skills & MCP) you *call*; **`_RESOURCES`**
> = assets you *reference*; **`B_OPERATIONS/_OUTPUT`** = the heavy files these tools *produce*.
