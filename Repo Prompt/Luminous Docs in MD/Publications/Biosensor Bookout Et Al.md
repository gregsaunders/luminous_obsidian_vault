# Construction of Whole Cell Bacterial Biosensors as an Alternative Environmental Monitoring Technology to Detect Naphthenic Acids in Oil Sands Process-Affected Water

**Authors:** Tyson Bookout, Steve Shideler, Evan Cooper, Kira Goff, John V. Headley, Lisa M. Gieg, and Shawn Lewenza*

**Citation:** https://doi.org/10.1021/acssynbio.4c00260

**Journal:** ACS Synthetic Biology

---

## Abstract

After extraction of bitumen from oil sands deposits, the oil sand process-affected water (OSPW) is stored in tailings ponds. Naphthenic acids (NA) in tailings ponds have been identified as the primary contributor to toxicity to aquatic life. As an alternative to other analytical methods, here we identify bacterial genes induced after growth in naphthenic acids and use synthetic biology approaches to construct a panel of candidate biosensors for NA detection in water.

The main promoters of interest were:

- The **atuAR promoters** from a naphthenic acid degradation operon and upstream TetR regulator
- The **marR operon** which includes a MarR regulator and downstream naphthenic acid resistance genes
- A **hypothetical gene** with a possible role in fatty acid biology

Promoters were printed and cloned as transcriptional lux reporter plasmids that were introduced into a tailings pond-derived _Pseudomonas_ species. All candidate biosensor strains were tested for transcriptional responses to naphthenic acid mixtures and individual compounds. The three priority promoters respond in a dose-dependent manner to simple, acyclic, and complex NA mixtures, and each promoter has unique NA specificities.

**Key Results:**

- Limits of NA detection from the various NA mixtures ranged between **1.5 and 15 mg/L**
- The atuA and marR promoters also detected NA in small volumes of OSPW samples and were induced by extracts of the panel of OSPW samples

While biosensors have been constructed for other hydrocarbons, here we describe a biosensor approach that could be employed in environmental monitoring of naphthenic acids in oil sands mining wastewater.

**Keywords:** bacterial biosensor, gene expression, naphthenic acids, tailings pond, oil sands mining, environmental monitoring

---

## Introduction

### Oil Sands Background

The Athabasca oil sands in northern Alberta represent one of the world's largest sources of recoverable bitumen. Bitumen is a heavily biodegraded crude oil recovered from surface mining the oil sands through the Clark process, or alkaline hot water extraction. After separation of the oil from the extraction water, the resulting oil sands process-affected water (OSPW) is deposited and stored in tailings ponds where solids can settle, and the water can be recycled for repeat extractions.

The OSPW contains many compounds including:

- Sand, silt, and clay
- Dissolved ions
- Heavy metals
- Unrecovered oil
- Numerous acid-extractable organic (AEO) compounds like naphthenic acids

### Naphthenic Acids (NA)

Naphthenic acids are naturally produced during the degradation of petroleum and are present in the oil sands ore used to produce bitumen. They are classically defined by the formula **CnH2n-zO2**, where:

- n = number of carbons
- Z = number of hydrogens lost due to ring formation

NA comprise a complex mixture of:

- Monocyclic carboxylic acids
- Polycyclic carboxylic acids
- Acyclic alkyl-substituted carboxylic acids

**Concentration ranges:**

- Low end (5-30 mg/L): In-line with Athabasca wetlands
- Midrange (50-120 mg/L): In-line with OSPW and industrially affected experimental wetlands

**Environmental Impact:**

- NA have been identified as the main contributor to OSPW toxicity
- Demonstrated toxicity in microbes, plants, fish, amphibians, birds and mammals
- Some naphthenic acid compounds are difficult for bacteria to degrade, particularly high molecular weight compounds containing multiringed structures and branched carboxylic acids

### Current Analytical Methods

Standard practice is to store OSPW in large tailings ponds, resulting in the accumulation of over **1 billion m³** of OSPW. Current analytical methods for monitoring and quantifying NA include:

**Conventional screening techniques:**

- Gas Chromatography-Mass Spectrometry (GC-MS)
- Fourier Transform Infrared Spectroscopy (FTIR)

**High resolution mass spectrometry:**

- Fourier transform Ion cyclotron resonance
- Orbitrap analysis with Negative Ion Electrospray Ionization-Mass Spectrometry (ESI-MS)
- With or without online High-Performance Liquid Chromatography (HPLC)

**Limitations:**

