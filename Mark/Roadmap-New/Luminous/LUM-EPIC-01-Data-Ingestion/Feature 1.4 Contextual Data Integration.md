---
status: "Not Started"
priority: "High"
assigned: ""
dependencies:
  - "Feature 1.3"
linear_id: "SQU-20"
---

# Feature 1.4: Contextual Data Integration

**Linear:** [SQU-20](https://linear.app/squarehead/issue/SQU-20)

**Used By:**
- [[../LUM-EPIC-03-Customer-Dashboard/Feature 3.6 Correlation View|LUM-EPIC-03 Feature 3.6]] - Correlation View

---

## Outcome

An analyst can view weather and environmental conditions alongside biosensor results to identify correlations.

---

## What Success Looks Like

- Analyst views sample results
- Sees weather data for that date/location (temperature, precipitation, wind)
- Can filter or sort by weather conditions
- System automatically fetches historical weather for sample dates

---

## Context

NA concentrations may correlate with weather events (rain runoff, temperature changes). Having this data alongside results enables correlation analysis.

The **Relational Context Engine** is an existing SquareHead platform capability. This feature focuses on:
1. **Ingesting** contextual data (weather, SCADA, dosing) into the platform
2. **Configuring** how that data relates to samples in the Context Engine
3. The correlation logic itself already exists - we configure it for Luminous relationships

---

## Constraints

- Must work with historical data (samples may be weeks old before upload)
- Weather API rate limits and costs to consider

---

## Scope: Owned Files

- `apps/platform_groups/luminous/services/weather.py`
- `apps/platform_groups/luminous/models/contextual.py`

---

## Requirements

- Weather data is fetched from Environment Canada API (or similar)
  - Temperature, precipitation, wind data available
  - Historical data can be fetched for past sample dates
- Contextual data schema stores environmental data in database
- Contextual data is linked to samples by date and location
- Auto-correlation reports show relationships (temperature vs. NA concentration, precipitation vs. toxicity)
- Pattern detection alerts notify when significant correlations are discovered

---

## Future Scope

- SCADA integration framework
- Dosing data integration
