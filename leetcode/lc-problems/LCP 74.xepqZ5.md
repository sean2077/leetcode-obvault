---
tags:
  - leetcode/problem
questionId: "LCP 74"
title: 最强祝福力场
translatedTitle: 最强祝福力场
titleSlug: xepqZ5
aliases:
  - 最强祝福力场
  - xepqZ5
  - 最强祝福力场
lcLinks:
  - https://leetcode.com/problems/xepqZ5/
  - https://leetcode.cn/problems/xepqZ5/
lcTopics:
lcDifficulty: Medium
lcAcRate: 36.2%
similarQuestions:
grade: ⭐⭐⭐⭐⭐
likes: 42
dislikes: 0
favorites: []
created: 2025-11-16 12:09
updated: 2025-11-16 12:09
---

**Nav:** << previous: [[LCP 73.0Zeoeg|LCP 73.探险营地]] | next: [[LCP 75.rdmXM7|LCP 75.传送卷轴]] >>

---

## Description

小扣在探索丛林的过程中，无意间发现了传说中“落寞的黄金之都”。而在这片建筑废墟的地带中，小扣使用探测仪监测到了存在某种带有「祝福」效果的力场。
经过不断的勘测记录，小扣将所有力场的分布都记录了下来。`forceField[i] = [x,y,side]` 表示第 `i` 片力场将覆盖以坐标 `(x,y)` 为中心，边长为 `side` 的正方形区域。

若任意一点的 **力场强度** 等于覆盖该点的力场数量，请求出在这片地带中 **力场强度** 最强处的 **力场强度**。

**注意：** 
- 力场范围的边缘同样被力场覆盖。

**示例 1：**
>输入：
>`forceField = [[0,0,1],[1,0,1]]`
>
>输出：`2`
>
>解释：如图所示，（0.5, 0) 处力场强度最强为 2， （0.5，-0.5）处力场强度同样是 2。
![image.png](https://pic.leetcode.cn/1681805536-zGfghe-image.png){:width=400px}


**示例 2：**
>输入：
>`forceField = [[4,4,6],[7,5,3],[1,6,2],[5,6,3]]`
>
>输出：`3`
>
>解释：如下图所示，
>`forceField[0]、forceField[1]、forceField[3]` 重叠的区域力场强度最大，返回 `3`
![image.png](https://pic.leetcode.cn/1681805437-HQkyZS-image.png){:width=500px}



**提示：**
- `1 <= forceField.length <= 100`
- `forceField[i].length == 3`
- `0 <= forceField[i][0], forceField[i][1] <= 10^9`
- `1 <= forceField[i][2] <= 10^9`


---

[提交记录](https://leetcode.cn/problems/xepqZ5/submissions/) | [题解](https://leetcode.cn/problems/xepqZ5/solution/)


## Solutions & Notes

```base
properties:
  note.updated:
    displayName: Last Updated
  note.relative_links:
    displayName: Related Links
  note.desc:
    displayName: Description
  note.grade:
    displayName: Rating
  note.program_language:
    displayName: Language
  note.time_complexity:
    displayName: TC
  note.space_complexity:
    displayName: SC
views:
  - type: table
    name: Solutions & Notes
    filters:
      and:
        - file.hasLink(this.file)
        - file.tags.containsAny("leetcode/solution", "leetcode/note")
    order:
      - file.name
      - desc
      - program_language
      - time_complexity
      - space_complexity
      - grade
      - relative_links
      - updated
    sort:
      - property: grade
        direction: ASC
      - property: time_complexity
        direction: ASC
      - property: program_language
        direction: ASC
    columnSize:
      file.name: 104
      note.space_complexity: 65
      note.grade: 126

```

## Similar Problems

```base
properties:
  note.lcTopics:
    displayName: Topics
  note.lcAcRate:
    displayName: AC Rate
  note.favorites:
    displayName: Favorites
  note.grade:
    displayName: Rating
  note.translatedTitle:
    displayName: Title (CN)
  note.lcDifficulty:
    displayName: Difficulty
views:
  - type: table
    name: Similar Problems
    filters:
      and:
        - file.hasLink(this.file)
        - similarQuestions.contains(this.file)
    order:
      - file.name
      - translatedTitle
      - lcTopics
      - lcDifficulty
      - lcAcRate
      - grade
      - favorites
    sort:
      - property: file.name
        direction: ASC
      - property: lcTopics
        direction: DESC
    columnSize:
      note.translatedTitle: 240
      note.lcTopics: 347
      note.lcAcRate: 75
      note.grade: 122

```