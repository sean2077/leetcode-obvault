---
tags:
  - leetcode/topic
title: Breadth-First Search
translatedName: 广度优先搜索
aliases:
  - Breadth-First Search
  - 广度优先搜索
lcLink: https://leetcode.com/tag/breadth-first-search/
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

