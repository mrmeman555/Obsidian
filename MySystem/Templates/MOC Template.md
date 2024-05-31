---
tags:
  - MOC
Description: "{This is a template used for producing properly formatted files.}"
parent_moc: Master MOC
related_notes:
  - Master MOC.md
author: Aaron
status: in-progress
priority:
  - medium
created: <% tp.date.now("YYYY-MM-DD") %>
updated: <% tp.date.now("YYYY-MM-DD") %>
---

# {{title}}

**Description:**  
{{description}}

## Subpages
```dataview
table file.link as "Subpage", file.frontmatter.description as "Description"
from [[{{title}}]]
```
