---
tags:
  - leetcode/problem
questionId: "LCP 16"
title: 游乐园的游览计划
translatedTitle: 游乐园的游览计划
titleSlug: you-le-yuan-de-you-lan-ji-hua
aliases:
  - 游乐园的游览计划
  - you-le-yuan-de-you-lan-ji-hua
  - 游乐园的游览计划
lcLinks:
  - https://leetcode.com/problems/you-le-yuan-de-you-lan-ji-hua/
  - https://leetcode.cn/problems/you-le-yuan-de-you-lan-ji-hua/
lcTopics:
lcDifficulty: Hard
lcAcRate: 36.8%
similarQuestions:
grade: ⭐⭐⭐⭐⭐
likes: 32
dislikes: 0
favorites: []
created: 2025-11-16 12:09
updated: 2025-11-16 12:09
---

**Nav:** << previous: [[LCP 15.you-le-yuan-de-mi-gong|LCP 15.游乐园的迷宫]] | next: [[LCP 17.nGK0Fy|LCP 17.速算机器人]] >>

---

## Description

<p>又到了一年一度的春游时间，小吴计划去游乐场游玩 1 天，游乐场总共有 <code>N</code> 个游乐项目，编号从 <code>0</code> 到 <code>N-1</code>。小吴给每个游乐项目定义了一个非负整数值 <code>value[i]</code> 表示自己的喜爱值。两个游乐项目之间会有双向路径相连，整个游乐场总共有 <code>M</code> 条双向路径，保存在二维数组&nbsp;<code>edges</code>中。 小吴计划选择一个游乐项目 <code>A</code> 作为这一天游玩的重点项目。上午小吴准备游玩重点项目 <code>A</code> 以及与项目 <code>A</code> 相邻的两个项目 <code>B</code>、<code>C</code> （项目<code>A</code>、<code>B</code>与<code>C</code>要求是不同的项目，且项目<code>B</code>与项目<code>C</code>要求相邻），并返回 <code>A</code> ，即存在一条 <code>A-B-C-A</code> 的路径。 下午，小吴决定再游玩重点项目 <code>A</code>以及与<code>A</code>相邻的两个项目 <code>B&#39;</code>、<code>C&#39;</code>，（项目<code>A</code>、<code>B&#39;</code>与<code>C&#39;</code>要求是不同的项目，且项目<code>B&#39;</code>与项目<code>C&#39;</code>要求相邻），并返回 <code>A</code> ，即存在一条 <code>A-B&#39;-C&#39;-A</code> 的路径。下午游玩项目 <code>B&#39;</code>、<code>C&#39;</code> 可与上午游玩项目<code>B</code>、<code>C</code>存在重复项目。 小吴希望提前安排好游玩路径，使得喜爱值之和最大。请你返回满足游玩路径选取条件的最大喜爱值之和，如果没有这样的路径，返回 <code>0</code>。 注意：一天中重复游玩同一个项目并不能重复增加喜爱值了。例如：上下午游玩路径分别是 <code>A-B-C-A</code>与<code>A-C-D-A</code> 那么只能获得 <code>value[A] + value[B] + value[C] + value[D]</code> 的总和。</p>

<p><strong>示例 1：</strong></p>

<blockquote>
<p>输入：<code>edges = [[0,1],[1,2],[0,2]], value = [1,2,3]</code></p>

<p>输出：<code>6</code></p>

<p>解释：喜爱值之和最高的方案之一是 0-&gt;1-&gt;2-&gt;0 与 0-&gt;2-&gt;1-&gt;0 。重复游玩同一点不重复计入喜爱值，返回1+2+3=6</p>
</blockquote>

<p><strong>示例 2：</strong></p>

<blockquote>
<p>输入：<code>edges = [[0,2],[2,1]], value = [1,2,5]</code></p>

<p>输出：<code>0</code></p>

<p>解释：无满足要求的游玩路径，返回 0</p>
</blockquote>

<p><strong>示例 3：</strong></p>

<blockquote>
<p>输入：<code>edges = [[0,1],[0,2],[0,3],[0,4],[0,5],[1,3],[2,4],[2,5],[3,4],[3,5],[4,5]], value = [7,8,6,8,9,7]</code></p>

<p>输出：<code>39</code></p>

<p>解释：喜爱值之和最高的方案之一是 3-&gt;0-&gt;1-&gt;3 与 3-&gt;4-&gt;5-&gt;3 。喜爱值最高为 7+8+8+9+7=39</p>
</blockquote>

<p><strong>限制：</strong></p>

<ul>
	<li><code>3 &lt;= value.length &lt;= 10000</code></li>
	<li><code>1 &lt;=&nbsp;edges.length &lt;= 10000</code></li>
	<li><code>0 &lt;= edges[i][0],edges[i][1] &lt;&nbsp;value.length</code></li>
	<li><code>0 &lt;= value[i] &lt;= 10000</code></li>
	<li><code>edges中没有重复的边</code></li>
	<li><code>edges[i][0] != edges[i][1]</code></li>
</ul>



---

[提交记录](https://leetcode.cn/problems/you-le-yuan-de-you-lan-ji-hua/submissions/) | [题解](https://leetcode.cn/problems/you-le-yuan-de-you-lan-ji-hua/solution/)


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