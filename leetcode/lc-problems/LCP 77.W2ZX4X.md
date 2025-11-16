---
tags:
  - leetcode/problem
questionId: "LCP 77"
title: 符文储备
translatedTitle: 符文储备
titleSlug: W2ZX4X
aliases:
  - 符文储备
  - W2ZX4X
  - 符文储备
lcLinks:
  - https://leetcode.com/problems/W2ZX4X/
  - https://leetcode.cn/problems/W2ZX4X/
lcTopics:
lcDifficulty: Easy
lcAcRate: 68.9%
similarQuestions:
grade: ⭐⭐⭐⭐⭐
likes: 5
dislikes: 0
favorites: []
created: 2025-11-16 12:09
updated: 2025-11-16 12:09
---

**Nav:** << previous: [[LCP 76.1ybDKD|LCP 76.魔法棋盘]] | next: [[LCP 78.Nsibyl|LCP 78.城墙防线]] >>

---

## Description

远征队在出发前需要携带一些「符文」，作为后续的冒险储备。`runes[i]` 表示第 `i` 枚符文的魔力值。

他们将从中选取若干符文进行携带，并对这些符文进行重新排列，以确保任意相邻的两块符文之间的魔力值相差不超过 `1`。

请返回他们能够携带的符文 **最大数量**。

**示例 1：**
>输入：`runes = [1,3,5,4,1,7]`
>
>输出：`3`
>
>解释：最佳的选择方案为[3,5,4]
>将其排列为 [3,4,5] 后，任意相邻的两块符文魔力值均不超过 `1`，携带数量为 `3`
>其他满足条件的方案为 [1,1] 和 [7]，数量均小于 3。
>因此返回可携带的最大数量 `3`。

**示例 2：**
>输入：`runes = [1,1,3,3,2,4]`
>
>输出：`6`
>
>解释：排列为 [1,1,2,3,3,4]，可携带所有的符文

**提示：**
- `1 <= runes.length <= 10^4`
- `0 <= runes[i] <= 10^4`



---

[提交记录](https://leetcode.cn/problems/W2ZX4X/submissions/) | [题解](https://leetcode.cn/problems/W2ZX4X/solution/)


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