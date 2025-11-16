---
tags:
  - leetcode/problem
questionId: "LCP 72"
title: 补给马车
translatedTitle: 补给马车
titleSlug: hqCnmP
aliases:
  - 补给马车
  - hqCnmP
  - 补给马车
lcLinks:
  - https://leetcode.com/problems/hqCnmP/
  - https://leetcode.cn/problems/hqCnmP/
lcTopics:
lcDifficulty: Easy
lcAcRate: 68.0%
similarQuestions:
grade: ⭐⭐⭐⭐⭐
likes: 12
dislikes: 0
favorites: []
created: 2025-11-16 11:17
updated: 2025-11-16 11:17
---

**Nav:** << previous: [[LCP 71.kskhHQ|LCP 71.集水器]] | next: [[LCP 73.0Zeoeg|LCP 73.探险营地]] >>

---

## Description

远征队即将开启未知的冒险之旅，不过在此之前，将对补给车队进行最后的检查。`supplies[i]` 表示编号为 `i` 的补给马车装载的物资数量。
考虑到车队过长容易被野兽偷袭，他们决定将车队的长度变为原来的一半（向下取整），计划为：
- 找出车队中 **物资之和最小** 两辆 **相邻** 马车，将它们车辆的物资整合为一辆。若存在多组物资之和相同的马车，则取编号最小的两辆马车进行整合；
- 重复上述操作直到车队长度符合要求。

请返回车队长度符合要求后，物资的分布情况。

**示例 1：**
>输入：`supplies = [7,3,6,1,8]`
>
>输出：`[10,15]`
>
>解释：
> 第 1 次合并，符合条件的两辆马车为 6,1，合并后的车队为 [7,3,7,8]；
> 第 2 次合并，符合条件的两辆马车为 (7,3) 和 (3,7)，取编号最小的 (7,3)，合并后的车队为 [10,7,8]；
> 第 3 次合并，符合条件的两辆马车为 7,8，合并后的车队为 [10,15]；
>返回 `[10,15]`

**示例 2：**
>输入：`supplies = [1,3,1,5]`
>
>输出：`[5,5]`

**解释：**
- `2 <= supplies.length <= 1000`
- `1 <= supplies[i] <= 1000`


---

[提交记录](https://leetcode.cn/problems/hqCnmP/submissions/) | [题解](https://leetcode.cn/problems/hqCnmP/solution/)


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