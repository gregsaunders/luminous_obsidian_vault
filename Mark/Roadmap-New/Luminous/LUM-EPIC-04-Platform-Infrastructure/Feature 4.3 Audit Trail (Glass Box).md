---
status: "In Progress"
priority: "Medium"
assigned: ""
dependencies:
  - "LUM-EPIC-01 Feature 1.1"
linear_id: "SQU-24"
---

# Feature 4.3: Audit Trail (Glass Box)

**Linear:** [SQU-24](https://linear.app/squarehead/issue/SQU-24)
**Status Note:** TerminusDB has capability

---

## Outcome

A regulator or auditor can request a complete history of all data changes for any biosensor record.

---

## What Success Looks Like

- Auditor requests history for a specific sample
- System shows every change: who, what, when
- Export as CSV/PDF for compliance documentation
- Data cannot be altered retroactively without trace

---

## Context

TerminusDB provides built-in versioning. This feature configures it for Luminous data and exposes the audit trail to users.

---

## Scope: Owned Files

- `apps/platform_groups/luminous/audit/` (audit views and exports)

---

## Requirements

- TerminusDB versioning is configured for all biosensor data
- Query interface allows retrieving audit history for any record
- Reports show "who changed what when" for any data point
- Audit logs can be exported for regulator review (CSV/PDF)
- Data retention policy is defined and enforced
- Regulatory audit dashboard visualizes full chain: Field Scan → Lab Receipt → Plate Reader → Platform Ingestion
