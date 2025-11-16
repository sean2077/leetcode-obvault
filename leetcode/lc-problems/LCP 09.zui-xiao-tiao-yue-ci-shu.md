---
tags:
  - leetcode/problem
questionId: "LCP 09"
title: 最小跳跃次数
translatedTitle: 最小跳跃次数
titleSlug: zui-xiao-tiao-yue-ci-shu
aliases:
  - 最小跳跃次数
  - zui-xiao-tiao-yue-ci-shu
  - 最小跳跃次数
lcLinks:
  - https://leetcode.com/problems/zui-xiao-tiao-yue-ci-shu/
  - https://leetcode.cn/problems/zui-xiao-tiao-yue-ci-shu/
lcTopics:
lcDifficulty: Hard
lcAcRate: 32.6%
similarQuestions:
grade: ⭐⭐⭐⭐⭐
likes: 101
dislikes: 0
favorites: []
created: 2025-11-16 11:17
updated: 2025-11-16 11:17
---

**Nav:** << previous: [[LCP 08.ju-qing-hong-fa-shi-jian|LCP 08.剧情触发时间]] | next: [[LCP 10.er-cha-shu-ren-wu-diao-du|LCP 10.二叉树任务调度]] >>

---

## Description

<p>为了给刷题的同学一些奖励，力扣团队引入了一个弹簧游戏机。游戏机由 <code>N</code> 个特殊弹簧排成一排，编号为 <code>0</code> 到 <code>N-1</code>。初始有一个小球在编号 <code>0</code> 的弹簧处。若小球在编号为 <code>i</code> 的弹簧处，通过按动弹簧，可以选择把小球向右弹射&nbsp;<code>jump[i]</code> 的距离，或者向左弹射到任意左侧弹簧的位置。也就是说，在编号为 <code>i</code> 弹簧处按动弹簧，小球可以弹向 <code>0</code> 到 <code>i-1</code> 中任意弹簧或者 <code>i+jump[i]</code> 的弹簧（若 <code>i+jump[i]&gt;=N</code> ，则表示小球弹出了机器）。小球位于编号 0 处的弹簧时不能再向左弹。</p>

<p>为了获得奖励，你需要将小球弹出机器。请求出最少需要按动多少次弹簧，可以将小球从编号 <code>0</code> 弹簧弹出整个机器，即向右越过编号 <code>N-1</code> 的弹簧。</p>

<p><strong>示例 1：</strong></p>

<blockquote>
<p>输入：<code>jump = [2, 5, 1, 1, 1, 1]</code></p>

<p>输出：<code>3</code></p>

<p>解释：小 Z 最少需要按动 3 次弹簧，小球依次到达的顺序为 0 -&gt; 2 -&gt; 1 -&gt; 6，最终小球弹出了机器。</p>
</blockquote>

<p><strong>限制：</strong></p>

<ul>
	<li><code>1 &lt;= jump.length &lt;= 10^6</code></li>
	<li><code>1 &lt;= jump[i] &lt;= 10000</code></li>
</ul>



---

[提交记录](https://leetcode.cn/problems/zui-xiao-tiao-yue-ci-shu/submissions/) | [题解](https://leetcode.cn/problems/zui-xiao-tiao-yue-ci-shu/solution/)


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