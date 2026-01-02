# Luminous BioSolutions: Service Delivery Process Map

**Version:** 1.2
**Created:** 2025-12-23
**Last Updated:** 2025-12-30
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
| **Service Name** | NA Biological Monitoring & Operational Intelligence Service |
| **Target Turnaround** | 24-72 hours from lab receipt to results in platform |
| **Sampling Frequency** | Daily preferred (customer-dependent) |
| **Deployment Model** | Zero-friction offsite lab (Calgary) |
| **Output** | Operational decisions, not just data (see [[05-Pilot-Deliverables-Framework]]) |

---

## The Value Shift: From "Monitoring" to "Operational Intelligence"

**What we deliver is NOT:**
- Just data points
- Just a dashboard
- Just reports

**What we deliver IS:**
- **Decisions they couldn't make before** (seasonal shutdown timing, spatial routing, refill recovery)
- **Evidence for regulators** (immutable audit trail)
- **Speed of learning** (compress 5 years into 18 months)

### Validated Baseline: Five Operational Scenarios from Kearl

The Kearl wetland study proved these five value scenarios. They represent a **validated floor**, not a ceiling.

| Scenario | The Decision Enabled | Annual Value |
|----------|---------------------|--------------|
| Seasonal Strategy | Operate 3 weeks longer (temperature-based, not calendar) | $104k |
| Spatial Optimization | Route flow to high-performing cells (+26% capacity) | $78k |
| Toxicity Validation | Reduce expensive bio-assays by 75% | $36k |
| Refill Management | Resume outflow 7 days earlier per event | $14k |
| Regulatory Reporting | Prove data integrity with immutable audit trail | $24k |
| **VALIDATED BASELINE** | | **$256k/year** |

### Beyond the Baseline: Pilot & Commercial Upside

The Kearl study used **monthly sampling**. A pilot with **daily or weekly sampling** will reveal patterns invisible at lower frequencies. We expect significantly more value from:

| Upside Category | Potential Insights | Why It Matters |
|-----------------|-------------------|----------------|
| **Real-time anomaly detection** | Catch NA spikes within hours, not weeks | Faster response = reduced risk |
| **Weather correlation refinement** | Precise temperature thresholds for your specific site | Site-optimized operating windows |
| **Predictive models** | Forecast NA levels based on conditions | Proactive vs. reactive management |
| **Multi-year trend analysis** | Degradation rates, long-term remediation progress | Strategic planning, regulatory confidence |
| **Cross-site benchmarking** | Compare performance across water bodies | Best practice identification |
| **Unknown patterns** | Correlations we can't anticipate today | "Turning on headlights in the dark" |

> **The $256k baseline is what we've proven. The pilot is how we discover what else is possible.**

### Commercial Value Trajectory

```
                                    ┌─────────────────────────────┐
                                    │  COMMERCIAL (Year 2+)       │
                                    │  • Multi-year insights      │
                                    │  • Predictive models        │
                            ┌───────│  • Cross-site benchmarks    │
                            │       │  • Continuous optimization  │
                    ┌───────┘       └─────────────────────────────┘
                    │       ┌─────────────────────────────┐
            ┌───────┘       │  PILOT (6-12 months)        │
            │               │  • Validate 5 scenarios     │
    ┌───────┘               │  • Discover new patterns    │
    │                       │  • Refine correlations      │
    │                       │  • Build predictive models  │
────┴───────────────────────┴─────────────────────────────┴──────────▶
  $256k                   $256k+                        $400k+?
  (Validated)             (Expected)                    (Projected)
```

See [[05-Pilot-Deliverables-Framework]] for full details.

---

## End-to-End Process Phases

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   PHASE 0   │───▶│   PHASE 1   │───▶│   PHASE 2   │───▶│   PHASE 3   │───▶│   PHASE 4   │───▶│   PHASE 5   │
│   SERVICE   │    │   SAMPLE    │    │  TRANSPORT  │    │     LAB     │    │  PLATFORM   │    │  CUSTOMER   │
│ PREPARATION │    │ COLLECTION  │    │  & RECEIPT  │    │  ANALYSIS   │    │ PROCESSING  │    │  DELIVERY   │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
   Luminous           Customer           Shared            Luminous          Luminous          Luminous
  (Internal)
