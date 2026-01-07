# EPIC-11: Record-Level Access Control

**Status:** 🔴 Not Started
**Priority:** Medium (needed before multi-user production deployments)
**Owner:** TBD

---

## Vision

Users can be restricted to viewing and editing only records they own, are assigned to, or have been explicitly granted access to—enabling team hierarchies where managers see all records while staff see only their own.

---

## User Stories

- As a **sales manager**, I want my sales reps to only see leads assigned to them
- As a **team admin**, I can define record visibility rules (owner-only, team-wide, role-based)
- As a **compliance officer**, I need audit logs showing who accessed sensitive records
- As a **HR admin**, I want to hide salary fields from non-HR team members

---

## Context

SquareHead currently implements team-level isolation: all team members with the "Editor" role can view and edit ALL records in their team. This is adequate for small teams but insufficient for:
- Sales teams with territory assignments
- Support teams with case ownership
- Any organization with data segregation requirements

**Depends On:**
- [SQH-EPIC-01](SQH-EPIC-01-Platform-Groups.md) - Platform Group framework (complete)
- `apps/teams/models.py` - Membership and role system (complete)

**Used By:**
- All Platform Groups requiring per-record access control
- [LUM-EPIC-02](../Luminous/LUM-EPIC-02-Luminous-Platform-Group.md) - Luminous may need sensor data access rules

---

## Features

### Feature 11.1: Record Ownership Model
**Status:** 🔴 Not Started
**Priority:** High

#### Outcome
Every record has an owner and optional assignees, enabling ownership-based filtering.

#### Scope: Owned Files
- `apps/platform_groups/models.py` - Base model mixin
- `apps/platform_groups/crm/models.py` - CRM model updates

#### Tasks

**Base Ownership Mixin:**
- [ ] Create `OwnedRecordMixin` with `created_by`, `owned_by`, `assigned_to` fields
- [ ] Auto-populate `created_by` on record creation
- [ ] `assigned_to` as ManyToMany for multi-assignee support
- [ ] Migration for existing Platform Group records

**Ownership Transfer:**
- [ ] API endpoint to transfer ownership
- [ ] Bulk ownership reassignment (when user leaves)
- [ ] Ownership transfer permission check

---

### Feature 11.2: Record-Level Permission Policies
**Status:** 🔴 Not Started
**Priority:** High

#### Outcome
Team admins can define visibility rules that determine which records users can see.

#### Scope: Owned Files
- `apps/teams/access_policies.py` - Policy definitions
- `apps/teams/models.py` - Policy storage

#### Tasks

**Policy Model:**
- [ ] `RecordAccessPolicy` model with policy types:
  - `TEAM_WIDE` - All team members see all records (current behavior)
  - `OWNER_ONLY` - Users see only records they own
  - `ASSIGNED_ONLY` - Users see records assigned to them
  - `HIERARCHICAL` - Managers see subordinates' records
- [ ] Policy attachment to Platform Group record types
- [ ] Default policy configuration per team

**Policy Evaluation:**
- [ ] `RecordAccessEvaluator` class for policy checks
- [ ] QuerySet filtering based on active policy
- [ ] Permission check integration with DRF

---

### Feature 11.3: Record Access QuerySet Filtering
**Status:** 🔴 Not Started
**Priority:** High

#### Outcome
Database queries automatically filter to records the user has access to.

#### Scope: Owned Files
- `apps/platform_groups/querysets.py` - Base QuerySet
- `apps/platform_groups/managers.py` - Model managers

#### Tasks

**Access-Aware QuerySet:**
- [ ] `AccessFilteredQuerySet` base class
- [ ] `.for_user(user)` method applying access policies
- [ ] Integration with existing Platform Group querysets
- [ ] Performance optimization (ensure indexes exist)

**API Integration:**
- [ ] Automatic filtering on list endpoints
- [ ] Permission check on detail/update/delete endpoints
- [ ] 404 vs 403 response handling (prevent info leakage)

---

### Feature 11.4: Agent Permission Enforcement
**Status:** 🔴 Not Started
**Priority:** High

#### Outcome
AI agents operate under the same permission constraints as the user who initiated them—agents cannot access data the user cannot access.

#### Context
**Current Problem:**
- Agents access data via `hybrid_search` tool without user context
- SearchService has optional team filtering that agents bypass
- HookContext has user_id but tools don't use it
- Result: Agents can see ALL tenant data regardless of user permissions

**Attack Surface:**
- User with limited permissions could prompt agent to retrieve restricted data
- Agent-generated summaries could leak data from other teams
- No audit trail of agent data access

#### Scope: Owned Files
- `apps/workflows/agents/base.py` - BaseAgentTask
- `apps/workflows/agents/tools/search.py` - hybrid_search tool
- `apps/documents/graph/search_service.py` - SearchService
- `apps/platform_groups/protocols.py` - HookContext

#### Tasks

