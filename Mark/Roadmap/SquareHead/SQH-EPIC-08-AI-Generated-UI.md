---
linear_id: SQU-45
linear_url: https://linear.app/squarehead/issue/SQU-45
---

# EPIC-08: AI-Generated UI

**Linear:** [SQU-45](https://linear.app/squarehead/issue/SQU-45)
**Status:** Not Started
**Priority:** Medium
**Owner:** TBD

---

## Vision

AI agents can generate composable, ephemeral user interfaces on the fly using JSON Schema, enabling dynamic data collection and visualization during agent conversations.

---

## User Stories

- As an **AI agent**, I can generate a form UI using JSON Schema to collect structured input from users
- As a **user**, I see a well-designed form appear inline when an agent needs information from me
- As a **developer**, I can extend the UI vocabulary without modifying the core rendering layer
- As an **agent developer**, I can request visualizations (charts, tables) using the same schema format

---

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

---

## Features

### Feature 8.1: UI Schema Vocabulary
**Linear:** [SQU-51](https://linear.app/squarehead/issue/SQU-51)

#### Outcome
A defined JSON Schema vocabulary for UI components that works with the existing form system and is optimized for LLM generation.

#### What Success Looks Like
- JSON Schema conventions documented for forms, fields, layouts
- Schema covers: text, number, date, enum, reference, array, object
- Layout hints (col-span) expressible via `x-ui-*` extensions
- Validation rules expressible in standard JSON Schema format
- Example prompts that reliably produce valid schemas

#### Example Schema
```json
{
  "type": "object",
  "title": "Contact Form",
  "properties": {
    "name": {
      "type": "string",
      "title": "Name",
      "x-ui-col-span": 6
    },
    "email": {
      "type": "string",
      "format": "email",
      "title": "Email",
      "x-ui-col-span": 6
    },
    "phone": {
      "type": "string",
      "title": "Phone",
      "x-ui-col-span": 6
    },
    "status": {
      "type": "string",
      "enum": ["active", "inactive", "lead"],
      "title": "Status",
      "x-ui-col-span": 6
    },
    "notes": {
      "type": "string",
      "title": "Notes",
      "x-ui-col-span": 12,
      "x-ui-widget": "textarea"
    }
  },
  "required": ["name", "email"]
}
```

#### Scope: Owned Files
- `docs/ai-ui/schema-vocabulary.md`
- `docs/ai-ui/examples/`

#### Tasks
- [ ] Document JSON Schema conventions for form fields
- [ ] Define `x-ui-*` extension vocabulary (col-span, widget, sections)
- [ ] Document type mappings to Flutter widgets
- [ ] Create example schemas for common patterns
- [ ] Create example prompts for LLM generation
- [ ] Document validation rule patterns

---

### Feature 8.2: Agent UI Generation API
**Linear:** [SQU-52](https://linear.app/squarehead/issue/SQU-52)

#### Outcome
Agents can request UI generation through a simple API that returns rendered UI specifications.

#### What Success Looks Like
- Agent sends JSON Schema, receives UI ready for rendering
- Error handling for invalid schemas
- Schema validation before rendering
- Supports both form input and display-only modes

#### Scope: Owned Files
- `square_head/apps/ai_ui/api/`
- `frontend/flutter/packages/workflows/lib/src/widgets/agent_ui_renderer.dart`

#### Tasks
- [ ] API endpoint: POST /api/v1/ai-ui/generate
- [ ] JSON Schema validation
- [ ] Error response format with helpful messages
- [ ] Flutter widget for rendering agent-generated UI
- [ ] Callback mechanism for form submission
- [ ] Display-only mode for visualizations

---

### Feature 8.3: Composable UI Components
**Linear:** [SQU-53](https://linear.app/squarehead/issue/SQU-53)

#### Outcome
The UI vocabulary includes visualization components beyond forms (charts, tables, cards).

#### What Success Looks Like
- Agent can request a chart with data inline
- Agent can request a data table
- Agent can compose multiple components in a layout
- Components use Base UI Kit (SQH-EPIC-02)

#### Example Schema
```json
{
  "type": "object",
  "x-ui-component": "chart",
  "properties": {
    "chartType": { "const": "line" },
    "title": { "const": "NA Concentration Over Time" },
    "xAxis": { "const": "date" },
    "yAxis": { "const": "concentration" },
    "yAxisLabel": { "const": "mg/L" },
    "data": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "date": { "type": "string" },
          "concentration": { "type": "number" }
        }
      },
      "default": [
        { "date": "2024-01-01", "concentration": 12.5 },
        { "date": "2024-01-02", "concentration": 14.2 },
        { "date": "2024-01-03", "concentration": 11.8 }
      ]
    }
  }
}
```

#### Dependencies
- [SQH-EPIC-02 Feature 2.4](SQH-EPIC-02-Base-UI-Kit.md) - Dashboard Components

#### Scope: Owned Files
- `docs/ai-ui/schema-vocabulary.md` (extended)
- `frontend/flutter/packages/ai_ui/lib/src/components/`

#### Tasks
- [ ] Define JSON Schema for chart specification
- [ ] Define JSON Schema for data table
- [ ] Define JSON Schema for stat cards
- [ ] Layout composition (multiple components)
- [ ] Integrate with Base UI Kit chart components

---

### Feature 8.4: Ephemeral UI Lifecycle
**Linear:** [SQU-54](https://linear.app/squarehead/issue/SQU-54)

#### Outcome
Agent-generated UIs can be created, rendered, collected, and disposed without persisting.

#### What Success Looks Like
- UI appears inline in agent conversation
- User fills form, submits to agent
- Agent receives structured data
- UI can be dismissed or replaced
- No permanent UI artifacts created

#### Scope: Owned Files
- `frontend/flutter/packages/workflows/lib/src/widgets/ephemeral_ui_container.dart`

#### Tasks
- [ ] Ephemeral UI container widget
- [ ] Submission callback to agent
- [ ] Dismissal/replacement handling
- [ ] Animation for appearance/disappearance
- [ ] State cleanup on disposal

---

## Key Files

- `docs/ai-ui/` - Schema vocabulary documentation
- `square_head/apps/ai_ui/` - Backend validation service
- `frontend/flutter/packages/ai_ui/` - Flutter package
- `frontend/flutter/packages/workflows/` - Existing form renderer (dependency)

---

## References

- [SQH-EPIC-02: Base UI Kit](SQH-EPIC-02-Base-UI-Kit.md) - UI components (Feature 8.3 dependency)
- [SQH-EPIC-06: Workflow Engine](SQH-EPIC-06-Workflow-Engine.md) - Agent integration
- [SQH-EPIC-11: Frontend Apps](SQH-EPIC-11-Frontend-Apps.md) - Dynamic forms documentation
- Existing form system: `frontend/flutter/packages/workflows/lib/src/widgets/forms/`
