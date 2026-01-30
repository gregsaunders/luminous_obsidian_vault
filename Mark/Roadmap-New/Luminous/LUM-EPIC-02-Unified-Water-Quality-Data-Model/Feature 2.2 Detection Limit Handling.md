---
status: "Not Started"
priority: "High"
assigned: ""
dependencies:
  - "Feature 2.0"
linear_id: "TBD"
---

# Feature 2.2: Detection Limit Handling

**Linear:** TBD

**Used By:**
- Feature 2.4 (Query Services) - statistical calculations
- Feature 2.6 (Dashboard Views) - visual indicators

---

## Outcome

Analysts can compute meaningful statistics even when 15-30% of measurements are non-detects, with clear documentation of methods used.

---

## What Success Looks Like

- Query for mean concentration includes detection limit handling method in response
- User can select substitution method (DL/2, DL/sqrt(2), Kaplan-Meier) at query time
- Charts visually distinguish detect vs non-detect values
- Percentile estimates account for censoring

---

## Context

Environmental data frequently contains "non-detect" values where the true concentration is below the instrument's detection limit. Statistical summaries must handle these appropriately.

---

## Scope: Owned Files

- `apps/platform_groups/luminous/services/detection_limits.py`
- `apps/platform_groups/luminous/services/statistics.py`

---

## Tasks

- [ ] Implement substitution methods: zero, DL/2, DL, DL/sqrt(2)
- [ ] Implement Maximum Likelihood Estimation for censored data
- [ ] Implement Kaplan-Meier estimation for highly censored datasets
- [ ] Add detection limit method parameter to query endpoints
- [ ] Tag query results with method used for transparency
- [ ] Calculate detection frequency summaries per parameter/station
