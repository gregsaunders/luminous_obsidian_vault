# Luminous BioSolutions: Service Delivery Process Map

**Version:** 1.0 (Draft)
**Created:** 2025-12-23
**Status:** 🟡 In Development
**Owner:** Jeff Violo

---

## Purpose

This document defines the end-to-end service delivery process for Luminous BioSolutions' Naphthenic Acid (NA) Monitoring Service. It serves as:
1. **Internal playbook** for executing a commercial pilot
2. **Proof of operational readiness** for prospects
3. **Foundation** for technology requirements and staffing decisions

---

## Service Overview

| Attribute | Value |
|-----------|-------|
| **Service Name** | NA Biological Monitoring & Intelligence Service |
| **Target Turnaround** | 24-72 hours from lab receipt to results in platform |
| **Sampling Frequency** | Daily preferred (customer-dependent) |
| **Deployment Model** | Zero-friction offsite lab (Calgary) |
| **Output** | Dashboard with NA detection, concentration estimates, and trend correlation |

---

## End-to-End Process Phases

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   PHASE 1   │───▶│   PHASE 2   │───▶│   PHASE 3   │───▶│   PHASE 4   │───▶│   PHASE 5   │
│   SAMPLE    │    │  TRANSPORT  │    │     LAB     │    │  PLATFORM   │    │  CUSTOMER   │
│ COLLECTION  │    │  & RECEIPT  │    │  ANALYSIS   │    │ PROCESSING  │    │  DELIVERY   │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
   Customer           Shared            Luminous          Luminous          Luminous
