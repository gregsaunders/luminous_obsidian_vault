# Detailed Summary: Naphthenic Acids Biosensors Presentation

**Presenter:** Dr. Shawn Lewenza (Athabasca University & University of Calgary)  
**Event:** NAFC Measurement Workshop hosted by NAIT  
**Date:** July 29, 2025

## Overview

This presentation introduces a novel biosensor technology for detecting naphthenic acids (NA) in oil sands process-affected water (OSPW), offering a rapid, high-throughput, and cost-effective alternative to traditional analytical methods.

## What are Whole Cell Bacterial Biosensors?

### Technology Foundation

- **Development timeline:** Biosensor technology has been evolving since the 1990s
- **Core principle:** Engineered bacterial strains that detect specific pollutants/analytes
- **Mechanism:** Fusion of NA-inducible promoters to reporter genes (lux, gfp, lacZ)
- **Sensitivity:** Parts per million (ppm) to parts per billion (ppb) detection levels

### Key Advantages

- **Simple:** Easy to use and interpret
- **Rapid:** Real-time detection capabilities
- **Inexpensive:** Low-cost compared to mass spectrometry
- **High throughput:** Can process many samples simultaneously
- **Specific and sensitive:** Tailored to detect particular compound classes

### Patent Status

- Patent submitted in 2021
- Research published in ACS Synthetic Biology 2024 (Bookout et al.)
- Preprint available on BioRxiv

## Biosensor Design Generations

### Three-Generation Evolution

**First Generation:**

- Target promoter + dual ribosome binding sites (RBS)
- Contains both native promoter RBS and vector RBS
- Functional but suboptimal expression

**Second Generation:**

- Optimized design with vector RBS removed
- Single RBS from native promoter region
- Improved expression levels (~10x higher)

**Third Generation:**

- Complete system including transcriptional repressor
- Constitutive low-level repressor expression
- Enhanced sensitivity and specificity
- Most sophisticated design

## Three Main Biosensor Types Developed

### 1. marR-Based Biosensor

**Target compounds:** Complex and classic naphthenic acids

- **Mechanism:** Detects resistance and efflux operon induction
- **Key inducer:** Fusaric acid (antibiotic with NA-like structure)
- **Detection range:** 7-15 mg/L
- **Specificity:**
    - Strong response to fusaric acid (10-fold induction)
    - Responds to complex compounds like 5,6,7,8-tetrahydro-2-naphthoic acid
    - Detects diverse NA mixtures including OSPW extracts

### 2. 3680-Based Biosensor (Hypothetical Protein)

**Target compounds:** Classical naphthenic acids

- **Mechanism:** Linked to lipid metabolism pathway
- **Detection range:** 2-4 mg/L (most sensitive)
- **Specificity:**
    - Responds to "classic" NA like cyclopentane carboxylic acid (6-fold)
    - Strong response to cyclohexane carboxylic acid (3-fold)
    - Detects simple NA structures preferentially

### 3. atuA-Based Biosensor

**Target compounds:** Medium length and branched fatty acids

- **Mechanism:** Fatty acid degradation cluster induction
- **Detection range:** 15-30 mg/L
- **Specificity:**
    - Responds to acyclic naphthenic acids
    - Strong induction by hexanoic acid, citronellate, stearic acid
    - Does not respond to alkanes, BTEX compounds, or terpenes

## Mass Spectrometry Validation

### Commercial NA Analysis Comparison

- **Sigma Aldrich NA:** Mostly acyclic compounds (Z=0)
- **Industry NAFC:** Primarily 2-3 ring compounds (Z=-4, -6)
- Described as "mix of alkylated cyclopentane carboxylic acids"

### Detection Performance

The biosensors show excellent correlation with analytical methods:

- Dose-response curves demonstrate linear relationships
- Detection limits ranging from 1.5-30 mg/L depending on biosensor type
- Successfully validated against Orbitrap MS and LC-QTOF-MS

## Real-World Applications

### OSPW Environmental Monitoring

**Performance in actual samples:**

- **NAFC extracts (~40 mg/L):** 11/24 samples detected by at least one biosensor
- **Raw OSPW samples:** 22/24 samples detected by at least two biosensors
- **Detection pattern:** 2/3 biosensors typically respond, providing specificity information

### NA Degradation Monitoring

**High-throughput screening capability:**

- Tested OSPW-derived _Pseudomonas_ isolates for NA degradation ability
- 24-well microplate format for rapid assessment
- Cell-free supernatants tested using p3680-lux biosensor
- Successfully identified several effective NA-degrading strains

### LC-QTOF-MS Confirmation

**Validation studies:**

