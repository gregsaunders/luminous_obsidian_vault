# Luminous BioSolutions: Operating Model

**Version:** 1.1
**Created:** 2025-12-23
**Last Updated:** 2025-12-23
**Status:** 🟢 Active
**Purpose:** Define how Luminous delivers Operational Intelligence for Water Release

---

## Document Index

| # | Document | Purpose | Status |
|---|----------|---------|--------|
| 01 | [[01-Service-Delivery-Process-Map]] | End-to-end workflow from sample collection to customer delivery | 🟢 v1.1 |
| 02 | [[02-Roles-and-Responsibilities]] | Who does what (RACI matrix, role profiles) | 🟢 v1.0 |
| 03 | [[03-Technology-Requirements]] | Systems needed, build vs. buy decisions | 🟢 v1.0 |
| 04 | [[04-Pilot-Readiness-Scorecard]] | What exists vs. gaps, action plan | 🟢 v1.1 |
| 05 | [[05-Pilot-Deliverables-Framework]] | Operational intelligence deliverables (5 validated scenarios + discovery) | 🟢 v1.1 |

---

## The Value Proposition

> **We don't just give you data. We give you decisions you couldn't make before.**

| What They Have Today | What Luminous Delivers |
|---------------------|----------------------|
| 4 data points/year (HRMS) | **100+ data points/month** |
| Feedback in 4 weeks | **Feedback in 24-72 hours** |
| Calendar-based decisions | **Evidence-based decisions** |
| "Trust us" to regulators | **"Here's the proof"** (immutable audit trail) |

---

## The Scientific Advantage

**Our biosensor measures what matters:**
- HRMS measures **total NAs** (poor proxy for toxicity)
- Luminous measures **bioavailable/hydrophobic fraction** (correlates with actual toxicity)
- This is validated by HRMS specialists and aligns with NA Workshop (July 2025) recommendations

---

## Validated Scenarios (Examples, Not Limits)

The following are **proven value** from Kearl, not the complete set of possibilities. A pilot with higher-frequency sampling may reveal insights we can't anticipate today.

| Scenario | Decision Enabled | Annual Value |
|----------|------------------|--------------|
| **Seasonal Strategy** | Operate 3 weeks longer (temperature-based shutdown) | $104k |
| **Spatial Optimization** | Route flow to high-performers (+26% capacity) | $78k |
| **Toxicity Validation** | Reduce expensive bio-assays by 75% | $36k |
| **Refill Management** | Resume outflow 7 days earlier per event | $14k |
| **Regulatory Reporting** | Prove data integrity with Glass Box audit trail | $24k |
| **TOTAL (validated)** | | **$260k/year** |
| **+ Unknown insights** | Patterns only visible with high-frequency data | **TBD** |

> **"The pilot isn't just validation. It's exploration. We're turning on headlights in the dark."**

See [[05-Pilot-Deliverables-Framework]] for full details.

---

## Process Summary

```
CUSTOMER                    LUMINOUS
────────────────────────────────────────────────────────────

 ┌─────────┐    Ship      ┌─────────┐    Process    ┌─────────┐
 │ Collect │────────────▶ │ Lab     │─────────────▶ │Platform │
 │ Samples │              │ Analysis│               │ Engine  │
 └─────────┘              └─────────┘               └────┬────┘
     │                         │                         │
     │                         │ Tyson Bookout           │
     │                         │ (Biosensor author)      │
     │                    ┌─────────┐                    │
     │                    │Dashboard│◀───────────────────┘
     │                    │DECISIONS│  (not just data)
     │                    └────┬────┘
     │                         │
     └─────────────────────────┘
          Operational Intelligence
```

---

## Current Readiness: ~50% 🟡

### ✅ Resolved
- Lab Technician: **Tyson Bookout** (biosensor paper lead author)
- Core Science: Peer-reviewed, 22/24 OSPW samples detected
- Platform Infrastructure: Squarehead Foundry base exists

### 🔴 Must Resolve Before Pilot
1. **Build Customer Dashboard MVP** → Owner: Greg
2. **Formalize Lab SOPs** → Owner: Shawn/Tyson
3. **Sample Metadata Capture Solution** → Owner: Jeff

See [[04-Pilot-Readiness-Scorecard]] for full assessment.

---

## Key Contacts

| Role                   | Person            | Responsibility                                     |
| ---------------------- | ----------------- | -------------------------------------------------- |
| COO / Customer Success | Jeff Violo        | Commercial, customer relationship                  |
| Lab Manager            | Shawn Lewenza     | Lab operations, biosensor science                  |
| Platform Lead          | Greg              | Data platform, dashboard, integrations             |
| Lab Technician         | **Tyson Bookout** | Day-to-day lab processing (biosensor paper author) |

---

## Related Documents

### Master Context
- [[Luminous-Master-Context]] - Company positioning and messaging
- [[Squarehead-Foundry-Master-Context]] - Commercial strategy

### Research & Validation
- [[sprint-01-upstream-optimization]] - $260k ROI analysis
- [[sprint-02-remediation-landscape]] - Complexity gap analysis
- [[sprint-04-confluent-value-map]] - Platform capabilities
- [[Complete Kearl Wetland Report]] - Field validation data

### Technical
- Biosensor publication: `04-KNOWLEDGE/1-Technical-Docs/publications/Bookout et al/`

---

## Next Steps

1. ~~Create hiring plan for lab technician~~ ✅ Tyson confirmed
2. Review these documents with Shawn and Greg
3. Make technology decisions (dashboard: Metabase vs. custom)
4. Make technology decisions (field app: Fulcrum vs. paper forms)
5. Greg to estimate platform development effort
6. Develop timeline for pilot readiness

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-12-23 | Jeff Violo / Claude | Initial creation |
| 1.1 | 2025-12-23 | Jeff Violo / Claude | Added Pilot Deliverables Framework, updated for Tyson, added Kearl insights |
| 1.2 | 2025-12-23 | Jeff Violo / Claude | Added scientific advantage (bioavailable fraction); reframed 5 scenarios as examples not limits |

