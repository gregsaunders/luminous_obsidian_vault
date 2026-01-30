# Session Summary: Operating Model Build

**Date:** 2025-12-23
**Duration:** Extended session (context continuation)
**Participants:** Jeff Violo (CEO), Claude (Enterprise Architect)
**Purpose:** Build operational readiness documentation for commercial pilot

---

## Executive Summary

This session transformed a request for a "Business Capabilities Map" into a comprehensive **Operating Model** for Luminous BioSolutions. Through iterative discovery and challenge, we identified that the real need was proving **pilot readiness** to prospects, not creating a traditional enterprise architecture artifact.

### Key Outcome
Six operating model documents created, demonstrating end-to-end service delivery capability for the NA Biological Monitoring Service.

---

## Session Journey

### Phase 1: Challenge the Premise

**Initial Request:** Create a Business Capability Map (BCM)

**Challenge Raised:** BCM is typically used for large organizations with multiple business units. For a pre-revenue startup with a single product, this approach may be premature.

**Clarifying Questions Asked:**
- What decision will this BCM inform?
- Who is the audience?
- What's the timeline?

**User Clarification:**
- **Real Need:** Proof of operational readiness for commercial pilot
- **Audience:** Co-founders (Greg, Shawn), new employees, prospects
- **Timeline:** 1-2 days
- **Goal:** "Show we have our shit together"

**Pivot Decision:** Not a BCM exercise. This is an **Operating Model** with **Service Delivery Process Maps**.

---

### Phase 2: Discovery & Information Gathering

**Key Questions Asked:**

| Topic | Question | Answer |
|-------|----------|--------|
| Sample Collection | Who collects samples? | Customer (with Luminous support) |
| Sample Tracking | How are samples tracked? | Barcoded containers |
| Lab Location | Where is the lab? | U of C (academic, needs migration) |
| Lab Tech | Who runs the lab? | *Gap identified* → Later resolved: Tyson Bookout |
| Platform | What's the status? | Base built, front-end needed |
| Handheld App | Does it exist? | No, needs to be built |
| Turnaround | What's the target? | 24-72 hours from lab receipt |
| Test Method | What technology? | Proprietary biosensor (bacterial luminescence) |

**Technical Deep Dive:**
Read Bookout et al. 2024 publication (ACS Synthetic Biology) to understand:
- Whole-cell bacterial biosensors using *Pseudomonas sp.* OST1909
- Bioluminescence detection (luxCDABE reporter system)
- Multiple biosensor panel: atuA (acyclic NAs), marR (complex NAs), p3680 (classic NAs)
- Detection limits: 1.5-15 mg/L
- 15-hour protocol with readings every 20 minutes

---

### Phase 3: Document Creation

**Documents Produced:**

| # | Document | Purpose |
|---|----------|---------|
| 00 | Operating Model Index | Navigation hub, value proposition summary |
| 01 | Service Delivery Process Map | 40+ process steps across 5 phases |
| 02 | Roles & Responsibilities | RACI matrix, role profiles |
| 03 | Technology Requirements | Build vs. buy decisions, data model |
| 04 | Pilot Readiness Scorecard | Gap assessment, action plan |
| 05 | Pilot Deliverables Framework | Customer value definition |

---

### Phase 4: Critical Gap Resolution

**Blocker Identified:** No lab technician

**Resolution:** Tyson Bookout confirmed as lab tech
- Lead author on the biosensor publication
- Literally built the biosensors
- Major de-risk for pilot execution

**Impact:** Lab Operations category score improved from ~45% to ~60%

---

### Phase 5: Strategic Reframe

**User Feedback (Critical):**
> "I do not want to be limited to the 5 scenarios... there may be way more insights and revelations... one of the deliverables from the pilot is all of the operational insights that allow data driven decisions."

**Problem Identified:** I was anchoring too hard on the 5 validated scenarios from Kearl. This was limiting the value proposition.

**Reframe Applied:**
- 5 scenarios are **examples**, not "the product"
- Real deliverable is **all operational insights** from unprecedented data density
- Pilot is **exploration**, not just validation
- "We're turning on headlights in the dark"

---

### Phase 6: Scientific Positioning

**New Insight from User:**
> "Toxicity degrades rapidly in wetlands. The most hydrophobic NAs are most toxic and degrade first. Our biosensors measure the bioavailable/hydrophobic fraction - what's actually toxic - not total NAs like HRMS."

**Significance:** This is a critical differentiator:
- HRMS measures everything (total NAs) - poor proxy for toxicity
- Biosensor measures what matters (bioavailable fraction) - correlates with actual toxicity
- Validated by HRMS specialist at NA Workshop

**New Positioning Added:**
> "We don't just measure NAs. We measure the NAs that matter."

---

### Phase 7: Industry Validation

**NA Workshop Notes (July 2025)** incorporated:
- Hosted by NAIT, attended by ECCC, Gov't of Alberta, InnoTech, university researchers
- Industry needs: High-throughput screening, tiered monitoring, standardization
- Workshop consensus: "Use simple, fast methods for routine detection and advanced techniques for anomalies"
- This aligns exactly with Luminous positioning

---

## Key Insights & Learnings

### Strategic Insights

| # | Insight | Implication |
|---|---------|-------------|
| 1 | **BCM is wrong tool for startups** | Use Operating Model + Process Maps instead |
| 2 | **Don't limit to validated scenarios** | Sell discovery opportunity, not fixed reports |
| 3 | **Lead with science, not just speed** | Biosensor measures bioavailable fraction = toxicity indicator |
| 4 | **Industry is ready for tiered approach** | NA Workshop validates our positioning |
| 5 | **Tyson is a major de-risk** | Lab tech is biosensor paper author |

