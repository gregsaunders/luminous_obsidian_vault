# Pilot Proposal: Integrated Water Readiness Infrastructure

Prepared For: CNRL / [Operator Name] Operations Team

Prepared By: Luminous BioSolutions

Date: November 19, 2025

Status: DRAFT v1.4

## 1. Executive Summary

**The Challenge:** The 2027 AER Water Release Guidelines will hinge on one critical variable: **Naphthenic Acids (NAFCs).** These complex toxins are the primary regulatory barrier to release. Current monitoring (Quarterly HRMS) is too slow for process control, leaving operators blind to the one contaminant that matters most.

**The Proposal:** Luminous BioSolutions proposes a 9-month deployment of our **Readiness Infrastructure**. We combine the industry's only high-frequency NAFC Biosensor ("The Mine Detector") with a Relational Context Engine ("The Map") to solve the toxicity bottleneck.

The Business Case:

Based on validated data from the Imperial Kearl wetland pilot, this system generates $260,000/year in operational efficiencies, delivering a 5-month payback period.

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
    

## 8. Investment & Next Steps

Pilot Investment: [Insert Cost] (Eligible for ERA/Alberta Innovates Matching)

Term: 9 Months

The "Cost of Waiting" Analysis:

Operators who delay NAFC baseline data collection until the 2027 guidelines are released will face a 12-18 month lag to build the required history. By starting now, you secure the Readiness Infrastructure required for release authorization while the system pays for itself through operational efficiencies.

Next Action:

Technical Discovery Meeting (30 Mins) to review historical data availability.

Wiki Links:

[[Research Sprint 2: The Validated Wedge]]

[[Research Sprint 4: Confluent Infrastructure Capabilities]]

[[_MASTER-CONTEXT]]