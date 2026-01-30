# Surface Water Quality Data Model Research

**Date:** 2026-01-21
**Data Source:** Alberta Government Surface Water Quality Discrete Monitoring
**Location:** `/mnt/c/Users/mdrob/ObsidianJournals/Luminous/Square Head Data/Government/Surface Water Quality Discreet`

---

## Executive Summary

This document captures data modeling requirements derived from analyzing Alberta Government surface water quality monitoring data. The dataset represents a canonical example of environmental time-series monitoring data with complex relationships between locations, samples, measurements, and contextual factors.

**Key characteristics:**
- ~980 MB of historical data spanning 1998-2026
- 230 monitoring stations across Northern Alberta
- 71 CSV files organized by monitoring program
- 40 columns per measurement record
- Denormalized structure requiring normalization for efficient storage and querying

---

## Data Domain Overview

### What This Data Represents

Surface water quality monitoring involves:
1. **Field teams** visiting stations to collect water samples
2. **Laboratories** analyzing samples for various chemical/biological parameters
3. **Programs** organizing monitoring activities under regulatory/funding frameworks
4. **Quality control** tracking data reliability through qualifier codes

### Hierarchical Structure

```
Monitoring Program (funding/regulatory context)
  └── Station (physical location)
      └── Sample Event (single visit: date + time + conditions)
          └── Measurements (20-40+ parameter readings per sample)
              ├── Parameter (what was measured)
              ├── Method (how it was measured)
              ├── Value + Unit
              └── Quality flags
```

---

## Source Data Analysis

### File Organization

```
Surface Water Quality Discreet/
├── station_metadata_sw_discrete.csv    # 230 stations
├── sample_metadata_lab_qualifiers.csv  # 15 QC codes
├── abs058-20260106_165045/             # Program ABS058 (18 files, 1998-2015)
├── abs098-20260106_165047/             # Program ABS098 (29 files, 1998-2026)
├── abs191-20260106_165050/             # Program ABS191 (5 files, 2011-2015)
├── abs240-20260106_165051/             # Program ABS240 (12 files, 2015-2026)
└── abs264/                             # Program ABS264 (5 files, 2018-2022)
```

### Source Schema (40 columns)

| Category | Fields |
|----------|--------|
| **Program/Location** | Measuring program, Site name, Station number, Station name, Latitude, Longitude |
| **Sample Collection** | Sampling location, Sample date, Sample time, Sample depth, Sample final depth, Sample number, Sample Matrix, Sample Type, Sample Collection |
| **Laboratory** | Laboratory, QC Sample (Y/N), Lab QAQC Batch ID |
| **Analysis Method** | Analysis method name, Analysis method code, Reporting Detection Limit (RDL), RDL Unit |
| **Parameter** | Parameter type group, Parameter type name |
| **Measurement** | Parameter sign, Parameter value, Parameter unit symbol, Parameter value and sign, Parameter unit name |
| **Quality Flags** | Lab Qualifier 1, Lab Qualifier 2, Lab Qualifier 3, Lab Qualifier 4 |
| **Comments** | Sampling comment, Sample remark, Parameter remark, Parameter standard remark, Last modified date and time |

### Sample Data Examples

**Direct Measurement (ICAP Spectrometry):**
```
Station: AB07DA2750 (Muskeg River D/S of Stanly Creek)
Date: 1998-05-27 10:50:00
Parameter: Calcium Dissolved
Method: Inductively coupled argon plasma (ICAP) emission spectrometry
Value: 40.700 mg/L
```

**Calculated Value:**
```
Station: AB07DA2750
Date: 1998-05-27 10:50:00
Parameter: Hardness Total (Calcd.) CaCO3
Method: Total hardness by calculated method
Value: 143 mg/L
Formula: 2.497×Ca + 4.118×Mg
```

**Below Detection Limit:**
```
Parameter: Sulphate Dissolved
Sign: <
Value: 3.00 mg/L
Interpretation: Actual value is below 3.00 mg/L
```

