# Default skill · Produce the organisation's official documents

**Goal:** generate an official document (report, minutes, memo, record card, email) with the correct
visual identity and deliver it in the right format.

## 1. Draft in lightweight HTML (work)

- Write the document as **lightweight HTML** in the working directory that fits its type (e.g. meeting
  minutes are evidence → `B_OPERATIONS/03_WORK_Flow`; a process card → `A_REFERENCE/30_HOW`).
- **Logos and images are REFERENCED** from `_RESOURCES/` (not embedded):
  `<img src="../_RESOURCES/logos/primary.svg">`. This keeps the working document light.
- Place the logos **as the profile says** (`08_CORE_Profile`): which ones, in what order, in which
  corner, at what size. (This is a per-organisation particularity — see `CONFIG_QUESTIONS.md`, block B/C.)

## 2. Generate the deliverable (with `_TOOLS`)

When the document is ready to send/archive:

1. **Embed images** → `_TOOLS/embed_images.py`: turns the HTML with **referenced** images into a
   **self-contained** HTML (images in base64). Essential for sending by **chat/email** (one file, no
   dependencies).
2. **Convert to PDF** (if needed) → `_TOOLS/html2pdf.py`: produces the PDF with careful pagination
   (no orphan headings, no widows).
3. The final (heavy) deliverable is stored **organised** in `B_OPERATIONS/_OUTPUT/`.

## 3. Delivery and trace

- The heavy file lives in `_OUTPUT/`; it does **not** go into the working directories (which stay light).
- If the document is **evidence** of something that happened/was sent, leave a **stub** (lightweight .md)
  in `B_OPERATIONS/03_WORK_Flow` with the `[Source:]` and a **pointer** to the heavy file in
  `_OUTPUT/` (stub+blob model). Do not duplicate the binary.

## 4. Flow summary

```
work HTML (logo referenced)  →  embed_images.py  →  self-contained HTML  →  html2pdf.py  →  PDF
                                                            └──────────────► _OUTPUT/ (deliverable)
                                                                              stub+pointer → 03_WORK_Flow
```

> When you adapt this skill for a real organisation, replace the generic placeholders with the real
> document types, the real logo placement, and the real tone/register declared in `08_CORE_Profile`.
