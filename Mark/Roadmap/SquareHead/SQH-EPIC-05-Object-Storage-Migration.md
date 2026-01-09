# EPIC-05: Object Storage Migration

**Status:** 🔴 Not Started
**Priority:** High
**Owner:** Greg
**Target:** Q2 2026 (Before Pilot)

**Dependencies:**
- ⭐ **Foundational:** No external blockers - critical infrastructure change
- 🔗 **Related:** EPIC-09 Document Management (primary consumer of object storage)

---

## Vision

Replace MinIO with a license-compliant, self-hosted S3-compatible object storage solution before pilot launch.

---

## User Stories

- As a **platform operator**, I can deploy object storage without AGPL licensing concerns so we can commercialize the product
- As a **developer**, I can use the same S3-compatible APIs so existing integrations continue working
- As a **tenant admin**, I can manage storage permissions for my team so data isolation is maintained

---

## Context

MinIO entered **maintenance mode** in December 2025:
- Community edition is now source-only (no binaries)
- Admin console features removed from community version
- Commercial license starts at ~$96k/year
- AGPL requires open-sourcing any modifications

**Current MinIO integration is heavy** - not a simple swap:

| Feature | Current Usage | Migration Complexity |
|---------|---------------|---------------------|
| S3-compatible API | Buckets, objects, versioning | Low - standard S3 API |
| **IAM/Policy Management** | Users, groups, per-bucket policies | **High** - MinIO-specific admin API |
| Presigned URLs | Direct client uploads (15-min TTL) | Medium - SDK-specific |
| Event Notifications | Redis queue for file processing | Medium - needs event system |
| Multi-tenancy | Bucket-per-team, user credentials | High - custom provisioning logic |

### Critical Files

- `apps/documents/minio/client.py` - MinIO client wrapper
- `apps/users/minio_service.py` - **630+ lines** of user/group/policy management
- `apps/documents/bucket_service.py` - Bucket CRUD operations
- `apps/documents/infrastructure.py` - Orchestration (MinIO + Qdrant + Meilisearch)
- `apps/documents/api/upload_views.py` - Presigned URL generation

---

## Replacement Options

| Option | License | S3 API | IAM | Events | Maturity | Notes |
|--------|---------|--------|-----|--------|----------|-------|
| **RustFS** | Apache 2.0 | ✅ | ⚠️ | ⚠️ | New | 2.3x faster for small objects |
| **SeaweedFS** | Apache 2.0 | ✅ | ⚠️ Basic | ⚠️ | Mature | Needs `--iam` flag |
| **Ceph RGW** | LGPL | ✅ | ✅ | ✅ | Production | Operationally complex |
| **Garage** | AGPL v3 | ⚠️ | ❌ | ❌ | Mature | Same license concern |

### Recommended Approaches

**Option A: RustFS + Application-Layer Auth** (Lower risk)
1. Use RustFS for object storage (Apache 2.0)
2. Move IAM/policy logic from MinIO to Django application layer
3. Single service account for RustFS, Django enforces permissions
4. Rewrite `minio_service.py` → `storage_auth_service.py`

**Option B: Ceph RGW** (Full feature parity)
1. Deploy Ceph via Rook on Kubernetes
2. Use RGW's native IAM for user/policy management
3. Smaller code changes, but ops complexity increases

---

## Features

### Feature 5.1: Technology Evaluation Spike
**Status:** 🔴 Not Started
**Priority:** Critical
**Dependencies:** None

#### Outcome
Team has data-driven decision on which storage solution to adopt.

#### What Success Looks Like
- RustFS spike complete: IAM capabilities, presigned URL support documented
- Ceph RGW spike complete: deployment complexity, ops overhead evaluated
- Application-layer auth feasibility assessed
- Go/no-go decision made with documented rationale

#### Tasks
- [ ] RustFS proof-of-concept deployment
- [ ] Test presigned URL generation with RustFS
- [ ] Evaluate RustFS IAM/policy capabilities
- [ ] Ceph RGW proof-of-concept (Rook on K8s)
- [ ] Prototype application-layer auth for bucket access
- [ ] Document findings and recommendation

