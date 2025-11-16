---
tags:
  - leetcode/problem
questionId: "LCP 64"
title: 二叉树灯饰
translatedTitle: 二叉树灯饰
titleSlug: U7WvvU
aliases:
  - 二叉树灯饰
  - U7WvvU
  - 二叉树灯饰
lcLinks:
  - https://leetcode.com/problems/U7WvvU/
  - https://leetcode.cn/problems/U7WvvU/
lcTopics:
lcDifficulty: Medium
lcAcRate: 38.5%
similarQuestions:
grade: ⭐⭐⭐⭐⭐
likes: 27
dislikes: 0
favorites: []
created: 2025-11-16 12:09
updated: 2025-11-16 12:09
---

**Nav:** << previous: [[LCP 63.EXvqDp|LCP 63.弹珠游戏]] | next: [[LCP 65.3aqs1c|LCP 65.舒适的湿度]] >>

---

## Description

「力扣嘉年华」的中心广场放置了一个巨型的二叉树形状的装饰树。每个节点上均有一盏灯和三个开关。节点值为 `0` 表示灯处于「关闭」状态，节点值为 `1` 表示灯处于「开启」状态。每个节点上的三个开关各自功能如下：
- 开关 `1`：切换当前节点的灯的状态；
- 开关 `2`：切换 **以当前节点为根** 的子树中，所有节点上的灯的状态，；
- 开关 `3`：切换 **当前节点及其左右子节点**（若存在的话） 上的灯的状态；

给定该装饰的初始状态 `root`，请返回最少需要操作多少次开关，可以关闭所有节点的灯。

**示例 1：**
>输入：`root = [1,1,0,null,null,null,1]`
>
>输出：`2`
>
>解释：以下是最佳的方案之一，如图所示
![b71b95bf405e3b223e00b2820a062ba4.gif](https://pic.leetcode-cn.com/1629357030-GSbzpY-b71b95bf405e3b223e00b2820a062ba4.gif){:width="300px"}

**示例 2：**
>输入：`root = [1,1,1,1,null,null,1]`
>
>输出：`1`
>
>解释：以下是最佳的方案，如图所示
![a4091b6448a0089b4d9e8f0390ff9ac6.gif](https://pic.leetcode-cn.com/1629356950-HZsKZC-a4091b6448a0089b4d9e8f0390ff9ac6.gif){:width="300px"}

**示例 3：**
>输入：`root = [0,null,0]`
>
>输出：`0`
>
>解释：无需操作开关，当前所有节点上的灯均已关闭

**提示：**
- `1 <= 节点个数 <= 10^5`
- `0 <= Node.val <= 1`


---

[提交记录](https://leetcode.cn/problems/U7WvvU/submissions/) | [题解](https://leetcode.cn/problems/U7WvvU/solution/)


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