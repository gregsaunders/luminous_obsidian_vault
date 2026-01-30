---
status: "Not Started"
priority: "Medium"
epic_id: "SQH-EPIC-08"
linear_id: "SQU-41"
linear_url: "https://linear.app/squarehead/issue/SQU-41"
---

# EPIC-08: Record-Level Access Control

## Vision

Users can be restricted to viewing and editing only records they own, are assigned to, or meet attribute-based conditions—enabling team hierarchies, ownership-based filtering, and fine-grained access to CDC-mirrored data.

## User Stories

- As a **sales manager**, I want my sales reps to only see leads assigned to them
- As a **team admin**, I can define record visibility rules (owner-only, team-wide, role-based)
- As a **compliance officer**, I need audit logs showing who accessed sensitive records
- As an **accountant**, I want to view vendor bills but not customer invoices (attribute-based)
- As a **HR admin**, I want to hide salary fields from non-HR team members

## Context

### Current Security Model

SquareHead has team-level isolation but lacks record-level access control:

| What's Implemented | Status |
|-------------------|--------|
| Authentication (session + JWT) | ✅ Complete |
| Multi-tenancy (Tenant → Team isolation) | ✅ Complete |
| Team roles (Admin, Editor, Viewer) | ✅ Complete |
| API authorization (TeamScopedPermission) | ✅ Complete |
| Platform Group permissions (CRM has 23+) | ✅ Complete |

| What's Missing | Impact |
|---------------|--------|
| Record-level access | Users see ALL records in team |
| Attribute-based filtering | Can't filter CDC data by field values |
| Field-level security | Cannot hide sensitive fields |
| Audit logging | No security event tracking |

### Access Control Models: Terminology

This EPIC implements three complementary access control models:

#### RBAC (Role-Based Access Control)
**"What can users with this role do?"**

Permissions are assigned to **roles**, and users inherit permissions through role membership.

**SquareHead today:** Platform Group permissions (e.g., `crm.leads.view`) are RBAC. The CRM has 23+ permissions assigned via `TenantGroupPermissionGrant`.

**Limitation:** RBAC grants access to *all* records of a type. A Sales Rep can view *all* leads, not just their own.

#### Ownership-Based Access Control
**"Who owns or is assigned to this record?"**

Access is determined by the **relationship** between the user and the record.

**SquareHead today:** Not implemented. All team members see all records.

**Use cases:** Sales territories, support ticket assignment, personal documents.

#### ABAC (Attribute-Based Access Control)
**"What are the properties of this record?"**

Access is determined by **field values** on the record, matched against conditions on the permission.

**SquareHead today:** Not implemented. Permissions don't include attribute conditions.

**Use cases:** CDC-mirrored data where record types share a table, department-specific data, classification levels.

#### How They Work Together

| Model | Question Answered | Applied When |
|-------|------------------|--------------|
| **RBAC** | "Does user have permission X?" | Always (first check) |
| **Ownership** | "Is user related to this record?" | When policy ≠ TEAM_WIDE |
| **ABAC** | "Do record attributes match user's conditions?" | When permission has conditions |

**Evaluation order:**
1. **RBAC check:** Does user have the base permission? (e.g., `invoices.view`)
2. **Ownership check:** If policy requires it, is user owner/assigned?
3. **ABAC check:** If permission has conditions, do record attributes match?

All applicable checks must pass for access to be granted.

### Multi-Storage Architecture Challenge

Data flows through **5+ storage systems**, requiring access control at multiple layers:

| Storage | Purpose | Current Team Isolation |
|---------|---------|----------------------|
| TerminusDB | Document graph (Platform Groups) | ✓ team_id field (optional check) |
| Qdrant | Vector search | ⚠️ bucket_name only |
| Meilisearch | Keyword search | ⚠️ bucket_name only |
| PostgreSQL (Django) | Platform config | ✓ Foreign key to Team |
| PostgreSQL (SQLAlchemy) | Customer data (EPIC-02) | ✓ Per-tenant DB + SQL WHERE |
| MinIO | File storage | ✓ Bucket-per-team |

**Critical Gap:** Qdrant and Meilisearch don't filter by team_id or attribute values.

## Dependencies

**Depends On:**
- [[../SQH-EPIC-03-Platform-Groups/00-Platform-Groups|SQH-EPIC-03]] - Platform Group framework (complete)
- `apps/teams/models.py` - Membership and role system (complete)

**Used By:**
- All Platform Groups requiring per-record access control
- [[../../Luminous/LUM-EPIC-01-Data-Ingestion/00-Data-Ingestion|LUM-EPIC-01]] - Luminous sensor data access rules

## Features

### Phase 1: Ownership-Based Access Control
- [[Feature 8.1 Record Ownership Model]]
- [[Feature 8.2 Ownership Policy Configuration]]
- [[Feature 8.3 Unified Access Control Service]]

### Phase 2: ABAC (Attribute-Based Access Control)
- [[Feature 8.4 ABAC Condition Model]]
- [[Feature 8.5 CDC Field Indexing]]
- [[Feature 8.6 ABAC Evaluator]]

### Phase 3: Storage Layer Integration
- [[Feature 8.7 Qdrant Team + Attribute Filtering]]
- [[Feature 8.8 Meilisearch Team Filtering]]
- [[Feature 8.9 TerminusDB Enforcement]]

### Phase 4: Entry Point Enforcement
- [[Feature 8.10 SearchService Integration]]
- [[Feature 8.11 Agent Tool Enforcement]]
- [[Feature 8.12 API View Updates]]

### Phase 5: Advanced Features
- [[Feature 8.13 Audit Logging]]
- [[Feature 8.14 Field-Level Security]]
- [[Feature 8.15 Sharing & Explicit Grants]]

## Implementation Order

| Phase | Features | Model | Rationale |
|-------|----------|-------|-----------|
| **Phase 1** | 8.1, 8.2, 8.3 | Ownership | Ownership fields + policies + unified service |
| **Phase 2** | 8.4, 8.5, 8.6 | ABAC | Attribute conditions for CDC data filtering |
| **Phase 3** | 8.7, 8.8, 8.9 | All | Wire storage layers (Qdrant, Meilisearch, TerminusDB) |
| **Phase 4** | 8.10, 8.11, 8.12 | All | Enforce at all entry points (API, Agents) |
| **Phase 5** | 8.13, 8.14, 8.15 | — | Advanced features (audit, field security, sharing) |

## References

- `apps/teams/models.py` - Existing team/membership models
- `apps/teams/roles.py` - Role permission functions
- `apps/documents/api/permissions.py` - TeamScopedPermission pattern
- `apps/platform_groups/crm/permissions.py` - Platform Group permission pattern
- `apps/platform_groups/protocols.py` - HookContext definition
