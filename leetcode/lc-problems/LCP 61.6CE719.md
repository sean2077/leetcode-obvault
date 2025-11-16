---
tags:
  - leetcode/problem
questionId: "LCP 61"
title: 气温变化趋势
translatedTitle: 气温变化趋势
titleSlug: 6CE719
aliases:
  - 气温变化趋势
  - 6CE719
  - 气温变化趋势
lcLinks:
  - https://leetcode.com/problems/6CE719/
  - https://leetcode.cn/problems/6CE719/
lcTopics:
lcDifficulty: Easy
lcAcRate: 70.1%
similarQuestions:
grade: ⭐⭐⭐⭐⭐
likes: 35
dislikes: 0
favorites: []
created: 2025-11-16 11:17
updated: 2025-11-16 11:17
---

**Nav:** << previous: [[LCP 60.WInSav|LCP 60.力扣泡泡龙]] | next: [[LCP 62.D9PW8w|LCP 62.交通枢纽]] >>

---

## Description

力扣城计划在两地设立「力扣嘉年华」的分会场，气象小组正在分析两地区的气温变化趋势，对于第 `i ~ (i+1)` 天的气温变化趋势，将根据以下规则判断：
- 若第 `i+1` 天的气温 **高于** 第 `i` 天，为 **上升** 趋势
- 若第 `i+1` 天的气温 **等于** 第 `i` 天，为 **平稳** 趋势
- 若第 `i+1` 天的气温 **低于** 第 `i` 天，为 **下降** 趋势

已知 `temperatureA[i]` 和 `temperatureB[i]` 分别表示第 `i` 天两地区的气温。
组委会希望找到一段天数尽可能多，且两地气温变化趋势相同的时间举办嘉年华活动。请分析并返回两地气温变化趋势**相同的最大连续天数**。
> 即最大的 `n`，使得第 `i~i+n` 天之间，两地气温变化趋势相同

**示例 1：**
>输入：
>`temperatureA = [21,18,18,18,31]`
>`temperatureB = [34,32,16,16,17]`
>
>输出：`2`
>
>解释：如下表所示， 第 `2～4` 天两地气温变化趋势相同，且持续时间最长，因此返回 `4-2=2`
![image.png](https://pic.leetcode-cn.com/1663902654-hlrSvs-image.png){:width=1000px}


**示例 2：**
>输入：
>`temperatureA = [5,10,16,-6,15,11,3]`
>`temperatureB = [16,22,23,23,25,3,-16]`
>
>输出：`3`

**提示：**
- `2 <= temperatureA.length == temperatureB.length <= 1000`
- `-20 <= temperatureA[i], temperatureB[i] <= 40`



---

[提交记录](https://leetcode.cn/problems/6CE719/submissions/) | [题解](https://leetcode.cn/problems/6CE719/solution/)


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