# Luminous Data Modeling Research: JOSM Groundwater Quality

**Research Date:** 2026-01-21
**Data Source:** Joint Canada-Alberta Implementation Plan for Oil Sands Monitoring (JOSM)
**Files Analyzed:** Government groundwater quality datasets (2009-2011)

---

## Executive Summary

This research documents the data modeling requirements for integrating government environmental monitoring data into the Luminous platform. The JOSM groundwater quality dataset serves as the first reference implementation, establishing patterns for high-volume scientific measurement data, spatial hierarchies, and research document linkage.

---

## 1. Source Data Characteristics

### 1.1 Dataset Overview

The JOSM groundwater monitoring program collected **182 shallow groundwater samples** across four assessment areas in the Oil Sands region of northern Alberta:

| Assessment Area | River Code | Sample Prefix |
|-----------------|------------|---------------|
| Athabasca River | AR | AR-09-xxx, AR-10-xxx, AR-11-xxx |
| Ells River | ER | ER-10-xxx |
| Muskeg River | MR | MR-11-xxx |
| Steepbank River | SR | SR-09-xxx, SR-10-xxx |

**Key research focus:** Identifying whether groundwater contamination near oil sands tailings ponds originates from Oil Sands Process-Affected Water (OSPW).

### 1.2 File Types

| File Type | Purpose | Volume |
|-----------|---------|--------|
| CSV | Measurement data | 182 samples × 60 parameters = ~11,000 measurements per dataset |
| KMZ | Sample site coordinates | 11 KB per file |
| PDF | Research papers and methodology | 1-2 MB each |

### 1.3 CSV Structure

The CSV files follow a standardized government data format:

**Metadata Section (Rows 1-30):**
- Title, filename, generation date
- Organization: Environment and Climate Change Canada
- Program: JOSM (Joint Oil Sands Monitoring)
- Principal Investigator, Data Steward
- Open Government Licence reference
- QA Level (Level 1 = complete QA/QC)
- Assessment area mapping (station ID prefixes)
- Analytical method abbreviations

**Data Header (Rows 31-32):**
- Column headers with units
- ~60 columns of measured parameters

**Data Rows (Row 33+):**
- One row per sample
- Multiple samples at same station (different depths)

---

## 2. Measurement Parameters

### 2.1 Parameter Categories

**Trace Metals (D-MS - Dissolved Mass Spectrometry) - ug/L:**
| Symbol | Name | Typical Range |
|--------|------|---------------|
| Ag | Silver | 0-10 |
| Al | Aluminum | 0-5000 |
| As | Arsenic | 0-50 |
| B | Boron | 0-1000 |
| Ba | Barium | 0-500 |
| Be | Beryllium | 0-5 |
| Bi | Bismuth | 0-10 |
| Cd | Cadmium | 0-5 |
| Co | Cobalt | 0-50 |
| Cr | Chromium | 0-50 |
| Cu | Copper | 0-100 |
| Fe | Iron | 0-50000 |
| Ga | Gallium | 0-10 |
| La | Lanthanum | 0-10 |
| Li | Lithium | 0-100 |
| Mn | Manganese | 0-5000 |
| Mo | Molybdenum | 0-50 |
| Ni | Nickel | 0-100 |
| Pb | Lead | 0-50 |
| Rb | Rubidium | 0-100 |
| Sb | Antimony | 0-10 |
| Se | Selenium | 0-50 |
| Sr | Strontium | 0-5000 |
| Tl | Thallium | 0-5 |
| U | Uranium | 0-50 |
| V | Vanadium | 0-50 |
| Zn | Zinc | 0-500 |

**Major Ions (D-IC - Dissolved Ion Chromatography) - mg/L:**
| Symbol | Name | Typical Range |
|--------|------|---------------|
| Alkalinity | Alkalinity (as CaCO3) | 0-1000 |
| Ca | Calcium | 0-500 |
| Mg | Magnesium | 0-200 |
| Na | Sodium | 0-1000 |
| K | Potassium | 0-50 |
| Br | Bromide | 0-10 |
| Cl | Chloride | 0-500 |
| F | Fluoride | 0-10 |
| NO2 | Nitrite | 0-10 |
| NO3 | Nitrate | 0-50 |
| PO4 | Phosphate | 0-10 |
| SO4 | Sulphate | 0-500 |
| NH4 | Ammonium | 0-50 |

**Field Measurements:**
| Parameter | Unit | Typical Range |
|-----------|------|---------------|
| Dissolved Oxygen (DO) | mg/L | 0-15 |
| Electrical Conductivity (EC) | uS/cm | 0-5000 |
| Oxidation Reduction Potential (ORP) | mV | -500 to +500 |
| pH | pH Units | 4-10 |
| Temperature | °C | 0-30 |

