# Wetland Surface Water Quality - Data Analysis

**Date:** 2026-01-21
**Source:** Alberta OSM Wetland Monitoring Program
**Purpose:** Inform Luminous Platform Group data modeling requirements

---

## Executive Summary

Analysis of the Alberta Oil Sands Monitoring (OSM) Wetland Surface Water Quality dataset reveals a comprehensive environmental monitoring data structure that serves as a reference model for Luminous's water quality data management needs. The dataset spans 7 fiscal years (2017-2025) with 18,463 records across 10 wetland sites, measuring 250+ analytical parameters.

This document captures the data structure, relationships, and modeling considerations that should inform the Luminous data model design.

---

## Dataset Overview

### Source Files

| Fiscal Year | File | Records | Columns |
|-------------|------|---------|---------|
| 2017-18 | `2017-18-osm-wetland-monitoring-surface-water-quality.xlsx` | 4,095 | 37 |
| 2018-19 | `2018-19-osm-wetland-monitoring-surface-water-quality.xlsx` | 2,423 | 37 |
| 2019-20 | `2019-20-osm-wetland-monitoring-surface-water-quality.xlsx` | 2,638 | 37 |
| 2020-21 | *Missing* | - | - |
| 2021-22 | `2021-22-osm-wetland-monitoring-surface-water-quality.xlsx` | 1,988 | 37 |
| 2022-23 | `2022-23-osm-wetland-monitoring-surface-water-quality.xlsx` | 2,982 | 38 |
| 2023-24 | `2023-24-osm-wetland-monitoring-surface-water-quality.xlsx` | 1,834 | 38 |
| 2024-25 | `2024-25-osm-wetland-monitoring-surface-water-quality.xlsx` | 2,503 | 38 |

**Total Records:** 18,463
**Note:** Schema evolved from 37 to 38 columns in 2022-23 (additional field added)

### Data Structure

Each row represents a **single analytical measurement** - one parameter result from one sample. A single water sample collected at a site generates 20-50+ rows (one per parameter measured).

---

## Data Dimensions

### 1. Location Hierarchy

```
Monitoring Program (ABS261)
└── Site (GREAT DIVIDE, PEACE-ATHABASCA DELTA, etc.)
    └── Station (AB07CC0460 - UNNAMED WETLAND)
        └── GPS Coordinates (56.1075°N, 111.8384°W)
```

**Sites Identified (10 total):**
- GREAT DIVIDE (highest sample volume)
- HANGINGSTONE EXPANSION
- NEAR HALFWAY CREEK
- NEAR MAQUA LAKE
- NEAR MARIANNA LAKE
- NORTHWEST OF MCCLELLAND LAKE
- PEACE-ATHABASCA DELTA
- QC (Quality Control site)
- SUNCOR MACKAY ACCESS ROAD
- TOWER ROAD

**Station Naming Convention:** `AB07CC0460` format with descriptive suffix (e.g., "UNNAMED WETLAND (HOR01 - BORROW PIT)")

### 2. Temporal Dimension

| Field | Format | Example |
|-------|--------|---------|
| Sample Date | Excel serial date | 42959 (= 2017-09-25) |
| Sample Time | Decimal fraction of day | 0.319 (= 7:40 AM) |
| Fiscal Year | Derived from filename | 2017-18 |

**Consideration:** Sample date should be the primary temporal key. Time is optional but valuable for same-day multi-sample events.

### 3. Sample Identification

| Field | Description | Example |
|-------|-------------|---------|
| Sample Number | Unique identifier | Sequential or coded |
| Sample Depth | Reference code | 17SWE13125 |
| Final Depth | Adjusted depth (meters) | Numeric |
| Sample Matrix | Material type | WATER, SEDIMENT, BIOTA |
| Sample Type | Category | Various classifications |
| Collection Method | How collected | HAND COLLECTION |

**Matrix Distribution:** Predominantly WATER samples, with minor SEDIMENT and BIOTA

### 4. Parameter Classification

```
Parameter Type Group (broad category)
└── Parameter Type Name (specific analyte)
    └── Parameter Subject (focus area)
```

