# Discussion Notes for Naphthenic Acids Measurement Workshop

**Date:** July 29, 2025

## Contents

- List of Participants
    
- Key Notes of Discussions
    
- 1. What are NAFCs and why do we care about them?
        
- 2. What are the methods used to measure NAFCs
        
- 3. Sample preparation – importance and key notes
        
- 4. Characterization Techniques: Mass Spec Methods vs. FTIR
        
- Key Takeaways and Next Steps
    
- Recommended literature
    
- Appendix
    
- Menti Results
    

---

## List of Participants

- **Heather Kaminsky** (NAIT Applied Research Chair for Sustainable Mining)
    
- **Andrea Sedgwick** (Government of Alberta, Water Quality)
    
- **Aprami Jaggi** (InnoTech Alberta, Research Scientist)
    
- **Daniel Palys** (Coanda)
    
- **Daniel Reslan** (Bureau Veritas, Laboratory Supervisor)
    
- **Douglas Muench** (University of Calgary, Applied Microbiologist Professor)
    
- **Jeff Violo** (Luminous BioSolutions)
    
- **Ralph Hindle** (Vogon Laboratory Services Ltd.)
    
- **Richard Frank** (ECCC)
    
- **Shawn Lewenza** (Athabasca University, Professor)
    
- **Joanne Wudrich** (Agat Labs)
    
- **Ian Vander Meulen** (ECCC, Senior Laboratory Technologist)
    
- **Chenxing (Angela) Sun** (Government of Alberta, Reclamation Policy Specialist)
    
- **Ryan Melnichuk** (InnoTech Alberta, Research Scientist)
    
- **Selamawit Messele** (NAIT, Lead Researcher)
    
- **Danuta Sztukowski** (Coanda)
    
- **Lingling Yang** (University of Alberta)
    
- **Blake Skanes** (ECCC, Physical Scientist)
    
- **Fedelina DeOliveira** (ECCC, Chemical Technologist)
    
- **Sarah Pomfret** (ECCC, IQM Quality Manager)
    
- **Mohamed Gamal El-Din** (University of Alberta, Civil and Environmental Engineering Dept, Professor)
    
- **Vicky Qualie** (NAIT, Knowledge to Practice Services Lead)
    
- **Yunhui Li** (NAIT, Technical Engagement Lead)
    
- **Simon Sun** (NAIT, Research Engineer)
    

---

## Key Notes of Discussions

### 1. What are NAFCs and why do we care about them?

**Definition:** “Naphthenic acids (NAs) are a complex class of thousands of naturally occurring aliphatic and alicyclic carboxylic acids found in oil sands bitumen and in wastewater generated from bitumen processing.” (Kovalchik et al. 2017).

**Classic NAs vs NAs in OSPW**

- **IUPAC definition (classic NAs):** chiefly monocarboxylic, derived from naphthenes. Cn​H2n+z​O2​ where n is the carbon number, Z is an even, negative integer corresponding to hydrogen deficiency due to ring formation.
    

**NAs in OSPW**

- > 50% of the compounds in the extracts of OSPW are not classic NAs (Grewer et al. 2010).
    
- Cn​H2n+z​Ox​ where x = 2 – 7 
    
- Other heteroatoms such as sulfur and nitrogen in the compounds
    
- Aromatic acids were detected in NAs extracted from OSPW.
    
- NAs common to OSPW are chemical stable and non-volatile compounds (Kavanagh et al. 2009).
    
- **Suggested definition:** oil sands tailings water acid-extractable organics (Grewer, et al. 2010)
    

### 2. What are the methods used to measure NAFCs

**A list of methods (Chen et al., 2024)** UPLC-TOF-MS; HPLC-QqQ-MS, GC-Orbitrap-MS, UPLC-TWIM-TOF-MS, GCxGC-TOF-MS, FT-ICR MS, GC-EIMS, FITR, Microchip electrophoresis, Triple quadruple MS, GC-FT-ICR MS, HPLC-Orbitrap MS

**Calibration standards used for NAFC measurement**

- Four chemicals have been used across labs: Merichem NA, Sigma-Aldrich NA mix, Acros NA (CAS 133820-45), TCL, and Fluka NA.
    
- Fluka NA was discontinued.
    
- Merichem NA were derived from refinery-based NAs, and varied by batch. It is only available through ECCC.
    
    - It is not a certified standard and its exact composition is unknown.
        