**Organic Analysis (SFS - Synchronous Fluorescence Spectroscopy):**
| Wavelength | Unit | Purpose |
|------------|------|---------|
| 282 nm | Intensity | Aromatic compound detection |
| 320 nm | Intensity | Aromatic compound detection |
| 333 nm | Intensity | Aromatic compound detection |

### 2.2 Quality Considerations

- **Detection Limits:** Many trace metals have values below detection limits (BDL), recorded as null or special flags
- **QA Flags:** Standard environmental data quality flags (J=estimated, U=non-detect, etc.)
- **Outliers:** Iron (Fe) can reach 25,000+ ug/L in some samples - natural variation, not errors

---

## 3. Spatial Hierarchy

### 3.1 Geographic Structure

```
Assessment Area (region)
    └── Sampling Station (point location)
            └── Sample (depth + date)
                    └── Measurements (parameter values)
```

### 3.2 Station Identification

**Naming Convention:** `{RiverCode}-{Year}-{SequenceNumber}`
- Example: `SR-09-001` = Steepbank River, 2009, Station 001

**Station Attributes:**
- Master Station ID (unique identifier)
- Latitude (decimal degrees, North)
- Longitude (decimal degrees, West - stored as positive)
- Position Note (optional qualitative description)
- Station Type (piezometer, monitoring well, surface water)

### 3.3 Coordinate Sources

Coordinates may come from:
1. **KMZ files** - Most accurate, from GPS surveys
2. **CSV data** - Embedded in data rows
3. **Manual entry** - From field notes or maps

KMZ files contain KML (XML) with Placemark elements:
```xml
<Placemark>
  <name>SR-09-001</name>
  <Point>
    <coordinates>-111.4805319,57.01980941,0</coordinates>
  </Point>
</Placemark>
```

---

## 4. Temporal Dimensions

### 4.1 Time Scales

| Dimension | Granularity | Purpose |
|-----------|-------------|---------|
| Sample Date | Day | When water was collected |
| Sample Time | Hour:Minute | Optional, for diurnal studies |
| Import Date | Timestamp | Audit trail |
| Dataset Period | Year range | Dataset version tracking |

### 4.2 Multi-Year Datasets

Datasets span multiple years (2009-2011) with:
- Same stations revisited across years
- Different depths sampled at same station/date
- Replicate samples for QA purposes

**Uniqueness:** A sample is uniquely identified by (Station + Date + Depth + Replicate Number)

---

## 5. Research Document Integration

### 5.1 Document Types

| Type | Purpose | Example |
|------|---------|---------|
| Research Paper | Published analysis of data | EST source identification study |
| Methodology | Lab procedures, QA protocols | Analytical methods documentation |
| Report | Government reports | JOSM annual reports |
| Supplementary | Supporting materials | Raw data appendices |

### 5.2 Document Metadata

Research documents should capture:
- Title, Authors, Publication Year
- Journal/Publisher
- DOI (if available)
- Abstract
- Keywords
- Linked datasets (which datasets this paper analyzes)

### 5.3 Key Research Findings (Context)

The EST-source-identification.pdf reveals:
- 6 groundwater samples near tailings ponds show OSPW chemical signatures
- 2 samples from <1m beneath Athabasca River indicate contamination migration
- Multi-level analysis: basic geochemistry, SFS, naphthenic acids, ESI-HRMS

This context is important for interpreting the measurement data.

---

## 6. Data Provenance Requirements

### 6.1 Dataset-Level Provenance

Every imported dataset must record:

| Field | Source | Purpose |
|-------|--------|---------|
| Organization | CSV metadata | Data ownership |
| Principal Investigator | CSV metadata | Scientific accountability |
| QA Level | CSV metadata | Data quality tier |
| License | CSV metadata | Usage rights |
| Source File Hash | Computed | Duplicate detection |
| Import User | System | Audit trail |
| Import Timestamp | System | Audit trail |

### 6.2 Row-Level Audit

For debugging and data quality investigations:
- Original CSV row number
- Original row data (JSON)
- Content hash for duplicate detection

---

## 7. Data Volume Projections

### 7.1 Current Dataset

| Entity | Count | Growth Pattern |
|--------|-------|----------------|
| Datasets | 3 | Per import batch |
| Stations | ~50 | Fixed per study area |
| Samples | 182 | Per dataset |
| Measurements | ~11,000 | Samples × Parameters |
| Parameters | 60 | Fixed catalog |

### 7.2 Future Growth

With ongoing monitoring programs:
- New datasets quarterly/annually
- 100-500 samples per dataset
- Cumulative measurements: 100K-1M+ over 5 years

