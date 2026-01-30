---
title: "Squarehead Backlog Index"
---

# Squarehead Backlog Index

## Epic Overview
## Dependency Map

![[assets/cross-area-dependencies.svg]]


| Epic | Status | Priority | Features |
|------|--------|----------|----------|
| [[SQH-EPIC-01-MCP-Server/00-MCP-Server\|SQH-EPIC-01: MCP Server]] | Not Started | High | 11 |
| [[SQH-EPIC-02-Unified-Data-Access-Layer/00-Unified-Data-Access-Layer\|SQH-EPIC-02: Unified Data Access Layer]] | Not Started | High | 10 |
| [[SQH-EPIC-03-Platform-Groups/00-Platform-Groups\|SQH-EPIC-03: Platform Groups]] | In Progress | High | 3 |
| [[SQH-EPIC-04-Base-UI-Kit/00-Base-UI-Kit\|SQH-EPIC-04: Base UI Kit]] | In Progress | High | 11 |
| [[SQH-EPIC-05-Workflow-Engine/00-Workflow-Engine\|SQH-EPIC-05: Workflow Engine]] | In Progress | High | 4 |
| [[SQH-EPIC-06-AI-Services/00-AI-Services\|SQH-EPIC-06: AI Services]] | In Progress | Medium | 4 |
| [[SQH-EPIC-07-CDC-Pipeline/00-CDC-Pipeline\|SQH-EPIC-07: CDC Pipeline]] | In Progress | Medium | 3 |
| [[SQH-EPIC-08-Record-Access-Control/00-Record-Access-Control\|SQH-EPIC-08: Record Access Control]] | Not Started | Medium | 15 |
| [[SQH-EPIC-09-Object-Storage-Migration/00-Object-Storage-Migration\|SQH-EPIC-09: Object Storage Migration]] | Not Started | High | 5 |
| [[SQH-EPIC-10-AI-Generated-UI/00-AI-Generated-UI\|SQH-EPIC-10: AI-Generated UI]] | Not Started | Medium | 4 |
| [[SQH-EPIC-11-Frontend-Apps/00-Frontend-Apps\|SQH-EPIC-11: Frontend Apps]] | In Progress | Medium | 4 |
| [[SQH-EPIC-12-Document-Management/00-Document-Management\|SQH-EPIC-12: Document Management]] | Complete | Low | 3 |
| [[SQH-EPIC-13-Extended-Database-Connectors/00-Extended-Database-Support\|SQH-EPIC-13: Extended Database Connectors]] | Not Started | Low | 3 |
| [[SQH-EPIC-14-Tech-Debt/00-Tech-Debt\|SQH-EPIC-14: Tech Debt]] | In Progress | Medium | 5 |

## Full Feature Table

