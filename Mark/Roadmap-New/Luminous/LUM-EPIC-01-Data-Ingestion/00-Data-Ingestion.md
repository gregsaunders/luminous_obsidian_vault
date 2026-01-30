---
status: "Not Started"
priority: "Critical"
epic_id: "LUM-EPIC-01"
linear_id: "SQU-6"
linear_url: "https://linear.app/squarehead/issue/SQU-6/epic-02-data-ingestion"
---

# EPIC-01: Data Ingestion

**Linear:** [SQU-6](https://linear.app/squarehead/issue/SQU-6)
**Owner:** Greg
**Target:** Q2 2026 (Before Pilot)

---

## Vision

Lab technicians and field operators can submit biosensor data and sample metadata into the platform, with automatic linking and traceability from field collection to lab analysis.

---

## User Stories

- As a **lab technician**, I can upload plate reader results so that data enters the system without manual data entry
- As a **field operator**, I can record sample metadata at collection time so that results are linked to their source
- As an **analyst**, I can see the complete chain from field sample to lab result so that I can trust data provenance
- As a **data manager**, I can identify orphaned or unlinked records so that data quality issues are surfaced

---

## Context

Currently, lab results are exported from plate readers as Excel files and manually processed. Field metadata is recorded on paper or in separate systems. Linking samples to results requires manual barcode matching, which is error-prone and time-consuming.

This is the data foundation - nothing else works until data flows into the platform.

---

## Dependencies

- ⭐ **Foundational:** This EPIC enables LUM-EPIC-03 and LUM-EPIC-04
- 🔗 **Related:** LUM-EPIC-05 Feature 5.1 (field metadata flows into Feature 1.3)
- 🔗 **Platform:** [[../Squarehead/SQH-EPIC-03-Platform-Groups/00-Platform-Groups|SQH-EPIC-03 Platform Groups]]

---

## Features

- [[Feature 1.0 Luminous Platform Group Scaffolding]]
- [[Feature 1.1 Biosensor Results Data Model]]
- [[Feature 1.2 Lab Results Upload Pipeline]]
- [[Feature 1.3 Sample Metadata Linkage]]
- [[Feature 1.4 Contextual Data Integration]]
- [[Feature 1.5 Analysis Script Automation]]

---

## Open Questions

These questions should be resolved when developers are assigned to this epic:

### Barcode Management
1. **Barcode uniqueness** - How are barcodes guaranteed unique across customers/time? What is the generation strategy?
2. **Barcode lifecycle** - What happens when a barcode is damaged or lost? Can it be re-issued?

### Equipment & Format Stability
3. **Plate reader format stability** - What happens when a lab uses different equipment than PerkinElmer Victor? How do we handle multiple plate reader formats?
4. **Format versioning** - How do we handle plate reader firmware updates that may change export format?

### Data Synchronization
5. **Offline sync conflicts** - What if field metadata syncs AFTER lab results are uploaded? What is the reconciliation workflow?
6. **Late metadata handling** - Is it acceptable to have lab results without field metadata for some period? How long?

### QC & Validation
7. **QC failure workflow** - What happens when a batch QC fails? Quarantine? Manual review? Notification workflow?
8. **Partial batch handling** - Can some samples in a batch pass QC while others fail?

### Analysis Validation
9. **Analysis script validation** - Who validates that the Python implementation matches Excel macros exactly? What is the acceptance criteria?
10. **Calculation drift** - How do we detect if Excel macros are updated without corresponding Python updates?

### Data Volume
11. **TerminusDB data volume** - Will TerminusDB hit performance limits with biosensor data growth? At what volume should we consider PostgreSQL migration?

---

## Data Flow Diagram

```
Field                    Lab                      Platform
─────                    ───                      ────────
Sample collected    →    Sample received     →    Metadata uploaded
  ↓                        ↓                         ↓
Barcode scanned     →    Plate reader run    →    Results uploaded
  ↓                        ↓                         ↓
Metadata captured   →    CSV exported        →    Barcode linked
                                                     ↓
                                              Dashboard displays
```

---

## References

- [Technology Requirements - Data Ingestion Section](../../03-OPERATING-MODEL/03-Technology-Requirements.md)
- [[../Squarehead/SQH-EPIC-03-Platform-Groups/00-Platform-Groups|Platform Groups Architecture]]
- CRM manifest.yaml reference: `square_head/apps/platform_groups/crm/manifest.yaml`
- CRM PATTERNS.md: `square_head/apps/platform_groups/crm/PATTERNS.md`
- Existing document processing: `square_head/apps/documents/`
