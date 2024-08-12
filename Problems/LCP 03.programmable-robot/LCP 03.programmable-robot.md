---
tags:
  - leetcode/problem
questionId: LCP 03
title: Programmable Robot
translatedTitle: 机器人大冒险
titleSlug: programmable-robot
aliases:
  - Programmable Robot
  - programmable-robot
  - 机器人大冒险
lcLinks:
  - https://leetcode.cn/problems/programmable-robot/
lcTopics:
  - '[[array]]'
  - '[[hash-table]]'
  - '[[simulation]]'
lcDifficulty: Medium
lcAcRate: 23.6%
similarQuestions: []
grade: ⭐⭐⭐⭐⭐
likes: 143
dislikes: 0
favorites: []
solutions: []
notes: []
cssclasses: []
created: 2024-08-13 00:28
updated:
---

**Nav:** << previous: [[LCP 02.deep-dark-fraction]] | next: [[LCP 04.broken-board-dominoes]] >>

---

## Description

~~~tabs
tab: English

No description

---

[submissions](https://leetcode.com/problems/programmable-robot/submissions/) | [solutions](https://leetcode.com/problems/programmable-robot/solutions/)


tab: 中文

<p>力扣团队买了一个可编程机器人，机器人初始位置在原点<code>(0, 0)</code>。小伙伴事先给机器人输入一串指令<code>command</code>，机器人就会<strong>无限循环</strong>这条指令的步骤进行移动。指令有两种：</p>

<ol>
	<li><code>U</code>: 向<code>y</code>轴正方向移动一格</li>
	<li><code>R</code>: 向<code>x</code>轴正方向移动一格。</li>
</ol>

<p>不幸的是，在 xy 平面上还有一些障碍物，他们的坐标用<code>obstacles</code>表示。机器人一旦碰到障碍物就会被<strong>损毁</strong>。</p>

<p>给定终点坐标<code>(x, y)</code>，返回机器人能否<strong>完好</strong>地到达终点。如果能，返回<code>true</code>；否则返回<code>false</code>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>command = &quot;URR&quot;, obstacles = [], x = 3, y = 2
<strong>输出：</strong>true
<strong>解释：</strong>U(0, 1) -&gt; R(1, 1) -&gt; R(2, 1) -&gt; U(2, 2) -&gt; R(3, 2)。</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>command = &quot;URR&quot;, obstacles = [[2, 2]], x = 3, y = 2
<strong>输出：</strong>false
<strong>解释：</strong>机器人在到达终点前会碰到(2, 2)的障碍物。</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>command = &quot;URR&quot;, obstacles = [[4, 2]], x = 3, y = 2
<strong>输出：</strong>true
<strong>解释：</strong>到达终点后，再碰到障碍物也不影响返回结果。</pre>

<p>&nbsp;</p>

<p><strong>限制：</strong></p>

<ol>
	<li><code>2 &lt;= command的长度 &lt;= 1000</code></li>
	<li><code>command</code>由<code>U，R</code>构成，且至少有一个<code>U</code>，至少有一个<code>R</code></li>
	<li><code>0 &lt;= x &lt;= 1e9, 0 &lt;= y &lt;= 1e9</code></li>
	<li><code>0 &lt;= obstacles的长度 &lt;= 1000</code></li>
	<li><code>obstacles[i]</code>不为原点或者终点</li>
</ol>


---

[提交记录](https://leetcode.cn/problems/programmable-robot/submissions/) | [题解](https://leetcode.cn/problems/programmable-robot/solution/)


~~~

## Code Snippets

~~~tabs
tab: C++

```cpp
class Solution {
public:
    bool robot(string command, vector<vector<int>>& obstacles, int x, int y) {

    }
};
```

tab: Java

```java
class Solution {
    public boolean robot(String command, int[][] obstacles, int x, int y) {

    }
}
```

tab: Python

```python
class Solution(object):
    def robot(self, command, obstacles, x, y):
        """
        :type command: str
        :type obstacles: List[List[int]]
        :type x: int
        :type y: int
        :rtype: bool
        """
```

tab: Python3

```python
class Solution:
    def robot(self, command: str, obstacles: List[List[int]], x: int, y: int) -> bool:
```

tab: C

```c


bool robot(char * command, int** obstacles, int obstaclesSize, int* obstaclesColSize, int x, int y){

}

```

tab: JavaScript

```javascript
/**
 * @param {string} command
 * @param {number[][]} obstacles
 * @param {number} x
 * @param {number} y
 * @return {boolean}
 */
var robot = function(command, obstacles, x, y) {

};
```

tab: TypeScript

```typescript
function robot(command: string, obstacles: number[][], x: number, y: number): boolean {

};
```

tab: Dart

```dart
class Solution {
  bool robot(String command, List<List<int>> obstacles, int x, int y) {

  }
}
```

tab: Go

```go
func robot(command string, obstacles [][]int, x int, y int) bool {

}
```

tab: Racket

```racket
(define/contract (robot command obstacles x y)
  (-> string? (listof (listof exact-integer?)) exact-integer? exact-integer? boolean?)

  )
```

tab: Erlang

```erlang
-spec robot(Command :: unicode:unicode_binary(), Obstacles :: [[integer()]], X :: integer(), Y :: integer()) -> boolean().
robot(Command, Obstacles, X, Y) ->
  .
```

tab: Elixir

```elixir
defmodule Solution do
  @spec robot(command :: String.t, obstacles :: [[integer]], x :: integer, y :: integer) :: boolean
  def robot(command, obstacles, x, y) do

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
          
