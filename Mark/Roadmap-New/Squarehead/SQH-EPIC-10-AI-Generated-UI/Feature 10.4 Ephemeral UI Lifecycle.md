---
status: "Not Started"
priority: "Medium"
assigned: ""
dependencies: []
linear_id: "SQU-54"
---

# Feature 10.4: Ephemeral UI Lifecycle

## Outcome

Agent-generated UIs can be created, rendered, collected, and disposed without persisting.

## What Success Looks Like

- UI appears inline in agent conversation
- User fills form, submits to agent
- Agent receives structured data
- UI can be dismissed or replaced
- No permanent UI artifacts created

## Scope: Owned Files

- `frontend/flutter/packages/workflows/lib/src/widgets/ephemeral_ui_container.dart`

## Requirements

- Ephemeral UI container widget renders inline in agent conversation
- Submission callback delivers structured data to agent
- UIs can be dismissed or replaced by subsequent agent actions
- Appearance/disappearance animations are smooth and intentional
- State is cleaned up on disposal (no memory leaks)
