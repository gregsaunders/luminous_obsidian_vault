# Luminous BioSolutions: Technology Requirements

**Version:** 1.0 (Draft)
**Created:** 2025-12-23
**Status:** 🟡 In Development
**Related:** [[01-Service-Delivery-Process-Map]], [[02-Roles-and-Responsibilities]]

---

## Purpose

This document maps the technology systems required to execute the Luminous NA Monitoring Service, identifies what exists vs. what needs to be built, and prioritizes development for pilot readiness.

---

## Technology Landscape Overview

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                           LUMINOUS TECHNOLOGY STACK                                  │
├─────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                     │
│  ┌─────────────┐   ┌─────────────┐   ┌─────────────┐   ┌─────────────────────────┐ │
│  │  FIELD      │   │    LAB      │   │  PLATFORM   │   │     CUSTOMER            │ │
│  │  SYSTEMS    │   │  SYSTEMS    │   │  (Core)     │   │     INTERFACE           │ │
│  ├─────────────┤   ├─────────────┤   ├─────────────┤   ├─────────────────────────┤ │
│  │ Handheld    │──▶│ Lab Receiv- │──▶│ Relational  │──▶│ Customer Dashboard      │ │
│  │ App         │   │ ing/LIMS    │   │ Context     │   │                         │ │
│  │             │   │             │   │ Engine      │   │ Notifications           │ │
│  │ Sample Kits │   │ Plate Reader│   │             │   │                         │ │
│  │ (Barcodes)  │   │ Software    │   │ Correlation │   │ Reports                 │ │
│  │             │   │             │   │ Engine      │   │                         │ │
│  └─────────────┘   │ Analysis    │   │             │   │ Data Export             │ │
│                    │ Scripts     │   │ Data Store  │   │                         │ │
│                    └─────────────┘   └─────────────┘   └─────────────────────────┘ │
│                                                                                     │
│  ┌─────────────────────────────────────────────────────────────────────────────┐   │
│  │                      SUPPORTING SYSTEMS                                      │   │
│  ├─────────────────────────────────────────────────────────────────────────────┤   │
│  │ Courier Tracking │ External Data APIs │ Billing/Invoicing │ Communication   │   │
│  └─────────────────────────────────────────────────────────────────────────────┘   │
│                                                                                     │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

---

## Technology Inventory by Process Phase

### Phase 1: Sample Collection (Field Systems)

| Component | Purpose | Status | Priority | Notes |
|-----------|---------|--------|----------|-------|
| **Handheld Sample App** | Capture sample metadata (barcode, time, location, depth) | 🔴 Needs to be built | HIGH | Critical for data integrity |
| **Barcode System** | Unique ID for each sample container | 🟡 Partial | HIGH | Barcodes exist; scanning workflow TBD |
| **Sample Kits** | Physical containers, labels, packaging | 🟢 Exists | — | Operational |
| **GPS Integration** | Auto-capture location | 🔴 Needs to be built | MEDIUM | Can be manual entry initially |

#### Handheld App Requirements (MVP)

**Core Functions:**
1. Scan barcode on sample container
2. Auto-capture timestamp
3. Capture GPS coordinates (auto or manual entry)
4. Input fields: Water body ID, depth, sample type
5. Offline capability (sync when connected)
6. Confirmation screen before submission

**Technical Options:**
| Option | Pros | Cons | Effort |
|--------|------|------|--------|
| Native iOS/Android app | Best UX, offline support | Higher dev cost, two platforms | 4-8 weeks |
| Progressive Web App (PWA) | Single codebase, works on any device | Limited offline, less native feel | 2-4 weeks |
| Off-the-shelf (e.g., Fulcrum, Survey123) | Fast deployment, no dev needed | Subscription cost, less customization | 1 week setup |
| Paper forms + manual entry | Zero dev, immediate | Error-prone, slow, doesn't scale | 0 weeks |

