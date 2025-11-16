---
tags:
  - leetcode/problem
questionId: "LCP 41"
title: 黑白翻转棋
translatedTitle: 黑白翻转棋
titleSlug: fHi6rV
aliases:
  - 黑白翻转棋
  - fHi6rV
  - 黑白翻转棋
lcLinks:
  - https://leetcode.com/problems/fHi6rV/
  - https://leetcode.cn/problems/fHi6rV/
lcTopics:
lcDifficulty: Medium
lcAcRate: 68.0%
similarQuestions:
grade: ⭐⭐⭐⭐⭐
likes: 82
dislikes: 0
favorites: []
created: 2025-11-16 11:17
updated: 2025-11-16 11:17
---

**Nav:** << previous: [[LCP 40.uOAnQW|LCP 40.心算挑战]] | next: [[LCP 42.vFjcfV|LCP 42.玩具套圈]] >>

---

## Description

在 `n*m` 大小的棋盘中，有黑白两种棋子，黑棋记作字母 `"X"`, 白棋记作字母 `"O"`，空余位置记作 `"."`。当落下的棋子与其他相同颜色的棋子在行、列或对角线完全包围（中间不存在空白位置）另一种颜色的棋子，则可以翻转这些棋子的颜色。



![1.gif](https://pic.leetcode-cn.com/1630396029-eTgzpN-6da662e67368466a96d203f67bb6e793.gif){:height=170px}![2.gif](https://pic.leetcode-cn.com/1630396240-nMvdcc-8e4261afe9f60e05a4f740694b439b6b.gif){:height=170px}![3.gif](https://pic.leetcode-cn.com/1630396291-kEtzLL-6fcb682daeecb5c3f56eb88b23c81d33.gif){:height=170px}

「力扣挑战赛」黑白翻转棋项目中，将提供给选手一个未形成可翻转棋子的棋盘残局，其状态记作 `chessboard`。若下一步可放置一枚黑棋，请问选手最多能翻转多少枚白棋。

**注意：**
- 若翻转白棋成黑棋后，棋盘上仍存在可以翻转的白棋，将可以 **继续** 翻转白棋
- 输入数据保证初始棋盘状态无可以翻转的棋子且存在空余位置

**示例 1：**
> 输入：`chessboard = ["....X.","....X.","XOOO..","......","......"]`
> 
> 输出：`3`
> 
> 解释：
> 可以选择下在 `[2,4]` 处，能够翻转白方三枚棋子。

**示例 2：**
> 输入：`chessboard = [".X.",".O.","XO."]`
> 
> 输出：`2`
> 
> 解释：
> 可以选择下在 `[2,2]` 处，能够翻转白方两枚棋子。
![2126c1d21b1b9a9924c639d449cc6e65.gif](https://pic.leetcode-cn.com/1626683255-OBtBud-2126c1d21b1b9a9924c639d449cc6e65.gif)

**示例 3：**
> 输入：`chessboard = [".......",".......",".......","X......",".O.....","..O....","....OOX"]`
> 
> 输出：`4`
> 
> 解释：
> 可以选择下在 `[6,3]` 处，能够翻转白方四枚棋子。
![803f2f04098b6174397d6c696f54d709.gif](https://pic.leetcode-cn.com/1630393770-Puyked-803f2f04098b6174397d6c696f54d709.gif)



**提示：**
- `1 <= chessboard.length, chessboard[i].length <= 8`
- `chessboard[i]` 仅包含 `"."、"O"` 和 `"X"`


---

[提交记录](https://leetcode.cn/problems/fHi6rV/submissions/) | [题解](https://leetcode.cn/problems/fHi6rV/solution/)


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