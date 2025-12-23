# Luminous BioSolutions: Roles & Responsibilities (RACI)

**Version:** 1.0 (Draft)
**Created:** 2025-12-23
**Status:** 🟡 In Development
**Related:** [[01-Service-Delivery-Process-Map]]

---

## Purpose

This document defines the roles required to execute the Luminous NA Monitoring Service and assigns accountability across the service delivery process.

---

## Core Roles

### Luminous Internal Roles

| Role | Description | Current Owner | FTE Estimate (Pilot) |
|------|-------------|---------------|---------------------|
| **Lab Manager** | Oversees all lab operations, QC, biosensor production, SOPs | Shawn Lewenza | 0.25 - 0.5 FTE |
| **Lab Technician** | Executes sample processing, runs assays, records results | TBD (hire or contract) | 0.5 - 1.0 FTE |
| **Platform Lead** | Manages data ingestion, correlation engine, dashboard development | Greg | 0.25 - 0.5 FTE |
| **Data Analyst** | Processes contextual data, generates insights, supports reporting | TBD (or Greg initially) | 0.25 FTE |
| **Customer Success Lead** | Onboards customer, manages relationship, delivers reports | Jeff Violo | 0.25 FTE |
| **Operations Coordinator** | Manages sample kit logistics, courier tracking, scheduling | TBD (or Jeff initially) | 0.25 FTE |

### Customer Roles

| Role | Description | Typical Title |
|------|-------------|---------------|
| **Site Operator** | Collects samples, scans barcodes, ships samples | Environmental Tech, Field Operator |
| **Site Coordinator** | Schedules sampling, liaises with Luminous | Environmental Coordinator |
| **Data Provider** | Provides SCADA data, dosing logs, operational context | Process Engineer, IT |
| **Executive Sponsor** | Approves pilot, receives summary reports | Environmental Manager, VP Operations |

---

## RACI Matrix by Process Phase

**Legend:**
- **R** = Responsible (Does the work)
- **A** = Accountable (Owns the outcome)
- **C** = Consulted (Provides input)
- **I** = Informed (Kept in the loop)

### Phase 1: Sample Collection

| Activity | Site Operator | Site Coordinator | Customer Success | Lab Manager | Lab Tech |
|----------|---------------|------------------|------------------|-------------|----------|
| Receive sample kit | R | I | A | C | — |
| Collect water sample | R | A | I | C | — |
| Scan barcode & capture metadata | R | A | I | — | — |
| Store sample in cooler | R | A | — | — | — |
| Arrange courier pickup | R | A | C | — | — |

### Phase 2: Transport & Receipt

| Activity | Site Operator | Ops Coordinator | Lab Tech | Lab Manager | Customer Success |
|----------|---------------|-----------------|----------|-------------|------------------|
| Package & ship samples | R/A | I | — | — | I |
| Track shipment | I | R | I | — | A |
| Receive samples at lab | — | I | R | A | — |
| Scan barcodes, log receipt | — | — | R | A | — |
| Inspect for integrity | — | — | R | A | — |
| Log issues | — | C | R | A | I |

### Phase 3: Lab Analysis

| Activity | Lab Tech | Lab Manager | Platform Lead | Customer Success |
|----------|----------|-------------|---------------|------------------|
| Prepare biosensor culture | R | A | — | — |
| Prepare assay plate | R | A | — | — |
| Run bioluminescence assay | R | A | — | — |
| Export raw data | R | A | — | — |
| Perform QC check | R | A | — | — |
| Calculate results | R | A | C | — |
| Upload results to platform | R | A | C | I |

### Phase 4: Platform Processing

| Activity | Platform Lead | Data Analyst | Lab Manager | Customer Success |
|----------|---------------|--------------|-------------|------------------|
| Ingest biosensor results | R | C | I | — |
| Link results to sample metadata | R | C | — | — |
| Ingest contextual data | R | R | — | C |
| Correlate NA results with context | R | A | C | — |
| Generate trend analysis | R | R | — | I |
| Flag anomalies | R | A | — | I |
| Prepare dashboard | R | A | — | C |

### Phase 5: Customer Delivery

| Activity | Customer Success | Platform Lead | Lab Manager | Customer (Exec Sponsor) |
|----------|------------------|---------------|-------------|------------------------|
| Notify customer of new results | R/A | C | — | I |
| Provide interpretation support | R/A | C | C | — |
| Generate summary report | R | C | C | I |
| Conduct monthly review | R/A | C | C | R (participates) |
| Adjust sampling strategy | A | C | C | R (approves) |

---

## Role Profiles (Detailed)

### Lab Technician

