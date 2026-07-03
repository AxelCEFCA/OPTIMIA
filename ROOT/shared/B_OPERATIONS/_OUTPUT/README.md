# _OUTPUT — heavy generated output (deliverables)

**What goes here:** the **heavy generated files** to deliver/send/archive: **PDFs**, **embedded HTML**
(self-contained, images in base64), exports. It is the document **outbox**.

**What does NOT go here:** the **working** documents (those are lightweight HTML, living in their 5W2H
folder), the source assets (`C_OPERATIONAL_KIT/_RESOURCES/`), or the tools (`C_OPERATIONAL_KIT/_TOOLS/`).

## Why separate

Working directories stay **light** (referenced images). The heavy, self-contained material — which
duplicates and inflates — is concentrated **here**, outside the work, so the working structure is not
dirtied or grown uncontrollably.

## Suggested organisation

```
_OUTPUT/
├── <YYYY>/
│   └── <MM>/                    by date
│       ├── <yymmdd_ReportX>.pdf
│       └── <yymmdd_ReportX>_embed.html   (self-contained, for chat/email)
└── by_type/  (optional)         by type: reports/, minutes/, cards/, emails/
```
(Naming convention and organisation = an entity particularity; see `C_OPERATIONAL_KIT/_SKILLS/CONFIG_QUESTIONS.md` block D.)

## Operational nature

`_OUTPUT/` is **generated** (not source): it is rebuilt with the tools in `C_OPERATIONAL_KIT/_TOOLS/` from
the work. If a deliverable is **evidence** of something sent, leave a **stub** (lightweight .md) in
`B_OPERATIONS/03_WORK_Flow` with `[Source:]` pointing here (stub+blob model): the binary lives in
`_OUTPUT/`, the immutable trace in STATUS. In a real repository, `_OUTPUT/` is usually **gitignored**.