**Parameter Groups Identified:**
- **Minor Elements:** Aluminum, Iron, Manganese, etc. (dissolved and total recoverable forms)
- **Major Elements:** Calcium, Magnesium, Sodium, Potassium
- **Trace Metals:** Arsenic, Barium, Beryllium, Bismuth, Cadmium, Chromium, Copper, Lead, Mercury, etc.
- **Polycyclic Aromatic Hydrocarbons (PAHs):** Naphthalene, Anthracene, Phenanthrene, Pyrene, etc.
- **Alkylated PAHs:** C1-C4 homologs of various PAH compounds
- **Nutrients:** Total Nitrogen, Total Phosphorus, Nitrate, Ammonia
- **Field Measurements:** pH, Temperature, Conductivity, Dissolved Oxygen, Turbidity
- **Hydrocarbons:** Fractionated hydrocarbons (F2, F3, F4)
- **Other:** Sulfide, TSS, TDS, Hardness

**Total Unique Parameters:** 250+

### 5. Analytical Method

| Field | Description | Example |
|-------|-------------|---------|
| Method Code | Coded identifier | Alphanumeric |
| Method Name | Full description | "ICP-MS (Dissolved elements by inductively coupled argon plasma emission spectrometry)" |
| RDL | Reporting Detection Limit | 0.4 |
| RDL Unit | Unit for detection limit | µg/L |

### 6. Laboratory Information

| Field | Description |
|-------|-------------|
| Laboratory | Lab name/code |
| Lab QAQC Batch ID | Batch tracking |

**Laboratories Identified (30+ unique):**
- AITF-EAS (Environmental Analytical Services)
- AXYS Analytical Services Ltd
- Maxxam (Chemex) Labs Alberta Inc., Calgary
- University of Alberta - Biogeochemical Analytical Service Laboratory
- Various field-based labs (WG60731, etc.)
- Multiple batch IDs: 17080145-001, 17080146-001, etc.

### 7. Measurement Results

| Field | Description | Example |
|-------|-------------|---------|
| Parameter Value | Numeric measurement | 1.6 |
| Parameter Sign | Relation to detection limit | `<`, `>`, `=`, or blank |
| Parameter Unit Symbol | Abbreviated unit | µg/L, mg/L, °C |
| Parameter Unit Name | Full unit name | micrograms per liter |
| Value and Sign | Combined display | "<0.4", "1.6" |

**Censored Data Handling:** Values below detection limit indicated by `<` sign. This is critical for statistical analysis.

### 8. Quality Control

| Field | Description |
|-------|-------------|
| QC Sample (Y/N) | Is this a QC sample? |
| Lab Qualifier 1-4 | Laboratory quality flags |
| Sampling Comment | Field notes |
| Parameter Standard Remark | Comparison to standards |
| Parameter Remark | Additional notes |

---

## Key Data Relationships

### Entity Relationship Model

```
┌─────────────────┐
│ Program         │
│ (ABS261)        │
└────────┬────────┘
         │ 1:N
         ▼
┌─────────────────┐
│ Site            │
│ (GREAT DIVIDE)  │
└────────┬────────┘
         │ 1:N
         ▼
┌─────────────────┐
│ Station         │
│ (AB07CC0460)    │
│ + GPS coords    │
└────────┬────────┘
         │ 1:N
         ▼
┌─────────────────┐      ┌─────────────────┐
│ Sample          │      │ Weather         │
│ (date, time,    │◄────►│ (conditions at  │
│  matrix, depth) │ 1:N  │  sample time)   │
└────────┬────────┘      └─────────────────┘
         │ 1:N
         ▼
┌─────────────────┐      ┌─────────────────┐
│ Result          │─────►│ Parameter       │
│ (value, sign,   │ N:1  │ (name, group,   │
│  qualifiers)    │      │  units, CAS#)   │
└────────┬────────┘      └─────────────────┘
         │ N:1
         ▼
┌─────────────────┐      ┌─────────────────┐
│ Method          │      │ Laboratory      │
│ (code, RDL)     │      │ (name, accred.) │
└─────────────────┘      └─────────────────┘
```

### Cardinality Summary

| Relationship | Cardinality | Notes |
|--------------|-------------|-------|
| Program → Site | 1:N | One program monitors multiple sites |
| Site → Station | 1:N | Sites contain multiple sampling stations |
| Station → Sample | 1:N | Stations sampled multiple times |
| Sample → Result | 1:N | Each sample yields 20-50+ results |
| Result → Parameter | N:1 | Many results for same parameter |
| Result → Method | N:1 | Results linked to analytical method |
| Result → Laboratory | N:1 | Results linked to performing lab |
| Sample → Weather | 1:N | Multiple weather readings possible |

