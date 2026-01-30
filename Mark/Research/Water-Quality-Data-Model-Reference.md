# Water Quality Data Model Reference

**Date:** 2026-01-22
**Purpose:** Consolidated reference for unified water quality data modeling across multiple environmental monitoring datasets

---

## Part 1: Design Overview

### Executive Summary

Analysis of four government environmental monitoring datasets reveals they share a **fundamentally identical hierarchical structure**:

```
Program/Project
  └── Station (geographic point)
      └── Sample Event (collection at date/time/depth)
          └── Measurement (parameter value + quality metadata)
```

**Key insight:** A single unified data model serves all four sources without over-engineering. The differences between sources are superficial—naming conventions, quality flag vocabularies, and file formats—not structural.

### Datasets Analyzed

| Source | Type | Stations | Years | Parameters | Measurements |
|--------|------|----------|-------|------------|--------------|
| **Federal Mainstem (LTWQM)** | Surface water | ~10 | 2011-2025 | 600+ | ~5M |
| **Surface Water Quality** | Surface water | 230 | 1998-2026 | 100+ | ~500K |
| **Wetland** | Wetland water | ~50 | 2017-2025 | 250+ | ~18K |
| **JOSM Groundwater** | Groundwater | ~50 | 2009-2011 | 60 | ~11K |

---

### Key Design Decisions

#### 1. Detection Limits: Store Both MDL and RL
Federal data has dual-tier limits (Method Detection Limit + Reporting Limit). Provincial data has single-tier RDL.

**Decision:** Two optional fields (`detection_limit`, `reporting_limit`). Provincial data populates only the first.

#### 2. Method Tracking: At Measurement Level
The same parameter can be measured by different methods (e.g., Metals52 vs Metals56) that aren't directly comparable.

**Decision:** Track method per measurement, not per sample.

#### 3. Calculated Values: Flag, Don't Store Formulas
Some values are derived (e.g., Total Dissolved Solids from ion sum).

**Decision:** Boolean `is_calculated` flag on the method. Don't store calculation formulas.

#### 4. Unit Normalization: Canonical Units on Import
Minor variations exist: "mg/L" vs "mg/l", "µg/L" vs "ug/L".

**Decision:** Normalize to canonical units during import. Store only the canonical form.

#### 5. Quality Flags: Store Raw, Interpret via Lookup
Each source uses different qualifier vocabularies (lab-specific codes).

**Decision:** Store original flags as string array. Maintain a lookup table mapping to canonical meanings (BELOW_DETECTION, ESTIMATED, QC_ISSUE, etc.).

---

### Anti-Patterns to Avoid

| Don't Do This | Why Not | Do This Instead |
|---------------|---------|-----------------|
| Separate station tables per source | Same concept across all sources | Single Station table with `data_source` field |
| Separate measurement tables per source | Same entity everywhere | Single Measurement table with `data_source` field |
| Complex hierarchies (Program → Site → Station) | Adds no analytical value | Simple `region` or `site_name` field on Station |
| Separate tables per parameter type (metals, nutrients, PAHs) | EAV pattern works fine | Single Measurement table with Parameter FK |
| Per-lab qualifier schemas | Over-normalized | Store flags as arrays, lookup for interpretation |
| Complex method hierarchy tables | Not needed for analysis | Simple `method_code` string field |

---

### Volume & Storage Projections

| Entity | Initial Load | Annual Growth |
|--------|-------------|---------------|
| Stations | ~500 | ~10 |
| Parameters | ~700 | ~20 |
| Samples | ~50,000 | ~2,000 |
| Measurements | ~10,000,000+ | ~200K |

**Storage Implications:**
- Partition Measurement table by year or data_source
- Index on `(sample_id)` for sample profiles
- Index on `(parameter_id, sample_datetime)` for time series
- Consider compression for historical partitions

---

## Part 2: Unified Schema

