---
name: Financial-Agents
description: Autonomous 6-Subagent Financial Audit Council & Data Analysis Engine for UAE Statutory Comparative Mainland Audit Reports, Trial Balance auditing, P&L mapping, corporate legal context integration, and mathematical verification.
---

# /Financial-Agents — Autonomous 6-Subagent Financial Audit Council

An autonomous, multi-agent AI council designed to analyze raw corporate financial statements and generate statutory UAE Comparative Mainland Audit Reports in full compliance with **IFRS / IFRS for SMEs**, **UAE Commercial Companies Law (Federal Decree-Law No. 32 of 2021)**, **UAE Corporate Tax Law (Federal Decree-Law No. 47 of 2022)**, and **Standard Spreadsheet / Excel Formula Calculation Rules** (`SUM`, `SUMIF`, `SUMIFS`, `GROUPBY`, `IF`, `MIN`, `SUBTOTAL`, `XLOOKUP`).

## Quick Trigger Commands
- `/Financial-Agents`
- `/financial-agents`
- `python3 run_audit_council.py --sample`

---

## 🏛️ The 6-Subagent Council Pipeline

When `/Financial-Agents` is invoked, execute the sequential 6-stage audit pipeline:

| Stage | Subagent | Role | Key Function & Formula Logic |
|:---:|:---|:---|:---|
| **1/6** | ⚖️ **Corporate Legal Extractor** | `legal_extraction` | Ingests Trade License & MOA (Document 3); extracts entity legal names (English & Arabic), License No., DET/DED authority, shareholding schedule (names, nationalities, shares, %, capital in AED), General Manager authority, and licensed activities. Verifies `=SUM(Shareholder_Capital) == Total_Capital` and `=SUM(Ownership_Percentages) == 100%`. |
| **2/6** | 📊 **Trial Balance Auditor** | `tb_audit` | Ingests Balance Sheet / Trial Balance (Document 1); audits debit/credit equilibrium (`=SUM(Debits) - SUM(Credits) == 0.00`), categorizes accounts into Current/Non-Current Assets and Liabilities via Excel aggregation functions (`=SUMIF(Category, "Assets", Amount)`, `=SUMIFS(...)`, `=GROUPBY(...)`), and audits provisions for 2025 and 2024. |
| **3/6** | 📈 **Profit & Loss Analyst** | `pl_analysis` | Ingests P&L Statement (Document 2); audits revenue streams (IFRS 15), Cost of Sales, G&A expenses, and computes 9% statutory UAE Corporate Tax using conditional Excel formulas: `=IF(Taxable_Profit > 375000, (Taxable_Profit - 375000) * 0.09, 0)`. |
| **4/6** | 📑 **Comparative Mainland Mapper** | `mainland_mapping` | Formulates the structured field-by-field mapping specification; enforces **2025 (Left Column) / 2024 (Right Column)** chronological presentation, `-` zero balance notation, Notes 1–29 index mapping, and field-level Excel formula allocations. |
| **5/6** | 🖋️ **Audit Report Synthesis Chair** | `report_synthesis` | Synthesizes the full statutory audit report: Corporate Directory, Independent Auditor's Report (Unqualified Opinion), SOFP, SOPL, SOCE, CFS (Indirect Method), and comprehensive Notes 1 to 29 embedding explicit calculation formulas in working schedules. |
| **6/6** | 🔍 **Audit Math Verification Critic** | `math_qc` | Performs adversarial line-by-line formula tie-out verification: $\text{Total Assets} = \text{Total Liabilities} + \text{Total Equity}$ ($0.00$ variance), Retained Earnings roll-forward, Statutory Reserve threshold check, and flags discrepancies. |

---

## 📋 Mandatory Statutory & Spreadsheet Calculation Rules

Every report produced by `/Financial-Agents` must adhere to these non-negotiable rules:

1. **Strict Chronological Presentation (2025-First)**:
   - **Column 1 (Left)**: **2025** (Current Reporting Period)
   - **Column 2 (Right)**: **2024** (Prior Comparative Period)
   - **Never reverse this order** across all statements (SOFP, SOPL, SOCE, CFS) and disclosure tables.

