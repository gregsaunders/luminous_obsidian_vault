---
status: "Not Started"
priority: "High"
assigned: ""
dependencies: []
linear_id: ""
---

# Feature 4.7: List/Table Component

## Outcome

A comprehensive, reusable list/table component that Platform Groups use to display tabular data with full user customization.

## What Success Looks Like

- Developer renders a data table by passing columns and data
- User can hide/show columns via column visibility menu
- User preferences persist across sessions
- Tables handle large datasets efficiently with virtualization
- Sorting, filtering, and selection work consistently across all tables

## Context

This is a foundational UI component used across all Platform Groups for displaying lists of records (invoices, customers, sensor readings, etc.). The shell's App Content Pane renders this component.

**Used By:**
- All Platform Groups displaying record lists
- [[../SQH-EPIC-10-AI-Generated-UI/00-AI-Generated-UI|SQH-EPIC-10]] Feature 10.3 - AI-generated table views

## Scope: Owned Files

- `frontend/flutter/packages/ui/lib/components/data_table/`
- `frontend/flutter/packages/ui/lib/components/data_table/data_table.dart`
- `frontend/flutter/packages/ui/lib/components/data_table/column_visibility_menu.dart`
- `frontend/flutter/packages/ui/lib/components/data_table/table_header.dart`
- `frontend/flutter/packages/ui/lib/components/data_table/table_row.dart`

## Requirements

**Core Table:**
- Data table component accepts typed column definitions
- Column headers display labels and sort indicators
- Table rows render cells with appropriate formatting
- Loading state shows skeleton rows
- Empty state displays customizable message
- Error state offers retry action

**Column Management:**
- Column visibility toggle menu allows hiding/showing columns
- Column visibility preferences persist per-table and per-user
- Column borders are draggable for resizing
- Columns can be reordered via drag-and-drop
- Column widths respect minimum/maximum constraints
- Columns can be pinned (frozen) left or right

**Sorting & Filtering:**
- Single-column sort activates on header click
- Multi-column sort activates on shift+click
- Sort indicators show ascending/descending state
- Column filter popover appears on filter icon click
- Text filters support: contains, starts with, equals
- Numeric filters support: greater than, less than, between
- Date filters support: before, after, range
- Active filters show indicator on column header

**Row Selection:**
- Single-select mode behaves like radio buttons
- Multi-select mode adds checkbox column
- Select all / deselect all works correctly
- Selection callback provides selected row data
- Rows highlight on hover
- Selected rows show distinct styling

**Performance:**
- Virtualized scrolling handles large datasets efficiently
- Lazy loading / infinite scroll loads data as needed
- Re-renders are optimized on data changes

**Export:**
- Visible data can be exported to CSV
- Selected rows can be exported to CSV
- Selected rows can be copied to clipboard
