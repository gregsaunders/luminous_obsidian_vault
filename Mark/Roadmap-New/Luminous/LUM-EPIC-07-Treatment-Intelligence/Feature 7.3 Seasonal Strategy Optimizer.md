---
status: "Not Started"
priority: "High"
assigned: ""
dependencies:
  - "Feature 7.1"
  - "LUM-EPIC-02 Feature 2.4"
linear_id: "TBD"
---

# Feature 7.3: Seasonal Strategy Optimizer

**Linear:** TBD

---

## Outcome

Operations managers can see temperature-based recommendations for treatment season start/end rather than relying on calendar dates.

---

## What Success Looks Like

- Manager views seasonal analysis dashboard
- System shows temperature thresholds where treatment effectiveness drops
- Recommendation: "Based on current forecast, extend operation 2 weeks beyond calendar shutdown"
- Historical comparison: "Last year's early shutdown cost an estimated $X in lost treatment capacity"
- Can model scenarios: "What if we operate until temperature drops below Y?"

---

## Scope: Owned Files

- `apps/platform_groups/luminous/services/seasonal_analyzer.py`
- `apps/platform_groups/luminous/models/seasonal_strategy.py`

---

## Tasks

- [ ] Identify temperature thresholds from historical data (when does effectiveness drop?)
- [ ] Build seasonal analysis service
- [ ] Integrate weather forecast data for projections
- [ ] Calculate value of extended operation (days x throughput x cost)
- [ ] Create scenario modeling capability
- [ ] Seasonal recommendation generation
