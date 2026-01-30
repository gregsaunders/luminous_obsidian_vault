# Luminous Unified Water Quality Data Model Research

**Date:** 2026-01-22
**Purpose:** Consolidated analysis of 4 environmental monitoring datasets for unified data modeling

---

## Executive Summary

All four datasets share a **fundamentally identical hierarchical structure**:

```
Program/Project
  └── Station/Site (geographic point)
      └── Sample Event (collection at date/time/depth)
          └── Measurement (parameter value + quality metadata)
```

The differences are primarily in:
1. **Column naming** (cosmetic - same concepts, different labels)
2. **Parameter breadth** (60 to 600+ parameters)
3. **Quality flag vocabularies** (lab-specific codes)
4. **Detection limit handling** (single vs dual-tier)

**Key insight:** A single unified data model can serve all four sources without over-engineering.

---

## Data Source Summary

| Source | Type | Stations | Years | Parameters | Measurements |
|--------|------|----------|-------|------------|--------------|
| **Federal Mainstem** | Surface water | ~10 | 2011-2025 | 600+ | ~5M |
| **JOSM Groundwater** | Groundwater | ~50 | 2009-2011 | 60 | ~11K |
| **Surface Water Quality** | Surface water | 230 | 1998-2026 | 100+ | ~500K |
| **Wetland** | Wetland water | ~50 | 2017-2025 | 250+ | ~18K |

---

## Column Mapping: Same Concept, Different Names

### Location Fields

| Concept | Federal | JOSM | Surface WQ | Wetland |
|---------|---------|------|------------|---------|
| Station ID | Station Number/Code | Station ID | Station number | Station number |
| Station Name | Station or Location Name | (derived from ID) | Station name | Station name |
| Site/Water Body | (in station name) | Assessment Area | Site name | Site name |
| Latitude | Latitude | Latitude | Latitude | Latitude |
| Longitude | Longitude | Longitude | Longitude | Longitude |

### Sample Fields

| Concept | Federal | JOSM | Surface WQ | Wetland |
|---------|---------|------|------------|---------|
| Sample ID | Field Sample Number | (Station+Date+Depth) | Sample number | Sample number |
| Sample Date | Sample Date/DateTime | Sample Date | Sample date | Sample date |
| Sample Time | (in DateTime) | Sample Time | Sample time | Sample time |
| Sample Depth | Water Depth (m) | Depth | Sample depth | Sample final depth |
| Matrix | Matrix | (implicit: groundwater) | Sample Matrix | Sample Matrix |
| Collection Method | Sample Type | (implicit) | Sample Collection | Sample Collection |

### Measurement Fields

| Concept | Federal | JOSM | Surface WQ | Wetland |
|---------|---------|------|------------|---------|
| Parameter Name | (column header) | (column header) | Parameter type name | Parameter type name |
| Parameter Group | (file category) | (D-MS, D-IC, etc.) | Parameter type group | Parameter type group |
| Value | (numeric value) | (numeric value) | Parameter value | Parameter value |
| Value Sign | (implicit in flag) | (implicit) | Parameter sign | Parameter sign |
| Unit | (from VMV catalog) | (from header) | Parameter unit symbol | Parameter unit symbol |
| Detection Limit | MDL, RL | (from method) | RDL | RDL |
| Method | Analytical Method | (D-MS, D-IC, SFS) | Analysis method name | Parameter method |
| Quality Flags | Flag column (L/R/Q) | (standard flags) | Lab Qualifier 1-4 | Lab Qualifier 1-4 |

---

## Overlapping Parameters

### Parameters Common to ALL Sources

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

### Specialized Parameters by Source

| Source | Unique Parameters |
|--------|------------------|
| **Federal** | PAHs (50+), Alkylated PAHs (100+), BTEX, Mercury (6 types), Rare earth elements |
| **JOSM** | SFS wavelengths (282nm, 320nm, 333nm), ORP |
| **Surface WQ** | Chlorophyll A, BOD, Color, Turbidity |
| **Wetland** | Hydrocarbons (F2, F3, F4 fractions), Sulfide |

---

## Quality Flag Systems

### Detection Limit Approaches

| Source | Approach | Fields |
|--------|----------|--------|
| **Federal** | Dual-tier | MDL (Method Detection Limit) + RL (Reporting Limit) |
| **JOSM** | Implicit | Below detection = null or flag |
| **Surface WQ** | Single-tier | RDL + sign (<, >) |
| **Wetland** | Single-tier | RDL + sign (<, >) |

**Unified approach:** Store both MDL and RDL where available; use single RDL field for sources with one limit.

### Quality Flag Vocabularies

