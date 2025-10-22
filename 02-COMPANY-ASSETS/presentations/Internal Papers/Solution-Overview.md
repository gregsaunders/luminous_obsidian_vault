# Luminous BioSolutions: Solution Overview

**Three-Tier NA Intelligence Platform for Oil Sands Water Management**
**October 2025**

---

## The Challenge: Managing What You Can't See

The oil sands industry is transitioning from tailings ponds containment to active treatment and release of process-affected water—addressing one of the industry's largest environmental challenges. This shift requires answering a question that current monitoring approaches weren't designed to address:

**"Is Naphthenic Acid treatment working right now, and what should we adjust?"**

**Why Naphthenic Acids matter:** NAs are one of the principal contaminants of concern preventing regulatory approval for water release. You cannot get release approval—even if everything else is clean—if NA levels aren't demonstrated to be safe.

**The monitoring gap:** Current NA analysis relies on High-Resolution Mass Spectrometry (HRMS)—the gold standard for regulatory compliance. HRMS provides molecular-level precision, but with 6-8 week turnaround times and $700-$1,000 per sample, it creates a data scarcity problem. Operators managing multi-million dollar remediation programs with quarterly snapshots of a dynamic biological process—making decisions based on data that's weeks to months old—face an untenable situation.

**Real-world example:** The recent multi-season Kearl engineered wetland study collected 9 NA samples over two field seasons. When degradation rates declined mid-season, this wasn't discovered until the following year's analysis—too late to optimize treatment approaches.

**What's needed:** A complementary monitoring approach that preserves HRMS accuracy for regulatory compliance while enabling operational frequency for process control.

---

## The Solution: Three-Tier NA Monitoring Strategy

Luminous BioSolutions has developed an integrated platform that addresses the operational monitoring gap while maintaining regulatory compliance standards. This approach recognizes that different monitoring tiers serve different purposes.

### **TIER 1: Compliance & Validation (HRMS)**
**What it is:** Gold standard High-Resolution Mass Spectrometry for regulatory NA compliance
**Frequency:** Quarterly to semi-annual
**Turnaround:** 6-8 weeks
**Cost:** $700-$1,000 per sample
**Role:** Validation standard that all other methods must correlate against
**Status:** Already established industry-wide

### **TIER 2: Operational Screening (Luminous Biosensor)**
**What it is:** Peer-reviewed (*ACS Synthetic Biology*, 2024) and field-tested (Kearl Wetland Pilot, 2024/25) biosensor technology specifically targeting Naphthenic Acids
**Frequency:** Daily to weekly across multiple sampling points
**Turnaround:** 24 hours
**Cost:** Monthly/quarterly service fee (not per-test charges—test as frequently as needed)
**Role:** Bridge the gap between compliance events with operational intelligence

**How it works:**
The biosensor uses genetically engineered bacteria that produce a bioluminescent signal when exposed to specific NA compound classes. Three detection panels provide compound-class specificity:
- **Panel 1:** Acyclic NAs
- **Panel 2:** Complex/aromatic NAs
- **Panel 3:** Classical NAs

This panel approach goes beyond simple total NA quantification, providing insight into which NA fractions are responding to treatment—critical for optimizing remediation strategies.

**Field validation:**
Recent field trials at the Kearl engineered wetland study (completed June 2025) demonstrated high correlation between Luminous biosensors and industry gold-standard Orbitrap Mass Spectrometry on real OSPW samples. The technology performs under actual operational conditions, not just controlled laboratory settings.

**Operational capacity:**
- 96 samples processed simultaneously per batch
- Hundreds to thousands of tests per day
- Minimal sample preparation (raw OSPW analysis)
- Results delivered to Confluent platform within 24 hours

**Strategic positioning:**
The biosensor complements HRMS, not replaces it—enabling strategic deployment where HRMS provides molecular-level precision for regulatory compliance while biosensors provide operational frequency for process control. This preserves gold-standard validation for quarterly correlation and regulatory milestones while achieving comprehensive spatial and temporal coverage within existing budgets.

### **TIER 3: AI-Native Intelligence (Confluent Platform)**
**What it is:** AI-native data intelligence platform currently focused on NA data, designed to transform monitoring results into actionable operational insights
**Frequency:** Real-time data aggregation and analysis
**Role:** Decision support system enabling natural language querying, multi-stakeholder transparency, and predictive analytics

**What makes it "AI-native":**
Most environmental data systems are databases with visualization layers—digital filing cabinets. Confluent was built from inception in the era of large language models and graph databases. NA data relationships are explicit and queryable. Unstructured information (decades of PDF reports) becomes searchable alongside structured data (biosensor results, HRMS data, SCADA outputs).

**Key capabilities:**

