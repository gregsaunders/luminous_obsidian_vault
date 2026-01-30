---
status: "Complete"
priority: "Low"
epic_id: "SQH-EPIC-12"
linear_id: "SQU-46"
linear_url: "https://linear.app/squarehead/issue/SQU-46"
---

# EPIC-12: Document Management

## Vision

Users can upload, search, and retrieve documents with full-text and semantic search capabilities.

## User Stories

- As a **user**, I can upload documents and find them later using natural language search
- As an **analyst**, I can search across all documents using keywords and semantic queries
- As a **developer**, I can leverage document embeddings for AI-powered features

## Context

Comprehensive document processing system with 20+ models. Supports upload, versioning, chunking, embedding, and hybrid search.

**What exists:** Document upload (MinIO), versioning, chunking, embeddings (Qdrant), keyword search (Meilisearch), RAPTOR indexing

**What's needed:** Per-model Qdrant collections, search optimization, RAPTOR improvements

## Features

- [[Feature 12.1 Per-Model Qdrant Collections]]
- [[Feature 12.2 Hybrid Search Optimization]]
- [[Feature 12.3 RAPTOR Indexing Improvements]]

## Key Files

- `apps/documents/models.py` - 20+ models
- `apps/documents/tasks.py` - Document pipeline
- `apps/documents/graph/search_service.py` - Hybrid search
- `apps/documents/quality/tasks.py` - Quality metrics
