# Pilot Proposal: Integrated Water Readiness Infrastructure

Prepared For: CNRL / [Operator Name] Operations Team

Prepared By: Luminous BioSolutions

Date: November 29, 2025

Status: ACTIVE v1.5

## 1. Executive Summary

**The Challenge:** The 2027 AER Water Release Guidelines will hinge on one critical variable: **Naphthenic Acids (NAFCs).** These complex toxins are the primary regulatory barrier to release. Current monitoring (Quarterly HRMS) is too slow for process control, leaving operators blind to the one contaminant that matters most.

**The Proposal:** Luminous BioSolutions proposes a 9-month deployment of our **Readiness Infrastructure**. We combine the industry's only high-frequency NAFC Biosensor ("The Mine Detector") with a Relational Context Engine ("The Map") to solve the toxicity bottleneck.

The Business Case:

Based on validated data from the Imperial Kearl wetland pilot, this system generates $260,000/year in operational efficiencies, delivering a ~5-month payback period.

- **Phase 1 (The Wedge):** Deliver immediate process control on NAFC treatment performance.

- **Phase 2 (The Driver):** Build the defensible 12-month toxicity baseline required for 2027 release authorization.


## 2. The Problem: The NAFC Blind Spot

Operators are currently managing water release strategies with a critical blind spot.

1. **The Regulatory Block:** Release is impossible without proving NAFC detoxification.

2. **The Data Gap:** Standard labs take weeks to return NAFC data. You cannot optimize a treatment system when the feedback loop is 45 days long.

3. **The Toxicity Confusion:** "Total NAFC" counts are misleading. You need to know if you are removing the _toxic_ fraction, not just the background carbon.


**The Consequence:** Without high-frequency toxicity data, you are forced to run conservative retention times and expensive safety factors. You are effectively driving a Ferrari with the headlights off, through a minefield.

## 3. The Solution: Luminous Readiness Infrastructure

We provide the only infrastructure capable of tracking the toxic fraction of NAFCs at operational speed.

### Part A: The "Headlights" (3-Panel Biosensor Array)

- **What it is:** A patent-pending biosensor that mimics the biological effect of NAFCs on living tissue (TRL 8).

- **The Differentiator:** Unlike standard labs that give you one number (Total NAs), we provide a **3-Panel Resolution**:

    - **Panel 1:** Surrogates / Background

    - **Panel 2:** **The Toxic Fraction (O2-NAFCs)** – _This is the regulatory key._

    - **Panel 3:** Complex / Recalcitrant Structures

- **The Value:** We isolate the signal from the noise. You get 3-panel data every 24-72 hours, allowing you to treat the _toxicity_, not just the water volume.


### Part B: The "Relational Context Engine" (Confluent)

- **What it is:** A data integration platform that contextualizes this new NAFC data.

- **How it works:** It ingests the Biosensor results and automatically maps them against your existing SCADA (Flow, Temp, Level) and Weather data.

- **The Value:** It answers the question _"Why did NAFC removal drop in Cell 3?"_ in minutes. It correlates toxicity spikes to operational events (e.g., "Refill #2 caused a Panel 2 spike due to poor mixing").


## 4. Validated ROI: The "Safe Bet"

We are not asking for an R&D budget. We are proposing an efficiency upgrade that pays for itself. The following values are based on actual operational scenarios validated during the Kearl Wetland Pilot.

|   |   |   |   |
|---|---|---|---|
|**Operational Scenario**|**The Inefficiency**|**The Luminous Fix**|**Annual Value**|
|**1. Seasonal Strategy**|Shutting down early (Sept 15) based on calendar dates.|**Temperature Correlation:** Proved NAFC treatment continues to 5°C, extending season by 3 weeks.|**$104,000**|
|**2. Flow Optimization**|Running equal flow to deep & shallow cells.|**Spatial Resolution:** Proved shallow cells treat **NAFCs 18% better**; optimized routing increases throughput.|**$78,000**|
|**3. Toxicity Proxy**|Running expensive Microtox bio-assays ($8k) quarterly.|**Correlation:** Validated **Panel 2** as a reliable proxy for O2-NAFC toxicity, reducing testing frequency.|**$36,000**|
|**4. Refill Management**|Pausing outflow for 14 days post-refill (conservative).|**Recovery Tracking:** Proved NAFC removal rates recover in 7 days, regaining 1 week of capacity.|**$14,000**|
|**5. Auto-Reporting**|Manual aggregation of data for regulatory submissions.|**Automated Audit Trail:** Aggregates all streams into compliance-ready formats.|**$28,000**|
|**TOTAL ANNUAL VALUE**|||**$260,000**|

