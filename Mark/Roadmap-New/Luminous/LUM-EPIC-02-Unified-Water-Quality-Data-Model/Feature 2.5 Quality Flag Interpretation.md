---
status: "Not Started"
priority: "Medium"
assigned: ""
dependencies:
  - "Feature 2.3"
linear_id: "TBD"
---

# Feature 2.5: Quality Flag Interpretation

**Linear:** TBD

**Used By:**
- Feature 2.6 (Dashboard Views) - flag display and filtering

---

## Outcome

Quality flags display as human-readable explanations with consistent severity categorization across all four data sources.

---

## What Success Looks Like

- Hovering over a flagged value shows tooltip explaining the flag meaning
- User can filter to exclude "suspect" or "rejected" data
- Flag statistics dashboard shows data quality trends
- Cross-source flags map to common severity levels

---

## Context

Each data source uses different quality flag systems:
- **Federal**: L (below MDL), R (below RL), Q + QA codes
- **Provincial/Wetland**: Lab-specific codes (I, K, T, U from AITF; H, ND, NDR from AXYS)
- **JOSM**: Standard environmental (J=estimated, U=non-detect)

---

## Scope: Owned Files

- `apps/platform_groups/luminous/models/water_quality/quality_flag.py`
- `apps/platform_groups/luminous/services/flags.py`

---

## Tasks

- [ ] Create QualityFlagInterpretation model with source, code, meaning, severity
- [ ] Define severity levels: informational, caution, suspect, rejected
- [ ] Seed interpretation catalog from research document tables
- [ ] Implement API endpoint returning flag meanings for display
- [ ] Add flag severity filtering to query endpoints
- [ ] Create flag statistics dashboard (data quality over time)
- [ ] Document flag harmonization decisions
