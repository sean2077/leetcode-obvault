---
tags:
  - leetcode/problem
questionId: "LCP 54"
title: 夺回据点
translatedTitle: 夺回据点
titleSlug: s5kipK
aliases:
  - 夺回据点
  - s5kipK
  - 夺回据点
lcLinks:
  - https://leetcode.com/problems/s5kipK/
  - https://leetcode.cn/problems/s5kipK/
lcTopics:
lcDifficulty: Hard
lcAcRate: 44.1%
similarQuestions:
grade: ⭐⭐⭐⭐⭐
likes: 14
dislikes: 0
favorites: []
created: 2025-11-16 11:17
updated: 2025-11-16 11:17
---

**Nav:** << previous: [[LCP 53.EJvmW4|LCP 53.守护太空城]] | next: [[LCP 55.PTXy4P|LCP 55.采集果实]] >>

---

## Description

欢迎各位勇者来到力扣城，本次试炼主题为「夺回据点」。

魔物了占领若干据点，这些据点被若干条道路相连接，`roads[i] = [x, y]` 表示编号 `x`、`y` 的两个据点通过一条道路连接。

现在勇者要将按照以下原则将这些据点逐一夺回：

- 在开始的时候，勇者可以花费资源先夺回一些据点，初始夺回第 `j` 个据点所需消耗的资源数量为 `cost[j]` 

- 接下来，勇者在不消耗资源情况下，每次可以夺回**一个**和「已夺回据点」相连接的魔物据点，并对其进行夺回

> 注：为了防止魔物暴动，勇者在每一次夺回据点后（包括花费资源夺回据点后），需要保证剩余的所有魔物据点之间是相连通的（不经过「已夺回据点」）。

请返回勇者夺回所有据点需要消耗的最少资源数量。

**注意：**
- 输入保证初始所有据点都是连通的，且不存在重边和自环

**示例 1：**
>输入：
>`cost = [1,2,3,4,5,6]`
>`roads = [[0,1],[0,2],[1,3],[2,3],[1,2],[2,4],[2,5]]`
>
>输出：`6`
>
>解释：
>勇者消耗资源 `6` 夺回据点 `0` 和 `4`，魔物据点 `1、2、3、5` 相连通；
>第一次夺回据点 `1`，魔物据点 `2、3、5` 相连通；
>第二次夺回据点 `3`，魔物据点 `2、5` 相连通；
>第三次夺回据点 `2`，剩余魔物据点 `5`；
>第四次夺回据点 `5`，无剩余魔物据点；
>因此最少需要消耗资源为 `6`，可占领所有据点。
![image.png](https://pic.leetcode-cn.com/1648706944-KJstUN-image.png){:height=170px}


**示例 2：**
>输入：
>`cost = [3,2,1,4]`
>`roads = [[0,2],[2,3],[3,1]]`
>
>输出：`2`
>
>解释：
>勇者消耗资源 `2` 夺回据点 `1`，魔物据点 `0、2、3` 相连通；
>第一次夺回据点 `3`，魔物据点 `2、0` 相连通；
>第二次夺回据点 `2`，剩余魔物据点 `0`；
>第三次夺回据点 `0`，无剩余魔物据点；
>因此最少需要消耗资源为 `2`，可占领所有据点。
![image.png](https://pic.leetcode-cn.com/1648707186-LJRwzU-image.png){:height=60px}


**提示：**
- `1 <= roads.length, cost.length <= 10^5`
- `0 <= roads[i][0], roads[i][1] < cost.length`
- `1 <= cost[i] <= 10^9`



---

[提交记录](https://leetcode.cn/problems/s5kipK/submissions/) | [题解](https://leetcode.cn/problems/s5kipK/solution/)


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