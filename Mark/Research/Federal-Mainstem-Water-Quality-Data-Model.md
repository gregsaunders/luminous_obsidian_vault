# Federal Mainstem Water Quality Data Model Research

**Date:** 2026-01-21
**Data Source:** Environment Canada Long-Term Water Quality Monitoring (LTWQM)
**Location:** `/mnt/c/Users/mdrob/ObsidianJournals/Luminous/Square Head Data/Government/Mainstem Water Quality - Oil Sands Region`

---

## Executive Summary

This document captures data modeling requirements derived from analyzing Environment Canada's Long-Term Water Quality Monitoring dataset from the Oil Sands Region. This federal dataset complements the provincial Surface Water Quality data, providing specialized monitoring focused on the mainstem Athabasca River and its major tributaries.

**Key characteristics:**
- 5 CSV files organized by analytical category (not by program/year like provincial data)
- 600+ measurement parameters including specialized organics and trace metals
- ~1,650 sampling events spanning 2011-2025
- Wide-format data (600+ columns) requiring EAV transformation
- Sophisticated quality control system with dual-tier detection limits (MDL/RL)
- Multiple analytical methods for metals requiring careful data segregation

---

## Data Domain Overview

### What This Data Represents

Federal mainstem water quality monitoring involves:
1. **Focused geographic scope** - M2-M7 mainstem monitoring points along the Lower Athabasca River
2. **Specialized analytics** - Mercury, trace metals, PAHs, and alkylated organics not typically in provincial programs
3. **Dual analytical methods** - Two different ICP-MS methods for metals (Metals52 vs Metals56)
4. **Rigorous QC** - Multi-tier detection limits and extensive qualifier codes

### Hierarchical Structure

```
Monitoring Project (Long-Term Water Quality Monitoring)
  └── Station (M2-M7 mainstem points + tributaries)
      └── Sample Event (field visit with collection metadata)
          └── Measurements (600+ parameters per sample)
              ├── Parameter (VMV code identifier)
              ├── Analytical Method (Metals52, Metals56, etc.)
              ├── Value + Unit + Detection Limits
              └── Quality Flags (L, R, Q + QA codes)
```

### Key Difference from Provincial Data

| Aspect | Provincial (Surface WQ) | Federal (Mainstem LTWQM) |
|--------|------------------------|--------------------------|
| Organization | By program + year (71 files) | By analytical category (5 files) |
| Parameters | ~100 common parameters | 600+ specialized parameters |
| Format | Narrow (40 columns) | Wide (600+ columns) |
| Detection Limits | Single RDL | Dual MDL + RL |
| Methods | Various | Specific ICP-MS variants |
| Geographic Focus | 230 stations across Alberta | ~10 mainstem stations |

---

## Source Data Analysis

### File Organization

```
Mainstem Water Quality - Oil Sands Region/
├── MainstemWaterQuality-LTWQM-M2-M7-Mercury-2011-2025.V2.csv      (0.27 MB)
├── MainstemWaterQuality-LTWQM-M2-M7-Metals52-2011-2025.v2.csv    (0.75 MB)
├── MainstemWaterQuality-LTWQM-M2-M7-Metals56-2011-2025.V2.csv    (1.11 MB)
├── MainstemWaterQuality-LTWQM-M2-M7-Nutrients-2011-2025.v2.csv   (0.65 MB)
├── MainstemWaterQuality-LTWQM-M2-M7-Organics&Others-2011-2025.V2.csv (1.46 MB)
├── OSM-Schemas-Variable-Names-VMV-Detection-Limits-June2019.csv  (reference)
└── SurfaceWaterQualityNotes-English-June2019.pdf                  (documentation)
```

### CSV Structure (Unique Format)

Unlike standard CSVs, these files have a complex header structure:

```
Rows 1-3:     File metadata (generation date, context notes)
Rows 4-91:    Extended documentation and parameter descriptions
Row 92:       Actual column headers (this is the schema row)
Rows 93+:     Data records
```

**Implication:** CSV parsers must skip the first 91 rows to reach the actual data schema.

### Source Schema (Common Columns)

| Category | Fields |
|----------|--------|
| **Sample Identity** | Field Sample Number |
| **Project** | Project Name |
| **Location** | Station or Location Name, Station Number/Code, Latitude, Longitude |
| **Timing** | Sample Date/DateTime |
| **Sample Type** | Matrix, Sample Type, Water Depth (m) |
| **Measurements** | 600+ parameter columns (value + flag pairs) |

