---
title: "Luminous Backlog Index"
---

# Luminous Backlog Index

## Epic Overview
## Dependency Map

![[assets/luminous-dependency-map.svg]]


| Epic | Status | Priority | Features |
|------|--------|----------|----------|
| [[LUM-EPIC-01-Data-Ingestion/00-Data-Ingestion\|LUM-EPIC-01: Data Ingestion]] | Not Started | Critical | 6 |
| [[LUM-EPIC-02-Unified-Water-Quality-Data-Model/00-Unified-Water-Quality-Data-Model\|LUM-EPIC-02: Unified Water Quality Data Model]] | Not Started | Critical | 7 |
| [[LUM-EPIC-03-Customer-Dashboard/00-Customer-Dashboard\|LUM-EPIC-03: Customer Dashboard]] | Not Started | Critical | 8 |
| [[LUM-EPIC-04-Platform-Infrastructure/00-Platform-Infrastructure\|LUM-EPIC-04: Platform Infrastructure]] | In Progress | High | 6 |
| [[LUM-EPIC-05-Field-Operations/00-Field-Operations\|LUM-EPIC-05: Field Operations]] | Not Started | High | 5 |
| [[LUM-EPIC-06-Observability-Docs/00-Observability-Docs\|LUM-EPIC-06: Observability & Documentation]] | In Progress | Medium | 5 |
| [[LUM-EPIC-07-Treatment-Intelligence/00-Treatment-Intelligence\|LUM-EPIC-07: Treatment Intelligence]] | Not Started | High | 5 |

## Full Feature Table

