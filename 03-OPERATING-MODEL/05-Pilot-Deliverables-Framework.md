# Luminous BioSolutions: Pilot Deliverables Framework

**Version:** 1.0
**Created:** 2025-12-23
**Status:** 🟢 Active
**Source:** Validated from Kearl Wetland Study (Vander Meulen et al. 2025)

---

## Purpose

This document defines **what the customer actually receives** from a Luminous pilot. The output isn't just "monitoring data" - it's **operational intelligence that drives decisions**.

---

## The Value Proposition (Summary)

> **"We don't just give you data. We give you the feedback loops to make decisions you couldn't make before."**

| What They Have Today | What Luminous Provides |
|---------------------|----------------------|
| 4 data points/year (HRMS) | 100+ data points/month (Biosensor) |
| Feedback in 4 weeks | Feedback in 24-72 hours |
| Manual correlation (Excel) | Automated correlation (Context Engine) |
| Calendar-based decisions | Evidence-based decisions |
| "Trust us" to regulators | "Here's the proof" (Glass Box) |

---

## The Five Operational Scenarios

These are the **specific decisions** a customer can make with Luminous that they cannot make without it. Each represents a validated use case from the Kearl Wetland Study.

---

### Scenario 1: Seasonal Operating Strategy

**Annual Value:** $104,000

#### The Blind Spot (Without Luminous)
- Operators shut down wetlands by **calendar date** (e.g., September 15)
- Why? Because HRMS lab results take 4+ weeks - they can't confirm biological activity is still occurring
- Result: Lost treatment capacity at the end of every season

#### What Luminous Delivers
- **Daily biosensor readings** show biological activity in real-time
- **Temperature correlation** proves treatment continues until ~5°C threshold
- **Evidence package** for regulators showing extended window is safe

#### The Decision Enabled
> "We can operate 3 weeks longer because we can **see** treatment is still working."

#### Pilot Deliverable
- **Seasonal Optimization Report**: Temperature vs. treatment effectiveness curve, recommended shutdown threshold, regulatory evidence package

---

### Scenario 2: Spatial Optimization

**Annual Value:** $78,000

#### The Blind Spot (Without Luminous)
- Operators treat the entire wetland as a "black box"
- All cells get equal flow regardless of performance
- No visibility into which areas are doing the heavy lifting

#### What Luminous Delivers
- **Cell-by-cell performance data** showing treatment rates by location
- **Kearl finding**: Shallow vegetated cells outperform deep pools by 18%
- **Flow routing recommendations** based on actual performance

#### The Decision Enabled
> "Route 60% more flow to shallow cells. **Increase capacity 26% without building new infrastructure.**"

#### Pilot Deliverable
- **Spatial Performance Map**: Cell-by-cell treatment rates, depth vs. performance correlation, flow optimization recommendations

---

### Scenario 3: Toxicity-Targeted Validation

**Annual Value:** $36,000

#### The Blind Spot (Without Luminous)
- "Total NAs" is a poor proxy for actual toxicity
- Operators pay $8,000 per Microtox bioassay to confirm toxicity reduction
- Assays are slow (weeks) and infrequent

#### What Luminous Delivers
- **Biosensor Panel 2 (marR-L)** correlates R² = 0.89 with toxic O₂-NAFC fraction
- **Daily leading indicator** of toxicity, not monthly lagging confirmation
- **Validated correlation** between biosensor response and HRMS chemistry

#### The Decision Enabled
> "Our biosensor shows toxicity is dropping. We can **reduce expensive bio-assays by 75%**."

#### Pilot Deliverable
- **Toxicity Correlation Report**: Biosensor vs. Microtox correlation, recommended assay reduction strategy, cost savings analysis

---

### Scenario 4: Refill Impact Management

**Annual Value:** $14,000

#### The Blind Spot (Without Luminous)
- When OSPW is added to top up the wetland, operators pause outflow for 14 days "just to be safe"
- Why? They can't see how quickly the system recovers
- Result: Lost capacity during every refill event

#### What Luminous Delivers
- **Continuous monitoring** before, during, and after refill
- **Kearl finding**: Recovery happens in 7 days, not 14
- **Threshold-based restart** instead of calendar-based

#### The Decision Enabled
> "We can resume outflow 7 days earlier. **That's 7 extra days of treatment capacity per refill event.**"

#### Pilot Deliverable
- **Refill Recovery Analysis**: Time-to-recovery curves, recommended restart thresholds, capacity recapture estimate

---

### Scenario 5: Automated Regulatory Reporting

