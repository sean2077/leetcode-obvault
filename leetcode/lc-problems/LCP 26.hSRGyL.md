---
tags:
  - leetcode/problem
questionId: "LCP 26"
title: 导航装置
translatedTitle: 导航装置
titleSlug: hSRGyL
aliases:
  - 导航装置
  - hSRGyL
  - 导航装置
lcLinks:
  - https://leetcode.com/problems/hSRGyL/
  - https://leetcode.cn/problems/hSRGyL/
lcTopics:
lcDifficulty: Hard
lcAcRate: 37.5%
similarQuestions:
grade: ⭐⭐⭐⭐⭐
likes: 22
dislikes: 0
favorites: []
created: 2025-11-16 12:09
updated: 2025-11-16 12:09
---

**Nav:** << previous: [[LCP 25.Uh984O|LCP 25.古董键盘]] | next: [[LCP 27.IQvJ9i|LCP 27.黑盒光线反射]] >>

---

## Description

小扣参加的秋日市集景区共有 $N$ 个景点，景点编号为 $1$~$N$。景点内设有 $N-1$ 条双向道路，使所有景点形成了一个二叉树结构，根结点记为 `root`，景点编号即为节点值。

由于秋日市集景区的结构特殊，游客很容易迷路，主办方决定在景区的若干个景点设置导航装置，按照所在景点编号升序排列后定义装置编号为 1 ~ M。导航装置向游客发送数据，数据内容为列表 `[游客与装置 1 的相对距离,游客与装置 2 的相对距离,...,游客与装置 M 的相对距离]`。由于游客根据导航装置发送的信息来确认位置，因此主办方需保证游客在每个景点接收的数据信息皆不相同。请返回主办方最少需要设置多少个导航装置。

**示例 1：**
>输入：`root = [1,2,null,3,4]`
>
>输出：`2`
>
>解释：在景点 1、3 或景点 1、4 或景点 3、4 设置导航装置。
>
>![image.png](https://pic.leetcode-cn.com/1597996812-tqrgwu-image.png){:height="250px"}



**示例 2：**
>输入：`root = [1,2,3,4]`
>
>输出：`1`
>
>解释：在景点 3、4 设置导航装置皆可。
>
>![image.png](https://pic.leetcode-cn.com/1597996826-EUQRyz-image.png){:height="200px"}



**提示：**
- `2 <= N <= 50000`
- 二叉树的非空节点值为 `1~N` 的一个排列。



---

[提交记录](https://leetcode.cn/problems/hSRGyL/submissions/) | [题解](https://leetcode.cn/problems/hSRGyL/solution/)


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