| Epic | Feature | Status | Priority | Assigned | Dependencies |
|------|---------|--------|----------|----------|--------------|
| LUM-01 | [[LUM-EPIC-01-Data-Ingestion/Feature 1.0 Luminous Platform Group Scaffolding\|Feature 1.0 Luminous Platform Group Scaffolding]] | Not Started | Critical | | - |
| LUM-01 | [[LUM-EPIC-01-Data-Ingestion/Feature 1.1 Biosensor Results Data Model\|Feature 1.1 Biosensor Results Data Model]] | Not Started | Critical | | Feature 1.0 |
| LUM-01 | [[LUM-EPIC-01-Data-Ingestion/Feature 1.2 Lab Results Upload Pipeline\|Feature 1.2 Lab Results Upload Pipeline]] | Not Started | Critical | | Feature 1.1 |
| LUM-01 | [[LUM-EPIC-01-Data-Ingestion/Feature 1.3 Sample Metadata Linkage\|Feature 1.3 Sample Metadata Linkage]] | Not Started | Critical | | Feature 1.1, Feature 1.2, LUM-EPIC-05 Feature 5.1 |
| LUM-01 | [[LUM-EPIC-01-Data-Ingestion/Feature 1.4 Contextual Data Integration\|Feature 1.4 Contextual Data Integration]] | Not Started | High | | Feature 1.3 |
| LUM-01 | [[LUM-EPIC-01-Data-Ingestion/Feature 1.5 Analysis Script Automation\|Feature 1.5 Analysis Script Automation]] | Not Started | Medium | | Feature 1.2 |
| LUM-02 | [[LUM-EPIC-02-Unified-Water-Quality-Data-Model/Feature 2.0 Core Data Model (PostgreSQL Schema)\|Feature 2.0 Core Data Model (PostgreSQL Schema)]] | Not Started | Critical | | SQH-EPIC-02 (Unified Data Access Layer) |
| LUM-02 | [[LUM-EPIC-02-Unified-Water-Quality-Data-Model/Feature 2.1 Parameter Aliasing & Unit Normalization\|Feature 2.1 Parameter Aliasing & Unit Normalization]] | Not Started | Critical | | Feature 2.0 |
| LUM-02 | [[LUM-EPIC-02-Unified-Water-Quality-Data-Model/Feature 2.2 Detection Limit Handling\|Feature 2.2 Detection Limit Handling]] | Not Started | High | | Feature 2.0 |
| LUM-02 | [[LUM-EPIC-02-Unified-Water-Quality-Data-Model/Feature 2.3 ETL Pipelines (4 Data Sources)\|Feature 2.3 ETL Pipelines (4 Data Sources)]] | Not Started | Critical | | Feature 2.0, Feature 2.1 |
| LUM-02 | [[LUM-EPIC-02-Unified-Water-Quality-Data-Model/Feature 2.4 Query Services & Time-Series Analysis\|Feature 2.4 Query Services & Time-Series Analysis]] | Not Started | High | | Feature 2.2, Feature 2.3 |
| LUM-02 | [[LUM-EPIC-02-Unified-Water-Quality-Data-Model/Feature 2.5 Quality Flag Interpretation\|Feature 2.5 Quality Flag Interpretation]] | Not Started | Medium | | Feature 2.3 |
| LUM-02 | [[LUM-EPIC-02-Unified-Water-Quality-Data-Model/Feature 2.6 Water Quality Dashboard Views\|Feature 2.6 Water Quality Dashboard Views]] | Not Started | Medium | | Feature 2.4, SQH-EPIC-04 Feature 4.4, SQH-EPIC-04 Feature 4.7, SQH-EPIC-04 Feature 4.8 |
| LUM-03 | [[LUM-EPIC-03-Customer-Dashboard/Feature 3.1 User Authentication\|Feature 3.1 User Authentication]] | In Progress | Critical | | LUM-EPIC-04 Feature 4.1 |
| LUM-03 | [[LUM-EPIC-03-Customer-Dashboard/Feature 3.2 Summary View\|Feature 3.2 Summary View]] | Not Started | Critical | | LUM-EPIC-01 Feature 1.1, LUM-EPIC-01 Feature 1.2, LUM-EPIC-01 Feature 1.3 |
| LUM-03 | [[LUM-EPIC-03-Customer-Dashboard/Feature 3.3 Trend Charts\|Feature 3.3 Trend Charts]] | Not Started | Critical | | Feature 3.2, LUM-EPIC-01 Feature 1.1 |
| LUM-03 | [[LUM-EPIC-03-Customer-Dashboard/Feature 3.4 Spatial View\|Feature 3.4 Spatial View]] | Not Started | High | | Feature 3.2, LUM-EPIC-01 Feature 1.3 |
| LUM-03 | [[LUM-EPIC-03-Customer-Dashboard/Feature 3.5 Data Table & Export\|Feature 3.5 Data Table & Export]] | Not Started | Critical | | LUM-EPIC-01 Feature 1.1, LUM-EPIC-01 Feature 1.2, LUM-EPIC-01 Feature 1.3 |
| LUM-03 | [[LUM-EPIC-03-Customer-Dashboard/Feature 3.6 Correlation View\|Feature 3.6 Correlation View]] | Not Started | High | | Feature 3.3, LUM-EPIC-01 Feature 1.4 |
| LUM-03 | [[LUM-EPIC-03-Customer-Dashboard/Feature 3.7 Community Dashboard\|Feature 3.7 Community Dashboard]] | Not Started | High | | Feature 3.2, Feature 3.3 |
| LUM-03 | [[LUM-EPIC-03-Customer-Dashboard/Feature 3.8 Operator Annotation System\|Feature 3.8 Operator Annotation System]] | Not Started | Medium | | Feature 3.2, Feature 3.3 |
| LUM-04 | [[LUM-EPIC-04-Platform-Infrastructure/Feature 4.1 Customer User Provisioning\|Feature 4.1 Customer User Provisioning]] | In Progress | High | | - |
| LUM-04 | [[LUM-EPIC-04-Platform-Infrastructure/Feature 4.2 Notification System\|Feature 4.2 Notification System]] | In Progress | Medium | | Feature 4.1, LUM-EPIC-01 Feature 1.2 |
| LUM-04 | [[LUM-EPIC-04-Platform-Infrastructure/Feature 4.3 Audit Trail (Glass Box)\|Feature 4.3 Audit Trail (Glass Box)]] | In Progress | Medium | | LUM-EPIC-01 Feature 1.1 |
| LUM-04 | [[LUM-EPIC-04-Platform-Infrastructure/Feature 4.4 PDF Report Generation\|Feature 4.4 PDF Report Generation]] | Not Started | Medium | | LUM-EPIC-01 Feature 1.1, LUM-EPIC-01 Feature 1.2, LUM-EPIC-01 Feature 1.3, LUM-EPIC-03 Feature 3.2, LUM-EPIC-03 Feature 3.3 |
| LUM-04 | [[LUM-EPIC-04-Platform-Infrastructure/Feature 4.5 API Documentation\|Feature 4.5 API Documentation]] | In Progress | Medium | | LUM-EPIC-01 Feature 1.2, LUM-EPIC-01 Feature 1.3 |
| LUM-04 | [[LUM-EPIC-04-Platform-Infrastructure/Feature 4.6 Pilot UAT Process\|Feature 4.6 Pilot UAT Process]] | Not Started | High | | LUM-EPIC-01, LUM-EPIC-03, LUM-EPIC-04 |
| LUM-05 | [[LUM-EPIC-05-Field-Operations/Feature 5.1 Sample Metadata Capture App\|Feature 5.1 Sample Metadata Capture App]] | Not Started | High | | - |
| LUM-05 | [[LUM-EPIC-05-Field-Operations/Feature 5.2 Sampling SOP for Customers\|Feature 5.2 Sampling SOP for Customers]] | In Progress | High | | - |
| LUM-05 | [[LUM-EPIC-05-Field-Operations/Feature 5.3 Sample Kit Management\|Feature 5.3 Sample Kit Management]] | Not Started | Medium | | LUM-EPIC-04 Feature 4.1 |
| LUM-05 | [[LUM-EPIC-05-Field-Operations/Feature 5.4 Courier Logistics\|Feature 5.4 Courier Logistics]] | In Progress | Medium | | - |
| LUM-05 | [[LUM-EPIC-05-Field-Operations/Feature 5.5 Custom Flutter Field App\|Feature 5.5 Custom Flutter Field App]] | Not Started | Low | | SquareHead EPIC-11 (Frontend Apps), Pilot feedback |
| LUM-06 | [[LUM-EPIC-06-Observability-Docs/Feature 6.1 Platform Monitoring Dashboard\|Feature 6.1 Platform Monitoring Dashboard]] | In Progress | Medium | | - |
| LUM-06 | [[LUM-EPIC-06-Observability-Docs/Feature 6.2 Luminous AI Usage Patterns\|Feature 6.2 Luminous AI Usage Patterns]] | Not Started | Medium | | SQH-EPIC-06 Feature 6.1 |
| LUM-06 | [[LUM-EPIC-06-Observability-Docs/Feature 6.3 Developer Onboarding Guide\|Feature 6.3 Developer Onboarding Guide]] | In Progress | Medium | | - |
| LUM-06 | [[LUM-EPIC-06-Observability-Docs/Feature 6.4 Flutter Client Documentation\|Feature 6.4 Flutter Client Documentation]] | In Progress | Medium | | - |
| LUM-06 | [[LUM-EPIC-06-Observability-Docs/Feature 6.5 Runbook for Operations\|Feature 6.5 Runbook for Operations]] | Not Started | Low | | Feature 6.1 |
| LUM-07 | [[LUM-EPIC-07-Treatment-Intelligence/Feature 7.1 Treatment Performance Metrics\|Feature 7.1 Treatment Performance Metrics]] | Not Started | Critical | | LUM-EPIC-02 Features 2.1-2.3 |
| LUM-07 | [[LUM-EPIC-07-Treatment-Intelligence/Feature 7.2 Cell Routing Recommendations\|Feature 7.2 Cell Routing Recommendations]] | Not Started | High | | Feature 7.1 |
| LUM-07 | [[LUM-EPIC-07-Treatment-Intelligence/Feature 7.3 Seasonal Strategy Optimizer\|Feature 7.3 Seasonal Strategy Optimizer]] | Not Started | High | | Feature 7.1, LUM-EPIC-02 Feature 2.4 |
| LUM-07 | [[LUM-EPIC-07-Treatment-Intelligence/Feature 7.4 Intervention Outcome Tracking\|Feature 7.4 Intervention Outcome Tracking]] | Not Started | Critical | | Feature 7.2 |
| LUM-07 | [[LUM-EPIC-07-Treatment-Intelligence/Feature 7.5 Prescriptive Alerts\|Feature 7.5 Prescriptive Alerts]] | Not Started | Medium | | Feature 7.1, Feature 7.2, Feature 7.4, SQH-EPIC-06 (Anomaly Detection Service) |
