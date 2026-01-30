# Squarehead Foundry: Customer Outcomes Document
**For Oil Sands Tailings Remediation Programs**

**Document Purpose:** This document translates business outcomes into system requirements for the Squarehead Foundry development team. It bridges non-technical business vision with technical implementation needs.

**Date:** January 2026
**Version:** 1.0
**Author:** Jeff Violo, COO

---

## Executive Context: The Paradigm Shift

### The Historical Challenge
For decades, oil sands operators have operated in **containment mode** because:
- No regulatory pathway existed to release tailings water
- Naphthenic acids (the principal contaminant) are toxic, pervasive, complex to monitor, and don't break down naturally
- High-Resolution Mass Spectrometry (HRMS) was the only available monitoring technology—but it's:
  - **Slow:** 6-8 weeks per result
  - **Expensive:** Not designed for high-frequency testing
  - **Low-throughput:** Cannot support mass-scale monitoring needed for treatment optimization

### The New Reality: Moving to Active Treatment
The 2027 regulatory timeline is forcing a fundamental shift from **containment to treatment**. Engineered wetlands (like the Imperial Oil Kearl-Grow Wetland Project) and other treatment technologies show promise for handling the volume and scale required.

**These treatment programs require:**
- **High-frequency monitoring** to understand treatment performance
- **Rapid feedback loops** to optimize treatment effectiveness
- **Data integration** across biological, chemical, physical, and operational variables
- **Transparent, auditable records** for regulators and Indigenous communities

### Luminous BioSolutions' Role
Our biosensor provides:
- **Rapid results:** 24-72 hours vs. 6-8 weeks
- **High frequency:** Daily/weekly testing capability
- **Cost-effective:** Enables mass-scale monitoring
- **Treatment-focused:** Measures naphthenic acid toxicity (bioavailable fraction that correlates with actual toxicity, not just total NAs)

**Note:** Specific biosensor output formats, reporting structures, and presentation details are still being determined. Developers should design for flexibility in how biosensor data is ingested and displayed.

**Squarehead Foundry** is the intelligence layer that transforms this high-frequency biosensor data—combined with environmental and operational data—into actionable insights that enable treatment optimization.

### Validated Results from Kearl Wetland Pilot

**IMPORTANT CONTEXT: How These Numbers Were Derived**

The Kearl-Grow Wetland pilot operated using traditional methods (HRMS testing, low-frequency sampling). The **$260k+/year value represents opportunity analysis**—we reverse-engineered what high-frequency biosensor monitoring + Squarehead Foundry **would have enabled** if the system had been deployed.

This is a **baseline validated example**, not a ceiling. Actual pilots using our system will likely reveal additional optimization opportunities that weren't visible in retrospective analysis.

| Validated Scenario | Decision Enabled | Annual Value |
|-------------------|------------------|--------------|
| **Seasonal Strategy** | Operate 3 weeks longer (temperature-based shutdown vs. calendar) | $104k |
| **Spatial Optimization** | Route flow to high-performing cells (+26% capacity) | $78k |
| **Toxicity Validation** | Reduce expensive bio-assays by 75% | $36k |
| **Refill Management** | Resume outflow 7 days earlier per refill event | $14k |
| **Regulatory Reporting** | Auto-generate reports with immutable audit trail | $24k |
| **+ Discovery** | Patterns only visible with high-frequency data | TBD |

**Key finding:** High-frequency monitoring reveals patterns invisible to quarterly HRMS sampling—enabling data-driven optimization instead of calendar-based guesswork. The Kearl analysis shows what's possible; actual deployments will uncover site-specific opportunities we can't predict today.

---

## System Vision: Squarehead Foundry's Role

Squarehead Foundry is the **core information tool** for oil sands tailings remediation programs. It ingests multiple data streams and provides the intelligence operators need to:

1. Understand what's happening in their treatment system (monitoring)
2. Understand why it's happening (correlation and causation)
3. Predict what will happen next (forecasting)
4. Decide what actions to take (optimization)
5. Prove to regulators and communities that treatment is working (transparency and compliance)

---

## Data Inputs: What Squarehead Foundry Must Ingest

### 1. **Biosensor Data (Primary Input)**
**Source:** Luminous BioSolutions 3-Panel Biosensor
- **Panel 2 (Toxic Fraction):** Naphthenic acid toxicity levels
- **Frequency:** Daily to weekly measurements
- **Format:** Structured data with timestamps, GPS coordinates, sample IDs
- **Volume:** High-frequency, high-volume testing across multiple sampling locations

**Developer Needs:**
- Automated ingestion pipeline for biosensor results
- Support for spatial data (GPS coordinates of sampling locations)
- Timestamped data with clear sample-to-result traceability
- Ability to handle increasing data volume as monitoring scales up

### 2. **HRMS Data (Validation/Compliance Layer)**
**Source:** High-Resolution Mass Spectrometry lab results
- **Purpose:** Legal compliance, validation of biosensor results
- **Frequency:** Lower frequency (monthly/quarterly)
- **Format:** Detailed chemical composition data

**Developer Needs:**
- Integration capability to cross-reference biosensor results with HRMS validation
- Automatic flagging when biosensor and HRMS results diverge
- Long-term storage for regulatory audit trail

