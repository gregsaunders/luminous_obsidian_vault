# Luminous 18-Sheet Excel Standard

**Version:** 3.0
**Date:** 2026-01-29
**Standard:** [FAST Standard Organisation](https://www.fast-standard.org/)

---

## Overview

This document defines the Luminous 18-sheet Excel architecture standard for financial models. Based on the FAST (Flexible, Appropriate, Structured, Transparent) methodology, this standard ensures:

- **Transparency**: All calculations visible in Excel formulas
- **Auditability**: Clear data flow from inputs to outputs
- **Interactivity**: User-adjustable inputs that recalculate in real-time
- **Scalability**: Portfolio-level aggregation via numerical prefixes

---

## Sheet Naming Convention

### Numerical Prefix Standard

All sheets use numerical prefixes (0-17) to ensure:
- Consistent tab sorting across workbooks
- Easy reference in formulas
- Portfolio aggregation compatibility

| Index | Sheet Name | Category | Purpose |
|-------|------------|----------|---------|
| 0 | `0_Cover` | Navigation | Model hub, status summary |
| 1 | `1_TOC` | Control | Table of contents, navigation |
| 2 | `2_Instructions` | Reference | Methodology, data sources, glossary |
| 3 | `3_Assumptions` | Input | ALL inputs consolidated (timing, site config, costs, testing) |
| 4 | `4_Scenarios` | Input | Value scenario definitions |
| 5 | `5_ServiceModels` | Input | Monte Carlo distribution parameters |
| 6 | `6_Calc_Timeline` | Calculation | Time series generation |
| 7 | `7_Calc_Stochastic` | Calculation | Random variable generation |
| 8 | `8_Calc_Value` | Calculation | Gated value calculations |
| 9 | `9_Calc_Costs` | Calculation | Cost calculations |
| 10 | `10_Calc_Sim` | Calculation | Data Table Monte Carlo (1000 iterations) |
| 11 | `11_PL_Monthly` | Output | Monthly P&L (placeholder for future) |
| 12 | `12_PL_Annual` | Output | Annual projections |
| 13 | `13_CashFlow` | Output | Cumulative projections, NPV |
| 14 | `14_UnitEconomics` | Output | Cost/value per m³, breakeven analysis |
| 15 | `15_Sensitivity` | Calculation | Tornado analysis |
| 16 | `16_Dashboard` | Output | Executive summary, KPIs |
| 17 | `17_Checks` | Validation | Integrity checks |

---

## Tab Color Scheme

Visual categorization by sheet type:

| Category | Color | RGB | Sheets |
|----------|-------|-----|--------|
| Navigation | White | `#FFFFFF` | 0_Cover |
| Control | Yellow | `#FFFF00` | 1_TOC |
| Reference | Gray | `#808080` | 2_Instructions |
| Input | Yellow | `#FFFF00` | 3-5 (Assumptions, Scenarios, ServiceModels) |
| Calculation | Blue | `#4472C4` | 6-10, 15 (Calc_*, Sensitivity) |
| Output | Green | `#70AD47` | 11-14, 16 (PL_*, CashFlow, UnitEconomics, Dashboard) |
| Validation | Red | `#FF0000` | 17_Checks |

### User-Editable Indicators

- **Yellow fill** (`#FFFF99`) on cells that users can modify
- Input sheets (3-5) contain all user-editable cells
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
[INPUT SHEETS]           [CALCULATION SHEETS]              [OUTPUT]

1_TOC ────────────┐
3_Assumptions ────┼──► 6_Calc_Timeline ───────────────┐
4_Scenarios ──────┤    7_Calc_Stochastic              │
5_ServiceModels ──┘    8_Calc_Value                   │
                       9_Calc_Costs                   ├──► 16_Dashboard
                       10_Calc_Sim                    │
                       15_Sensitivity ────────────────┤
                                                      │
                       12_PL_Annual ──────────────────┤
                       13_CashFlow ───────────────────┤
                       14_UnitEconomics ──────────────┘

                                      ▼
                                17_Checks ◄───────────────────────┘
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

- `6_Calc_*` through `10_Calc_Sim` - Calculation engine
- `15_Sensitivity` - Tornado analysis
- `17_Checks` - Validation logic

### Unprotected Sheets (Editable)

- `1_TOC` - Navigation
- `3_Assumptions` - All business assumptions
- `4_Scenarios` - Scenario definitions
- `5_ServiceModels` - Distribution parameters

### Cell-Level Formatting

- **Yellow fill** indicates user-editable
- **White/no fill** indicates calculated or reference

---

## Version Control

### Change Log Location

Sheet `2_Instructions` contains change log table:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
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
3. Creates all 18 sheets in numerical order (0-17)
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

---

## References

- [FAST Standard Organisation](https://www.fast-standard.org/)
- [Monte Carlo Data Tables Guide](https://chandoo.org/wp/data-tables-monte-carlo-simulations-in-excel-a-comprehensive-guide/)
- [Microsoft LET Function](https://support.microsoft.com/en-us/office/let-function)
- Kadlec & Wallace (2009) Treatment Wetlands, 2nd Ed.
- Zhang (2026) Long-Dated Environmental Liabilities in Oil Sands