---

## Sample Record Analysis

### Example Record (2017-18, Row 2)

```yaml
# Location
Program: ABS261
Site: GREAT DIVIDE
Station: AB07CC0460 - UNNAMED WETLAND (HOR01 - BORROW PIT)
Latitude: 56.1075
Longitude: -111.8384

# Sample
Date: 2017-09-25 (serial: 42959)
Time: 7:40 AM (0.319)
Depth Code: 17SWE13125
Matrix: WATER
Collection: HAND COLLECTION

# Analysis
Laboratory: AITF-EAS
Batch ID: 17080145-001
Parameter: Aluminum Dissolved
Method: ICP-MS
RDL: 0.4 µg/L

# Result
Value: 1.6
Unit: µg/L
Sign: (none - above detection limit)

# Quality
QC Sample: N
Qualifiers: (none)
Comments: "Shoreline Grab; Sandy loam texture; Low organic matter"
```

### Data Volume Projections

For a typical monitoring program:
- **Per sample:** 20-50 analytical results
- **Per site/year:** 200-500 samples
- **Per program/year:** 2,000-4,000 results
- **Multi-year archive:** 10,000-100,000+ results

This volume justifies PostgreSQL for efficient aggregation queries.

---

## Data Quality Considerations

### Detection Limit Handling

Three scenarios for measurement values:
1. **Above RDL:** Value is reported as-is
2. **Below RDL:** Value shown with `<` sign (e.g., `<0.4`)
3. **Above upper limit:** Value shown with `>` sign

**Modeling implication:** Store both `value` and `value_sign` separately for proper statistical treatment.

### Quality Control Samples

QC samples are flagged separately and should be:
- Included in data validation analysis
- Excluded from environmental trend analysis
- Tracked for lab performance metrics

### Lab Qualifiers

Four qualifier fields (Lab Qualifier 1-4) capture:
- Instrument issues
- Sample handling notes
- Analytical anomalies
- Validation flags

These should be preserved but may not need individual columns - JSONB array is sufficient.

---

## Regulatory Compliance Context

### Standards Referenced

The dataset includes `Parameter Standard Remark` field suggesting comparison against:
- Alberta Environmental Quality Guidelines
- Canadian Council of Ministers of the Environment (CCME) guidelines
- Site-specific thresholds

### Exceedance Tracking Requirements

For compliance monitoring, the system must:
1. Compare results against applicable standards
2. Flag exceedances immediately
3. Track exceedance history by parameter/site
4. Support both absolute thresholds and percentage-based limits
5. Handle range-based standards (min/max)

---

## Data Modeling Recommendations

### High-Volume Considerations

The `Result` entity will contain the vast majority of records. Optimize for:
- Efficient bulk inserts (batch imports)
- Fast aggregation queries (GROUP BY parameter, site, date range)
- Time-series analysis (trend detection)
- Partial index on exceedance flag

### Reference Data Stability

These entities change infrequently and should be cached:
- Parameters (250+ but stable)
- Methods (analytical methods rarely change)
- Laboratories (new labs added occasionally)
- Sites/Stations (geographic, rarely change)

### Temporal Partitioning

Consider partitioning the results table by:
- **Sample date (recommended):** Natural partitioning for time-series queries
- **Fiscal year:** Aligns with data source structure

### Multi-Source Data

The model must distinguish:
- **External data:** Imported from government sources (read-only after import)
- **Internal data:** Generated by Luminous operations (full CRUD)

Track provenance via import batch linkage.

### Weather Integration

Weather data can be:
1. **Embedded:** JSONB summary on sample record (quick access)
2. **Normalized:** Separate table with full meteorological detail
3. **Both:** Embedded summary + normalized detail for analysis

Recommendation: Both approaches serve different use cases.

---

## Field Inventory

### Complete Column List (38 fields as of 2022-23)