---

## Entity Definitions

### 1. Monitoring Program

**Purpose:** Organizational container for monitoring activities under a funding/regulatory framework.

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| code | string | Short identifier | ABS058, ABS098 |
| name | string | Full name | (varies by program) |
| description | string? | Purpose/scope | |
| start_date | date? | When monitoring began | 1998-01-01 |
| end_date | date? | When ended (null if active) | null |
| is_active | boolean | Currently active | true |

**Cardinality:** ~5-10 programs in this dataset

### 2. Station

**Purpose:** Physical monitoring location with geographic coordinates.

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| station_number | string | Government code (unique) | AB07DA2750 |
| station_name | string | Short name | D/S OF STANLY CREEK |
| long_name | string? | Full descriptive name | MUSKEG RIVER D/S OF STANLY CREEK |
| site_name | string | Water body | MUSKEG RIVER |
| latitude | float | GPS latitude | 57.33111 |
| longitude | float | GPS longitude | -111.37389 |
| theme | string | Category | Surface Water |
| josm_station_code | string? | JOSM reference | |
| ramp_station_code | string? | RAMP reference | AC-DS |
| parent_station | Station? | For transect groupings | (see below) |

**Station Hierarchy:** Some stations form transects (multiple sampling points across a river cross-section):
- ATR-DC-CC (Athabasca River - centre)
- ATR-DC-E (Athabasca River - east)
- ATR-DC-M (Athabasca River - middle)
- ATR-DC-W (Athabasca River - west)

These should reference a parent station for grouping.

**Cardinality:** 230 stations in metadata file

**Relationship to Programs:** Many-to-many. A station can participate in multiple programs over time.

### 3. Parameter

**Purpose:** What is being measured (the analyte or physical property).

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| name | string | Parameter name | Calcium Dissolved |
| type_group | string | Category | Major Ions |
| canonical_unit | string | Standard unit | mg/L |

**Parameter Groups Found:**
- Major Ions (Ca, Mg, Na, K, Cl, F, SO4, alkalinity, hardness)
- Nutrients (nitrogen, phosphorus, ammonia)
- Routine (pH, temperature, conductance, turbidity, color)
- Carbon (dissolved organic, particulate)
- Biological (Chlorophyll A)
- Minor Elements (Fe, Mn)
- Oxygen (dissolved, BOD)
- Metals (various trace metals)

**Cardinality:** ~100+ unique parameters

### 4. Lab Method

**Purpose:** Analytical technique used to determine a measurement.

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| code | string | Method code | 1516 |
| name | string | Method name | Inductively coupled argon plasma (ICAP) emission spectrometry |
| description | string? | Full description | |
| is_calculated | boolean | Derived vs direct | false |

**Critical Insight:** The same parameter can be determined by different methods:
- **Total Dissolved Solids** can be:
  - Calculated (method 12, 14)
  - Gravimetric (method 407)

The `is_calculated` flag distinguishes:
- **Calculated methods:** "Calculated value", "Total hardness by calculated method"
- **Direct methods:** Specific lab techniques (spectrometry, titration, etc.)

**Cardinality:** ~50+ unique methods

### 5. Laboratory

**Purpose:** Organization performing the analysis.

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| name | string | Lab name | ALBERTA RESEARCH COUNCIL, INORGANIC ANALYSIS LABORATORY |
| short_code | string? | Abbreviation | AITF-EAS |

**Labs in Dataset:**
- Alberta Research Council (various divisions)
- Alberta Environmental Protection Monitoring Branch
- AXYS Analytical Services Ltd
- University of Alberta - Biogeochemical Analytical Service Laboratory
- FIELD (for in-situ measurements)

**Note:** Could be a simple string field or a normalized lookup table depending on needs.

### 6. Lab Qualifier

**Purpose:** Quality control codes explaining data reliability.

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| code | string | Qualifier code | I |
| lab | string | Which lab uses this | AITF-EAS |
| description | string | Meaning | Between method detection limit and practical quantitation limit |