- Sigma-Aldrich NA mix is composed primarily of fatty acids, and solubility in water is a known challenge.
    
- Acros currently is used by some labs including BV.
    
- The standard chemical should be applicable to Alberta oil sands and have a reliable supply.
    

### 3. Sample preparation – importance and key notes

_(Diagram Note: 10 samples x 3 sampling events -> Sample Preparation (SPE, LLE, NoPT) -> Instrument Method -> Calibration)_

Menti results showed that sample preparation including extraction of NAs from water and preparing extract for analysis (i.e. separation method) are the most critical step to obtain a good, reliable result. 

**Solid phase extract (SPE) vs. liquid-liquid extraction (LLE)** Menti results showed that SPE was recommended compared to LLE.

|Aspect|SPE|LLE|
|---|---|---|
|**Solvent use**|Ethanol, methanol, PEG-ethanol; compatible with LC-MS and bioassays|DCM (toxic and less compatible with downstream biological testing)|
|**Repeatability**|High, especially with automated systems|Low|
|**Target compounds**|Depends on sorbent: ENV+ for aromatics and acids, C18 for non-polar organics|Broad range, but less selective; may miss polar or aromatic compounds|
|**Sample volume**|Flexible; scalable from mL to L with cartridge size|Challenging with large volumes (e.g., 10 L); labor-intensive|
|**Automation**|Possible with systems like Dionex Autotrace|Rare; mostly manual|
|**Equipment Needed**|Cartridges, vacuum manifold, pump, nitrogen evaporator, Teflon tubing|Separatory funnels, solvents, drying equipment|
|**Setup Cost**|High upfront (Autotrace ~$88K–$100K)|Low; basic glassware and solvents|
|**Learning Curve**|Moderate to high; method tuning required|Low to moderate; but labor-intensive|
|**Use Case**|Ideal for consistent, high-throughput, selective extraction|Suitable for simple, low-cost, broad-spectrum extraction|
|**Selectivity**|Sorbent-dependent; can isolate specific fractions (e.g., aliphatic acids)|Less selective; depends on solvent polarity and partitioning behavior|

Export to Sheets

**Filtration vs. centrifugation**

|Aspect|Filtration|Centrifugation|
|---|---|---|
|**Pore size / cutoff**|Defined by filter (0.2 or 0.45 µm)|Depends on RCF and time, typically removes particles down to ~0.2 µm|
|**Material impact**|Filter material can adsorb analytes||
|**Analyte loss risk**|Higher, especially for amphiphilic compounds like NAs|Lower, but NAs may still adsorb to particles in sediment|
|**Consistency**|Can vary with sample turbidity and filter choice|More consistent if RCF, time, and temperature are standardized|
|**Column protection**|Effective if properly filtered|Proven effective|
|**Best use case**|When defining dissolved fraction or removing emulsions|When minimizing analytes loss and ensuring reproducibility|

Export to Sheets

### 4. Characterization Techniques: Mass Spec Methods vs. FTIR

