
```dataview
TABLE 
    topic as "Topic",
    file.mtime as "Last Activity"
FROM "Discussions"
WHERE file.name != "index"
SORT file.mtime desc
```
