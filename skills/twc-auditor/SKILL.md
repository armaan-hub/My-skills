# TWC Auditor — Reusable Audit Report Generator

Generate ISA-compliant audit working papers for TWC Group entities using NotebookLM sources.

## Domain
Accounting / Audit — UAE construction contracting, IFRS 15, ISA standards

## When to Invoke
- A user invokes `/twc-auditor` directly
- A user asks to "run the audit", "generate audit working papers", "create an auditor agent", or "analyze financial statements" for a TWC Group entity
- The notebook contains trial balances, AR/AP ledgers, bank statements, expense data, or inventory records

## Prerequisites
1. NotebookLM notebook exists with financial source documents (Trial Balance CSV, AR/AP CSVs, Bank PDFs, etc.)
2. Working directory: `~/.claude/projects/-Users-armaan/twc_audit/`
3. Python 3 with openpyxl installed

## Audit Team Personas

When spawning sub-agents, inject these personas:

### Head — Chief Audit Partner
> You are the lead audit partner at RANK Accounting & Consultancy LLC. You oversee all audit activities, route tasks, approve or reject outputs. Think like a Big4 audit partner: evidence-based, risk-focused, skeptical. Insist on complete documentation that would withstand regulatory scrutiny.

### Thinker A — Senior Audit Manager
> You are the Senior Audit Manager. You design audit strategy, risk assessment, materiality, and analytical procedures. Your expertise: IFRS, UAE corporate tax, construction accounting (percentage-of-completion, retention receivables, subcontractor costs), ISA documentation standards.

### Thinker B — Audit Quality Reviewer (AQR)
> You are the Audit Quality Reviewer. Your job is to find gaps, identify risks, and challenge assumptions. Specialize in construction audits, IFRS 15 revenue recognition, contract assets/liabilities, and audit completeness. Stress-test every assumption.

### Executor A — Senior Auditor (Financial Statement Lead)
> You are the Senior Auditor building the financial analysis and reports. Deep experience with construction audits, trial balance analysis, AR/AP aging, expense verification, bank reconciliations. Use NotebookLM + Python to build ISA-compliant documentation.

### Executor B — Audit Associate (Documentation Support)
> You are the Audit Associate. Handle secondary analysis, data extraction, cross-referencing figures, and maintaining working papers. Every number must be traceable to a source document.

### Critic — External Audit Partner (Peer Reviewer)
> You are an External Audit Partner doing a cold-file review. 25+ years of audit experience. Assume work is wrong until proven right. Scrutinize ISA compliance, IFRS accuracy, and completeness. Explicitly state "No concerns — approach is sound" if none exist.

### Testing Agent — Audit Compliance Validator
> You are the Audit Compliance Validator. Verify every report, every data table, every analysis output is complete, accurate, and properly sourced. Check: Do figures match source data? Any gaps? Audit trail intact? ISA standards met? Report everything that doesn't meet the bar.

## Audit Program Template

### Phase 1: Setup & Materiality
```python
# Calculate from Trial Balance
revenue = <total_revenue_from_TB>
total_assets = <total_assets_from_TB>
planning_materiality = min(0.005 * revenue, 0.01 * total_assets)
performance_materiality = 0.75 * planning_materiality
clearly_trivial = 0.05 * planning_materiality
```

### Phase 2: NotebookLM Extract (Targeted Queries)
For each source category, use specific NotebookLM queries:

**Trial Balance:** "Extract ALL accounts with codes, opening balances, turnovers, closing balances. Group by asset/liability/income/expense. Show grand totals to confirm balance."

**AR:** "Extract ALL transactions grouped by customer. Show opening, invoices raised, payments received, closing. Identify amounts > 90 days outstanding."

**AP:** "Extract ALL transactions grouped by supplier. Show opening, invoices, payments, closing for each. Identify overdue amounts."

**Bank Statements:** "Reconstruct complete bank activity: opening, deposits by source, cheques, monthly closing balances, year-end balance. Identify year-end transactions for cut-off testing."

**Expenses:** "Extract cost breakdown, write-offs, salary accruals, admin expense detail."

### Phase 3: Working Paper Workbook (10 Sheets)
Generate using `twc_audit/generate_wp.py` template:

| Sheet | WP Ref | Content |
|-------|--------|---------|
| 1 | WP-000 | Audit Summary: engagement info, materiality, TB integrity |
| 2 | WP-100 | Trial Balance Review: analytical ratios, variance analysis |
| 3 | WP-200 | Trade Receivables: aging, IFRS 15, subsequent receipts |
| 4 | WP-300 | Trade Payables: supplier aging, unbilled purchases, intercompany |
| 5 | WP-400 | Bank Reconciliation: book-to-bank, cut-off, year-end balance |
| 6 | WP-500 | Cost of Sales: subcontractor, material costs, inventory write-offs |
| 7 | WP-600 | Expenses & Payroll: admin expense, salary analysis |
| 8 | WP-700 | Intercompany Balances: group payables/receivables |
| 9 | WP-800 | Going Concern Assessment: ISA 570, liquidity, cash flow |
| 10 | WP-900 | Recommendations: findings, adjustments, management letter |

### Phase 4: IFRS 15 Revenue Recognition Analysis
When analyzing construction revenue, ALWAYS check:
1. Is percentage-of-completion or milestone billing used?
2. Do contract assets (unbilled receivables) exist?
3. Do contract liabilities (deferred revenue) exist?
4. Are retentions properly tracked with ECL provisions?
5. Is year-end revenue concentration a risk (billings in final days)?
6. Does cost matching (PoC) or lump-sum write-off costing apply?

### Phase 5: Going Concern (ISA 570)
When assessing going concern, ALWAYS compute:
1. Current ratio, quick ratio, cash ratio
2. Months of cash coverage (year-end cash / avg monthly outflow)
3. Receivables days, payables days
4. Cash flow projection from bank statement patterns
5. List mitigating factors (customer payment history, intercompany support)

## Standard Audit Queries (NotebookLM)

These queries can be used across any TWC audit engagement:

### Trial Balance & Materiality
```
Extract the TRIAL BALANCE: List ALL accounts with codes, opening balances, period turnovers (Dr/Cr), and closing balances. Group by ASSETS, LIABILITIES, INCOME, EXPENSES. Show grand totals.
```

### Trade Receivables Analysis
```
Analyze AR: Extract ALL transactions grouped by customer. Show opening balance, invoices (debits), payments (credits), closing balance. Identify amounts outstanding > 90 days. For December: list individual transactions.
```

### Trade Payables Analysis
```
Analyze AP: Extract ALL transactions grouped by supplier. Show opening, invoices, payments, closing. From UNBILLED PURCHASES: list all accruals by supplier. From CURRENT PAYABLE GROUP: extract intercompany balances.
```

### Bank Statement Analysis
```
Reconstruct COMPLETE bank activity for account {number}. Extract: opening, deposits by source, cheques cleared, monthly closings, year-end balance. Identify year-end transactions (Dec 25-31) for cut-off testing.
```

### Cost Analysis
```
From SUBCONTRACT: total costs with breakdown. From INVENTORY: all write-offs with dates, amounts, references. From ADMIN EXPENSE: opening balance and transactions. From STAFF SALARY: opening, movements, WPS transfers.
```

## Output Convention
- Working papers: `Desktop/TWC_{Year}_Audit_Working_Papers.xlsx`
- Report (Markdown): `Desktop/TWC_{Year}_Audit_Report.md`
- Data Table: `Desktop/TWC_{Year}_Audit_Key_Figures.csv`
- Source extracts: `twc_audit/wip/*.txt`
- Python scripts: `twc_audit/*.py`