**Recommendation:** Start with **off-the-shelf app** (Fulcrum or similar) for pilot, build custom later.

---

### Phase 2: Transport & Receipt (Lab Receiving)

| Component | Purpose | Status | Priority | Notes |
|-----------|---------|--------|----------|-------|
| **Courier Tracking Portal** | Track shipments in transit | 🟢 Exists | — | Use Purolator/FedEx portals |
| **Lab Receiving System** | Log incoming samples, scan barcodes, confirm receipt | 🔴 Needs to be built | HIGH | Could be simple spreadsheet initially |
| **Barcode Scanner** | Hardware to scan sample barcodes | 🟡 Partial | MEDIUM | Lab may have; verify compatibility |
| **Issue Tracking** | Log damaged/missing/late samples | 🟡 Partial | LOW | Can use email/spreadsheet initially |

#### Lab Receiving System Requirements (MVP)

**Core Functions:**
1. Scan barcode → auto-lookup expected sample
2. Confirm receipt (timestamp, condition)
3. Flag discrepancies (missing, damaged)
4. Generate receipt confirmation

**Technical Options:**
| Option | Pros | Cons | Effort |
|--------|------|------|--------|
| Spreadsheet (Google Sheets/Excel) | Immediate, free, simple | Manual barcode entry, error-prone | 0 weeks |
| Simple web form + database | Better data integrity, scannable | Some dev needed | 1-2 weeks |
| LIMS software (LabArchives, Quartzy) | Full featured, audit trail | Cost, overkill for pilot | 2-4 weeks setup |

**Recommendation:** Start with **structured spreadsheet** with barcode column for pilot. Build simple receiving module in platform later.

---

### Phase 3: Lab Analysis (Lab Systems)

| Component | Purpose | Status | Priority | Notes |
|-----------|---------|--------|----------|-------|
| **Plate Reader** | Measure bioluminescence (CPS) | 🟢 Exists | — | PerkinElmer Victor at U of C |
| **Plate Reader Software** | Run protocol, export data | 🟢 Exists | — | Comes with reader |
| **Analysis Scripts** | Calculate fold gene expression, QC | 🟡 Partial | MEDIUM | Excel-based; could automate |
| **Lab SOPs** | Documented procedures | 🟡 Partial | HIGH | Need to formalize for operational use |
| **QC Checklists** | Acceptance criteria, control validation | 🟡 Partial | HIGH | Need to document |
| **Biosensor Stock Management** | Track frozen biosensor inventory | 🔴 Needs to be built | LOW | Spreadsheet sufficient |

#### Analysis Scripts Requirements

**Current State:** Manual calculation in Excel
**Future State:** Automated script that:
1. Imports raw CPS data from plate reader
2. Normalizes by OD600
3. Calculates fold gene expression vs. controls
4. Flags QC failures
5. Outputs results ready for platform upload

**Technical Options:**
| Option | Pros | Cons | Effort |
|--------|------|------|--------|
| Excel template | Familiar, immediate | Manual, error-prone | 1-2 days |
| Python script | Automated, reproducible | Requires Python knowledge | 1-2 weeks |
| R script | Good for stats, Shawn may prefer | Requires R knowledge | 1-2 weeks |

**Recommendation:** Create **Excel template** for pilot. Automate with Python after pilot proves the process.

---

### Phase 4: Platform Processing (Core Platform)

| Component | Purpose | Status | Priority | Notes |
|-----------|---------|--------|----------|-------|
| **Relational Context Engine** | Core data store and correlation | 🟢 Exists (base) | — | Squarehead Foundry infrastructure |
| **Data Ingestion Module** | Import biosensor results, sample metadata | 🟡 Partial | HIGH | API or manual upload |
| **Contextual Data Integration** | Weather, SCADA, dosing logs | 🔴 Needs to be built | MEDIUM | Can be manual CSV import initially |
| **Correlation Engine** | Link NA results to contextual factors | 🟡 Partial | HIGH | Core value prop |
| **Alerting/Thresholds** | Flag anomalies, threshold breaches | 🔴 Needs to be built | LOW | Not critical for pilot |
| **Audit Trail / Immutability** | Prove data integrity (TerminusDB) | 🟡 Partial | MEDIUM | "Glass Box" value prop |