- Four bacterial strains grown for one week
- Confirmed as NA degraders of 3-5 compounds in 9x NA mixture
- Results analyzed by Vogon Labs (Ralph Hindle)
- **Potential application:** Bioaugmentation approach for constructed wetlands

## GROW Genomics Project Integration

### Dual-Scale Research Approach

**Greenhouse Mesocosms:**

- Recirculating horizontal surface flow
- ~95 L substrate, ~105 L surface water
- ~30 L flow/day (20 mL/min)
- Up to 24 mesocosms operating simultaneously

**Constructed Treatment Wetland System (CTWS):**

- Recirculating horizontal surface flow
- 1 hectare, 400 m³ outflow/day
- 14-day retention time
- Operational since 2013
- First tailings water flow in 2021

## Novel Detection Methods

### Agar Spot Plate Method

**Simplified field-deployable approach:**

1. Evaporate 2-4 mL sample to 25 μL (80-160 fold concentration)
2. Spread biosensor culture over agar plate
3. Spot 4 μL of concentrated water samples
4. Incubate plates overnight
5. Image luminescence rings for quantification

**Results demonstrated:**

- Clear concentration gradients visible
- Successful detection in treatment system samples
- Progressive signal loss correlating with treatment efficacy

### Treatment System Monitoring

**Greenhouse mesocosm validation:**

- Five treatment conditions tested (water only, soil only, _Carex_, _Typha_, combined)
- Orbitrap MS showed significant NA reduction (R = -0.97 to -0.99, p < 0.00)
- Biosensors successfully tracked treatment progression
- Signal loss below ~32-36 mg/L detection threshold

**Field-scale constructed wetland:**

- Monitored 1-hectare treatment system over multiple seasons
- Biosensors tracked NA degradation from ~70 mg/L to ~40 mg/L
- Different cell locations showed varying treatment efficacy
- Successful correlation with Orbitrap MS measurements

## Biosensor Specificity Profiles

### Comprehensive Compound Coverage

**patuA (atuA-based):** Medium length and branched fatty acids **pmarR (marR-based):** Complex and classic naphthenic acids  
**p3680:** Classic naphthenic acids

**Non-responsive to:**

- Alkanes
- BTEX compounds (benzene, toluene, ethylbenzene, xylene)
- Acyclic terpenes

This specificity pattern provides comprehensive coverage of NA compound classes while avoiding false positives from other hydrocarbon contaminants.

## Current Development Status

### Commercialization Efforts

**Luminous BioSolutions:**

- Website: www.luminousbiosolutions.com
- Mission: Commercialize biosensor NA testing for oil sands industry
- **Key innovation:** Developing bioaugmentation approach
- **Strategy:** Adding large-volume cultures of known NA degraders to treatment processes

### Technical Advantages

**Rapid results:** 24-hour turnaround time **Minimal sample preparation:** No extensive SPE concentration required**Qualitative assessment:** Shows NA detection and decreasing levels post-treatment **Cost-effective:** Significantly cheaper than mass spectrometry methods **High throughput:** Multiple samples processed simultaneously

### Current Limitations

**Sensitivity threshold:** Signal lost below ~32-36 mg/L on agar plates **Camera dependency:** Sensitivity limited by luminescence imaging equipment **Qualitative focus:** Quantitative biosensor testing still under development

## Future Applications

### Environmental Monitoring

- **Routine OSPW assessment:** Regular monitoring of treatment system performance
- **Regulatory compliance:** Potential tool for environmental oversight
- **Treatment optimization:** Real-time feedback for system adjustments

### Bioaugmentation Strategy

- **Enhanced remediation:** Adding proven NA-degrading bacteria to treatment systems
- **Accelerated treatment:** Reducing time required for NA removal
- **Cost reduction:** Potentially reducing overall treatment costs

### Research Applications

- **Strain screening:** Rapid identification of effective NA-degrading microorganisms
- **Treatment validation:** Quick assessment of remediation technology effectiveness
- **Ecological studies:** Understanding NA fate in natural and engineered systems

## Summary

This biosensor technology represents a significant advancement in naphthenic acid detection and monitoring. The three-biosensor panel provides comprehensive coverage of different NA compound classes with detection limits suitable for most environmental applications. The technology successfully bridges the gap between expensive, time-consuming analytical methods and the need for rapid, cost-effective environmental monitoring. With ongoing commercialization efforts and proven field validation, these biosensors offer a practical solution for the oil sands industry's NA monitoring and remediation challenges.

The integration with existing research programs (GROW Genomics) and validation against established analytical methods (Orbitrap MS, LC-QTOF-MS) demonstrates the technology's scientific rigor and practical applicability. The development of simplified detection methods (agar spot plates) further enhances the technology's potential for field deployment and routine environmental monitoring.