---
tags:
  - leetcode/problem
questionId: "LCP 76"
title: 魔法棋盘
translatedTitle: 魔法棋盘
titleSlug: 1ybDKD
aliases:
  - 魔法棋盘
  - 1ybDKD
  - 魔法棋盘
lcLinks:
  - https://leetcode.com/problems/1ybDKD/
  - https://leetcode.cn/problems/1ybDKD/
lcTopics:
lcDifficulty: Hard
lcAcRate: 39.5%
similarQuestions:
grade: ⭐⭐⭐⭐⭐
likes: 7
dislikes: 0
favorites: []
created: 2025-11-16 11:17
updated: 2025-11-16 11:17
---

**Nav:** << previous: [[LCP 75.rdmXM7|LCP 75.传送卷轴]] | next: [[LCP 77.W2ZX4X|LCP 77.符文储备]] >>

---

## Description

在大小为 `n * m` 的棋盘中，有两种不同的棋子：黑色，红色。当两颗颜色不同的棋子同时满足以下两种情况时，将会产生魔法共鸣：
- 两颗异色棋子在同一行或者同一列
- 两颗异色棋子之间恰好只有一颗棋子
    > 注：异色棋子之间可以有空位

由于棋盘上被施加了魔法禁制，棋盘上的部分格子变成问号。`chessboard[i][j]` 表示棋盘第 `i` 行 `j` 列的状态：
- 若为 `.` ，表示当前格子确定为空
- 若为 `B` ，表示当前格子确定为 黑棋
- 若为 `R` ，表示当前格子确定为 红棋
- 若为 `?` ，表示当前格子待定

现在，探险家小扣的任务是确定所有问号位置的状态（留空/放黑棋/放红棋），使最终的棋盘上，任意两颗棋子间都 **无法** 产生共鸣。请返回可以满足上述条件的放置方案数量。

**示例1：**
> 输入：`n = 3, m = 3, chessboard = ["..R","..B","?R?"]`
>
> 输出：`5`
>
> 解释：给定的棋盘如图：
>![image.png](https://pic.leetcode.cn/1681714583-unbRox-image.png){:height=150px}
> 所有符合题意的最终局面如图：
>![image.png](https://pic.leetcode.cn/1681714596-beaOHK-image.png){:height=150px}

**示例2：**
> 输入：`n = 3, m = 3, chessboard = ["?R?","B?B","?R?"]`
>
> 输出：`105`

**提示：**
- `n == chessboard.length`
- `m == chessboard[i].length`
- `1 <= n*m <= 30`
- `chessboard` 中仅包含 `"."、"B"、"R"、"?"`


---

[提交记录](https://leetcode.cn/problems/1ybDKD/submissions/) | [题解](https://leetcode.cn/problems/1ybDKD/solution/)


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