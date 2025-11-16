---
tags:
  - leetcode/problem
questionId: "LCP 80"
title: 生物进化录
translatedTitle: 生物进化录
titleSlug: qoQAMX
aliases:
  - 生物进化录
  - qoQAMX
  - 生物进化录
lcLinks:
  - https://leetcode.com/problems/qoQAMX/
  - https://leetcode.cn/problems/qoQAMX/
lcTopics:
lcDifficulty: Hard
lcAcRate: 48.7%
similarQuestions:
grade: ⭐⭐⭐⭐⭐
likes: 5
dislikes: 0
favorites: []
created: 2025-11-16 11:17
updated: 2025-11-16 11:17
---

**Nav:** << previous: [[LCP 79.kjpLFZ|LCP 79.提取咒文]] | next: [[LCP 81.ryfUiz|LCP 81.与非的谜题]] >>

---

## Description

在永恒之森中，存在着一本生物进化录，以 **一个树形结构** 记载了所有生物的演化过程。经过观察并整理了各节点间的关系，`parents[i]` 表示编号 `i` 节点的父节点编号(根节点的父节点为 `-1`)。

为了探索和记录其中的演化规律，队伍中的炼金术师提出了一种方法，可以以字符串的形式将其复刻下来，规则如下：
- 初始只有一个根节点，表示演化的起点，依次记录 `01` 字符串中的字符，
- 如果记录 `0`，则在当前节点下添加一个子节点，并将指针指向新添加的子节点；
- 如果记录 `1`，则将指针回退到当前节点的父节点处。

现在需要应用上述的记录方法，复刻下它的演化过程。请返回能够复刻演化过程的字符串中， **字典序最小** 的 `01` 字符串。

**注意：**
- 节点指针最终可以停在任何节点上，不一定要回到根节点。

**示例 1：**
> 输入：`parents = [-1,0,0,2]`
>
> 输出：`"00110"`
>
>解释：树结构如下图所示，共存在 2 种记录方案：
>第 1 种方案为：0(记录编号 1 的节点) -> 1(回退至节点 0) -> 0(记录编号 2 的节点) -> 0((记录编号 3 的节点))
>第 2 种方案为：0(记录编号 2 的节点) -> 0(记录编号 3 的节点) -> 1(回退至节点 2) -> 1(回退至节点 0) -> 0(记录编号 1 的节点)
>返回字典序更小的 `"00110"`
![image.png](https://pic.leetcode.cn/1682319485-cRVudI-image.png){:width=120px}![进化 (3).gif](https://pic.leetcode.cn/1682412701-waHdnm-%E8%BF%9B%E5%8C%96%20\(3\).gif){:width=320px}



**示例 2：**
> 输入：`parents = [-1,0,0,1,2,2]`
>
> 输出：`"00101100"`

**提示：**

- `1 <= parents.length <= 10^4`
- `-1 <= parents[i] < i` (即父节点编号小于子节点)


---

[提交记录](https://leetcode.cn/problems/qoQAMX/submissions/) | [题解](https://leetcode.cn/problems/qoQAMX/solution/)


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