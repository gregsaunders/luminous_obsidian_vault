---
status: "Not Started"
priority: "Low"
assigned: ""
dependencies:
  - "SquareHead EPIC-11 (Frontend Apps)"
  - "Pilot feedback"
linear_id: "SQU-32"
---

# Feature 5.5: Custom Flutter Field App

**Linear:** [SQU-32](https://linear.app/squarehead/issue/SQU-32)
**Timeline:** Post-Pilot (not for Q2 2026 pilot)

---

## Outcome

Field technicians use a native Flutter app integrated with the platform instead of Fulcrum.

---

## Context

MVP uses Fulcrum for fast deployment. Post-pilot, a custom Flutter app may provide better integration, offline sync, and user experience.

---

## Why Post-Pilot

- Fulcrum is sufficient for pilot
- Custom app requires Flutter mobile infrastructure (SquareHead EPIC-11)
- Need pilot feedback to inform requirements

---

## Scope: Owned Files (Future)

- `frontend/flutter/apps/mobile/lib/features/field_capture/`

---

## Requirements (Future)

- Flutter mobile app is scaffolded and buildable
- Barcode scanner reads sample container barcodes
- Form captures all required metadata fields
- App works offline and syncs when connectivity is restored
- API integration sends data to platform backend