```

---

## Phase 1: Sample Collection (Customer Site)

**Owner:** Customer (with Luminous support)
**Location:** Oil sands site (e.g., wetland, tailings pond)

### Process Steps

| Step | Activity | Responsible | Input | Output | System/Tool |
|------|----------|-------------|-------|--------|-------------|
| 1.1 | Receive sample kit from Luminous | Site Operator | Shipment notification | Sample kit in hand | Courier tracking |
| 1.2 | Collect water sample at designated location | Site Operator | Sampling SOP, GPS coordinates | Filled sample container | Sample Kit |
| 1.3 | Scan barcode on sample container | Site Operator | Sample container | Sample metadata captured | **Handheld App** (TBD) |
| 1.4 | Confirm metadata (time, location, depth, water body ID) | Site Operator | Auto-populated fields | Validated sample record | **Handheld App** (TBD) |
| 1.5 | Store sample in cooler for transport | Site Operator | Filled container | Sample ready for shipment | Cooler/ice packs |
| 1.6 | Arrange courier pickup | Site Operator / Luminous | Pickup schedule | Courier dispatched | Courier portal |

### Quality Gates
- [ ] Barcode scanned successfully
- [ ] All required metadata fields populated
- [ ] Sample stored at appropriate temperature
- [ ] Courier pickup confirmed

### Key Decisions
- **Sampling frequency**: Daily, every 2 days, or weekly (customer preference vs. cost)
- **Number of sampling points per water body**: TBD based on wetland size/complexity
- **Sample volume required**: ~100mL minimum (confirm with Shawn)

---

## Phase 2: Transport & Lab Receipt

**Owner:** Shared (Customer initiates, Luminous receives)
**Location:** Site → Calgary Lab

### Process Steps

| Step | Activity | Responsible | Input | Output | System/Tool |
|------|----------|-------------|-------|--------|-------------|
| 2.1 | Package samples for shipment | Site Operator | Samples in cooler | Sealed shipment | Packaging SOP |
| 2.2 | Hand off to courier | Site Operator | Packaged samples | Tracking number | Courier (Purolator/FedEx) |
| 2.3 | Track shipment in transit | Lab Coordinator | Tracking number | ETA notification | Courier tracking portal |
| 2.4 | Receive samples at Calgary lab | Lab Tech | Physical shipment | Samples logged as received | **Lab Receiving System** (TBD) |
| 2.5 | Scan barcodes to confirm receipt | Lab Tech | Sample containers | Receipt confirmed in system | Barcode scanner + LIMS |
| 2.6 | Inspect samples for integrity | Lab Tech | Physical samples | QC pass/fail | Visual inspection SOP |
| 2.7 | Log any issues (damaged, missing, late) | Lab Tech | Inspection results | Issue ticket created | Issue tracking system |

### Quality Gates
- [ ] All expected samples received (count matches manifest)
- [ ] Barcodes scan successfully and match expected shipment
- [ ] No visible contamination or damage
- [ ] Received within acceptable time window (TBD - 48 hours from collection?)

### Logistics Considerations
- **Fort McMurray → Calgary**: ~450km, courier typically overnight
- **Recommended courier**: Purolator (reliable, temperature-controlled options)
- **Contingency**: What if shipment delayed? (Customer notification protocol)

---

## Phase 3: Lab Analysis (Biosensor Testing)

**Owner:** Luminous Lab Operations
**Location:** Calgary Lab (currently: University facility → migrate to operational lab)

### Process Steps

| Step | Activity | Responsible | Input | Output | System/Tool |
|------|----------|-------------|-------|--------|-------------|
| 3.1 | Retrieve samples from receiving area | Lab Tech | Logged samples | Samples at workstation | — |
| 3.2 | Prepare biosensor culture | Lab Tech | Frozen biosensor stock | Active biosensor culture | Incubator, growth media |
| 3.3 | Prepare 96-well assay plate | Lab Tech | Sample + biosensor + media | Loaded plate | Pipettes, plate |
| 3.4 | Add sample to wells (90μL sample + 10μL media) | Lab Tech | Prepared plate | Inoculated plate | Multichannel pipette |
| 3.5 | Load plate into plate reader | Lab Tech | Inoculated plate | Plate in reader | PerkinElmer Victor plate reader |
| 3.6 | Run bioluminescence assay (15-hour protocol) | Automated | Plate in reader | Raw luminescence data (CPS) | Plate reader + protocol |
| 3.7 | Export raw data | Lab Tech | Completed run | CSV/data file | Plate reader software |
| 3.8 | Perform QC check on results | Lab Tech / Lab Manager | Raw data | QC-validated results | QC checklist / SOP |
| 3.9 | Calculate fold gene expression & concentration estimates | Lab Tech | QC'd data | Processed results | Excel / Analysis script |
| 3.10 | Scan barcode to link results to sample ID | Lab Tech | Processed results | Results linked to sample | Barcode scanner |
| 3.11 | Upload results to platform | Lab Tech | Linked results | Data in Relational Context Engine | **Platform API / Import** (TBD) |

### Quality Gates
- [ ] Biosensor culture viability confirmed (positive control)
- [ ] Negative control shows no NA response
- [ ] Results within expected range for sample type
- [ ] No contamination detected
- [ ] Barcode linkage verified

### Lab Process Notes (from Bookout et al. publication)
- **Assay duration**: 15-hour protocol with readings every 20 minutes (45 time points)
- **Output**: CPS (counts per second) normalized by OD600, then fold gene expression calculated
- **Biosensor panel**: atuA-L (acyclic NA), marR-L (complex/OSPW NA), p3680-lux (classic NA)
- **Detection limits**: 1.5 - 15 mg/L depending on NA type
- **Interpretation**: Fold change >2 = biologically significant NA detection

### Critical Dependencies
- [ ] **Biosensor strain availability**: Frozen stocks of engineered Pseudomonas sp. OST1909
- [ ] **Plate reader access**: PerkinElmer Victor or equivalent
- [ ] **Lab SOPs**: Documented procedures for each step
- [ ] **QC protocols**: Positive/negative controls, acceptance criteria

---

## Phase 4: Platform Processing & Correlation

**Owner:** Luminous Platform / Data Team
**Location:** Cloud (Squarehead Foundry Relational Context Engine)

### Process Steps

| Step | Activity | Responsible | Input | Output | System/Tool |
|------|----------|-------------|-------|--------|-------------|
| 4.1 | Ingest biosensor results | Platform | Uploaded results file | Data in platform | API / Import module |
| 4.2 | Link results to sample metadata | Platform | Sample ID, barcode | Enriched sample record | Relational Context Engine |
| 4.3 | Ingest contextual data (weather, flow, dosing) | Platform / Customer | External data feeds | Contextual data in platform | API / CSV import |
| 4.4 | Correlate NA results with contextual factors | Platform | All linked data | Correlation insights | Automated correlation engine |
| 4.5 | Generate trend analysis | Platform | Historical + current data | Trend visualizations | Analytics module |
| 4.6 | Flag anomalies or threshold breaches | Platform | Results vs. thresholds | Alerts generated | Alerting rules |
| 4.7 | Prepare customer-facing dashboard | Platform | All processed data | Dashboard ready | Dashboard UI |

### Data Inputs Required

| Data Type | Source | Frequency | Integration Method |
|-----------|--------|-----------|-------------------|
| Biosensor results | Luminous Lab | Per sample batch | API / CSV upload |
| Sample metadata | Handheld app | Per sample | API (real-time sync) |
| Weather data | Public API (Environment Canada) | Daily | API integration |
| Water flow / level | Customer SCADA | Daily / hourly | Customer export / API |
| Chemical dosing logs | Customer operations | As events occur | Manual entry / CSV |
| Rewatering events | Customer operations | As events occur | Manual entry / CSV |

### Platform Requirements (TBD)
- [ ] **Data model**: Sample → Results → Contextual Data relationships
- [ ] **Dashboard views**: Trend over time, spatial view, anomaly highlights
- [ ] **Export capability**: CSV download for customer internal use
- [ ] **User access**: Customer-specific login with view-only access
- [ ] **Audit trail**: Immutable record of all data (for regulatory trust)

---

## Phase 5: Customer Delivery & Ongoing Support

**Owner:** Luminous Customer Success
**Location:** Remote (with periodic on-site visits)

### Process Steps

| Step | Activity | Responsible | Input | Output | System/Tool |
|------|----------|-------------|-------|--------|-------------|
| 5.1 | Notify customer of new results | Customer Success | Dashboard updated | Email/notification sent | Notification system |
| 5.2 | Customer reviews dashboard | Customer | Dashboard access | Customer informed | Platform |
| 5.3 | Provide interpretation support (if requested) | Customer Success | Customer questions | Answers / insights | Video call / email |
| 5.4 | Generate periodic summary report | Customer Success | Accumulated data | Summary report (PDF/dashboard) | Reporting module |
| 5.5 | Conduct monthly review call | Customer Success | Monthly data | Action items, feedback | Video call |
| 5.6 | Adjust sampling strategy (if needed) | Customer Success + Customer | Pilot learnings | Updated sampling plan | Collaborative decision |

### Customer Deliverables

| Deliverable | Frequency | Format |
|-------------|-----------|--------|
| Real-time dashboard access | Continuous | Web app |
| New results notification | Per batch (daily/weekly) | Email alert |
| Weekly summary | Weekly | Dashboard view / PDF |
| Monthly review report | Monthly | PDF + call |
| Pilot completion report | End of pilot | PDF + presentation |

---

## Billing & Commercial (Phase 6 - Future)

**Status:** Not yet designed
**Model:** Subscription (volume-unlimited)

### Open Questions
- [ ] Pricing structure: Per water body? Per site? Flat fee?
- [ ] What's included: Number of samples? Support hours?
- [ ] Billing cycle: Monthly? Quarterly?
- [ ] Contract terms: Pilot duration? Renewal?

---

## Process Swim Lane Diagram (Visual)

```
─────────────────────────────────────────────────────────────────────────────────────────
                    │ PHASE 1      │ PHASE 2       │ PHASE 3      │ PHASE 4      │ PHASE 5
                    │ Collection   │ Transport     │ Lab          │ Platform     │ Delivery
