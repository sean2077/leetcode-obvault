---
tags:
  - leetcode/favorite
cssclasses: 
created: 2024-08-06 00:22
updated: 2024-08-06 00:24
---

## 收藏问题

```dataviewjs
await dv.view("_scripts/dv_pagingTable", {
    container: this.container,
    header: ["题号", "标题", "标题(中)", "分类", "难度", "通过率", "评分", "解法", "笔记"],
    data: dv.pages("#leetcode/problem")
        .filter((p) => p.favorites && p.favorites.some((q) => q.path === dv.current().file.path))
        .sort((p) => [parseInt(p.questionId)])
        .map((p) => [p.file.link, p.title, p.translatedTitle, p.lcTopics, p.lcDifficulty, p.lcAcRate, p.grade, p.solutions, p.notes])
        .array(),
});
```
