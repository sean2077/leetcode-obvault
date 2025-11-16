---
tags:
  - leetcode/problem
questionId: "LCP 49"
title: 环形闯关游戏
translatedTitle: 环形闯关游戏
titleSlug: K8GULz
aliases:
  - 环形闯关游戏
  - K8GULz
  - 环形闯关游戏
lcLinks:
  - https://leetcode.com/problems/K8GULz/
  - https://leetcode.cn/problems/K8GULz/
lcTopics:
lcDifficulty: Hard
lcAcRate: 40.3%
similarQuestions:
grade: ⭐⭐⭐⭐⭐
likes: 14
dislikes: 0
favorites: []
created: 2025-11-16 12:09
updated: 2025-11-16 12:09
---

**Nav:** << previous: [[LCP 48.fsa7oZ|LCP 48.无限棋局]] | next: [[LCP 50.WHnhjV|LCP 50.宝石补给]] >>

---

## Description

「力扣挑战赛」中有一个由 `N` 个关卡组成的**环形**闯关游戏，关卡编号为 `0`~`N-1`，编号 `0` 的关卡和编号 `N-1` 的关卡相邻。每个关卡均有积分要求，`challenge[i]` 表示挑战编号 `i` 的关卡最少需要拥有的积分。
![图片.png](https://pic.leetcode-cn.com/1630392170-ucncVS-%E5%9B%BE%E7%89%87.png){:width="240px"}


小扣想要挑战关卡，闯关具体规则如下：

- 初始小扣可以指定其中一个关卡为「开启」状态，其余关卡将处于「未开启」状态。
- 小扣可以挑战处于「开启」状态且**满足最少积分要求**的关卡，若小扣挑战该关卡前积分为 `score`，挑战结束后，积分将增长为 `score|challenge[i]`（即位运算中的 `"OR"` 运算）
- 在挑战某个关卡后，该关卡两侧相邻的关卡将会开启（若之前未开启）

请帮助小扣进行计算，初始最少需要多少积分，可以挑战 **环形闯关游戏** 的所有关卡。

**示例1：**

> 输入：`challenge = [5,4,6,2,7]`
>
> 输出：`4`
> 
> 解释： 初始选择编号 3 的关卡开启，积分为 4
>挑战编号 3 的关卡，积分变为 $4 | 2 = 6$，开启 2、4 处的关卡
>挑战编号 2 的关卡，积分变为 $6 | 6 = 6$，开启 1 处的关卡
>挑战编号 1 的关卡，积分变为 $6 | 4 = 6$，开启 0 处的关卡
>挑战编号 0 的关卡，积分变为 $6 | 5 = 7$
>挑战编号 4 的关卡，顺利完成全部的关卡


**示例2：**

> 输入：`challenge = [12,7,11,3,9]`
>
> 输出：`8`
>
> 解释： 初始选择编号 3 的关卡开启，积分为 8
>挑战编号 3 的关卡，积分变为 $8 | 3 = 11$，开启 2、4 处的关卡
>挑战编号 2 的关卡，积分变为 $11 | 11 = 11$，开启 1 处的关卡
>挑战编号 4 的关卡，积分变为 $11 | 9 = 11$，开启 0 处的关卡
>挑战编号 1 的关卡，积分变为 $11 | 7 = 15$
>挑战编号 0 的关卡，顺利完成全部的关卡

**示例3：**

> 输入：`challenge = [1,1,1]`
>
> 输出：`1`

**提示：** 
- `1 <= challenge.length <= 5*10^4`
- `1 <= challenge[i] <= 10^14`


---

[提交记录](https://leetcode.cn/problems/K8GULz/submissions/) | [题解](https://leetcode.cn/problems/K8GULz/solution/)


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