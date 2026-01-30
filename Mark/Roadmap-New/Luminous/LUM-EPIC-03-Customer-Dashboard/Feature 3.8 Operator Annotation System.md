---
status: "Not Started"
priority: "Medium"
assigned: ""
dependencies:
  - "Feature 3.2"
  - "Feature 3.3"
linear_id: "TBD"
---

# Feature 3.8: Operator Annotation System

**Linear:** TBD

**Used By:**
- [[../LUM-EPIC-07-Treatment-Intelligence/Feature 7.4 Intervention Outcome Tracking|LUM-EPIC-07 Feature 7.4]] - Intervention Outcome Tracking

---

## Outcome

Operators can capture institutional knowledge by annotating events, samples, and trends with notes about what happened and what actions were taken.

---

## What Success Looks Like

- Operator views a spike in toxicity readings
- Clicks to add annotation: "Spike caused by heavy rainfall runoff. Increased flow to Cell 3, resolved within 48 hours."
- Annotation is permanently linked to that data point/period
- Future operators viewing similar conditions see the annotation
- Search finds past annotations matching current conditions
- Knowledge compounds over time rather than being lost to turnover

---

## Context

The Foundry storyline emphasizes that "institutional knowledge remains trapped in PDF reports and spreadsheets. Personnel turnover means hard-won lessons get lost." This feature captures operator knowledge directly in the system.

---

## Scope: Owned Files

- `apps/platform_groups/luminous/models/annotation.py`
- `apps/platform_groups/luminous/api/annotations.py`
- `apps/platform_groups/luminous/services/annotation_search.py`

---

## Requirements

- Annotation model stores target type, target ID, content, operator, and timestamp
- Annotations can be created directly from any dashboard view
- Annotations are linked to samples, results, time periods, and events
- Tags categorize annotations by type: cause, action, outcome
- Search finds past annotations matching keywords or criteria
- "Similar situation" suggestions appear when viewing anomalies
- Annotation visibility can be set to team-only or public
