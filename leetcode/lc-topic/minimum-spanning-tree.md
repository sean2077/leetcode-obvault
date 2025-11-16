---
tags:
  - leetcode/topic
title: Minimum Spanning Tree
translatedName: 最小生成树
aliases:
  - Minimum Spanning Tree
  - 最小生成树
lcLink: https://leetcode.com/tag/minimum-spanning-tree/
cssclasses: []
created: 2024-08-05 18:23
updated:
---



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