**Qualifier Codes Found:**

| Code | Lab | Meaning |
|------|-----|---------|
| I | AITF-EAS | Between detection limit and quantitation limit |
| K | AITF-EAS | Off-scale low (actual < reported) |
| T | AITF-EAS | Below method detection limit |
| U | AITF-EAS | Analyzed but not detected |
| H | AXYS | Concentration estimated |
| ND | AXYS | Not detected |
| NDR | AXYS | Peak detected but below quantification |
| NQ | AXYS | Data not quantifiable |
| VV | U of A | Value verified |
| HT | U of A | Holding time exceeded |
| CA | U of A | Analysis cancelled |
| LE | U of A | Lost sample due to lab error |

**Cardinality:** 15 qualifier codes

### 7. Sample Event

**Purpose:** A single sampling visit - one trip to a station at a specific date/time.

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| sample_number | string | Unique ID (business key) | 98SWE00810-01 |
| station | Station | Where | AB07DA2750 |
| sample_date | date | When | 1998-05-27 |
| sample_time | time | When | 10:50:00 |
| sample_depth | float? | Depth in water column | null |
| sample_final_depth | float? | Final measurement depth | null |
| sample_matrix | string | Sample type | WATER |
| sample_type | enum | Collection method | DISCRETE_GRAB |
| collection_method | string | How collected | HAND COLLECTION |
| sampling_location | string | Position | Centre |
| is_qc_sample | boolean | Quality control flag | false |
| laboratory | string | Primary lab | Alberta Research Council |
| lab_batch_id | string? | QAQC batch | null |
| sampling_comment | string? | Field notes | |
| sample_remark | string? | Lab notes | |

**Sample Types Found:**
- DISCRETE SAMPLE (GRAB) - single point-in-time sample
- EUPHOTIC COMPOSITE - depth-integrated sample using weighted tube
- Others as encountered

**Cardinality:** ~10,000+ sample events (estimate based on file sizes)

### 8. Measurement

**Purpose:** Individual parameter reading from a sample.

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| sample_event | SampleEvent | Parent sample | |
| parameter | Parameter | What measured | Calcium Dissolved |
| lab_method | LabMethod | How measured | ICAP |
| laboratory | string | Which lab | ARC |
| value | float | Numeric result | 40.700 |
| value_sign | string? | <, >, or null | null |
| unit_symbol | string | Unit | mg/L |
| detection_limit | float? | RDL | 0.01 |
| detection_limit_unit | string? | RDL unit | mg/L |
| qualifier_1 | string? | QC flag 1 | |
| qualifier_2 | string? | QC flag 2 | |
| qualifier_3 | string? | QC flag 3 | |
| qualifier_4 | string? | QC flag 4 | |
| parameter_remark | string? | Notes | |
| standard_remark | string? | Standard notes | |
| last_modified | datetime | Record timestamp | 2021-04-20 08:52:36 |

**Value Sign Interpretation:**
- null: Exact value
- `<`: Below detection limit (value is the limit)
- `>`: Above measurement range (value is the maximum)

**Cardinality:** ~500,000+ measurements (20-40 per sample event)

### 9. Weather Observation (Contextual)

**Purpose:** Environmental conditions for correlation analysis.

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| station | Station | Nearest WQ station | |
| observation_date | date | Date | 1998-05-27 |
| observation_time | time? | Time if available | |
| weather_station_id | string? | Source station | |
| temperature_c | float? | Air temp | 15.5 |
| temperature_min_c | float? | Daily min | 8.2 |
| temperature_max_c | float? | Daily max | 22.1 |
| precipitation_mm | float? | Precipitation | 0.0 |
| precipitation_type | string? | Rain/snow | |
| wind_speed_kmh | float? | Wind speed | 12.5 |
| wind_direction | string? | Direction | NW |
| humidity_percent | float? | Relative humidity | 65 |
| pressure_kpa | float? | Atm pressure | 101.3 |
| data_source | string | Provider | Environment Canada |