**1. Natural Language Querying**
Operators ask questions in plain English, not SQL:
- *"Show me all wetland areas where NA levels increased after heavy rain events in last 3 years"*
- *"Compare NA degradation rates between shallow vegetated cells and deep open water cells"*
- *"What treatment adjustments worked when NA levels exceeded thresholds for three consecutive weeks?"*

Confluent queries the graph database, retrieves relevant historical PDFs, correlates with weather and SCADA data, and returns map visualizations, trend charts, historical context, and evidence-based recommendations.

**2. Unified Structured + Unstructured Data**
Current biosensor results automatically link to historical consultant reports describing similar NA conditions. Decades of institutional knowledge trapped in PDFs becomes queryable. The system discovers connections: "Sample #4523 taken at GPS X,Y on Date Z during 15mm rainfall shows NA increase, correlates with increased flow in SCADA data, similar to pattern documented in 2019 consultant report."

**3. Compounding Intelligence Effect**
The platform becomes more valuable with every dataset added:
- **Day 1:** Biosensor data alone provides spatial/temporal visualization
- **Month 3:** + Historical HRMS data enables automatic correlation validation and 5-year baseline context
- **Month 6:** + SCADA & weather data enables environmental correlation and treatment effectiveness analysis
- **Month 12:** + Historical PDF reports unlocks institutional memory and lessons learned
- **Year 2:** + Multiple sites enables cross-site comparison and industry benchmarking

**4. Multi-Stakeholder Transparency**
One platform, three dashboard views—same trusted data, appropriate presentation:

- **Operator Dashboard:** Real-time biosensor results, treatment optimization recommendations, operational alerts, predictive forecasting, full data access
- **Regulator Dashboard:** Compliance metrics, trend analysis, immutable audit trail, automated reporting, threshold comparisons
- **Community/Indigenous Stakeholder Dashboard:** Public-friendly visualizations (color-coded maps, plain language), NA levels relative to safety thresholds, treatment progress, transparency timestamps

This multi-view capability directly addresses OSMWSC September 2025 recommendations requiring operators to demonstrate technology transparency to Indigenous communities and stakeholders. Rather than producing separate reports for different audiences, Confluent provides real-time access to the same trusted data, presented appropriately for each stakeholder group.

**Technical architecture:**
Built on graph database foundation (TerminusDB) with model-agnostic AI orchestration (Claude, GPT-4, Gemini). REST/GraphQL APIs enable integration with existing LIMS, SCADA, and GIS systems. Backend services operational, frontend interfaces finalizing for Q4 2025 deployment.

**Future expansion:**
While currently focused on NA intelligence (the bottleneck preventing water release), Confluent's architecture is designed to eventually integrate monitoring data from other contaminant systems (metals, salts, other organics) as operators expand their comprehensive water treatment programs.

---

## Business Value: Addressing Multiple Operational Challenges

### **1. Risk Reduction: Early Detection**
**Without operational monitoring:** NA treatment failure begins in May. HRMS sample collected July, results September. Failure detected 4 months late. Corrective action too late for seasonal window. Cost: $2-5M wasted, 12-month delay.

**With operational monitoring:** Daily biosensor detects anomaly within 72 hours. Confluent flags similar historical pattern. Operator investigates, discovers flow obstruction, corrects within one week. Seasonal effectiveness preserved.

### **2. Cost Optimization: Strategic HRMS Deployment**
Biosensor enables 10-50x increase in monitoring frequency cost-effectively. Comprehensive spatial coverage (multiple sampling points) AND temporal coverage (daily monitoring) within existing budgets. HRMS reserved for quarterly validation and regulatory milestones.

### **3. Treatment Optimization: Data-Driven Decisions**
High-frequency datasets enable correlation analysis (which parameters drive NA degradation?), A/B testing of treatment approaches with statistical significance, predictive modeling, and continuous improvement through systematic optimization.

### **4. Social License: Transparent Progress**
Real-time community dashboard provides continuous visibility into NA reduction progress. Auditable data trail. Plain-language explanations. Proactive Indigenous engagement addressing OSMWSC transparency requirements. Differentiation through transparency leadership.

### **5. Regulatory Preparedness: Early Positioning**
Operators who establish comprehensive NA monitoring before release standards are finalized (12-18 month timeline) gain positioning advantages: multi-year baseline datasets, established transparency protocols, validated biosensor-HRMS correlation, auditable data trail meeting regulatory scrutiny.

---

## Validation & Credibility

**Peer-Reviewed Science:**
- *ACS Synthetic Biology*, 2024 (biosensor validation publication)
- Additional peer-reviewed papers expected year-end 2025
- University partnerships: Athabasca, Calgary

