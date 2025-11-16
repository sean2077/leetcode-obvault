---
tags:
  - leetcode/topic
title: Divide and Conquer
translatedName: 分治
aliases:
  - Divide and Conquer
  - 分治
lcLink: https://leetcode.com/tag/divide-and-conquer/
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

