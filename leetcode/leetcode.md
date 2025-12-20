---
tags: 
aliases:
  - LeetCode
cssclasses:
  - noyaml
---

# LeetCode Dashboard

```base
views:
  - type: paginated-table
    name: LeetCode Problems
    order:
      - file.name
      - title
      - translatedTitle
      - lcTopics
      - lcDifficulty
      - lcAcRate
      - grade
    sort: []
    showSearchBox: true
    showFilterBar: true
    stickyHeader: true
    paginationPosition: top
    filterableColumns:
      - note.lcTopics
      - note.lcDifficulty
      - note.grade

```