## 5. The Joint Discovery (The Upside)

_Note: The values above are validated. The opportunities below are hypotheses we intend to explore with you during this pilot._

While the NAFC Biosensor is the "Key" to unlocking the door, the Confluent platform is designed to manage the entire house. Once the data pipeline is established, we can rapidly expand the system to broader water quality intelligence:

1. **Expanded Biosensor Targets:** Our platform is modular. We can develop and deploy additional biosensor panels for emerging contaminants or specific toxicity markers relevant to your site.

2. **Integrated Chemistry (Salts & Metals):** We ingest your existing Chloride, Metal, and Process Chemical data streams. By correlating these against the NAFC Toxicity data, we can finally answer complex questions like: _"Is it the salt or the acid that is limiting our release potential?"_

3. **Fresh Water Substitution:** Using this integrated view to prove that recycled water (with optimized treatment) is safe for reuse, potentially saving millions in fresh water withdrawal costs.


We do not charge for these "Discovery Modules" upfront. We use the pilot to prove the data value first.

## 6. Deployment: Zero-Friction & IT Safety

We designed this pilot to bypass the typical logistical headaches of site access and IT integration.

### A. "No Boots on Ground" Physical Deployment

- **Offsite Lab Model:** For the pilot phase, we do not need to install hardware at your wetland.

- **Process:** You ship weekly samples to our Calgary facility. We run the **3-Panel Analysis** and push the data to your dashboard.

- **Benefit:** Zero trenching, zero power requirements, and no site access permits required for Luminous staff.


### B. IT Security & Data Sovereignty

We understand that Operational Technology (OT) networks are critical infrastructure. Our architecture respects the "Air Gap."

- **One-Way Ingestion:** We do not require write-access to your SCADA. We accept read-only API access, or simple flat-file (CSV) exports via secure email/FTP.

- **Data Isolation:** Your data resides in a single-tenant, encrypted instance. It is never co-mingled with other operators' data.

- **Plain Text Analytics:** The interface does not require SQL coding or specialized data science training. Operators query the system using plain English (e.g., _"Show me Panel 2 spikes when temp < 10°C"_).


## 7. Project Timeline (9 Months)

- **Month 1:** **Data Ingestion Setup.** We map your historical PDFs and SCADA structure into the Relational Context Engine.

- **Month 2:** **Baseline Calibration.** Analysis of initial samples to calibrate the Biosensor Panels to your specific matrix.

- **Months 3-8:** **Operational Pilot.** Weekly reporting, active optimization recommendations (Flow, Seasonal), and validation of the $260k ROI.

- **Month 9:** **Readiness Report.** Delivery of the 2027 Readiness Baseline (Toxicity Trends) and Final ROI Audit.


## 8. Pilot Deliverables: What You Get

At the end of the 9-month pilot, you receive a comprehensive intelligence package that becomes a permanent operational asset. This isn't just data—it's actionable insight that informs all future remediation projects.

### A. Readiness Baseline Report (The Regulatory Asset)

**Purpose:** The 12-month toxicity trend documentation required for 2027 release authorization.

| Deliverable | Description | Value |
|-------------|-------------|-------|
| **Toxicity Trend Analysis** | 9-month Panel 2 (O2-NAFC) trajectory with seasonal correlations | Proves treatment effectiveness to AER |
| **Compliance-Ready Documentation** | Immutable audit trail, chain of custody, methodology validation | Eliminates "data trust" friction with regulator |
| **Benchmark Dataset** | Your site's toxicity profile vs. industry benchmarks (anonymized) | Positions you as leader vs. peers |

### B. Operational Intelligence Package (The Efficiency Asset)

**Purpose:** Site-specific insights you've never had access to before—each one informs future projects and compounds savings.

