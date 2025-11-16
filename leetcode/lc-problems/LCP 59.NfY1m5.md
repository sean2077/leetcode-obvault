---
tags:
  - leetcode/problem
questionId: "LCP 59"
title: 搭桥过河
translatedTitle: 搭桥过河
titleSlug: NfY1m5
aliases:
  - 搭桥过河
  - NfY1m5
  - 搭桥过河
lcLinks:
  - https://leetcode.com/problems/NfY1m5/
  - https://leetcode.cn/problems/NfY1m5/
lcTopics:
lcDifficulty: Hard
lcAcRate: 26.4%
similarQuestions:
grade: ⭐⭐⭐⭐⭐
likes: 12
dislikes: 0
favorites: []
created: 2025-11-16 11:17
updated: 2025-11-16 11:17
---

**Nav:** << previous: [[LCP 58.De4qBB|LCP 58.积木拼接]] | next: [[LCP 60.WInSav|LCP 60.力扣泡泡龙]] >>

---

## Description

欢迎各位勇者来到力扣城，本次试炼主题为「搭桥过河」。

勇者面前有一段长度为 `num` 的河流，河流可以划分为若干河道。每条河道上恰有一块浮木，`wood[i]` 记录了第 `i` 条河道上的浮木初始的覆盖范围。

- 当且仅当浮木与相邻河道的浮木覆盖范围有重叠时，勇者才可以在两条浮木间移动
- 勇者 **仅能在岸上** 通过花费一点「自然之力」，使任意一条浮木沿着河流移动一个单位距离

请问勇者跨越这条河流，最少需要花费多少「自然之力」。


**示例 1：**
> 输入： `num = 10, wood = [[1,2],[4,7],[8,9]]`
> 输出： `3`
> 解释：如下图所示，
> 将 [1,2] 浮木移动至 [3,4]，花费 2「自然之力」，
> 将 [8,9] 浮木移动至 [7,8]，花费 1「自然之力」，
> 此时勇者可以顺着 [3,4]->[4,7]->[7,8] 跨越河流，
> 因此，勇者最少需要花费 3 点「自然之力」跨越这条河流
![wood (2).gif](https://pic.leetcode-cn.com/1648196478-ophADL-wood%20\(2\).gif){:width=650px}


**示例 2：**
> 输入： `num = 10, wood = [[1,5],[1,1],[10,10],[6,7],[7,8]]`
> 输出： `10`
> 解释：
> 将 [1,5] 浮木移动至 [2,6]，花费 1「自然之力」，
> 将 [1,1] 浮木移动至 [6,6]，花费 5「自然之力」，
> 将 [10,10] 浮木移动至 [6,6]，花费 4「自然之力」，
> 此时勇者可以顺着 [2,6]->[6,6]->[6,6]->[6,7]->[7,8] 跨越河流，
> 因此，勇者最少需要花费 10 点「自然之力」跨越这条河流


**示例 3：**
> 输入： `num = 5, wood = [[1,2],[2,4]]`
> 输出： `0`
> 解释：勇者不需要移动浮木，仍可以跨越这条河流

**提示:**
- `1 <= num <= 10^9`
- `1 <= wood.length <= 10^5`
- `wood[i].length == 2`
- `1 <= wood[i][0] <= wood[i][1] <= num`




---

[提交记录](https://leetcode.cn/problems/NfY1m5/submissions/) | [题解](https://leetcode.cn/problems/NfY1m5/solution/)


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