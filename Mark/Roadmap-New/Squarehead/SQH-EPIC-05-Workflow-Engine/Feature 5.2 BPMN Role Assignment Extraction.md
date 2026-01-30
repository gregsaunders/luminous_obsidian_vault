---
status: "Not Started"
priority: "Medium"
assigned: ""
dependencies: []
linear_id: ""
---

# Feature 5.2: BPMN Role Assignment Extraction

## Outcome

Role assignments from BPMN extensions are parsed and used for dynamic task assignment.

## What Success Looks Like

- BPMN files can specify role assignments
- Roles are extracted during workflow parsing
- Task assignment respects role specifications
- Dynamic assignment based on workflow context works

## Scope: Owned Files

- `apps/workflows/engine.py`

## Requirements

- Parse role assignments from BPMN extensions
- Dynamic assignment based on workflow context