| Deliverable | Description | Value |
|-------------|-------------|-------|
| **Seasonal Operating Window Analysis** | Exact temperature correlations for treatment effectiveness | Extend operating season 2-4 weeks/year |
| **Spatial Performance Map** | Cell-by-cell treatment efficiency (shallow vs. deep, vegetated vs. open) | Route flow to highest-performing zones |
| **Refill Recovery Curves** | Site-specific recovery times after each event type | Reduce conservative buffer days by 50% |
| **Treatment Response Profiles** | How your system responds to chemical dosing, flow changes, weather events | Optimize interventions in real-time |
| **Anomaly Detection Library** | Documented "what happened when" correlations | Institutional memory that survives staff turnover |

### C. ROI Validation Report (The Business Case Asset)

**Purpose:** Quantified proof of operational savings to justify ongoing investment and expansion.

| Deliverable | Description | Value |
|-------------|-------------|-------|
| **Validated Savings by Scenario** | Actual $ captured vs. the 5 operational scenarios ($260k target) | Budget justification for annual contract |
| **Payback Analysis** | Pilot cost vs. savings delivered | CFO-ready documentation |
| **Expansion ROI Projections** | "If we deploy to Sites B, C, D, here's the expected return" | Business case for multi-site rollout |

### D. Future Project Intelligence (The Strategic Asset)

**Purpose:** Insights that inform remediation investments beyond this pilot.

| Deliverable | Description | Value |
|-------------|-------------|-------|
| **Treatment Technology Recommendations** | Based on your specific NAFC profile, which remediation approaches will work best | De-risk future capital investments |
| **Monitoring Protocol Optimization** | Recommended sampling frequency, locations, and timing for ongoing operations | Reduce monitoring costs while improving coverage |
| **Regulatory Submission Roadmap** | Step-by-step path to 2027 release authorization using your baseline data | Accelerate approval timeline |

### The Lasting Value

These deliverables don't expire when the pilot ends. They become:
- **Your baseline** for all future water release applications
- **Your playbook** for optimizing treatment operations across all sites
- **Your competitive advantage** over operators who started later

---

## 9. Investment & Next Steps

### Pilot Investment Model: Cost Recovery + Grant Matching

**Our Philosophy:** This pilot is an investment in the partnership, not a revenue opportunity. We're pricing at **cost recovery only** (zero profit margin) to prove the system's value before commercial terms.

**Sampling Strategy:** More samples = higher resolution insights. We recommend maximum practical sampling frequency to capture seasonal variations, treatment responses, and operational correlations. This isn't a per-test model—it's about building the most complete picture possible.

### Cost Structure (9-Month Pilot)

**Total Pilot Cost:** $[TBD] (cost recovery, zero profit margin)

**Cost Components:**
- Lab operations (consumables, analysis, quality control)
- Labor (weekly reporting, optimization recommendations, data integration)
- Platform hosting & technology licensing (data storage, API access, dashboard)
- Lab facility rental (Calgary offsite processing center)
- Grant application coordination (ERA/Alberta Innovates 50% matching)

**Payment Structure: Monthly Retainer Model**
- **Month 1 Retainer (Due upon execution):** $[X] (covers Month 1 estimated costs + setup)
- **Months 2-9 Retainer (Due 1st of each month):** $[X]/month prepaid
- **Monthly Reconciliation:** Actual costs tracked and reconciled at month-end
  - Overage billing: Invoiced with next month's retainer (Net 30)
  - Underage credit: Applied to following month's retainer
- **Grant Matching Applied:** ERA/Alberta Innovates 50% funding reduces monthly retainer by [X]%

**Operator Net Monthly Investment:** $[X]/month (after grant matching)

**Collaborative Partnership Approach:**
This pilot is a joint discovery process. Operator contributions that accelerate insights:
- Historical data access (PDFs, SCADA exports, weather logs)
- Site operations context (seasonal timing, treatment protocols, known anomalies)
- Subject matter expert availability (monthly check-ins, anomaly interpretation)
- Sample collection coordination (if operator staff can assist with logistics)

Any operator-provided resources reduce project overhead and accelerate time-to-insight.

### Grant Matching: The "No-Brainer" Structure