─────────────────────────────────────────────────────────────────────────────────────────
 CUSTOMER           │              │               │              │              │
 (Site Operator)    │ ●─Collect    │ ●─Ship        │              │              │ ●─Review
                    │ ●─Scan       │               │              │              │   Dashboard
                    │ ●─Store      │               │              │              │
─────────────────────────────────────────────────────────────────────────────────────────
 LUMINOUS           │              │               │              │              │
 Lab Ops            │              │ ●─Receive     │ ●─Prepare    │              │
                    │              │ ●─Log         │ ●─Run Assay  │              │
                    │              │ ●─QC Receipt  │ ●─QC Results │              │
                    │              │               │ ●─Upload     │              │
─────────────────────────────────────────────────────────────────────────────────────────
 LUMINOUS           │              │               │              │              │
 Platform           │              │               │              │ ●─Ingest     │
                    │              │               │              │ ●─Correlate  │
                    │              │               │              │ ●─Visualize  │
─────────────────────────────────────────────────────────────────────────────────────────
 LUMINOUS           │ ●─Ship kits  │ ●─Track       │              │              │ ●─Notify
 Customer Success   │ ●─Onboard    │   shipment    │              │              │ ●─Support
                    │              │               │              │              │ ●─Report
─────────────────────────────────────────────────────────────────────────────────────────
```

---

## Critical Path & Bottlenecks

| Bottleneck | Risk | Mitigation |
|------------|------|------------|
| **Handheld app not built** | Sample metadata capture is manual/error-prone | Phase 1: Use paper forms + manual data entry as interim |
| **Lab at university** | May not support evening/overnight runs | Negotiate access or prioritize commercial lab migration |
| **Platform front-end not complete** | Customer has no dashboard to view | Phase 1: Manual report generation (PDF) |
| **Courier delays** | Samples arrive late, miss processing window | Build 48-72 hour buffer into turnaround commitment |
| **Single lab tech** | No redundancy, vacation = service gap | Cross-train second person or contract backup |

---

## Next Steps

1. **Validate with Shawn**: Lab process steps, timing, equipment needs
2. **Validate with Greg**: Platform capabilities, data model, API readiness
3. **Define interim workarounds**: For handheld app, dashboard
4. **Create Readiness Scorecard**: What exists vs. what needs to be built
5. **Estimate costs**: Per-sample cost for pricing model

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-12-23 | Jeff Violo / Claude | Initial draft |

