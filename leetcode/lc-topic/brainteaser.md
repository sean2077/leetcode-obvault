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


## 相关问题

```dataviewjs
await dv.view("leetcode/dv_pagingTable", {
    container: this.container,
    header: ["Question", "Title", "Topics", "Difficulty", "Acceptance", "Rating", "Solutions", "Notes"],
    data: dv.pages("#leetcode/problem")
        .filter((p) => p.lcTopics && p.lcTopics.some((q) => q.path === dv.current().file.path))
        .sort((p) => [parseInt(p.questionId)])
        .map((p) => [p.file.link, p.translatedTitle, p.lcTopics, p.lcDifficulty, p.lcAcRate, p.grade, p.solutions, p.notes])
        .array(),
});
```

