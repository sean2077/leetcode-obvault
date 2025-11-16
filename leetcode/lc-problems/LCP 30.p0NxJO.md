---
tags:
  - leetcode/problem
questionId: "LCP 30"
title: 魔塔游戏
translatedTitle: 魔塔游戏
titleSlug: p0NxJO
aliases:
  - 魔塔游戏
  - p0NxJO
  - 魔塔游戏
lcLinks:
  - https://leetcode.com/problems/p0NxJO/
  - https://leetcode.cn/problems/p0NxJO/
lcTopics:
lcDifficulty: Medium
lcAcRate: 46.3%
similarQuestions:
grade: ⭐⭐⭐⭐⭐
likes: 128
dislikes: 0
favorites: []
created: 2025-11-16 12:09
updated: 2025-11-16 12:09
---

**Nav:** << previous: [[LCP 29.SNJvJP|LCP 29.乐团站位]] | next: [[LCP 31.Db3wC1|LCP 31.变换的迷宫]] >>

---

## Description

小扣当前位于魔塔游戏第一层，共有 `N` 个房间，编号为 `0 ~ N-1`。每个房间的补血道具/怪物对于血量影响记于数组 `nums`，其中正数表示道具补血数值，即血量增加对应数值；负数表示怪物造成伤害值，即血量减少对应数值；`0` 表示房间对血量无影响。

**小扣初始血量为 1，且无上限**。假定小扣原计划按房间编号升序访问所有房间补血/打怪，**为保证血量始终为正值**，小扣需对房间访问顺序进行调整，**每次仅能将一个怪物房间（负数的房间）调整至访问顺序末尾**。请返回小扣最少需要调整几次，才能顺利访问所有房间。若调整顺序也无法访问完全部房间，请返回 -1。


**示例 1：**
>输入：`nums = [100,100,100,-250,-60,-140,-50,-50,100,150]`
>
>输出：`1`
>
>解释：初始血量为 1。至少需要将 nums[3] 调整至访问顺序末尾以满足要求。

**示例 2：**
>输入：`nums = [-200,-300,400,0]`
>
>输出：`-1`
>
>解释：调整访问顺序也无法完成全部房间的访问。

**提示：**
- `1 <= nums.length <= 10^5`
- `-10^5 <= nums[i] <= 10^5`


---

[提交记录](https://leetcode.cn/problems/p0NxJO/submissions/) | [题解](https://leetcode.cn/problems/p0NxJO/solution/)


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