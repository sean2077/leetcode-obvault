---
tags:
  - leetcode/problem
questionId: "LCP 57"
title: 打地鼠
translatedTitle: 打地鼠
titleSlug: ZbAuEH
aliases:
  - 打地鼠
  - ZbAuEH
  - 打地鼠
lcLinks:
  - https://leetcode.com/problems/ZbAuEH/
  - https://leetcode.cn/problems/ZbAuEH/
lcTopics:
lcDifficulty: Hard
lcAcRate: 29.0%
similarQuestions:
grade: ⭐⭐⭐⭐⭐
likes: 14
dislikes: 0
favorites: []
created: 2025-11-16 11:17
updated: 2025-11-16 11:17
---

**Nav:** << previous: [[LCP 56.6UEx57|LCP 56.信物传送]] | next: [[LCP 58.De4qBB|LCP 58.积木拼接]] >>

---

## Description

欢迎各位勇者来到力扣城，本次试炼主题为「打地鼠」。
![middle_img_v2_d5d09656-0616-4a80-845e-ece461c5ba9g.png](https://pic.leetcode-cn.com/1650273183-nZIijm-middle_img_v2_d5d09656-0616-4a80-845e-ece461c5ba9g.png){:height="200px"}
勇者面前有一个大小为 `3*3` 的打地鼠游戏机，地鼠将随机出现在各个位置，`moles[i] = [t,x,y]` 表示在第 `t` 秒会有地鼠出现在 `(x,y)` 位置上，并于第 `t+1` 秒该地鼠消失。

勇者有一把可敲打地鼠的锤子，初始时刻（即第 `0` 秒）锤子位于正中间的格子 `(1,1)`，锤子的使用规则如下：
- 锤子每经过 `1` 秒可以往上、下、左、右中的一个方向移动一格，也可以不移动
- 锤子只可敲击所在格子的地鼠，**敲击不耗时**

请返回勇者**最多**能够敲击多少只地鼠。

**注意：** 
- 输入用例保证在相同时间相同位置最多仅有一只地鼠


**示例 1：**
>输入： `moles = [[1,1,0],[2,0,1],[4,2,2]]`
>
>输出： `2`
>
>解释：
>第 0 秒，锤子位于 (1,1)
>第 1 秒，锤子移动至 (1,0) 并敲击地鼠
>第 2 秒，锤子移动至 (2,0)
>第 3 秒，锤子移动至 (2,1)
>第 4 秒，锤子移动至 (2,2) 并敲击地鼠
>因此勇者最多可敲击 2 只地鼠


**示例 2：**
>输入：`moles = [[2,0,2],[5,2,0],[4,1,0],[1,2,1],[3,0,2]]`
>
>输出：`3`
>
>解释：
>第 0 秒，锤子位于 (1,1)
>第 1 秒，锤子移动至 (2,1) 并敲击地鼠
>第 2 秒，锤子移动至 (1,1)
>第 3 秒，锤子移动至 (1,0)
>第 4 秒，锤子在 (1,0) 不移动并敲击地鼠
>第 5 秒，锤子移动至 (2,0) 并敲击地鼠
>因此勇者最多可敲击 3 只地鼠


**示例 3：**
>输入：`moles = [[0,1,0],[0,0,1]]`
>
>输出：`0`
>
>解释：
>第 0 秒，锤子初始位于 (1,1)，此时并不能敲击 (1,0)、(0,1) 位置处的地鼠


**提示：**
+ `1 <= moles.length <= 10^5`
+ `moles[i].length == 3`
+ `0 <= moles[i][0] <= 10^9`
+ `0 <= moles[i][1], moles[i][2] < 3`



---

[提交记录](https://leetcode.cn/problems/ZbAuEH/submissions/) | [题解](https://leetcode.cn/problems/ZbAuEH/solution/)


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