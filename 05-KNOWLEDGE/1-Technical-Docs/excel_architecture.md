# Luminous FAST Excel Standard

**Version:** 4.0
**Date:** 2026-01-31
**Standard:** [FAST Standard Organisation](https://www.fast-standard.org/)

---

## Overview

This document defines the Luminous architecture standard for financial models. Based on the FAST (Flexible, Appropriate, Structured, Transparent) methodology, this standard ensures:

- **Transparency**: All calculations visible in Excel formulas
- **Auditability**: Clear data flow from inputs to outputs
- **Interactivity**: User-adjustable inputs that recalculate in real-time
- **Scalability**: Consistent structure across the portfolio
- **No Coordinate References**: Formula references must use semantic names, never grid addresses.

---

## Sheet Organization Principles

Models should use numerical prefixes to ensure consistent tab sorting and logic flow. While the exact number of sheets may vary based on model complexity, the following flow (Input -> Calculation -> Output) is mandatory.

### Standard Template (Reference Implementation)
The following is the recommended starting point for a full-scale commercial model, but should be adapted as needed.

| Index | Sheet Name | Category | Purpose |
|-------|------------|----------|---------|
| 0 | `0_Cover` | Navigation | Model hub, status summary |
| 1 | `1_TOC` | Control | Table of contents, navigation |
| 2 | `2_Instructions` | Reference | Methodology, data sources, glossary |
| 3 | `3_Assumptions` | Input | Primary inputs consolidated |
| 4 | `4_Scenarios` | Input | Value scenario definitions & selection |
| 5 | `5_ServiceModels` | Input | Detailed variable distributions/configs |
| 6+ | `Calculation Sheets` | Calculation | Logic blocks (Timeline, Stochastic, Value, Costs) |
| 10+ | `Simulation` | Calculation | Monte Carlo / Data Tables |
| 11+ | `Outputs` | Output | P&L, Cash Flow, Definitions |
| 15+ | `Analysis` | Output | Sensitivity, Dashboards |
| 99 | `Checks` | Validation | Integrity checks |

**Governance**: 
- **Sub-sheets** (e.g., `6b_Calc_Kinetics`) are permitted if they improve clarity or separate distinct logical phases. 
- **Re-indexing**: If inserting new sheets, ensure the numerical sequence remains logical (Input < Calc < Output).
- **Consolidation**: Avoid creating new sheets for single small tables; prefer standard consolidated sheets (`Assumption`, `Calculation`, `Output`) where possible.

---

## Technical Patterns (Python Generation)

### 1. Variables Strategy (No Coordinates)
Generators must maintain a strict separation between **Write-Locations** and **Read-References**.
- **Write**: The script knows where to put data (e.g., `ws['B5'] = 10`).
- **Read**: Formulas must ONLY reference Named Ranges (e.g., `=Season_Length * 5`).

### 2. Validation
- **Registry Check**: The generator should assert that every variable defined in external configuration (YAML) has a corresponding Named Range created in the Excel file.
- **Orphan Check**: Scan for Named Ranges that are never referenced in any formula.

---

## Key Financial Benchmarks (Base Case)
- **LTV:CAC Target**: >3x
- **CAC Payback**: <18 months
- **Gross Margin**: >60%
- **Break-Even Churn**: Calculated based on retention curves.
