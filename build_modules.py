from pathlib import Path

# We name the folders like "software modules" so they blend in at work!
FAR_MODULES = {
    "01-sys-framework": ["conceptual_framework", "financial_statements", "fair_value"],
    "02-core-assets": ["cash_and_receivables", "inventory_valuation", "fixed_assets_depreciation"],
    "03-liabilities-equity": ["current_liabilities", "bonds_and_notes", "leases_asc842", "stockholders_equity"],
    "04-revenue-ops": ["revenue_recognition_606", "long_term_contracts", "income_taxes_asc740"],
    "05-combinations": ["business_combinations", "consolidations", "foreign_currency"],
    "06-gov-nonprofit": ["state_local_government", "fund_accounting", "not_for_profit_reporting"]
}

TEMPLATE = """# {title}

## 1. PPT Core Concepts (Visual Architecture)
* **Key Framework:** 
* **Core Formula:** 

## 2. Textbook Nuances & Deep Dive
* 

## 3. Gleim Practice Traps & Edge Cases
* **Sim Alert:** 
* **MCQ Trap:** 

---
*Use the comment section below to log new mistakes or add daily study notes.*
"""

def build_repo():
    base_dir = Path("docs")
    for folder, topics in FAR_MODULES.items():
        folder_path = base_dir / folder
        folder_path.mkdir(exist_ok=True)
        for topic in topics:
            file_path = folder_path / f"{topic}.md"
            if not file_path.exists():
                title = topic.replace("_", " ").title()
                file_path.write_text(TEMPLATE.format(title=title), encoding="utf-8")
                print(f"Generated: {file_path}")

if __name__ == "__main__":
    build_repo()
    print("\nSUCCESS: Your stealth CPA study modules have been generated!")