| Epic | Feature | Status | Priority | Assigned | Dependencies |
|------|---------|--------|----------|----------|--------------|
| SQH-01 | [[SQH-EPIC-01-MCP-Server/Feature 1.1 MCP Server Foundation\|Feature 1.1 MCP Server Foundation]] | Not Started | High | | - |
| SQH-01 | [[SQH-EPIC-01-MCP-Server/Feature 1.2 Search Tools\|Feature 1.2 Search Tools]] | Not Started | High | | Feature 1.1 MCP Server Foundation |
| SQH-01 | [[SQH-EPIC-01-MCP-Server/Feature 1.3 RAG Chat Tools\|Feature 1.3 RAG Chat Tools]] | Not Started | High | | Feature 1.1 MCP Server Foundation |
| SQH-01 | [[SQH-EPIC-01-MCP-Server/Feature 1.4 Document Tools\|Feature 1.4 Document Tools]] | Not Started | Medium | | Feature 1.1 MCP Server Foundation |
| SQH-01 | [[SQH-EPIC-01-MCP-Server/Feature 1.5 Document Resources\|Feature 1.5 Document Resources]] | Not Started | Medium | | Feature 1.1 MCP Server Foundation |
| SQH-01 | [[SQH-EPIC-01-MCP-Server/Feature 1.6 Knowledge Graph Tools\|Feature 1.6 Knowledge Graph Tools]] | Not Started | Low | | Feature 1.1 MCP Server Foundation |
| SQH-01 | [[SQH-EPIC-01-MCP-Server/Feature 1.7 Platform Group Tools\|Feature 1.7 Platform Group Tools]] | Not Started | Medium | | Feature 1.1 MCP Server Foundation, SQH-EPIC-02-Unified-Data-Access-Layer |
| SQH-01 | [[SQH-EPIC-01-MCP-Server/Feature 1.8 OAuth 2.1 Authorization\|Feature 1.8 OAuth 2.1 Authorization]] | Not Started | High | | Feature 1.1 MCP Server Foundation |
| SQH-01 | [[SQH-EPIC-01-MCP-Server/Feature 1.9 Prompt Templates\|Feature 1.9 Prompt Templates]] | Not Started | Low | | Feature 1.2 Search Tools, Feature 1.3 RAG Chat Tools, Feature 1.4 Document Tools |
| SQH-01 | [[SQH-EPIC-01-MCP-Server/Feature 1.10 Observability Integration\|Feature 1.10 Observability Integration]] | Not Started | Medium | | Feature 1.1 MCP Server Foundation |
| SQH-01 | [[SQH-EPIC-01-MCP-Server/Feature 1.11 Deployment Configuration\|Feature 1.11 Deployment Configuration]] | Not Started | High | | Feature 1.1 MCP Server Foundation, Feature 1.8 OAuth 2.1 Authorization |
| SQH-02 | [[SQH-EPIC-02-Unified-Data-Access-Layer/Feature 2.1 Storage Configuration\|Feature 2.1 Storage Configuration]] | Not Started | High | | - |
| SQH-02 | [[SQH-EPIC-02-Unified-Data-Access-Layer/Feature 2.2 Storage Backend Protocol\|Feature 2.2 Storage Backend Protocol]] | Not Started | High | | Feature 2.1 Storage Configuration |
| SQH-02 | [[SQH-EPIC-02-Unified-Data-Access-Layer/Feature 2.3 TerminusDB Backend\|Feature 2.3 TerminusDB Backend]] | Not Started | High | | Feature 2.2 Storage Backend Protocol |
| SQH-02 | [[SQH-EPIC-02-Unified-Data-Access-Layer/Feature 2.4 PostgreSQL Backend\|Feature 2.4 PostgreSQL Backend]] | Not Started | High | | Feature 2.2 Storage Backend Protocol |
| SQH-02 | [[SQH-EPIC-02-Unified-Data-Access-Layer/Feature 2.5 Service Refactoring\|Feature 2.5 Service Refactoring]] | Not Started | High | | Feature 2.3 TerminusDB Backend, Feature 2.4 PostgreSQL Backend |
| SQH-02 | [[SQH-EPIC-02-Unified-Data-Access-Layer/Feature 2.6 PostgreSQL Query Service\|Feature 2.6 PostgreSQL Query Service]] | Not Started | Medium | | Feature 2.4 PostgreSQL Backend |
| SQH-02 | [[SQH-EPIC-02-Unified-Data-Access-Layer/Feature 2.7 TerminusDB Query Service\|Feature 2.7 TerminusDB Query Service]] | Not Started | Medium | | Feature 2.3 TerminusDB Backend |
| SQH-02 | [[SQH-EPIC-02-Unified-Data-Access-Layer/Feature 2.8 Access Control Integration\|Feature 2.8 Access Control Integration]] | Not Started | High | | Feature 2.3 TerminusDB Backend, Feature 2.4 PostgreSQL Backend, SQH-EPIC-08-Record-Access-Control |
| SQH-02 | [[SQH-EPIC-02-Unified-Data-Access-Layer/Feature 2.9 ISON Output Formatting\|Feature 2.9 ISON Output Formatting]] | Not Started | Low | | Feature 2.6 PostgreSQL Query Service, Feature 2.7 TerminusDB Query Service |
| SQH-02 | [[SQH-EPIC-02-Unified-Data-Access-Layer/Feature 2.10 Shared Reference Database\|Feature 2.10 Shared Reference Database]] | Not Started | Medium | | Feature 2.4 PostgreSQL Backend |
| SQH-03 | [[SQH-EPIC-03-Platform-Groups/Feature 3.1 Platform Group Documentation\|Feature 3.1 Platform Group Documentation]] | Not Started | High | | - |
| SQH-03 | [[SQH-EPIC-03-Platform-Groups/Feature 3.2 UI Hints Schema Documentation\|Feature 3.2 UI Hints Schema Documentation]] | Not Started | Medium | | - |
| SQH-03 | [[SQH-EPIC-03-Platform-Groups/Feature 3.3 Extension System Validation\|Feature 3.3 Extension System Validation]] | Not Started | Medium | | - |
| SQH-04 | [[SQH-EPIC-04-Base-UI-Kit/Feature 4.1 Component Library Documentation\|Feature 4.1 Component Library Documentation]] | Not Started | High | | - |
| SQH-04 | [[SQH-EPIC-04-Base-UI-Kit/Feature 4.2 Design Tokens System\|Feature 4.2 Design Tokens System]] | Not Started | High | | - |
| SQH-04 | [[SQH-EPIC-04-Base-UI-Kit/Feature 4.3 Accessibility Compliance\|Feature 4.3 Accessibility Compliance]] | Not Started | High | | - |
| SQH-04 | [[SQH-EPIC-04-Base-UI-Kit/Feature 4.4 Dashboard Components\|Feature 4.4 Dashboard Components]] | Not Started | High | | - |
| SQH-04 | [[SQH-EPIC-04-Base-UI-Kit/Feature 4.5 Component Storybook\|Feature 4.5 Component Storybook]] | Not Started | Medium | | Feature 4.1 Component Library Documentation |
| SQH-04 | [[SQH-EPIC-04-Base-UI-Kit/Feature 4.6 Application Shell Architecture\|Feature 4.6 Application Shell Architecture]] | Not Started | High | | - |
| SQH-04 | [[SQH-EPIC-04-Base-UI-Kit/Feature 4.7 List Table Component\|Feature 4.7 List Table Component]] | Not Started | High | | - |
| SQH-04 | [[SQH-EPIC-04-Base-UI-Kit/Feature 4.8 Map Component\|Feature 4.8 Map Component]] | Not Started | High | | - |
| SQH-04 | [[SQH-EPIC-04-Base-UI-Kit/Feature 4.9 Hierarchical Prompt Shortcuts\|Feature 4.9 Hierarchical Prompt Shortcuts]] | Not Started | Medium | | Feature 4.6 Application Shell Architecture |
| SQH-04 | [[SQH-EPIC-04-Base-UI-Kit/Feature 4.10 Agent Progress Panel\|Feature 4.10 Agent Progress Panel]] | Not Started | Medium | | Feature 4.6 Application Shell Architecture |
| SQH-04 | [[SQH-EPIC-04-Base-UI-Kit/Feature 4.11 Gradient Fade Layout\|Feature 4.11 Gradient Fade Layout]] | Not Started | Low | | Feature 4.6 Application Shell Architecture, Feature 4.10 Agent Progress Panel |
| SQH-05 | [[SQH-EPIC-05-Workflow-Engine/Feature 5.1 Task Escalation Logic\|Feature 5.1 Task Escalation Logic]] | Not Started | High | | - |
| SQH-05 | [[SQH-EPIC-05-Workflow-Engine/Feature 5.2 BPMN Role Assignment Extraction\|Feature 5.2 BPMN Role Assignment Extraction]] | Not Started | Medium | | - |
| SQH-05 | [[SQH-EPIC-05-Workflow-Engine/Feature 5.3 Workflow Template Library\|Feature 5.3 Workflow Template Library]] | Not Started | Medium | | - |
| SQH-05 | [[SQH-EPIC-05-Workflow-Engine/Feature 5.4 Agent Task Patterns Documentation\|Feature 5.4 Agent Task Patterns Documentation]] | Not Started | Medium | | - |
| SQH-06 | [[SQH-EPIC-06-AI-Services/Feature 6.1 AI Services Documentation\|Feature 6.1 AI Services Documentation]] | Not Started | High | | - |
| SQH-06 | [[SQH-EPIC-06-AI-Services/Feature 6.2 Cost Monitoring Dashboard\|Feature 6.2 Cost Monitoring Dashboard]] | Not Started | Medium | | - |
| SQH-06 | [[SQH-EPIC-06-AI-Services/Feature 6.3 Model Selection Guidelines\|Feature 6.3 Model Selection Guidelines]] | Not Started | Medium | | - |
| SQH-06 | [[SQH-EPIC-06-AI-Services/Feature 6.4 Anomaly Detection Service\|Feature 6.4 Anomaly Detection Service]] | Not Started | High | | - |
| SQH-07 | [[SQH-EPIC-07-CDC-Pipeline/Feature 7.1 Processing Profiles\|Feature 7.1 Processing Profiles]] | Not Started | High | | - |
| SQH-07 | [[SQH-EPIC-07-CDC-Pipeline/Feature 7.2 Secret Resolution\|Feature 7.2 Secret Resolution]] | Not Started | High | | - |
| SQH-07 | [[SQH-EPIC-07-CDC-Pipeline/Feature 7.3 CDC Documentation\|Feature 7.3 CDC Documentation]] | Not Started | Medium | | - |
| SQH-08 | [[SQH-EPIC-08-Record-Access-Control/Feature 8.1 Record Ownership Model\|Feature 8.1 Record Ownership Model]] | Not Started | High | | - |
| SQH-08 | [[SQH-EPIC-08-Record-Access-Control/Feature 8.2 Ownership Policy Configuration\|Feature 8.2 Ownership Policy Configuration]] | Not Started | High | | - |
| SQH-08 | [[SQH-EPIC-08-Record-Access-Control/Feature 8.3 Unified Access Control Service\|Feature 8.3 Unified Access Control Service]] | Not Started | High | | - |
| SQH-08 | [[SQH-EPIC-08-Record-Access-Control/Feature 8.4 ABAC Condition Model\|Feature 8.4 ABAC Condition Model]] | Not Started | High | | - |
| SQH-08 | [[SQH-EPIC-08-Record-Access-Control/Feature 8.5 CDC Field Indexing\|Feature 8.5 CDC Field Indexing]] | Not Started | High | | - |
| SQH-08 | [[SQH-EPIC-08-Record-Access-Control/Feature 8.6 ABAC Evaluator\|Feature 8.6 ABAC Evaluator]] | Not Started | High | | - |
| SQH-08 | [[SQH-EPIC-08-Record-Access-Control/Feature 8.7 Qdrant Team + Attribute Filtering\|Feature 8.7 Qdrant Team + Attribute Filtering]] | Not Started | High | | - |
| SQH-08 | [[SQH-EPIC-08-Record-Access-Control/Feature 8.8 Meilisearch Team Filtering\|Feature 8.8 Meilisearch Team Filtering]] | Not Started | High | | - |
| SQH-08 | [[SQH-EPIC-08-Record-Access-Control/Feature 8.9 TerminusDB Enforcement\|Feature 8.9 TerminusDB Enforcement]] | Not Started | High | | - |
| SQH-08 | [[SQH-EPIC-08-Record-Access-Control/Feature 8.10 SearchService Integration\|Feature 8.10 SearchService Integration]] | Not Started | High | | - |
| SQH-08 | [[SQH-EPIC-08-Record-Access-Control/Feature 8.11 Agent Tool Enforcement\|Feature 8.11 Agent Tool Enforcement]] | Not Started | High | | - |
| SQH-08 | [[SQH-EPIC-08-Record-Access-Control/Feature 8.12 API View Updates\|Feature 8.12 API View Updates]] | Not Started | Medium | | - |
| SQH-08 | [[SQH-EPIC-08-Record-Access-Control/Feature 8.13 Audit Logging\|Feature 8.13 Audit Logging]] | Not Started | Medium | | - |
| SQH-08 | [[SQH-EPIC-08-Record-Access-Control/Feature 8.14 Field-Level Security\|Feature 8.14 Field-Level Security]] | Not Started | Low | | - |
| SQH-08 | [[SQH-EPIC-08-Record-Access-Control/Feature 8.15 Sharing & Explicit Grants\|Feature 8.15 Sharing & Explicit Grants]] | Not Started | Low | | - |
| SQH-09 | [[SQH-EPIC-09-Object-Storage-Migration/Feature 9.1 Technology Evaluation Spike\|Feature 9.1 Technology Evaluation Spike]] | Not Started | Critical | | - |
| SQH-09 | [[SQH-EPIC-09-Object-Storage-Migration/Feature 9.2 Storage Abstraction Layer\|Feature 9.2 Storage Abstraction Layer]] | Not Started | High | | Feature 9.1 Technology Evaluation Spike |
| SQH-09 | [[SQH-EPIC-09-Object-Storage-Migration/Feature 9.3 Auth Service Migration\|Feature 9.3 Auth Service Migration]] | Not Started | High | | Feature 9.1 Technology Evaluation Spike, Feature 9.2 Storage Abstraction Layer |
| SQH-09 | [[SQH-EPIC-09-Object-Storage-Migration/Feature 9.4 Event System Migration\|Feature 9.4 Event System Migration]] | Not Started | Medium | | Feature 9.2 Storage Abstraction Layer |
| SQH-09 | [[SQH-EPIC-09-Object-Storage-Migration/Feature 9.5 Data Migration & Cutover\|Feature 9.5 Data Migration & Cutover]] | Not Started | High | | Feature 9.2 Storage Abstraction Layer, Feature 9.3 Auth Service Migration, Feature 9.4 Event System Migration |
| SQH-10 | [[SQH-EPIC-10-AI-Generated-UI/Feature 10.1 UI Schema Vocabulary\|Feature 10.1 UI Schema Vocabulary]] | Not Started | High | | - |
| SQH-10 | [[SQH-EPIC-10-AI-Generated-UI/Feature 10.2 Agent UI Generation API\|Feature 10.2 Agent UI Generation API]] | Not Started | High | | - |
| SQH-10 | [[SQH-EPIC-10-AI-Generated-UI/Feature 10.3 Composable UI Components\|Feature 10.3 Composable UI Components]] | Not Started | Medium | | SQH-EPIC-04 Feature 4.4 Dashboard Components |
| SQH-10 | [[SQH-EPIC-10-AI-Generated-UI/Feature 10.4 Ephemeral UI Lifecycle\|Feature 10.4 Ephemeral UI Lifecycle]] | Not Started | Medium | | - |
| SQH-11 | [[SQH-EPIC-11-Frontend-Apps/Feature 11.1 Flutter Dynamic Forms Documentation\|Feature 11.1 Flutter Dynamic Forms Documentation]] | Not Started | Medium | | - |
| SQH-11 | [[SQH-EPIC-11-Frontend-Apps/Feature 11.2 Desktop Sync Completion\|Feature 11.2 Desktop Sync Completion]] | Not Started | Medium | | - |
| SQH-11 | [[SQH-EPIC-11-Frontend-Apps/Feature 11.3 React Graph Visualizer Maintenance\|Feature 11.3 React Graph Visualizer Maintenance]] | Not Started | Low | | - |
| SQH-11 | [[SQH-EPIC-11-Frontend-Apps/Feature 11.4 Web App Modernization\|Feature 11.4 Web App Modernization]] | Not Started | Low | | - |
| SQH-12 | [[SQH-EPIC-12-Document-Management/Feature 12.1 Per-Model Qdrant Collections\|Feature 12.1 Per-Model Qdrant Collections]] | Not Started | Medium | | - |
| SQH-12 | [[SQH-EPIC-12-Document-Management/Feature 12.2 Hybrid Search Optimization\|Feature 12.2 Hybrid Search Optimization]] | Not Started | Medium | | - |
| SQH-12 | [[SQH-EPIC-12-Document-Management/Feature 12.3 RAPTOR Indexing Improvements\|Feature 12.3 RAPTOR Indexing Improvements]] | Not Started | Low | | - |
| SQH-13 | [[SQH-EPIC-13-Extended-Database-Connectors/Feature 13.1 SQL Server Documentation\|Feature 13.1 SQL Server Documentation]] | In Progress | Low | | - |
| SQH-13 | [[SQH-EPIC-13-Extended-Database-Connectors/Feature 13.2 Oracle ConfigBuilder\|Feature 13.2 Oracle ConfigBuilder]] | Not Started | Low | | - |
| SQH-13 | [[SQH-EPIC-13-Extended-Database-Connectors/Feature 13.3 MongoDB Support Evaluation\|Feature 13.3 MongoDB Support Evaluation]] | Not Started | Low | | - |
| SQH-14 | [[SQH-EPIC-14-Tech-Debt/Feature 14.1 Email Notification Delivery\|Feature 14.1 Email Notification Delivery]] | Not Started | Medium | | - |
| SQH-14 | [[SQH-EPIC-14-Tech-Debt/Feature 14.2 Push Notification Support\|Feature 14.2 Push Notification Support]] | Not Started | Low | | - |
| SQH-14 | [[SQH-EPIC-14-Tech-Debt/Feature 14.3 Test Coverage Gaps\|Feature 14.3 Test Coverage Gaps]] | In Progress | Medium | | - |
| SQH-14 | [[SQH-EPIC-14-Tech-Debt/Feature 14.4 Support Ticket System\|Feature 14.4 Support Ticket System]] | Not Started | Low | | - |
| SQH-14 | [[SQH-EPIC-14-Tech-Debt/Feature 14.5 Group Chat UI Integration\|Feature 14.5 Group Chat UI Integration]] | Not Started | Low | | - |
