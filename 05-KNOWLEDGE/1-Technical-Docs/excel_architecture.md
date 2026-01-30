# Luminous Excel Architecture Standard

**Version:** 3.1
**Date:** 2026-01-29
**Standard:** [FAST Standard Organisation](https://www.fast-standard.org/)

---

## Overview

This document defines the Luminous Excel architecture standard for financial models. Based on the FAST (Flexible, Appropriate, Structured, Transparent) methodology, this standard ensures:

- **Transparency**: All calculations visible in Excel formulas
- **Auditability**: Clear data flow from inputs to outputs
- **Interactivity**: User-adjustable inputs that recalculate in real-time
- **Scalability**: Portfolio-level aggregation via numerical prefixes
- **Extensibility**: New sheets can be added within each category

---

## Sheet Naming Convention

### Numerical Prefix Standard

Sheets use numerical prefixes organized by **category ranges**:

| Range | Category | Purpose |
|-------|----------|---------|
| 0-2 | Navigation/Control | Cover, TOC, Instructions |
| 3-5 | Input | Assumptions, Scenarios, Distributions |
| 6-19 | Calculation | All calculation engines |
| 20-29 | Output | P&L, Cash Flow, Dashboards |
| 30+ | Validation | Checks, Audits |

This range-based approach allows adding sheets within each category without restructuring.

### Core Sheets (Required)

These sheets form the minimum viable model:

| Index | Sheet Name | Category | Purpose |
|-------|------------|----------|---------|
| 0 | `0_Cover` | Navigation | Model hub, status summary |
| 1 | `1_TOC` | Control | Table of contents, navigation |
| 2 | `2_Instructions` | Reference | Methodology, data sources, glossary |
| 3 | `3_Assumptions` | Input | Primary inputs (timing, site config, costs) |
| 20 | `20_Dashboard` | Output | Executive summary, KPIs |
| 30 | `30_Checks` | Validation | Integrity checks |

### Standard Sheets (Typical Model)

A typical model includes these additional sheets:

| Index | Sheet Name | Category | Purpose |
|-------|------------|----------|---------|
| 4 | `4_Scenarios` | Input | Value scenario definitions |
| 5 | `5_ServiceModels` | Input | Monte Carlo distribution parameters |
| 6 | `6_Calc_Timeline` | Calculation | Time series generation |
| 7 | `7_Calc_Stochastic` | Calculation | Random variable generation |
| 8 | `8_Calc_Value` | Calculation | Gated value calculations |
| 9 | `9_Calc_Costs` | Calculation | Cost calculations |
| 10 | `10_Calc_Sim` | Calculation | Data Table Monte Carlo (1000 iterations) |
| 15 | `15_Sensitivity` | Calculation | Tornado analysis |
| 21 | `21_PL_Annual` | Output | Annual projections |
| 22 | `22_CashFlow` | Output | Cumulative projections, NPV |
| 23 | `23_UnitEconomics` | Output | Cost/value per m³, breakeven analysis |

### Adding New Sheets

When extending the model:

1. **Identify the category** (Input, Calculation, Output, Validation)
2. **Choose an available index** within the category range
3. **Follow naming convention**: `<Index>_<Category>_<Description>` or `<Index>_<Description>`
4. **Update the TOC** sheet with the new sheet reference
5. **Register in LOCATIONS** if using Python generator

**Examples of valid extensions:**
- `11_Calc_Reserves` - Additional calculation for reserve modeling
- `12_Calc_Emissions` - Carbon/emissions calculations
- `16_Calc_Regulatory` - Regulatory compliance calculations
- `24_PL_Monthly` - Monthly P&L detail
- `25_Waterfall` - Waterfall chart data
- `31_Audit_Trail` - Detailed audit logging

---

## Tab Color Scheme

Visual categorization by sheet type:

| Category | Color | RGB | Index Range |
|----------|-------|-----|-------------|
| Navigation | White | `#FFFFFF` | 0 |
| Control | Yellow | `#FFFF00` | 1 |
| Reference | Gray | `#808080` | 2 |
| Input | Yellow | `#FFFF00` | 3-5 |
| Calculation | Blue | `#4472C4` | 6-19 |
| Output | Green | `#70AD47` | 20-29 |
| Validation | Red | `#FF0000` | 30+ |

### User-Editable Indicators

- **Yellow fill** (`#FFFF99`) on cells that users can modify
- Input sheets (range 3-5) contain all user-editable cells
- Calculation and Reference sheets are protected

---

## Naming Conventions

### Named Ranges

Format: `<Category>_<Parameter>`

Examples:
- `Testing_Option` - Selected testing option
- `Discount_Rate` - Discount rate for NPV
- `Season_Length` - Operating season in days
- `Dist_SeasonExt` - Season extension distribution

### Table Names

Format: `tbl_<Description>`

Examples:
- `tbl_Timing` - Timing parameters
- `tbl_SiteConfig` - Site configuration
- `tbl_TestOptions` - Testing option reference
- `tbl_Timeline` - Projection timeline
- `tbl_Checks` - Validation checks

### Column Names in Tables

Use descriptive, CamelCase names:
- `Year_Index`, `Calendar_Year`
- `Discount_Factor`, `Learning_Mult`
- `S1_Value`, `S2_Value`, `S3_Value`, `S4_Value`
- `Gross_Value`, `Net_Annual`, `Cumulative_NPV`

---

## Data Flow Architecture

```
[INPUT: 3-5]             [CALCULATION: 6-19]               [OUTPUT: 20-29]

1_TOC ────────────┐
3_Assumptions ────┼──► 6_Calc_Timeline ───────────────┐
4_Scenarios ──────┤    7_Calc_Stochastic              │
5_ServiceModels ──┘    8_Calc_Value                   │
                       9_Calc_Costs                   ├──► 20_Dashboard
                       10_Calc_Sim                    │
                       15_Sensitivity ────────────────┤
                       [Additional Calc sheets...]    │
                                                      │
                       21_PL_Annual ──────────────────┤
                       22_CashFlow ───────────────────┤
                       23_UnitEconomics ──────────────┘
                       [Additional Output sheets...]

                                      ▼
                                30_Checks ◄───────────────────────┘
                                [Additional Validation sheets...]
```

### Flow Rules

1. **Inputs flow RIGHT** → Calculation → Output
2. **No backward references** from CALC to INPUT (except through named ranges)
3. **All hardcoded values** reside in sheets 3-5 only
4. **CALC sheets reference only** named ranges and LOCATIONS registry, never raw cell addresses

---

## Formula Best Practices

### Use Named Ranges

```excel
# Good
=[@Value] * Discount_Rate

# Bad
=B5 * 'INPUTS'!$C$10
```

### Use LET() for Complex Formulas

```excel
=LET(
    U, RAND(),
    MinVal, tbl_Distributions[@Min],
    ModeVal, tbl_Distributions[@Mode],
    MaxVal, tbl_Distributions[@Max],
    Fc, (ModeVal-MinVal)/(MaxVal-MinVal),
    IF(U < Fc,
        MinVal + SQRT(U * (MaxVal-MinVal) * (ModeVal-MinVal)),
        MaxVal - SQRT((1-U) * (MaxVal-MinVal) * (MaxVal-ModeVal))
    )
)
```

### Use Structured Table References

```excel
# Good (structured reference)
=INDEX(tbl_LearningCurve[Multiplier], [@Year_Index]+1)

# Bad (absolute reference)
=INDEX('3_Assumptions'!$D$5:$D$10, B5+1)
```

### INDEX/MATCH Over VLOOKUP

```excel
# Good
=INDEX(tbl_TestOptions[Cost_Per_Test],
       MATCH(Testing_Option, tbl_TestOptions[Option], 0))

# Acceptable but less flexible
=VLOOKUP(Testing_Option, tbl_TestOptions, 5, FALSE)
```

---

## Monte Carlo Implementation

### Data Table Method (Excel-Native)

1. Create iteration column (1-1000) in Column A of `10_Calc_Sim`
2. Place formulas referencing volatile cells in Row 4
3. Select range A4:H1004
4. Data → What-If Analysis → Data Table
5. Column Input Cell: MC Anchor cell in `3_Assumptions`

### Recalculation

- **Manual calculation mode** for performance
- **Ctrl+Alt+F9** forces full Data Table recalculation
- Each recalc generates new random draws

### Statistics from Monte Carlo

```excel
Expected_NPV: =AVERAGE('10_Calc_Sim'!B:B)
P10_NPV: =PERCENTILE.INC('10_Calc_Sim'!B:B, 0.10)
P50_NPV: =PERCENTILE.INC('10_Calc_Sim'!B:B, 0.50)
P90_NPV: =PERCENTILE.INC('10_Calc_Sim'!B:B, 0.90)
StdDev: =STDEV('10_Calc_Sim'!B:B)
Prob_Positive: =COUNTIF('10_Calc_Sim'!B:B, ">0") / 1000
```

---

## Checks Sheet Requirements

### Required Checks

| ID | Category | Check |
|----|----------|-------|
| CHK001 | Balance | Components sum correctly |
| CHK002 | Range | Discount rate within bounds |
| CHK003 | Range | Season length within bounds |
| CHK004 | Integrity | No #REF! errors |
| CHK005 | Integrity | No #NAME? errors |
| CHK006 | Integrity | Automatic calculation enabled |
| CHK007 | Sanity | NPV within reasonable bounds |
| CHK008 | Sanity | All costs positive |
| CHK009 | Logic | Gating rules consistent |
| CHK010 | MC | 1000 iterations present |

### Status Formula

```excel
Status: =IF([@Result]=TRUE, "PASS", "FAIL")
Health: =IF(COUNTIF(tbl_Checks[Status], "FAIL")=0,
            "HEALTHY", "REVIEW REQUIRED")
```

---

## Sheet Protection

### Protected Sheets (Locked)

- All Calculation sheets (index range 6-19)
- All Validation sheets (index range 30+)

### Unprotected Sheets (Editable)

- `1_TOC` - Navigation
- All Input sheets (index range 3-5)

### Cell-Level Formatting

- **Yellow fill** indicates user-editable
- **White/no fill** indicates calculated or reference

---

## Version Control

### Change Log Location

Sheet `2_Instructions` contains change log table:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 3.1 | 2026-01-29 | [Author] | Range-based indexing for extensibility, Core vs Standard sheets |
| 3.0 | 2026-01-29 | [Author] | FAST 18-sheet standardization, LOCATIONS registry |
| 2.0 | 2026-01-29 | [Author] | FAST migration, Excel-native MC |

### Version Naming

`<Major>.<Minor>` where:
- Major: Architecture changes
- Minor: Parameter updates, bug fixes

---

## Compatibility

### Target Versions

- **Excel 365** (recommended)
- **Excel 2021**

### Required Features

- LET() function
- LAMBDA() function (optional)
- Dynamic arrays (FILTER, SORT, UNIQUE)
- Data Tables

### Features to Avoid

- VBA macros (unless explicitly required)
- External data connections
- Power Query (unless data refresh needed)

---

## File Naming

Format: `<project>_<model_type>_model.xlsx`

Examples:
- `luminous_wetland_monte_carlo_model.xlsx`
- `luminous_pilot_npv_model.xlsx`
- `luminous_portfolio_summary_model.xlsx`

---

## Python Generator

The financial model is generated by `luminous_wetland_monte_carlo.py` which:

1. Uses a **LOCATIONS registry** to track all cell addresses
2. Generates formulas via `loc()` helper function
3. Creates sheets in numerical order based on index ranges
4. Writes formulas only - Excel performs all calculations

### LOCATIONS Registry Pattern

```python
LOCATIONS = {}

def loc(var_name: str) -> str:
    """Return Excel address for a named variable."""
    return LOCATIONS[var_name]

def register_location(var_name: str, sheet: str, col: str, row: int):
    """Register a variable's location for formula generation."""
    LOCATIONS[var_name] = f"'{sheet}'!${col}${row}"
```

This pattern eliminates brittle find/replace operations and ensures all cross-sheet references are tracked centrally.

### Adding New Sheets in Python

When extending the generator:

```python
# Define sheet indices at module level for clarity
SHEET_INDICES = {
    'Cover': 0,
    'TOC': 1,
    'Instructions': 2,
    'Assumptions': 3,
    'Scenarios': 4,
    'ServiceModels': 5,
    'Calc_Timeline': 6,
    'Calc_Stochastic': 7,
    # ... add new calculation sheets in range 6-19
    'Calc_NewFeature': 11,  # Example extension
    'Dashboard': 20,
    'PL_Annual': 21,
    'CashFlow': 22,
    # ... add new output sheets in range 20-29
    'Checks': 30,
}
```

---

## References

- [FAST Standard Organisation](https://www.fast-standard.org/)
- [Monte Carlo Data Tables Guide](https://chandoo.org/wp/data-tables-monte-carlo-simulations-in-excel-a-comprehensive-guide/)
- [Microsoft LET Function](https://support.microsoft.com/en-us/office/let-function)
- Kadlec & Wallace (2009) Treatment Wetlands, 2nd Ed.
- Zhang (2026) Long-Dated Environmental Liabilities in Oil Sands
