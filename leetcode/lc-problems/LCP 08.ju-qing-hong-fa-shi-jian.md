---
tags:
  - leetcode/problem
questionId: "LCP 08"
title: 剧情触发时间
translatedTitle: 剧情触发时间
titleSlug: ju-qing-hong-fa-shi-jian
aliases:
  - 剧情触发时间
  - ju-qing-hong-fa-shi-jian
  - 剧情触发时间
lcLinks:
  - https://leetcode.com/problems/ju-qing-hong-fa-shi-jian/
  - https://leetcode.cn/problems/ju-qing-hong-fa-shi-jian/
lcTopics:
lcDifficulty: Medium
lcAcRate: 39.3%
similarQuestions:
grade: ⭐⭐⭐⭐⭐
likes: 66
dislikes: 0
favorites: []
created: 2025-11-16 11:17
updated: 2025-11-16 11:17
---

**Nav:** << previous: [[LCP 07.chuan-di-xin-xi|LCP 07.传递信息]] | next: [[LCP 09.zui-xiao-tiao-yue-ci-shu|LCP 09.最小跳跃次数]] >>

---

## Description

<p>在战略游戏中，玩家往往需要发展自己的势力来触发各种新的剧情。一个势力的主要属性有三种，分别是文明等级（<code>C</code>），资源储备（<code>R</code>）以及人口数量（<code>H</code>）。在游戏开始时（第 0 天），三种属性的值均为 0。</p>

<p>随着游戏进程的进行，每一天玩家的三种属性都会对应<strong>增加</strong>，我们用一个二维数组 <code>increase</code> 来表示每天的增加情况。这个二维数组的每个元素是一个长度为 3 的一维数组，例如 <code>[[1,2,1],[3,4,2]]</code> 表示第一天三种属性分别增加 <code>1,2,1</code> 而第二天分别增加 <code>3,4,2</code>。</p>

<p>所有剧情的触发条件也用一个二维数组 <code>requirements</code> 表示。这个二维数组的每个元素是一个长度为 3 的一维数组，对于某个剧情的触发条件 <code>c[i], r[i], h[i]</code>，如果当前 <code>C &gt;= c[i]</code> 且 <code>R &gt;= r[i]</code> 且 <code>H &gt;= h[i]</code> ，则剧情会被触发。</p>

<p>根据所给信息，请计算每个剧情的触发时间，并以一个数组返回。如果某个剧情不会被触发，则该剧情对应的触发时间为 -1 。</p>

<p><strong>示例 1：</strong></p>

<blockquote>
<p>输入： <code>increase = [[2,8,4],[2,5,0],[10,9,8]]</code> <code>requirements = [[2,11,3],[15,10,7],[9,17,12],[8,1,14]]</code></p>

<p>输出: <code>[2,-1,3,-1]</code></p>

<p>解释：</p>

<p>初始时，C = 0，R = 0，H = 0</p>

<p>第 1 天，C = 2，R = 8，H = 4</p>

<p>第 2 天，C = 4，R = 13，H = 4，此时触发剧情 0</p>

<p>第 3 天，C = 14，R = 22，H = 12，此时触发剧情 2</p>

<p>剧情 1 和 3 无法触发。</p>
</blockquote>

<p><strong>示例 2：</strong></p>

<blockquote>
<p>输入： <code>increase = [[0,4,5],[4,8,8],[8,6,1],[10,10,0]]</code> <code>requirements = [[12,11,16],[20,2,6],[9,2,6],[10,18,3],[8,14,9]]</code></p>

<p>输出: <code>[-1,4,3,3,3]</code></p>
</blockquote>

<p><strong>示例 3：</strong></p>

<blockquote>
<p>输入： <code>increase = [[1,1,1]]</code> <code>requirements = [[0,0,0]]</code></p>

<p>输出: <code>[0]</code></p>
</blockquote>

<p><strong>限制：</strong></p>

<ul>
	<li><code>1 &lt;= increase.length &lt;= 10000</code></li>
	<li><code>1 &lt;= requirements.length &lt;= 100000</code></li>
	<li><code>0 &lt;= increase[i] &lt;= 10</code></li>
	<li><code>0 &lt;= requirements[i] &lt;= 100000</code></li>
</ul>



---

[提交记录](https://leetcode.cn/problems/ju-qing-hong-fa-shi-jian/submissions/) | [题解](https://leetcode.cn/problems/ju-qing-hong-fa-shi-jian/solution/)


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