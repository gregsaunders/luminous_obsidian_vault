---
status: "Not Started"
priority: "High"
epic_id: "LUM-EPIC-05"
linear_id: "SQU-8"
linear_url: "https://linear.app/squarehead/issue/SQU-8/epic-04-field-operations"
---

# EPIC-05: Field Operations

**Linear:** [SQU-8](https://linear.app/squarehead/issue/SQU-8)
**Owner:** Jeff (Greg for Fulcrum API integration)
**Target:** Q2 2026 (Before Pilot)

---

## Vision

Field technicians can capture sample metadata quickly and reliably at collection time, even in remote locations with poor connectivity.

---

## User Stories

- As a **field technician**, I can record sample metadata on my tablet so I don't have to remember details later
- As a **field technician**, I can scan barcodes to link my metadata to the correct sample
- As a **lab technician**, I can see field context when processing samples so I understand the collection conditions
- As a **customer**, I receive clear instructions on how to collect and ship samples correctly

---

## Context

Field technicians need to capture sample metadata when collecting samples. This metadata links to lab results via barcode, enabling traceability and contextual analysis. Without this, we can't correlate results to locations and conditions.

Currently, metadata is captured on paper or in ad-hoc systems, leading to data entry errors and missing information.

---

## Dependencies

- **Foundational:** No external blockers - this EPIC feeds into LUM-EPIC-01 Feature 1.3
- **Related:** LUM-EPIC-01 Feature 1.3 (Sample Metadata Linkage consumes field data)

---

## Features

- [[Feature 5.1 Sample Metadata Capture App]]
- [[Feature 5.2 Sampling SOP for Customers]]
- [[Feature 5.3 Sample Kit Management]]
- [[Feature 5.4 Courier Logistics]]
- [[Feature 5.5 Custom Flutter Field App]]

---

## Field Data Flow

```
Field Technician              Platform                    Lab
────────────────              ────────                    ───
Collect sample
     ↓
Scan barcode             →   Metadata received
     ↓                            ↓
Capture metadata              Validate barcode
     ↓                            ↓
Ship to lab              →   Track shipment         →   Receive sample
                                                            ↓
                              Link metadata          ←   Process & upload
                                  ↓
                              Dashboard displays
```

---

## References

- [Technology Requirements - Field Systems](../03-OPERATING-MODEL/03-Technology-Requirements.md)
- [Pilot Readiness Scorecard - Field Operations](../03-OPERATING-MODEL/04-Pilot-Readiness-Scorecard.md)
- Fulcrum: https://www.fulcrumapp.com/
