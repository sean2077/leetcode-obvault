---
tags:
  - leetcode/favorite
cssclasses: 
created: 2024-08-06 00:22
updated: 2024-08-06 00:24
---

```dataviewjs
await dv.view("leetcode/dv_pagingTable", {
    container: this.container,
    header: ["Question", "Title", "Topic", "Difficulty", "Acceptance", "Grade", "Solutions", "Notes"],
    data: dv.pages("#leetcode/problem")
        .filter((p) => p.favorites && p.favorites.some((q) => q.path === dv.current().file.path))
        .sort((p) => [parseInt(p.questionId)])
        .map((p) => [p.file.link, p.translatedTitle, p.lcTopics, p.lcDifficulty, p.lcAcRate, p.grade, p.solutions, p.notes])
        .array(),
});
```
