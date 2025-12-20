---
tags:
  - leetcode/topic
title: Brainteaser
translatedName: 脑筋急转弯
aliases:
  - Brainteaser
  - 脑筋急转弯
lcLink: https://leetcode.com/tag/brainteaser/
cssclasses: []
created: 2024-08-05 18:23
updated:
---

```base
views:
  - type: paginated-table
    name: Relative Problems
    filters:
      and:
        - file.tags.contains("leetcode/problem")
        - lcTopics.contains(this.file)
    order:
      - file.name
      - translatedTitle
      - lcTopics
      - lcDifficulty
      - lcAcRate
      - grade

```