### 3. **SCADA Network Data (Operational Variables)**
**Source:** Site operational systems
- **Examples:** Water flow rates, retention times, pump operations, valve positions, treatment cell water levels
- **Frequency:** Real-time or near-real-time
- **Format:** Time-series data from industrial sensors

**Developer Needs:**
- Real-time data ingestion capability
- Correlation engine to link operational changes to biosensor results
- Ability to identify process anomalies (e.g., flow rate drops, unexpected valve changes)

### 4. **Weather and Environmental Data**
**Source:** On-site weather stations and/or public weather services
- **Rain data:** Precipitation amounts and duration
- **Sunlight data:** Solar radiation, daylight hours
- **Temperature:** Air and water temperature
- **Wind:** Speed and direction
- **Other:** Humidity, atmospheric pressure

**Developer Needs:**
- Integration with weather APIs or on-site weather station data
- Correlation of weather events with treatment performance changes
- Historical weather data storage for pattern analysis

### 5. **Unstructured Historical Data**
**Source:** Legacy documents and reports
- **Examples:** PDF consultant reports, historical studies, regulatory submissions, operational logs
- **Purpose:** Institutional memory, lessons learned, historical context

**Developer Needs:**
- Document ingestion and OCR processing
- Vector search capability to find relevant historical context
- Knowledge graph to link historical events to current conditions

---

## Customer Outcomes: What Oil Sands Operators Need to Achieve

---

## OUTCOME 1: Real-Time Anomaly Detection and Alerting

### What Operators Need to Achieve:
**Detect toxicity changes or treatment performance issues within 72 hours and understand what caused them—not 6-8 weeks later when it's too late to respond.**

### Why This Matters:
- Treatment systems are dynamic—weather, flow rates, seasonal changes all impact performance
- Current HRMS testing means operators learn about problems months after they occur
- Rapid detection enables corrective action before minor issues become major failures
- Seasonal treatment windows are short; operators can't afford to waste time

### Concrete Examples:

**Example 1: Toxicity Spike Detection**
- **Scenario:** Biosensor results show a toxicity spike in Wetland Cell 3
- **What Squarehead Foundry Must Do:**
  - Automatically detect that toxicity increased by 35% compared to the 7-day moving average
  - Alert the operator within hours of receiving the biosensor result
  - Immediately correlate with recent operational and environmental changes:
    - SCADA data shows flow rate to Cell 3 decreased by 40% two days ago
    - Weather data shows 25mm rainfall event occurred 24 hours before spike
    - Historical data shows similar patterns occurred in 2023 under similar conditions
  - Present operator with: "Toxicity spike in Cell 3 likely caused by reduced flow + heavy rainfall. Similar event in Sept 2023 resolved by increasing flow rate to 650 m³/hr."

**Real-world validation (Kearl):**
- 22 of 24 OSPW samples correctly identified as NA-positive (92% accuracy)
- Strong correlation with toxic HRMS fractions
- System demonstrated ability to distinguish OSPW-affected vs. reference waters

**Example 2: Treatment Performance Degradation**
- **Scenario:** Gradual decline in treatment effectiveness across multiple cells over 2 weeks
- **What Squarehead Foundry Must Do:**
  - Detect the trend before it becomes critical
  - Correlate with environmental factors: temperature drop from 18°C to 12°C, reduced sunlight hours
  - Surface historical context: "Wetland biological activity typically decreases when temperature drops below 15°C. 2022 data shows treatment effectiveness dropped 25% during similar conditions."
  - Recommend: "Consider reducing flow rate or extending retention time to maintain treatment effectiveness."

**Real-world validation (Kearl):**
- Mid-season treatment rate dropped 53% (0.53 → 0.25 mg/L/day)
- System correlated drop with temperature shift (expected seasonal variation)
- Prevented unnecessary $12k intervention—"do nothing" was correct response
- Demonstrated critical difference between "anomaly requiring action" vs. "normal seasonal pattern"

**Example 3: Process Failure Detection**
- **Scenario:** Biosensor results show no change in toxicity despite treatment process running
- **What Squarehead Foundry Must Do:**
  - Flag unexpected result: "Expected 10-15% toxicity reduction based on flow rate and retention time, but biosensor shows 0% reduction"
  - Check SCADA data for process anomalies: valve malfunction, pump failure, flow bypass
  - Alert operator: "Treatment effectiveness lower than expected. Check Cell 2 inlet valve position—SCADA shows intermittent operation."

### Developer Requirements Summary:

**Detection Capabilities:**
- Statistical anomaly detection (deviation from baseline, moving averages, expected ranges)
- Trend analysis (gradual changes over time)
- Expected vs. actual performance comparison
- Multi-variable pattern recognition

**Alerting System:**
- Configurable alert thresholds (by parameter, location, severity)
- Multi-channel alerts (dashboard, email, SMS)
- Alert prioritization (critical vs. informational)
- Alert escalation (if not acknowledged)

**Correlation Engine:**
- Automatic correlation of biosensor results with:
  - SCADA operational data (time-aligned, +/- 48 hours)
  - Weather events (rainfall, temperature changes)
  - Historical similar patterns
