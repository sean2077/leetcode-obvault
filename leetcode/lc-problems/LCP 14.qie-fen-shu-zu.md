---
tags:
  - leetcode/problem
questionId: "LCP 14"
title: 切分数组
translatedTitle: 切分数组
titleSlug: qie-fen-shu-zu
aliases:
  - 切分数组
  - qie-fen-shu-zu
  - 切分数组
lcLinks:
  - https://leetcode.com/problems/qie-fen-shu-zu/
  - https://leetcode.cn/problems/qie-fen-shu-zu/
lcTopics:
lcDifficulty: Hard
lcAcRate: 26.2%
similarQuestions:
grade: ⭐⭐⭐⭐⭐
likes: 66
dislikes: 0
favorites: []
created: 2025-11-16 12:09
updated: 2025-11-16 12:09
---

**Nav:** << previous: [[LCP 13.xun-bao|LCP 13.寻宝]] | next: [[LCP 15.you-le-yuan-de-mi-gong|LCP 15.游乐园的迷宫]] >>

---

## Description

<p>给定一个整数数组 <code>nums</code> ，小李想将 <code>nums</code> 切割成若干个非空子数组，使得每个子数组最左边的数和最右边的数的最大公约数大于 1 。为了减少他的工作量，请求出最少可以切成多少个子数组。</p>

<p><strong>示例 1：</strong></p>

<blockquote>
<p>输入：<code>nums = [2,3,3,2,3,3]</code></p>

<p>输出：<code>2</code></p>

<p>解释：最优切割为 [2,3,3,2] 和 [3,3] 。第一个子数组头尾数字的最大公约数为 2 ，第二个子数组头尾数字的最大公约数为 3 。</p>
</blockquote>

<p><strong>示例 2：</strong></p>

<blockquote>
<p>输入：<code>nums = [2,3,5,7]</code></p>

<p>输出：<code>4</code></p>

<p>解释：只有一种可行的切割：[2], [3], [5], [7]</p>
</blockquote>

<p><strong>限制：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10^5</code></li>
	<li><code>2 &lt;= nums[i] &lt;= 10^6</code></li>
</ul>



---

[提交记录](https://leetcode.cn/problems/qie-fen-shu-zu/submissions/) | [题解](https://leetcode.cn/problems/qie-fen-shu-zu/solution/)


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