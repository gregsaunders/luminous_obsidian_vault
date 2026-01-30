# Unified Water Quality Data Model for Luminous

**Date:** 2026-01-22
**Purpose:** Consolidate research findings from multiple environmental monitoring datasets to inform a unified, non-over-engineered data model for the Luminous platform.

---

## Executive Summary

Analysis of four government environmental monitoring datasets reveals significant structural overlap despite different source organizations, file formats, and naming conventions. All datasets fundamentally represent the same domain: **water quality measurements at monitored locations over time**.

**Key finding:** A single unified data model can serve all four datasets with minimal source-specific variations. The core entities (Station, Sample, Measurement, Parameter) are essentially identical across sources—only naming conventions and quality flag vocabularies differ.

---

## Datasets Analyzed

| Dataset | Source | Water Type | Records | Parameters | Date Range |
|---------|--------|------------|---------|------------|------------|
| Wetland Surface Water | Alberta OSM | Surface (wetlands) | 18,463 | 250+ | 2017-2025 |
| Surface Water Quality | Alberta Gov | Surface (rivers/streams) | ~500,000+ | ~100 | 1998-2026 |
| Federal Mainstem LTWQM | Environment Canada | Surface (rivers) | ~5,000,000 | 600+ | 2011-2025 |
| JOSM Groundwater | ECCC (Federal) | Groundwater | ~11,000 | 60 | 2009-2011 |

---

## Common Entity Structure

All four datasets share the same fundamental structure:

```
Monitoring Program / Dataset
    └── Station (physical location with GPS coordinates)
        └── Sample Event (field visit at date/time)
            └── Measurement (parameter value with quality flags)
                ├── Parameter (what was measured)
                └── Method (how it was measured)
```

This hierarchy is universal across all environmental monitoring data.

---

## Entity Comparison: Finding the Overlap

### 1. Station (Location)

All datasets have a station/location entity with nearly identical fields:

| Concept | Wetland | Surface WQ | Federal Mainstem | JOSM Groundwater |
|---------|---------|------------|------------------|------------------|
| **ID field** | Station number | station_number | station_code | Master Station ID |
| **Name** | Station name | station_name | station_name | (derived from ID) |
| **Latitude** | Latitude | latitude | Latitude | Latitude |
| **Longitude** | Longitude | longitude | Longitude | Longitude |
| **Site/Region** | Site name | site_name | drainage_region | Assessment Area |
| **Water body** | (in station name) | site_name | river_system | (in station ID) |

**Unified Model:**
```
Station
├── station_code (string, unique) - Government identifier
├── name (string) - Human-readable name
├── latitude (decimal)
├── longitude (decimal)
├── water_body (string) - River/lake/wetland name
├── region (string) - Geographic region or assessment area
├── station_type (enum) - mainstem, tributary, wetland, groundwater
└── data_source (enum) - provincial_surface, federal_mainstem, wetland_osm, josm_groundwater
```

**Observation:** All four datasets use nearly the same structure. The station_code format varies (AB07DA2750 vs AL07DD0004 vs SR-09-001), but this is just a naming convention, not a structural difference.

### 2. Sample Event (Collection Visit)

All datasets represent a sample collection event:

| Concept               | Wetland            | Surface WQ         | Federal Mainstem     | JOSM Groundwater         |
| --------------------- | ------------------ | ------------------ | -------------------- | ------------------------ |
| **ID field**          | Sample Number      | sample_number      | field_sample_number  | (Station + Date + Depth) |
| **Date**              | Sample date        | sample_date        | Sample Date          | Sample Date              |
| **Time**              | Sample time        | sample_time        | (in datetime)        | Sample Time              |
| **Depth**             | Sample final depth | sample_final_depth | Water Depth (m)      | Depth                    |
| **Matrix**            | Sample Matrix      | sample_matrix      | Matrix               | (always WATER)           |
| **Collection method** | Sample Collection  | collection_method  | sample_type          | Station Type             |
| **Lab**               | Laboratory         | laboratory         | (in measurements)    | (in measurements)        |
| **QC flag**           | QC Sample (Y/N)    | is_qc_sample       | (via replicate type) | (via QA flags)           |
| **Comments**          | Sampling comment   | sampling_comment   | -                    | -                        |

**Unified Model:**
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

**Observation:** Essentially identical across all datasets. The only variations are which fields are populated (groundwater has no matrix variation—always water).

### 3. Measurement (Parameter Value)