- Semi-quantitative with relatively low limits of detection (as low as 0.01 mg/L with ESI-MS)
- Require multiple sample processing steps
- Include organic solvent extraction of OSPW, which may bias analysis
- Can be time-consuming and costly

### Whole Cell Biosensors

Whole cell biosensors are engineered bacterial strains capable of detecting and quantifying various compounds and analytes by producing a simple optical or electrochemical output proportional to the analyte of interest. This technology:

- Utilizes refined metabolite sensing mechanisms of bacterial cells
- Provides a useful tool for environmental monitoring
- Is specific and capable of detecting low levels of small molecules
- Has sensitivity commonly in the parts per million range (mg/L)
- Has been used for detecting aromatic compounds, alkanes, alkenes, heavy metals, and antibiotics

---

## Methods

### Library Construction and RNA-Seq Analysis

**Organism:** _Pseudomonas_ sp. OST1909 (derived from a tailings pond)

**Growth conditions:**

- Grown to mid log phase (~25°C) in TB medium with 2% DMSO
- Exposed for 3 h to 150 mg/L of different NA mixtures:
    - Acyclic naphthenic acids (Sigma-Aldrich 70340)
    - Custom mix of 9X naphthenic acids
    - Acid extracted organics (NAFC) from OSPW

**RNA-seq procedure:**

- Total bacterial RNA isolated using Qiagen RNeasy kit
- DNase treatment and ribosomal depletion
- cDNA synthesis and sequencing library preparation
- SOLiD 5500xl DNA sequencer for 75 bp sequencing
- ~270 million reads total

### Biosensor Construction

**Three generations of biosensor designs:**

1. **First-generation:** Target promoter + vector RBS + luxCDABE
2. **Second-generation:** Target promoter (vector RBS removed) + luxCDABE
3. **Third-generation:** Constitutive promoter + regulator gene + target promoter + luxCDABE

**Key promoters targeted:**

- **atuA/atuR:** From naphthenic acid degradation operon
- **marR:** From antimicrobial resistance operon
- **3680:** Hypothetical gene with potential fatty acid biology role

### High-Throughput Screening

**Assay conditions:**

- 96-well clear bottom plates
- M9 or BM2 minimal defined media with 20 mM succinate
- 2% DMSO to increase NA solubility
- 15-hour protocol with measurements every 20 minutes
- Gene expression measured as counts per second (CPS) normalized by OD600

**Fold Gene Expression calculation:**

- CPS/OD600 (treated) ÷ CPS/OD600 (control)
- Fold change of 1 = no change
- Fold change of 2 = doubling of expression

---

## Results and Discussion

### Transcriptome Analysis

RNA-seq revealed significantly upregulated genes under experimental conditions:

- **OSPW:** p < 0.05 = 56 genes; q < 0.05 = 0 genes
- **Acyclic NA:** p < 0.05 = 140 genes; q < 0.05 = 18 genes
- **9xNA:** p < 0.05 = 110 genes; q < 0.05 = 14 genes

**Key findings:**

- Genes involved in fatty acid degradation (β-oxidation)
- Metabolite sensing transcriptional regulators
- Transport and efflux systems
- Stress response pathways

### The atuA and atuR Promoters

**Background:**

- Homologous to _Pseudomonas aeruginosa_ acyclic terpene utilization (atu) operon
- Encodes genes for degrading terpenes and carboxylic acids through β-oxidation
- Regulated by AtuR, a TetR-type transcriptional repressor

**Key characteristics:**

- **atuA promoter:** Faster response (5-7 h), higher fold changes (~8-fold in first-generation)
- **atuR promoter:** Slower response (15 h), lower fold changes (~4-fold)
- **Specificity:** Primarily responds to acyclic naphthenic acids
- **Detection limit:** 15 mg/L for atuA, 125 mg/L for atuR

**Specificity profile:**

- Strong response to acyclic NA mixtures (Sigma-Aldrich, Acros)
- Individual compounds: hexanoic acid (2-fold), citronellate (3-fold), pentadecanoic acid (2.5-fold), stearic acid (~2.8-fold)
- No response to ringed naphthenic acids, alkanes, or BTEX compounds

### The marR Promoter

**Background:**

- Encodes MarR family regulator controlling antimicrobial resistance genes
- Associated with fusaric acid transport, efflux and resistance
- Fusaric acid is an antibiotic with naphthenic acid-like structure

**Key characteristics:**

- **Response:** Strong induction by fusaric acid (~20-fold in first-generation)
- **Detection range:** Responds to NAFC at concentrations as low as 16 mg/L
- **Specificity:** Detects diverse and complex NA mixtures