- Causation analysis: "X likely caused by Y because Z"
- Multi-factor analysis: "X caused by combination of Y and Z"

**Historical Context Retrieval:**
- Similar pattern matching: "This has happened before under these conditions"
- Outcome tracking: "When this happened before, operators did X and the result was Y"
- Lessons learned: Surface relevant reports, studies, operational logs

---

## OUTCOME 2: Treatment Optimization Decisions

### What Operators Need to Achieve:
**Make data-driven decisions to optimize engineered wetland performance: adjusting flow rates, retention times, cell configurations, and seasonal strategies to maximize treatment effectiveness.**

### Why This Matters:
- Engineered wetlands are new at this scale—operators are learning what works
- Treatment effectiveness varies based on weather, season, water chemistry, biological activity
- Optimization requires testing different approaches and learning from results
- Each site has unique characteristics—solutions must be tailored

### Concrete Examples:

**Example 1: Flow Rate Optimization**
- **Scenario:** Operator wants to maximize throughput while maintaining treatment effectiveness
- **What Squarehead Foundry Must Do:**
  - Analyze historical data: "At flow rates 400-500 m³/hr, average toxicity reduction is 18%. At 500-600 m³/hr, reduction drops to 12%. At 600-700 m³/hr, reduction drops to 8%."
  - Correlate with environmental factors: "Treatment effectiveness improves by 5% when water temperature > 16°C, suggesting higher flow rates may be viable in summer."
  - Provide recommendation: "Current conditions (temp 17°C, sunny) suggest optimal flow rate is 550-600 m³/hr. This balances throughput and treatment effectiveness."
  - Enable testing: "To test if 650 m³/hr is viable, increase flow gradually and monitor biosensor results over 5-7 days."

**Real-world validation (Kearl):**
- Temperature-toxicity correlation identified: NA bioavailability drops below 15°C
- **Decision enabled:** Extend operating season by 3 weeks (until temperature reaches 5°C threshold instead of calendar shutdown date)
- **Value:** $104k/year in additional treatment capacity

**Example 2: Seasonal Strategy Optimization**
- **Scenario:** Operator wants to extend treatment season into shoulder months (early spring, late fall)
- **What Squarehead Foundry Must Do:**
  - Analyze seasonal performance patterns: "Historical data shows treatment effectiveness drops below 10% when temperature < 10°C or sunlight < 6 hours/day"
  - Identify seasonal windows: "2024 data shows treatment remained effective until Nov 15 (temp 11°C). 2025 spring treatment became effective after April 10 (temp 12°C)."
  - Predict seasonal transitions: "Based on 5-year weather data, average fall transition is Nov 10-20. Current year trending 5 days earlier."
  - Recommend: "Begin reducing flow rate by Oct 25 to prepare for seasonal shutdown. Consider early spring startup if temps reach 12°C by April 1."

**Example 3: Cell Configuration Optimization**
- **Scenario:** Wetland has multiple cells with different characteristics (depth, vegetation, size)—operator wants to know which cells perform best under which conditions
- **What Squarehead Foundry Must Do:**
  - Compare performance across cells: "Cell 1 (shallow, vegetated) achieves 22% reduction in summer but only 8% in fall. Cell 3 (deep, open water) achieves 15% reduction year-round."
  - Correlate with conditions: "Vegetated cells outperform in warm, sunny conditions (temp > 18°C, sunlight > 10 hrs). Deep cells maintain consistent performance across seasons."
  - Recommend adaptive strategies: "Route 70% of flow through vegetated cells in summer, 30% in winter. Use deep cells for consistent baseline treatment."
  - Enable A/B testing: "Test Cell 2 configuration change: Add vegetation to 50% of cell surface. Monitor treatment effectiveness over 30 days vs. baseline."

**Real-world validation (Kearl):**
- Cell 4 outperformed Cell 3 by 26%
- **Decision enabled:** Route 60% more flow to high-performing cells without building new infrastructure
- **Value:** $78k/year in increased capacity through intelligent flow routing

**Example 4: Retention Time Optimization**
- **Scenario:** Operator wants to understand minimum retention time needed for effective treatment
- **What Squarehead Foundry Must Do:**
  - Analyze retention time vs. effectiveness: "Biosensor data shows toxicity reduction continues for 5-7 days after water enters wetland, then plateaus. 80% of total reduction occurs in first 4 days."
  - Correlate with flow rate: "At 500 m³/hr flow, average retention time is 6 days. Increasing to 600 m³/hr reduces retention to 5 days but maintains 85% of treatment effectiveness."
  - Provide optimization guidance: "To maximize throughput while maintaining effectiveness, target 5-day minimum retention time in summer, 7-day in winter when biological activity is lower."

**Real-world validation (Kearl):**
- High-frequency monitoring enabled recovery tracking after OSPW refill events
- **Decision enabled:** Resume outflow 7 days earlier per refill event (vs. 14-day "safety margin")
- **Value:** $14k/year in recaptured treatment capacity

### Developer Requirements Summary:

**Analysis Capabilities:**
- Multi-variable correlation analysis (identify relationships between inputs and outcomes)
- Performance comparison across locations, time periods, configurations
- Optimization modeling (what-if scenarios, sensitivity analysis)
- A/B testing framework (compare different approaches, track outcomes)

