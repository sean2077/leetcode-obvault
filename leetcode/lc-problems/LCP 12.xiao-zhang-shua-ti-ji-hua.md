---
tags:
  - leetcode/problem
questionId: "LCP 12"
title: 小张刷题计划
translatedTitle: 小张刷题计划
titleSlug: xiao-zhang-shua-ti-ji-hua
aliases:
  - 小张刷题计划
  - xiao-zhang-shua-ti-ji-hua
  - 小张刷题计划
lcLinks:
  - https://leetcode.com/problems/xiao-zhang-shua-ti-ji-hua/
  - https://leetcode.cn/problems/xiao-zhang-shua-ti-ji-hua/
lcTopics:
lcDifficulty: Medium
lcAcRate: 44.5%
similarQuestions:
grade: ⭐⭐⭐⭐⭐
likes: 114
dislikes: 0
favorites: []
created: 2025-11-16 11:17
updated: 2025-11-16 11:17
---

**Nav:** << previous: [[LCP 11.qi-wang-ge-shu-tong-ji|LCP 11.期望个数统计]] | next: [[LCP 13.xun-bao|LCP 13.寻宝]] >>

---

## Description

<p>为了提高自己的代码能力，小张制定了 <code>LeetCode</code> 刷题计划，他选中了 <code>LeetCode</code> 题库中的 <code>n</code> 道题，编号从 <code>0</code> 到 <code>n-1</code>，并计划在 <code>m</code> 天内<strong>按照题目编号顺序</strong>刷完所有的题目（注意，小张不能用多天完成同一题）。</p>

<p>在小张刷题计划中，小张需要用 <code>time[i]</code> 的时间完成编号 <code>i</code> 的题目。此外，小张还可以使用场外求助功能，通过询问他的好朋友小杨题目的解法，可以省去该题的做题时间。为了防止&ldquo;小张刷题计划&rdquo;变成&ldquo;小杨刷题计划&rdquo;，小张每天最多使用一次求助。</p>

<p>我们定义 <code>m</code> 天中做题时间最多的一天耗时为 <code>T</code>（小杨完成的题目不计入做题总时间）。请你帮小张求出最小的 <code>T</code>是多少。</p>

<p><strong>示例 1：</strong></p>

<blockquote>
<p>输入：<code>time = [1,2,3,3], m = 2</code></p>

<p>输出：<code>3</code></p>

<p>解释：第一天小张完成前三题，其中第三题找小杨帮忙；第二天完成第四题，并且找小杨帮忙。这样做题时间最多的一天花费了 3 的时间，并且这个值是最小的。</p>
</blockquote>

<p><strong>示例 2：</strong></p>

<blockquote>
<p>输入：<code>time = [999,999,999], m = 4</code></p>

<p>输出：<code>0</code></p>

<p>解释：在前三天中，小张每天求助小杨一次，这样他可以在三天内完成所有的题目并不花任何时间。</p>
</blockquote>

<p>&nbsp;</p>

<p><strong>限制：</strong></p>

<ul>
	<li><code>1 &lt;= time.length &lt;= 10^5</code></li>
	<li><code>1 &lt;= time[i] &lt;= 10000</code></li>
	<li><code>1 &lt;= m &lt;= 1000</code></li>
</ul>



---

[提交记录](https://leetcode.cn/problems/xiao-zhang-shua-ti-ji-hua/submissions/) | [题解](https://leetcode.cn/problems/xiao-zhang-shua-ti-ji-hua/solution/)


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