**Annual Value:** $24,000

#### The Blind Spot (Without Luminous)
- Data is trapped in spreadsheets across multiple systems
- Regulatory reporting is a manual, time-consuming project
- Auditors question data integrity ("Was this manipulated?")

#### What Luminous Delivers
- **Immutable audit trail** (TerminusDB) - data cannot be altered
- **Automated correlation** of all data sources (biosensor, LIMS, weather, flow)
- **Regulator-ready exports** with complete chain of custody

#### The Decision Enabled
> "When regulators ask for proof, we hand them a **digital key to an immutable record**, not a PDF."

#### Pilot Deliverable
- **Regulatory Readiness Package**: Complete audit trail, data lineage documentation, view-only regulator access (optional)

---

## Pilot Deliverables Summary

### Monthly Deliverables

| Deliverable | Format | Purpose |
|-------------|--------|---------|
| NA Detection Dashboard | Web dashboard | Real-time access to results |
| Weekly Trend Report | Dashboard view | Pattern identification |
| Monthly Summary | PDF + Call | Strategic discussion with stakeholder |

### Pilot Completion Deliverables

| Deliverable | Format | Value |
|-------------|--------|-------|
| **Readiness Baseline Report** | PDF | Regulatory asset for 2027 release |
| **Operational Intelligence Package** | PDF + Data | Seasonal windows, spatial maps, recovery curves |
| **ROI Validation Report** | PDF | Business case for expansion |
| **Future Project Intelligence** | PDF | Treatment recommendations, monitoring optimization |

---

## The "Multivariate Correlation" Value

### Why Can't They Just Use Excel?

The Kearl study revealed treatment rates dropped **53% mid-season** (0.53 → 0.25 mg/L/day).

| Response | Without Luminous | With Luminous |
|----------|-----------------|---------------|
| **Detection** | 4 weeks later (next HRMS) | 24-72 hours |
| **Root Cause** | Guess: Add nutrients? ($12k) | System correlates to temperature shift (normal) |
| **Decision** | Panic intervention | "Do nothing" (saved $12k) |

### The Correlation Challenge

A single biosensor reading is **meaningless without context**. The platform answers:

1. **What changed?** (the reading)
2. **Why did it change?** (temperature? flow? season? refill?)
3. **Has this happened before?** (historical pattern match)
4. **Is this normal?** (threshold vs. anomaly)
5. **What should we do?** (recommended action)

---

## Data Inputs Required from Customer

To deliver these operational scenarios, we need:

| Data Type | Purpose | Frequency | Integration |
|-----------|---------|-----------|-------------|
| **Water samples** | Biosensor analysis | Daily (preferred) | Physical shipment |
| **Flow rates** | Correlation | Daily/hourly | SCADA export or CSV |
| **Temperature** | Seasonal correlation | Continuous | SCADA or weather station |
| **Refill events** | Recovery analysis | As events occur | Manual notification |
| **Dosing logs** | Intervention correlation | As events occur | CSV or manual entry |
| **Historical reports** | Institutional memory | One-time upload | PDF ingestion |

---

## Success Criteria for Pilot

### Quantitative

| Metric | Target | Measurement |
|--------|--------|-------------|
| Samples processed | >90% on-time | Lab tracking |
| Results turnaround | <72 hours | Timestamp comparison |
| Dashboard uptime | >99% | System monitoring |
| Customer data access | Self-serve | Dashboard login |

### Qualitative

| Outcome | Evidence |
|---------|----------|
| Customer makes decision they couldn't make before | Documented decision + rationale |
| Customer identifies optimization opportunity | Spatial, seasonal, or refill insight |
| Customer sees value for regulatory readiness | Feedback in review calls |
| Customer requests expansion | Verbal or written indication |

---

## Pricing Implications

The $260k annual value is based on a **mature, multi-water-body operation**.

For a 1-2 water body pilot, realistic scenario validation:
- Scenario 1 (Seasonal): **Likely achievable** (if pilot spans season end)
- Scenario 2 (Spatial): **Achievable if multiple cells sampled**
- Scenario 3 (Toxicity): **Achievable** (correlation validation)
- Scenario 4 (Refill): **Achievable if refill event occurs**
- Scenario 5 (Reporting): **Achievable** (automated from Day 1)

**Minimum pilot scope to validate 3/5 scenarios:**
- 1 water body with multiple sampling points
- Duration: 4-6 months (to capture seasonal variation)
- Sampling frequency: Daily to weekly

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-12-23 | Jeff Violo / Claude | Initial creation from Kearl analysis |

