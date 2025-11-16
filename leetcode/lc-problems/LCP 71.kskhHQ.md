---
tags:
  - leetcode/problem
questionId: "LCP 71"
title: 集水器
translatedTitle: 集水器
titleSlug: kskhHQ
aliases:
  - 集水器
  - kskhHQ
  - 集水器
lcLinks:
  - https://leetcode.com/problems/kskhHQ/
  - https://leetcode.cn/problems/kskhHQ/
lcTopics:
lcDifficulty: Hard
lcAcRate: 55.7%
similarQuestions:
grade: ⭐⭐⭐⭐⭐
likes: 9
dislikes: 0
favorites: []
created: 2025-11-16 11:17
updated: 2025-11-16 11:17
---

**Nav:** << previous: [[LCP 70.XxZZjK|LCP 70.沙地治理]] | next: [[LCP 72.hqCnmP|LCP 72.补给马车]] >>

---

## Description

字符串数组 `shape` 描述了一个二维平面中的矩阵形式的集水器，`shape[i][j]` 表示集水器的第 `i` 行 `j` 列为：
- `'l'`表示向左倾斜的隔板（即从左上到右下）；
- `'r'`表示向右倾斜的隔板（即从左下到右上）；
- `'.'` 表示此位置没有隔板
![image.png](https://pic.leetcode-cn.com/1664424667-wMnPja-image.png){:width=200px}

已知当隔板构成存储容器可以存水，每个方格代表的蓄水量为 `2`。集水器初始浸泡在水中，除内部密闭空间外，所有位置均被水填满。
现将其从水中竖直向上取出，请返回集水器最终的蓄水量。

**注意：**
- 隔板具有良好的透气性，因此空气可以穿过隔板，但水无法穿过

**示例 1：**
> 输入：
> `shape = ["....rl","l.lr.r",".l..r.","..lr.."]`
>
> 输出：`18`
>
> 解释：如下图所示，由于空气会穿过隔板，因此红框区域没有水
![image.png](https://pic.leetcode-cn.com/1664436239-eyYxeP-image.png){:width="280px"}


**示例 2：**
> 输入：
> `shape = [".rlrlrlrl","ll..rl..r",".llrrllrr","..lr..lr."]`
> 输出：`18`
>
> 解释：如图所示。由于红框右侧未闭合，因此多余的水会从该处流走。
![image.png](https://pic.leetcode-cn.com/1664436082-SibVMv-image.png){:width="400px"}


**示例 3：**
> 输入：
> `shape = ["rlrr","llrl","llr."]`
> 输出：`6`
>
> 解释：如图所示。
![image.png](https://pic.leetcode-cn.com/1664424855-dwpUHO-image.png){:width="230px"}




**示例 4：**
> 输入：
> `shape = ["...rl...","..r..l..",".r.rl.l.","r.r..l.l","l.l..rl.",".l.lr.r.","..l..r..","...lr..."]`
>
> 输出：`30`
>
> 解释：如下图所示。由于中间为内部密闭空间，无法蓄水。
![image.png](https://pic.leetcode-cn.com/1664424894-mClEXh-image.png){:width="350px"}


**提示**：
- `1 <= shape.length <= 50`
- `1 <= shape[i].length <= 50`
- `shape[i][j]` 仅为 `'l'`、`'r'` 或 `'.'`



---

[提交记录](https://leetcode.cn/problems/kskhHQ/submissions/) | [题解](https://leetcode.cn/problems/kskhHQ/solution/)


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