| Funding Source | Contribution | Net Investment |
|----------------|--------------|----------------|
| ERA / Alberta Innovates (50%) | $[TBD] | — |
| **Operator Net Investment** | | **$[TBD]/month** |

**The Math:**
- **Your Monthly Investment:** $[X] (after grant matching)
- **Validated Annual ROI:** $260,000
- **Payback Period:** [X] months
- **Cost of Waiting:** 12-18 month regulatory baseline lag if you start after 2027 guidelines release

### Data Ownership & Confidentiality

- **Your Data:** Operator retains full ownership of all site-specific data generated
- **Luminous Use:** Anonymized, aggregated insights for product improvement only (with written approval)
- **No Co-mingling:** Single-tenant, encrypted instance—your data is never mixed with other operators

### Intellectual Property & Methodology

**Luminous IP (Protected):**
- **Biosensor Technology:** All biosensor panels, assay methodologies, and analysis protocols remain Luminous proprietary IP
- **Relational Context Engine:** Software architecture, correlation algorithms, and data integration methods remain Luminous IP
- **Improvements & Derivatives:** Any modifications, enhancements, or derivative works developed during pilot remain Luminous IP

**Operator Rights:**
- **Data Ownership:** Full ownership of all site-specific data, results, and deliverables
- **Deployment Rights:** Right to use Luminous system at Operator sites under annual monitoring contract
- **No License Restrictions:** Operator can use deliverables (Readiness Baseline, Operational Intelligence) for internal operations and regulatory submissions

**What This Means:**
- Operator gets the operational value (the insights, the data, the $260K savings)
- Luminous retains the methodology (the "how" we generate those insights)
- No joint ownership, no automatic IP transfer

### Transition to Annual Monitoring Contract

**What the Pilot Delivers:**
At completion, Operator receives comprehensive intelligence package (Section 8):
1. **Readiness Baseline Report:** 9-month toxicity trend documentation for 2027 AER release authorization
2. **Operational Intelligence Package:** Site-specific insights (seasonal windows, spatial performance, recovery curves)
3. **ROI Validation Report:** Quantified operational savings achieved during pilot
4. **Future Project Intelligence:** Treatment recommendations and monitoring optimization roadmap

These deliverables become permanent operational assets that inform all future remediation investments.

**Annual Contract Option:**
Upon successful pilot completion, Operator has first right to negotiate ongoing annual monitoring services at commercial rates. Annual contracts include profit margin to support continued R&D, talent retention, and service quality improvements.

**Early Commitment Incentive:**
Operators who execute Letter of Intent (LOI) for annual contract by Month 6 receive:
- Priority deployment scheduling for Year 1 operations
- Fixed pricing protection (Year 1 rates locked)
- Beta access to new biosensor capabilities as developed

### The "Cost of Waiting" Analysis

Operators who delay NAFC baseline data collection until the 2027 guidelines are released will face a **12-18 month lag** to build the required toxicity history.

**The Strategic Risk:**
- Suncor and Imperial are actively evaluating monitoring solutions
- First-mover advantage: Operators with validated baselines will receive expedited release authorization
- The $260k/year operational efficiency compounds—waiting costs real money

By starting now, you secure the Readiness Infrastructure required for release authorization while the system pays for itself through operational efficiencies.

### Next Steps

1. **Technical Discovery Meeting (30 Mins)** - Review historical data availability, site selection, sampling logistics
2. **Grant Application Coordination** - Luminous prepares ERA/AI applications; Operator provides support letter
3. **Pilot Agreement** - Scope, timeline, deliverables, success metrics
4. **Q2 2026 Deployment** - Operational pilot begins with spring thaw

**Timeline to Commitment:** [X weeks] to secure Q2 2026 deployment slot

---

**Wiki Links:**

[[Research Sprint 2: The Validated Wedge]]

[[Research Sprint 4: Confluent Infrastructure Capabilities]]

[[_MASTER-CONTEXT]]

---

**Version History:**
- **V1.5 (Nov 29, 2025):** Updated Section 9 with retainer payment model, IP protection language, and deliverables-focused contract transition. Removed risk reversal guarantee and pilot credit language.
- **V1.4 (Nov 19, 2025):** Added detailed deliverables breakdown (Section 8) and cost recovery pilot economics.
