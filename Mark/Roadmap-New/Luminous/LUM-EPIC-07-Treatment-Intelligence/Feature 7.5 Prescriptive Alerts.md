---
status: "Not Started"
priority: "Medium"
assigned: ""
dependencies:
  - "Feature 7.1"
  - "Feature 7.2"
  - "Feature 7.4"
  - "SQH-EPIC-06 (Anomaly Detection Service)"
linear_id: "TBD"
---

# Feature 7.5: Prescriptive Alerts

**Linear:** TBD

---

## Outcome

Operators receive proactive recommendations when conditions suggest an action should be taken, rather than only reacting to problems.

---

## What Success Looks Like

- Operator receives alert: "Flow rate in Cell 3 should be increased based on current conditions"
- Alert includes: recommended action, confidence level, expected benefit, similar past events
- Operator can view supporting evidence before acting
- Alerts respect notification preferences (don't spam)
- Alert history shows which were acted on and outcomes

---

## Scope: Owned Files

- `apps/platform_groups/luminous/services/prescriptive_alerts.py`
- `apps/platform_groups/luminous/notifications/` (Luminous-specific alert triggers)

---

## Tasks

- [ ] Define alert conditions (when to recommend action vs. wait)
- [ ] Build prescriptive alert service
- [ ] Integrate with platform notification system
- [ ] Confidence scoring for recommendations
- [ ] Similar event retrieval for supporting evidence
- [ ] Alert effectiveness tracking
