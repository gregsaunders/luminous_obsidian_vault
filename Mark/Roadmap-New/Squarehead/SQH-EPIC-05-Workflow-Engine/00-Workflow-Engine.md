---
status: "In Progress"
priority: "High"
epic_id: "SQH-EPIC-05"
linear_id: "SQU-43"
linear_url: "https://linear.app/squarehead/issue/SQU-43"
---

# EPIC-05: Workflow Engine

## Vision

Business processes can be automated using BPMN workflows with AI agent support, crash recovery, and configurable task assignment.

## User Stories

- As a **process designer**, I can define workflows using BPMN and have them execute reliably
- As a **workflow user**, my tasks are assigned based on role/queue and escalate if not completed
- As a **developer**, I can create AI agent tasks that integrate with workflows

## Context

BPMN-based workflow engine with AI agent task support. Core engine works; some advanced features have TODOs in code.

**What exists:** BPMN parsing/execution, DMN decision tables, LangGraph agents, DBOS durability, task assignment

**What's needed:** Task escalation, BPMN role extraction, workflow templates, documentation

## Features

- [[Feature 5.1 Task Escalation Logic]]
- [[Feature 5.2 BPMN Role Assignment Extraction]]
- [[Feature 5.3 Workflow Template Library]]
- [[Feature 5.4 Agent Task Patterns Documentation]]

## Key Files

- `apps/workflows/models.py` - WorkflowDefinition, WorkflowInstance, WorkflowTask
- `apps/workflows/engine.py` - BPMN execution
- `apps/workflows/tasks.py` - Celery task handlers
- `apps/workflows/agents/base.py` - BaseAgentTask
- `apps/workflows/dmn/` - Decision table support
- `apps/platform_groups/crm/workflows/` - Reference workflows

## Dependencies

**Depends On:** None (core platform capability)

**Used By:**
- All Platform Groups with automated processes
- [[LUM-EPIC-04-Platform-Infrastructure]] - Luminous workflows
