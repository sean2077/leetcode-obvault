---
tags:
  - leetcode/problem
questionId: "LCP 73"
title: 探险营地
translatedTitle: 探险营地
titleSlug: 0Zeoeg
aliases:
  - 探险营地
  - 0Zeoeg
  - 探险营地
lcLinks:
  - https://leetcode.com/problems/0Zeoeg/
  - https://leetcode.cn/problems/0Zeoeg/
lcTopics:
lcDifficulty: Medium
lcAcRate: 47.2%
similarQuestions:
grade: ⭐⭐⭐⭐⭐
likes: 4
dislikes: 0
favorites: []
created: 2025-11-16 11:17
updated: 2025-11-16 11:17
---

**Nav:** << previous: [[LCP 72.hqCnmP|LCP 72.补给马车]] | next: [[LCP 74.xepqZ5|LCP 74.最强祝福力场]] >>

---

## Description

探险家小扣的行动轨迹，都将保存在记录仪中。`expeditions[i]` 表示小扣第 `i` 次探险记录，用一个字符串数组表示。其中的每个「营地」由大小写字母组成，通过子串 `->` 连接。
> 例："Leet->code->Campsite"，表示到访了 "Leet"、"code"、"Campsite" 三个营地。

`expeditions[0]` 包含了初始小扣已知的所有营地；对于之后的第 `i` 次探险(即 `expeditions[i]` 且 i > 0)，如果记录中包含了之前均没出现的营地，则表示小扣 **新发现** 的营地。

请你找出小扣发现新营地最多且索引最小的那次探险，并返回对应的记录索引。如果所有探险记录都没有发现新的营地，返回 `-1`

**注意：**
- 大小写不同的营地视为不同的营地；
- 营地的名称长度均大于 `0`。

**示例 1：**
>输入：`expeditions = ["leet->code","leet->code->Campsite->Leet","leet->code->leet->courier"]`
>
>输出：`1`
>
>解释：
>初始已知的所有营地为 "leet" 和 "code"
>第 1 次，到访了 "leet"、"code"、"Campsite"、"Leet"，新发现营地 2 处："Campsite"、"Leet"
>第 2 次，到访了 "leet"、"code"、"courier"，新发现营地 1 处："courier"
>第 1 次探险发现的新营地数量最多，因此返回 `1`

**示例 2：**
>输入：`expeditions = ["Alice->Dex","","Dex"]`
>
>输出：`-1`
>
>解释：
>初始已知的所有营地为 "Alice" 和 "Dex"
>第 1 次，未到访任何营地；
>第 2 次，到访了 "Dex"，未新发现营地；
>因为两次探险均未发现新的营地，返回 `-1`

**示例 3：**
>输入：`expeditions = ["","Gryffindor->Slytherin->Gryffindor","Hogwarts->Hufflepuff->Ravenclaw"]`
>
>输出：`2`
>
>解释：
>初始未发现任何营地；
>第 1 次，到访 "Gryffindor"、"Slytherin" 营地，其中重复到访 "Gryffindor" 两次，
>因此新发现营地为 2 处："Gryffindor"、"Slytherin"
>第 2 次，到访 "Hogwarts"、"Hufflepuff"、"Ravenclaw" 营地；
>新发现营地 3 处："Hogwarts"、"Hufflepuff"、"Ravenclaw"；
>第 2 次探险发现的新营地数量最多，因此返回 `2`

**提示：**
- `1 <= expeditions.length <= 1000`
- `0 <= expeditions[i].length <= 1000`
- 探险记录中只包含大小写字母和子串"->"


---

[提交记录](https://leetcode.cn/problems/0Zeoeg/submissions/) | [题解](https://leetcode.cn/problems/0Zeoeg/solution/)


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