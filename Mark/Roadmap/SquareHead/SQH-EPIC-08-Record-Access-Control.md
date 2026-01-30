---
linear_id: SQU-41
linear_url: https://linear.app/squarehead/issue/SQU-41
---

# EPIC-08: Record-Level Access Control

**Linear:** [SQU-41](https://linear.app/squarehead/issue/SQU-41)
**Status:** 🔴 Not Started
**Priority:** Medium (needed before multi-user production deployments)
**Owner:** TBD

---

## Vision

Users can be restricted to viewing and editing only records they own, are assigned to, or meet attribute-based conditions—enabling team hierarchies, ownership-based filtering, and fine-grained access to CDC-mirrored data.

---

## User Stories

- As a **sales manager**, I want my sales reps to only see leads assigned to them
- As a **team admin**, I can define record visibility rules (owner-only, team-wide, role-based)
- As a **compliance officer**, I need audit logs showing who accessed sensitive records
- As an **accountant**, I want to view vendor bills but not customer invoices (attribute-based)
- As a **HR admin**, I want to hide salary fields from non-HR team members

---

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

This EPIC implements three complementary access control models. Understanding the differences is critical for correct implementation.

#### RBAC (Role-Based Access Control)
**"What can users with this role do?"**

Permissions are assigned to **roles**, and users inherit permissions through role membership.

```
Role: Sales Rep
├── Can view leads ✓
├── Can edit leads ✓
├── Can delete leads ✗
└── Can view reports ✗
```

**SquareHead today:** Platform Group permissions (e.g., `crm.leads.view`) are RBAC. The CRM has 23+ permissions assigned via `TenantGroupPermissionGrant`.

**Limitation:** RBAC grants access to *all* records of a type. A Sales Rep can view *all* leads, not just their own.

#### Ownership-Based Access Control
**"Who owns or is assigned to this record?"**

Access is determined by the **relationship** between the user and the record.

```
Record: Lead #123
├── owned_by: alice@example.com
├── assigned_to: [bob@example.com, charlie@example.com]
└── created_by: alice@example.com

Policy: ASSIGNED_ONLY
├── alice can access ✓ (owner)
├── bob can access ✓ (assigned)
├── charlie can access ✓ (assigned)
└── dave cannot access ✗ (not owner/assigned)
```

**SquareHead today:** Not implemented. All team members see all records.

**Use cases:** Sales territories, support ticket assignment, personal documents.

#### ABAC (Attribute-Based Access Control)
**"What are the properties of this record?"**

Access is determined by **field values** on the record, matched against conditions on the permission.

```
Permission: invoices.view
└── Condition: invoice_type IN ["vendor_bill"]

Record: Invoice #456 (invoice_type = "vendor_bill")     → Accountant can see ✓
Record: Invoice #789 (invoice_type = "customer_invoice") → Accountant cannot see ✗
```

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

### PostgreSQL Usage: Two Distinct Roles

SquareHead uses PostgreSQL in **two different ways**—this distinction is critical for understanding access control:

| PostgreSQL Role | ORM | Database | Data Type | Access Control |
|-----------------|-----|----------|-----------|----------------|
| **Platform Config** | Django ORM | Shared `confluent` DB | Users, Tenants, Teams, CDC configs, Permissions | Django QuerySet `.filter()` |
| **Customer Data** ([EPIC-02](SQH-EPIC-02-Unified-Data-Access-Layer.md)) | SQLAlchemy | Per-tenant `sqh_tenant_{slug}` | High-volume Platform Group models (e.g., lab results) | SQL WHERE clauses via `AccessContext` |

**Key points:**
- Django ORM is **only** for platform configuration—not customer/tenant business data
- Customer data in PostgreSQL uses **separate per-tenant databases** accessed via SQLAlchemy
- Platform Group models can choose their backend: TerminusDB (graph) or PostgreSQL (relational) - see [EPIC-02](SQH-EPIC-02-Unified-Data-Access-Layer.md)
- The `PlatformGroupRecordService` routes to the appropriate backend based on model's `_storage` config

### Multi-Storage Architecture Challenge

Data flows through **5+ storage systems**, requiring access control at multiple layers:

| Storage | Purpose | Current Team Isolation |
|---------|---------|----------------------|
| TerminusDB | Document graph (Platform Groups) | ✓ team_id field (optional check) |
| Qdrant | Vector search | ⚠️ bucket_name only |
| Meilisearch | Keyword search | ⚠️ bucket_name only |
| PostgreSQL (Django) | Platform config | ✓ Foreign key to Team |
| PostgreSQL (SQLAlchemy) | Customer data ([EPIC-02](SQH-EPIC-02-Unified-Data-Access-Layer.md)) | ✓ Per-tenant DB + SQL WHERE |
| MinIO | File storage | ✓ Bucket-per-team |

**Critical Gap:** Qdrant and Meilisearch don't filter by team_id or attribute values.

#### Data Flow Diagram

![[assets/access-control-data-flow.svg]]
*Data flow diagram showing access control enforcement points. User path (left, green) has team isolation but lacks ABAC and ownership filtering. Agent path (right, orange) has critical gaps—context is available but tools ignore it, resulting in unfiltered queries.*

### Storage-Specific Implementation Strategies

Access control implementation differs by storage system. **Django QuerySets are NOT universally applicable**—only PostgreSQL-backed models support them.

| Storage | Data Access Pattern | Access Control Strategy |
|---------|--------------------|-----------------------|
| **PostgreSQL** | Django ORM QuerySet | `AccessFilteredQuerySet` mixin with `.filter()` |
| **TerminusDB (Documents)** | `DocumentGraphAPI` returns `dict` | WOQL query conditions + post-fetch filtering |
| **TerminusDB (Platform Groups)** | `PlatformGroupRecordService` returns `list[dict]` | WOQL query conditions in `list()` and `search()` |
| **Qdrant** | Vector search returns payloads | Payload filters (`team_id`, attribute fields) |
| **Meilisearch** | Keyword search returns documents | Filter expressions (`team_id = "x"`) |
| **MinIO** | Bucket-per-team | Bucket naming convention (no change needed) |

#### Platform Group Records: No QuerySet Available

`PlatformGroupRecordService` ([record_service.py:14](apps/platform_groups/record_service.py#L14)) returns Python dictionaries, not Django QuerySets:

```python
# Current implementation - returns dict, not QuerySet
def get(self, ...) -> dict[str, Any] | None:
    return client.get_document(record_id)  # Returns JSON dict

def list(self, ...) -> list[dict[str, Any]]:
    return list(client.query_document(query))  # Returns list of dicts
```

**Implication:** Cannot use `.filter(owned_by=user)` on results. Access control must be implemented via:

1. **WOQL Query Conditions** - Add filters to the WOQL query before execution
2. **Post-Fetch Filtering** - Filter `list[dict]` results (less efficient for large datasets)
3. **Service Wrapper** - `DocumentAccessControl` filters results after retrieval

#### Recommended Approach per Data Type

| Data Type | Approach | Implementation |
|-----------|----------|----------------|
| **Django Models** (Teams, CDC configs) | QuerySet filtering | `AccessFilteredQuerySet.for_user()` |
| **Platform Group Records** (CRM, Luminous) | WOQL query + service wrapper | Extend `PlatformGroupRecordService.list()` with access filters |
| **Document Search Results** | Storage-level + post-fetch | Qdrant/Meilisearch filters + `DocumentAccessControl.filter_documents()` |
| **CDC-Mirrored Records** | Attribute-based filters | ABAC conditions pushed to Qdrant/Meilisearch |

### Why ABAC is Required for CDC Data

CDC-mirrored records from external systems (ERPs, databases) often use a single table for multiple record types distinguished by a field value. Traditional RBAC cannot filter these—ABAC is required.

See the [ABAC definition above](#abac-attribute-based-access-control) for the invoice example.

**Depends On:**
- [SQH-EPIC-03](SQH-EPIC-03-Platform-Groups.md) - Platform Group framework (complete)
- `apps/teams/models.py` - Membership and role system (complete)

**Used By:**
- All Platform Groups requiring per-record access control
- [LUM-EPIC-01](../Luminous/LUM-EPIC-01-Data-Ingestion.md) - Luminous sensor data access rules

---

## Features

### Phase 1: Ownership-Based Access Control

#### Feature 8.1: Record Ownership Model
**Status:** 🔴 Not Started
**Priority:** High

##### Outcome
Every record has an owner and optional assignees, enabling ownership-based filtering.

##### Scope: Owned Files
- `apps/platform_groups/loader.py` - Manifest loader (inject ownership fields)
- `apps/platform_groups/record_service.py` - Auto-populate created_by on create
- `apps/platform_groups/models.py` - Django mixin (for PostgreSQL models only)

##### Requirements

**Schema-Level Ownership Fields:**

Platform Group records are stored in TerminusDB, not Django ORM. A Django mixin cannot add fields to TerminusDB documents. Instead, ownership fields must be injected during schema loading.

- Ownership fields (`created_by`, `owned_by`, `assigned_to`) are injected into `ManifestModel` objects within `loader.py` before TerminusDB schema generation
- In-memory model representation is modified after loading from `manifest.yaml`
- Ownership field types are defined in base schema (user reference fields)
- `created_by` is auto-populated in `PlatformGroupRecordService.create()` from `HookContext.user_id`
- `assigned_to` supports multiple assignees as array field
- Migration note: pre-production, no data migration needed

**Django Model Ownership (PostgreSQL-backed models only):**
- `OwnedModelMixin` provides ownership fields for Django models (CDC configs, Teams, etc.)
- This mixin is NOT used for Platform Group records

**Ownership Transfer:**
- API endpoint transfers ownership via `PlatformGroupRecordService.update()`
- Bulk ownership reassignment is available via WOQL update query
- Ownership transfer permission is checked before allowing transfer

---

#### Feature 8.2: Ownership Policy Configuration
**Status:** 🔴 Not Started
**Priority:** High

##### Outcome
Team admins can define ownership-based visibility policies that determine which records users can see based on their relationship to the record (owner, assignee, etc.).

##### Scope: Owned Files
- `apps/teams/access_policies.py` - Policy definitions
- `apps/teams/models.py` - Policy storage

##### Requirements

**Ownership Policy Model:**
- `OwnershipPolicy` model supports four policy types:
  - `TEAM_WIDE` - All team members see all records (current behavior, no ownership check)
  - `OWNER_ONLY` - Users see only records where `owned_by = user`
  - `ASSIGNED_ONLY` - Users see records where `owned_by = user` OR `user IN assigned_to`
  - `HIERARCHICAL` - Managers see subordinates' records (requires org hierarchy)
- Policies are attached per team (not per-Platform-Group)
- Default policy is TEAM_WIDE (maintains current behavior)

**Ownership Evaluation:**
- `OwnershipEvaluator` class evaluates ownership-based filtering
- `WOQLOwnershipFilter` builds WOQL query conditions from policy:
  ```python
  # Example: ASSIGNED_ONLY policy generates this WOQL fragment
  WOQL().woql_or(
      WOQL().triple("v:Doc", "owned_by", user_id),
      WOQL().triple("v:Doc", "assigned_to", user_id),
  )
  ```
- `QuerySetOwnershipFilter` handles Django models (PostgreSQL only)
- Ownership checks integrate with RBAC permission checks

---

#### Feature 8.3: Unified Access Control Service
**Status:** 🔴 Not Started
**Priority:** High

##### Outcome
A centralized service that combines RBAC, Ownership, and ABAC checks across all storage systems.

##### Scope: Owned Files
- `apps/documents/access_control.py` - **CREATE** new file

##### Requirements

- `AccessControlService` class holds user + team context
- `check_access(user, permission, record)` performs combined RBAC + Ownership + ABAC check
- `filter_records(records, user, permission)` provides batch filtering for lists
- Service integrates with `OwnershipPolicy` and `AttributeCondition`
- Caching layer improves performance for permission and policy lookups

---

### Phase 2: ABAC (Attribute-Based Access Control)

#### Feature 8.4: ABAC Condition Model
**Status:** 🔴 Not Started
**Priority:** High

##### Outcome
RBAC permissions can include attribute conditions that filter records by field values. This extends the existing permission system without replacing it.

##### Scope: Owned Files
- `apps/platform_groups/permissions.py` - Permission model extension

##### Requirements

**Attribute Condition Model:**
- `AttributeCondition` dataclass contains field, operator, and values:
  ```python
  @dataclass(frozen=True)
  class AttributeCondition:
      field: str           # "invoice_type"
      operator: str        # "equals", "in", "not_in", "contains"
      values: list[str]    # ["vendor_bill"]
  ```
- Supported operators are: `equals`, `not_equals`, `in`, `not_in`, `contains`

**Permission Grant with Conditions:**
- `TenantGroupPermissionGrant.attribute_conditions` JSON field is available (optional)
- When conditions are present, ABAC filtering applies *in addition to* RBAC check
- Admin-only UI allows defining conditions
- Condition fields are validated against source schema

---

#### Feature 8.5: CDC Field Indexing
**Status:** 🔴 Not Started
**Priority:** High

##### Outcome
CDC-mirrored records include designated fields in search indexes for filtering.

##### Scope: Owned Files
- `apps/cdc/models.py` - ConnectorTableConfig.field_mapping usage
- `apps/documents/graph/consistency.py` - Qdrant payload creation
- `apps/cdc/assembly/` - Field extraction during assembly

##### Requirements

**Connector Configuration:**
- `field_mapping` schema defines access control fields:
  ```json
  {
    "access_control_fields": ["invoice_type", "department"],
    "index_for_search": ["invoice_type", "status"]
  }
  ```
- Field names are validated against source schema

**Indexing Pipeline:**
- Access control fields are extracted during CDC assembly
- Fields are included in Qdrant payloads during chunk indexing
- Fields are included in Meilisearch documents

---

#### Feature 8.6: ABAC Evaluator
**Status:** 🔴 Not Started
**Priority:** High

##### Outcome
Attribute conditions from the user's permissions are evaluated at query time to filter results. Works alongside RBAC and Ownership checks.

##### Scope: Owned Files
- `apps/documents/access_control.py` - Extend with ABAC

##### Requirements

- `ABACEvaluator` class handles condition evaluation
- `get_user_conditions(user, permission)` extracts conditions from granted permissions

**Storage-Native Filtering (preferred - push to database):**
- `WOQLConditionBuilder` converts `AttributeCondition` to WOQL filters:
  ```python
  # AttributeCondition(field="invoice_type", operator="in", values=["vendor_bill"])
  # Generates:
  WOQL().woql_or(
      WOQL().triple("v:Doc", "invoice_type", "vendor_bill"),
  )
  ```
- Qdrant filters are built from user's attribute conditions
- Meilisearch filters are built from conditions

**Post-Query Filtering (fallback only):**
- Python-based filtering is available for complex conditions that can't be pushed to storage
- Warning is logged when falling back to post-query filtering (performance concern)
- Documentation specifies which condition types require fallback

---

### Phase 3: Storage Layer Integration

#### Feature 8.7: Qdrant Team + Attribute Filtering
**Status:** 🔴 Not Started
**Priority:** High

##### Outcome
Qdrant payloads include team_id and configurable fields for filtering.

##### Scope: Owned Files
- `apps/documents/graph/consistency.py` - Payload creation
- `apps/documents/vector_store/qdrant_store.py` - Search filtering

##### Requirements

**Payload Extension:**
- All Qdrant payloads include `team_id`
- Ownership fields (`owned_by`, `created_by`) are added to payloads
- CDC access control fields from `field_mapping` are included
- Filterable fields are configured in index settings

**Search Filtering:**
- `team_id` filter is required on all searches
- Attribute filters from user permissions are optionally applied
- Filters are combined efficiently

**Migration (Required):**

Qdrant does not support updating payloads in place. New fields require re-ingesting all vectors.

- Migration script re-indexes all existing documents with new payload fields
- Migration runs BEFORE enabling team_id filtering (otherwise old records disappear from search)
- Impact is full re-index of all vectors (pre-production, acceptable)
- `team_id` backfill logic looks up team from document's bucket or TerminusDB record

---

#### Feature 8.8: Meilisearch Team Filtering
**Status:** 🔴 Not Started
**Priority:** High

##### Outcome
Meilisearch documents include team_id and filterable attributes.

##### Scope: Owned Files
- `apps/documents/indexing/` - Document creation
- Search service Meilisearch integration

##### Requirements

- All indexed documents include `team_id`
- Ownership fields are added to documents
- CDC access control fields are included
- Filterable attributes are configured in index settings
- Team filter is required on all searches

---

#### Feature 8.9: TerminusDB Enforcement
**Status:** 🔴 Not Started
**Priority:** High

##### Outcome
TerminusDB operations always validate team access, including Platform Group records.

##### Scope: Owned Files
- `apps/documents/graph/operations.py` - DocumentGraphAPI
- `apps/platform_groups/record_service.py` - PlatformGroupRecordService

##### Requirements

**DocumentGraphAPI:**
- `team_id` parameter is REQUIRED (not optional)
- `user_id` parameter is available for record-level checks (optional for system context)
- Operations fail closed: return None/empty if team_id is missing
- Access denials are logged for audit

**System Context (for background tasks):**

Background tasks (CDC sync, projections, scheduled jobs) run without a logged-in user. They must not break when `user_id` is None.

- `SystemContext` class represents system-level operations
- `SystemContext` bypasses ownership checks but still requires `team_id`
- Celery tasks use `SystemContext` instead of user context
- All system-context operations are logged for audit trail
- Example usage:
  ```python
  # In Celery task
  context = SystemContext(team_id=team_id, task_name="projection_sync")
  service.list(team_id=team_id, context=context)  # Bypasses ownership, respects team
  ```

**PlatformGroupRecordService:**
- `user_id` and `team_id` parameters are available on `get()`, `list()`, `search()` methods
- WOQL conditions in `list()` enforce ownership/assignment filtering:
  ```python
  # Example: Add ownership filter to WOQL query
  woql_query = WOQL().woql_and(
      WOQL().triple("v:Doc", "rdf:type", f"@schema:{model_name}"),
      WOQL().triple("v:Doc", "team_id", team_id),
      WOQL().woql_or(
          WOQL().triple("v:Doc", "owned_by", user_id),
          WOQL().triple("v:Doc", "assigned_to", user_id),
      )
  )
  ```
- WOQL conditions in `search()` enforce access filtering
- Post-fetch filtering fallback is available for complex ABAC conditions
- `list_for_user(user, team, ...)` wrapper method applies policies automatically

---

### Phase 4: Entry Point Enforcement

#### Feature 8.10: SearchService Integration
**Status:** 🔴 Not Started
**Priority:** High

##### Outcome
SearchService requires team context and applies access control to all searches.

##### Scope: Owned Files
- `apps/documents/graph/search_service.py`
- `apps/documents/api/services.py`

##### Requirements

- All search methods require `team_id` parameter
- Optional `user_id` is available for record-level filtering
- Optional `access_control: DocumentAccessControl` parameter is supported
- ABAC filters are applied before returning results
- All callers pass team context

---

#### Feature 8.11: Agent Tool Enforcement
**Status:** 🔴 Not Started
**Priority:** High

##### Outcome
AI agents operate under the same permission constraints as the user who initiated them.

##### Context
**Current Problem:**
- Agents access data via `hybrid_search` tool without user context
- SearchService has optional team filtering that agents bypass
- HookContext has user_id but tools don't use it
- Result: Agents can see ALL tenant data regardless of user permissions

##### Scope: Owned Files
- `apps/workflows/agents/base.py` - BaseAgentTask
- `apps/workflows/agents/tools/search.py` - hybrid_search tool
- `apps/platform_groups/protocols.py` - HookContext

##### Requirements

**User Context Propagation:**
- `user` is required in HookContext (not optional)
- `user_permissions: set[str]` is available in HookContext (pre-computed)
- BaseAgentTask requires user in context
- User context is passed from workflow execution to agents

**Tool Permission Enforcement:**
- `@agent_permission_required(permission)` decorator is available for tools
- `hybrid_search` requires and enforces user_id + team_id
- DocumentAccessControl is built from context
- Tool calls are rejected if context is incomplete

**Testing:**
- Agents cannot access data outside user's team
- Agents respect attribute-based permissions
- Permission denials are logged

---

#### Feature 8.12: API View Updates
**Status:** 🔴 Not Started
**Priority:** Medium

##### Outcome
All API views pass user and team context through to services.

##### Scope: Owned Files
- `apps/documents/api/search_views.py`
- `apps/documents/api/rest_views.py`
- `apps/documents/api/graph_views.py`
- `apps/documents/api/bulk_views.py`

##### Requirements

- Search views pass `request.user` and `request.team` to SearchService
- REST views use DocumentAccessControl for filtering
- Graph views include team filters in WOQL queries
- Bulk views validate per-record access
- 404 vs 403 response handling prevents info leakage

---

### Phase 5: Advanced Features

#### Feature 8.13: Audit Logging
**Status:** 🔴 Not Started
**Priority:** Medium

##### Outcome
Security-relevant actions are logged for compliance and debugging.

##### Scope: Owned Files
- `apps/audit/models.py`
- `apps/audit/middleware.py`

##### Requirements

**Audit Log Model:**
- `AuditLog` model stores action, actor, target, timestamp, and metadata
- Logs are indexed for efficient querying by actor, target, and date range
- Retention policy is configurable

**Event Capture:**
- Record access logging is available (configurable, off by default)
- Record modifications are logged
- Permission changes are logged
- Failed access attempts are logged
- Agent data access is logged

**Query Interface:**
- API endpoint provides audit log retrieval (admin only)
- Logs are filterable by actor, action type, and date range
- CSV export is available for compliance reports

---

#### Feature 8.14: Field-Level Security
**Status:** 🔴 Not Started
**Priority:** Low

##### Outcome
Specific fields can be hidden from users based on their role or permissions.

##### Scope: Owned Files
- `apps/platform_groups/field_security.py`
- `apps/platform_groups/serializers.py` - Base serializer

##### Requirements

**Field Visibility Rules:**
- `FieldVisibilityRule` model defines field, required_permission, and fallback_value
- Rules integrate with Platform Group field definitions
- UI hints metadata enables frontend field hiding

**Serializer Integration:**
- `SecuredModelSerializer` base class is available
- Fields are dynamically excluded based on user permissions
- Masked values (e.g., "****") are supported for hidden but present fields

---

#### Feature 8.15: Sharing & Explicit Grants
**Status:** 🔴 Not Started
**Priority:** Low

##### Outcome
Users can share individual records with specific team members.

##### Scope: Owned Files
- `apps/platform_groups/sharing.py`

##### Requirements

**Share Model:**
- `RecordShare` model stores record, granted_to, permission_level, and expires_at
- Share permission levels are: VIEW, EDIT, FULL
- Expiring shares are supported

**Share UI:**
- Share button is integrated in record detail views
- User picker allows selecting share recipients
- Active shares can be managed (view, revoke)

---

## Implementation Order

| Phase | Features | Model | Rationale |
|-------|----------|-------|-----------|
| **Phase 1** | 8.1, 8.2, 8.3 | Ownership | Ownership fields + policies + unified service |
| **Phase 2** | 8.4, 8.5, 8.6 | ABAC | Attribute conditions for CDC data filtering |
| **Phase 3** | 8.7, 8.8, 8.9 | All | Wire storage layers (Qdrant, Meilisearch, TerminusDB) |
| **Phase 4** | 8.10, 8.11, 8.12 | All | Enforce at all entry points (API, Agents) |
| **Phase 5** | 8.13, 8.14, 8.15 | — | Advanced features (audit, field security, sharing) |

**Note:** RBAC is already implemented via Platform Group permissions. This EPIC adds Ownership and ABAC layers on top.

**Note:** For multi-backend access control (TerminusDB + PostgreSQL), see [SQH-EPIC-02 Feature 2.8](SQH-EPIC-02-Unified-Data-Access-Layer.md#feature-28-access-control-integration).

---

## Key Files

**Models & Schema:**
- `apps/platform_groups/loader.py` - Inject ownership fields into TerminusDB schema
- `apps/platform_groups/models.py` - Django mixin (PostgreSQL models only)
- `apps/teams/models.py` - OwnershipPolicy
- `apps/platform_groups/permissions.py` - ConditionalPermission, AttributeCondition
- `apps/cdc/models.py` - field_mapping configuration

**Service Layer:**
- `apps/documents/access_control.py` - **NEW** DocumentAccessControl + ABAC
- `apps/documents/graph/search_service.py` - Search with access control
- `apps/documents/graph/operations.py` - TerminusDB with mandatory team validation
- `apps/platform_groups/record_service.py` - Platform Group CRUD with access control

**Storage Layer:**
- `apps/documents/graph/consistency.py` - Qdrant payload creation
- `apps/documents/vector_store/qdrant_store.py` - Vector search filtering

**Entry Points:**
- `apps/workflows/agents/tools/search.py` - Agent search tool
- `apps/workflows/agents/base.py` - Agent base class
- `apps/documents/api/*.py` - REST API views
- `apps/platform_groups/crm/api.py` - Platform Group API views

---

## References

- `apps/teams/models.py` - Existing team/membership models
- `apps/teams/roles.py` - Role permission functions
- `apps/documents/api/permissions.py` - TeamScopedPermission pattern
- `apps/platform_groups/crm/permissions.py` - Platform Group permission pattern
- `apps/platform_groups/protocols.py` - HookContext definition
