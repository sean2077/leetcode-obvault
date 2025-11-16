---
tags:
  - leetcode/problem
questionId: "LCP 51"
title: 烹饪料理
translatedTitle: 烹饪料理
titleSlug: UEcfPD
aliases:
  - 烹饪料理
  - UEcfPD
  - 烹饪料理
lcLinks:
  - https://leetcode.com/problems/UEcfPD/
  - https://leetcode.cn/problems/UEcfPD/
lcTopics:
lcDifficulty: Easy
lcAcRate: 53.8%
similarQuestions:
grade: ⭐⭐⭐⭐⭐
likes: 45
dislikes: 0
favorites: []
created: 2025-11-16 12:09
updated: 2025-11-16 12:09
---

**Nav:** << previous: [[LCP 50.WHnhjV|LCP 50.宝石补给]] | next: [[LCP 52.QO5KpG|LCP 52.二叉搜索树染色]] >>

---

## Description

欢迎各位勇者来到力扣城，城内设有烹饪锅供勇者制作料理，为自己恢复状态。

勇者背包内共有编号为 `0 ~ 4` 的五种食材，其中 `materials[j]` 表示第 `j` 种食材的数量。通过这些食材可以制作若干料理，`cookbooks[i][j]` 表示制作第 `i` 种料理需要第 `j` 种食材的数量，而 `attribute[i] = [x,y]` 表示第 `i` 道料理的美味度 `x` 和饱腹感 `y`。

在饱腹感不小于 `limit` 的情况下，请返回勇者可获得的最大美味度。如果无法满足饱腹感要求，则返回 `-1`。

**注意：**
- 每种料理只能制作一次。


**示例 1：**
>输入：`materials = [3,2,4,1,2]`
>`cookbooks = [[1,1,0,1,2],[2,1,4,0,0],[3,2,4,1,0]]`
>`attribute = [[3,2],[2,4],[7,6]]`
>`limit = 5`
>
>输出：`7`
>
>解释：
>食材数量可以满足以下两种方案：
>方案一：制作料理 0 和料理 1，可获得饱腹感 2+4、美味度 3+2
>方案二：仅制作料理 2， 可饱腹感为 6、美味度为 7
>因此在满足饱腹感的要求下，可获得最高美味度 7

**示例 2：**
>输入：`materials = [10,10,10,10,10]`
>`cookbooks = [[1,1,1,1,1],[3,3,3,3,3],[10,10,10,10,10]]`
>`attribute = [[5,5],[6,6],[10,10]]`
>`limit = 1`
>
>输出：`11`
>
>解释：通过制作料理 0 和 1，可满足饱腹感，并获得最高美味度 11

**提示：**
+ `materials.length == 5`
+ `1 <= cookbooks.length == attribute.length <= 8`
+ `cookbooks[i].length == 5`
+ `attribute[i].length == 2`
+ `0 <= materials[i], cookbooks[i][j], attribute[i][j] <= 20`
+ `1 <= limit <= 100`



---

[提交记录](https://leetcode.cn/problems/UEcfPD/submissions/) | [题解](https://leetcode.cn/problems/UEcfPD/solution/)


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