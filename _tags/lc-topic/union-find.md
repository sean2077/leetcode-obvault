---
tags:
  - leetcode/topic
title: Union Find
translatedName: 并查集
aliases:
  - Union Find
  - 并查集
lcLink: https://leetcode.com/tag/union-find/
cssclasses: []
created: 2024-08-05 18:23
updated:
---


## 相关问题

```dataviewjs
await dv.view("_scripts/dv_pagingTable", {
    container: this.container,
    header: ["题号", "标题", "标题(中)", "分类", "难度", "通过率", "评分", "解法", "笔记"],
    data: dv.pages("#leetcode/problem")
        .filter((p) => p.lcTopics && p.lcTopics.some((q) => q.path === dv.current().file.path))
        .sort((p) => [parseInt(p.questionId)])
        .map((p) => [p.file.link, p.title, p.translatedTitle, p.lcTopics, p.lcDifficulty, p.lcAcRate, p.grade, p.solutions, p.notes])
        .array(),
});
```