---

### Feature 5.2: Storage Abstraction Layer
**Status:** 🔴 Not Started
**Priority:** High
**Dependencies:** Feature 5.1 (decision on storage solution)

#### Outcome
Application code is decoupled from specific storage implementation.

#### What Success Looks Like
- Storage operations use abstract interface
- MinIO-specific code isolated to adapter
- New storage backend can be swapped without app changes
- Existing tests pass with abstraction layer

#### Scope: Owned Files
- `apps/documents/storage/` (new abstraction layer)
- `apps/documents/minio/` (refactored as adapter)

#### Tasks
- [ ] Design storage abstraction interface
- [ ] Create `StorageClient` abstract base class
- [ ] Implement MinIO adapter (preserves current functionality)
- [ ] Implement new storage adapter (RustFS or Ceph)
- [ ] Update `infrastructure.py` to use abstraction
- [ ] Update all storage consumers to use interface

---

### Feature 5.3: Auth Service Migration
**Status:** 🔴 Not Started
**Priority:** High
**Dependencies:** Feature 5.1, Feature 5.2

#### Outcome
User/group/policy management works with new storage solution.

#### What Success Looks Like
- Multi-tenancy preserved (bucket-per-team isolation)
- User credentials work for their team's buckets only
- Policy enforcement is equivalent to current MinIO setup
- No regression in access control

#### Scope: Owned Files
- `apps/users/minio_service.py` → `apps/users/storage_auth_service.py`
- `apps/teams/storage_provisioning.py` (new)

#### Tasks
- [ ] Audit current MinIO policy patterns
- [ ] Design application-layer auth model (if Option A)
- [ ] Migrate user provisioning logic
- [ ] Migrate group/team provisioning logic
- [ ] Migrate bucket policy logic
- [ ] Update team creation signals
- [ ] Integration tests for multi-tenancy

---

### Feature 5.4: Event System Migration
**Status:** 🔴 Not Started
**Priority:** Medium
**Dependencies:** Feature 5.2

#### Outcome
File upload events trigger processing pipelines as before.

#### What Success Looks Like
- Upload completion triggers Celery task
- Document processing pipeline works
- Event format is normalized across backends
- No lost events during migration

#### Scope: Owned Files
- `apps/documents/events/` (new event abstraction)
- `apps/documents/minio_utils.py` (refactored)

#### Tasks
- [ ] Document current MinIO event flow
- [ ] Design event abstraction layer
- [ ] Implement event adapter for new storage
- [ ] Update Celery task handlers
- [ ] Test event delivery reliability

---

### Feature 5.5: Data Migration & Cutover
**Status:** 🔴 Not Started
**Priority:** High
**Dependencies:** Features 5.2, 5.3, 5.4

#### Outcome
All existing data is migrated to new storage with zero data loss.

#### What Success Looks Like
- Migration tool copies all buckets/objects
- Metadata preserved (content-type, custom headers)
- Verification confirms data integrity
- Rollback plan documented and tested
- Zero-downtime cutover executed

#### Tasks
- [ ] Build bucket enumeration tool
- [ ] Build object migration script
- [ ] Implement integrity verification (checksums)
- [ ] Create rollback procedure
- [ ] Document cutover runbook
- [ ] Execute migration in staging
- [ ] Execute production cutover

---

## References

- [MinIO maintenance mode announcement (InfoQ, Dec 2025)](https://www.infoq.com/news/2025/12/minio-s3-api-alternatives/)
- [RustFS GitHub](https://github.com/rustfs/rustfs)
- [SeaweedFS GitHub](https://github.com/seaweedfs/seaweedfs)
- [Ceph RGW Documentation](https://docs.ceph.com/en/latest/radosgw/)
- Current MinIO code: `apps/documents/minio/`, `apps/users/minio_service.py`