**Decision Support:**
- Recommendation engine based on current conditions + historical outcomes
- Confidence scoring ("high confidence this will work" vs. "experimental, uncertain outcome")
- Risk assessment (potential downside of proposed action)
- Trade-off analysis (throughput vs. effectiveness, cost vs. performance)

**Predictive Modeling:**
- Forecast treatment effectiveness based on weather forecasts
- Predict seasonal transition points
- Estimate time-to-result for different operational changes
- Project long-term performance trends

**Learning System:**
- Track operator decisions and outcomes (what was tried, what worked)
- Build institutional knowledge over time
- Improve recommendations as more data is collected
- Capture "tribal knowledge" (operator insights, lessons learned)

---

## OUTCOME 3: Historical Pattern Analysis and Learning

### What Operators Need to Achieve:
**Connect current conditions to past events and outcomes, building institutional knowledge that prevents operators from repeating mistakes and accelerates learning across the organization.**

### Why This Matters:
- Treatment programs are new—operators are learning by doing
- Personnel turnover means knowledge gets lost
- Historical reports and data exist but are locked in PDFs and spreadsheets
- Similar problems have often been solved before—but operators don't know it
- Industry needs to build collective intelligence, not start from scratch at every site

### Concrete Examples:

**Example 1: "This Has Happened Before"**
- **Scenario:** Biosensor shows unusual toxicity pattern operator hasn't seen before
- **What Squarehead Foundry Must Do:**
  - Search historical data: "Similar pattern occurred July 2022 in Cell 4 and October 2023 in Cell 1"
  - Surface relevant context: "2022 event correlated with heavy rainfall (40mm in 24 hours) following 3-week dry period. Toxicity returned to baseline within 10 days without intervention."
  - Retrieve historical documents: Pull 2022 consultant report that analyzed the event and recommended "no action needed for rainfall-induced spikes < 50% above baseline"
  - Provide operator with: "Current pattern matches historical rainfall-induced spike. Based on past events, expect return to baseline within 7-10 days. Monitor but no intervention needed unless spike exceeds 60% above baseline."

**Real-world validation (Kearl):**
- Predictable NA dynamics identified across freeze/thaw cycles
- Seasonal patterns enable proactive management instead of reactive troubleshooting
- Historical pattern matching prevents unnecessary interventions (saving costs and maintaining throughput)

**Example 2: "What Worked Last Time"**
- **Scenario:** Treatment effectiveness dropping, operator considering intervention
- **What Squarehead Foundry Must Do:**
  - Identify similar historical situations: "Treatment effectiveness dropped to similar levels in Sept 2023 and April 2024"
  - Retrieve actions taken: "Sept 2023: Reduced flow rate from 600 to 450 m³/hr. Result: Effectiveness improved 12% within 5 days. April 2024: No action taken. Result: Effectiveness naturally recovered after 3 weeks when temperature increased."
  - Analyze outcomes: "Flow rate reduction provided faster recovery but reduced throughput by 25%. Natural recovery took longer but maintained throughput."
  - Present options: "Based on historical outcomes: Option 1 - Reduce flow rate for rapid recovery (cost: reduced throughput). Option 2 - Monitor and wait for natural recovery (cost: 2-3 weeks of reduced effectiveness)."

**Example 3: "Learning from Other Sites"**
- **Scenario:** Operator at Site A facing issue that Site B solved 6 months ago
- **What Squarehead Foundry Must Do:**
  - Cross-site pattern matching: "Current conditions at Site A match conditions at Site B in June 2025"
  - Surface Site B solution: "Site B operators addressed similar issue by adjusting inlet diffuser design, resulting in 18% improvement in treatment effectiveness"
  - Provide context: "Site B has similar water chemistry (naphthenic acid 45mg/L) and wetland design (shallow vegetated cells)"
  - Recommend: "Consider implementing Site B's inlet diffuser modification. Historical data suggests high probability of similar improvement."

**Example 4: "Building the Knowledge Base"**
- **Scenario:** Operator discovers that pre-treating influent with aeration improves wetland performance
- **What Squarehead Foundry Must Do:**
  - Document the discovery: Capture operator notes, link to biosensor data showing improvement, record operational parameters
  - Make it searchable: Future operators searching "how to improve wetland performance" or "pre-treatment options" will find this
  - Track replication: When other sites try the same approach, track whether results are consistent
  - Build best practices: "Aeration pre-treatment has been tested at 3 sites with average 15% improvement in treatment effectiveness (range: 12-19%). Recommended as standard practice."

**Example 5: "Preventing Repeated Mistakes"**
- **Scenario:** New operator considers intervention that was tried before and failed
- **What Squarehead Foundry Must Do:**
  - Flag potential issue: "Similar approach was attempted in March 2024"
  - Surface negative outcome: "March 2024 trial: Increased flow rate to 750 m³/hr resulted in treatment effectiveness dropping to 5% and required 3-week recovery period"
  - Explain why it failed: "High flow rate exceeded wetland's biological processing capacity, causing system shock"
  - Warn operator: "Historical data suggests this approach has high risk of negative outcome. Consider alternative: gradual flow increase in 50 m³/hr increments with 1-week monitoring between steps."

