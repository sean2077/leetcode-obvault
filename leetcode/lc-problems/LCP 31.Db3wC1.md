---
tags:
  - leetcode/problem
questionId: "LCP 31"
title: 变换的迷宫
translatedTitle: 变换的迷宫
titleSlug: Db3wC1
aliases:
  - 变换的迷宫
  - Db3wC1
  - 变换的迷宫
lcLinks:
  - https://leetcode.com/problems/Db3wC1/
  - https://leetcode.cn/problems/Db3wC1/
lcTopics:
lcDifficulty: Hard
lcAcRate: 31.3%
similarQuestions:
grade: ⭐⭐⭐⭐⭐
likes: 39
dislikes: 0
favorites: []
created: 2025-11-16 11:17
updated: 2025-11-16 11:17
---

**Nav:** << previous: [[LCP 30.p0NxJO|LCP 30.魔塔游戏]] | next: [[LCP 32.t3fKg1|LCP 32.批量处理任务]] >>

---

## Description

某解密游戏中，有一个 N\*M 的迷宫，迷宫地形会随时间变化而改变，迷宫出口一直位于 `(n-1,m-1)` 位置。迷宫变化规律记录于 `maze` 中，`maze[i]` 表示 `i` 时刻迷宫的地形状态，`"."` 表示可通行空地，`"#"` 表示陷阱。

地形图初始状态记作 `maze[0]`，此时小力位于起点 `(0,0)`。此后每一时刻可选择往上、下、左、右其一方向走一步，或者停留在原地。

小力背包有以下两个魔法卷轴（卷轴使用一次后消失）：
+ 临时消除术：将指定位置在下一个时刻变为空地；
+ 永久消除术：将指定位置永久变为空地。

请判断在迷宫变化结束前（含最后时刻），小力能否在不经过任意陷阱的情况下到达迷宫出口呢？

**注意： 输入数据保证起点和终点在所有时刻均为空地。**

**示例 1：**
>输入：`maze = [[".#.","#.."],["...",".#."],[".##",".#."],["..#",".#."]]`
>
>输出：`true`
>
>解释：
![maze.gif](https://pic.leetcode-cn.com/1615892239-SCIjyf-maze.gif)


**示例 2：**
>输入：`maze = [[".#.","..."],["...","..."]]`
>
>输出：`false`
>
>解释：由于时间不够，小力无法到达终点逃出迷宫。

**示例 3：**
>输入：`maze = [["...","...","..."],[".##","###","##."],[".##","###","##."],[".##","###","##."],[".##","###","##."],[".##","###","##."],[".##","###","##."]]`
>
>输出：`false`
>
>解释：由于道路不通，小力无法到达终点逃出迷宫。

**提示：**
- `1 <= maze.length <= 100`
- `1 <= maze[i].length, maze[i][j].length <= 50`
- `maze[i][j]` 仅包含 `"."`、`"#"`


---

[提交记录](https://leetcode.cn/problems/Db3wC1/submissions/) | [题解](https://leetcode.cn/problems/Db3wC1/solution/)


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