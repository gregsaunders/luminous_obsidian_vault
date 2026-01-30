---
status: "Not Started"
priority: "Critical"
assigned: ""
dependencies: []
linear_id: "SQU-16"
---

# Feature 1.0: Luminous Platform Group Scaffolding

**Linear:** [SQU-16](https://linear.app/squarehead/issue/SQU-16)

---

## Outcome

A tenant administrator can install the Luminous platform group and see it available in their workspace.

---

## What Success Looks Like

- Admin navigates to platform group catalog
- Selects "Luminous" and installs it
- Luminous appears in navigation
- No data yet, but structure is ready

---

## Scope: Owned Files

- `apps/platform_groups/luminous/`

---

## Requirements

- `apps/platform_groups/luminous/` directory structure follows CRM patterns
- `manifest.yaml` defines core models with required fields
- `ui_hints.yaml` skeleton is in place for future views
- `relationship_types.yaml` defines sample→result linking
- `workflows/` directory is ready for future agent definitions
- Luminous is registered in platform group catalog and installable
- Barcodes can be pre-registered before kit shipment (active in system before field use)
- Kit batches track which barcodes were prepared together
- Test fixtures exist in `apps/platform_groups/luminous/tests/conftest.py`
- E2E test command is available at `apps/platform_groups/management/commands/e2e_luminous.py`
- Test data seeding script generates realistic sample/result data

**Reference:** `apps/platform_groups/crm/` for structure and patterns
