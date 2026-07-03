---
# ILLUSTRATIVE EXAMPLE (skill service) - delete or replace on configuration.
id: official-documents
kind: skill
status: available
owner: role:operations
summary: "Produce an official document and deliver it as PDF / embedded HTML."
skill_ref: ../_SKILLS/skill_official_documents.md
auth: none
scopes: []
requires_confirmation: false
---

# Official documents (example skill service)

## Purpose
Exposes the document-production capability as a discoverable service: draft an official document in
lightweight HTML, then generate the heavy deliverable. Reach for it whenever the organisation needs a
report, minutes, memo, record card or email produced to brand.

## How to use
Follow the instruction body in [`../_SKILLS/skill_official_documents.md`](../_SKILLS/skill_official_documents.md).
In short: write the working HTML (logos *referenced* from `_RESOURCES`) → `embed_images.py` → `html2pdf.py`
→ `B_OPERATIONS/_OUTPUT/`, leaving a stub+pointer in `03_WORK_Flow` if it is evidence.

## Interface
| Step | Input | Output |
|------|-------|--------|
| draft | document content + type | lightweight HTML in the right working dir |
| produce | the working HTML | PDF / embedded HTML in `_OUTPUT/` |

## Auth & config
None. Visual identity (which logos, placement, tone) comes from `08_CORE_Profile`.

## Limits
Advise/produce only; sending the result is a separate, human-approved step (`02_WORK_Outbox`). Anonymise
before any public-cloud step (`04_CORE_Governance`).

## Source
`_SKILLS/skill_official_documents.md`, using `_TOOLS/embed_images.py` + `_TOOLS/html2pdf.py`.
