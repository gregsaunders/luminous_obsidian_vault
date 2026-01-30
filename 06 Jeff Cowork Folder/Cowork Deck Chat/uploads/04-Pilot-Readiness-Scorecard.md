c# Luminous BioSolutions: Pilot Readiness Scorecard

**Version:** 1.0 (Draft)
**Created:** 2025-12-23
**Status:** 🟡 In Development
**Purpose:** Demonstrate operational readiness for commercial pilot

---

## Executive Summary

This scorecard assesses Luminous BioSolutions' readiness to execute a commercial pilot of the NA Biological Monitoring Service. It identifies what exists, what has gaps, and what must be addressed before pilot launch.

### Overall Readiness: 🟡 PARTIAL (Estimated: 60-65%)

**Key Findings:**
- ✅ Core biosensor technology is proven (peer-reviewed publication)
- ✅ Platform infrastructure exists
- ✅ Lab technician confirmed (Tyson Bookout - biosensor paper author)
- 🟡 Lab operations need formalization (SOPs, QC protocols)
- 🔴 Customer-facing dashboard needs to be built
- 🔴 Field data capture app needs solution

**Update (2025-12-23):** Lab technician gap resolved. Tyson Bookout, lead author on the biosensor publication, will serve as lab tech. This is a major de-risk - he literally built the biosensors.

---

## Readiness by Category

### 1. Science & Technology Readiness

| Item | Status | Evidence | Gap | Action |
|------|--------|----------|-----|--------|
| Biosensor technology validated | ✅ Ready | Bookout et al. 2024, ACS Synthetic Biology | — | — |
| Detection of NA in OSPW proven | ✅ Ready | 22/24 water samples detected (paper) | — | — |
| Dose-response curves established | ✅ Ready | Limits of detection: 1.5-15 mg/L | — | — |
| Multiple biosensor panel (atuA, marR, 3680) | ✅ Ready | Covers acyclic, complex, classic NA | — | — |
| Biosensor strain stocks available | 🟡 Partial | Frozen stocks at U of C lab | Verify inventory | Confirm with Shawn |
| Plate reader protocol optimized | ✅ Ready | 15-hour protocol documented | — | — |

**Category Score: 90%** ✅

---

### 2. Lab Operations Readiness

| Item | Status | Evidence | Gap | Action |
|------|--------|----------|-----|--------|
| Lab space available | 🟡 Partial | University of Calgary facility | Not operational lab; access constraints? | Plan migration timeline |
| Lab equipment available | ✅ Ready | PerkinElmer Victor plate reader | — | — |
| Sample receiving process defined | 🔴 Gap | No formal process | Need SOP, tracking system | Define process, create spreadsheet |
| Lab SOPs documented | 🟡 Partial | Research protocols exist | Not formalized for operations | Shawn to formalize |
| QC protocols defined | 🟡 Partial | Controls used in research | Not documented for operations | Document acceptance criteria |
| Lab technician in place | ✅ Ready | Tyson Bookout (biosensor paper lead author) | — | Confirmed |
| Biosensor culture production process | 🟡 Partial | Research process exists | Not scaled/documented | Document SOP |
| Contamination control measures | 🟡 Partial | Standard lab practices | Need checklist | Create contamination control SOP |

**Category Score: 45%** 🔴

---

### 3. Platform & Data Readiness

| Item | Status | Evidence | Gap | Action |
|------|--------|----------|-----|--------|
| Core data infrastructure | ✅ Ready | Squarehead Foundry platform | — | — |
| Data model defined | 🟡 Partial | Conceptual model exists | Not implemented | Finalize schema with Greg |
| Biosensor results ingestion | 🟡 Partial | Manual upload possible | No automated pipeline | Create CSV import workflow |
| Sample metadata linkage | 🔴 Gap | No current workflow | Barcode → result linkage needed | Build with Greg |
| Contextual data integration | 🔴 Gap | No current workflow | Weather, SCADA, dosing | Define integration approach |
| Correlation engine | 🟡 Partial | Platform has capability | Needs configuration | Configure for NA use case |
| Audit trail / immutability | 🟡 Partial | TerminusDB capability | Not implemented | Implement for "Glass Box" |

