---
tags:
  - leetcode/problem
questionId: "LCP 28"
title: 采购方案
translatedTitle: 采购方案
titleSlug: 4xy4Wx
aliases:
  - 采购方案
  - 4xy4Wx
  - 采购方案
lcLinks:
  - https://leetcode.com/problems/4xy4Wx/
  - https://leetcode.cn/problems/4xy4Wx/
lcTopics:
lcDifficulty: Easy
lcAcRate: 35.2%
similarQuestions:
grade: ⭐⭐⭐⭐⭐
likes: 69
dislikes: 0
favorites: []
created: 2025-11-16 11:17
updated: 2025-11-16 11:17
---

**Nav:** << previous: [[LCP 27.IQvJ9i|LCP 27.黑盒光线反射]] | next: [[LCP 29.SNJvJP|LCP 29.乐团站位]] >>

---

## Description

小力将 N 个零件的报价存于数组 `nums`。小力预算为 `target`，假定小力仅购买两个零件，要求购买零件的花费不超过预算，请问他有多少种采购方案。

注意：答案需要以 `1e9 + 7 (1000000007)` 为底取模，如：计算初始结果为：`1000000008`，请返回 `1`


**示例 1：**
>输入：`nums = [2,5,3,5], target = 6`
>
>输出：`1`
>
>解释：预算内仅能购买 nums[0] 与 nums[2]。

**示例 2：**
>输入：`nums = [2,2,1,9], target = 10`
>
>输出：`4`
>
>解释：符合预算的采购方案如下：
>nums[0] + nums[1] = 4
>nums[0] + nums[2] = 3
>nums[1] + nums[2] = 3
>nums[2] + nums[3] = 10

**提示：**
- `2 <= nums.length <= 10^5`
- `1 <= nums[i], target <= 10^5`



---

[提交记录](https://leetcode.cn/problems/4xy4Wx/submissions/) | [题解](https://leetcode.cn/problems/4xy4Wx/solution/)


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