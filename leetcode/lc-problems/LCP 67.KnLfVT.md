---
tags:
  - leetcode/problem
questionId: "LCP 67"
title: 装饰树
translatedTitle: 装饰树
titleSlug: KnLfVT
aliases:
  - 装饰树
  - KnLfVT
  - 装饰树
lcLinks:
  - https://leetcode.com/problems/KnLfVT/
  - https://leetcode.cn/problems/KnLfVT/
lcTopics:
lcDifficulty: Medium
lcAcRate: 86.4%
similarQuestions:
grade: ⭐⭐⭐⭐⭐
likes: 14
dislikes: 0
favorites: []
created: 2025-11-16 12:09
updated: 2025-11-16 12:09
---

**Nav:** << previous: [[LCP 66.600YaG|LCP 66.最小展台数量]] | next: [[LCP 68.1GxJYY|LCP 68.美观的花束]] >>

---

## Description

力扣嘉年华上的 DIY 手工展位准备了一棵缩小版的 **二叉** 装饰树 `root` 和灯饰，你需要将灯饰逐一插入装饰树中，要求如下：

- 完成装饰的二叉树根结点与 `root` 的根结点值相同
- 若一个节点拥有父节点，则在该节点和他的父节点之间插入一个灯饰（即插入一个值为 `-1` 的节点）。具体地：
    - 在一个 父节点 x 与其左子节点 y 之间添加 -1 节点， 节点 -1、节点 y 为各自父节点的左子节点，
    - 在一个 父节点 x 与其右子节点 y 之间添加 -1 节点， 节点 -1、节点 y 为各自父节点的右子节点，
    
现给定二叉树的根节点 `root` ，请返回完成装饰后的树的根节点。
**示例 1：**
>输入：
>`root = [7,5,6]`
>
>输出：`[7,-1,-1,5,null,null,6]`
>
>解释：如下图所示，
>![image.png](https://pic.leetcode-cn.com/1663575757-yRLGaq-image.png){:width=400px}

**示例 2：**
>输入：
>`root = [3,1,7,3,8,null,4]`
>
>输出：`[3,-1,-1,1,null,null,7,-1,-1,null,-1,3,null,null,8,null,4]`
>
>解释：如下图所示
![image.png](https://pic.leetcode-cn.com/1663577920-sjrAYH-image.png){:width=500px}

**提示：**
>`0 <= root.Val <= 1000`
>`root` 节点数量范围为 `[1, 10^5]`


---

[提交记录](https://leetcode.cn/problems/KnLfVT/submissions/) | [题解](https://leetcode.cn/problems/KnLfVT/solution/)


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