**Category Score: 50%** 🟡

---

### 4. Customer Interface Readiness

| Item | Status | Evidence | Gap | Action |
|------|--------|----------|-----|--------|
| Customer dashboard | 🔴 Gap | **Does not exist** | **CRITICAL** | Build MVP (Metabase or custom) |
| User authentication | 🟡 Partial | Platform has auth | Customer provisioning needed | Configure customer access |
| Results visualization | 🔴 Gap | No UI exists | Trend charts, tables needed | Include in dashboard MVP |
| Notification system | 🔴 Gap | No system | Email alerts needed | Manual email initially |
| Report generation | 🔴 Gap | No system | PDF summaries needed | Manual creation initially |
| Data export | 🔴 Gap | No UI for export | CSV download needed | Include in dashboard MVP |

**Category Score: 15%** 🔴

---

### 5. Field Operations Readiness

| Item | Status | Evidence | Gap | Action |
|------|--------|----------|-----|--------|
| Sample collection kits | ✅ Ready | Containers, labels exist | — | — |
| Barcode system | 🟢 Ready | Barcoded containers available | — | — |
| Handheld data capture app | 🔴 Gap | **Does not exist** | Metadata capture needed | Use Fulcrum or paper forms |
| Sampling SOPs for customer | 🟡 Partial | General guidance exists | Not customer-facing document | Create customer sampling guide |
| Courier logistics | 🟡 Partial | Courier accounts exist | Process not documented | Document shipping protocol |
| Sample kit replenishment process | 🔴 Gap | No process defined | Kit inventory management | Define replenishment workflow |

**Category Score: 45%** 🔴

---

### 6. Commercial & Support Readiness

| Item | Status | Evidence | Gap | Action |
|------|--------|----------|-----|--------|
| Pricing model defined | 🔴 Gap | Subscription concept only | No specific pricing | Cost analysis needed |
| Pilot contract template | 🔴 Gap | No template exists | Legal/commercial terms | Draft with advisor |
| Customer onboarding process | 🔴 Gap | No process defined | Training, access setup | Define onboarding checklist |
| Customer success playbook | 🔴 Gap | No playbook | Communication cadence, escalation | Create playbook |
| Support/issue tracking | 🔴 Gap | No system | Issue logging needed | Use email/spreadsheet initially |

**Category Score: 10%** 🔴

---

### 7. Team & Organization Readiness

| Item | Status | Evidence | Gap | Action |
|------|--------|----------|-----|--------|
| Lab Manager identified | ✅ Ready | Shawn Lewenza | — | — |
| Platform Lead identified | ✅ Ready | Greg | — | — |
| Customer Success Lead identified | ✅ Ready | Jeff Violo | — | — |
| Lab Technician in place | ✅ Ready | Tyson Bookout | — | Confirmed |
| Operations Coordinator | 🟡 Partial | Jeff can cover initially | Not sustainable | Plan future hire |
| Roles & responsibilities documented | ✅ Ready | RACI matrix created | — | Validate with team |
| Capacity for pilot workload | ✅ Ready | Core team + Tyson | — | — |

**Category Score: 75%** 🟢

---

## Critical Path to Pilot Readiness

### 🔴 BLOCKERS (Must resolve before pilot)

| # | Item | Owner | Effort | Target Date |
|---|------|-------|--------|-------------|
| 1 | ~~**Hire Lab Technician**~~ | ~~Jeff/Shawn~~ | ~~2-4 weeks~~ | ✅ **RESOLVED** (Tyson Bookout) |
| 2 | **Build Customer Dashboard MVP** | Greg | 2-4 weeks | Before pilot start |
| 3 | **Formalize Lab SOPs** | Shawn/Tyson | 1-2 weeks | Before pilot start |
| 4 | **Sample Metadata Capture Solution** | Jeff | 1 week | Before pilot start |

