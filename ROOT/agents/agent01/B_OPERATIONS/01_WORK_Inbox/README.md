# 01_WORK_Inbox - all received messages

> **5W2H - WORK ->** Every message that arrives, through any channel, lands here as one **immutable** file. This is the single front door of the memory.

**Naming.** `yymmdd_hhmmss_CHANNEL_SenderId_Subject.html`

```
260701_102311_EMAILops_acmeco_RequestQuoteRenewal.html
```
= a message received at 10:23:11 on 2026-07-01 by the EMAIL account `ops`, sent by `acmeco` (a supplier organisation), subject "request a quote renewal".

**Fields.**
- `CHANNEL` - the intake channel. Default catalogue (set in `08_CORE_Profile` / `15_WHAT_Catalogs`): `EMAIL WHATSAPP TELEGRAM PHONE VIDEOCONF INPERSON`. The channel is often written together with the receiving account (`EMAILops` = the EMAIL account *ops*).
- `SenderId` - short id of who sent it, with their org (`acmeco`).
- `Subject` - CamelCase, no spaces/accents.

**Rules.**
- One file per message; **immutable** once written (it is the received record).
- At intake the message is **classified** and routed to the right expediente under `03_WORK_Flow` (triage is an action here, not a separate folder). Low confidence -> leave it in the Inbox flagged for human triage; **never delete**.
- The outgoing counterpart is `02_WORK_Outbox` (symmetric I/O pair).

**Status.** Empty in the template. Populate when this organisation is configured (`08_CORE_Profile` + `C_OPERATIONAL_KIT/_SKILLS/CONFIG_QUESTIONS.md`).
