# EPIC-01: Platform Groups & Composable Apps

**Status:** 🟡 Partial
**Priority:** High (Luminous depends on this)
**Owner:** TBD

---

## Vision

Developers can create modular, tenant-installable application bundles that extend the platform without modifying core code.

---

## User Stories

- As a **platform developer**, I can create a new Platform Group following documented patterns
- As a **tenant admin**, I can install Platform Groups to add capabilities to my workspace
- As a **tenant developer**, I can extend installed Platform Groups with custom fields and workflows

---

## Context

Platform Groups are the foundation for all product-specific functionality (Luminous, CRM, etc.). The framework is complete with a CRM reference implementation.

**What exists:** Full data model, installation flow, extension system, UI hints, CRM reference

**What's needed:** Documentation, production testing

**Note:** Luminous Platform Group scaffolding is defined in LUM-EPIC-02 Feature 2.0

---

## Features

### Feature 1.1: Platform Group Documentation

#### Outcome
A developer can build a new Platform Group by following step-by-step documentation.

#### Scope: Owned Files
- `docs/platform-groups/`

#### Tasks
- [ ] Architecture overview
- [ ] Pattern catalog (from CRM PATTERNS.md)
- [ ] Step-by-step guide for new groups

---

### Feature 1.2: Support Luminous Platform Group Review

#### Outcome
Platform team reviews and supports Luminous team's Platform Group implementation to ensure it follows patterns correctly.

#### Context
The Luminous team owns their scaffolding (Luminous EPIC-02 Feature 2.0). This feature provides platform expertise and review.

#### Scope: Owned Files
- None (review/advisory role)

#### Tasks
- [ ] Review Luminous manifest.yaml for pattern compliance
- [ ] Validate ui_hints.yaml schema usage
- [ ] Assist with relationship_types.yaml configuration
- [ ] Provide feedback on integration with platform loader

---

### Feature 1.3: UI Hints Schema Documentation

#### Outcome
A developer can configure dynamic UI generation using documented schema patterns.

#### Scope: Owned Files
- `docs/platform-groups/ui-hints/`

#### Tasks
- [ ] Field types and formats
- [ ] Layout system (col_span, sections)
- [ ] Dynamic form generation patterns

---

### Feature 1.4: Extension System Validation

#### Outcome
Tenant extensions work reliably in production with clear deployment patterns.

#### Scope: Owned Files
- `apps/platform_groups/extensions/`
- `docs/platform-groups/extensions/`

#### Tasks
- [ ] Production testing of tenant extensions
- [ ] Schema migration patterns
- [ ] Extension deployment workflows

---

## Key Files

- `apps/platform_groups/models.py` - Core data models
- `apps/platform_groups/loader.py` - Manifest loading
- `apps/platform_groups/schema_service.py` - UI metadata extraction
- `apps/platform_groups/crm/` - Reference implementation
- `apps/platform_groups/crm/PATTERNS.md` - Design patterns
