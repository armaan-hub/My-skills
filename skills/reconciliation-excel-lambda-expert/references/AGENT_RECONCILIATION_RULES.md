# Shared Rules for Reconciliation Agents

**Required reading for every agent working on a ledger, reconciliation workbook, or related report in this project.** Read this file before analysis or implementation. Use [Al_Hilal_Reconciliation_Explained.xlsx](Reconciled%20Ledger/Al_Hilal_Reconciliation_Explained.xlsx) as the current presentation example.

## 1. Follow the user's scope and keep accounts separate

- Follow the latest user instruction for company, ledger, period, and output. Work on one company or ledger at a time unless the user asks to compare more.
- Keep different companies, account codes, and statement sections separate. Never net or combine them just because they are in one source file.
- Reuse the Al Hilal report's layout and controls, not its account IDs, grouping assumptions, or labels. Inspect each new ledger and map its real fields first.
- Do not silently move an entry to a customer, property, account, or reference based on its description. Preserve the source values and flag inconsistencies for review.

## 2. Build a simple Main Report linked to entry-level detail

Use the Al Hilal workbook as the default layout unless the user requests another format.

- Put **Main Report** first. Show one row per non-zero comparison group, the account/ledger, the source reference, the property or unit as printed, total debits, total credits, debit remaining, credit remaining, **Evidence in the ledger**, **What to check next**, and a link to the entries.
- Use plain language. Define any source abbreviations that are not explained in the source. Do not introduce accounting terms without a short explanation.
- Keep all source rows in **Entry Details**, including zero-net groups. Preserve source row number, exact description, date, voucher/type, cheque number/date, account, debit, credit, and printed balance where available.
- Give each group a stable, visible Group ID. Use it as the key for formula totals and links between sheets. A summary link should land on a matching detail row; users should be able to filter details by Group ID.
- Use formulas to connect summary totals and remaining amounts to details. Save formula results for preview apps, and avoid broken references such as `#REF!`.
- Include separate close checks for every account/section. Show each section's debits, credits, calculated close, printed source close, difference, and status. Do not combine close checks across accounts.

## 3. Explain each difference from the source

- For each non-zero group, state the source row numbers, entry types, debit/credit amounts, and relevant descriptions, references, cheque dates, or source-field differences that explain the arithmetic.
- Separate two things: **what the ledger shows** and **what still needs evidence**. Name the next document or check, such as an invoice, lease/unit schedule, receipt, bank statement, cheque image, journal support, or allocation schedule.
- Do not use generic filler such as “No source-field conflict noted.” If the source does not explain the cause, say what is visible, what remains unexplained, and what evidence is needed.
- Treat description-based clues as review prompts. Do not relabel, reallocate, remove, or net entries without evidence and an explicit basis.
- Where the evidence is incomplete, state the uncertainty plainly. Do not invent a root cause to make the report sound conclusive.

## 4. Do not claim settlement or propose unsupported entries

- Ledger debits and credits show postings. They do not by themselves prove that an invoice was received or paid, a cheque cleared, cash was received, a line is a duplicate or reversal, or money is legally owed.
- Confirm settlement and allocation from independent support, such as bank records, invoice/lease documents, remittance advice, or approved journal documentation.
- Do not recommend or post an adjusting journal entry based only on a remaining ledger difference. If the user requests an AJE, show the evidence, balanced debit/credit, rationale, and approval/support required; otherwise record the item as an open check.
- Do not use a modulo-9 result or fuzzy description match as proof of a transposition, duplicate, or transaction match. Treat such signals as leads to investigate.

## 5. Verify before delivery

The preparer and the independent reviewer should check:

1. Source file, worksheet, date label/cutoff, account sections, and source row count.
2. Every source row is retained once, with source identifiers and amounts preserved.
3. Every Main Report Group ID has detail rows; every detail row has a Group ID; no non-zero group is omitted.
4. Each group's debit, credit, debit remaining, and credit remaining independently recompute from its detail rows.
5. Running balances and source-balance differences tie by source order; sorting/filtering must not change the calculated ledger order.
6. Formula results are present, links point to the correct Group ID, and there are no formula errors or `#REF!` references.
7. Every account section ties separately to its printed close, or the difference is clearly reported.
8. Evidence notes are factual, next checks are actionable, and the report does not claim settlement without support.

Have the Excel/model reviewer check formulas and navigation, the internal-control reviewer check allocation and process risks, and the external-audit reviewer challenge source support and conclusions. Resolve review comments against the exact saved output and confirm that all summary rows—including the first data rows—were included in the review scan.

## 6. Record the work for the next ledger

- Append the scope, source file/cutoff, account boundaries, grouping method, row counts, separate close results, key evidence clues, unresolved support, verification, and reviewer disposition to `RECONCILIATION_ACTIVITY_LOG.md`.
- Update `SCALING_TO_400_LEDGERS.md` only with a working method validated on an actual ledger. Keep unimplemented automation labeled as conceptual.
- Preserve previous company workbooks and source files unless the user specifically asks to replace them. Deliver a clearly named, company/ledger-specific workbook.
- Default to the linked Main Report + Entry Details pattern in the Al Hilal example. Follow any newer user request if they ask for a smaller or differently structured output.

## Priority when instructions differ

Follow this order: **latest user scope → these shared project rules → agent role profile → generic templates or assumptions**. Raise a conflict to the manager/coordinator; do not silently merge companies, accounts, or unsupported conclusions.