### Measurement Column Pattern

Each parameter has two adjacent columns:
```
[Parameter Name / Nom du paramètre] | [Flag / Marqueur]
              40.7                  |        L
```

- **Value column**: Numeric value OR non-numeric code (DE, IS, FC, etc.)
- **Flag column**: Quality indicator (L, R, Q, or blank)

---

## Entity Definitions

### 1. Station

**Purpose:** Fixed monitoring location along the mainstem river system.

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| station_code | string | Government code (unique) | AL07DD0004 |
| station_name | string | Short descriptive name | M4 LT WQ PANEL 1 OF 10 |
| latitude | float | WGS84 decimal degrees | 57.12622222 |
| longitude | float | WGS84 decimal degrees | -111.6040278 |
| station_type | enum | Category | mainstem, tributary, reference |
| river_system | string | Water body | Athabasca River |
| drainage_region | string | Region | Oil Sands Region |

**Station Naming Convention:**
- M0-M7: Mainstem monitoring points (upstream to downstream)
- Tributaries: Named by creek/river
- Panel notation: "PANEL X OF 10" indicates multi-point transect sampling

**Cardinality:** ~10 unique station codes, ~67 site name variations

### 2. Parameter (VMV Code)

**Purpose:** Definition of what is being measured, identified by Variable-Method-Version code.

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| vmv_code | string | Unique identifier | MERC_T_001 |
| parameter_name | string | Human name | Mercury Total |
| category | enum | High-level group | mercury, metals, nutrients, organics |
| parameter_type | enum | Measurement type | concentration, ratio, count |
| unit_of_measure | string | Standard unit | ng/L, ug/L, mg/L |
| typical_mdl | float? | Method Detection Limit | 0.035 |
| typical_rl | float? | Reporting Limit | 0.07 |
| chemical_group | string? | Chemical family | PAH, Alkylated PAH, Heavy Metal |
| analyte_fraction | string? | Fraction analyzed | dissolved, total, particulate |

**Parameter Categories Found:**

| Category | Count | Examples |
|----------|-------|----------|
| Mercury | 6 | Total Mercury, Methyl Mercury |
| Metals (52-element) | 71 | Al, Sb, As, Ba, Be, Bi, Cd, Co, Cr, Cu, Fe... |
| Metals (56-element) | 107 | Above + rare earth elements (Eu, Gd, Hf, Ho...) |
| Nutrients | 21 | Ammonia, Nitrate, Phosphorus, Carbon, TSS |
| BTEX | 4 | Benzene, Toluene, Ethylbenzene, Xylenes |
| PAHs | ~50 | Naphthalene, Pyrene, Chrysene, Benzo(a)pyrene |
| Alkylated PAHs | ~100 | C1-C4 naphthalenes, fluorenes, phenanthrenes |
| Other Organics | ~200 | Phenols, Cyanide, Petroleum hydrocarbons |

**Cardinality:** 600+ unique parameters

### 3. Analytical Method

**Purpose:** Laboratory technique used for analysis - critical for data comparability.

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| method_code | string | Method identifier | Metals52, Metals56 |
| method_name | string | Full name | In-Bottle Digestion ICP-MS |
| standard_reference | string? | EPA/ISO method | EPA 200.8 |
| description | string? | Method details | |

**Critical Methods:**

| Method | Name | Parameters | Key Distinction |
|--------|------|------------|-----------------|
| Metals52 | In-Bottle Digestion ICP-MS | 71 elements | Historical standard, pre-2011 compatible |
| Metals56 | Modified EPA 200.8 ICP-MS | 107 elements | More aggressive digestion, includes REEs |
| Mercury | Cold Vapor AAS/AFS | 6 | Specialized mercury analysis |

**Data Comparability Warning:** Metals52 and Metals56 results are NOT directly comparable for trend analysis due to different digestion methods affecting particulate-bound metal recovery.

**Cardinality:** ~5-10 methods

### 4. Quality Flag

**Purpose:** Data quality indicators explaining measurement reliability.

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| flag_code | string | Short code | L, R, Q |
| flag_name | string | Human name | Below MDL |
| category | enum | Flag type | detection_limit, quality_control, missing_data |
| description | string | Full explanation | |
| numeric_treatment | string? | How to handle in stats | substitute_half_mdl, exclude |

