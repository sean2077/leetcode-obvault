---
tags:
  - leetcode/favorite
cssclasses: 
created: 2024-08-06 00:22
updated: 2024-08-06 00:24
---

```base
views:
  - type: paginated-table
    name: Relative Problems
    filters:
      and:
        - file.tags.contains("leetcode/problem")
        - favorites.contains(this.file)
    order:
      - file.name
      - translatedTitle
      - lcTopics
      - lcDifficulty
      - lcAcRate
      - grade

```
