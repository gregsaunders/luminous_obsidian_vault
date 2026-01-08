# EPIC-05: Workflow Engine

**Status:** 🟡 Partial
**Priority:** High
**Owner:** TBD

---

## Vision

Business processes can be automated using BPMN workflows with AI agent support, crash recovery, and configurable task assignment.

---

## User Stories

- As a **process designer**, I can define workflows using BPMN and have them execute reliably
- As a **workflow user**, my tasks are assigned based on role/queue and escalate if not completed
- As a **developer**, I can create AI agent tasks that integrate with workflows

---

## Context

BPMN-based workflow engine with AI agent task support. Core engine works; some advanced features have TODOs in code.

**What exists:** BPMN parsing/execution, DMN decision tables, LangGraph agents, DBOS durability, task assignment

**What's needed:** Task escalation, BPMN role extraction, workflow templates, documentation

---

## Features

### Feature 5.1: Task Escalation Logic

#### Outcome
Tasks that exceed SLA are automatically escalated to appropriate parties.

#### Scope: Owned Files
- `apps/workflows/tasks.py`
- `apps/workflows/escalation.py`

#### Tasks
- [ ] Implement escalation when tasks exceed SLA
- [ ] Configurable escalation paths
- [ ] Notification on escalation

---

### Feature 5.2: BPMN Role Assignment Extraction

#### Outcome
Role assignments from BPMN extensions are parsed and used for dynamic task assignment.

#### Scope: Owned Files
- `apps/workflows/engine.py`

#### Tasks
- [ ] Parse role assignments from BPMN extensions
- [ ] Dynamic assignment based on workflow context

---

### Feature 5.3: Workflow Template Library

#### Outcome
Common workflow patterns are available as templates to accelerate new workflow creation.

#### Scope: Owned Files
- `apps/workflows/templates/`
- `docs/workflows/templates/`

#### Tasks
- [ ] Approval workflow templates
- [ ] Multi-step process templates
- [ ] Agent-assisted workflow templates

---

### Feature 5.4: Agent Task Patterns Documentation

#### Outcome
A developer can create AI agent tasks following documented patterns.

#### Scope: Owned Files
- `docs/workflows/agents/`

#### Tasks
- [ ] BaseAgentTask usage guide
- [ ] Input/output schemas
- [ ] Durability and retry patterns

---

## Key Files

- `apps/workflows/models.py` - WorkflowDefinition, WorkflowInstance, WorkflowTask
- `apps/workflows/engine.py` - BPMN execution
- `apps/workflows/tasks.py` - Celery task handlers
- `apps/workflows/agents/base.py` - BaseAgentTask
- `apps/workflows/dmn/` - Decision table support
- `apps/platform_groups/crm/workflows/` - Reference workflows
