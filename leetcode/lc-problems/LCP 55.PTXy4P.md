---
tags:
  - leetcode/problem
questionId: "LCP 55"
title: 采集果实
translatedTitle: 采集果实
titleSlug: PTXy4P
aliases:
  - 采集果实
  - PTXy4P
  - 采集果实
lcLinks:
  - https://leetcode.com/problems/PTXy4P/
  - https://leetcode.cn/problems/PTXy4P/
lcTopics:
lcDifficulty: Easy
lcAcRate: 74.1%
similarQuestions:
grade: ⭐⭐⭐⭐⭐
likes: 10
dislikes: 0
favorites: []
created: 2025-11-16 12:09
updated: 2025-11-16 12:09
---

**Nav:** << previous: [[LCP 54.s5kipK|LCP 54.夺回据点]] | next: [[LCP 56.6UEx57|LCP 56.信物传送]] >>

---

## Description

欢迎各位勇者来到力扣新手村，本次训练内容为「采集果实」。

在新手村中，各位勇者需要采集一些果实来制作药剂。`time[i]` 表示勇者每次采集 `1～limit` 颗第 `i` 种类型的果实需要的时间（即每次最多可以采集 `limit` 颗果实）。

当前勇者需要完成「采集若干批果实」的任务， `fruits[j] = [type, num]` 表示第 `j` 批需要采集 `num` 颗 `type` 类型的果实。采集规则如下：
- 按 `fruits` 给定的顺序**依次**采集每一批次
- 采集完当前批次的果实才能开始采集下一批次
- 勇者完成当前批次的采集后将**清空背包**（即多余的果实将清空）

请计算并返回勇者完成采集任务最少需要的时间。


**示例 1：**
>输入：`time = [2,3,2], fruits = [[0,2],[1,4],[2,1]], limit = 3`
>
>输出：`10`
>
>解释：
>由于单次最多采集 3 颗
>第 0 批需要采集 2 颗第 0 类型果实，需要采集 1 次，耗时为 2\*1=2
>第 1 批需要采集 4 颗第 1 类型果实，需要采集 2 次，耗时为 3\*2=6
>第 2 批需要采集 1 颗第 2 类型果实，需要采集 1 次，耗时为 2\*1=2
>返回总耗时 2+6+2=10

**示例 2：**
>输入：`time = [1], fruits = [[0,3],[0,5]], limit = 2`
>
>输出：`5`
>
>解释：
>由于单次最多采集 2 颗
>第 0 批需要采集 3 颗第 0 类型果实，需要采集 2 次，耗时为 1\*2=2
>第 1 批需要采集 5 颗第 0 类型果实，需要采集 3 次，耗时为 1\*3=3
>需按照顺序依次采集，返回 2+3=5

**提示：**
- `1 <= time.length <= 100`
- `1 <= time[i] <= 100`
- `1 <= fruits.length <= 10^3`
- `0 <= fruits[i][0] < time.length`
- `1 <= fruits[i][1] < 10^3`
- `1 <= limit <= 100`


---

[提交记录](https://leetcode.cn/problems/PTXy4P/submissions/) | [题解](https://leetcode.cn/problems/PTXy4P/solution/)


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