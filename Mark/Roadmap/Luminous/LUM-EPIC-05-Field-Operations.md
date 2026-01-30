---
linear_id: SQU-8
linear_url: https://linear.app/squarehead/issue/SQU-8/epic-04-field-operations
---

# EPIC-05: Field Operations

**Linear:** [SQU-8](https://linear.app/squarehead/issue/SQU-8)
**Status:** 🔴 Not Started
**Priority:** High
**Owner:** Jeff (Greg for Fulcrum API integration)
**Target:** Q2 2026 (Before Pilot)

**Dependencies:**
- ⭐ **Foundational:** No external blockers - this EPIC feeds into LUM-EPIC-01 Feature 1.3
- 🔗 **Related:** LUM-EPIC-01 Feature 1.3 (Sample Metadata Linkage consumes field data)

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

## Features

### Feature 5.1: Sample Metadata Capture App
**Linear:** [SQU-28](https://linear.app/squarehead/issue/SQU-28)
**Status:** 🔴 Not Started
**Priority:** High
**Dependencies:** None (foundational, enables LUM-EPIC-01 Feature 1.3)
**Used By:**
- [LUM-EPIC-01 Feature 1.3](LUM-EPIC-01-Data-Ingestion.md) - Sample Metadata Linkage

#### Outcome
A field technician can capture sample metadata on a mobile device at collection time, even without internet connectivity.

#### What Success Looks Like
- Technician arrives at sampling site
- Opens app, scans barcode on sample container
- App auto-captures GPS and timestamp
- Technician fills in location name, conditions
- Data syncs to platform when connectivity restored
- Metadata appears linked to sample in dashboard

#### Context
MVP uses Fulcrum (off-the-shelf). Future may use custom Flutter app.

#### Constraints
- Must work offline (field sites often have no connectivity)
- Must support barcode scanning
- Must auto-capture GPS coordinates

#### Scope: Owned Files
- `apps/platform_groups/luminous/api/field_sync.py` (API for receiving field data)

#### Requirements (Fulcrum approach - MVP)
- Fulcrum account is configured and accessible
- Form includes all required fields (see below)
- Barcode scanning captures sample IDs correctly
- GPS coordinates are auto-captured at collection time
- Offline mode is tested and works in areas without connectivity
- Data exports to platform API when connection is available

**Required Fields:**
- Barcode ID (scanned)
- Collection date/time
- Location name
- GPS coordinates (auto-captured)
- Collector name
- Weather conditions (dropdown)
- Sample type
- Notes (optional)

---

### Feature 5.2: Sampling SOP for Customers
**Linear:** [SQU-29](https://linear.app/squarehead/issue/SQU-29)
**Status:** 🟡 Partial
**Priority:** High
**Dependencies:** None

#### Outcome
A customer's field staff can follow clear instructions to collect and ship samples correctly, reducing errors and delays.

#### What Success Looks Like
- Customer receives sample kit with printed instructions
- Instructions cover: how to collect, how to label, how to ship
- Common mistakes are addressed proactively
- Chain of custody is maintained
- Samples arrive at lab in good condition

#### Scope: Owned Files
- `docs/customer/sampling-sop.md`
- `Luminous/Mark/SOP/` (source documents)

#### Requirements
- Sampling procedure is documented step-by-step
- Container handling instructions are included (storage, temperature, contamination prevention)
- Barcode labeling process is clearly explained with examples
- Chain of custody documentation tracks sample from collection to lab
- Shipping instructions specify courier, packaging, and timing requirements
- Troubleshooting section addresses common issues (damaged containers, lost labels, missed shipments)

---

### Feature 5.3: Sample Kit Management
**Linear:** [SQU-30](https://linear.app/squarehead/issue/SQU-30)
**Status:** 🔴 Not Started
**Priority:** Medium
**Dependencies:** [LUM-EPIC-04 Feature 4.1](LUM-EPIC-04-Platform-Infrastructure.md) (customer provisioning)

#### Outcome
Luminous operations can track sample kit inventory and ensure customers never run out of supplies.

#### What Success Looks Like
- Operations sees inventory levels per customer
- Gets alert when a customer is running low
- Can trigger replenishment shipment
- Customers always have kits available when needed

#### Scope: Owned Files
- `apps/platform_groups/luminous/inventory/` (kit tracking)

#### Requirements
- Kit inventory levels are tracked per customer
- Alerts notify operations when inventory falls below threshold
- Replenishment workflow triggers shipment of new kits
- Kit assignments link barcodes to specific customers

---

### Feature 5.4: Courier Logistics
**Linear:** [SQU-31](https://linear.app/squarehead/issue/SQU-31)
**Status:** 🟡 Partial
**Priority:** Medium
**Dependencies:** None

#### Outcome
Sample shipping is streamlined with clear processes and tracking visibility.

#### What Success Looks Like
- Customer knows which courier to use
- Can generate shipping labels easily
- Tracking number is captured in system
- Lab knows when to expect samples
- Delays are surfaced proactively

#### Scope: Owned Files
- `docs/customer/shipping-guide.md`
- `apps/platform_groups/luminous/logistics/` (tracking integration)

#### Requirements
- Courier accounts and processes are documented for customers
- Shipping labels can be generated easily
- Tracking numbers are captured in the system
- Notifications inform lab of expected delivery times

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

## Post-Pilot: Custom Field App

**Status:** 🔴 Future (not for Q2 2026 pilot)
**Dependencies:** SquareHead EPIC-11 (Frontend Apps), Pilot feedback

### Feature 5.5: Custom Flutter Field App
**Linear:** [SQU-32](https://linear.app/squarehead/issue/SQU-32)

#### Outcome
Field technicians use a native Flutter app integrated with the platform instead of Fulcrum.

#### Context
MVP uses Fulcrum for fast deployment. Post-pilot, a custom Flutter app may provide better integration, offline sync, and user experience.

#### Why Post-Pilot
- Fulcrum is sufficient for pilot
- Custom app requires Flutter mobile infrastructure (SquareHead EPIC-11)
- Need pilot feedback to inform requirements

#### Scope: Owned Files (Future)
- `frontend/flutter/apps/mobile/lib/features/field_capture/`

#### Requirements (Future)
- Flutter mobile app is scaffolded and buildable
- Barcode scanner reads sample container barcodes
- Form captures all required metadata fields
- App works offline and syncs when connectivity is restored
- API integration sends data to platform backend

---

## References

- [Technology Requirements - Field Systems](../03-OPERATING-MODEL/03-Technology-Requirements.md)
- [Pilot Readiness Scorecard - Field Operations](../03-OPERATING-MODEL/04-Pilot-Readiness-Scorecard.md)
- Fulcrum: https://www.fulcrumapp.com/
