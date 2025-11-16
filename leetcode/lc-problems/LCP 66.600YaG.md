---
tags:
  - leetcode/problem
questionId: "LCP 66"
title: 最小展台数量
translatedTitle: 最小展台数量
titleSlug: 600YaG
aliases:
  - 最小展台数量
  - 600YaG
  - 最小展台数量
lcLinks:
  - https://leetcode.com/problems/600YaG/
  - https://leetcode.cn/problems/600YaG/
lcTopics:
lcDifficulty: Easy
lcAcRate: 77.6%
similarQuestions:
grade: ⭐⭐⭐⭐⭐
likes: 13
dislikes: 0
favorites: []
created: 2025-11-16 11:17
updated: 2025-11-16 11:17
---

**Nav:** << previous: [[LCP 65.3aqs1c|LCP 65.舒适的湿度]] | next: [[LCP 67.KnLfVT|LCP 67.装饰树]] >>

---

## Description

力扣嘉年华将举办一系列展览活动，后勤部将负责为每场展览提供所需要的展台。
已知后勤部得到了一份需求清单，记录了近期展览所需要的展台类型， `demand[i][j]` 表示第 `i` 天展览时第 `j` 个展台的类型。
在满足每一天展台需求的基础上，请返回后勤部需要准备的 **最小** 展台数量。

**注意：**
- 同一展台在不同天中可以重复使用。

**示例 1：**
>输入：`demand = ["acd","bed","accd"]`
>
>输出：`6`
>
>解释：
>第 `0` 天需要展台 `a、c、d`；
>第 `1` 天需要展台 `b、e、d`；
>第 `2` 天需要展台 `a、c、c、d`；
>因此，后勤部准备 `abccde` 的展台，可以满足每天的展览需求;

**示例 2：**
>输入：`demand = ["abc","ab","ac","b"]`
>
>输出：`3`


**提示：**
- `1 <= demand.length,demand[i].length <= 100`
- `demand[i][j]` 仅为小写字母


---

[提交记录](https://leetcode.cn/problems/600YaG/submissions/) | [题解](https://leetcode.cn/problems/600YaG/solution/)


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
    name: Table
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