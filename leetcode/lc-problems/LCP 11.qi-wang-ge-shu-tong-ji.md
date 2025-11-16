---
tags:
  - leetcode/problem
questionId: "LCP 11"
title: 期望个数统计
translatedTitle: 期望个数统计
titleSlug: qi-wang-ge-shu-tong-ji
aliases:
  - 期望个数统计
  - qi-wang-ge-shu-tong-ji
  - 期望个数统计
lcLinks:
  - https://leetcode.com/problems/qi-wang-ge-shu-tong-ji/
  - https://leetcode.cn/problems/qi-wang-ge-shu-tong-ji/
lcTopics:
lcDifficulty: Easy
lcAcRate: 72.8%
similarQuestions:
grade: ⭐⭐⭐⭐⭐
likes: 41
dislikes: 0
favorites: []
created: 2025-11-16 11:17
updated: 2025-11-16 11:17
---

**Nav:** << previous: [[LCP 10.er-cha-shu-ren-wu-diao-du|LCP 10.二叉树任务调度]] | next: [[LCP 12.xiao-zhang-shua-ti-ji-hua|LCP 12.小张刷题计划]] >>

---

## Description

<p>某互联网公司一年一度的春招开始了，一共有 <code>n</code> 名面试者入选。每名面试者都会提交一份简历，公司会根据提供的简历资料产生一个预估的能力值，数值越大代表越有可能通过面试。</p>

<p>小 A 和小 B 负责审核面试者，他们均有所有面试者的简历，并且将各自根据面试者能力值从大到小的顺序浏览。由于简历事先被打乱过，能力值相同的简历的出现顺序是从它们的全排列中<strong>等可能</strong>地取一个。现在给定 <code>n</code> 名面试者的能力值 <code>scores</code>，设 <code>X</code> 代表小 A 和小 B 的浏览顺序中出现在同一位置的简历数，求 <code>X</code> 的期望。</p>

<p>提示：离散的非负随机变量的期望计算公式为 <img alt="1" src="http://latex.codecogs.com/svg.latex?E%28X%29%3D%5Csum_%7Bk%3D1%7D%5E%7B%5Cinfty%7D%20k%20%5CPr%28X%20%3D%20k%29" />。在本题中，由于 <code>X</code> 的取值为 0 到 <code>n</code> 之间，期望计算公式可以是 <img alt="2" src="http://latex.codecogs.com/svg.latex?E%28X%29%3D%5Csum_%7Bk%3D1%7D%5E%7Bn%7D%20k%20%5CPr%28X%20%3D%20k%29" />。</p>

<p><strong>示例 1：</strong></p>

<blockquote>
<p>输入：<code>scores = [1,2,3]</code></p>

<p>输出：<code>3</code></p>

<p>解释：由于面试者能力值互不相同，小 A 和小 B 的浏览顺序一定是相同的。<code>X</code>的期望是 3 。</p>
</blockquote>

<p><strong>示例 2：</strong></p>

<blockquote>
<p>输入：<code>scores = [1,1]</code></p>

<p>输出：<code>1</code></p>

<p>解释：设两位面试者的编号为 0, 1。由于他们的能力值都是 1，小 A 和小 B 的浏览顺序都为从全排列 <code>[[0,1],[1,0]]</code> 中等可能地取一个。如果小 A 和小 B 的浏览顺序都是 <code>[0,1]</code> 或者 <code>[1,0]</code> ，那么出现在同一位置的简历数为 2 ，否则是 0 。所以 <code>X</code> 的期望是 (2+0+2+0) * 1/4 = 1</p>
</blockquote>

<p><strong>示例 3：</strong></p>

<blockquote>
<p>输入：<code>scores = [1,1,2]</code></p>

<p>输出：<code>2</code></p>
</blockquote>

<p><strong>限制：</strong></p>

<ul>
	<li><code>1 &lt;= scores.length &lt;= 10^5</code></li>
	<li><code>0 &lt;= scores[i] &lt;= 10^6</code></li>
</ul>



---

[提交记录](https://leetcode.cn/problems/qi-wang-ge-shu-tong-ji/submissions/) | [题解](https://leetcode.cn/problems/qi-wang-ge-shu-tong-ji/solution/)


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