**Implication:** Measurement storage must be optimized for high-volume queries:
- Time-series by station and parameter
- Cross-station comparisons for a parameter
- Full sample profiles (all parameters for one sample)

---

## 8. Query Patterns

### 8.1 Primary Access Patterns

| Pattern | Description | Frequency |
|---------|-------------|-----------|
| Sample Detail | All measurements for one sample | High |
| Station Time Series | One parameter at one station over time | High |
| Parameter Distribution | One parameter across all stations | Medium |
| Dataset Overview | Sample counts, date ranges, station list | Medium |
| Spatial Query | Samples within geographic bounds | Medium |
| QA Filtering | Exclude flagged measurements | Always |

### 8.2 Aggregation Needs

| Aggregation | Use Case |
|-------------|----------|
| Min/Max/Mean per station-parameter | Trend analysis |
| Detection frequency | QA reporting |
| Temporal gaps | Data completeness |
| Exceedance counts | Regulatory compliance |

---

## 9. Integration Points

### 9.1 Weather Correlation

The JOSM data includes weather as a factor in contamination transport. Future enhancement:
- Link samples to Environment Canada weather data
- Auto-fetch historical weather for sample dates
- Support correlation analysis (temperature vs. NA concentration)

### 9.2 Biosensor Data (Future)

Luminous biosensor data (naphthenic acid detection via atuA, marR, 3680 panels) will need:
- Same spatial hierarchy (sites, samples)
- Different measurement structure (fluorescence readings, calculated concentrations)
- Linkage between field samples and lab results

**Design for extensibility:** The station/sample hierarchy should be shared; measurement structures may differ by data source.

### 9.3 External Systems

| System | Integration |
|--------|-------------|
| Fulcrum | Field data collection webhooks |
| Environment Canada API | Weather data |
| GIS/Mapping | GeoJSON export of stations |

---

## 10. Data Quality Rules

### 10.1 Validation at Import

| Rule | Action |
|------|--------|
| Missing Station ID | Reject row |
| Missing Sample Date | Reject row |
| Invalid Station ID format | Reject row |
| Missing coordinates | Accept with warning |
| Duplicate sample | Reject with error |
| Value out of range | Accept with warning flag |
| Non-numeric measurement | Accept as text, flag |

### 10.2 Business Rules

| Rule | Enforcement |
|------|-------------|
| Station ID must follow naming convention | Regex validation |
| Coordinates must be in Alberta region | Bounding box check |
| Sample date cannot be in future | Date comparison |
| Detection limit must be positive | Range check |

---

## 11. Open Questions for Data Modeling Epic

1. **Shared vs. Separate Hierarchies:** Should biosensor data share the same station/sample tables as JOSM data, or use separate tables with relationships?

2. **Parameter Extensibility:** How to handle new parameters added in future datasets? Dynamic schema vs. EAV pattern?

3. **Historical Data Imports:** Will we need to import historical data from other monitoring programs (pre-2009)?

4. **Real-time vs. Batch:** Is all data batch-imported, or will there be real-time sensor data in future?

5. **Multi-tenant Considerations:** Will multiple organizations (tenants) share parameter catalogs, or maintain separate ones?

6. **Regulatory Thresholds:** Should guideline values (CCME, Alberta Environment) be stored with parameters for automated compliance checking?

---

## 12. Recommended Entity Summary

Based on this research, the core entities for JOSM groundwater data are:

| Entity | Purpose | Key Relationships |
|--------|---------|-------------------|
| **Dataset** | Import batch with provenance | Has many Samples |
| **Station** | Physical sampling location | Has many Samples |
| **Sample** | Collection event | Belongs to Dataset, Station; Has many Measurements |
| **Measurement** | Individual parameter value | Belongs to Sample, Parameter |
| **Parameter** | Analyte catalog | Referenced by Measurements |
| **DatasetDocument** | Linked research papers | Belongs to Dataset |

This structure supports:
- High-volume measurement storage
- Flexible parameter catalogs
- Full audit trail
- Research document linkage
- Spatial and temporal queries

---

## References

- Environment and Climate Change Canada. (2015). *Groundwater Quality 2009-2011 Dataset*.
- Frank, R.A., et al. (2014). *Profiling Oil Sands Mixtures from Industrial Developments and Natural Groundwaters for Source Identification*. Environmental Science & Technology.
- Roy, J.W., et al. (2016). *Assessing Risks of Shallow Riparian Groundwater Quality Near an Oil Sands Tailings Pond*. Groundwater.
- Open Government Licence - Canada: https://open.canada.ca/en/open-government-licence-canada
