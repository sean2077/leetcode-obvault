---
tags:
  - leetcode/problem
questionId: LCP 07
title: 传递信息
translatedTitle: 传递信息
titleSlug: chuan-di-xin-xi
aliases:
  - 传递信息
  - chuan-di-xin-xi
  - 传递信息
lcLink: https://leetcode.com/problems/chuan-di-xin-xi/
lcTopics:
  - '[[depth-first-search]]'
  - '[[breadth-first-search]]'
  - '[[graph]]'
  - '[[dynamic-programming]]'
lcDifficulty: Easy
lcAcRate: 75.2%
similarQuestions: []
grade: ⭐⭐⭐⭐⭐
likes: 284
dislikes: 0
favorites: []
solutions: []
notes: []
cssclasses: []
created: 2024-08-13 00:10
updated:
---

**Nav:** << previous: [[LCP 06.na-ying-bi]] | next: [[LCP 08.ju-qing-hong-fa-shi-jian]] >>

---

## Description

~~~tabs
tab: English

No description

---

[submissions](https://leetcode.com/problems/chuan-di-xin-xi/submissions/) | [solutions](https://leetcode.com/problems/chuan-di-xin-xi/solutions/)


tab: 中文

<p>小朋友 A 在和 ta 的小伙伴们玩传信息游戏，游戏规则如下：</p>

<ol>
	<li>有 n 名玩家，所有玩家编号分别为 0 ～ n-1，其中小朋友 A 的编号为 0</li>
	<li>每个玩家都有固定的若干个可传信息的其他玩家（也可能没有）。传信息的关系是单向的（比如 A 可以向 B 传信息，但 B 不能向 A 传信息）。</li>
	<li>每轮信息必须需要传递给另一个人，且信息可重复经过同一个人</li>
</ol>

<p>给定总玩家数 <code>n</code>，以及按 <code>[玩家编号,对应可传递玩家编号]</code> 关系组成的二维数组 <code>relation</code>。返回信息从小 A (编号 0 ) 经过 <code>k</code> 轮传递到编号为 n-1 的小伙伴处的方案数；若不能到达，返回 0。</p>

<p><strong>示例 1：</strong></p>

<blockquote>
<p>输入：<code>n = 5, relation = [[0,2],[2,1],[3,4],[2,3],[1,4],[2,0],[0,4]], k = 3</code></p>

<p>输出：<code>3</code></p>

<p>解释：信息从小 A 编号 0 处开始，经 3 轮传递，到达编号 4。共有 3 种方案，分别是 0-&gt;2-&gt;0-&gt;4， 0-&gt;2-&gt;1-&gt;4， 0-&gt;2-&gt;3-&gt;4。</p>
</blockquote>

<p><strong>示例 2：</strong></p>

<blockquote>
<p>输入：<code>n = 3, relation = [[0,2],[2,1]], k = 2</code></p>

<p>输出：<code>0</code></p>

<p>解释：信息不能从小 A 处经过 2 轮传递到编号 2</p>
</blockquote>

<p><strong>限制：</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 10</code></li>
	<li><code>1 &lt;= k &lt;= 5</code></li>
	<li><code>1 &lt;= relation.length &lt;= 90, 且 relation[i].length == 2</code></li>
	<li><code>0 &lt;= relation[i][0],relation[i][1] &lt; n 且 relation[i][0] != relation[i][1]</code></li>
</ul>


---

[提交记录](https://leetcode.cn/problems/chuan-di-xin-xi/submissions/) | [题解](https://leetcode.cn/problems/chuan-di-xin-xi/solution/)


~~~

## Code Snippets

~~~tabs
tab: C++

```cpp
class Solution {
public:
    int numWays(int n, vector<vector<int>>& relation, int k) {

    }
};
```

tab: Java

```java
class Solution {
    public int numWays(int n, int[][] relation, int k) {

    }
}
```

tab: Python

```python
class Solution(object):
    def numWays(self, n, relation, k):
        """
        :type n: int
        :type relation: List[List[int]]
        :type k: int
        :rtype: int
        """
```

tab: Python3

```python
class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
```

tab: C

```c


int numWays(int n, int** relation, int relationSize, int* relationColSize, int k){

}

```

tab: C#

```csharp
public class Solution {
    public int NumWays(int n, int[][] relation, int k) {

    }
}
```

tab: JavaScript

```javascript
/**
 * @param {number} n
 * @param {number[][]} relation
 * @param {number} k
 * @return {number}
 */
var numWays = function(n, relation, k) {

};
```

tab: TypeScript

```typescript
function numWays(n: number, relation: number[][], k: number): number {

};
```

tab: PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $relation
     * @param Integer $k
     * @return Integer
     */
    function numWays($n, $relation, $k) {

    }
}
```

tab: Swift

```swift
class Solution {
    func numWays(_ n: Int, _ relation: [[Int]], _ k: Int) -> Int {

    }
}
```

tab: Kotlin

```kotlin
class Solution {
    fun numWays(n: Int, relation: Array<IntArray>, k: Int): Int {

    }
}
```

tab: Dart

```dart
class Solution {
  int numWays(int n, List<List<int>> relation, int k) {

  }
}
```

tab: Go

```go
func numWays(n int, relation [][]int, k int) int {

}
```

tab: Ruby

```ruby
# @param {Integer} n
# @param {Integer[][]} relation
# @param {Integer} k
# @return {Integer}
def num_ways(n, relation, k)

end
```

tab: Scala

```scala
object Solution {
    def numWays(n: Int, relation: Array[Array[Int]], k: Int): Int = {

    }
}
```

tab: Rust

```rust
impl Solution {
    pub fn num_ways(n: i32, relation: Vec<Vec<i32>>, k: i32) -> i32 {

    }
}
```

tab: Racket

```racket
(define/contract (num-ways n relation k)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer? exact-integer?)

  )
```

tab: Erlang

```erlang
-spec num_ways(N :: integer(), Relation :: [[integer()]], K :: integer()) -> integer().
num_ways(N, Relation, K) ->
  .
```

tab: Elixir

```elixir
defmodule Solution do
  @spec num_ways(n :: integer, relation :: [[integer]], k :: integer) :: integer
  def num_ways(n, relation, k) do

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
          
