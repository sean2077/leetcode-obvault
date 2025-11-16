---
tags:
  - leetcode/problem
questionId: "LCP 68"
title: 美观的花束
translatedTitle: 美观的花束
titleSlug: 1GxJYY
aliases:
  - 美观的花束
  - 1GxJYY
  - 美观的花束
lcLinks:
  - https://leetcode.com/problems/1GxJYY/
  - https://leetcode.cn/problems/1GxJYY/
lcTopics:
lcDifficulty: Medium
lcAcRate: 68.0%
similarQuestions:
grade: ⭐⭐⭐⭐⭐
likes: 36
dislikes: 0
favorites: []
created: 2025-11-16 11:17
updated: 2025-11-16 11:17
---

**Nav:** << previous: [[LCP 67.KnLfVT|LCP 67.装饰树]] | next: [[LCP 69.rMeRt2|LCP 69.Hello LeetCode!]] >>

---

## Description

力扣嘉年华的花店中从左至右摆放了一排鲜花，记录于整型一维矩阵 `flowers` 中每个数字表示该位置所种鲜花的品种编号。你可以选择一段区间的鲜花做成插花，且不能丢弃。
在你选择的插花中，如果每一品种的鲜花数量都不超过 `cnt` 朵，那么我们认为这束插花是 「美观的」。
> - 例如：`[5,5,5,6,6]` 中品种为 `5` 的花有 `3` 朵， 品种为 `6` 的花有 `2` 朵，**每一品种** 的数量均不超过 `3`

请返回在这一排鲜花中，共有多少种可选择的区间，使得插花是「美观的」。

**注意：**
- 答案需要以 `1e9 + 7 (1000000007)` 为底取模，如：计算初始结果为：`1000000008`，请返回 `1`

**示例 1：**
>输入：`flowers = [1,2,3,2], cnt = 1`
>
>输出：`8`
>
>解释：相同的鲜花不超过 `1` 朵，共有 `8` 种花束是美观的；
>长度为 `1` 的区间 `[1]、[2]、[3]、[2]` 均满足条件，共 `4` 种可选择区间
>长度为 `2` 的区间 `[1,2]、[2,3]、[3,2]` 均满足条件，共 `3` 种可选择区间
>长度为 `3` 的区间 `[1,2,3]` 满足条件，共 `1` 种可选择区间。
>区间 `[2,3,2],[1,2,3,2]` 都包含了 `2` 朵鲜花 `2` ，不满足条件。
>返回总数 `4+3+1 = 8`

**示例 2：**
>输入：`flowers = [5,3,3,3], cnt = 2`
>
>输出：`8`

**提示：**
- `1 <= flowers.length <= 10^5`
- `1 <= flowers[i] <= 10^5`
- `1 <= cnt <= 10^5`


---

[提交记录](https://leetcode.cn/problems/1GxJYY/submissions/) | [题解](https://leetcode.cn/problems/1GxJYY/solution/)


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