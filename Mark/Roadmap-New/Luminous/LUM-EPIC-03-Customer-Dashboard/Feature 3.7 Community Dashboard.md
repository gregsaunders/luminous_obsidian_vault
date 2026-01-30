---
status: "Not Started"
priority: "High"
assigned: ""
dependencies:
  - "Feature 3.2"
  - "Feature 3.3"
linear_id: "TBD"
---

# Feature 3.7: Community Dashboard

**Linear:** TBD

---

## Outcome

Indigenous communities and public stakeholders can view water quality status in plain language without technical expertise.

---

## What Success Looks Like

- Community member visits public dashboard (no login required for public view)
- Sees simple status indicators: Safe / Monitoring / Concern
- Plain-language explanations: "Water quality is within normal range" vs technical metrics
- Can view trends without needing to interpret complex charts
- Educational content explains what is being measured and why it matters
- Available in multiple languages (English, French, Indigenous languages as needed)

---

## Context

The Foundry storyline promises "simplified plain-language views for communities." This serves the transparency goal of building trust with stakeholders who have waited decades for progress on tailings remediation.

---

## Scope: Owned Files

- `apps/platform_groups/luminous/views/community.py`
- `apps/platform_groups/luminous/templates/community/`
- `apps/platform_groups/luminous/ui_hints.yaml` (community view config)

---

## Requirements

- Status thresholds are defined for Safe/Monitoring/Concern levels
- Each status level has plain-language explanations that non-technical users understand
- Trend visualization uses simple indicators (up/down/stable arrows) instead of complex charts
- Educational content explains what NA monitoring measures and why it matters
- All components meet WCAG 2.1 AA accessibility standards
- Multi-language support is available (English, French, Indigenous languages)
- Public users can view the community dashboard without authentication
