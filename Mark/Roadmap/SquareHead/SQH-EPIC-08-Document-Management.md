# EPIC-08: Document Management

**Status:** 🟢 Complete
**Priority:** Low (not directly needed for Luminous)
**Owner:** TBD

---

## Vision

Users can upload, search, and retrieve documents with full-text and semantic search capabilities.

---

## User Stories

- As a **user**, I can upload documents and find them later using natural language search
- As an **analyst**, I can search across all documents using keywords and semantic queries
- As a **developer**, I can leverage document embeddings for AI-powered features

---

## Context

Comprehensive document processing system with 20+ models. Supports upload, versioning, chunking, embedding, and hybrid search.

**What exists:** Document upload (MinIO), versioning, chunking, embeddings (Qdrant), keyword search (Meilisearch), RAPTOR indexing

**What's needed:** Per-model Qdrant collections, search optimization, RAPTOR improvements

---

## Features

### Feature 8.1: Per-Model Qdrant Collections

#### Outcome
Different document types are stored in separate Qdrant collections for better organization and performance.

#### Scope: Owned Files
- `apps/documents/graph/search_service.py`

#### Tasks
- [ ] Separate collections for different document types
- [ ] Collection management API

---

### Feature 8.2: Hybrid Search Optimization

#### Outcome
Search queries return more relevant results faster.

#### Scope: Owned Files
- `apps/documents/graph/search_service.py`

#### Tasks
- [ ] Query performance tuning
- [ ] Relevance improvements

---

### Feature 8.3: RAPTOR Indexing Improvements

#### Outcome
Hierarchical document summaries improve retrieval for long documents.

#### Scope: Owned Files
- `apps/documents/indexing/raptor.py`

#### Tasks
- [ ] Hierarchical summary generation
- [ ] Index maintenance

---

## Key Files

- `apps/documents/models.py` - 20+ models
- `apps/documents/tasks.py` - Document pipeline
- `apps/documents/graph/search_service.py` - Hybrid search
- `apps/documents/quality/tasks.py` - Quality metrics
