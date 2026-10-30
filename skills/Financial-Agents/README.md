# Financial-Agent-Skill 🏛️

**Autonomous 6-Subagent Financial Audit Council & Data Analysis Engine for Claude Code and Standalone Local CLI.**

Generates statutory UAE Comparative Mainland Audit Reports in full compliance with:
- **IFRS / IFRS for SMEs**
- **UAE Commercial Companies Law (Federal Decree-Law No. 32 of 2021)**
- **UAE Corporate Tax Law (Federal Decree-Law No. 47 of 2022)**
- **Standard Spreadsheet / Excel Formula Calculation Rules** (`SUM`, `SUMIF`, `SUMIFS`, `GROUPBY`, `IF`, `MIN`, `SUBTOTAL`)

---

## 🚀 Installation into Claude Code

Clone this repository directly into your Claude Code skills directory:

```bash
git clone https://github.com/armaan-hub/Financial-Agent-Skill.git ~/.claude/skills/Financial-Agents
```

Once installed, invoke the skill anywhere inside Claude Code:
```
/Financial-Agents
```
or
```
/financial-agents
```

---

## 🏛️ The 6-Subagent Council Pipeline

| Stage | Subagent | Role | Key Function & Formula Logic |
|:---:|:---|:---|:---|
| **1/6** | ⚖️ **Corporate Legal Extractor** | `legal_extraction` | Ingests Trade License & MOA; extracts legal entity names (English & Arabic), License No., DET/DED authority, shareholding schedule (names, nationalities, shares, %, capital in AED), General Manager authority, and licensed activities. Verifies `=SUM(Capital) == Total_Capital` and `=SUM(Percentages) == 100%`. |
| **2/6** | 📊 **Trial Balance Auditor** | `tb_audit` | Analyzes 2025/2024 Trial Balances, debit/credit parity (`=SUM(Debits) - SUM(Credits) == 0.00`), categorizes accounts via Excel aggregation functions (`=SUMIF(...)`, `=SUMIFS(...)`, `=GROUPBY(...)`), and audits provisions. |
| **3/6** | 📈 **Profit & Loss Analyst** | `pl_analysis` | Audits revenue streams, Cost of Sales, G&A expenses, and computes 9% Corporate Tax using conditional Excel formulas: `=IF(Taxable_Profit > 375000, (Taxable_Profit - 375000) * 0.09, 0)`. |
| **4/6** | 📑 **Comparative Mainland Mapper** | `mainland_mapping` | Enforces strict **2025-first / 2024-second** chronological presentation, Note indexing, `-` zero notation, and field-level Excel formula allocations. |
| **5/6** | 🖋️ **Audit Report Synthesis Chair** | `report_synthesis` | Synthesizes full statutory report: Corporate Directory, Unqualified Opinion, SOFP, SOPL, SOCE, CFS, and Notes 1–29 embedding explicit calculation formulas in working schedules. |
| **6/6** | 🔍 **Audit Math Verification Critic** | `math_qc` | Performs adversarial line-by-line formula tie-outs ($\text{Total Assets} = \text{Total Liabilities} + \text{Total Equity}$), checks retained earnings roll-forward, and flags discrepancies. |

---

## 💻 Standalone Local CLI Usage

Run without external dependencies using standard Python 3.9+:

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

### 3. OpenCode Zen Model Configuration
The runner comes pre-configured with the free OpenCode Zen model:
- `laguna-s-2.1-free` (Default active model)

```bash
# Run with default OpenCode Zen model
python3 run_audit_council.py --sample

# Run with custom API key
python3 run_audit_council.py --sample --api-key "sk-..."
```

### 4. Local LLM Proxy / LM Studio / Ollama
```bash
python3 run_audit_council.py --sample \
  --provider proxy \
  --base-url "http://127.0.0.1:4001/v1" \
  --model "gpt-4o"
```

---

## 📋 Mandatory Statutory & Spreadsheet Calculation Rules

1. **Strict Chronological Presentation**: Column 1: **2025** (Left), Column 2: **2024** (Right).
2. **Corporate Context Integration**: Entity Name (English/Arabic), DET License No., Shareholding breakdown, GM powers.
3. **Audit Zero Notation**: Nil / blank balances rendered as `-`.
4. **Spreadsheet & Excel Formula Modeling**:
   - $\text{Total Assets} = \text{Total Liabilities} + \text{Total Equity}$ ($0.00$ variance).
   - $\text{Net Profit} = \text{EBIT} - \text{Finance Costs} - \text{Corporate Tax (9\%)}$.
   - Retained earnings reconciliation matching dividends and 10% statutory reserve transfers (capped at 50% share capital).
   - Explicit spreadsheet formulas embedded in working schedules (`SUM`, `SUMIF`, `SUMIFS`, `GROUPBY`, `IF`, `MIN`).
5. **Notes 1 to 29**: Complete standard disclosures.

---

## 🧪 Unit Tests

Run the standalone unit test suite:
```bash
PYTHONPATH=Project_AccountingLegalChatbot python3 -m unittest audit_council_local/test_local_council.py
```

---

## 📄 License

MIT License.
