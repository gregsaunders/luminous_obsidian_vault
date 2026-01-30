# Squarehead Foundry: Developer Executive Brief
**Customer Outcomes for Oil Sands Tailings Remediation**

**Date:** January 2026 | **Version:** 1.0 | **For:** Development Team

---

## The 30-Second Context

Oil sands operators are shifting from **containment** (storing tailings water indefinitely) to **active treatment** (treating water for eventual release). This requires:

- **High-frequency monitoring** to optimize treatment systems (engineered wetlands)
- **Rapid feedback loops** (72 hours, not 6-8 weeks)
- **Multivariate correlation** to understand why treatment effectiveness changes
- **Regulatory transparency** to prove water meets release standards by 2027

**Squarehead Foundry** is the intelligence layer that makes this possible. It ingests biosensor data + operational/environmental data and delivers the insights operators need to optimize treatment and prove regulatory readiness.

---

## What Squarehead Foundry Does

Takes in multiple data streams:
- **Biosensor results** (daily/weekly naphthenic acid toxicity measurements - formats TBD)
- **SCADA data** (flow rates, water levels, pump operations)
- **Weather data** (temperature, rainfall, sunlight)
- **HRMS validation** (periodic high-resolution chemistry)
- **Historical documents** (consultant reports, studies, operational logs)

Delivers operational intelligence:
- **Detects anomalies** and explains what caused them
- **Optimizes treatment** (flow rates, cell routing, seasonal strategies)
- **Learns from history** (connects current conditions to past events)
- **Proves compliance** (immutable audit trail for regulators and communities)

**Design Note:** Biosensor output formats and reporting structures are still being finalized. Build for flexibility.

---

## The 4 Core Customer Outcomes

### 1. Real-Time Anomaly Detection
**What operators need:** Detect toxicity changes in 72 hours and understand what caused them.

**Example:** Toxicity spikes in Cell 3 → System automatically correlates with flow rate drop + rainfall event → Surfaces similar 2023 pattern and resolution → Operator knows what to do.

**Developer requirements:** Statistical anomaly detection, multivariate correlation engine, historical pattern matching, alert system.

---

### 2. Treatment Optimization
**What operators need:** Make data-driven decisions to maximize wetland performance.

**Example (validated at Kearl):**
- Shallow vegetated cells outperform deep cells by 26%
- Temperature correlation shows treatment viable until 5°C (not calendar shutdown)
- System recommends: "Route 70% flow to vegetated cells in summer, extend season 3 weeks"
- **Result:** $104k seasonal savings + $78k spatial optimization = $182k/year

**Developer requirements:** Performance comparison across locations/conditions, optimization modeling, predictive forecasting, recommendation engine.

---

### 3. Historical Pattern Analysis
**What operators need:** Connect current conditions to past events, preventing repeated mistakes and accelerating learning.

**Example:** Treatment effectiveness drops → System finds similar 2023 event → Shows operators reduced flow rate, recovered in 5 days → Presents option: "Do same intervention (fast recovery, reduced throughput) or wait for natural recovery (slower, maintains throughput)."

**Developer requirements:** Similarity search, document ingestion (PDFs), knowledge graph, outcome tracking, cross-site learning.

---

### 4. Regulatory Compliance & Transparency
**What operators need:** Build defensible evidence that treatment is working for 2027 release authorization.

**Example:**
- Multi-year baseline: "Treatment effectiveness maintained >70% in 87% of monitoring periods"
- Immutable audit trail: Complete chain of custody for all data
- Multi-stakeholder dashboards: Operators get full detail, regulators get compliance metrics, communities get simplified public dashboard

**Developer requirements:** Immutable data storage, audit trail, automated reporting, role-based dashboards (operator/regulator/community views).

---

## Validated Scenarios from Kearl Pilot

**IMPORTANT:** These numbers are **opportunity analysis**—reverse-engineered from the Kearl pilot which used traditional HRMS testing. This shows what high-frequency biosensor monitoring + Squarehead Foundry **would have enabled**. This is a **baseline example**, not a ceiling—actual pilots will likely reveal additional site-specific optimizations.

| Scenario | Decision Enabled | Annual Value |
|----------|------------------|--------------|
| **Seasonal Strategy** | Operate 3 weeks longer based on temperature threshold | $104k |
| **Spatial Optimization** | Route flow to high-performing cells (+26% capacity) | $78k |
| **Toxicity Validation** | Reduce expensive bio-assays by 75% | $36k |
| **Refill Management** | Resume outflow 7 days earlier per event | $14k |
| **Regulatory Reporting** | Auto-generate reports with immutable audit trail | $24k |
| **+ Discovery** | Patterns only visible with high-frequency data | TBD |

**Total validated baseline value:** $260k+/year

---

## Key Technical Capabilities Required

### 1. Multivariate Correlation Engine
- Time-series alignment (different data sources, different frequencies)
- Correlation analysis (identify statistical relationships)
- Lag analysis (X happened, then Y happened 24 hours later)
- Multi-factor analysis (Y caused by combination of X1, X2, X3)
- Causation inference (probable cause, not just correlation)

