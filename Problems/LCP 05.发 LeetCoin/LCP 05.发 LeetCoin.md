---
tags:
  - leetcode/problem
questionId: LCP 05
title: Coin Bonus
translatedTitle: 发 LeetCoin
titleSlug: coin-bonus
aliases:
  - Coin Bonus
  - coin-bonus
  - 发 LeetCoin
lcLinks:
  - https://leetcode.cn/problems/coin-bonus/
lcTopics:
  - '[[binary-indexed-tree]]'
  - '[[segment-tree]]'
  - '[[array]]'
lcDifficulty: Hard
lcAcRate: 22.9%
similarQuestions: []
grade: ⭐⭐⭐⭐⭐
likes: 68
dislikes: 0
favorites: []
solutions: []
notes: []
---

**Nav:** << previous: [[LCP 04.覆盖]] | next: [[LCP 06.拿硬币]] >>

---

## Description

~~~tabs
tab: English

No description

---

[submissions](https://leetcode.com/problems/coin-bonus/submissions/) | [solutions](https://leetcode.com/problems/coin-bonus/solutions/)


tab: 中文

<p>力扣决定给一个刷题团队发<code>LeetCoin</code>作为奖励。同时，为了监控给大家发了多少<code>LeetCoin</code>，力扣有时候也会进行查询。</p>

<p>&nbsp;</p>

<p>该刷题团队的管理模式可以用一棵树表示：</p>

<ol>
	<li>团队只有一个负责人，编号为1。除了该负责人外，每个人有且仅有一个领导（负责人没有领导）；</li>
	<li>不存在循环管理的情况，如A管理B，B管理C，C管理A。</li>
</ol>

<p>&nbsp;</p>

<p>力扣想进行的操作有以下三种：</p>

<ol>
	<li>给团队的一个成员（也可以是负责人）发一定数量的<code>LeetCoin</code>；</li>
	<li>给团队的一个成员（也可以是负责人），以及他/她管理的所有人（即他/她的下属、他/她下属的下属，&hellip;&hellip;），发一定数量的<code>LeetCoin</code>；</li>
	<li>查询某一个成员（也可以是负责人），以及他/她管理的所有人被发到的<code>LeetCoin</code>之和。</li>
</ol>

<p>&nbsp;</p>

<p><strong>输入：</strong></p>

<ol>
	<li><code>N</code>表示团队成员的个数（编号为1～N，负责人为1）；</li>
	<li><code>leadership</code>是大小为<code>(N&nbsp;- 1) * 2</code>的二维数组，其中每个元素<code>[a, b]</code>代表<code>b</code>是<code>a</code>的下属；</li>
	<li><code>operations</code>是一个长度为<code>Q</code>的二维数组，代表以时间排序的操作，格式如下：
	<ol>
		<li><code>operations[i][0] = 1</code>: 代表第一种操作，<code>operations[i][1]</code>代表成员的编号，<code>operations[i][2]</code>代表<code>LeetCoin</code>的数量；</li>
		<li><code>operations[i][0] = 2</code>: 代表第二种操作，<code>operations[i][1]</code>代表成员的编号，<code>operations[i][2]</code>代表<code>LeetCoin</code>的数量；</li>
		<li><code>operations[i][0] = 3</code>: 代表第三种操作，<code>operations[i][1]</code>代表成员的编号；</li>
	</ol>
	</li>
</ol>

<p><strong>输出：</strong></p>

<p>返回一个数组，数组里是每次<strong>查询</strong>的返回值（发<code>LeetCoin</code>的操作不需要任何返回值）。由于发的<code>LeetCoin</code>很多，请把每次查询的结果模<code>1e9+7 (1000000007)</code>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>N = 6, leadership = [[1, 2], [1, 6], [2, 3], [2, 5], [1, 4]], operations = [[1, 1, 500], [2, 2, 50], [3, 1], [2, 6, 15], [3, 1]]
<strong>输出：</strong>[650, 665]
<strong>解释：</strong>团队的管理关系见下图。
第一次查询时，每个成员得到的LeetCoin的数量分别为（按编号顺序）：500, 50, 50, 0, 50, 0;
第二次查询时，每个成员得到的LeetCoin的数量分别为（按编号顺序）：500, 50, 50, 0, 50, 15.
</pre>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/09/09/coin_example_1.jpg" style="height: 344px; width: 300px;"></p>

<p>&nbsp;</p>

<p><strong>限制：</strong></p>

<ol>
	<li><code>1 &lt;= N &lt;= 50000</code></li>
	<li><code>1 &lt;= Q &lt;= 50000</code></li>
	<li><code>operations[i][0] != 3 时，1 &lt;= operations[i][2]&nbsp;&lt;= 5000</code></li>
</ol>


---

[提交记录](https://leetcode.cn/problems/coin-bonus/submissions/) | [题解](https://leetcode.cn/problems/coin-bonus/solution/)


~~~

## Code Snippets

~~~tabs
tab: C++

```cpp
class Solution {
public:
    vector<int> bonus(int n, vector<vector<int>>& leadership, vector<vector<int>>& operations) {

    }
};
```

tab: Java

```java
class Solution {
    public int[] bonus(int n, int[][] leadership, int[][] operations) {

    }
}
```

tab: Python

```python
class Solution(object):
    def bonus(self, n, leadership, operations):
        """
        :type n: int
        :type leadership: List[List[int]]
        :type operations: List[List[int]]
        :rtype: List[int]
        """
```

tab: Python3

```python
class Solution:
    def bonus(self, n: int, leadership: List[List[int]], operations: List[List[int]]) -> List[int]:
```

tab: C

```c


/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* bonus(int n, int** leadership, int leadershipSize, int* leadershipColSize, int** operations, int operationsSize, int* operationsColSize, int* returnSize){

}

```

tab: JavaScript

```javascript
/**
 * @param {number} n
 * @param {number[][]} leadership
 * @param {number[][]} operations
 * @return {number[]}
 */
var bonus = function(n, leadership, operations) {

};
```

tab: TypeScript

```typescript
function bonus(n: number, leadership: number[][], operations: number[][]): number[] {

};
```

tab: Dart

```dart
class Solution {
  List<int> bonus(int n, List<List<int>> leadership, List<List<int>> operations) {

  }
}
```

tab: Go

```go
func bonus(n int, leadership [][]int, operations [][]int) []int {

}
```

tab: Racket

```racket
(define/contract (bonus n leadership operations)
  (-> exact-integer? (listof (listof exact-integer?)) (listof (listof exact-integer?)) (listof exact-integer?))

  )
```

tab: Erlang

```erlang
-spec bonus(N :: integer(), Leadership :: [[integer()]], Operations :: [[integer()]]) -> [integer()].
bonus(N, Leadership, Operations) ->
  .
```

tab: Elixir

```elixir
defmodule Solution do
  @spec bonus(n :: integer, leadership :: [[integer]], operations :: [[integer]]) :: [integer]
  def bonus(n, leadership, operations) do

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
          