| # | Field Name | Data Type | Required | Notes |
|---|------------|-----------|----------|-------|
| 1 | Measuring program name | VARCHAR(20) | Yes | Program code |
| 2 | Site name | VARCHAR(255) | Yes | Wetland name |
| 3 | Station number | VARCHAR(50) | Yes | Station code |
| 4 | Station name | VARCHAR(500) | No | Detailed description |
| 5 | Latitude | DECIMAL(10,7) | Yes | GPS |
| 6 | Longitude | DECIMAL(11,7) | Yes | GPS |
| 7 | Location | VARCHAR(50) | No | Location code |
| 8 | Sample date | DATE | Yes | Collection date |
| 9 | Sample time | TIME | No | Collection time |
| 10 | Sample depth | VARCHAR(50) | No | Depth code |
| 11 | Sample final depth | DECIMAL(8,2) | No | Depth in meters |
| 12 | Sample number | VARCHAR(100) | Yes | Unique ID |
| 13 | Sample Matrix | VARCHAR(20) | Yes | WATER/SEDIMENT/BIOTA |
| 14 | Sample Type | VARCHAR(50) | No | Category |
| 15 | Sample Collection | VARCHAR(100) | No | Method |
| 16 | Laboratory | VARCHAR(255) | No | Lab name |
| 17 | QC Sample (Y/N) | BOOLEAN | Yes | QC flag |
| 18 | Lab QAQC Batch ID | VARCHAR(100) | No | Batch tracking |
| 19 | Parameter method | VARCHAR(500) | No | Method name |
| 20 | Method code | VARCHAR(50) | No | Method ID |
| 21 | Reporting Detection Limit | DECIMAL(20,10) | No | RDL |
| 22 | RDL Unit | VARCHAR(20) | No | RDL unit |
| 23 | Parameter type group | VARCHAR(100) | No | Broad category |
| 24 | Parameter type name | VARCHAR(255) | Yes | Specific parameter |
| 25 | Parameter subject | VARCHAR(100) | No | Focus area |
| 26 | Parameter sign | VARCHAR(5) | No | <, >, = |
| 27 | Parameter value | DECIMAL(20,10) | No | Measurement |
| 28 | Parameter unit symbol | VARCHAR(20) | No | Unit abbrev |
| 29 | Parameter value and sign | VARCHAR(50) | No | Display format |
| 30 | Parameter unit name | VARCHAR(100) | No | Full unit name |
| 31 | Lab Qualifier 1 | VARCHAR(50) | No | QC flag |
| 32 | Lab Qualifier 2 | VARCHAR(50) | No | QC flag |
| 33 | Lab Qualifier 3 | VARCHAR(50) | No | QC flag |
| 34 | Lab Qualifier 4 | VARCHAR(50) | No | QC flag |
| 35 | Sampling comment | TEXT | No | Field notes |
| 36 | Parameter standard remark | TEXT | No | Standard comparison |
| 37 | Parameter remark | TEXT | No | Additional notes |
| 38 | *New field (2022+)* | TBD | No | Added in schema evolution |

---

## Analytical Use Cases

The data model should support these queries efficiently:

### Trend Analysis
- Parameter concentration over time at a station
- Seasonal patterns across years
- Rate of change detection

### Compliance Reporting
- Exceedance counts by parameter/site/period
- Comparison against multiple standards
- Historical compliance status

### Spatial Analysis
- Cross-site parameter comparison
- Geographic clustering of exceedances
- Upstream/downstream correlations

### Laboratory Performance
- Turnaround time analysis
- QC sample pass rates
- Method detection limit trends

### Data Quality
- Missing data identification
- Outlier detection
- Duplicate sample flagging

---

## Next Steps for Data Modeling

1. **Normalize reference data:** Parameters, methods, laboratories, sites
2. **Design result schema:** Optimized for high-volume analytical data
3. **Define exceedance logic:** How to calculate and store compliance flags
4. **Plan import pipeline:** Excel parsing with validation and provenance
5. **Consider weather integration:** Meteorological data sources and linkage
6. **Document regulatory standards:** Alberta ESRD, CCME, site-specific thresholds

---

## References

- Source data: `/mnt/c/Users/mdrob/ObsidianJournals/Luminous/Square Head Data/Government/Wetland Surface Water Quality/`
- Alberta OSM Program: Oil Sands Monitoring wetland water quality program
- Related epics: Platform Groups (EPIC-01), Unified Data Access (EPIC-03), MCP Server (EPIC-14)