```

---

## Phase 0: Service Preparation (Internal)

**Owner:** Luminous Operations
**Location:** Calgary Lab / Operations
**Trigger:** Customer contract signed, before first sample collection

This phase covers all internal preparation required before samples can be collected, processed, and analyzed. These are Luminous-controlled processes that ensure quality and traceability from the start.

### Process Steps

| Step | Activity | Responsible | Input | Output | System/Tool |
|------|----------|-------------|-------|--------|-------------|
| 0.1 | Design barcode schema for customer | Operations | Customer requirements, water body count | Barcode specification document | Internal |
| 0.2 | Generate unique barcodes for sample containers | Operations | Barcode spec, quantity needed | Printed barcode labels | Barcode generator + printer |
| 0.3 | Procure/prepare sample containers | Lab Tech | Container specs, quantity | Sterile containers ready | Supplier / sterilization |
| 0.4 | Apply barcode labels to containers | Lab Tech | Labels, containers | Labeled containers | Manual application |
| 0.5 | Pre-register barcodes in platform | Operations | Barcode batch list | Barcodes active in system | Platform admin |
| 0.6 | Assemble sample collection kits | Operations | Containers, cooler, ice packs, instructions, return labels | Complete sample kits | Kit assembly SOP |
| 0.7 | QC check assembled kits | Lab Tech / Operations | Assembled kits | QC-approved kits | Kit checklist |
| 0.8 | Ship kits to customer site | Operations | Approved kits, shipping address | Kits in transit | Courier (Purolator/FedEx) |
| 0.9 | Confirm kit receipt with customer | Customer Success | Tracking confirmation | Customer acknowledges receipt | Email / phone |

### Barcode Schema Design

The barcode encodes critical metadata for traceability:

| Field | Format | Example | Purpose |
|-------|--------|---------|---------|
| Customer ID | 3-letter code | `KEA` | Identifies customer (e.g., Kearl) |
| Water Body ID | 2-digit code | `04` | Identifies sampling location (e.g., Cell 4) |
| Kit Batch | 4-digit | `0001` | Links to kit preparation batch |
| Container # | 3-digit | `001` | Unique container within batch |
| Check digit | 1-digit | `7` | Error detection |

**Full barcode example:** `KEA-04-0001-001-7`

**Barcode format options:**
- **Code 128**: High density, alphanumeric, widely supported
- **QR Code**: Can encode more data, works with smartphone cameras
- **Recommendation**: Use Code 128 for scanner compatibility + QR for handheld app backup

### Sample Kit Contents

| Item | Quantity | Specification | Notes |
|------|----------|---------------|-------|
| Sample containers | 10-20 per kit | 125mL HDPE, sterile, wide-mouth | Pre-labeled with barcodes |
| Insulated cooler | 1 | Minimum 24-hour cold retention | Reusable, branded |
| Ice packs | 2-4 | Gel-based, reusable | Pre-frozen by customer |
| Sampling instructions | 1 | Laminated card | Waterproof, field-ready |
| Chain of custody form | 1 | Paper + digital option | For regulatory compliance |
| Return shipping label | 1 | Pre-paid, pre-addressed | Purolator/FedEx |
| Sampling gloves | 5 pairs | Nitrile, disposable | Prevent contamination |

### Quality Gates

- [ ] Barcode schema approved by Operations
- [ ] All barcodes scan correctly (100% test)
- [ ] Barcodes pre-registered in platform
- [ ] Kit contents match checklist
- [ ] Customer receipt confirmed

### Key Decisions

- **Barcode format**: Code 128 vs. QR Code (recommend Code 128 primary + QR backup)
- **Container size**: 125mL standard (confirm with Shawn - minimum 100mL needed)
- **Kit quantity per shipment**: Based on sampling frequency × duration between shipments
- **Reusable vs. disposable coolers**: Reusable reduces cost, requires return logistics

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

### Technology Roadmap: Current vs. Future State

The lab process can be progressively automated to improve throughput, reduce errors, and lower per-sample costs.

#### Equipment Inventory

| Category | Current State (MVP) | Future State (Scale) | Investment Range |
|----------|---------------------|---------------------|------------------|
| **Plate Reader** | PerkinElmer Victor (manual load) | Same + automated plate stacker | $15-25k for stacker |
| **Liquid Handling** | Manual multichannel pipette | Hamilton STAR or Tecan liquid handler | $50-150k |
| **Incubator** | Standard CO2 incubator | Same (adequate for current needs) | — |
| **Barcode Integration** | Handheld scanner (manual) | Integrated scanner on liquid handler | Included with handler |
| **Data Export** | Manual CSV export | Direct API to platform | Development effort |
| **Environmental Monitoring** | Visual checks | IoT temp/humidity loggers | $500-2k |
| **Imaging/Documentation** | Manual photos | Plate reader imaging module or separate camera | $5-15k |

#### Automation Priorities (Recommended Sequence)

| Priority | Automation | Benefit | Investment | Payback |
|----------|-----------|---------|------------|---------|
| 1 | **API data export** | Eliminates manual upload, reduces errors | Dev time only | Immediate |
| 2 | **Barcode-to-well mapping** | Auto-links results to samples | $2-5k + dev | 3-6 months |
| 3 | **Environmental monitoring** | QC documentation, audit trail | $500-2k | Immediate |
| 4 | **Liquid handler** | 10x throughput, reduced variability | $50-150k | 12-24 months |
| 5 | **Plate stacker** | Unattended overnight runs | $15-25k | 18-36 months |

#### Recommended Equipment for High-Quality Results

| Equipment | Specification | Purpose | Vendor Options |
|-----------|--------------|---------|----------------|
| **Multichannel pipette** | 8 or 12 channel, 10-100μL | Sample dispensing (MVP) | Eppendorf, Gilson, Rainin |
| **Electronic pipette** | Programmable, reduces fatigue | Consistent volumes | Eppendorf Xplorer, Sartorius |
| **Plate sealer** | Adhesive film applicator | Prevents evaporation during 15hr assay | Bio-Rad, Eppendorf |
| **Vortex mixer** | Plate adapter | Consistent sample mixing | VWR, Fisher |
| **Barcode scanner** | 2D capable (QR + Code 128) | Sample tracking | Zebra, Honeywell |
| **Lab notebook (electronic)** | Cloud-based, audit trail | 21 CFR Part 11 compliance ready | Benchling, LabArchives |

#### Future Consideration: Microfluidics

For very high throughput (100+ samples/day), consider microfluidic biosensor platforms that could reduce sample volume and assay time. This is a 3-5 year horizon technology decision.

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

### Automation Architecture: Barcode-to-Platform Flow

The goal is to minimize human intervention while maintaining full traceability. Here's how data flows from the lab to the platform automatically:

#### Data Flow Diagram

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  PLATE READER   │────▶│  WATCHED FOLDER │────▶│   TRANSFORM     │────▶│    PLATFORM     │
│  Exports CSV    │     │  or API Trigger │     │   SERVICE       │     │    API          │
└─────────────────┘     └─────────────────┘     └─────────────────┘     └─────────────────┘
        │                                               │                        │
        │                                               │                        │
        ▼                                               ▼                        ▼
  Raw CPS data                                  Barcode → Well                Sample record
  Well positions                                mapping applied               enriched with
  Timestamps                                    QC validation                 NA results
                                                Fold calculation
```

