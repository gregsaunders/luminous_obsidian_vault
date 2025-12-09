# Luminous BioSolutions: Technical Data Sheet

**Tier 2 Monitoring Platform for Naphthenic Acid Quantification in OSPW**

---

## Technology Overview

**Platform:** Panel of three engineered bacterial biosensors for rapid NA quantification
**Publication:** Peer-reviewed in *ACS Synthetic Biology* (2024)
**Positioning:** Tier 2 operational screening to complement HRMS compliance analysis

---

## Performance Specifications

### Detection Limits by Biosensor

| Biosensor | Target NA Class | Detection Limit | Response Time |
|-----------|----------------|-----------------|---------------|
| **p3680-lux** | Classic NAs (cyclopentane/cyclohexane) | 2-4 mg/L | 24 hours |
| **marR-lux** | Complex multi-ring NAs | 7-15 mg/L | 24 hours |
| **atuA-lux** | Acyclic NAs | 15-30 mg/L | 24 hours |

### Correlation with Mass Spectrometry

**Controlled Mesocosm Studies:**
- **Correlation coefficient:** R = -0.98 (statistically significant)
- **Method:** Comparison with Orbitrap Mass Spectrometry
- **Study design:** Greenhouse mesocosm tracking NA degradation across concentration ranges

**Large-Scale Field Pilot:**
- **Qualitative agreement:** Strong concordance with MS trend data
- **Concentration range:** Successfully tracked 70 mg/L → 32-36 mg/L (signal threshold)
- **Study duration:** Multi-season deployment in constructed wetland
- **Performance:** Consistent sensor response in operational field conditions

### Matrix Compatibility

**Raw OSPW Performance:**
- **Success rate:** 22/24 unique raw OSPW samples successfully analyzed
- **Sample preparation:** Minimal preparation required (can analyze raw water)
- **Matrix effects:** Validated in complex OSPW matrices from multiple operators

**Interference Profile:**
- **Non-responsive to:** Alkanes, BTEX, common petroleum hydrocarbons
- **Specificity:** Class-specific response (acyclic vs multi-ring vs classic NAs)
- **Known limitations:** Potential inhibition by extreme toxicity (observed with p3680 in untreated OSPW)

---

## Appropriate Use Cases

### Tier 2 Applications (Primary)

✅ **Operational screening** between HRMS compliance sampling events
✅ **Treatment system optimization** requiring near real-time feedback
✅ **Sample prioritization** for cost-effective HRMS resource allocation
✅ **High-frequency monitoring** at multiple locations (10-50x increase vs HRMS)
✅ **Process control** for biological treatment systems

### HRMS Integration (Required)

**HRMS remains essential for:**
- Regulatory compliance reporting to Alberta Energy Regulator
- Forensic analysis and source apportionment
- Legal chain-of-custody requirements
- Final release confirmation and compliance verification
- Detailed molecular characterization

**Recommended monitoring strategy:**
- Biosensor: Weekly to daily operational screening
- HRMS: Monthly validation and quarterly compliance reporting

---

## Confluent Data Platform Specifications

### Data Management Architecture

**Input:**
- Real-time biosensor data ingestion
- Automated data validation and QA/QC flagging
- Integration with laboratory metadata

**Analytics:**
- Trend analysis and pattern recognition
- Treatment performance metrics
- Statistical process control charts
- Predictive modeling for treatment optimization

**Output:**
- REST API for enterprise system integration
- CSV export for existing LIMS compatibility
- Real-time operational dashboards
- Regulatory reporting templates with immutable audit trails

**Security & Compliance:**
- Timestamped transaction logging
- Role-based access control
- Data integrity verification
- Audit trail for regulatory review

---

## Technical Validation Summary

### Academic Credibility
✅ Peer-reviewed publication (*ACS Synthetic Biology*, 2024)
✅ University of Calgary independent validation
✅ Multi-year field pilot with continuous monitoring
✅ Controlled mesocosm studies with statistical validation

### Operational Validation
✅ Raw OSPW matrix compatibility demonstrated
✅ Multi-season field deployment completed
✅ Treatment system tracking from high to low concentrations
✅ Consistent performance across diverse OSPW samples

### Comparison with Current Methods

| Method | Turnaround | Cost/Sample | Specificity | Use Case |
|--------|-----------|-------------|-------------|----------|
| **FTIR** | Minutes | $10-50 | Low (total acids) | Tier 1: Initial screening |
| **Luminous Biosensor** | 24 hours | $50-150 | Moderate-High (NA classes) | Tier 2: Operational monitoring |
| **HRMS (Orbitrap/FT-ICR)** | 6-8 weeks | $700-1,000 | Excellent (molecular ID) | Tier 3: Compliance/forensics |

---

## Implementation Requirements

### On-Site Requirements
- Basic laboratory space (biosafety level 1)
- Standard incubator and plate reader
- Minimal technical training (protocols provided)
- Quality control standards and validation samples

### Integration Requirements
- Network connectivity for Confluent platform (cloud-based)
- Optional: API integration with existing LIMS systems
- HRMS validation schedule (recommended monthly minimum)
- Standard operating procedures and training (provided)

### Validation Protocol
- Initial correlation study with site-specific OSPW (10-15 paired samples)
- Ongoing QA/QC with reference standards
- Periodic HRMS cross-validation (frequency determined by application)
- Method performance review and optimization

---

## Limitations and Constraints

**Quantitative Range:**
- Signal loss threshold: ~32-36 mg/L (varies by biosensor)
- Not suitable for very low concentration compliance verification (<2 mg/L)
- Semi-quantitative nature requires HRMS calibration for absolute accuracy

**Matrix Effects:**
- Extreme toxicity may inhibit biological response (false negatives possible)
- Site-specific validation required for optimal performance
- Response to humic/fulvic acid interference not fully characterized

**Operational Constraints:**
- 24-hour turnaround (not real-time)
- Requires basic laboratory infrastructure
- Living biosensor system requires proper handling and storage

---

## Technical Support

**Included with Platform:**
- Initial training and method validation
- Standard operating procedures
- Quality control materials
- Technical support hotline
- Confluent platform access and training

**Available Upon Request:**
- Detailed validation study data
- Peer-reviewed publication
- University of Calgary independent validation results
- Site-specific pilot program design

---

**Contact:**
Jeff Violo, COO
Luminous BioSolutions

**For Technical Inquiries:**
Detailed methodology, validation protocols, and performance data available upon request
