---
tags:
  - leetcode/problem
questionId: LCP 04
title: Broken Board Dominoes
translatedTitle: 覆盖
titleSlug: broken-board-dominoes
aliases:
  - Broken Board Dominoes
  - broken-board-dominoes
  - 覆盖
lcLinks:
  - https://leetcode.cn/problems/broken-board-dominoes/
lcTopics:
  - '[[bit-manipulation]]'
  - '[[graph]]'
  - '[[array]]'
  - '[[dynamic-programming]]'
  - '[[bitmask]]'
lcDifficulty: Hard
lcAcRate: 42.2%
similarQuestions: []
grade: ⭐⭐⭐⭐⭐
likes: 80
dislikes: 0
favorites: []
solutions: []
notes: []
---

**Nav:** << previous: [[LCP 03.机器人大冒险]] | next: [[LCP 05.发 LeetCoin]] >>

---

## Description

~~~tabs
tab: English

No description

---

[submissions](https://leetcode.com/problems/broken-board-dominoes/submissions/) | [solutions](https://leetcode.com/problems/broken-board-dominoes/solutions/)


tab: 中文

<p>你有一块棋盘，棋盘上有一些格子已经坏掉了。你还有无穷块大小为<code>1 * 2</code>的多米诺骨牌，你想把这些骨牌<strong>不重叠</strong>地覆盖在<strong>完好</strong>的格子上，请找出你最多能在棋盘上放多少块骨牌？这些骨牌可以横着或者竖着放。</p>

<p>&nbsp;</p>

<p>输入：<code>n, m</code>代表棋盘的大小；<code>broken</code>是一个<code>b * 2</code>的二维数组，其中每个元素代表棋盘上每一个坏掉的格子的位置。</p>

<p>输出：一个整数，代表最多能在棋盘上放的骨牌数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>n = 2, m = 3, broken = [[1, 0], [1, 1]]
<strong>输出：</strong>2
<strong>解释：</strong>我们最多可以放两块骨牌：[[0, 0], [0, 1]]以及[[0, 2], [1, 2]]。（见下图）</pre>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/09/09/domino_example_1.jpg" style="height: 204px; width: 304px;"></p>

<p>&nbsp;</p>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>n = 3, m = 3, broken = []
<strong>输出：</strong>4
<strong>解释：</strong>下图是其中一种可行的摆放方式
</pre>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/09/09/domino_example_2.jpg" style="height: 304px; width: 304px;"></p>

<p>&nbsp;</p>

<p><strong>限制：</strong></p>

<ol>
	<li><code>1 &lt;= n &lt;= 8</code></li>
	<li><code>1 &lt;= m &lt;= 8</code></li>
	<li><code>0 &lt;= b &lt;= n * m</code></li>
</ol>


---

[提交记录](https://leetcode.cn/problems/broken-board-dominoes/submissions/) | [题解](https://leetcode.cn/problems/broken-board-dominoes/solution/)


~~~

## Code Snippets

~~~tabs
tab: C++

```cpp
class Solution {
public:
    int domino(int n, int m, vector<vector<int>>& broken) {

    }
};
```

tab: Java

```java
class Solution {
    public int domino(int n, int m, int[][] broken) {

    }
}
```

tab: Python

```python
class Solution(object):
    def domino(self, n, m, broken):
        """
        :type n: int
        :type m: int
        :type broken: List[List[int]]
        :rtype: int
        """
```

tab: Python3

```python
class Solution:
    def domino(self, n: int, m: int, broken: List[List[int]]) -> int:
```

tab: C

```c


int domino(int n, int m, int** broken, int brokenSize, int* brokenColSize){

}

```

tab: JavaScript

```javascript
/**
 * @param {number} n
 * @param {number} m
 * @param {number[][]} broken
 * @return {number}
 */
var domino = function(n, m, broken) {

};
```

tab: TypeScript

```typescript
function domino(n: number, m: number, broken: number[][]): number {

};
```

tab: Dart

```dart
class Solution {
  int domino(int n, int m, List<List<int>> broken) {

  }
}
```

tab: Go

```go
func domino(n int, m int, broken [][]int) int {

}
```

tab: Racket

```racket
(define/contract (domino n m broken)
  (-> exact-integer? exact-integer? (listof (listof exact-integer?)) exact-integer?)

  )
```

tab: Erlang

```erlang
-spec domino(N :: integer(), M :: integer(), Broken :: [[integer()]]) -> integer().
domino(N, M, Broken) ->
  .
```

tab: Elixir

```elixir
defmodule Solution do
  @spec domino(n :: integer, m :: integer, broken :: [[integer]]) :: integer
  def domino(n, m, broken) do

  end
end
```

~~~

## Similar Questions

```dataviewjs
const currentFilePath = dv.current().file.path;
dv.table(
    ["题号", "标题", "标题(中)", "分类",  "难度", "通过率", "评分", "解法", "笔记", "收藏"],
    dv.pages("#leetcode/problem")
        .filter(p => p.similarQuestions && p.similarQuestions.some(q => q.path === currentFilePath))
        .map((p) => [p.file.link, p.title, p.translatedTitle, p.lcTopics, p.lcDifficulty, p.lcAcRate, p.grade, p.solutions, p.notes, p.favorites])
);
```

## Solutions

```dataviewjs
const currentDir = dv.current().file.folder;
const solutionPages = dv.pages(`"${currentDir}" and #leetcode/solution`);
dv.table(
    ["解法", "描述", "编程语言", "评分", "相关链接", "最后更新"],
    solutionPages
        .map((p) => [p.file.link, p.desc, p.program_language,p.grade, p.related_links, p.updated])
);
//  更新 solutions 元信息
const currentFile = app.vault.getAbstractFileByPath(dv.current().file.path);
let solutionList = solutionPages.map(p => `[[${p.file.link.path}|${p.file.name}]]`).array();
await app.fileManager.processFrontMatter(currentFile, (fm) => {
  fm["solutions"] = solutionList;
});
```

## Notes

```dataviewjs
const currentFilePath = dv.current().file.path;
let notePages = dv.pages(`#leetcode/note`)
	.filter(p => p.related_questions && p.related_questions.some(q => q.path === currentFilePath));
dv.table(["笔记", "标题", "描述", "评分", "最后更新"],
  notePages.map(p => [p.file.link, p.title, p.desc, p.grade, p.updated])
);
// 更新 notes 元信息
const currentFile = app.vault.getAbstractFileByPath(currentFilePath);
let noteList = notePages.map(p => `[[${p.file.link.path}|${p.file.name}]]`).array();
await app.fileManager.processFrontMatter(currentFile, (fm) => {
  fm["notes"] = noteList;
});
```
          
