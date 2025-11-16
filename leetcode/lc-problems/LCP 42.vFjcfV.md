---
tags:
  - leetcode/problem
questionId: "LCP 42"
title: 玩具套圈
translatedTitle: 玩具套圈
titleSlug: vFjcfV
aliases:
  - 玩具套圈
  - vFjcfV
  - 玩具套圈
lcLinks:
  - https://leetcode.com/problems/vFjcfV/
  - https://leetcode.cn/problems/vFjcfV/
lcTopics:
lcDifficulty: Hard
lcAcRate: 29.7%
similarQuestions:
grade: ⭐⭐⭐⭐⭐
likes: 17
dislikes: 0
favorites: []
created: 2025-11-16 12:09
updated: 2025-11-16 12:09
---

**Nav:** << previous: [[LCP 41.fHi6rV|LCP 41.黑白翻转棋]] | next: [[LCP 43.Y1VbOX|LCP 43.十字路口的交通]] >>

---

## Description

「力扣挑战赛」场地外，小力组织了一个套玩具的游戏。所有的玩具摆在平地上，`toys[i]` 以 `[xi,yi,ri]` 的形式记录了第 `i` 个玩具的坐标 `(xi,yi)` 和半径 `ri`。小扣试玩了一下，他扔了若干个半径均为 `r` 的圈，`circles[j]` 记录了第 `j` 个圈的坐标 `(xj,yj)`。套圈的规则如下：
- 若一个玩具被某个圈完整覆盖了（即玩具的任意部分均在圈内或者圈上），则该玩具被套中。
- 若一个玩具被多个圈同时套中，最终仅计算为套中一个玩具

请帮助小扣计算，他成功套中了多少玩具。

**注意：**
- 输入数据保证任意两个玩具的圆心不会重合，但玩具之间可能存在重叠。


**示例 1：**

> 输入：`toys = [[3,3,1],[3,2,1]], circles = [[4,3]], r = 2`
>
> 输出：`1`
> 
> 解释： 如图所示，仅套中一个玩具
![image.png](https://pic.leetcode-cn.com/1629194140-ydKiGF-image.png)


**示例 2：**

> 输入：`toys = [[1,3,2],[4,3,1],[7,1,2]], circles = [[1,0],[3,3]], r = 4`
>
> 输出：`2`
> 
> 解释： 如图所示，套中两个玩具
![image.png](https://pic.leetcode-cn.com/1629194157-RiOAuy-image.png){:width="400px"}



**提示：** 
- `1 <= toys.length <= 10^4`
- `0 <= toys[i][0], toys[i][1] <= 10^9`
- `1 <= circles.length <= 10^4`
- `0 <= circles[i][0], circles[i][1] <= 10^9`
- `1 <= toys[i][2], r <= 10`



---

[提交记录](https://leetcode.cn/problems/vFjcfV/submissions/) | [题解](https://leetcode.cn/problems/vFjcfV/solution/)


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