#### Data Model (Conceptual)

```
┌──────────────┐       ┌──────────────┐       ┌──────────────┐
│   SAMPLE     │       │   RESULT     │       │  CONTEXT     │
├──────────────┤       ├──────────────┤       ├──────────────┤
│ sample_id    │──────▶│ result_id    │◀──────│ context_id   │
│ barcode      │       │ sample_id    │       │ sample_id    │
│ collected_at │       │ biosensor    │       │ type         │
│ location     │       │ fold_change  │       │ (weather,    │
│ depth        │       │ concentration│       │  flow, dose) │
│ water_body   │       │ qc_status    │       │ value        │
│ ...          │       │ ...          │       │ timestamp    │
└──────────────┘       └──────────────┘       └──────────────┘
```

#### Integration Requirements

| Data Source | Method | Frequency | Owner |
|-------------|--------|-----------|-------|
| Biosensor results | CSV upload or API | Per batch | Lab Tech |
| Sample metadata | API from handheld app | Real-time | Platform |
| Weather data | API (Environment Canada) | Daily | Platform (auto) |
| Water flow/level | Customer CSV or API | Daily/hourly | Customer + Platform |
| Dosing logs | Manual entry or CSV | As events occur | Customer |

---

### Phase 5: Customer Delivery (Customer Interface)

| Component | Purpose | Status | Priority | Notes |
|-----------|---------|--------|----------|-------|
| **Customer Dashboard** | Visualize NA results, trends, correlations | 🔴 Needs to be built | **CRITICAL** | Core deliverable |
| **User Authentication** | Customer-specific login | 🟡 Partial | HIGH | Platform has auth; need customer provisioning |
| **Notifications** | Alert customer to new results | 🔴 Needs to be built | MEDIUM | Email-based initially |
| **Reporting Module** | Generate PDF summary reports | 🔴 Needs to be built | MEDIUM | Can be manual initially |
| **Data Export** | CSV download for customer | 🔴 Needs to be built | MEDIUM | Table export from dashboard |

#### Dashboard Requirements (MVP)

**Views Required:**
1. **Summary View**: Latest results, status indicators (normal/elevated)
2. **Trend View**: NA levels over time (line chart)
3. **Spatial View**: Results by sampling location (map or table)
4. **Correlation View**: NA vs. contextual factors (e.g., NA vs. rainfall)
5. **Data Table**: Raw results with filter/sort/export

**Visual Inspiration:**
- Simple, clean, engineer-friendly (not flashy)
- Color-coded status (green/yellow/red)
- Downloadable charts and data
- Mobile-responsive (for field access)

**Technical Options:**
| Option | Pros | Cons | Effort |
|--------|------|------|--------|
| Custom build (React/Vue) | Full control, best UX | Highest dev effort | 4-8 weeks |
| Metabase/Superset | Fast, connects to DB directly | Less custom, hosted cost | 1-2 weeks |
| Retool/Appsmith | Low-code, fast iteration | Subscription, less polished | 1-2 weeks |
| Manual PDF reports | No dev needed | Doesn't scale, not self-serve | 0 weeks |

**Recommendation:** Use **Metabase or Retool** for pilot to validate what customers want. Build custom dashboard after pilot feedback.

---

## Technology Readiness Summary