**Specificity profile:**

- **Strongest inducer:** Fusaric acid (10-fold)
- **Complex NAs:** 5,6,7,8-tetrahydro-2-naphthoic acid (3-fold), 3-phenylpropionic acid (3-fold)
- **Cyclic NAs:** Cyclohexyl succinic acid (2.5-fold), cyclohexane acetic acid (2.5-fold)
- **Acyclic NAs:** Citronellate, decanoic acid, pentadecanoic acid

### The Hypothetical 3680 Promoter

**Background:**

- Upregulated by custom NA mixture
- Contains three n-myristoylation sites
- Adjacent to TetR regulator homologous to fatty acid desaturation control

**Key characteristics:**

- **Detection limit:** As low as 1.5 mg/L for 9xNA mixture
- **Specificity:** Primarily responds to simple "classic" NA compounds
- **Response:** Fast and strong linear dose-dependent response

**Specificity profile:**

- **Classic NAs:** Cyclopentane carboxylic acid (6-fold), cyclohexane carboxylic acid (3-fold)
- **Simple compounds:** Phenylpropionic acid (3-fold), hexanoic acid (3-fold)
- **Limited response** to OSPW extracts or acyclic NA

### Dose Response and Detection Limits

|Biosensor|Target Mixture|Detection Limit|Linear Range|
|---|---|---|---|
|atuA-L|Acyclic NA|15 mg/L|7.8-125 mg/L|
|atuR-L|Acyclic NA|125 mg/L|62.5-500 mg/L|
|marR-L|NAFC|16 mg/L|16-512 mg/L|
|p3680²|9xNA mix|1.5 mg/L|1.5-100 mg/L|

### OSPW Sample Testing

**NAFC Extracts (concentrated, ~40 mg/L):**

- 11/24 samples induced significant response from at least one biosensor
- Each biosensor responded to specific NA compound profiles
- marR-L detected complex multiringed compounds
- atuA-L detected acyclic NA compounds

**Raw OSPW Samples (minimal dilution):**

- 22/24 samples induced significant response from at least two biosensors
- marR-L and atuA-L displayed high fold expression (4-12 fold) for most samples
- p3680-lux did not respond to any water sample
- Minimal sample preparation required

---

## Conclusions

This study successfully developed a panel of whole cell bacterial biosensors for detecting naphthenic acids in oil sands process-affected water. Key achievements include:

### Technical Accomplishments

1. **Environmentally relevant chassis:** Used _Pseudomonas_ sp. OST1909 isolated from tailings ponds
2. **Comprehensive approach:** Performed transcriptome analysis with diverse NA mixtures
3. **Synthetic biology platform:** Used automated DNA synthesis and assembly for large-scale biosensor construction
4. **Thorough characterization:** Multiple rounds of biosensor optimization and testing

### Biosensor Performance

**Sensitivity:**

- Detection limits ranging from 1.5-125 mg/L depending on biosensor and NA mixture
- Dose-dependent responses suitable for semi-quantitative analysis

**Specificity:**

- Each promoter demonstrates unique NA specificity profiles
- atuA: Acyclic naphthenic acids
- marR: Complex and antimicrobial-like NAs
- 3680: Simple "classic" naphthenic acids

**Real-world application:**

- Successfully detected NA in 22/24 raw OSPW samples with minimal preparation
- Rapid detection (minutes to hours) compared to conventional analytical methods

### Advantages Over Current Methods

1. **Cost-effective:** Lower cost than mass spectrometry methods
2. **Rapid:** Real-time detection without extensive sample preparation
3. **Minimal sample prep:** Can test small volumes of raw water samples
4. **Field-deployable potential:** Whole-cell biosensors suitable for on-site monitoring
5. **Semi-quantitative:** Dose-response curves allow concentration estimation

### Future Applications

The NA biosensors show great potential as:

- **Environmental monitoring tools** for tailings pond management
- **Rapid screening methods** for OSPW treatment efficacy
- **Early warning systems** for environmental contamination
- **Research tools** for studying NA biodegradation and fate

This biosensor approach provides a valuable complement to existing analytical methods for naphthenic acid detection and could be particularly useful for routine monitoring applications where rapid, cost-effective detection is prioritized over the highest analytical precision.

---

## Supporting Information

Additional details including:

- Stock concentrations of NA compounds and mixtures
- Concentrations of NA in water and extracts
- DNA sequences of synthetic promoters
- Differential gene expression analysis
- Complete experimental protocols

Available at: https://pubs.acs.org/doi/10.1021/acssynbio.4c00260