**Linking Strategy:** Weather should be linkable to samples with a days_offset (-1, 0, +1) to capture conditions before/during/after sampling.

---

## Relationship Summary

```
Program ←──M:N──→ Station (via StationProgram junction)
                      │
                      │ 1:N
                      ▼
                 SampleEvent
                      │
                      │ 1:N
                      ▼
                 Measurement
                   │     │
              N:1  │     │  N:1
                   ▼     ▼
             Parameter  LabMethod
                          │
                          │ (is_calculated flag)
                          ▼
                    [calculated vs measured]

Station ──── parent_station ───→ Station (self-reference for hierarchy)

SampleEvent ←──M:N──→ WeatherObservation (via link table with days_offset)
```

---

## Data Quality Considerations

### Detection Limits
- Values below detection limits are flagged with `<` sign
- The reported value IS the detection limit, not the actual measurement
- Different methods have different detection limits for the same parameter

### Calculated vs Measured
- Some values are calculated from other measurements in the same sample
- Example: Hardness = 2.497×Ca + 4.118×Mg
- Important for data quality assessment - calculated values propagate errors

### Holding Time
- Some samples flagged with "HT" (holding time exceeded)
- Sample integrity degrades over time between collection and analysis

### Missing Data
- Some program-year files are essentially empty (3 bytes = header only)
- Gaps in monitoring programs are common

### Unit Variations
- Same unit may appear differently: "mg/L" vs "mg/l"
- Normalize to canonical units during import

---

## Query Patterns to Support

1. **Time Series:** pH at station X from 2010-2020
2. **Spatial:** All stations with elevated phosphorus in date range
3. **Comparison:** Parameter Y across all stations in program Z
4. **Trends:** Monthly averages of conductance by watershed
5. **Correlation:** Parameter values vs weather conditions
6. **Quality Filtering:** Exclude calculated values, show only QC-passed
7. **Aggregation:** Statistics by parameter group, station, or program

---

## Volume Estimates

| Entity | Estimated Records | Growth Rate |
|--------|-------------------|-------------|
| Programs | 5-10 | Rare additions |
| Stations | 230 | Occasional additions |
| Parameters | 100+ | Rare additions |
| Lab Methods | 50+ | Rare additions |
| Lab Qualifiers | 15 | Stable |
| Sample Events | 10,000+ | Ongoing (seasonal) |
| Measurements | 500,000+ | Ongoing (20-40 per event) |
| Weather Obs | 10,000+ | Ongoing (daily per station) |

---

## Storage Recommendations

### High-Volume Entities (Time-Series)
- **Measurements** and **Weather Observations** benefit from time-series optimized storage
- Partitioning by date enables efficient range queries
- Compression important for historical data

### Catalog/Lookup Entities
- **Programs, Stations, Parameters, Methods, Qualifiers** are low-volume
- Standard relational storage appropriate
- Frequently joined with high-volume tables - optimize indexes

### Junction Tables
- **StationProgram** and **SampleWeatherLink** are moderate volume
- Standard relational storage with composite indexes

---

## Open Questions for Other Datasets

When analyzing additional data sources for Luminous, consider:

1. **Temporal Resolution:** Is data collected continuously, daily, seasonally?
2. **Spatial Resolution:** Point locations, transects, areas?
3. **Parameter Overlap:** Do datasets share parameters that need unified definitions?
4. **Quality Frameworks:** Different labs/programs may use different QC codes
5. **Contextual Data Needs:** What environmental factors correlate with measurements?
6. **Calculated Fields:** What derivations are needed and how should they be tracked?

---

## References

- Source Data: Alberta Government Open Data Portal
- Station Metadata: `station_metadata_sw_discrete.csv`
- Qualifier Codes: `sample_metadata_lab_qualifiers.csv`
- CRM Platform Group Patterns: `apps/platform_groups/crm/PATTERNS.md`