**User Context Propagation:**
- [ ] Make `user` required in HookContext (not optional)
- [ ] Add `user_permissions: set[str]` to HookContext (pre-computed)
- [ ] Update BaseAgentTask to require user in context
- [ ] Pass user context from workflow execution to agents

**Tool Permission Enforcement:**
- [ ] Create `@agent_permission_required(permission)` decorator for tools
- [ ] Update `hybrid_search` to require and enforce user_id + team_id
- [ ] Add permission check before returning search results
- [ ] Reject tool calls if user lacks required permission

**SearchService Enforcement:**
- [ ] Make team_id REQUIRED (not optional) in search methods
- [ ] Add user_id parameter for record-level filtering
- [ ] Default deny: return empty results if team_id missing
- [ ] Log permission denials for security audit

**Agent Execution Context:**
- [ ] Capture initiating user when workflow starts
- [ ] Propagate user through BPMN execution to Service Tasks
- [ ] Ensure HookContext always has valid user object
- [ ] Handle system-triggered workflows (use service account with limited scope)

**Testing:**
- [ ] Test agent cannot access data outside user's team
- [ ] Test agent respects Platform Group permissions
- [ ] Test agent respects record-level access policies
- [ ] Test permission denial logging
- [ ] Test system workflows have appropriate scoping

---

### Feature 11.5: Audit Logging
**Status:** 🔴 Not Started
**Priority:** Medium

#### Outcome
Security-relevant actions are logged for compliance and debugging.

#### Scope: Owned Files
- `apps/audit/models.py`
- `apps/audit/middleware.py`

#### Tasks

**Audit Log Model:**
- [ ] `AuditLog` model with action, actor, target, timestamp, metadata
- [ ] Indexed for efficient querying by actor, target, date range
- [ ] Retention policy configuration

**Event Capture:**
- [ ] Record access logging (configurable, off by default)
- [ ] Record modification logging
- [ ] Permission change logging
- [ ] Failed access attempt logging

**Query Interface:**
- [ ] API endpoint for audit log retrieval (admin only)
- [ ] Filtering by actor, action type, date range
- [ ] Export to CSV for compliance reports

---

### Feature 11.6: Field-Level Security
**Status:** 🔴 Not Started
**Priority:** Low

#### Outcome
Specific fields can be hidden from users based on their role or permissions.

#### Scope: Owned Files
- `apps/platform_groups/field_security.py`
- `apps/platform_groups/serializers.py` - Base serializer

#### Tasks

**Field Visibility Rules:**
- [ ] `FieldVisibilityRule` model (field, required_permission, fallback_value)
- [ ] Integration with Platform Group field definitions
- [ ] UI hints metadata for frontend field hiding

**Serializer Integration:**
- [ ] `SecuredModelSerializer` base class
- [ ] Dynamic field exclusion based on user permissions
- [ ] Masked value support (e.g., "****" for hidden but present)

---

### Feature 11.7: Sharing & Explicit Grants
**Status:** 🔴 Not Started
**Priority:** Low

#### Outcome
Users can share individual records with specific team members.

#### Scope: Owned Files
- `apps/platform_groups/sharing.py`

#### Tasks

**Share Model:**
- [ ] `RecordShare` model (record, granted_to, permission_level, expires_at)
- [ ] Share permission levels: VIEW, EDIT, FULL
- [ ] Expiring shares support

**Share UI:**
- [ ] Share button integration in record detail views
- [ ] User picker for share recipients
- [ ] Active shares management

---

## Implementation Order

| Phase | Features | Rationale |
|-------|----------|-----------|
| **Phase 1** | 11.1, 11.2, 11.3 (Record Ownership + Policies + QuerySet) | Build the foundation first |
| **Phase 2** | 11.4 (Agent Permission Enforcement) | Wire agents into the complete system once |
| **Phase 3** | 11.5 (Audit Logging) | Compliance and debugging |
| **Phase 4** | 11.6, 11.7 (Field Security, Sharing) | Advanced features |

---

## Key Files

- `apps/platform_groups/models.py` - Ownership mixin
- `apps/teams/access_policies.py` - Policy definitions
- `apps/platform_groups/querysets.py` - Access-filtered querysets
- `apps/platform_groups/field_security.py` - Field-level rules
- `apps/audit/` - Audit logging system
- `apps/workflows/agents/base.py` - Agent base class (user context propagation)
- `apps/workflows/agents/tools/search.py` - Agent search tool (permission enforcement)
- `apps/documents/graph/search_service.py` - SearchService (team/user filtering)

---

## References

- `apps/teams/models.py` - Existing team/membership models
- `apps/teams/roles.py` - Role permission functions
- `apps/documents/api/permissions.py` - TeamScopedPermission pattern
- `apps/platform_groups/crm/permissions.py` - Platform Group permission pattern
- `apps/platform_groups/protocols.py` - HookContext definition
