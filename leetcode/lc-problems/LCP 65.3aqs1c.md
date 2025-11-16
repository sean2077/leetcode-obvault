---
tags:
  - leetcode/problem
questionId: "LCP 65"
title: 舒适的湿度
translatedTitle: 舒适的湿度
titleSlug: 3aqs1c
aliases:
  - 舒适的湿度
  - 3aqs1c
  - 舒适的湿度
lcLinks:
  - https://leetcode.com/problems/3aqs1c/
  - https://leetcode.cn/problems/3aqs1c/
lcTopics:
lcDifficulty: Hard
lcAcRate: 48.7%
similarQuestions:
grade: ⭐⭐⭐⭐⭐
likes: 15
dislikes: 0
favorites: []
created: 2025-11-16 12:09
updated: 2025-11-16 12:09
---

**Nav:** << previous: [[LCP 64.U7WvvU|LCP 64.二叉树灯饰]] | next: [[LCP 66.600YaG|LCP 66.最小展台数量]] >>

---

## Description

力扣嘉年华为了确保更舒适的游览环境条件，在会场的各处设置了湿度调节装置，这些调节装置受控于总控室中的一台控制器。
控制器中已经预设了一些调节指令，整数数组`operate[i]` 表示第 `i` 条指令增加空气湿度的大小。现在你可以将任意数量的指令修改为降低湿度（变化的数值不变），以确保湿度尽可能的适宜：
- 控制器会选择 **一段连续的指令** ，从而进行湿度调节的操作；
- 这段指令最终对湿度影响的绝对值，即为当前操作的「不适宜度」
- 在控制器所有可能的操作中，**最大** 的「不适宜度」即为「整体不适宜度」

请返回在所有修改指令的方案中，可以得到的 **最小** 「整体不适宜度」。

**示例 1：**
> 输入：`operate = [5,3,7]`
>
> 输出：`8`
>
> 解释：对于方案 `2` 的 `[5,3,-7]`
>操作指令 `[5],[3],[-7]` 的「不适宜度」分别为 `5,3,7`
>操作指令 `[5,3],[3,-7]` 的「不适宜度」分别为 `8,4`
>操作指令 `[5,3,-7]` 的「不适宜度」为 `1`，
>因此对于方案 `[5,3,-7]`的「整体不适宜度」为 `8`，其余方案的「整体不适宜度」均不小于 `8`，如下表所示：
![image.png](https://pic.leetcode-cn.com/1663902759-dgDCxn-image.png){:width=650px}

**示例 2：**
> 输入：`operate = [20,10]`
>
> 输出：`20`

**提示：**
- `1 <= operate.length <= 1000`
- `1 <= operate[i] <= 1000`


---

[提交记录](https://leetcode.cn/problems/3aqs1c/submissions/) | [题解](https://leetcode.cn/problems/3aqs1c/solution/)


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