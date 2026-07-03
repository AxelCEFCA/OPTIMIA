# 02_WORK_Outbox - all outgoing messages (human approval)

> **5W2H - WORK ->** Every message the organisation sends, through any channel, under human-in-the-loop approval. State = subfolder.

**Naming.** `yymmdd_hhmmss_CHANNEL_RecipientId_Subject.html` (same channel catalogue as the Inbox: `EMAIL WHATSAPP TELEGRAM PHONE VIDEOCONF INPERSON`).

**States (subfolders).** `1_PROPOSED -> 2_EDITING -> 3_APPROVED -> 5_SENT` (or `4_DISCARDED`). The agent proposes; the human decides. On SEND, a heavy copy is produced in `_OUTPUT` and the sent message stays here as the immutable record; the fact is emitted to the day's rollup (`12_STATUS_Daily`).

**Symmetric to `01_WORK_Inbox`** (the I/O pair).

**Status.** Empty in the template. Populate when this organisation is configured (`08_CORE_Profile` + `C_OPERATIONAL_KIT/_SKILLS/CONFIG_QUESTIONS.md`).
