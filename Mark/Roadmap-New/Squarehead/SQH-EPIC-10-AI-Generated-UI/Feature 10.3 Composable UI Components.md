---
status: "Not Started"
priority: "Medium"
assigned: ""
dependencies:
  - "[[../SQH-EPIC-04-Base-UI-Kit/Feature 4.4 Dashboard Components|SQH-EPIC-04 Feature 4.4 Dashboard Components]]"
linear_id: "SQU-53"
---

# Feature 10.3: Composable UI Components

## Outcome

The UI vocabulary includes visualization components beyond forms (charts, tables, cards).

## What Success Looks Like

- Agent can request a chart with data inline
- Agent can request a data table
- Agent can compose multiple components in a layout
- Components use Base UI Kit (SQH-EPIC-04)

## Context

Example Schema:
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

## Scope: Owned Files

- `docs/ai-ui/schema-vocabulary.md` (extended)
- `frontend/flutter/packages/ai_ui/lib/src/components/`

## Requirements

- JSON Schema specification for charts is defined
- JSON Schema specification for data tables is defined
- JSON Schema specification for stat cards is defined
- Layout composition supports multiple components in a single UI
- Components integrate with Base UI Kit chart components
