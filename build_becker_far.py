import shutil
from pathlib import Path

# Becker FAR Units mapped to "Software Feature Releases" for camouflage
BECKER_FAR_STRUCTURE = {
    "F1-System-Reporting": [
        "M1-Balance-Sheet-and-Income-Statement",
        "M2-Statement-of-Cash-Flows",
        "M3-Securities-and-EPS",
        "M4-Segment-and-Interim-Reporting",
    ],
    "F2-Balance-Sheet-Assets": [
        "M1-Cash-and-Accounts-Receivable",
        "M2-Inventory-Valuation-Models",
        "M3-Fixed-Assets-and-Depreciation",
        "M4-Intangibles-and-Impairment",
    ],
    "F3-Transaction-Logic": [
        "M1-Leases-ASC842-Architecture",
        "M2-Bonds-and-Long-Term-Debt",
        "M3-Stockholders-Equity-and-Comp",
        "M4-Revenue-Recognition-ASC606",
        "M5-Income-Taxes-ASC740",
    ],
    "F4-State-Local-Gov": [
        "M1-Gov-Accounting-Framework",
        "M2-Modified-Accrual-Logic",
        "M3-Gov-Budgetary-Accounting",
    ],
    "F5-Gov-Fund-Accounting": [
        "M1-Governmental-Funds",
        "M2-Proprietary-and-Fiduciary-Funds",
        "M3-Gov-Financial-Statements",
    ],
    "F6-Non-Profit-Accounting": [
        "M1-NFP-Revenue-and-Support",
        "M2-NFP-Financial-Statements",
        "M3-NFP-Health-and-Education",
    ],
}

# We use standard single strings joined together so syntax errors are impossible!
TEMPLATE = "\n".join(
    [
        "# {title}",
        "",
        "## 1. Executive Summary & Core Framework",
        "* **Overview:** ",
        "* **Key Accounting Standard:** ",
        "",
        "## 2. Deep-Dive Architecture (The No-Video Verbal Explanations)",
        "* *This section bridges the Becker PowerPoint slides with the textbook nuances.*",
        "",
        "## 3. Step-by-Step Journal Entries & Calculations",
        "```text",
        "Dr. Account Name                     $XX,XXX",
        "    Cr. Account Name                         $XX,XXX",
        "```",
        "",
        "## 4. Gleim & Becker Practice Traps (Sim & MCQ Edge Cases)",
        "* **MCQ Landmine:** ",
        "* **Simulation Alert:** ",
        "",
        "---",
        "*Use the discussion board below to log daily mistakes, notes, and progress.*",
    ]
)


def rebuild_becker_repo():
    base_dir = Path("docs")

    # Clean out the old dummy folders while keeping index.md
    if base_dir.exists():
        for item in base_dir.iterdir():
            if item.is_dir():
                shutil.rmtree(item)

    # Build the F1 > M1 hierarchy
    for unit, modules in BECKER_FAR_STRUCTURE.items():
        unit_path = base_dir / unit
        unit_path.mkdir(exist_ok=True)

        for mod in modules:
            file_path = unit_path / f"{mod}.md"
            title = mod.replace("-", " ")
            file_path.write_text(TEMPLATE.format(title=title), encoding="utf-8")
            print(f"Generated: {file_path}")


if __name__ == "__main__":
    rebuild_becker_repo()
    print("\nSUCCESS: Becker F1 -> M1 FAR Architecture successfully generated!")