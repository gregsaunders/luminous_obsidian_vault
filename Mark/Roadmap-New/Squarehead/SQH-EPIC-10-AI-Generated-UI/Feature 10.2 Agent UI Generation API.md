---
status: "Not Started"
priority: "High"
assigned: ""
dependencies: []
linear_id: "SQU-52"
---

# Feature 10.2: Agent UI Generation API

## Outcome

Agents can request UI generation through a simple API that returns rendered UI specifications.

## What Success Looks Like

- Agent sends JSON Schema, receives UI ready for rendering
- Error handling for invalid schemas
- Schema validation before rendering
- Supports both form input and display-only modes

## Scope: Owned Files

- `square_head/apps/ai_ui/api/`
- `frontend/flutter/packages/workflows/lib/src/widgets/agent_ui_renderer.dart`

## Requirements

- API endpoint (POST /api/v1/ai-ui/generate) accepts JSON Schema and returns UI specification
- JSON Schema is validated before rendering
- Error responses include helpful messages for debugging
- Flutter widget renders agent-generated UI
- Callback mechanism delivers form submission data back to agent
- Display-only mode supports visualizations without input collection
