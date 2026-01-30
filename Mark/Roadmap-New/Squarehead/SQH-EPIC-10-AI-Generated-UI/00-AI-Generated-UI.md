---
status: "Not Started"
priority: "Medium"
epic_id: "SQH-EPIC-10"
linear_id: "SQU-45"
linear_url: "https://linear.app/squarehead/issue/SQU-45"
---

# EPIC-10: AI-Generated UI

## Vision

AI agents can generate composable, ephemeral user interfaces on the fly using JSON Schema, enabling dynamic data collection and visualization during agent conversations.

## User Stories

- As an **AI agent**, I can generate a form UI using JSON Schema to collect structured input from users
- As a **user**, I see a well-designed form appear inline when an agent needs information from me
- As a **developer**, I can extend the UI vocabulary without modifying the core rendering layer
- As an **agent developer**, I can request visualizations (charts, tables) using the same schema format

## Context

The platform has a sophisticated JSON Schema-based form system (`WorkflowFormRenderer`) that renders Flutter Material 3 widgets from declarative schemas.

**Why JSON Schema for AI generation:**
- LLMs have extensive training on JSON Schema and Flutter widget patterns
- Direct generation eliminates translation layer complexity
- Accuracy matters more than token savings for UI generation (users see errors)
- Existing `WorkflowFormRenderer` already consumes JSON Schema

**Architecture:**
```
Agent generates JSON Schema → WorkflowFormRenderer → Flutter UI
                                        ↓
                              User fills form
                                        ↓
                              Data back to agent
```

## Dependencies

- [[../SQH-EPIC-04-Base-UI-Kit/00-Base-UI-Kit|SQH-EPIC-04: Base UI Kit]] - UI components (Feature 10.3 dependency)
- [[../SQH-EPIC-05-Workflow-Engine/00-Workflow-Engine|SQH-EPIC-05: Workflow Engine]] - Agent integration
- [[../SQH-EPIC-11-Frontend-Apps/00-Frontend-Apps|SQH-EPIC-11: Frontend Apps]] - Dynamic forms documentation

## Features

- [[Feature 10.1 UI Schema Vocabulary]]
- [[Feature 10.2 Agent UI Generation API]]
- [[Feature 10.3 Composable UI Components]]
- [[Feature 10.4 Ephemeral UI Lifecycle]]

## References

- Existing form system: `frontend/flutter/packages/workflows/lib/src/widgets/forms/`
