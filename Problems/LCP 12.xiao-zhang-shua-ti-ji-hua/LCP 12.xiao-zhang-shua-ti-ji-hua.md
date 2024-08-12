---
tags:
  - leetcode/problem
questionId: LCP 12
title: 小张刷题计划
translatedTitle: 小张刷题计划
titleSlug: xiao-zhang-shua-ti-ji-hua
aliases:
  - 小张刷题计划
  - xiao-zhang-shua-ti-ji-hua
  - 小张刷题计划
lcLink: https://leetcode.com/problems/xiao-zhang-shua-ti-ji-hua/
lcTopics:
  - '[[array]]'
  - '[[binary-search]]'
lcDifficulty: Medium
lcAcRate: 44.2%
similarQuestions: []
grade: ⭐⭐⭐⭐⭐
likes: 106
dislikes: 0
favorites: []
solutions: []
notes: []
cssclasses: []
created: 2024-08-13 00:10
updated:
---

**Nav:** << previous: [[LCP 11.qi-wang-ge-shu-tong-ji]] | next: [[LCP 13.xun-bao]] >>

---

## Description

~~~tabs
tab: English

No description

---

[submissions](https://leetcode.com/problems/xiao-zhang-shua-ti-ji-hua/submissions/) | [solutions](https://leetcode.com/problems/xiao-zhang-shua-ti-ji-hua/solutions/)


tab: 中文

<p>为了提高自己的代码能力，小张制定了 <code>LeetCode</code> 刷题计划，他选中了 <code>LeetCode</code> 题库中的 <code>n</code> 道题，编号从 <code>0</code> 到 <code>n-1</code>，并计划在 <code>m</code> 天内<strong>按照题目编号顺序</strong>刷完所有的题目（注意，小张不能用多天完成同一题）。</p>

<p>在小张刷题计划中，小张需要用 <code>time[i]</code> 的时间完成编号 <code>i</code> 的题目。此外，小张还可以使用场外求助功能，通过询问他的好朋友小杨题目的解法，可以省去该题的做题时间。为了防止&ldquo;小张刷题计划&rdquo;变成&ldquo;小杨刷题计划&rdquo;，小张每天最多使用一次求助。</p>

<p>我们定义 <code>m</code> 天中做题时间最多的一天耗时为 <code>T</code>（小杨完成的题目不计入做题总时间）。请你帮小张求出最小的 <code>T</code>是多少。</p>

<p><strong>示例 1：</strong></p>

<blockquote>
<p>输入：<code>time = [1,2,3,3], m = 2</code></p>

<p>输出：<code>3</code></p>

<p>解释：第一天小张完成前三题，其中第三题找小杨帮忙；第二天完成第四题，并且找小杨帮忙。这样做题时间最多的一天花费了 3 的时间，并且这个值是最小的。</p>
</blockquote>

<p><strong>示例 2：</strong></p>

<blockquote>
<p>输入：<code>time = [999,999,999], m = 4</code></p>

<p>输出：<code>0</code></p>

<p>解释：在前三天中，小张每天求助小杨一次，这样他可以在三天内完成所有的题目并不花任何时间。</p>
</blockquote>

<p>&nbsp;</p>

<p><strong>限制：</strong></p>

<ul>
	<li><code>1 &lt;= time.length &lt;= 10^5</code></li>
	<li><code>1 &lt;= time[i] &lt;= 10000</code></li>
	<li><code>1 &lt;= m &lt;= 1000</code></li>
</ul>


---

[提交记录](https://leetcode.cn/problems/xiao-zhang-shua-ti-ji-hua/submissions/) | [题解](https://leetcode.cn/problems/xiao-zhang-shua-ti-ji-hua/solution/)


~~~

## Code Snippets

~~~tabs
tab: C++

```cpp
class Solution {
public:
    int minTime(vector<int>& time, int m) {

    }
};
```

tab: Java

```java
class Solution {
    public int minTime(int[] time, int m) {

    }
}
```

tab: Python

```python
class Solution(object):
    def minTime(self, time, m):
        """
        :type time: List[int]
        :type m: int
        :rtype: int
        """
```

tab: Python3

```python
class Solution:
    def minTime(self, time: List[int], m: int) -> int:
```

tab: C

```c


int minTime(int* time, int timeSize, int m){

}
```

tab: C#

```csharp
public class Solution {
    public int MinTime(int[] time, int m) {

    }
}
```

tab: JavaScript

```javascript
/**
 * @param {number[]} time
 * @param {number} m
 * @return {number}
 */
var minTime = function(time, m) {

};
```

tab: TypeScript

```typescript
function minTime(time: number[], m: number): number {

};
```

tab: PHP

```php
class Solution {

    /**
     * @param Integer[] $time
     * @param Integer $m
     * @return Integer
     */
    function minTime($time, $m) {

    }
}
```

tab: Swift

```swift
class Solution {
    func minTime(_ time: [Int], _ m: Int) -> Int {

    }
}
```

tab: Kotlin

```kotlin
class Solution {
    fun minTime(time: IntArray, m: Int): Int {

    }
}
```

tab: Dart

```dart
class Solution {
  int minTime(List<int> time, int m) {

  }
}
```

tab: Go

```go
func minTime(time []int, m int) int {

}
```

tab: Ruby

```ruby
# @param {Integer[]} time
# @param {Integer} m
# @return {Integer}
def min_time(time, m)

end
```

tab: Scala

```scala
object Solution {
    def minTime(time: Array[Int], m: Int): Int = {

    }
}
```

tab: Rust

```rust
impl Solution {
    pub fn min_time(time: Vec<i32>, m: i32) -> i32 {

    }
}
```

tab: Racket

```racket
(define/contract (min-time time m)
  (-> (listof exact-integer?) exact-integer? exact-integer?)

  )
```

tab: Erlang

```erlang
-spec min_time(Time :: [integer()], M :: integer()) -> integer().
min_time(Time, M) ->
  .
```

tab: Elixir

```elixir
defmodule Solution do
  @spec min_time(time :: [integer], m :: integer) :: integer
  def min_time(time, m) do

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
          
