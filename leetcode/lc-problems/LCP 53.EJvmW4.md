---
tags:
  - leetcode/problem
questionId: "LCP 53"
title: 守护太空城
translatedTitle: 守护太空城
titleSlug: EJvmW4
aliases:
  - 守护太空城
  - EJvmW4
  - 守护太空城
lcLinks:
  - https://leetcode.com/problems/EJvmW4/
  - https://leetcode.cn/problems/EJvmW4/
lcTopics:
lcDifficulty: Hard
lcAcRate: 48.0%
similarQuestions:
grade: ⭐⭐⭐⭐⭐
likes: 13
dislikes: 0
favorites: []
created: 2025-11-16 11:17
updated: 2025-11-16 11:17
---

**Nav:** << previous: [[LCP 52.QO5KpG|LCP 52.二叉搜索树染色]] | next: [[LCP 54.s5kipK|LCP 54.夺回据点]] >>

---

## Description

各位勇者请注意，力扣太空城发布陨石雨红色预警。

太空城中的一些舱室将要受到陨石雨的冲击，这些舱室按照编号 `0 ~ N` 的顺序依次排列。为了阻挡陨石损毁舱室，太空城可以使用能量展开防护屏障，具体消耗如下：

- 选择一个舱室开启屏障，能量消耗为 `2` 
- 选择相邻两个舱室开启联合屏障，能量消耗为 `3`
- 对于已开启的**一个**屏障，**多维持一时刻**，能量消耗为 `1`

已知陨石雨的影响范围和到达时刻，`time[i]` 和 `position[i]` 分别表示该陨石的到达时刻和冲击位置。请返回太空舱能够守护所有舱室所需要的最少能量。

**注意：** 
- 同一时间，一个舱室不能被多个屏障覆盖
- 陨石雨仅在到达时刻对冲击位置处的舱室有影响


**示例 1：**
>输入：`time = [1,2,1], position = [6,3,3]`
>
>输出：`5`
>
>解释：
> 时刻 1，分别开启编号 3、6 舱室的屏障，能量消耗 2*2 = 4
> 时刻 2，维持编号 3 舱室的屏障，能量消耗 1
> 因此，最少需要能量 5

**示例 2：**
>输入：`time = [1,1,1,2,2,3,5], position = [1,2,3,1,2,1,3]`
>
>输出：`9`
>
>解释：
> 时刻 1，开启编号 1、2 舱室的联合屏障，能量消耗 3
> 时刻 1，开启编号 3 舱室的屏障，能量消耗 2
> 时刻 2，维持编号 1、2 舱室的联合屏障，能量消耗 1
> 时刻 3，维持编号 1、2 舱室的联合屏障，能量消耗 1
> 时刻 5，重新开启编号 3 舱室的联合屏障，能量消耗 2
> 因此，最少需要能量 9

**提示：**
+ `1 <= time.length == position.length <= 500`
+ `1 <= time[i] <= 5`
+ `0 <= position[i] <= 100`



---

[提交记录](https://leetcode.cn/problems/EJvmW4/submissions/) | [题解](https://leetcode.cn/problems/EJvmW4/solution/)


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