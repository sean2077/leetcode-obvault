---
tags:
  - leetcode/problem
questionId: "LCP 17"
title: 速算机器人
translatedTitle: 速算机器人
titleSlug: nGK0Fy
aliases:
  - 速算机器人
  - nGK0Fy
  - 速算机器人
lcLinks:
  - https://leetcode.com/problems/nGK0Fy/
  - https://leetcode.cn/problems/nGK0Fy/
lcTopics:
lcDifficulty: Easy
lcAcRate: 79.8%
similarQuestions:
grade: ⭐⭐⭐⭐⭐
likes: 51
dislikes: 0
favorites: []
created: 2025-11-16 11:17
updated: 2025-11-16 11:17
---

**Nav:** << previous: [[LCP 16.you-le-yuan-de-you-lan-ji-hua|LCP 16.游乐园的游览计划]] | next: [[LCP 18.2vYnGI|LCP 18.早餐组合]] >>

---

## Description

小扣在秋日市集发现了一款速算机器人。店家对机器人说出两个数字（记作 `x` 和 `y`），请小扣说出计算指令：
- `"A"` 运算：使 `x = 2 * x + y`；
- `"B"` 运算：使 `y = 2 * y + x`。

在本次游戏中，店家说出的数字为 `x = 1` 和 `y = 0`，小扣说出的计算指令记作仅由大写字母 `A`、`B` 组成的字符串 `s`，字符串中字符的顺序表示计算顺序，请返回最终 `x` 与 `y` 的和为多少。

**示例 1：**
>输入：`s = "AB"`
> 
>输出：`4`
> 
>解释：
>经过一次 A 运算后，x = 2, y = 0。
>再经过一次 B 运算，x = 2, y = 2。
>最终 x 与 y 之和为 4。

**提示：**
- `0 <= s.length <= 10`
- `s` 由 `'A'` 和 `'B'` 组成





---

[提交记录](https://leetcode.cn/problems/nGK0Fy/submissions/) | [题解](https://leetcode.cn/problems/nGK0Fy/solution/)


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