### Visual Schema Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│  ┌──────────────┐     ┌──────────────┐     ┌──────────────────┐    │
│  │   Station    │────▶│ SampleEvent  │────▶│   Measurement    │    │
│  │              │ 1:N │              │ 1:N │                  │    │
│  │ station_code │     │ sample_id    │     │ measurement_id   │    │
│  │ name         │     │ station_id   │     │ sample_id        │    │
│  │ latitude     │     │ datetime     │     │ parameter_id     │    │
│  │ longitude    │     │ depth_m      │     │ numeric_value    │    │
│  │ water_body   │     │ matrix       │     │ text_value       │    │
│  │ region       │     │ collection   │     │ unit             │    │
│  │ station_type │     │ is_qc        │     │ value_sign       │    │
│  │ data_source  │     │ laboratory   │     │ detection_limit  │    │
│  └──────────────┘     │ data_source  │     │ reporting_limit  │    │
│                       └──────────────┘     │ method_code      │    │
│                                            │ quality_flags[]  │    │
│  ┌──────────────┐                          │ remarks          │    │
│  │  Parameter   │◀─────────────────────────│                  │    │
│  │              │ N:1                       └──────────────────┘    │
│  │ parameter_id │                                                   │
│  │ name         │     ┌──────────────────┐                         │
│  │ category     │     │   QualityFlag    │  (reference table)      │
│  │ canonical_   │     │ flag_code        │                         │
│  │   unit       │     │ data_source      │                         │
│  │ cas_number   │     │ meaning          │                         │
│  │ is_calculated│     │ treatment        │                         │
│  └──────────────┘     └──────────────────┘                         │
└─────────────────────────────────────────────────────────────────────┘
```

---

### Station

A physical monitoring location with geographic coordinates.

```
Station
├── station_code (string, unique) - Government identifier (e.g., AB07DA2750)
├── name (string) - Human-readable name
├── latitude (decimal)
├── longitude (decimal)
├── water_body (string) - River/lake/wetland name
├── region (string) - Geographic region or assessment area
├── station_type (enum) - mainstem, tributary, wetland, groundwater
└── data_source (enum) - provincial_surface, federal_mainstem, wetland_osm, josm_groundwater
```

**Note:** Station code formats vary between sources (AB07DA2750 vs AL07DD0004 vs SR-09-001). Store as-is—format doesn't affect querying.

---

### SampleEvent

A field collection visit at a specific date/time/depth.

```
SampleEvent
├── sample_id (string, unique) - Business key
├── station_id (FK → Station)
├── sample_datetime (datetime)
├── sample_depth_m (decimal, nullable)
├── sample_matrix (enum) - WATER, SEDIMENT, BIOTA
├── collection_method (string)
├── is_qc_sample (boolean)
├── laboratory (string, nullable)
├── field_notes (text, nullable)
└── data_source (enum)
```

**Note:** Groundwater data has no matrix variation (always WATER). The field is nullable or defaults appropriately.

---

### Measurement

A single analytical result—the core data record.

```
Measurement
├── measurement_id (UUID)
├── sample_id (FK → SampleEvent)
├── parameter_id (FK → Parameter)
├── numeric_value (decimal, nullable)
├── text_value (string, nullable) - For non-numeric codes (DE, IS, FC, etc.)
├── is_numeric (boolean)
├── unit (string)
├── value_sign (enum) - null, '<', '>'
├── detection_limit (decimal, nullable) - Primary detection limit (RDL or MDL)
├── reporting_limit (decimal, nullable) - Secondary limit (federal RL only)
├── method_code (string, nullable)
├── quality_flags (string[]) - Array of qualifier codes
└── remarks (text, nullable)
```

**Detection Limit Handling:** When a measurement is below detection limit, the value field contains the detection limit and the sign field contains '<'. Calculate censored statistics at query time based on user preference (MDL/2, MDL/√2, Kaplan-Meier, etc.).

---

### Parameter

The analyte catalog—what is being measured.

```
Parameter
├── parameter_id (string, unique) - Canonical identifier
├── name (string) - Human-readable name
├── category (string) - Major Ions, Trace Metals, PAHs, Nutrients, etc.
├── canonical_unit (string) - Standard unit
├── cas_number (string, nullable) - CAS registry number
└── is_calculated (boolean) - Derived vs measured
```

**Note:** Parameter names vary between sources ("Calcium Dissolved" vs "Ca" vs "Calcium (D-IC)"). These map to the same underlying analyte. Use ParameterAlias for automated mapping if needed.

---

### Supporting Entities

#### QualityFlag (Reference Table)
Maps raw qualifier codes to canonical meanings.

```
QualityFlag
├── flag_code (string)
├── data_source (enum) - Which source uses this flag
├── meaning (string) - Human-readable description
└── statistical_treatment (enum) - exclude, substitute_half_dl, use_as_is
```

#### ParameterAlias (Optional)
For automated mapping of source-specific parameter names.

```
ParameterAlias
├── alias_name (string) - Source-specific name
├── data_source (enum)
└── canonical_parameter_id (FK → Parameter)
```

#### ImportBatch (Optional)
For data provenance tracking.

```
ImportBatch
├── batch_id (UUID)
├── source_file (string)
├── import_datetime (datetime)
├── record_count (integer)
└── notes (text)
```

#### RegulatoryThreshold (Optional)
For automated compliance checking.

```
RegulatoryThreshold
├── parameter_id (FK → Parameter)
├── threshold_value (decimal)
├── threshold_type (string) - CCME, Alberta_Tier1, etc.
└── water_use (string) - aquatic_life, drinking, irrigation
```

---

## Part 3: Technical Reference

### Column Mapping: Location Fields

| Concept | Federal Mainstem | JOSM Groundwater | Surface WQ | Wetland |
|---------|------------------|------------------|------------|---------|
| Station ID | Station Number/Code | Station ID | Station number | Station number |
| Station Name | Station or Location Name | (derived from ID) | Station name | Station name |
| Site/Water Body | (in station name) | Assessment Area | Site name | Site name |
| Latitude | Latitude | Latitude | Latitude | Latitude |
| Longitude | Longitude | Longitude | Longitude | Longitude |

---

### Column Mapping: Sample Fields

| Concept | Federal Mainstem | JOSM Groundwater | Surface WQ | Wetland |
|---------|------------------|------------------|------------|---------|
| Sample ID | Field Sample Number | (Station+Date+Depth) | Sample number | Sample number |
| Sample Date | Sample Date/DateTime | Sample Date | Sample date | Sample date |
| Sample Time | (in DateTime) | Sample Time | Sample time | Sample time |
| Sample Depth | Water Depth (m) | Depth | Sample depth | Sample final depth |
| Matrix | Matrix | (implicit: groundwater) | Sample Matrix | Sample Matrix |
| Collection Method | Sample Type | (implicit) | Sample Collection | Sample Collection |
| Laboratory | (in measurements) | (in measurements) | Laboratory | Laboratory |
| QC Flag | (via replicate type) | (via QA flags) | QC Sample (Y/N) | QC Sample (Y/N) |

---

### Column Mapping: Measurement Fields

| Concept | Federal Mainstem | JOSM Groundwater | Surface WQ | Wetland |
|---------|------------------|------------------|------------|---------|
| Parameter Name | (column header) | (column header) | Parameter type name | Parameter type name |
| Parameter Group | (file category) | (D-MS, D-IC, etc.) | Parameter type group | Parameter type group |
| Value | (numeric value) | (numeric value) | Parameter value | Parameter value |
| Value Sign | (implicit in flag) | (implicit) | Parameter sign | Parameter sign |
| Unit | (from VMV catalog) | (from header) | Parameter unit symbol | Parameter unit symbol |
| Detection Limit | MDL, RL | (from method) | RDL | RDL |
| Method | Analytical Method | (D-MS, D-IC, SFS) | Analysis method name | Parameter method |
| Quality Flags | Flag column (L/R/Q) | (standard flags) | Lab Qualifier 1-4 | Lab Qualifier 1-4 |

---

### Quality Flag Vocabularies

#### Federal Mainstem Flags

| Flag | Meaning |
|------|---------|
| L | Below Method Detection Limit (MDL) |
| R | Below Reporting Limit (RL) |
| Q + suffix | QA/QC issue (e.g., QEventL = lab contamination) |

#### JOSM Groundwater Flags

| Flag | Meaning |
|------|---------|
| J | Estimated value |
| U | Non-detect |

#### Provincial Lab Flags (Surface WQ & Wetland)

| Lab | Flags | Meanings |
|-----|-------|----------|
| AITF-EAS | I, K, T, U | Lab-specific qualifiers |
| AXYS | H, ND, NDR, NQ | H=hold issue, ND=non-detect, NDR=non-detect reported, NQ=not qualified |

**Note:** Store all flags as-is in the `quality_flags` array. Use QualityFlag reference table to interpret when needed.

---

### Detection Limit Approaches

| Source | Approach | Fields | Notes |
|--------|----------|--------|-------|
| **Federal Mainstem** | Dual-tier | MDL + RL | MDL is analytical limit, RL is reporting threshold |
| **Surface WQ** | Single-tier | RDL + sign | Sign indicates < or > |
| **Wetland** | Single-tier | RDL + sign | Same as Surface WQ |
| **JOSM Groundwater** | Implicit | flag or null | Below detection indicated by flag or null value |

**Unified approach:** Store both `detection_limit` (MDL or RDL) and `reporting_limit` (RL only). For single-tier sources, populate only `detection_limit`.

---

### Parameter Overlap

#### Parameters Common to ALL Sources

| Parameter | Units | Notes |
|-----------|-------|-------|
| **Major Ions** | | |
| Calcium (Ca) | mg/L | Dissolved form |
| Magnesium (Mg) | mg/L | Dissolved form |
| Sodium (Na) | mg/L | Dissolved form |
| Potassium (K) | mg/L | Dissolved form |
| Chloride (Cl) | mg/L | |
| Sulphate (SO4) | mg/L | |
| Alkalinity | mg/L as CaCO3 | |
| **Trace Metals** | | |
| Aluminum (Al) | µg/L | Total/dissolved |
| Arsenic (As) | µg/L | |
| Barium (Ba) | µg/L | |
| Cadmium (Cd) | µg/L | |
| Chromium (Cr) | µg/L | |
| Copper (Cu) | µg/L | |
| Iron (Fe) | µg/L | Total/dissolved |
| Lead (Pb) | µg/L | |
| Manganese (Mn) | µg/L | |
| Nickel (Ni) | µg/L | |
| Selenium (Se) | µg/L | |
| Zinc (Zn) | µg/L | |
| **Nutrients** | | |
| Total Nitrogen | mg/L | |
| Total Phosphorus | mg/L | |
| Ammonia | mg/L | |
| Nitrate | mg/L | |
| **Field Measurements** | | |
| pH | pH units | |
| Temperature | °C | |
| Conductivity | µS/cm | |
| Dissolved Oxygen | mg/L | |

#### Specialized Parameters by Source

| Source | Unique Parameters |
|--------|------------------|
| **Federal Mainstem** | PAHs (50+), Alkylated PAHs (100+), BTEX, Mercury (6 types), Rare earth elements |
| **JOSM Groundwater** | SFS wavelengths (282nm, 320nm, 333nm), ORP |
| **Surface WQ** | Chlorophyll A, BOD, Color, Turbidity |
| **Wetland** | Hydrocarbons (F2, F3, F4 fractions), Sulfide |

---

### Import Considerations

#### Wide-to-Narrow Transformation
Federal Mainstem data requires EAV transformation (600+ parameter columns → rows). All other sources are already in narrow format.

#### Parameter Name Mapping Examples

| Source Name | Canonical Parameter |
|-------------|---------------------|
| Calcium Dissolved (Wetland) | Calcium_Dissolved |
| Calcium Dissolved (Surface WQ) | Calcium_Dissolved |
| Ca (JOSM) | Calcium_Dissolved |
| Calcium (D-IC) (JOSM header) | Calcium_Dissolved |
| VMV code 12345 (Federal) | Calcium_Dissolved |

#### Unit Normalization Rules

| Source Format | Canonical Format |
|---------------|------------------|
| mg/l | mg/L |
| ug/L | µg/L |
| micrograms per liter | µg/L |
| deg C | °C |
| uS/cm | µS/cm |

---

## Source Documents

This reference consolidates findings from:
- [Federal Mainstem Water Quality Data Model](Federal-Mainstem-Water-Quality-Data-Model.md)
- [JOSM Groundwater Data Modeling](Luminous-Data-Modeling-JOSM-Groundwater.md)
- [Surface Water Quality Data Model](Surface-Water-Quality-Data-Model.md)
- [Wetland Surface Water Quality Analysis](Wetland-Surface-Water-Quality-Data-Analysis.md)
- [Luminous Unified Water Quality Data Model](Luminous-Unified-Water-Quality-Data-Model.md)
- [Unified Water Quality Data Model](Unified-Water-Quality-Data-Model.md)
