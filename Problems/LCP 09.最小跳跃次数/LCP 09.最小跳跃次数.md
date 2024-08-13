---
tags:
  - leetcode/problem
questionId: LCP 09
title: 最小跳跃次数
translatedTitle: 最小跳跃次数
titleSlug: zui-xiao-tiao-yue-ci-shu
aliases:
  - 最小跳跃次数
  - zui-xiao-tiao-yue-ci-shu
  - 最小跳跃次数
lcLinks:
  - https://leetcode.cn/problems/zui-xiao-tiao-yue-ci-shu/
lcTopics:
  - '[[breadth-first-search]]'
  - '[[segment-tree]]'
  - '[[array]]'
  - '[[dynamic-programming]]'
lcDifficulty: Hard
lcAcRate: 32.1%
similarQuestions: []
grade: ⭐⭐⭐⭐⭐
likes: 97
dislikes: 0
favorites: []
solutions: []
notes: []
---

**Nav:** << previous: [[LCP 08.剧情触发时间]] | next: [[LCP 10.二叉树任务调度]] >>

---

## Description

~~~tabs
tab: English

No description

---

[submissions](https://leetcode.com/problems/zui-xiao-tiao-yue-ci-shu/submissions/) | [solutions](https://leetcode.com/problems/zui-xiao-tiao-yue-ci-shu/solutions/)


tab: 中文

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


~~~

## Code Snippets

~~~tabs
tab: C++

```cpp
class Solution {
public:
    int minJump(vector<int>& jump) {

    }
};
```

tab: Java

```java
class Solution {
    public int minJump(int[] jump) {

    }
}
```

tab: Python

```python
class Solution(object):
    def minJump(self, jump):
        """
        :type jump: List[int]
        :rtype: int
        """
```

tab: Python3

```python
class Solution:
    def minJump(self, jump: List[int]) -> int:
```

tab: C

```c


int minJump(int* jump, int jumpSize){

}

```

tab: C#

```csharp
public class Solution {
    public int MinJump(int[] jump) {

    }
}
```

tab: JavaScript

```javascript
/**
 * @param {number[]} jump
 * @return {number}
 */
var minJump = function(jump) {

};
```

tab: TypeScript

```typescript
function minJump(jump: number[]): number {

};
```

tab: PHP

```php
class Solution {

    /**
     * @param Integer[] $jump
     * @return Integer
     */
    function minJump($jump) {

    }
}
```

tab: Swift

```swift
class Solution {
    func minJump(_ jump: [Int]) -> Int {

    }
}
```

tab: Kotlin

```kotlin
class Solution {
    fun minJump(jump: IntArray): Int {

    }
}
```

tab: Dart

```dart
class Solution {
  int minJump(List<int> jump) {

  }
}
```

tab: Go

```go
func minJump(jump []int) int {

}
```

tab: Ruby

```ruby
# @param {Integer[]} jump
# @return {Integer}
def min_jump(jump)

end
```

tab: Scala

```scala
object Solution {
    def minJump(jump: Array[Int]): Int = {

    }
}
```

tab: Rust

```rust
impl Solution {
    pub fn min_jump(jump: Vec<i32>) -> i32 {

    }
}
```

tab: Racket

```racket
(define/contract (min-jump jump)
  (-> (listof exact-integer?) exact-integer?)

  )
```

tab: Erlang

```erlang
-spec min_jump(Jump :: [integer()]) -> integer().
min_jump(Jump) ->
  .
```

tab: Elixir

```elixir
defmodule Solution do
  @spec min_jump(jump :: [integer]) :: integer
  def min_jump(jump) do

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
          