**Reports to:** Lab Manager (Shawn)

**Responsibilities:**
- Receive and log incoming samples
- Prepare biosensor cultures from frozen stock
- Execute 96-well plate assays per SOP
- Operate plate reader and export data
- Perform QC checks on all results
- Calculate fold gene expression values
- Upload results to platform
- Maintain lab cleanliness and contamination control
- Flag any anomalies to Lab Manager

**Skills Required:**
- Microbiology lab experience (aseptic technique)
- Familiarity with plate readers and bioluminescence assays
- Attention to detail (QC mindset)
- Basic data analysis (Excel)
- Ability to follow SOPs precisely

**Time Commitment (Pilot):**
- ~2-4 hours per sample batch for processing
- With daily sampling: ~0.5-1.0 FTE

**Hiring Considerations:**
- Contract lab tech vs. full-time hire
- Could be a graduate student if university lab is used
- Need backup coverage for continuity

---

### Operations Coordinator

**Reports to:** Jeff Violo

**Responsibilities:**
- Prepare and ship sample kits to customer sites
- Coordinate courier pickups and track shipments
- Maintain inventory of sample containers, barcodes, packaging
- Communicate shipping status to customer and lab
- Troubleshoot logistics issues (delayed shipments, lost packages)
- Schedule and confirm sampling activities with customer

**Skills Required:**
- Logistics/supply chain experience
- Strong organizational skills
- Customer communication
- Proficiency with courier portals (Purolator, FedEx)

**Time Commitment (Pilot):**
- ~5-10 hours per week
- Can be combined with other roles initially

---

### Customer Success Lead

**Reports to:** Jeff Violo (or is Jeff initially)

**Responsibilities:**
- Onboard new pilot customers (training, access setup)
- Serve as primary point of contact for customer
- Deliver results notifications and interpretation support
- Prepare and present monthly summary reports
- Gather customer feedback and improvement requests
- Coordinate sampling strategy adjustments
- Escalate technical issues to Lab Manager or Platform Lead

**Skills Required:**
- Relationship management
- Technical communication (able to explain NA results)
- Presentation skills
- Project management basics

**Time Commitment (Pilot):**
- ~5-10 hours per week per customer
- Increases during onboarding and monthly reviews

---

## Pilot Team Structure (Proposed)

```
                    ┌─────────────────┐
                    │   Jeff Violo    │
                    │   CEO / CS Lead │
                    └────────┬────────┘
                             │
        ┌────────────────────┼────────────────────┐
        │                    │                    │
        ▼                    ▼                    ▼
┌───────────────┐    ┌───────────────┐    ┌───────────────┐
│ Shawn Lewenza │    │     Greg      │    │ Ops Coord.    │
│ Lab Manager   │    │ Platform Lead │    │ (TBD/Jeff)    │
└───────┬───────┘    └───────────────┘    └───────────────┘
        │
        ▼
┌───────────────┐
│  Lab Tech     │
│  (TBD/Hire)   │
└───────────────┘
```

---

## Capacity Planning (Single Pilot)

### Assumptions
- 1-2 water bodies
- Daily sampling = ~7 samples/week per water body
- 14 samples/week maximum

### Workload Estimates

| Role | Hours/Week | Notes |
|------|------------|-------|
| Lab Tech | 15-20 | Processing, QC, data upload |
| Lab Manager | 5-10 | Oversight, troubleshooting, QC review |
| Platform Lead | 5-10 | Data ingestion, dashboard maintenance |
| Customer Success | 5-10 | Communication, reporting |
| Ops Coordinator | 5 | Logistics, kit replenishment |
| **Total** | **35-55** | |

### Scaling Considerations
- At 3+ pilots: Lab Tech becomes full-time
- At 5+ pilots: Need second Lab Tech or automation
- Platform work scales efficiently (same dashboard, more data)

---

## Gaps & Hiring Needs

| Role | Current State | Gap | Action Required |
|------|---------------|-----|-----------------|
| Lab Tech | No dedicated resource | **CRITICAL** | Hire or contract before pilot |
| Ops Coordinator | No dedicated resource | Medium | Jeff can cover initially |
| Data Analyst | Greg covers | Low | Not needed for pilot |
| Customer Success | Jeff covers | Low | Jeff handles pilot |

### Recommended First Hire
**Lab Technician** - Without this role, the service cannot operate. This is the most critical hire before pilot launch.

**Options:**
1. Contract through university (if lab stays at U of C)
2. Part-time hire (20-30 hours/week)
3. Graduate student (cost-effective, but less reliable)

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-12-23 | Jeff Violo / Claude | Initial draft |

