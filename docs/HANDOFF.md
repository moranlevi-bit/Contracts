# Contract.ly — handover for the next session

Read this first. It summarizes where the project stands and what to do next.

## Where things are

- **Live app (claude.ai artifact):** https://claude.ai/artifact/SYRtn3guQoLa9415cB7ZvZ
- **Source:** `app/contract-ledger.html` (single-file app), repo `moranlevi-bit/Contracts`, branch `claude/busy-galileo-i27dfg`
- **Logo files:** `app/brand/` (from the "Contract.ly Logo Kit" artifact https://claude.ai/artifact/HjGiMjzbkNM1LmU3bcMbvr)
- **MVP definition:** `docs/MVP Definition - Contract.ly.docx`; build status: `docs/MVP-status.md`
- **The user** is the product owner and not a developer: explain in plain language, step by step.
- **Republishing:** publish `app/contract-ledger.html` to the artifact URL above (pass `url`), omit `capabilities` to keep them
  (`db`, `user` with profile scope, `sample`, `downloads`). The live version may have been retitled from elsewhere: merge, don't overwrite.

## Data (artifact database, per user)

`data/users/<userId>/promisely` (ledger doc: `myCompany`, `users`, `settings`, `auto`, `outbox`, `savedReports`), with collections
`contracts`, `audit`, `chats`, `feedback`. Each contract has `area` (customers / suppliers / hr), `org`, `fields{}`
(value, quote, page, verification state), `obligations[]` (`side` mine = Commitment, theirs = Contractual obligation; due,
recurrence, amount, conditional, status, owner, note, history), `keyDates`, `documents`, `grants`, `activity`, and for messaging
`contactName`, `contactEmail`, `responsibleId`, `commPlan {rows: [{oid, send, kind, daysBefore, subject, body, reason}]}`.
Outbox items: `{id, key, cid, oid, due, kind, to, subject, body, approverId, status: awaiting|approved|denied|sent}`.

## What the app does today

- Design: CRM-style (white header, tab bar with carets, ring-chart cards, bottom bar with Ask the AI / To Do List / Outbox).
  The user rejected minimal redesigns: keep this look.
- Wording: **Commitments** (what we must pay or do) and **Contractual obligations** (what others must pay or do for us).
- Home: Commitments Total, Contractual obligations Total, Bonuses to Apply, Customers / Suppliers / HR boxes, Renewal Pipeline.
- Tabs: Home, Contracts (all permitted contracts; add / edit; delete is Administrator-only), Customers, Suppliers, HR
  (each with sub-tabs **Contracts** and **Deliverables & Milestones** = non-money duties as a Gantt timeline with tick-to-complete),
  Reports, Admin.
- Commitments / Contractual obligations reports open with a payment **Gantt** timeline (the user prefers Gantt over bar charts).
- All reports export to PDF (with logo), Excel and CSV.
- Ask the AI: short answers, shows the start of each answer, agentic tools (mark paid/done, dispute, owner, note,
  add obligation, add reminder, open page) — every change needs Approve / Decline in the chat.
- Upload: PDF, Word, images, or a saved email (.eml) with the contract attached; the AI picks Customers / Suppliers / HR.
- Automatic messages (Admin → Automatic messages): the AI plans each contract's messages (Messages tab on the contract);
  drafts go to the **Outbox** for the responsible administrator to Approve / Deny / Edit. Sending is currently manual
  ("Send from my email").

## The goal for the next session: email without logging in

The user wants Contract.ly to work by email with **no one logging in**:

1. Contracts emailed to a system address are uploaded, read and filed (customer / supplier / HR) automatically.
2. The AI decides the reminders / POs / notices per contract (they differ by contract).
3. Before anything goes to a customer or supplier, the contract's responsible administrator gets an **approval email**
   showing the exact message, with **Approve / Deny / Edit** buttons.
4. Approved messages are sent to the customer automatically.

**Prototype plan agreed with the user (Gmail + a scheduled Claude task):**

- The user is connecting **Gmail** at https://claude.ai/customize/connectors and will give the address to use
  (plan: plus-addressing such as `name+contractly@gmail.com` as the "system address").
- First, test what the Gmail connector can do in this session: search and read messages, read attachments (PDF),
  send vs. only create drafts. Report the result to the user before building.
- Then create a scheduled task (hourly or daily, connector: Gmail) that:
  - reads new emails to the system address, extracts attached contracts and writes them into the artifact database
    (same record shape the app creates), planning messages too;
  - for due items, emails the responsible administrator an approval request; buttons are `mailto:` reply links such as
    "APPROVE #id" / "DENY #id"; Edit = reply with the corrected text;
  - reads the replies and sends approved messages (or drafts them if the connector can't send), updating Outbox status
    and the contract's activity log.
- Be honest about limits: runs on a schedule (not instant), sends from the user's own Gmail, uses the user's Claude usage.

**Production (later):** own server and database, an email service (e.g. Postmark) with a domain, a Claude API key,
signed one-click links. See the conversation summary in this file's git history for details.
