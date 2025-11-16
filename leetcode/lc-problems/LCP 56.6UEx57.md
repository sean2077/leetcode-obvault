---
tags:
  - leetcode/problem
questionId: "LCP 56"
title: 信物传送
translatedTitle: 信物传送
titleSlug: 6UEx57
aliases:
  - 信物传送
  - 6UEx57
  - 信物传送
lcLinks:
  - https://leetcode.com/problems/6UEx57/
  - https://leetcode.cn/problems/6UEx57/
lcTopics:
lcDifficulty: Medium
lcAcRate: 48.2%
similarQuestions:
grade: ⭐⭐⭐⭐⭐
likes: 29
dislikes: 0
favorites: []
created: 2025-11-16 12:09
updated: 2025-11-16 12:09
---

**Nav:** << previous: [[LCP 55.PTXy4P|LCP 55.采集果实]] | next: [[LCP 57.ZbAuEH|LCP 57.打地鼠]] >>

---

## Description

<p>欢迎各位勇者来到力扣城，本次试炼主题为「信物传送」。</p>

<p>本次试炼场地设有若干传送带，<code>matrix[i][j]</code>&nbsp;表示第&nbsp;<code>i</code>&nbsp;行&nbsp;<code>j</code>&nbsp;列的传送带运作方向，<code>"^","v","&lt;","&gt;"</code>&nbsp;这四种符号分别表示&nbsp;<strong>上、下、左、右</strong>&nbsp;四个方向。信物会随传送带的方向移动。勇者<strong>每一次</strong>施法操作，可<strong>临时</strong>变更一处传送带的方向，在物品经过后传送带恢复原方向。<img alt="lcp (2).gif" src="https://pic.leetcode-cn.com/1649835246-vfupSL-lcp%20(2).gif" style="height: 385px; width: 400px;" /></p>

<p>通关信物初始位于坐标&nbsp;<code>start</code>处，勇者需要将其移动到坐标&nbsp;<code>end</code>&nbsp;处，请返回勇者施法操作的最少次数。</p>

<p><strong>注意：</strong></p>

<ul>
	<li><code>start</code>&nbsp;和&nbsp;<code>end</code>&nbsp;的格式均为&nbsp;<code>[i,j]</code></li>
</ul>

<p><strong>示例 1：</strong></p>

<blockquote>
<p>输入：<code>matrix = ["&gt;&gt;v","v^&lt;","&lt;&gt;&lt;"], start = [0,1], end = [2,0]</code></p>

<p>输出：<code>1</code></p>

<p>解释： 如上图所示 当信物移动到&nbsp;<code>[1,1]</code>&nbsp;时，勇者施法一次将&nbsp;<code>[1,1]</code>&nbsp;的传送方向&nbsp;<code>^</code>&nbsp;从变更为&nbsp;<code>&lt;</code>&nbsp;从而信物移动到&nbsp;<code>[1,0]</code>，后续到达&nbsp;<code>end</code>&nbsp;位置 因此勇者最少需要施法操作 1 次</p>
</blockquote>

<p><strong>示例 2：</strong></p>

<blockquote>
<p>输入：<code>matrix = ["&gt;&gt;v","&gt;&gt;v","^&lt;&lt;"], start = [0,0], end = [1,1]</code></p>

<p>输出：<code>0</code></p>

<p>解释：勇者无需施法，信物将自动传送至&nbsp;<code>end</code>&nbsp;位置</p>
</blockquote>

<p><strong>示例 3：</strong></p>

<blockquote>
<p>输入：<code>matrix = ["&gt;^^&gt;","&lt;^v&gt;","^v^&lt;"], start = [0,0], end = [1,3]</code></p>

<p>输出：<code>3</code></p>
</blockquote>

<p><strong>提示：</strong></p>

<ul>
	<li><code>matrix</code>&nbsp;中仅包含&nbsp;<code>'^'、'v'、'&lt;'、'&gt;'</code></li>
	<li><code>0 &lt; matrix.length &lt;= 100</code></li>
	<li><code>0 &lt; matrix[i].length &lt;= 100</code></li>
	<li><code>0 &lt;= start[0],end[0] &lt; matrix.length</code></li>
	<li><code>0 &lt;= start[1],end[1] &lt; matrix[i].length</code></li>
</ul>



---

[提交记录](https://leetcode.cn/problems/6UEx57/submissions/) | [题解](https://leetcode.cn/problems/6UEx57/solution/)


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