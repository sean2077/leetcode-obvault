---
tags:
  - leetcode/problem
questionId: "LCS 01"
title: 下载插件
translatedTitle: 下载插件
titleSlug: Ju9Xwi
aliases:
  - 下载插件
  - Ju9Xwi
  - 下载插件
lcLinks:
  - https://leetcode.com/problems/Ju9Xwi/
  - https://leetcode.cn/problems/Ju9Xwi/
lcTopics:
lcDifficulty: Easy
lcAcRate: 53.6%
similarQuestions:
grade: ⭐⭐⭐⭐⭐
likes: 53
dislikes: 0
favorites: []
created: 2025-11-16 11:18
updated: 2025-11-16 11:18
---

**Nav:** << previous: [[LCR 194.er-cha-shu-de-zui-jin-gong-gong-zu-xian-lcof|LCR 194.二叉树的最近公共祖先]] | next: [[LCS 02.WqXACV|LCS 02.完成一半题目]] >>

---

## Description

小扣打算给自己的 **VS code** 安装使用插件，初始状态下带宽每分钟可以完成 `1` 个插件的下载。假定每分钟选择以下两种策略之一:
- 使用当前带宽下载插件
- 将带宽加倍（下载插件数量随之加倍）

请返回小扣完成下载 `n` 个插件最少需要多少分钟。

注意：实际的下载的插件数量可以超过 `n` 个


**示例 1：**
>输入：`n = 2`
>
>输出：`2`
>
>解释：
> 以下两个方案，都能实现 2 分钟内下载 2 个插件
>- 方案一：第一分钟带宽加倍，带宽可每分钟下载 2 个插件；第二分钟下载 2 个插件
>- 方案二：第一分钟下载 1 个插件，第二分钟下载 1 个插件

**示例 2：**
>输入：`n = 4`
>
>输出：`3`
>
>解释：
> 最少需要 3 分钟可完成 4 个插件的下载，以下是其中一种方案:
> 第一分钟带宽加倍，带宽可每分钟下载 2 个插件;
> 第二分钟下载 2 个插件;
> 第三分钟下载 2 个插件。



**提示：**
- `1 <= n <= 10^5`



---

[提交记录](https://leetcode.cn/problems/Ju9Xwi/submissions/) | [题解](https://leetcode.cn/problems/Ju9Xwi/solution/)


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