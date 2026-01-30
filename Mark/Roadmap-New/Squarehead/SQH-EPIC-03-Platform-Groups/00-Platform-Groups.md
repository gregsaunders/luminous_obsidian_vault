---
status: "In Progress"
priority: "High"
epic_id: "SQH-EPIC-03"
linear_id: "SQU-38"
linear_url: "https://linear.app/squarehead/issue/SQU-38/epic-01-platform-groups-composable-apps"
---

# EPIC-03: Platform Groups & Composable Apps

## Vision

Developers can create modular, tenant-installable application bundles that extend the platform without modifying core code.

## User Stories

- As a **platform developer**, I can create a new Platform Group following documented patterns
- As a **tenant admin**, I can install Platform Groups to add capabilities to my workspace
- As a **tenant developer**, I can extend installed Platform Groups with custom fields and workflows

## Context

Platform Groups are the foundation for all product-specific functionality (Luminous, CRM, etc.). The framework is complete with a CRM reference implementation.

**What exists:** Full data model, installation flow, extension system, UI hints, CRM reference

**What's needed:** Documentation, production testing

**Note:** Luminous Platform Group scaffolding is defined in LUM-EPIC-01 Feature 1.0

## Features

- [[Feature 3.1 Platform Group Documentation]]
- [[Feature 3.2 UI Hints Schema Documentation]]
- [[Feature 3.3 Extension System Validation]]

## Key Files

- `apps/platform_groups/models.py` - Core data models
- `apps/platform_groups/loader.py` - Manifest loading
- `apps/platform_groups/schema_service.py` - UI metadata extraction
- `apps/platform_groups/crm/` - Reference implementation
- `apps/platform_groups/crm/PATTERNS.md` - Design patterns

## Dependencies

**Depends On:** None (foundation layer)

**Used By:**
- [[../SQH-EPIC-02-Unified-Data-Access-Layer/00-Unified-Data-Access-Layer|SQH-EPIC-02]] - Storage backend abstraction
- [[../../Luminous/LUM-EPIC-01-Data-Ingestion/00-Data-Ingestion|LUM-EPIC-01]] - Luminous Platform Group