| Source | Flags | Examples |
|--------|-------|----------|
| **Federal** | L, R, Q + QA codes | L (below MDL), R (below RL), QEventL (lab contamination) |
| **JOSM** | Standard environmental | J (estimated), U (non-detect) |
| **Surface WQ** | Lab-specific (15 codes) | I, K, T, U (AITF); H, ND, NDR, NQ (AXYS) |
| **Wetland** | Lab-specific (4 fields) | Same as Surface WQ |

**Unified approach:** Store raw qualifier codes; create lookup table mapping to canonical meanings (BELOW_DETECTION, ESTIMATED, QC_ISSUE, etc.)

---

## What NOT to Over-Engineer

### 1. Separate Station Tables per Source
**Don't do this.** All four sources have the same station concept: a geographic point with coordinates and a name/code.

**Unified station table:**
- `station_code` (unique across all sources)
- `station_name`
- `latitude`, `longitude`
- `source` (federal, provincial, josm, wetland)
- `water_body_type` (surface, groundwater, wetland)

### 2. Separate Measurement Tables per Source
**Don't do this.** All sources produce the same thing: a parameter value at a sample event.

**Unified measurement table:**
- `sample_id` (FK to sample)
- `parameter_id` (FK to parameter catalog)
- `value`, `value_sign`
- `method_id` (FK to method)
- `detection_limit`, `detection_limit_type` (MDL vs RDL)
- `qualifiers` (JSONB array)

### 3. Complex Parameter Hierarchies
**Don't do this.** Parameters are flat: a name, a unit, and optionally a category/group.

**Unified parameter table:**
- `parameter_code` (canonical identifier)
- `parameter_name`
- `parameter_group` (Major Ions, Trace Metals, PAHs, etc.)
- `canonical_unit`
- `cas_number` (for chemicals)

### 4. Per-Lab Qualifier Schemas
**Don't do this.** Store qualifiers as-is; normalize meaning via lookup when needed.

---

## Recommended Unified Schema

### Core Entities

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Station   │     │  Parameter  │     │   Method    │
│             │     │             │     │             │
│ code (PK)   │     │ code (PK)   │     │ code (PK)   │
│ name        │     │ name        │     │ name        │
│ lat/lon     │     │ group       │     │ description │
│ source      │     │ unit        │     │ is_calcul.  │
│ water_type  │     │ cas_number  │     └─────────────┘
└──────┬──────┘     └──────┬──────┘
       │                   │
       │ 1:N               │ N:1
       ▼                   │
┌─────────────┐            │
│   Sample    │            │
│             │            │
│ id (PK)     │            │
│ station_id  │            │
│ date/time   │            │
│ depth       │            │
│ matrix      │            │
│ source_file │            │
└──────┬──────┘            │
       │                   │
       │ 1:N               │
       ▼                   ▼
┌────────────────────────────┐
│       Measurement          │
│                            │
│ id (PK)                    │
│ sample_id (FK)             │
│ parameter_id (FK)          │
│ method_id (FK)             │
│ value                      │
│ value_sign (<, >, =)       │
│ mdl, rl                    │
│ qualifiers (JSONB)         │
│ lab_name                   │
└────────────────────────────┘
```

### Reference Tables

- **QualifierLookup:** Maps raw qualifier codes to canonical meanings
- **DataSource:** Tracks import provenance (file, date, program)
- **RegulatoryStandard:** Thresholds for compliance checking

---

## Key Design Decisions

### 1. Single vs Dual Detection Limits
Store **both** MDL and RL fields. For sources with single RDL, populate RL only.

### 2. Method Tracking Granularity
Track at **measurement level** (not sample level) because:
- Federal data has Metals52 vs Metals56 that aren't comparable
- Same parameter can have multiple methods

### 3. Wide-to-Narrow Transformation
Federal data requires EAV transformation (600+ columns → rows). All other sources are already narrow.

### 4. Calculated Values
Flag with `is_calculated` on method. Don't store calculation formulas - just track that it's derived.

### 5. Unit Normalization
Normalize to canonical units on import (mg/L not mg/l). Store original unit for audit.

---

## Volume Projections

| Entity | Initial Load | Annual Growth |
|--------|-------------|---------------|
| Stations | ~340 | ~10 |
| Parameters | ~700 | ~20 |
| Samples | ~25,000 | ~2,000 |
| Measurements | ~6M | ~200K |

**Implication:** Measurements table needs:
- Time-series partitioning (by year)
- Indexes on (sample_id), (parameter_id, sample_date)
- Compression for historical partitions

---

## Source Documents

This analysis consolidates findings from:
- [Federal Mainstem Water Quality Data Model](Federal-Mainstem-Water-Quality-Data-Model.md)
- [JOSM Groundwater Data Modeling](Luminous-Data-Modeling-JOSM-Groundwater.md)
- [Surface Water Quality Data Model](Surface-Water-Quality-Data-Model.md)
- [Wetland Surface Water Quality Analysis](Wetland-Surface-Water-Quality-Data-Analysis.md)
