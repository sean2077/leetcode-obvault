---
tags:
  - leetcode/problem
questionId: "LCP 48"
title: 无限棋局
translatedTitle: 无限棋局
titleSlug: fsa7oZ
aliases:
  - 无限棋局
  - fsa7oZ
  - 无限棋局
lcLinks:
  - https://leetcode.com/problems/fsa7oZ/
  - https://leetcode.cn/problems/fsa7oZ/
lcTopics:
lcDifficulty: Hard
lcAcRate: 28.7%
similarQuestions:
grade: ⭐⭐⭐⭐⭐
likes: 12
dislikes: 0
favorites: []
created: 2025-11-16 12:09
updated: 2025-11-16 12:09
---

**Nav:** << previous: [[LCP 47.oPs9Bm|LCP 47.入场安检]] | next: [[LCP 49.K8GULz|LCP 49.环形闯关游戏]] >>

---

## Description

小力正在通过残局练习来备战「力扣挑战赛」中的「五子棋」项目，他想请你能帮他预测当前残局的输赢情况。棋盘中的棋子分布信息记录于二维数组 `pieces` 中，其中 `pieces[i] = [x,y,color]` 表示第 `i` 枚棋子的横坐标为 `x`，纵坐标为 `y`，棋子颜色为 `color`(`0` 表示黑棋，`1` 表示白棋)。假如黑棋先行，并且黑棋和白棋都按最优策略落子，请你求出当前棋局在三步（按 **黑、白、黑** 的落子顺序）之内的输赢情况（三步之内先构成同行、列或对角线连续同颜色的至少 5 颗即为获胜）：
- 黑棋胜, 请返回 `"Black"`
- 白棋胜, 请返回 `"White"`
- 仍无胜者, 请返回 `"None"`

**注意：** 
- 和传统的五子棋项目不同，「力扣挑战赛」中的「五子棋」项目 **不存在边界限制**，即可在 **任意位置** 落子；
- 黑棋和白棋均按 3 步内的输赢情况进行最优策略的选择
- 测试数据保证所给棋局目前无胜者；
- 测试数据保证不会存在坐标一样的棋子。

**示例 1：**
> 输入：
> `pieces = [[0,0,1],[1,1,1],[2,2,0]]`
>
> 输出：`"None"`
>
> 解释：无论黑、白棋以何种方式落子，三步以内都不会产生胜者。

**示例 2：**
> 输入：
> `pieces = [[1,2,1],[1,4,1],[1,5,1],[2,1,0],[2,3,0],[2,4,0],[3,2,1],[3,4,0],[4,2,1],[5,2,1]]`
>
> 输出：`"Black"`
>
> 解释：三步之内黑棋必胜，以下是一种可能的落子情况：
>![902b87df29998b1c181146c8fdb3a4b6.gif](https://pic.leetcode-cn.com/1629800639-KabOfY-902b87df29998b1c181146c8fdb3a4b6.gif){:width="300px"}



**提示：**
- `0 <= pieces.length <= 1000`
- `pieces[i].length = 3`
- `-10^9 <= pieces[i][0], pieces[i][1] <=10^9` 
- `0 <= pieces[i][2] <=1`



---

[提交记录](https://leetcode.cn/problems/fsa7oZ/submissions/) | [题解](https://leetcode.cn/problems/fsa7oZ/solution/)


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