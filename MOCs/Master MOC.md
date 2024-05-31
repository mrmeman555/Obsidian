---
tags:
  - MOCobject
Description: A dynamic display of all my MOC files
---


# Master MOC

## Subpages
```dataview
table file.name as "File", description as "Description", tags as "Tags", created as "Created", updated as "Updated", author as "Author", status as "Status", priority as "Priority"
from ""
where contains(tags, "MOCobject")
sort file.name asc
   ```
