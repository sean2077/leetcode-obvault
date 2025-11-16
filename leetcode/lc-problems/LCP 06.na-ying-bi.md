---
tags:
  - leetcode/problem
questionId: "LCP 06"
title: 拿硬币
translatedTitle: 拿硬币
titleSlug: na-ying-bi
aliases:
  - 拿硬币
  - na-ying-bi
  - 拿硬币
lcLinks:
  - https://leetcode.com/problems/na-ying-bi/
  - https://leetcode.cn/problems/na-ying-bi/
lcTopics:
lcDifficulty: Easy
lcAcRate: 84.5%
similarQuestions:
grade: ⭐⭐⭐⭐⭐
likes: 132
dislikes: 0
favorites: []
created: 2025-11-16 11:17
updated: 2025-11-16 11:17
---

**Nav:** << previous: [[LCP 05.coin-bonus|LCP 05.发 LeetCoin]] | next: [[LCP 07.chuan-di-xin-xi|LCP 07.传递信息]] >>

---

## Description

<p>桌上有 <code>n</code> 堆力扣币，每堆的数量保存在数组 <code>coins</code> 中。我们每次可以选择任意一堆，拿走其中的一枚或者两枚，求拿完所有力扣币的最少次数。</p>

<p><strong>示例 1：</strong></p>

<blockquote>
<p>输入：<code>[4,2,1]</code></p>

<p>输出：<code>4</code></p>

<p>解释：第一堆力扣币最少需要拿 2 次，第二堆最少需要拿 1 次，第三堆最少需要拿 1 次，总共 4 次即可拿完。</p>
</blockquote>

<p><strong>示例 2：</strong></p>

<blockquote>
<p>输入：<code>[2,3,10]</code></p>

<p>输出：<code>8</code></p>
</blockquote>

<p><strong>限制：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 4</code></li>
	<li><code>1 &lt;= coins[i] &lt;= 10</code></li>
</ul>



---

[提交记录](https://leetcode.cn/problems/na-ying-bi/submissions/) | [题解](https://leetcode.cn/problems/na-ying-bi/solution/)


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