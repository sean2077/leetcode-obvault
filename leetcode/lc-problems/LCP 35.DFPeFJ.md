---
tags:
  - leetcode/problem
questionId: "LCP 35"
title: 电动车游城市
translatedTitle: 电动车游城市
titleSlug: DFPeFJ
aliases:
  - 电动车游城市
  - DFPeFJ
  - 电动车游城市
lcLinks:
  - https://leetcode.com/problems/DFPeFJ/
  - https://leetcode.cn/problems/DFPeFJ/
lcTopics:
lcDifficulty: Hard
lcAcRate: 54.9%
similarQuestions:
grade: ⭐⭐⭐⭐⭐
likes: 54
dislikes: 0
favorites: []
created: 2025-11-16 11:17
updated: 2025-11-16 11:17
---

**Nav:** << previous: [[LCP 34.er-cha-shu-ran-se-UGC|LCP 34.二叉树染色]] | next: [[LCP 36.Up5XYM|LCP 36.最多牌组数]] >>

---

## Description

<p>小明的电动车电量充满时可行驶距离为&nbsp;<code>cnt</code>，每行驶 1 单位距离消耗 1 单位电量，且花费 1 单位时间。小明想选择电动车作为代步工具。地图上共有 N 个景点，景点编号为 0 ~ N-1。他将地图信息以&nbsp;<code>[城市 A 编号,城市 B 编号,两城市间距离]</code>&nbsp;格式整理在在二维数组&nbsp;<code>paths</code>，表示城市 A、B 间存在双向通路。初始状态，电动车电量为 0。每个城市都设有充电桩，<code>charge[i]</code>&nbsp;表示第 i 个城市每充 1 单位电量需要花费的单位时间。请返回小明最少需要花费多少单位时间从起点城市&nbsp;<code>start</code>&nbsp;抵达终点城市&nbsp;<code>end</code>。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong><code>paths = [[1,3,3],[3,2,1],[2,1,3],[0,1,4],[3,0,5]], cnt = 6, start = 1, end = 0, charge = [2,10,4,1]</code>
<strong>输出：</strong><code>43</code>
<strong>解释：</strong>最佳路线为：1-&gt;3-&gt;0。 在城市 1 仅充 3 单位电至城市 3，然后在城市 3 充 5 单位电，行驶至城市 0。 充电用时共 3*10 + 5*1= 35 行驶用时 3 + 5 = 8，此时总用时最短 43。
</pre>
<img alt="image.png" src="https://pic.leetcode-cn.com/1616125304-mzVxIV-image.png" />
<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong><code>paths = [[0,4,2],[4,3,5],[3,0,5],[0,1,5],[3,2,4],[1,2,8]], cnt = 8, start = 0, end = 2, charge = [4,1,1,3,2]</code>
<strong>输出：</strong><code>38</code>
<strong>解释：</strong>最佳路线为：0-&gt;4-&gt;3-&gt;2。 城市 0 充电 2 单位，行驶至城市 4 充电 8 单位，行驶至城市 3 充电 1 单位，最终行驶至城市 2。 充电用时 4*2+2*8+3*1 = 27 行驶用时 2+5+4 = 11，总用时最短 38。
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= paths.length &lt;= 200</code></li>
	<li><code>paths[i].length == 3</code></li>
	<li><code>2 &lt;= charge.length == n &lt;= 100</code></li>
	<li><code>0 &lt;= path[i][0],path[i][1],start,end &lt; n</code></li>
	<li><code>1 &lt;= cnt &lt;= 100</code></li>
	<li><code>1 &lt;= path[i][2] &lt;= cnt</code></li>
	<li><code>1 &lt;= charge[i] &lt;= 100</code></li>
	<li>题目保证所有城市相互可以到达</li>
</ul>



---

[提交记录](https://leetcode.cn/problems/DFPeFJ/submissions/) | [题解](https://leetcode.cn/problems/DFPeFJ/solution/)


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