**Detection Limit Flags (Table B):**

| Flag | Meaning | Interpretation |
|------|---------|----------------|
| L | Below Method Detection Limit | Value detected but < MDL; use with caution |
| R | Below Reporting Limit | MDL ≤ value < RL; higher uncertainty |
| Q | Questionable | See QA code suffix for specific issue |

**QA/QC Codes (appended to Q flag):**

| Code | Category | Description |
|------|----------|-------------|
| Sum | Data Quality | Filtered > unfiltered (physically impossible) |
| EventL | Contamination | Lab contamination suspected |
| EventF | Contamination | Field contamination suspected |
| RangeL | Range | Value improbably low |
| RangeH | Range | Value improbably high |
| Ion | Chemistry | Ion balance check failed |
| Blank | Contamination | Blank contamination impact |
| Rep | Precision | Replicate disagreement |
| SpikeL/SpikeF | Recovery | Lab/field spike recovery issue |
| SurL/SurH | Recovery | Surrogate recovery issue |
| Noise | Instrument | Noisy baseline |
| Error | Various | Miscellaneous reasons |

**Non-Numeric Value Codes (Table C):**

| Code | Meaning |
|------|---------|
| DE | Sample depleted |
| IS | Insufficient sample volume |
| FC | Field contamination |
| LC | Lab contamination |
| SI | Suspected interference |
| NR | Not received |
| BR | Broken in transit |
| DS | Destroyed in lab |
| NV | No value recorded |
| TNTC | Too numerous to count |
| DV | Value deleted |
| TC | Test cancelled |
| NA | Not applicable |
| NC | Not calculatable |
| PM | Prerequisite missing |

**Cardinality:** ~20 flag/code combinations

### 5. Sample Event

**Purpose:** A single sampling visit - collection of water at a specific location/time.

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| field_sample_number | string | Unique ID | 2011PN200001 |
| station | Station | Location reference | AL07DD0004 |
| project_name | string | Program name | OIL SANDS LONGTERM WQ MONITORING |
| sample_datetime | datetime | Collection time | 2011-10-27 11:56 |
| matrix | enum | Sample medium | WATER |
| sample_type | enum | Collection method | VERTICAL_INTEGRATED |
| water_depth_m | float? | Depth at location | 0.27 |

**Sample Types Found:**

| Type | Description | Purpose |
|------|-------------|---------|
| VERTICAL INTEGRATED | Depth-integrated water column | Representative of full water column |
| TRIPLICATE SAMPLE | Three sequential replicates | QA/QC precision assessment |
| ISOKINETIC TRANSECT COMPOSITE - EWI | Equal-width increment, velocity-matched | Representative of cross-section flow |
| EQUAL VOLUME TRANSECT COMPOSITE | Equal-volume across transect | Alternative cross-section method |

**Field Sample Number Format:**
```
Format: YYYYPNxxxxxx
Example: 2011PN200001
- YYYY: Year (2011)
- PN: Project code
- xxxxxx: Sequential number
```

**Cardinality:** ~1,650 samples per file (spanning 2011-2025)

### 6. Measurement

**Purpose:** Individual parameter reading from a sample - the core data record.

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| sample_event | SampleEvent | Parent sample | 2011PN200001 |
| parameter | Parameter | What measured | MERC_T_001 |
| analytical_method | string | How measured | Mercury |
| numeric_value | float? | Numeric result | 2.86 |
| text_value | string? | Non-numeric code | DE, IS, FC |
| is_numeric | boolean | Value type flag | true |
| unit_symbol | string | Unit | ng/L |
| flag_code | string? | Quality flag | L |
| mdl_value | float? | Detection limit | 0.035 |
| rl_value | float? | Reporting limit | 0.07 |
| is_below_mdl | boolean | Below MDL flag | false |
| is_below_rl | boolean | Below RL flag | false |

**Value Handling:**
- **Numeric values:** Store in `numeric_value`, set `is_numeric = true`
- **Non-numeric codes:** Store code in `text_value`, set `is_numeric = false`
- **Detection limit treatment:** Store MDL/RL values; compute censored values at query time

