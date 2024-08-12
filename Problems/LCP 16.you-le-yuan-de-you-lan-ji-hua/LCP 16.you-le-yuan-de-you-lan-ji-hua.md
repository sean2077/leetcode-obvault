---
tags:
  - leetcode/problem
questionId: LCP 16
title: 游乐园的游览计划
translatedTitle: 游乐园的游览计划
titleSlug: you-le-yuan-de-you-lan-ji-hua
aliases:
  - 游乐园的游览计划
  - you-le-yuan-de-you-lan-ji-hua
  - 游乐园的游览计划
lcLink: https://leetcode.com/problems/you-le-yuan-de-you-lan-ji-hua/
lcTopics:
  - '[[graph]]'
  - '[[geometry]]'
  - '[[math]]'
lcDifficulty: Hard
lcAcRate: 36.1%
similarQuestions: []
grade: ⭐⭐⭐⭐⭐
likes: 30
dislikes: 0
favorites: []
solutions: []
notes: []
cssclasses: []
created: 2024-08-13 00:10
updated:
---

**Nav:** << previous: [[LCP 15.you-le-yuan-de-mi-gong]] | next: [[LCP 17.nGK0Fy]] >>

---

## Description

~~~tabs
tab: English

No description

---

[submissions](https://leetcode.com/problems/you-le-yuan-de-you-lan-ji-hua/submissions/) | [solutions](https://leetcode.com/problems/you-le-yuan-de-you-lan-ji-hua/solutions/)


tab: 中文

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


~~~

## Code Snippets

~~~tabs
tab: C++

```cpp
class Solution {
public:
    int maxWeight(vector<vector<int>>& edges, vector<int>& value) {

    }
};
```

tab: Java

```java
class Solution {
    public int maxWeight(int[][] edges, int[] value) {

    }
}
```

tab: Python

```python
class Solution(object):
    def maxWeight(self, edges, value):
        """
        :type edges: List[List[int]]
        :type value: List[int]
        :rtype: int
        """
```

tab: Python3

```python
class Solution:
    def maxWeight(self, edges: List[List[int]], value: List[int]) -> int:
```

tab: C

```c


int maxWeight(int** edges, int edgesSize, int* edgesColSize, int* value, int valueSize){

}

```

tab: C#

```csharp
public class Solution {
    public int MaxWeight(int[][] edges, int[] value) {

    }
}
```

tab: JavaScript

```javascript
/**
 * @param {number[][]} edges
 * @param {number[]} value
 * @return {number}
 */
var maxWeight = function(edges, value) {

};
```

tab: TypeScript

```typescript
function maxWeight(edges: number[][], value: number[]): number {

};
```

tab: PHP

```php
class Solution {

    /**
     * @param Integer[][] $edges
     * @param Integer[] $value
     * @return Integer
     */
    function maxWeight($edges, $value) {

    }
}
```

tab: Swift

```swift
class Solution {
    func maxWeight(_ edges: [[Int]], _ value: [Int]) -> Int {

    }
}
```

tab: Kotlin

```kotlin
class Solution {
    fun maxWeight(edges: Array<IntArray>, value: IntArray): Int {

    }
}
```

tab: Dart

```dart
class Solution {
  int maxWeight(List<List<int>> edges, List<int> value) {

  }
}
```

tab: Go

```go
func maxWeight(edges [][]int, value []int) int {

}
```

tab: Ruby

```ruby
# @param {Integer[][]} edges
# @param {Integer[]} value
# @return {Integer}
def max_weight(edges, value)

end
```

tab: Scala

```scala
object Solution {
    def maxWeight(edges: Array[Array[Int]], value: Array[Int]): Int = {

    }
}
```

tab: Rust

```rust
impl Solution {
    pub fn max_weight(edges: Vec<Vec<i32>>, value: Vec<i32>) -> i32 {

    }
}
```

tab: Racket

```racket
(define/contract (max-weight edges value)
  (-> (listof (listof exact-integer?)) (listof exact-integer?) exact-integer?)

  )
```

tab: Erlang

```erlang
-spec max_weight(Edges :: [[integer()]], Value :: [integer()]) -> integer().
max_weight(Edges, Value) ->
  .
```

tab: Elixir

```elixir
defmodule Solution do
  @spec max_weight(edges :: [[integer]], value :: [integer]) :: integer
  def max_weight(edges, value) do

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
          
