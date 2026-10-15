# Contract.ly MVP – prototype status

The prototype lives in `app/contract-ledger.html` (published as a claude.ai artifact).
Section numbers refer to "MVP Definition – AI Contract Management" v0.1.

## Built in the prototype
- **5 Contract areas:** Customers, Suppliers and HR tabs, each with its own fields, list, filters and default visibility. Contracts can be moved between tabs.
- **6.1 Upload:** drag and drop or file picker, several files at once. Accepts PDF (text or scanned), .docx and page images. The tab is chosen at upload or suggested by the AI, with an optional counterparty. Amendments, addenda and exhibits can be attached. Duplicates are detected with a SHA-256 hash. A status shows each step: Uploaded → Reading → Extracting → Ready for review. Each document is listed under the contract.
- **6.2 Extraction and review:** every field stores its value, source passage, page and confidence. Quotes are checked against the contract text; a quote that isn't found is marked low confidence. The review screen shows the contract text beside the fields, with highlighting. Reviewers can confirm, edit or reject a field, bulk-confirm high-confidence fields, and resolve conflicts from amendments. Fields the contract doesn't contain show "Not found". Every change is saved with the user and time. Unverified data is labeled everywhere, including in reports.
- **6.3 Ask the AI:** a chat for each contract and for each tab, plus a global chat. Answers must cite the counterparty, page and quote. Totals come from a deterministic `calculate_money` tool, and the calculation is shown. Each answer can be marked helpful or wrong; wrong answers are logged. Chat history is saved per user. The AI sees only contracts in the user's scope.
- **6.4 Obligations:** "we owe" and "they owe us" are two separate panels and are never netted. An obligation can be received, paid, done or disputed. Recurring items roll forward to the next due date. Each item has an owner, notes, grace period and late terms, a condition, and a link to its source. Fixed and conditional amounts are kept separate. Calendar view. Export to Excel or CSV.
- **6.5 Home dashboard:** We owe / They owe us for the next 30 days; expected income and payments for 30 days, 90 days and the quarter (fixed versus conditional); renewals and notices; items needing attention; contracts needing review; counts by tab and status; top counterparties. Every widget is clickable.
- **6.6 Reports:** all 8 standard reports, with filters for tab, counterparty, date range, status, verified-only and responsible party. Export to PDF, Excel or CSV, showing the generation date and an "unverified data" flag. Reports can be saved and re-run.
- **6.7 Access:** five roles and the permission matrix. Contracts can be shared at View, Edit or Manage level with a user or group, and restricted to named people. HR is hidden by default. Admins get an access review with one-step removal and an audit log. "Preview as" shows what any user would see.
- **8 AI quality:** the AI cites every value, says "not found" instead of guessing, relies on human confirmation, calculates totals in code, applies amendments, treats contract text as untrusted, and shows a "not legal advice" notice.

## Needs the production build (server)
- Real organizations, user invitations, sign-in, MFA and SSO. Server-side enforcement of every permission, including search and AI. Tenant isolation.
- Email reminders and scheduled report emails. In-app reminders already exist.
- Virus scanning, file storage with short-lived links, backups, retention and deletion schedules, encryption at rest, rate limiting.
- An accuracy test set and per-release measurement (section 8, "Measure and improve").