**Cardinality:** ~600 parameters × ~1,650 samples = ~1,000,000 measurements per file category

### 7. Sample Replicate

**Purpose:** Links original samples to their replicates for QA analysis.

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| original_sample | SampleEvent | Primary sample | 2011PN200001 |
| replicate_sample | SampleEvent | QC replicate | 2011PN200002 |
| replicate_type | enum | Type of replicate | field_duplicate, lab_replicate |
| relative_percent_difference | float? | Calculated RPD | 5.2 |
| qa_status | string? | Pass/fail assessment | pass |

**Replicate Types:**
- **Field Duplicate:** Two samples collected at same time/location
- **Lab Replicate:** Same sample analyzed twice
- **Split Sample:** Sample divided for multiple analyses

**Cardinality:** ~100s of replicate pairs

---

## Relationship Summary

```
Station
   │
   │ 1:N
   ▼
SampleEvent ←──── SampleReplicate (self-join for QA pairs)
   │
   │ 1:N
   ▼
Measurement
   │         │
   │ N:1     │ N:1
   ▼         ▼
Parameter   AnalyticalMethod
   │
   │ N:1
   ▼
QualityFlag (lookup)
```

---

## Data Quality Considerations

### Dual Detection Limits (MDL vs RL)

This dataset uses a two-tier detection limit system:

| Limit | Meaning | Flag |
|-------|---------|------|
| MDL (Method Detection Limit) | Lowest detectable concentration | L |
| RL (Reporting Limit) | Lowest reliably quantifiable concentration | R |

**Relationship:** MDL < RL always. Values between MDL and RL are detected but have higher uncertainty.

### Analytical Method Comparability

**Critical Warning:** Data from different analytical methods must NOT be combined:
- Metals52 vs Metals56 use different digestion methods
- Results are not directly comparable for trend analysis
- The data model must preserve method identity at the measurement level

### Wide-to-Narrow Transformation

**Problem:** Source files have 600+ columns (wide format), unsuitable for database storage.

**Solution:** Transform to EAV (Entity-Attribute-Value) pattern:
```
Wide:  sample_id | param_1 | flag_1 | param_2 | flag_2 | ... | param_600 | flag_600
Narrow: sample_id | parameter_id | value | flag
```

Each measurement becomes a row, enabling:
- Efficient indexing by parameter
- Flexible parameter addition
- Time-series optimized queries

### Detection Limit Statistics

**Challenge:** How to handle below-detection-limit values in statistical analysis?

**Options:**
1. **MDL/2:** Substitute half the detection limit (simple, common)
2. **MDL/√2:** Substitute MDL divided by √2 (theoretically better for lognormal)
3. **Kaplan-Meier:** Non-parametric survival analysis methods
4. **Maximum Likelihood:** Parametric estimation

**Recommendation:** Store raw MDL/RL values; compute substitution at query time based on analyst preference.

---

## Query Patterns to Support

1. **Parameter Time Series:** Mercury concentration at station M4 from 2015-2020
2. **Exceedance Analysis:** All measurements exceeding regulatory threshold X
3. **Station Summary:** Sample counts, parameter coverage, flag distribution by station
4. **Method Comparison:** Same parameter from Metals52 vs Metals56 (with warnings)
5. **Cross-Parameter Correlation:** Find samples with both parameter A and B measured
6. **Detection Limit Statistics:** % of measurements below MDL by parameter
7. **Replicate Analysis:** Calculate RPD for QA assessment
8. **Temporal Trends:** Annual/seasonal patterns with proper method stratification

---

## Volume Estimates

| Entity | Estimated Records | Growth Rate |
|--------|-------------------|-------------|
| Stations | ~10 | Rare additions |
| Parameters | 600+ | Rare additions |
| Analytical Methods | ~10 | Stable |
| Quality Flags | ~20 | Stable |
| Sample Events | ~1,650/file | Ongoing (seasonal) |
| Measurements | ~1,000,000/category | Ongoing |
| Sample Replicates | ~100s | Ongoing |

**Total Measurement Volume:** ~5,000,000 records across all 5 analytical categories

---

## Storage Recommendations

### High-Volume Entities (Time-Series)

**Measurements** benefit from:
- Time-series optimized storage (partitioning by year)
- Column indexing on `parameter_id`, `sample_datetime`
- Compression for historical data