### 2. Natural Language Query
- Operators ask questions in plain English
- System translates to queries across multiple data sources
- Returns intelligent answers with visualizations

**Example queries:**
- "Show toxicity trends in Cell 3 vs. temperature over past 6 months"
- "What happened when flow rate dropped below 500 m³/hr?"
- "Compare treatment effectiveness between shallow and deep cells"

### 3. Knowledge Graph & Data Integrity (CRITICAL)
**Data integrity is a core requirement, not optional:**
- **Immutable storage:** Data cannot be altered once recorded (regulatory requirement)
- **Auditable:** Complete chain of custody from sample → result → analysis
- **Text-based:** All data stored as text in graph database (AI-readable)
- **Traceable:** Every data point has timestamp, source, lineage

**Graph capabilities:**
- Relationships between samples, locations, cells, conditions, events, outcomes
- Automatic relationship inference
- Pattern recognition across time and space

### 4. Unstructured Data Processing
- PDF ingestion (OCR, table extraction)
- Vector search (find relevant historical documents)
- Semantic understanding of consultant reports, studies

### 5. Multi-Stakeholder Interfaces
- **Operator dashboard:** Real-time, full detail, optimization recommendations
- **Regulator dashboard:** Compliance metrics, audit trail, methodology
- **Community dashboard:** Simplified, public-facing, plain language
- All pulling from same trusted data source

---

## Data Inputs

| Data Source | Frequency | Integration Method |
|-------------|-----------|-------------------|
| Biosensor results | Daily/weekly | CSV upload or API |
| SCADA (flow, levels) | Real-time/hourly | API or CSV export |
| Weather | Hourly/daily | Weather API (auto) |
| HRMS validation | Monthly/quarterly | CSV upload |
| Historical PDFs | One-time | Bulk ingestion |

---

## Development Phases: Crawl, Walk, Run

**Approach:** Build Minimum Viable Product (MVP) first, validate with real users, then expand.

**MVP Goal:** Deliver **one complete outcome end-to-end** (recommend: Anomaly Detection)
- Operator receives alert about anomaly
- System shows what caused it (SCADA/weather correlation)
- Operator takes action based on insight
- Data is auditable and immutable

### Phase 1 (Months 1-3): Foundation - MVP (Crawl)
- Biosensor + HRMS data ingestion
- Time-series visualization
- Basic anomaly detection
- Operator dashboard MVP
- **Immutable data storage** (P0 requirement)

### Phase 2 (Months 4-6): Intelligence (Walk)
- SCADA + weather integration
- Correlation engine (bio + chem + physics)
- Historical pattern matching
- Treatment optimization recommendations
- Natural language query (P1)

### Phase 3 (Months 7-12): Context & Transparency (Run)
- PDF document ingestion
- Knowledge graph
- Advanced pattern recognition
- Regulator + community dashboards
- Automated reporting

### Phase 4 (Months 13+): Predictive (Sprint)
- Forecasting (predict treatment effectiveness)
- Prescriptive recommendations (confidence scoring)
- Cross-site benchmarking
- Continuous learning

**Key:** Don't build Phase 4 until Phases 1-3 are validated with real users.

---

## Success Metrics

**Operator success:**
- Detect issues in 72 hours (vs. 6-8 weeks)
- Increase treatment effectiveness 10-20%
- Extend treatment season 2-4 weeks
- $260k+ annual operational efficiencies

**System success:**
- All data sources ingested automatically
- Natural language queries return results <5 seconds
- Pattern recognition success rate >80%
- System uptime >99%

---

## What Makes This Different

This is not a generic data platform. Squarehead Foundry is purpose-built for **tailings remediation intelligence**:

✅ **Understands the problem:** Naphthenic acids, engineered wetlands, regulatory requirements
✅ **Integrates high-frequency biosensor data** (new capability) with legacy HRMS
✅ **Correlates bio + chem + physics + operations** automatically
✅ **Transparent reasoning** (not black-box AI)
✅ **Serves multiple stakeholders** (operators, regulators, communities)
✅ **Learns over time** (gets smarter with more data and outcomes)

---

## Your Impact as Developers

You're building the **core information tool** that enables the oil sands industry's transition from containment to treatment. Every feature has direct connection to:

- Operators making better decisions faster
- Treatment systems working more effectively
- Regulatory confidence in water release
- Community trust in environmental safety
- Environmental recovery from decades of tailings

This is meaningful work with real environmental and social impact.

---

## Questions or Need Clarification?

**Contact:** Jeff Violo (jeff.violo@luminousbiosolutions.com)

**Detailed Documentation:** See "Squarehead-Foundry-Customer-Outcomes.md" for comprehensive examples and technical requirements.

---

**Core Message:** We don't just give operators data. We give them the operational intelligence to make decisions they couldn't make before.