### 🟡 HIGH PRIORITY (Significantly improve readiness)

| # | Item | Owner | Effort | Target Date |
|---|------|-------|--------|-------------|
| 5 | Define data ingestion workflow | Greg | 1-2 weeks | Before pilot start |
| 6 | Create customer sampling guide | Jeff/Shawn | 1 week | Before pilot start |
| 7 | Document QC protocols | Shawn | 1 week | Before pilot start |
| 8 | Set up lab receiving spreadsheet | Jeff | 1 day | Before pilot start |
| 9 | Create customer onboarding checklist | Jeff | 1 week | Before pilot start |

### 🟢 NICE TO HAVE (Can develop during pilot)

| # | Item | Owner | Effort | Target Date |
|---|------|-------|--------|-------------|
| 10 | Automated email notifications | Greg | 1 week | Month 1 of pilot |
| 11 | Weather data integration | Greg | 1-2 weeks | Month 1 of pilot |
| 12 | Analysis script automation | Shawn/Greg | 1 week | Month 2 of pilot |
| 13 | Customer SCADA integration | Greg | Variable | Month 2-3 of pilot |
| 14 | PDF report generation | Greg | 2 weeks | Month 2 of pilot |

---

## Readiness Visualization

```
CATEGORY                          SCORE    STATUS
─────────────────────────────────────────────────
Science & Technology              ████████░░  90%  ✅
Lab Operations                    ██████░░░░  60%  🟡  (↑ Tyson confirmed)
Platform & Data                   █████░░░░░  50%  🟡
Customer Interface                █░░░░░░░░░  15%  🔴
Field Operations                  ████░░░░░░  45%  🔴
Commercial & Support              █░░░░░░░░░  10%  🔴
Team & Organization               ███████░░░  75%  🟢  (↑ Tyson confirmed)
─────────────────────────────────────────────────
OVERALL                           █████░░░░░  50%  🟡
```

**Note:** Lab tech gap resolved significantly improves overall readiness.

---

## What This Scorecard Proves to Prospects

### ✅ "We Have Our Shit Together" Evidence

1. **Proven Science**: Peer-reviewed publication validates the technology works
2. **Clear Process**: End-to-end service delivery is mapped and understood
3. **Defined Roles**: We know who does what at every stage
4. **Honest Assessment**: We've identified gaps and have a plan to close them
5. **Technology Plan**: We know what needs to be built and have prioritized it

### 🟡 Honest Gaps We're Addressing

1. ~~**Lab Tech Hire**~~: ✅ Resolved - Tyson Bookout confirmed
2. **Customer Dashboard**: Under development
3. **Operational SOPs**: Being formalized from research protocols
4. **Field App**: Using interim solution, building permanent later

### Key Message for Prospects

> "We have validated technology backed by peer-reviewed research. Our lab tech is the lead author of that publication. We've mapped our entire service delivery process and identified exactly what we need to operationalize. We're building a customer dashboard now. By pilot launch, we'll have a complete operational infrastructure ready to deliver 24-72 hour turnaround on NA monitoring - turning your 4-data-points-a-year into 100+ data points per month."

---

## Action Plan Summary

### Immediate (This Week)
- [x] ~~Confirm lab tech hiring approach with Shawn~~ → Tyson Bookout confirmed
- [ ] Decision: Dashboard technology (Metabase vs. custom)
- [ ] Decision: Field data capture (Fulcrum vs. paper)
- [ ] Greg to estimate platform development effort

### Before Pilot (Next 4-6 Weeks)
- [x] ~~Lab technician hired/contracted~~ → Tyson Bookout
- [ ] Dashboard MVP live
- [ ] Lab SOPs documented (Tyson can lead - he knows the protocols)
- [ ] Customer sampling guide created
- [ ] Data ingestion workflow operational

### During Pilot (Ongoing)
- [ ] Iterate on dashboard based on feedback
- [ ] Automate manual processes
- [ ] Refine SOPs based on learnings
- [ ] Build permanent handheld app

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-12-23 | Jeff Violo / Claude | Initial draft |