#### Barcode Auto-Injection Process

| Step | Trigger | Action | Output |
|------|---------|--------|--------|
| 1 | Lab tech loads plate | Scan barcodes in well order (A1→H12) | Plate layout file (barcode-to-well map) |
| 2 | Assay completes | Plate reader exports CSV to watched folder | Raw data file with timestamp |
| 3 | File detected | Transform service picks up file | Processing initiated |
| 4 | Transform | Merge raw data with plate layout (barcode mapping) | Enriched results file |
| 5 | Validation | Apply QC rules (control wells, thresholds) | QC status flags |
| 6 | Calculation | Compute fold gene expression from CPS | Final results |
| 7 | Upload | POST to Platform API with barcode as key | Results in platform |
| 8 | Linking | Platform matches barcode to pre-registered sample | Sample record complete |

#### Integration Options

| Method | Complexity | Reliability | Cost | Best For |
|--------|-----------|-------------|------|----------|
| **Watched folder + script** | Low | Medium | Low | MVP/pilot |
| **Plate reader API** | Medium | High | Medium | Production |
| **LIMS integration** | High | High | High | Enterprise scale |

**Recommended MVP approach:**
1. Plate reader exports to network folder
2. Python script monitors folder, processes new files
3. Script calls Platform API to upload results
4. Logging/alerting for failures

#### Correlation Data Sources

The platform should automatically ingest and correlate these data sources:

| Data Source | Integration Method | Refresh Frequency | Correlation Value |
|-------------|-------------------|-------------------|-------------------|
| **Weather (Environment Canada)** | Public API | Daily | Temperature-toxicity correlation |
| **Water level/flow (SCADA)** | Customer API or CSV | Hourly/Daily | Flow impact on NA |
| **Dosing events** | Manual entry or CSV | As occurs | Treatment effectiveness |
| **Rewatering events** | Manual entry or CSV | As occurs | Recovery tracking |
| **Historical NA results** | Platform (internal) | Continuous | Trend detection |
| **Spatial coordinates** | Pre-configured | Static | Cell/pond performance comparison |

#### Dashboard Visualization Priorities

| View | Purpose | Key Metrics |
|------|---------|-------------|
| **Time Series** | Track NA trends over time | Fold expression, moving average, thresholds |
| **Spatial Map** | Compare performance across locations | Color-coded NA levels by cell/pond |
| **Correlation Matrix** | Identify relationships | NA vs. temperature, flow, dosing |
| **Anomaly Alerts** | Highlight exceptions | Threshold breaches, unexpected patterns |
| **Audit Trail** | Regulatory compliance | Chain of custody, data provenance |

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
| **AER compliance report** | As required | Regulator-ready PDF |
| **Indigenous community report** | Monthly/Quarterly | Visual summary PDF |

