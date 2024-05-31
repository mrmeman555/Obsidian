---
tags:
  - MOCobject
Description: Items to review regularly. can be related to any topic.
des:
---
**Description:**  
{{This note is meant to house notes i review and use on a **regular basis** for personnl development and process development related to any aspect of my life, particularly my health, my study strategy, etc.}}


## Subpages
```dataview
table file.link as "Subpage", file.frontmatter.description as "Description", file.frontmatter.created as "Created", file.frontmatter.updated as "Updated", file.frontmatter.tags as "Tags", file.frontmatter.status as "Status"
from #MOC-DailyHabits
where contains(file.frontmatter.tags, "Habits")
sort file.frontmatter.created desc
```

## Links
- Back to [[Master MOC]]