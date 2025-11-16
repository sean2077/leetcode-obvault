---
tags:
  - leetcode/problem
questionId: "LCP 22"
title: 黑白方格画
translatedTitle: 黑白方格画
titleSlug: ccw6C7
aliases:
  - 黑白方格画
  - ccw6C7
  - 黑白方格画
lcLinks:
  - https://leetcode.com/problems/ccw6C7/
  - https://leetcode.cn/problems/ccw6C7/
lcTopics:
lcDifficulty: Easy
lcAcRate: 36.0%
similarQuestions:
grade: ⭐⭐⭐⭐⭐
likes: 75
dislikes: 0
favorites: []
created: 2025-11-16 12:09
updated: 2025-11-16 12:09
---

**Nav:** << previous: [[LCP 21.Za25hA|LCP 21.追逐游戏]] | next: [[LCP 23.er94lq|LCP 23.魔术排列]] >>

---

## Description

小扣注意到秋日市集上有一个创作黑白方格画的摊位。摊主给每个顾客提供一个固定在墙上的白色画板，画板不能转动。画板上有 `n * n` 的网格。绘画规则为，小扣可以选择任意多行以及任意多列的格子涂成黑色（选择的整行、整列均需涂成黑色），所选行数、列数均可为 0。

小扣希望最终的成品上需要有 `k` 个黑色格子，请返回小扣共有多少种涂色方案。

注意：两个方案中任意一个相同位置的格子颜色不同，就视为不同的方案。

**示例 1：**
>输入：`n = 2, k = 2`
>
>输出：`4`
> 
>解释：一共有四种不同的方案：
>第一种方案：涂第一列；
>第二种方案：涂第二列；
>第三种方案：涂第一行；
>第四种方案：涂第二行。

**示例 2：**
>输入：`n = 2, k = 1`
> 
>输出：`0`
> 
>解释：不可行，因为第一次涂色至少会涂两个黑格。

**示例 3：**
>输入：`n = 2, k = 4`
> 
>输出：`1`
>
>解释：共有 2*2=4 个格子，仅有一种涂色方案。

**限制：**
- `1 <= n <= 6`
- `0 <= k <= n * n`





---

[提交记录](https://leetcode.cn/problems/ccw6C7/submissions/) | [题解](https://leetcode.cn/problems/ccw6C7/solution/)


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