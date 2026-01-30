---
status: "Not Started"
priority: "High"
assigned: ""
dependencies:
  - "Feature 7.1"
linear_id: "TBD"
---

# Feature 7.2: Cell Routing Recommendations

**Linear:** TBD

---

## Outcome

Operators receive recommendations for which cells to route flow to based on current conditions and historical performance.

---

## What Success Looks Like

- Operator views current conditions (temperature, flow rate, recent toxicity)
- System displays recommended routing with confidence level
- Recommendation includes rationale ("Cell 3 performed 26% better under similar conditions in August 2025")
- Operator can accept, modify, or dismiss recommendation
- System tracks which recommendations were followed

---

## Scope: Owned Files

- `apps/platform_groups/luminous/services/routing_recommender.py`
- `apps/platform_groups/luminous/models/recommendation.py`

---

## Tasks

- [ ] Define conditions that affect cell performance (temperature, flow rate, time of year)
- [ ] Build condition-matching logic (find similar historical periods)
- [ ] Create recommendation model (recommendation, confidence, rationale, status)
- [ ] Build routing recommendation service
- [ ] API endpoint for current recommendations
- [ ] Recommendation acceptance/dismissal tracking