### Developer Requirements Summary:

**Pattern Matching Capabilities:**
- Similarity search across time periods, locations, conditions
- Multi-dimensional pattern recognition (biosensor + SCADA + weather + outcomes)
- Cross-site pattern matching
- Anomaly recognition ("this is genuinely new, no historical match")

**Historical Context Retrieval:**
- Natural language search across structured and unstructured data
- Document analysis and extraction (PDF reports, consultant studies, operator logs)
- Timeline reconstruction ("what happened, in what order, what was the outcome")
- Causal chain analysis ("X led to Y which caused Z")

**Knowledge Capture:**
- Operator annotation system (add notes, observations, insights to data)
- Outcome tracking (what was tried, what worked, what didn't)
- Best practices documentation (automatically identify successful approaches)
- Failure analysis (document what went wrong and why)

**Knowledge Sharing:**
- Cross-site knowledge base (learnings from one site available to others)
- Recommendation system ("based on what worked elsewhere, try this")
- Lessons learned library (searchable, categorized, tagged)
- Continuous learning (system gets smarter as more data and outcomes are added)

**Institutional Memory:**
- Persist knowledge across personnel changes
- Make tribal knowledge explicit and searchable
- Prevent knowledge loss when experienced operators leave
- Accelerate new operator onboarding (access to historical context)

---

## OUTCOME 4: Regulatory Reporting and Compliance

### What Operators Need to Achieve:
**Build defensible, auditable evidence that treatment is working and water meets release standards—providing transparency to regulators, Indigenous communities, and the public.**

### Why This Matters:
- 2027 regulatory release standards require proof that water is safe
- Regulators need confidence in monitoring data quality and treatment effectiveness
- Indigenous communities require transparency and trust-building
- Social license to operate depends on demonstrable environmental responsibility
- Operators need to prove they can maintain treatment performance over time

### Concrete Examples:

**Example 1: Building the Baseline**
- **Scenario:** Operator needs to establish multi-year baseline of water quality to demonstrate treatment progress
- **What Squarehead Foundry Must Do:**
  - Aggregate all biosensor and HRMS data over time
  - Visualize trends: "Influent toxicity baseline: 45 ± 8 mg/L naphthenic acids (2023-2025 average)"
  - Track treatment effectiveness: "Effluent toxicity: 12 ± 4 mg/L (73% average reduction over 2 years)"
  - Show consistency: "Treatment effectiveness maintained >70% in 87% of monitoring periods"
  - Provide regulatory report: "Multi-year baseline demonstrates consistent treatment performance, meeting proposed 2027 release criteria"

**Example 2: Immutable Audit Trail**
- **Scenario:** Regulator audits operator's monitoring data and treatment claims
- **What Squarehead Foundry Must Do:**
  - Provide complete chain of custody: Sample ID → Collection timestamp → GPS coordinates → Biosensor result → HRMS validation → Treatment calculation
  - Ensure data immutability: "All records timestamped and cryptographically signed, cannot be altered retroactively"
  - Cross-validate biosensor with HRMS: "98.2% correlation between biosensor results and HRMS validation testing"
  - Provide transparent methodology: "Treatment effectiveness calculated as (Influent - Effluent) / Influent × 100%. Methodology documented and consistent across all time periods."
  - Export audit package: Complete dataset, methodology documentation, validation results, quality control records

**Example 3: Real-Time Community Dashboard**
- **Scenario:** Indigenous community wants to monitor treatment progress and water quality in real-time
- **What Squarehead Foundry Must Do:**
  - Provide public-facing dashboard with simplified, non-technical visualizations
  - Show current status: "Water toxicity: 12 mg/L (Target: <15 mg/L)" with green/yellow/red indicators
  - Trend over time: "Treatment effectiveness over past 90 days" with easy-to-understand graph
  - Contextualize data: "Current water quality is 75% improved compared to untreated tailings water"
  - Provide transparency: "Data updated daily, last updated 2 hours ago"
  - Enable questions: Link to contact information or FAQ about monitoring program

**Example 4: Automated Regulatory Reporting**
- **Scenario:** Operator must submit quarterly monitoring reports to regulator
- **What Squarehead Foundry Must Do:**
  - Auto-generate report: "Q1 2026 Monitoring Report - Site A Wetland Treatment System"
  - Include required elements:
    - Summary statistics (average, min, max, standard deviation for all parameters)
    - Number of samples collected and analyzed
    - Quality control results (blanks, duplicates, spike recoveries)
    - Treatment performance metrics
    - Exceedances or anomalies with explanations
    - Comparison to regulatory thresholds
  - Format for submission: Generate PDF report in regulator-required format
  - Provide supporting data: Export raw data in regulator-specified format (Excel, CSV)

**Example 5: Proving Treatment Consistency**
- **Scenario:** Regulator questions whether treatment will remain effective under different conditions
- **What Squarehead Foundry Must Do:**
  - Demonstrate performance across conditions:
    - "Treatment effectiveness in summer (temp >18°C): 78% ± 6%"
    - "Treatment effectiveness in spring/fall (temp 10-18°C): 71% ± 9%"
    - "Treatment effectiveness during high-flow events: 65% ± 12%"
  - Show adaptive management: "During low-effectiveness periods, flow rate reduced to maintain >70% treatment effectiveness"
  - Provide statistical confidence: "95% confidence interval for annual average treatment effectiveness: 70-75%"
  - Demonstrate understanding: "System performance well-characterized. Operators can predict and maintain effectiveness under varying conditions."

**Example 6: Multi-Stakeholder Transparency**
- **Scenario:** Same data needs to be presented differently to operators, regulators, and community
- **What Squarehead Foundry Must Do:**
  - **Operator View:** Full technical detail, real-time alerts, optimization recommendations, all raw data
  - **Regulator View:** Compliance metrics, statistical summaries, audit trail, methodology documentation, threshold comparisons
  - **Community View:** Simplified visualizations, plain-language explanations, trend indicators (improving/stable/declining), context relative to safety standards
  - **Shared Foundation:** All views pull from same trusted data source, ensuring consistency and preventing "different numbers for different audiences"

### Developer Requirements Summary:

**Data Integrity:**
- Immutable data storage (tamper-proof, auditable)
- Chain of custody tracking (sample → result → validation)
- Timestamp and geolocation for all data points
- Version control (track any corrections or reprocessing)
- Digital signatures (cryptographic proof of data authenticity)

**Quality Control:**
- Automated QC checks (blanks, duplicates, spike recoveries)
- Cross-validation (biosensor vs. HRMS)
- Outlier detection and flagging
- Data quality scoring
- Quality assurance documentation

**Reporting Engine:**
- Automated report generation (regulatory formats)
- Customizable templates (different regulators, different requirements)
- Statistical analysis (summary stats, trends, confidence intervals)
- Data export (CSV, Excel, PDF, regulatory portal formats)
- Report scheduling (automatic quarterly/annual reports)

**Multi-Stakeholder Dashboards:**
- Role-based access control (operator / regulator / community views)
- Simplified public dashboard (non-technical, visual)
- Technical operator dashboard (full detail, real-time)
- Regulatory compliance dashboard (audit trail, methodology)
- All pulling from single trusted data source

**Compliance Tracking:**
- Threshold monitoring (alert when approaching or exceeding limits)
- Regulatory criteria comparison (current data vs. 2027 standards)
- Exceedance documentation (automatic flags + require explanation)
- Performance metrics (treatment effectiveness, consistency, reliability)
- Trend analysis (improving/stable/declining over time)

**Transparency Features:**
- Public data access (community dashboard, no login required)
- Plain-language explanations (no jargon, contextualized)
- Visual indicators (green/yellow/red, simple graphs)
- Real-time updates (show data freshness, "last updated X hours ago")
- Contact/feedback mechanism (enable questions, build trust)

---

## Cross-Cutting System Requirements

These requirements apply across all four outcome areas:

### 1. **Multivariate Correlation Engine**
The core intelligence of Squarehead Foundry is its ability to automatically identify relationships between variables:
- Biosensor results ↔ SCADA operational data
- Biosensor results ↔ Weather/environmental data
- Treatment effectiveness ↔ Seasonal patterns
- Current conditions ↔ Historical patterns
- Operational changes ↔ Performance outcomes

**Developer Requirements:**
- Time-series alignment (align data from different sources by timestamp)
- Correlation analysis (identify statistical relationships)
- Lag analysis (X happened, then Y happened 24 hours later)
- Multi-factor analysis (Y was caused by combination of X1, X2, X3)
- Causation inference (not just correlation, but probable cause)

### 2. **Natural Language Query Interface**
Non-technical operators need to ask questions in plain English and get intelligent answers:

**Example Queries:**
- "Show me toxicity trends in Cell 3 over the past 6 months"
- "What happened when toxicity spiked in September 2024?"
- "Compare treatment effectiveness between shallow and deep cells"
- "What weather conditions are associated with best treatment performance?"
- "Find all times when flow rate dropped below 500 m³/hr and show what happened to toxicity"

**Developer Requirements:**
- Natural language processing (understand operator intent)
- Query translation (convert English to database queries)
- Multi-source query (pull from biosensor + SCADA + weather + documents)
- Intelligent response (answer the question, provide context, suggest follow-up)
- Visualization generation (create appropriate charts/graphs for query results)

### 3. **Knowledge Graph Architecture & Data Integrity**
Squarehead Foundry must understand relationships between entities:
- Samples connected to locations
- Locations connected to wetland cells
- Cells connected to treatment configurations
- Results connected to operational conditions
- Conditions connected to weather events
- Events connected to historical precedents

**CRITICAL REQUIREMENT: Data Integrity**

All data must be:
- **Immutable:** Once recorded, data cannot be altered or deleted (regulatory requirement)
- **Auditable:** Complete chain of custody from sample collection → result → analysis
- **Text-based:** All data stored in graph database as text format (AI-readable, queryable)
- **Traceable:** Every data point has timestamp, source, and lineage
- **Transparent:** Regulators and auditors can verify data integrity

This is not a nice-to-have—it's a **core requirement** for regulatory compliance and social license.

**Developer Requirements:**
- Graph database with immutability features (TerminusDB recommended)
- Relationship mapping (define entity types and relationships)
- Automatic relationship inference (discover implicit connections)
- Graph traversal (follow chains of relationships)
- Pattern recognition (identify recurring relationship patterns)
- Data versioning and audit trail (all changes logged)
- Cryptographic verification (optional: digital signatures for data authenticity)

### 4. **Unstructured Data Processing**
Much of the valuable historical context exists in PDF reports, consultant studies, regulatory submissions:

**Developer Requirements:**
- Document ingestion pipeline (drag-and-drop folder, automatic processing)
- OCR and text extraction (handle scanned PDFs)
- Table extraction (pull data tables from PDFs)
- Metadata extraction (date, author, project, location from documents)
- Vector search (find relevant documents based on semantic similarity)
- Chunking and indexing (break documents into searchable segments)

### 5. **Compounding Intelligence**
Squarehead Foundry gets smarter over time as more data is added:
- Month 1: Basic visualization of biosensor results
- Month 3: + HRMS validation, anomaly detection
- Month 6: + SCADA/weather correlation, treatment optimization
- Month 12: + Historical PDF context, predictive modeling
- Year 2: + Cross-site learning, industry benchmarking

**Developer Requirements:**
- Modular data ingestion (easy to add new data sources)
- Backward integration (new data sources enrich old data)
- Progressive enhancement (system capabilities expand as data grows)
- Cross-dataset correlation (new data automatically correlated with existing)

### 6. **Visualization and Interface**
Different users need different views of the same data:

**Operator View:**
- Real-time dashboards (current status, recent trends)
- Alert notifications (critical issues, anomalies)
- Diagnostic tools (drill down into specific issues)
- Optimization recommendations (suggested actions)
- Full data access (view raw data, export datasets)

**Regulator View:**
- Compliance dashboards (metrics vs. thresholds)
- Audit trail (data provenance, QC results)
- Statistical summaries (long-term trends, confidence intervals)
- Report export (regulatory formats)
- Methodology documentation (transparent methods)

**Community View:**
- Simplified visualizations (easy-to-understand)
- Plain language (no jargon)
- Contextual information (what the numbers mean)
- Trend indicators (improving/stable/declining)
- Public access (no login required)

**Developer Requirements:**
- Role-based dashboards (different views for different users)
- Responsive design (works on desktop, tablet, mobile)
- Interactive visualizations (zoom, filter, drill-down)
- Export capabilities (PNG, PDF, data downloads)
- Real-time updates (websockets or polling)

### 7. **Integration Architecture**
Squarehead Foundry must integrate with existing systems:

**Integration Points:**
- Biosensor LIMS (automatic result ingestion)
- SCADA systems (real-time operational data)
- Weather services (APIs or on-site stations)
- Laboratory systems (HRMS results)
- Document repositories (SharePoint, network drives)
- Regulatory portals (automated report submission)

**Developer Requirements:**
- REST/GraphQL APIs (standard integration interfaces)
- Webhook support (real-time push notifications)
- File watch (auto-ingest from shared folders)
- API authentication (secure, token-based)
- Rate limiting and retry logic (robust integration)
- Integration monitoring (detect and alert on failures)

### 8. **Performance and Scalability**
Squarehead Foundry must handle growing data volumes:

**Scale Requirements:**
- Daily biosensor data: 10-100 samples per day per site
- SCADA data: 1-minute intervals, multiple parameters
- Weather data: Hourly updates
- Multi-site deployment: 5-20 sites over time
- Historical data: 5-10 years of legacy data
- User queries: Multiple simultaneous users

**Developer Requirements:**
- Efficient data storage (time-series optimized)
- Query optimization (fast response times even with large datasets)
- Caching (frequently accessed data and queries)
- Asynchronous processing (long-running analysis jobs)
- Horizontal scaling (add capacity as needed)

---

## Success Criteria: How We'll Know This Is Working

### Operator Success Metrics:
- **Time to decision:** Detect and diagnose issues in 72 hours (vs. 6-8 weeks with HRMS alone)
- **Treatment optimization:** Increase treatment effectiveness by 10-20% through data-driven adjustments
- **Seasonal extension:** Extend treatment season by 2-4 weeks through better seasonal strategy
- **Efficiency gains:** $260k+/year in operational efficiencies (validated at Kearl)
- **Learning acceleration:** New operators productive in weeks, not months

### Regulatory Success Metrics:
- **Baseline establishment:** Multi-year defensible baseline for 2027 release authorization
- **Data quality:** >95% cross-validation between biosensor and HRMS
- **Audit readiness:** Complete immutable audit trail for all monitoring data
- **Reporting efficiency:** Automated quarterly/annual reports (vs. manual compilation)
- **Compliance confidence:** Demonstrate consistent achievement of treatment targets

### Community Success Metrics:
- **Transparency:** Real-time public dashboard showing treatment progress
- **Trust building:** Plain-language explanations accessible to non-technical audiences
- **Engagement:** Community able to ask questions and understand responses
- **Social license:** Demonstrable commitment to environmental responsibility

### System Success Metrics:
- **Data integration:** All data sources (biosensor, HRMS, SCADA, weather) ingested automatically
- **Query performance:** Natural language queries return results in <5 seconds
- **Pattern recognition:** Successfully identify similar historical patterns in >80% of cases
- **Recommendation quality:** Operator follow-through on recommendations in >70% of cases
- **Uptime:** >99% system availability (minimal downtime)

---

## Development Priorities: Crawl, Walk, Run Approach

**Philosophy:** Build Minimum Viable Product (MVP) first, validate with real users, then expand capabilities based on actual usage patterns and feedback.

### What Is MVP?

The MVP must deliver **one complete outcome end-to-end** that demonstrates value to operators. Recommendation: Start with **Outcome 1 (Real-Time Anomaly Detection)** because it:
- Requires fewer dependencies (biosensor + SCADA + weather)
- Delivers immediate value (detect problems in 72 hours vs. weeks)
- Validates core correlation engine
- Proves data integrity/auditability
- Builds foundation for other outcomes

**MVP Success Criteria:**
- Operator receives alert about anomaly
- System shows what caused it (correlation with SCADA/weather)
- Operator takes action based on insight
- Data is auditable and immutable

Once MVP proves value, expand to Outcomes 2-4.

---

### Phase 1 (Months 1-3): Foundation - MVP
**Goal:** Core data ingestion and visualization for anomaly detection

**Must-Have (P0) - MVP Cannot Launch Without:**
- Biosensor data ingestion (automated, timestamped, geolocated)
- HRMS data ingestion (validation cross-referencing)
- Basic time-series visualization (trends, maps)
- Anomaly detection (statistical outliers, threshold exceedances)
- Alert system (email notifications for critical issues)
- Operator dashboard (current status, recent trends)
- **Immutable data storage** (audit trail from day 1)

### Phase 2 (Months 4-6): Intelligence - Walk
**Goal:** Multivariate correlation and optimization support (Outcomes 1 + 2)

**Must-Have (P0):**
- SCADA data integration (real-time operational data)
- Weather data integration (automated ingestion)
- Correlation engine (bio + chem + physics + operations)
- Historical pattern matching (similar conditions, outcomes)
- Treatment optimization recommendations (flow rate, retention time)

**Should-Have (P1) - Significantly Improves Experience:**
- Natural language query (basic English questions)
- Performance comparison across cells/locations

### Phase 3 (Months 7-12): Context and Transparency - Run
**Goal:** Historical knowledge base and multi-stakeholder access (All 4 Outcomes)

**Must-Have (P0):**
- PDF document ingestion (OCR, table extraction, vector search)
- Knowledge graph (relationships between entities, events, outcomes)
- Advanced pattern recognition (Outcome 3: Historical learning)
- Regulator dashboard (compliance metrics, audit trail)
- Community dashboard (simplified, public-facing)
- Automated reporting (quarterly/annual regulatory reports)

**Should-Have (P1):**
- Cross-site pattern recognition (learn from multiple operators)
- Advanced natural language query (complex multi-factor questions)

### Phase 4 (Months 13+): Predictive Intelligence - Sprint
**Goal:** Forecasting and proactive optimization

**Nice-to-Have (P2) - Future Enhancement:**
- Predictive modeling (forecast treatment effectiveness based on weather)
- Seasonal transition prediction (when to start/stop treatment)
- Prescriptive recommendations (what to do next, with confidence scoring)
- Cross-site benchmarking (compare performance across sites)
- Industry knowledge base (best practices, lessons learned)
- Continuous learning (system improves as more data and outcomes added)

**Key Principle:** Don't build Phase 4 features until Phases 1-3 are validated with real users. Let actual usage patterns guide which predictive capabilities deliver most value.

---

## Closing Thoughts for Developers

### What Makes Squarehead Foundry Different

This is not a generic data platform or a "black box" AI system. Squarehead Foundry is purpose-built for oil sands tailings remediation:

**It's a remediation intelligence system** that:
- Understands the unique challenges of naphthenic acid treatment
- Integrates high-frequency biosensor data (new capability) with legacy HRMS data
- Correlates biological, chemical, physical, and operational variables
- Learns from every decision and outcome
- Provides transparent, auditable reasoning (not black-box predictions)
- Serves multiple stakeholders with different needs (operators, regulators, communities)

**It enables a fundamental industry shift:**
- From containment → active treatment
- From slow forensic analysis → rapid operational intelligence
- From guesswork → data-driven optimization
- From opacity → transparency and social license
- From starting over each time → building collective industry knowledge

### Your Role as Developers

You're not just building a data platform—you're building the **core information tool that enables the oil sands industry to transition from containment to treatment**.

Every feature you build has a direct connection to:
- Operators making better decisions faster
- Treatment systems working more effectively
- Regulatory confidence in water release readiness
- Communities trusting that water is safe
- Environmental recovery from decades of tailings accumulation

This is meaningful work with real environmental and social impact.

---

## Questions for Developers?

This document is meant to bridge business vision with technical implementation. If you have questions about:
- **Why** a particular outcome matters
- **How** operators would use a feature
- **What** "good enough" looks like vs. "gold-plated"
- **When** to prioritize one feature over another

Please reach out to Jeff Violo (jeff.violo@luminousbiosolutions.com).

The goal is alignment: ensuring what you're building matches what our customers need and how they'll actually use it.

---

**Document Version:** 1.0
**Last Updated:** January 2026
**Next Review:** After Phase 1 development (Month 3)
