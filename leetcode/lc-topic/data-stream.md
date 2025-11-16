---
tags:
  - leetcode/topic
title: Data Stream
translatedName: 数据流
aliases:
  - Data Stream
  - 数据流
lcLink: https://leetcode.com/tag/data-stream/
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