|Aspect|Mass Spec|FTIR|
|---|---|---|
|**resolution**|High resolution (e.g., Orbitrap, QTOF) enables detailed profiling but not exact structures|Measures all C=O bonds; less specific, more general signal, less directly correlated to toxicity|
|**data richness**|Extremely data-rich; supports retrospective analysis|Simpler output; less data complexity|
|**sample prep sensitivity**|Highly sensitive to extraction method and instrument conditions|Also sensitive, but ostensibly less affected by minor prep variations (note: this may be not true due to NAIT unpublished study)|
|**routine monitoring suitability**|Not ideal for routine use due to cost and complexity|More feasible for routine screening|
|**standardization challenges**|Difficult due to instrument variability and response factors|Easier to standardize, but still affected by sample composition|
|**detection limits**|Labs claims low limits (e.g., 0.2 µg/L, but often report “<0.2” due to visibility issues|Moderate limits; less prone to overstatement|
|**response factor variability**|Varies with compound structure, ion source (ESI vs APCI), and mobile phase conditions|Measures functional groups; less affected by individual compound variability|
|**inter-lab consistency**|Poor without standardization; same extract yields different results across labs|Better consistency if sample prep is controlled|
|**use case**|Best for research, problem investigation, and retrospective analysis|Best for routine monitoring and performance-based testing|
|**cost and accessibility**|Expensive; requires specialized equipment and expertise|Lower cost; widely available in environmental labs|
|**correlation across methods**|Orbitrap and FTIR can correlate if sample prep is consistent|FTIR results vary with sample composition; not always comparable|
|**avoiding derivatization**|GC-MS not recommended due to need for derivatization||

Export to Sheets

---

## Key Takeaways and Next Steps

- **Scalability is essential :** with thousands of samples processed annually, we need a method that is scalable for high-throughput screening, followed by more complex analysis on selected subsets.
    
- Need to focus next discussion on the high throughput screening methods and review what data is available on how these methods trend with the high-resolution data.
    
- **Standardization is challenging but necessary :** a universal method may not be perfect, but consistency across labs is critical to ensure reliable comparisons and trend detection.
    
- First step is to obtain standard samples and calibration compounds that can be used to validate methods.
    
- Ideally this is an extract that is derived from oil sands water that can be used going forward.
    
- Is there a lab capable of creating such an extract?
    
- **Accuracy and error margins matter :** especially for long-term planning and closure strategies, acceptable levels of precision must be clearly defined and validated.
    
- Ideally ECCC/Government publish the data used/methodologies used in defining these acceptable precision levels.
    
- **Tiered monitoring approach :** routine monitoring should rely on simple, fast methods to detect changes.
    
- When anomalies are observed, more advanced techniques should be applied to investigate further.
    
- **Consistency across operators and labs :** Measurement trends must remain reliable regardless of who performs the analysis or where it is conducted.
    
- Current inconsistencies hinder validation and trust.
    
- Next discussions should highlight how to ensure consistent data between labs or some form of standard for comparison to build trust.
    
- **Research needs high resolution data:** FTIR data is not sufficiently detailed to be able to help understand mechanisms of toxicity or whether water treatment is effective at this stage.
    
- High resolution mass spec data is required for industrial samples over time to establish relevant baselines and enable understanding of mechanism.
    
- Recommend that industry perform Orbitrap or Q-TOF analysis on a select baseline subset of river water and pond/tailings streams to complement high throughput screening.
    
- Water treatment tests should confirm potential “best performers” with high resolution data.
    

---

## Recommended literature

- **Joanne L. Parrott, Danna M. Schock, Ian J. Vander Meulen, Lukas Mundy, Bruce Pauli, Kerry Peru, John V. Headley.** Disrupted development in fathead minnow embryos exposed to wetland waters from the Athabasca Oil Sands Region, Alberta, Canada. _Science of The Total Environment, Volume 957, 20 December 2024, 177407._[https://doi.org/10.1016/j.scitotenv.2024.177407](https://doi.org/10.1016/j.scitotenv.2024.177407)
    
- **Anthony E. Bauer, L. Mark Hewitt, James W. Roy, Joanne L. Parrott, Adrienne J. Bartlett, Patricia L. Gillis, Warren P. Norwood, Martina D. Rudy, Sheena D. Campbell, Maegan R. Rodrigues, Lisa R. Brown, Ruth Vanderveen, Lorna E. Deeth, Emily A.M. Holman, Joseph Salerno, Julie R. Marentette, Christine Lavalle, Cheryl Sullivan, Kallie Shires, Melissa Galicia, Julian Rubino, Mitra Brown, Alicia O'Neill, Greg Bickerton, D. George Dixon, Richard A. Frank.** The acute toxicity of bitumen-influenced groundwaters from the oil sands region to aquatic organisms. _Science of The Total Environment, Volume 848, 20 November 2022, 157676._[https://doi.org/10.1016/j.scitotenv.2022.157676](https://doi.org/10.1016/j.scitotenv.2022.157676)
    
- **Rongfu Huang, Kerry N. McPhedran, Nian Sun, Pamela Chelme-Ayala, Mohamed Gamal El-Din.**Investigation of the impact of organic solvent type and solution pH on the extraction efficiency of naphthenic acids from oil sands process-affected water. _Chemosphere, Volume 146, March 2016, Pages 472-477._[https://doi.org/10.1016/j.chemosphere.2015.12.054](https://doi.org/10.1016/j.chemosphere.2015.12.054)
    
- **John V. Headley, Kerry M. Peru, Mark P. Barrow, Peter J. Derrick.** Characterization of Naphthenic Acids from Athabasca Oil Sands Using Electrospray Ionization: The Significant Influence of Solvents. _Analytical Chemistry, 2007, 79, 16, 6222–6229._ [https://doi.org/10.1021/ac070905w](https://doi.org/10.1021/ac070905w)
    
- **Anthony E. Bauer, R.A. Frank, J.V. Headley, C.B. Milestone, S. Batchelor, K.M. Peru, M.D. Rudy, S.E. Barrett, R. Vanderveen, D.G. Dixon, L.M. Hewitt.** A preparative method for the isolation and fractionation of dissolved organic acids from bitumen-influenced waters. _Science of The Total Environment, Volume 671, 25 June 2019, Pages 587-597._ [https://doi.org/10.1016/j.scitotenv.2019.03.244](https://doi.org/10.1016/j.scitotenv.2019.03.244)
    
- **Rui Qin, Dustin Lillico, Zuo Tong How, Rongfu Huang, Miodrag Belosevic, James Stafford, Mohamed Gamal El-Din.** Separation of oil sands process water organics and inorganics and examination of their acute toxicity using standard in-vitro bioassays. _Science of The Total Environment, Volume 695, 10 December 2019, 133532._ [https://doi.org/10.1016/j.scitotenv.2019.07.338](https://doi.org/10.1016/j.scitotenv.2019.07.338).
    
- **Kyle D. Duncan, Larissa C. Richards, Joseph Monaghan, Monique C. Simair, Chukwuemeka Ajaero, Kerry M. Peru, Vanessa Friesen, Dena W. McMartin, John V. Headley, Chris G. Gill, Erik T. Krogh.** Direct analysis of naphthenic acids in constructed wetland samples by condensed phase membrane introduction mass spectrometry. _Science of The Total Environment. Volume 716, 10 May 2020, 137063._[https://doi.org/10.1016/j.scitotenv.2020.137063](https://doi.org/10.1016/j.scitotenv.2020.137063)
    
- **Remy Gavard, Hugh Jones, Diana Catalina Palacio Lozano, Mary J. Thomas, David Rossell, Simon E. F. Spencer, Mark P. Barrow.** KairosMS: A New Solution for the Processing of Hyphenated Ultrahigh Resolution Mass Spectrometry Data. _Anal. Chem. 2020, 92, 5, 3775–3786._ [https://doi.org/10.1021/acs.analchem.9b05113](https://doi.org/10.1021/acs.analchem.9b05113)
    
- **Ralph Hindle, John Headley and Douglas G. Muench.** Pros and Cons of Separation, Fractionation and Cleanup for Enhancement of the Quantitative Analysis of Bitumen-Derived Organics in Process-Affected Waters—A Review. _Separations 2023, 10(12), 583._ [https://doi.org/10.3390/separations10120583](https://doi.org/10.3390/separations10120583)
    

---

## Appendix

### Menti Results

**What are you hoping to get out of this workshop?**

- learn the pros and cons for various techniques
    
- Would like to get ideas about state of the art for NAs
    
- Current state of the field as we pivot our analysis from qualitative to quantitative.
    
- A path forward; there is a great deal of uncertainty right now, but enough knowledge around the subject that there is a feasible pather forward.
    
- Understand the NA testing landscape, the value of each option and validate Biosensor as a consideration.
    
- Find out who is doing NA analysis and get best practices
    
- Information regarding the most recent state of naphthenic acid analysis and current challenges being faced in NA analysis.
    
- Education on various techniques. Pro's/Con's. Rapid methods available for real-time analysis?
    
- To proselytize on the value of high-res mass spec
    
- Insights on breadth of ms approaches and extraction procedures for nafc
    

**In your opinion which of the following groupings is important to measure for routine monitoring of river/released water?**

- Classic Naphthenic acids (15 votes)
    
- Acid extractable organics (NAFCs) (13 votes)
    
- Dissolved organic matter (6 votes)
    
- Natural organic matter (1 vote)
    
- Humic & Fulvic Acids (1 vote)
    

**In your opinion, how important is it to quantify the following groups of NAFCs?**

- Classical NAFCs (O2 only) (Score: 4.4)
    
- NAs containing more Oxygen (Score: 3.8)
    
- NAs containing Heteroatoms (Score: 3.7)
    

**In your opinion, how important is it to quantify the following groups of NAFCs for the purpose of routine monitoring?**

- All the above (Score: 4.2)
    
- Classical NAFCs (O2 only) (Score: 4.1)
    
- NAs containing Heteroatoms (Score: 2.9)
    
- NAs containing more Oxygen (Score: 2.4)
    

**Rate how critical each stage of the method is to a good, reliable result in your opinion:**

- Extraction of NAs from Water (Score: 5.0)
    
- Preparing extract for analysis (i.e. separation method) (Score: 4.4)
    
- Analysis of the result (Score: 3.7)
    
- Detection/ running the detector and collecting the spectra (Score: 3.5)
    

**Which NA instrument detector(s) are you most familiar with?**

- Orbitrap (11 votes)
    
- FTIR (8 votes)
    
- QToF (6 votes)
    
- GC-MS (5 votes)
    
- Biosensors (3 votes)
    
- FT-ICR (2 votes)
    
- Other (0 votes)
    

**For liquid -liquid extraction which solvent would you recommend?**

- DCM (9 votes)
    
- I don't know/no opinion (5 votes)
    
- n-hexane (1 vote)
    
- ethyl ether (1 vote)
    
- Other (1 vote)
    
- n-pentane (0 votes)
    

**For solid phase extraction which cartridge would you recommend?**

- I don't know/no opinion (8 votes)
    
- Env+ (5 votes)
    
- MAX (2 votes)
    
- HLB (1 vote)
    
- Other (0 votes)
    

**Which extraction method would you recommend?**

- Solid Phase (6 votes)
    
- I don't have an opinion (6 votes)
    
- Nothing (2 votes)
    
- Liquid-Liquid (1 vote)
    
- Solid Phase Microextraction (0 votes)
    

**What reference materials/standards do you use?**

- Merichem
    
- Sigma Aldrich CAS # 1338-24-5
    
- Sigma NA mix
    
- NAFC from the Headley lab, SPE extract. I wouldn't use a Sigma Aldrich or Acros as standard, they are mostly fatty acids from what I read in the literature.
    
- Merichem, Sigma, Fisher, Fluka (discontinued), TCL. I ran calibration curves on each for FTIR and they are all different
    
- An OSPW-derived NAFC extract (800 L --> 1 L extracted by LLE) previously standardized against Merichem via FTIR
    
- Acros
    
- Internal standard (myristic acid-1-13C) for semi-quantification of NAs by QTOFMS.
    
- I like the "OSPW-derived..." approach
    
- Sigma
    
- we have compared Fluka and Acros as...
    
- CAS 1338-24-5
    

**Rate the level of expertise required for the data analysis from each of the following techniques:**

- FT-ICR (Score: 4.4)
    
- Orbitrap (Score: 4.3)
    
- QToF (Score: 4.2)
    
- GC-MS (Score: 3.2)
    
- FTIR (Score: 2.3)
    
- Biosensors (Score: 1.8)
    
- Other (Score: 1.0)
    

**Rate the level of expertise required to run the instrument from each of the following techniques:**

- FT-ICR (Score: 3.8)
    
- Orbitrap (Score: 3.2)
    
- GC-MS (Score: 3.2)
    
- QToF (Score: 3.1)
    
- Biosensors (Score: 2.0)
    
- FTIR (Score: 1.9)
    
- Other (Score: 1.3)
    

**Rate the level of expertise required to prepare the samples for each of the following techniques:**

- GC-MS (Score: 2.3)
    
- FT-ICR (Score: 2.3)
    
- Biosensors (Score: 2.0)
    
- QToF (Score: 2.0)
    
- Orbitrap (Score: 1.9)
    
- FTIR (Score: 1.8)
    
- Other (Score: 1.0)
    

**Rate the repeatability of the measurement for the following techniques:**

- QToF (Score: 3.6)
    
- No opinion/don't know (Score: 3.0)
    
- Orbitrap (Score: 3.0)
    
- FTIR (Score: 2.8)
    
- GC-MS (Score: 2.6)
    
- FT-ICR (Score: 2.3)
    
- Biosensors (Score: 1.8)
    
- Other (Score: 1.4)
    

**What you think the detection limits are for each detector**

- Orbitrap (Score: 3.2)
    
- QToF (Score: 3.2)
    
- FT-ICR (Score: 2.6)
    
- GC-MS (Score: 2.0)
    
- FTIR (Score: 1.9)
    
- No opinion/I don't know (Score: 1.8)
    
- Biosensors (Score: 1.7)
    
- Other (Score: 1.0)
    

---

**AI Context Links:** [[Naphthenic Acids]] [[Oil Sands Process-Affected Water]] [[Solid Phase Extraction]] [[Liquid-Liquid Extraction]] [[Mass Spectrometry]] [[FTIR Spectroscopy]] [[Biosensors]] [[Analytical Chemistry]]