The core data record—a single analytical result:

| Concept | Wetland | Surface WQ | Federal Mainstem | JOSM Groundwater |
|---------|---------|------------|------------------|------------------|
| **Parameter** | Parameter type name | parameter | parameter | Column header |
| **Value** | Parameter value | value | numeric_value | Cell value |
| **Value sign** | Parameter sign | value_sign | flag_code (L,R) | (via null/BDL) |
| **Unit** | Parameter unit symbol | unit_symbol | unit_symbol | (in column header) |
| **Detection limit** | RDL | detection_limit | MDL + RL | (in metadata) |
| **Method** | Method code | lab_method | analytical_method | Method abbrev |
| **Qualifiers** | Lab Qualifier 1-4 | qualifier_1-4 | flag_code + QA codes | QA flags |

**Unified Model:**
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
├── detection_limit (decimal, nullable) - Primary detection limit
├── reporting_limit (decimal, nullable) - Secondary limit (federal data)
├── method_code (string, nullable)
├── quality_flags (string[]) - Array of qualifier codes
└── remarks (text, nullable)
```

**Observation:** This is the same entity in all four datasets. The federal data has dual detection limits (MDL/RL) while others have a single RDL—easily handled with an optional second field rather than a separate model.

### 4. Parameter (Analyte Catalog)

What is being measured:

| Concept | Wetland | Surface WQ | Federal Mainstem | JOSM Groundwater |
|---------|---------|------------|------------------|------------------|
| **Name** | Parameter type name | name | parameter_name | Column header |
| **Group** | Parameter type group | type_group | category | (derived) |
| **Unit** | Parameter unit name | canonical_unit | unit_of_measure | (in header) |
| **CAS #** | (not present) | (not present) | (in VMV catalog) | (not present) |

**Unified Model:**
```
Parameter
├── parameter_id (string, unique) - Canonical identifier
├── name (string) - Human-readable name
├── category (string) - Major Ions, Trace Metals, PAHs, Nutrients, etc.
├── canonical_unit (string) - Standard unit
├── cas_number (string, nullable) - CAS registry number
└── is_calculated (boolean) - Derived vs measured
```

**Observation:** This is a simple lookup table that all datasets share. The parameter names vary slightly between sources (e.g., "Calcium Dissolved" vs "Ca" vs "Calcium (D-IC)"), but these map to the same underlying analyte. A canonical parameter catalog with source-specific aliases handles this.

### 5. Quality Flags

All datasets have quality control indicators, but with different vocabularies:

| Source | Flag System | Examples |
|--------|-------------|----------|
| Wetland | Lab Qualifier 1-4 | Lab-specific codes |
| Surface WQ | Lab-specific codes | I, K, T, U (AITF-EAS); H, ND, NDR (AXYS) |
| Federal Mainstem | L/R/Q + QA codes | L=below MDL, R=below RL, Q+suffix |
| JOSM Groundwater | Standard env flags | J=estimated, U=non-detect |

**Unified Approach:**
Store quality flags as a string array and maintain a lookup table for interpretation:

```
QualityFlag (reference table)
├── flag_code (string)
├── data_source (enum) - Which source uses this flag
├── meaning (string) - Human-readable description
└── statistical_treatment (enum) - exclude, substitute_half_dl, use_as_is
```

**Observation:** Don't try to normalize all quality flags into one unified scheme. Store the original flags and provide interpretation via lookup. This preserves data fidelity.

---

## What's Actually Different (Not Much)

### Detection Limit Structure
- **Federal data:** Dual limits (MDL + RL)
- **All others:** Single limit (RDL)

**Solution:** Two optional fields in Measurement (`detection_limit` and `reporting_limit`). Provincial data uses only the first.

### File Format
- **Wetland/Surface WQ:** Narrow format (one row per measurement)
- **Federal Mainstem:** Wide format (one row per sample, 600+ parameter columns)
- **JOSM Groundwater:** Wide format with metadata header rows

**Solution:** This is an import/ETL concern, not a data model concern. All formats transform to the same normalized structure.

### Station Code Formats
- Provincial: `AB07DA2750`
- Federal: `AL07DD0004`
- JOSM: `SR-09-001`

**Solution:** Store as-is. The format doesn't affect querying or analysis.

---

## Unnecessary Complexity to Avoid

Based on this analysis, the following would be over-engineering:

1. **Separate tables per data source** - Not needed. One Station, SampleEvent, and Measurement table handles all sources with a `data_source` discriminator.

2. **Complex hierarchies (Program → Site → Station)** - The Wetland data has this, but it's really just station grouping. A simple `region` or `site_name` field on Station suffices.

3. **Separate measurement tables per parameter type** - EAV pattern (one Measurement table) works for all. Don't create separate tables for metals, nutrients, PAHs, etc.

4. **Complex method tracking** - Method is just a string field on Measurement. Don't create elaborate method hierarchy tables unless actually needed for analysis.

5. **Normalized quality flag tables** - Store flags as arrays on Measurement. A simple lookup table for interpretation is enough.

6. **Weather as a separate major entity** - Weather correlation is mentioned in research but isn't in the source data. Add weather integration later if actually needed.

---

## Recommended Unified Model

### Core Entities (Required)

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
│  │ is_calculated│     │ meaning          │                         │
│  └──────────────┘     │ treatment        │                         │
│                       └──────────────────┘                         │
└─────────────────────────────────────────────────────────────────────┘
```

