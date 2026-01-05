# EPIC-04: Field Operations

**Status:** 🔴 Not Started
**Priority:** High
**Owner:** Jeff (Greg for Fulcrum API integration)
**Target:** Q2 2026 (Before Pilot)

**Dependencies:**
- ⭐ **Foundational:** No external blockers - this EPIC feeds into EPIC-02 Feature 2.3
- 🔗 **Related:** EPIC-02 Feature 2.3 (sample metadata linkage consumes field data)

---

## Business Value

Field technicians need to capture sample metadata when collecting samples. This metadata links to lab results via barcode, enabling traceability and contextual analysis. Without this, we can't correlate results to locations and conditions.

**Key Outcome:** Field metadata is captured consistently and flows into the platform.

---

## Features

### Feature 4.1: Sample Metadata Capture App
**Status:** 🔴 Not Started
**Priority:** High
**Dependencies:** None (foundational, enables EPIC-02 Feature 2.3)

Mobile/tablet app for field technicians to capture sample metadata.

**Options:**
1. **Fulcrum** (Recommended for MVP) - Off-the-shelf field data capture, fast deployment
2. **Paper forms** - Fallback, manual data entry later
3. **Custom Flutter app** - Future, fits existing stack

**Tasks (Fulcrum approach):**
- [ ] Fulcrum account setup
- [ ] Form design with required fields
- [ ] Barcode scanning integration
- [ ] GPS capture for location
- [ ] Offline capability testing
- [ ] Export workflow to platform API

**Tasks (Custom app approach - Future):**
- [ ] Flutter mobile app scaffolding
- [ ] Barcode scanner integration
- [ ] Form for metadata capture
- [ ] Offline-first with sync
- [ ] API integration

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

Customer-facing documentation for proper sample collection.

**Tasks:**
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

Track and replenish sample collection kits.

**Tasks:**
- [ ] Kit inventory tracking
- [ ] Low inventory alerts
- [ ] Replenishment workflow
- [ ] Kit assignment to customers

---

### Feature 4.4: Courier Logistics
**Status:** 🟡 Partial
**Priority:** Medium

Document and streamline sample shipping.

**Tasks:**
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

## References

- [Technology Requirements - Field Systems](../03-OPERATING-MODEL/03-Technology-Requirements.md)
- [Pilot Readiness Scorecard - Field Operations](../03-OPERATING-MODEL/04-Pilot-Readiness-Scorecard.md)
- Fulcrum: https://www.fulcrumapp.com/