### Catalog/Lookup Entities

**Stations, Parameters, Methods, Flags** are low-volume:
- Standard relational storage appropriate
- Frequent joins with measurements - optimize indexes
- Consider caching for application layer

### EAV Pattern Implementation

Transform wide CSV to narrow measurement table:
```sql
CREATE TABLE measurement (
    measurement_id UUID PRIMARY KEY,
    sample_id VARCHAR(20) NOT NULL,
    parameter_id VARCHAR(50) NOT NULL,
    numeric_value DOUBLE PRECISION,
    text_value VARCHAR(20),
    is_numeric BOOLEAN NOT NULL,
    flag_code VARCHAR(10),
    mdl_value DOUBLE PRECISION,
    rl_value DOUBLE PRECISION,
    is_below_mdl BOOLEAN DEFAULT FALSE,
    is_below_rl BOOLEAN DEFAULT FALSE,
    sample_year INTEGER NOT NULL,
    CONSTRAINT fk_sample FOREIGN KEY (sample_id) REFERENCES sample_event(field_sample_number),
    CONSTRAINT fk_parameter FOREIGN KEY (parameter_id) REFERENCES parameter(vmv_code)
) PARTITION BY RANGE (sample_year);
```

---

## Integration with Provincial Data

### Shared Concepts

Both federal and provincial datasets share:
- **Station concept** (though different station networks)
- **Sample event concept** (field visit with metadata)
- **Measurement concept** (parameter + value + quality)
- **Quality flag concept** (though different code vocabularies)

### Key Differences to Reconcile

| Aspect | Provincial | Federal | Reconciliation |
|--------|-----------|---------|----------------|
| Station codes | AB07DA2750 | AL07DD0004 | Separate namespaces or unified lookup |
| Parameters | ~100 common | 600+ specialized | Unified parameter catalog with source tags |
| Detection limits | Single RDL | Dual MDL+RL | Support both patterns |
| Quality flags | Lab-specific codes | L/R/Q + QA codes | Unified qualifier vocabulary |
| Sample types | GRAB, COMPOSITE | VERTICAL INTEGRATED, EWI | Unified sample type enum |

### Correlation Opportunities

Federal mainstem data can provide context for provincial data:
- **Spatial:** Federal stations often near provincial stations
- **Temporal:** Overlapping time periods enable cross-validation
- **Parameter:** Specialized federal parameters add depth to provincial data

---

## Integration with Luminous Biosensor Data

### Correlation Parameters

Federal water quality data provides environmental context for biosensor interpretation:

| Federal Parameter | Luminous Relevance |
|-------------------|-------------------|
| PAHs (total) | Organic contamination indicator |
| Naphthenic acids | Direct correlation with biosensor target |
| Dissolved organic carbon | Background organic load |
| pH | Affects NA speciation and toxicity |
| Temperature | Affects biosensor reaction kinetics |
| Metals (dissolved) | Potential biosensor interferents |
| TSS | Turbidity affecting optical measurements |

### Shared Location Framework

Both datasets can share:
- **Station definitions** - Same or nearby monitoring points
- **Temporal context** - Overlapping sampling periods
- **Quality vocabulary** - Unified flag/qualifier system

---

## Open Questions for Data Model Epic

1. **Station Unification:** Should federal and provincial stations be in the same table with a `source` discriminator, or separate tables with a common interface?

2. **Parameter Catalog:** How to handle 600+ federal parameters vs ~100 provincial? Unified catalog with category tags?

3. **Quality Flag Harmonization:** Map provincial lab-specific codes to federal L/R/Q system, or maintain both?

4. **Detection Limit Model:** Support dual MDL/RL from federal data while accommodating single RDL from provincial?

5. **Method Tracking:** How prominently should analytical method be tracked? At measurement level or sample level?

6. **Replicate Handling:** Unified replicate tracking across both data sources?

---

## References

- Environment and Climate Change Canada. (2019). *Surface Water Quality Notes - June 2019*.
- Environment and Climate Change Canada. (2019). *OSM Schemas Variable Names VMV Detection Limits - June 2019*.
- Oil Sands Monitoring Program. *Long-Term Water Quality Monitoring Data Files (2011-2025)*.
- See also: [Surface Water Quality Data Model](Surface-Water-Quality-Data-Model.md) for provincial data analysis
