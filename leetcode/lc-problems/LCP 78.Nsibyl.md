---
tags:
  - leetcode/problem
questionId: "LCP 78"
title: 城墙防线
translatedTitle: 城墙防线
titleSlug: Nsibyl
aliases:
  - 城墙防线
  - Nsibyl
  - 城墙防线
lcLinks:
  - https://leetcode.com/problems/Nsibyl/
  - https://leetcode.cn/problems/Nsibyl/
lcTopics:
lcDifficulty: Medium
lcAcRate: 48.8%
similarQuestions:
grade: ⭐⭐⭐⭐⭐
likes: 10
dislikes: 0
favorites: []
created: 2025-11-16 11:17
updated: 2025-11-16 11:17
---

**Nav:** << previous: [[LCP 77.W2ZX4X|LCP 77.符文储备]] | next: [[LCP 79.kjpLFZ|LCP 79.提取咒文]] >>

---

## Description

在探险营地间，小扣意外发现了一片城墙遗迹，在探索期间，却不巧遇到迁徙中的兽群向他迎面冲来。情急之下小扣吹响了他的苍蓝笛，随着笛声响起，遗迹中的城墙逐渐发生了横向膨胀。
已知 `rampart[i] = [x,y]` 表示第 `i` 段城墙的初始所在区间。当城墙发生膨胀时，将遵循以下规则：
- 所有的城墙会同时膨胀相等的长度；
- 每个城墙可以向左、向右或向两个方向膨胀。

小扣为了确保自身的安全，需要在所有城墙均无重叠的情况下，让城墙尽可能的膨胀。请返回城墙可以膨胀的 **最大值** 。

**注意：**
- 初始情况下，所有城墙均不重叠，且 `rampart` 中的元素升序排列；
- 两侧的城墙可以向外无限膨胀。

**示例 1：**
>输入：`rampart = [[0,3],[4,5],[7,9]]`
>
>输出：`3`
>
>解释：如下图所示：
>`rampart[0]` 向左侧膨胀 3 个单位；
>`rampart[2]` 向右侧膨胀 3 个单位；
>`rampart[1]` 向左侧膨胀 1 个单位，向右膨胀 2 个单位。
>不存在膨胀更多的方案，返回 3。
![image.png](https://pic.leetcode.cn/1681717918-tWywrp-image.png){:width=750px}

**示例 2：**
>输入：`rampart = [[1,2],[5,8],[11,15],[18,25]]`
>
>输出：`4`

**提示：**
- `3 <= rampart.length <= 10^4`
- `rampart[i].length == 2`
- `0 <= rampart[i][0] < rampart[i][1] <= rampart[i+1][0] <= 10^8`


---

[提交记录](https://leetcode.cn/problems/Nsibyl/submissions/) | [题解](https://leetcode.cn/problems/Nsibyl/solution/)


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