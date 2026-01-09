# EPIC-04: Field Operations

**Status:** 🔴 Not Started
**Priority:** High
**Owner:** Jeff (Greg for Fulcrum API integration)
**Target:** Q2 2026 (Before Pilot)

**Dependencies:**
- ⭐ **Foundational:** No external blockers - this EPIC feeds into EPIC-02 Feature 2.3
- 🔗 **Related:** EPIC-02 Feature 2.3 (sample metadata linkage consumes field data)

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

### Feature 4.1: Sample Metadata Capture App
**Status:** 🔴 Not Started
**Priority:** High
**Dependencies:** None (foundational, enables EPIC-02 Feature 2.3)
**Used By:**
- [LUM-EPIC-02 Feature 2.3](LUM-EPIC-02-Data-Ingestion.md) - Sample Metadata Linkage

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

#### Tasks (Fulcrum approach - MVP)
- [ ] Fulcrum account setup
- [ ] Form design with required fields
- [ ] Barcode scanning integration
- [ ] GPS capture for location
- [ ] Offline capability testing
- [ ] Export workflow to platform API

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

### Feature 4.2: Sampling SOP for Customers
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

#### Tasks
- [ ] Document sampling procedure
- [ ] Container handling instructions
- [ ] Barcode labeling process
- [ ] Chain of custody documentation
- [ ] Shipping instructions
- [ ] Troubleshooting common issues

---

### Feature 4.3: Sample Kit Management
**Status:** 🔴 Not Started
**Priority:** Medium
**Dependencies:** Feature 3.1 (customer provisioning)

#### Outcome
Luminous operations can track sample kit inventory and ensure customers never run out of supplies.

#### What Success Looks Like
- Operations sees inventory levels per customer
- Gets alert when a customer is running low
- Can trigger replenishment shipment
- Customers always have kits available when needed

#### Scope: Owned Files
- `apps/platform_groups/luminous/inventory/` (kit tracking)

#### Tasks
- [ ] Kit inventory tracking
- [ ] Low inventory alerts
- [ ] Replenishment workflow
- [ ] Kit assignment to customers

---

### Feature 4.4: Courier Logistics
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

#### Tasks
- [ ] Courier account documentation
- [ ] Shipping label generation
- [ ] Tracking number capture
- [ ] Expected delivery notifications

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

### Feature 4.5: Custom Flutter Field App

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

#### Tasks (Future)
- [ ] Flutter mobile app scaffolding
- [ ] Barcode scanner integration
- [ ] Form for metadata capture
- [ ] Offline-first with sync
- [ ] API integration

---

## References

- [Technology Requirements - Field Systems](../03-OPERATING-MODEL/03-Technology-Requirements.md)
- [Pilot Readiness Scorecard - Field Operations](../03-OPERATING-MODEL/04-Pilot-Readiness-Scorecard.md)
- Fulcrum: https://www.fulcrumapp.com/
