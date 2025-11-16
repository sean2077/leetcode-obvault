---
tags:
  - leetcode/problem
questionId: "LCP 29"
title: 乐团站位
translatedTitle: 乐团站位
titleSlug: SNJvJP
aliases:
  - 乐团站位
  - SNJvJP
  - 乐团站位
lcLinks:
  - https://leetcode.com/problems/SNJvJP/
  - https://leetcode.cn/problems/SNJvJP/
lcTopics:
lcDifficulty: Medium
lcAcRate: 21.5%
similarQuestions:
grade: ⭐⭐⭐⭐⭐
likes: 77
dislikes: 0
favorites: []
created: 2025-11-16 11:17
updated: 2025-11-16 11:17
---

**Nav:** << previous: [[LCP 28.4xy4Wx|LCP 28.采购方案]] | next: [[LCP 30.p0NxJO|LCP 30.魔塔游戏]] >>

---

## Description

某乐团的演出场地可视作 `num * num` 的二维矩阵 `grid`（左上角坐标为 `[0,0]`)，每个位置站有一位成员。乐团共有 `9` 种乐器，乐器编号为 `1~9`，每位成员持有 `1` 个乐器。

为保证声乐混合效果，成员站位规则为：自 `grid` 左上角开始顺时针螺旋形向内循环以 `1，2，...，9` 循环重复排列。例如当 num = `5` 时，站位如图所示

![image.png](https://pic.leetcode-cn.com/1616125411-WOblWH-image.png)


请返回位于场地坐标 [`Xpos`,`Ypos`] 的成员所持乐器编号。

**示例 1：**
>输入：`num = 3, Xpos = 0, Ypos = 2`
>
>输出：`3`
>
>解释：
![image.png](https://pic.leetcode-cn.com/1616125437-WUOwsu-image.png)


**示例 2：**
>输入：`num = 4, Xpos = 1, Ypos = 2`
>
>输出：`5`
>
>解释：
![image.png](https://pic.leetcode-cn.com/1616125453-IIDpxg-image.png)


**提示：**
- `1 <= num <= 10^9`
- `0 <= Xpos, Ypos < num`


---

[提交记录](https://leetcode.cn/problems/SNJvJP/submissions/) | [题解](https://leetcode.cn/problems/SNJvJP/solution/)


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