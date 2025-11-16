---
tags:
  - leetcode/problem
questionId: "LCP 45"
title: 自行车炫技赛场
translatedTitle: 自行车炫技赛场
titleSlug: kplEvH
aliases:
  - 自行车炫技赛场
  - kplEvH
  - 自行车炫技赛场
lcLinks:
  - https://leetcode.com/problems/kplEvH/
  - https://leetcode.cn/problems/kplEvH/
lcTopics:
lcDifficulty: Medium
lcAcRate: 32.3%
similarQuestions:
grade: ⭐⭐⭐⭐⭐
likes: 15
dislikes: 0
favorites: []
created: 2025-11-16 12:09
updated: 2025-11-16 12:09
---

**Nav:** << previous: [[LCP 44.sZ59z6|LCP 44.开幕式焰火]] | next: [[LCP 46.05ZEDJ|LCP 46.志愿者调配]] >>

---

## Description

「力扣挑战赛」中 `N*M` 大小的自行车炫技赛场的场地由一片连绵起伏的上下坡组成，场地的高度值记录于二维数组 `terrain` 中，场地的减速值记录于二维数组 `obstacle` 中。
- 若选手骑着自行车从高度为 `h1` 且减速值为 `o1` 的位置到高度为 `h2` 且减速值为 `o2` 的相邻位置（上下左右四个方向），速度变化值为 `h1-h2-o2`（负值减速，正值增速）。

选手初始位于坐标 `position` 处且初始速度为 1，请问选手可以刚好到其他哪些位置时速度依旧为 1。请以二维数组形式返回这些位置。若有多个位置则按行坐标升序排列，若有多个位置行坐标相同则按列坐标升序排列。

**注意：** 骑行过程中速度不能为零或负值

**示例 1：**
> 输入：`position = [0,0], terrain = [[0,0],[0,0]], obstacle = [[0,0],[0,0]]`
> 
> 输出：`[[0,1],[1,0],[1,1]]`
> 
> 解释：
> 由于当前场地属于平地，根据上面的规则，选手从`[0,0]`的位置出发都能刚好在其他处的位置速度为 1。

**示例 2：**
> 输入：`position = [1,1], terrain = [[5,0],[0,6]], obstacle = [[0,6],[7,0]]`
> 
> 输出：`[[0,1]]`
> 
> 解释：
> 选手从 `[1,1]` 处的位置出发，到 `[0,1]` 处的位置时恰好速度为 1。


**提示：**
- `n == terrain.length == obstacle.length`
- `m == terrain[i].length == obstacle[i].length`
- `1 <= n <= 100`
- `1 <= m <= 100`
- `0 <= terrain[i][j], obstacle[i][j] <= 100`
- `position.length == 2`
- `0 <= position[0] < n`
- `0 <= position[1] < m`


---

[提交记录](https://leetcode.cn/problems/kplEvH/submissions/) | [题解](https://leetcode.cn/problems/kplEvH/solution/)


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