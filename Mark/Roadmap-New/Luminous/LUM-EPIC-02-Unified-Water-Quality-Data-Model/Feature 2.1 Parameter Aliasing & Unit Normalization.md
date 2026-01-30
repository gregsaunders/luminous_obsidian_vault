---
status: "Not Started"
priority: "Critical"
assigned: ""
dependencies:
  - "Feature 2.0"
linear_id: "TBD"
---

# Feature 2.1: Parameter Aliasing & Unit Normalization

**Linear:** TBD

**Used By:**
- Feature 2.3 (ETL Pipelines) - alias resolution during import
- Feature 2.4 (Query Services) - canonical parameter lookup

---

## Outcome

Source-specific parameter codes automatically resolve to canonical parameters, and units normalize to standard bases during import and query.

---

## What Success Looks Like

- "Calcium Dissolved" (Wetland), "Ca" (JOSM), "Calcium (D-IC)" (Federal) all resolve to canonical "Calcium"
- Query by canonical name returns measurements from all sources
- Unit conversion handles mg/L ↔ ug/L with precision preservation
- Admin can review and approve new alias suggestions

---

## Context

The four data sources use different naming conventions for the same parameters. Rather than forcing users to know source-specific codes, the system maps aliases to canonical parameters.

---

## Scope: Owned Files

- `apps/platform_groups/luminous/models/water_quality/parameter_alias.py`
- `apps/platform_groups/luminous/services/aliasing.py`

---

## Tasks

- [ ] Create ParameterAlias model mapping source codes to canonical parameter IDs
- [ ] Implement unit conversion registry with bidirectional rules
- [ ] Build confidence scoring for alias mappings (exact, synonym, inferred)
- [ ] Create admin interface for alias review/approval workflow
- [ ] Implement audit log for alias changes
- [ ] Seed initial alias mappings from research document tables