### Supporting Entities (Optional, Add if Needed)

- **ImportBatch** - For data provenance tracking (which file, when imported, by whom)
- **ParameterAlias** - For mapping source-specific parameter names to canonical parameters
- **RegulatoryThreshold** - For automated compliance checking (CCME, Alberta guidelines)
- **Weather** - For environmental correlation (add later if needed)

---

## Import Considerations

### Parameter Mapping Challenge

The same analyte appears under different names:
- "Calcium Dissolved" (Wetland)
- "Calcium Dissolved" (Surface WQ)
- "Ca" (JOSM)
- "Calcium (D-IC)" (JOSM header with method)
- VMV code (Federal)

**Solution:** Build a canonical parameter catalog during import. Create a `ParameterAlias` table only if automated mapping is needed:

```
ParameterAlias
├── alias_name (string) - Source-specific name
├── data_source (enum)
└── canonical_parameter_id (FK → Parameter)
```

### Unit Normalization

Minor variations in unit representation:
- "mg/L" vs "mg/l"
- "µg/L" vs "ug/L" vs "micrograms per liter"

**Solution:** Normalize to canonical units during import. Store only the canonical form.

### Detection Limit as Value

When a measurement is below detection limit:
- The value field contains the detection limit
- The sign field contains '<'

**Solution:** Store both fields. Calculate censored statistics at query time based on user preference (MDL/2, MDL/√2, Kaplan-Meier, etc.).

---

## Volume Estimates (Combined)

| Entity | Estimated Records | Notes |
|--------|-------------------|-------|
| Station | ~500 | All sources combined |
| Parameter | ~700 | Union of all parameter catalogs |
| SampleEvent | ~50,000 | Growing seasonally |
| Measurement | ~10,000,000+ | High-volume table, needs optimization |
| QualityFlag | ~50 | Reference data |

**Storage Implications:**
- Partition Measurement table by year or data_source
- Index on (sample_id, parameter_id) for sample profiles
- Index on (parameter_id, sample_datetime) for time series
- Consider compression for historical data

---

## Conclusion

The four datasets analyzed are **structurally almost identical**. They all represent environmental monitoring data with:
- Locations (stations with coordinates)
- Collection events (samples with dates and metadata)
- Analytical results (measurements with values, units, and quality flags)
- A catalog of parameters (what's being measured)

The differences are superficial:
- Naming conventions (column names, station codes)
- Quality flag vocabularies
- File formats (narrow vs wide CSV)
- Detection limit granularity (single vs dual)

**A single unified data model handles all four sources.** The `data_source` discriminator field allows source-specific queries when needed, while enabling cross-source analysis by default.

This approach avoids:
- Duplicate entity structures
- Source-specific tables that would need to be union-queried
- Complex hierarchies that don't add analytical value
- Over-normalized quality flag systems

The model should be **simple, flat, and queryable**—optimized for the primary use case of time-series analysis and cross-station comparison.

---

## References

- [Wetland Surface Water Quality Data Analysis](Wetland-Surface-Water-Quality-Data-Analysis.md)
- [Surface Water Quality Data Model](Surface-Water-Quality-Data-Model.md)
- [Federal Mainstem Water Quality Data Model](Federal-Mainstem-Water-Quality-Data-Model.md)
- [JOSM Groundwater Data Modeling](Luminous-Data-Modeling-JOSM-Groundwater.md)