2. **Spreadsheet & Excel Formula Calculation Modeling**:
   - **Debit/Credit Parity**: `=SUM(Debit_Range) - SUM(Credit_Range) == 0.00`
   - **Balance Sheet Parity**: `=Total_Assets - (Total_Equity + Total_Liabilities) == 0.00`
   - **P&L Aggregation**: Subtotal categories with `=SUMIF(Account_Group, "Group_Name", Amount)` or `=GROUPBY(Account_Group, Amount, SUM)`
   - **Gross Profit**: `=Revenue - Cost_of_Sales`
   - **Operating Profit**: `=Gross_Profit - Total_GA_Expenses - Selling_Expenses + Other_Income`
   - **Corporate Tax Computation**: `=IF(Profit_Before_Tax > 375000, (Profit_Before_Tax - 375000) * 0.09, 0)`
   - **Statutory Reserve Transfer**: `=IF(Net_Profit > 0, MIN(Net_Profit * 0.10, MAX(0, Share_Capital * 0.50 - Existing_Reserve)), 0)`
   - **Retained Earnings Roll-forward**: `=Opening_RE + Net_Profit - Statutory_Reserve_Transfer - Dividends`

3. **Full Corporate Legal Context Integration**:
   - Company Name in English & Arabic.
   - Commercial License Number, Issuing Authority (Dubai DET), and Chamber of Commerce No.
   - Complete Shareholding Schedule: Shareholder Names, Nationalities, Share Counts, Ownership %, and Share Capital in AED.
   - General Manager powers and authorized signatory clauses integrated into Note 1.

4. **Standard Audit Zero Notation**:
   - Zero, nil, or unpopulated line items must be formatted as `-` (never left empty or written as `0.00` unless specifying a net variance).

5. **Complete Structure (Notes 1 to 29)**:
   - All 29 standard disclosure notes must be indexed, formatted with markdown tables, and properly referenced in the financial statement line items.

---

## 💻 Standalone Local CLI Execution

The audit council can be executed locally without external dependencies via the standalone runner:

### 1. Instant Sample Run
```bash
python3 run_audit_council.py --sample
```

### 2. Custom Client Documents
```bash
python3 run_audit_council.py \
  --doc1 path/to/balance_sheet_trial_balance.txt \
  --doc2 path/to/profit_loss.txt \
  --doc3 path/to/trade_license_and_moa.txt \
  --doc4 path/to/target_template_spec.txt \
  --output my_audit_report.md
```

### 3. OpenCode Zen Free Model Configuration
The runner connects by default to OpenCode Zen using the single pre-configured model:
- `laguna-s-2.1-free` (Default active model)

```bash
# Run with default OpenCode Zen model
python3 run_audit_council.py --sample

# Provide custom OpenCode key
python3 run_audit_council.py --sample --api-key "sk-..."
```

### 4. Local OpenAI Proxy / LM Studio / Ollama
```bash
python3 run_audit_council.py --sample \
  --provider proxy \
  --base-url "http://127.0.0.1:4001/v1" \
  --model "gpt-4o"
```

---

## 🧪 Unit Testing & Verification

Run the zero-dependency test suite to verify persona prompts, chronological constants, currency formatters, and mock streaming pipelines:
```bash
PYTHONPATH=Project_AccountingLegalChatbot python3 -m unittest audit_council_local/test_local_council.py
```

---

## 📁 Source Code & Directory Layout

- **Standalone Local Package**: `/Users/armaan/Analysis/Project_AccountingLegalChatbot/audit_council_local/`
- **CLI Runner**: `run_audit_council.py`
- **Sample Financial Datasets**: `audit_council_local/sample_data/`
- **FastAPI Backend Integration**: `Project_AccountingLegalChatbot/backend/api/council.py`
- **React Frontend Audit Dashboard**: `Project_AccountingLegalChatbot/frontend/src/components/Council/`
