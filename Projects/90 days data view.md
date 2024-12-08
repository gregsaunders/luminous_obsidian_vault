---
folder: ""
---

## Greg

```dataview
TABLE without id
  work_item_id as "Work Item ID",
  folder as "Folder",
  file.link as "Task",
  status as "Status",
  due-date as "Due Date",
  responsible as "Responsible",
  accountable as "Accountable",
  consulted as "Consulted",
  informed as "Informed"
FROM "Projects/90 days"
WHERE responsible = "Greg"
SORT due-date asc
```

## Jeff

```dataview
TABLE without id
  work_item_id as "Work Item ID",
  folder as "Folder",
  file.link as "Task",
  status as "Status",
  due-date as "Due Date",
  responsible as "Responsible",
  accountable as "Accountable",
  consulted as "Consulted",
  informed as "Informed"
FROM "Projects/90 days"
WHERE responsible = "Jeff"
SORT due-date asc
```

## Shawn

```dataview
TABLE without id
  work_item_id as "Work Item ID",
  folder as "Folder",
  file.link as "Task",
  status as "Status",
  due-date as "Due Date",
  responsible as "Responsible",
  accountable as "Accountable",
  consulted as "Consulted",
  informed as "Informed"
FROM "Projects/90 days"
WHERE responsible = "Shawn"
SORT due-date asc
```
[2024-12-08 3:02 PM]