| Category | Component | Status | Pilot-Ready? | Action Required |
|----------|-----------|--------|--------------|-----------------|
| **Field** | Handheld App | 🔴 | No | Use off-the-shelf (Fulcrum) or paper forms |
| **Field** | Barcodes | 🟢 | Yes | Operational |
| **Lab** | Plate Reader | 🟢 | Yes | Exists at U of C |
| **Lab** | Analysis Scripts | 🟡 | Partial | Create Excel template |
| **Lab** | Receiving System | 🔴 | No | Use spreadsheet |
| **Lab** | SOPs | 🟡 | Partial | Formalize documentation |
| **Platform** | Data Store | 🟢 | Yes | Squarehead infrastructure exists |
| **Platform** | Ingestion | 🟡 | Partial | Manual CSV upload |
| **Platform** | Correlation | 🟡 | Partial | Core exists; needs configuration |
| **Customer** | Dashboard | 🔴 | **No** | **CRITICAL** - Use Metabase or manual reports |
| **Customer** | Notifications | 🔴 | No | Manual email initially |
| **Customer** | Reports | 🔴 | No | Manual PDF generation |

---

## Development Priorities (Pilot Readiness)

### Must Have (P0) - Pilot Cannot Start Without

| Item | Description | Effort | Owner |
|------|-------------|--------|-------|
| Customer Dashboard (MVP) | Basic visualization of results | 2-4 weeks | Greg |
| Data Ingestion Workflow | Results → Platform pipeline | 1-2 weeks | Greg |
| Lab SOPs | Documented procedures | 1-2 weeks | Shawn |
| Sample Metadata Capture | Off-the-shelf app or paper forms | 1 week | Jeff |

### Should Have (P1) - Significantly Improves Experience

| Item | Description | Effort | Owner |
|------|-------------|--------|-------|
| Analysis Script Automation | Excel template for calculations | 1 week | Shawn/Greg |
| Weather Data Integration | Auto-fetch Environment Canada data | 1-2 weeks | Greg |
| Email Notifications | Alert customer to new results | 1 week | Greg |
| Lab Receiving Module | Simple barcode scan + log | 1-2 weeks | Greg |

### Nice to Have (P2) - Can Add During Pilot

| Item | Description | Effort | Owner |
|------|-------------|--------|-------|
| Custom Handheld App | Replace off-the-shelf solution | 4-8 weeks | Greg/Contractor |
| Automated Reporting | PDF generation from dashboard | 2 weeks | Greg |
| Alerting/Thresholds | Flag anomalies automatically | 2 weeks | Greg |
| Customer SCADA Integration | API or automated data pull | Variable | Greg + Customer IT |

---

## Interim Workarounds for Pilot

| Gap | Workaround | Limitations | Upgrade Path |
|-----|------------|-------------|--------------|
| No handheld app | Paper forms + manual data entry | Slower, error-prone | Off-the-shelf app (Fulcrum) |
| No dashboard | Manual PDF reports (weekly) | Not self-serve, labor-intensive | Metabase MVP dashboard |
| No notifications | Manual email from Jeff | Doesn't scale | Automated email trigger |
| No SCADA integration | Customer provides CSV weekly | Manual, delayed | API integration |
| No lab receiving system | Spreadsheet log | Manual barcode entry | Simple web form |

---

## Cost Estimates (Rough)

| Item | Type | Estimated Cost |
|------|------|----------------|
| Fulcrum (field data capture) | SaaS subscription | ~$50-100/month |
| Metabase Cloud | SaaS subscription | ~$85/month |
| Retool | SaaS subscription | ~$10-50/user/month |
| Barcode Scanner (if needed) | Hardware | ~$200-500 |
| Custom dashboard development | Contractor | $5,000-15,000 |
| Custom handheld app | Contractor | $10,000-30,000 |

---

## Next Steps

1. **Decision: Dashboard approach** - Metabase, Retool, or custom?
2. **Decision: Field data capture** - Fulcrum, paper forms, or other?
3. **Greg to estimate**: Platform development effort for P0 items
4. **Shawn to provide**: Lab SOPs, analysis workflow documentation
5. **Define data model**: Finalize sample/result/context schema

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-12-23 | Jeff Violo / Claude | Initial draft |