### Regulatory & Stakeholder Reporting

A key value proposition is eliminating manual reporting burden while providing regulator-ready documentation.

#### AER (Alberta Energy Regulator) Reporting

| Report Element | Data Source | Automation Level |
|----------------|-------------|------------------|
| NA concentration trends | Platform (biosensor results) | Fully automated |
| Sampling frequency compliance | Platform (sample metadata) | Fully automated |
| Chain of custody documentation | Platform (audit trail) | Fully automated |
| QC/QA records | Lab data (controls, calibration) | Semi-automated |
| Exceedance notifications | Platform (threshold alerts) | Fully automated |
| Annual summary statistics | Platform (aggregated data) | Fully automated |

**Report format:** Auto-generated PDF with:
- Executive summary
- Data tables in AER-required format
- Trend charts
- QC documentation
- Digital signature/timestamp for authenticity

#### Indigenous Community Reporting

Operators have commitments to local Indigenous communities. Luminous can help fulfill these with accessible, visual reports.

| Report Element | Design Principle | Format |
|----------------|-----------------|--------|
| Water quality summary | Plain language, no jargon | Visual infographic |
| Trend visualization | Color-coded (green/yellow/red) | Charts with clear legends |
| Comparison to baseline | Historical context | Before/after comparisons |
| Seasonal patterns | Align with traditional knowledge | Calendar-based views |
| Site map | Spatial context | Map with sampling locations |

**Value to customer:**
- Demonstrates environmental stewardship
- Builds trust with Indigenous partners
- Reduces internal reporting effort
- Consistent, professional presentation

#### Audit Trail & Data Integrity

All reports include immutable proof of data integrity:

| Element | Implementation |
|---------|----------------|
| Data provenance | Full chain from sample collection to report |
| Timestamps | Cryptographically signed, tamper-evident |
| Version control | All data changes logged with user/reason |
| Export certification | Hash of exported data for verification |

> **"We don't just give you reports. We give you evidence that stands up to regulatory scrutiny."**

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
───────────────────────────────────────────────────────────────────────────────────────────────────────────
              │ PHASE 0       │ PHASE 1      │ PHASE 2       │ PHASE 3      │ PHASE 4      │ PHASE 5
              │ Preparation   │ Collection   │ Transport     │ Lab          │ Platform     │ Delivery
───────────────────────────────────────────────────────────────────────────────────────────────────────────
 CUSTOMER     │               │              │               │              │              │
 (Site Op)    │               │ ●─Collect    │ ●─Ship        │              │              │ ●─Review
              │               │ ●─Scan       │               │              │              │   Dashboard
              │               │ ●─Store      │               │              │              │
───────────────────────────────────────────────────────────────────────────────────────────────────────────
 LUMINOUS     │ ●─Barcode     │              │               │              │              │
 Operations   │   schema      │              │               │              │              │
              │ ●─Assemble    │              │               │              │              │
              │   kits        │              │               │              │              │
───────────────────────────────────────────────────────────────────────────────────────────────────────────
 LUMINOUS     │ ●─Prep        │              │               │              │              │
 Lab Ops      │   containers  │              │ ●─Receive     │ ●─Prepare    │              │
              │ ●─Label       │              │ ●─Log         │ ●─Run Assay  │              │
              │               │              │ ●─QC Receipt  │ ●─QC Results │              │
              │               │              │               │ ●─Upload     │              │
───────────────────────────────────────────────────────────────────────────────────────────────────────────
 LUMINOUS     │ ●─Pre-register│              │               │              │ ●─Ingest     │ ●─AER
 Platform     │   barcodes    │              │               │              │ ●─Correlate  │   Reports
              │               │              │               │              │ ●─Visualize  │ ●─Community
              │               │              │               │              │              │   Reports
───────────────────────────────────────────────────────────────────────────────────────────────────────────
 LUMINOUS     │               │ ●─Ship kits  │ ●─Track       │              │              │ ●─Notify
 Cust Success │               │ ●─Onboard    │   shipment    │              │              │ ●─Support
              │               │              │               │              │              │ ●─Report
───────────────────────────────────────────────────────────────────────────────────────────────────────────
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
| 1.1 | 2025-12-30 | Jeff Violo / Claude | Added Phase 0 (Service Preparation) with barcode schema and kit assembly; Added Technology Roadmap to Phase 3 (equipment, automation priorities); Added Automation Architecture to Phase 4 (barcode-to-platform flow, correlation sources); Added Regulatory & Stakeholder Reporting to Phase 5 (AER, Indigenous community); Updated swim lane diagram |
| 1.2 | 2025-12-30 | Jeff Violo / Claude | Reframed 5 Kearl scenarios as "Validated Baseline" ($256k floor); Added "Beyond the Baseline" section with pilot/commercial upside potential; Added commercial value trajectory visualization |

