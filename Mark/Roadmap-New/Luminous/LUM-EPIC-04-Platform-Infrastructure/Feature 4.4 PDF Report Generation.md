---
status: "Not Started"
priority: "Medium"
assigned: ""
dependencies:
  - "LUM-EPIC-01 Feature 1.1"
  - "LUM-EPIC-01 Feature 1.2"
  - "LUM-EPIC-01 Feature 1.3"
  - "LUM-EPIC-03 Feature 3.2"
  - "LUM-EPIC-03 Feature 3.3"
linear_id: "SQU-25"
---

# Feature 4.4: PDF Report Generation

**Linear:** [SQU-25](https://linear.app/squarehead/issue/SQU-25)

---

## Outcome

A customer can download a professional PDF report to share with stakeholders who don't have platform access.

---

## What Success Looks Like

- Customer clicks "Generate Report" in dashboard
- Selects date range and locations to include
- Downloads PDF with summary, trends, and data table
- Report is branded and professional-looking
- Can be attached to regulatory filings

---

## Scope: Owned Files

- `apps/platform_groups/luminous/reports/` (report generation)
- `apps/platform_groups/luminous/templates/pdf/` (report templates)

---

## Requirements

- Report template includes summary, trends, and data table sections
- PDF generation produces downloadable documents
- Charts and visualizations are rendered in PDF output
- Reports can be generated on-demand from the dashboard
- AER compliance template is regulator-ready with data provenance
- Indigenous community template is visual, accessible, and uses plain language

---

## Future Scope

- Scheduled report emails
