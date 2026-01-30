---
status: "Not Started"
priority: "Critical"
assigned: ""
dependencies:
  - "Feature 2.0"
  - "Feature 2.1"
linear_id: "TBD"
---

# Feature 2.3: ETL Pipelines (4 Data Sources)

**Linear:** TBD

---

## Outcome

Data stewards can ingest new data releases from all four sources through a consistent interface, with validation feedback and reconciliation reports.

---

## What Success Looks Like

- Upload Federal Mainstem CSV → data appears in unified model within minutes
- Validation errors show specific rows/columns that failed
- Duplicate detection prevents accidental re-import
- Pipeline dashboard shows ingestion progress and error counts
- Initial 6M row load completes in reasonable time (<1 hour)

---

## Context

Each data source has unique file formats and conventions:
- **Federal Mainstem**: API-based retrieval with pagination
- **Provincial Surface Water**: Annual CSV releases
- **Wetland Monitoring**: Research database exports
- **JOSM Groundwater**: Regulatory submission format

---

## Scope: Owned Files

- `apps/platform_groups/luminous/etl/`
- `apps/platform_groups/luminous/etl/federal.py`
- `apps/platform_groups/luminous/etl/provincial.py`
- `apps/platform_groups/luminous/etl/wetland.py`
- `apps/platform_groups/luminous/etl/josm.py`

---

## Tasks

- [ ] Create base ETL pipeline class with validation, duplicate detection, error handling
- [ ] Implement Federal Mainstem parser (wide-to-narrow transformation)
- [ ] Implement Provincial Surface Water parser
- [ ] Implement Wetland Monitoring parser
- [ ] Implement JOSM Groundwater parser
- [ ] Use PostgreSQL COPY protocol for bulk loading (6M+ rows)
- [ ] Build quarantine table for records failing validation
- [ ] Create reconciliation reports (source counts vs loaded counts)
- [ ] Implement incremental loading for delta updates
- [ ] Build pipeline status dashboard