### Messaging Insights

| Old Framing | New Framing |
|-------------|-------------|
| "5 operational scenarios worth $260k" | "5 validated examples + unknown discoveries" |
| "Fast feedback (24-72 hours)" | "Fast feedback on the fraction that matters" |
| "We give you more data" | "We give you operational intelligence for decisions" |
| "Monitoring service" | "Operational Intelligence Discovery" |

### Technical Insights

| Topic | Learning |
|-------|----------|
| **Biosensor specificity** | Measures bioavailable/hydrophobic compounds, not total NAs |
| **Toxicity correlation** | marR-L biosensor correlates R²=0.89 with toxic O₂-NAFC fraction |
| **HRMS limitation** | Can't distinguish between toxic and degraded fractions |
| **Industry pain** | Mass Spec has poor inter-lab consistency; need standardization |

---

## Readiness Assessment (Final)

### Overall: ~50% 🟡

| Category | Score | Status |
|----------|-------|--------|
| Science & Technology | 90% | ✅ Ready |
| Lab Operations | 60% | 🟡 Partial (improved with Tyson) |
| Platform & Data | 50% | 🟡 Partial |
| Customer Interface | 15% | 🔴 Gap (dashboard needed) |
| Field Operations | 45% | 🔴 Gap (handheld app) |
| Commercial & Support | 10% | 🔴 Gap (pricing, contracts) |
| Team & Organization | 75% | 🟢 Ready |

### Critical Path (Blockers)

1. ~~Hire Lab Technician~~ ✅ **RESOLVED** (Tyson Bookout)
2. **Build Customer Dashboard MVP** → Owner: Greg
3. **Formalize Lab SOPs** → Owner: Shawn/Tyson
4. **Sample Metadata Capture Solution** → Owner: Jeff

---

## Decisions Made

| # | Decision | Rationale |
|---|----------|-----------|
| 1 | Operating Model over BCM | More appropriate for startup pilot readiness |
| 2 | Metabase for dashboard | Faster to deploy than custom build |
| 3 | Fulcrum for field capture | Off-the-shelf solution for metadata |
| 4 | Paper forms as interim | Start simple, build permanent app later |
| 5 | 5 scenarios as examples | Don't limit pilot value proposition |

---

## Open Questions for Team

### For Greg (Platform)
- [ ] Effort estimate for dashboard MVP?
- [ ] Data model confirmation - sample → result → context linkage?
- [ ] Weather API integration approach?

### For Shawn (Lab)
- [ ] Lab SOP timeline - can Tyson lead this?
- [ ] Biosensor strain inventory status?
- [ ] University lab access constraints?

### For Jeff (Commercial)
- [ ] Pricing model - per water body? Per site? Flat fee?
- [ ] Pilot contract template - who drafts?
- [ ] First prospect target?

---

## Documents Created This Session

| File | Path |
|------|------|
| Operating Model Index | `03-OPERATING-MODEL/00-Operating-Model-Index.md` |
| Service Delivery Process Map | `03-OPERATING-MODEL/01-Service-Delivery-Process-Map.md` |
| Roles & Responsibilities | `03-OPERATING-MODEL/02-Roles-and-Responsibilities.md` |
| Technology Requirements | `03-OPERATING-MODEL/03-Technology-Requirements.md` |
| Pilot Readiness Scorecard | `03-OPERATING-MODEL/04-Pilot-Readiness-Scorecard.md` |
| Pilot Deliverables Framework | `03-OPERATING-MODEL/05-Pilot-Deliverables-Framework.md` |
| Session Summary (this file) | `03-OPERATING-MODEL/06-Session-Summary-Operating-Model-Build.md` |

---

## Next Steps

### Immediate (This Week)
1. Review Operating Model with Shawn and Greg
2. Decision: Dashboard technology (Metabase vs. custom)
3. Decision: Field data capture (Fulcrum vs. paper)
4. Greg to estimate platform development effort

### Before Pilot
1. Dashboard MVP live
2. Lab SOPs documented
3. Customer sampling guide created
4. Data ingestion workflow operational
5. Pilot contract template drafted

---

## Quotable Positioning Statements

**For Prospects:**
> "Your wetlands are a black box. You get 4 data points a year, and each one takes a month to come back. By the time you know something's wrong, the season's over.
>
> We turn on the lights. Our biosensor measures the biologically relevant fraction—the compounds that actually correlate with toxicity—and delivers results in 24-72 hours.
>
> The 5 scenarios we've validated from Kearl are examples. The real value is what we'll discover together. We're not selling you 5 reports. We're selling you the operational intelligence to make decisions you couldn't make before."

**For Internal Team:**
> "The pilot isn't just validation. It's exploration. We're turning on headlights in the dark."

**Scientific Differentiator:**
> "We don't just measure NAs. We measure the NAs that matter."

---

## Session Value

This session produced:
- **6 operational documents** ready for team review
- **Clear gap assessment** with owners assigned
- **Refined value proposition** (discovery, not just 5 scenarios)
- **Scientific positioning** (bioavailable fraction = toxicity)
- **Industry validation** (NA Workshop alignment)
- **Critical blocker resolved** (Tyson Bookout confirmed)

**Confidence Level:** High that these documents demonstrate pilot readiness to prospects.

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-12-23 | Jeff Violo / Claude | Initial session summary |

