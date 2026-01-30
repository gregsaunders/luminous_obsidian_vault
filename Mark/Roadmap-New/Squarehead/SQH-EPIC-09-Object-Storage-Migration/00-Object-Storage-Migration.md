---
status: "Not Started"
priority: "High"
epic_id: "SQH-EPIC-09"
linear_id: "SQU-42"
linear_url: "https://linear.app/squarehead/issue/SQU-42"
---

# EPIC-09: Object Storage Migration

## Vision

Replace MinIO with a license-compliant, self-hosted S3-compatible object storage solution before pilot launch.

## User Stories

- As a **platform operator**, I can deploy object storage without AGPL licensing concerns so we can commercialize the product
- As a **developer**, I can use the same S3-compatible APIs so existing integrations continue working
- As a **tenant admin**, I can manage storage permissions for my team so data isolation is maintained

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

## Dependencies

- **Foundational:** No external blockers - critical infrastructure change
- **Related:** EPIC-12 Document Management (primary consumer of object storage)

## Replacement Options

| Option | License | S3 API | IAM | Events | Maturity | Notes |
|--------|---------|--------|-----|--------|----------|-------|
| **RustFS** | Apache 2.0 | Yes | Partial | Partial | New | 2.3x faster for small objects |
| **SeaweedFS** | Apache 2.0 | Yes | Basic | Partial | Mature | Needs `--iam` flag |
| **Ceph RGW** | LGPL | Yes | Yes | Yes | Production | Operationally complex |
| **Garage** | AGPL v3 | Partial | No | No | Mature | Same license concern |

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

## Features

- [[Feature 9.1 Technology Evaluation Spike]]
- [[Feature 9.2 Storage Abstraction Layer]]
- [[Feature 9.3 Auth Service Migration]]
- [[Feature 9.4 Event System Migration]]
- [[Feature 9.5 Data Migration & Cutover]]

## References

- [MinIO maintenance mode announcement (InfoQ, Dec 2025)](https://www.infoq.com/news/2025/12/minio-s3-api-alternatives/)
- [RustFS GitHub](https://github.com/rustfs/rustfs)
- [SeaweedFS GitHub](https://github.com/seaweedfs/seaweedfs)
- [Ceph RGW Documentation](https://docs.ceph.com/en/latest/radosgw/)
- Current MinIO code: `apps/documents/minio/`, `apps/users/minio_service.py`