**Field-Tested Performance:**
- Multi-season Kearl engineered wetland study (completed June 2025)
- High correlation with Orbitrap Mass Spectrometry on real OSPW samples
- Performance under actual operational conditions

**Independent Validation:**
- University partnerships providing credibility
- Consultant engagement (Stantec partnership discussions)
- Indigenous community consultation (Mikisew Cree First Nation)

**Industry Engagement:**
- Active conversations with CNRL, Suncor, Imperial (majority of tailings inventory)
- OSMWSC compliance frameworks ready for deployment

This is operational technology solving real problems today, not theoretical concepts.

---

## Implementation Pathway

### **Phase 1: Validation & Baseline (Months 1-6)**
Establish biosensor-HRMS correlation on site-specific OSPW. Deploy Confluent platform. Integrate historical data (3-5 years HRMS results, consultant reports, regulatory submissions). Operator training. Initial Indigenous community consultation.

**Success metrics:** High biosensor-HRMS correlation demonstrated, operators querying effectively, baseline NA distribution established, stakeholder framework operational.

### **Phase 2: Operational Deployment (Months 7-18)**
Daily biosensor monitoring with 24-hour reporting. Quarterly HRMS validation. AI-generated treatment recommendations tested. Community and regulator dashboards deployed.

**Success metrics:** Quantifiable treatment optimization, early issue detection (72 hours vs. months), 10-50x monitoring frequency increase within budget, transparent reporting satisfying OSMWSC requirements.

### **Phase 3: Scale & Leadership (Months 19+)**
Multi-site deployment (wetlands, end pit lakes, treatment pilots). Cross-site comparative analysis. Stakeholder engagement fully operationalized. Regulatory reporting automation.

**Success metrics:** Comprehensive coverage enterprise-wide, quantified treatment effectiveness, stakeholder confidence, regulatory approval readiness, early positioning advantage.

---

## What Differentiates This Approach

**Most providers offer:** Monitoring solution only. Operator handles stakeholder engagement separately. Basic data storage and reporting. Integration challenges.

**Luminous integrated platform:**
- Technical performance: 24-hour biosensor screening, compound-class specificity
- AI-native intelligence: Natural language querying, historical data integration, predictive analytics
- Regulatory compliance: OSMWSC transparency support, automated reporting, immutable audit trails
- Stakeholder engagement: Multi-dashboard capability, community frameworks, Indigenous engagement support
- Operational intelligence: Treatment recommendations, early warning, cross-site analysis
- System integration: APIs for LIMS, SCADA, GIS—works with existing infrastructure

**The result:** Not just monitoring, but integrated NA intelligence addressing technical, regulatory, and social license challenges.

---

## Regulatory Context: OSMWSC September 2025

The Oil Sands Mine Water Steering Committee recommendations create new requirements:
- Treatment and release standards for OSPW (to be established urgently by Government of Alberta)
- Pilot programs for active and passive NA treatment technologies requiring operational monitoring
- **Stakeholder transparency explicitly required:** "Operators should strive to share relevant information about technologies they are piloting with Indigenous communities, public and stakeholders"
- Operational monitoring emphasized for NAs, not just quarterly compliance snapshots
- Standardized measurement methods for naphthenic acids to be established

**Timeline impact:** Release standards expected within 12-18 months. Operators establishing monitoring capabilities before standards are finalized gain positioning advantages.

---

## Next Steps

### **1. Technical Briefing (45-60 minutes)**
Detailed biosensor validation and field performance data. Confluent architecture demonstration (live natural language querying). Site-specific application discussion. Integration approach. Q&A with Dr. Shawn Lewenza (Chief Science Officer, 10+ years NA research) and Greg Saunders (CTO).

### **2. Pilot Program Development (Collaborative Design)**
Custom NA monitoring program: sampling strategy, data integration roadmap, multi-stakeholder dashboard configuration, success metrics, timeline and budget, stakeholder engagement support.

### **3. Partnership Discussion (Strategic Alignment)**
Long-term relationship: multi-year monitoring program, technology integration with existing providers, regulatory compliance support, Indigenous engagement protocols, industry leadership positioning.

---

**Contact:**
Jeff Violo, COO
Luminous BioSolutions
jeff.violo@luminousbiosolutions.com

**Additional Materials:**
- Peer-reviewed publications (*ACS Synthetic Biology*, 2024; additional papers year-end 2025)
- Technical architecture documentation
- Multi-stakeholder dashboard demonstrations
- OSMWSC compliance framework alignment
- Field validation case studies
- Integration specifications (API documentation)

---

**Luminous BioSolutions: Transforming the Naphthenic Acid bottleneck from an insurmountable barrier into a manageable operational challenge through evidence-based intelligence.**
