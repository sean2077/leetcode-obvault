---
tags:
  - leetcode/problem
questionId: "LCP 34"
title: 二叉树染色
translatedTitle: 二叉树染色
titleSlug: er-cha-shu-ran-se-UGC
aliases:
  - 二叉树染色
  - er-cha-shu-ran-se-UGC
  - 二叉树染色
lcLinks:
  - https://leetcode.com/problems/er-cha-shu-ran-se-UGC/
  - https://leetcode.cn/problems/er-cha-shu-ran-se-UGC/
lcTopics:
lcDifficulty: Medium
lcAcRate: 57.8%
similarQuestions:
grade: ⭐⭐⭐⭐⭐
likes: 115
dislikes: 0
favorites: []
created: 2025-11-16 11:17
updated: 2025-11-16 11:17
---

**Nav:** << previous: [[LCP 33.o8SXZn|LCP 33.蓄水]] | next: [[LCP 35.DFPeFJ|LCP 35.电动车游城市]] >>

---

## Description

小扣有一个根结点为 `root` 的二叉树模型，初始所有结点均为白色，可以用蓝色染料给模型结点染色，模型的每个结点有一个 `val` 价值。小扣出于美观考虑，希望最后二叉树上每个蓝色相连部分的结点个数不能超过 `k` 个，求所有染成蓝色的结点价值总和最大是多少？


**示例 1：**
> 输入：`root = [5,2,3,4], k = 2`
>
> 输出：`12`
>
> 解释：`结点 5、3、4 染成蓝色，获得最大的价值 5+3+4=12`
![image.png](https://pic.leetcode-cn.com/1616126267-BqaCRj-image.png)


**示例 2：**
> 输入：`root = [4,1,3,9,null,null,2], k = 2`
>
> 输出：`16`
>
> 解释：结点 4、3、9 染成蓝色，获得最大的价值 4+3+9=16
![image.png](https://pic.leetcode-cn.com/1616126301-gJbhba-image.png)



**提示：**
+ `1 <= k <= 10`
+ `1 <= val <= 10000`
+ `1 <= 结点数量 <= 10000`
    


---

[提交记录](https://leetcode.cn/problems/er-cha-shu-ran-se-UGC/submissions/) | [题解](https://leetcode.cn/problems/er-cha-shu-ran-se-UGC/solution/)


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