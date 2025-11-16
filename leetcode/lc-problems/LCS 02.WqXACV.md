---
tags:
  - leetcode/problem
questionId: "LCS 02"
title: 完成一半题目
translatedTitle: 完成一半题目
titleSlug: WqXACV
aliases:
  - 完成一半题目
  - WqXACV
  - 完成一半题目
lcLinks:
  - https://leetcode.com/problems/WqXACV/
  - https://leetcode.cn/problems/WqXACV/
lcTopics:
lcDifficulty: Easy
lcAcRate: 65.0%
similarQuestions:
grade: ⭐⭐⭐⭐⭐
likes: 24
dislikes: 0
favorites: []
created: 2025-11-16 11:18
updated: 2025-11-16 11:18
---

**Nav:** << previous: [[LCS 01.Ju9Xwi|LCS 01.下载插件]] | next: [[LCS 03.YesdPw|LCS 03.主题空间]] >>

---

## Description

有 `N` 位扣友参加了微软与力扣举办了「以扣会友」线下活动。主办方提供了 `2*N` 道题目，整型数组 `questions` 中每个数字对应了每道题目所涉及的知识点类型。
若每位扣友选择不同的一题，请返回被选的 `N` 道题目至少包含多少种知识点类型。


**示例 1：**
>输入：`questions = [2,1,6,2]`
>
>输出：`1`
>
>解释：有 2 位扣友在 4 道题目中选择 2 题。
> 可选择完成知识点类型为 2 的题目时，此时仅一种知识点类型
> 因此至少包含 1 种知识点类型。

**示例 2：**
>输入：`questions = [1,5,1,3,4,5,2,5,3,3,8,6]`
>
>输出：`2`
>
>解释：有 6 位扣友在 12 道题目中选择题目，需要选择 6 题。
> 选择完成知识点类型为 3、5 的题目，因此至少包含 2 种知识点类型。



**提示：**
- `questions.length == 2*n`
- `2 <= questions.length <= 10^5`
- `1 <= questions[i] <= 1000`


---

[提交记录](https://leetcode.cn/problems/WqXACV/submissions/) | [题解](https://leetcode.cn/problems/WqXACV/solution/)


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