# Luminous BioSolutions: Operating Model

**Version:** 1.0
**Created:** 2025-12-23
**Status:** 🟡 In Development
**Purpose:** Define how Luminous delivers the NA Biological Monitoring Service

---

## Document Index

| # | Document | Purpose | Status |
|---|----------|---------|--------|
| 01 | [[01-Service-Delivery-Process-Map]] | End-to-end workflow from sample collection to customer delivery | 🟡 Draft |
| 02 | [[02-Roles-and-Responsibilities]] | Who does what (RACI matrix, role profiles) | 🟡 Draft |
| 03 | [[03-Technology-Requirements]] | Systems needed, build vs. buy decisions | 🟡 Draft |
| 04 | [[04-Pilot-Readiness-Scorecard]] | What exists vs. gaps, action plan | 🟡 Draft |

---

## Quick Reference: Service Overview

| Attribute | Value |
|-----------|-------|
| **Service** | NA Biological Monitoring & Intelligence |
| **Turnaround** | 24-72 hours from lab receipt |
| **Sampling** | Daily preferred (customer-dependent) |
| **Deployment** | Zero-friction offsite lab (Calgary) |
| **Output** | Dashboard + Reports |

---

## Process Summary

```
CUSTOMER                    LUMINOUS
────────────────────────────────────────────────────────────

 ┌─────────┐    Ship      ┌─────────┐    Process    ┌─────────┐
 │ Collect │────────────▶ │ Lab     │─────────────▶ │Platform │
 │ Samples │              │ Analysis│               │ Engine  │
 └─────────┘              └─────────┘               └────┬────┘
     │                                                   │
     │                    ┌─────────┐                    │
     │                    │Dashboard│◀───────────────────┘
     │                    │& Reports│
     │                    └────┬────┘
     │                         │
     └─────────────────────────┘
           View Results
```

---

## Critical Readiness Items

### 🔴 Must Resolve Before Pilot

1. **Hire Lab Technician** → Owner: Jeff/Shawn
2. **Build Customer Dashboard MVP** → Owner: Greg
3. **Formalize Lab SOPs** → Owner: Shawn
4. **Sample Metadata Capture Solution** → Owner: Jeff

### Current Readiness: ~45%

See [[04-Pilot-Readiness-Scorecard]] for full assessment.

---

## Key Contacts

| Role | Person | Responsibility |
|------|--------|----------------|
| CEO / Customer Success | Jeff Violo | Commercial, customer relationship |
| Lab Manager | Shawn Lewenza | Lab operations, biosensor science |
| Platform Lead | Greg | Data platform, dashboard, integrations |
| Lab Technician | TBD | Day-to-day lab processing |

---

## Related Documents

- [[Luminous-Master-Context]] - Company positioning and messaging
- [[Squarehead-Foundry-Master-Context]] - Commercial strategy
- Biosensor publication: `04-KNOWLEDGE/1-Technical-Docs/publications/Bookout et al/`

---

## Next Steps

1. Review these documents with Shawn and Greg
2. Validate process assumptions
3. Make technology decisions (dashboard, field app)
4. Create hiring plan for lab technician
5. Develop timeline for pilot readiness

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-12-23 | Jeff Violo / Claude | Initial creation |

