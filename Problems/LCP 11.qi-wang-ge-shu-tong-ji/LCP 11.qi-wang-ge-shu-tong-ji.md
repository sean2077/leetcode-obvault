---
tags:
  - leetcode/problem
questionId: LCP 11
title: 期望个数统计
translatedTitle: 期望个数统计
titleSlug: qi-wang-ge-shu-tong-ji
aliases:
  - 期望个数统计
  - qi-wang-ge-shu-tong-ji
  - 期望个数统计
lcLink: https://leetcode.com/problems/qi-wang-ge-shu-tong-ji/
lcTopics:
  - '[[array]]'
  - '[[hash-table]]'
  - '[[math]]'
  - '[[probability-and-statistics]]'
lcDifficulty: Easy
lcAcRate: 72.8%
similarQuestions: []
grade: ⭐⭐⭐⭐⭐
likes: 40
dislikes: 0
favorites: []
solutions: []
notes: []
cssclasses: []
created: 2024-08-13 00:10
updated:
---

**Nav:** << previous: [[LCP 10.er-cha-shu-ren-wu-diao-du]] | next: [[LCP 12.xiao-zhang-shua-ti-ji-hua]] >>

---

## Description

~~~tabs
tab: English

No description

---

[submissions](https://leetcode.com/problems/qi-wang-ge-shu-tong-ji/submissions/) | [solutions](https://leetcode.com/problems/qi-wang-ge-shu-tong-ji/solutions/)


tab: 中文

<p>某互联网公司一年一度的春招开始了，一共有 <code>n</code> 名面试者入选。每名面试者都会提交一份简历，公司会根据提供的简历资料产生一个预估的能力值，数值越大代表越有可能通过面试。</p>

<p>小 A 和小 B 负责审核面试者，他们均有所有面试者的简历，并且将各自根据面试者能力值从大到小的顺序浏览。由于简历事先被打乱过，能力值相同的简历的出现顺序是从它们的全排列中<strong>等可能</strong>地取一个。现在给定 <code>n</code> 名面试者的能力值 <code>scores</code>，设 <code>X</code> 代表小 A 和小 B 的浏览顺序中出现在同一位置的简历数，求 <code>X</code> 的期望。</p>

<p>提示：离散的非负随机变量的期望计算公式为 <img alt="1" src="https://pic.leetcode.cn/1694957445-AweiqF-svg.svg" style="width: 190px; height: 49px;" />。在本题中，由于 <code>X</code> 的取值为 0 到 <code>n</code> 之间，期望计算公式可以是 <img alt="2" src="https://pic.leetcode.cn/1694957449-DuBtfQ-svg1.svg" style="width: 190px; height: 49px;" />。</p>

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


~~~

## Code Snippets

~~~tabs
tab: C++

```cpp
class Solution {
public:
    int expectNumber(vector<int>& scores) {

    }
};
```

tab: Java

```java
class Solution {
    public int expectNumber(int[] scores) {

    }
}
```

tab: Python

```python
class Solution(object):
    def expectNumber(self, scores):
        """
        :type scores: List[int]
        :rtype: int
        """
```

tab: Python3

```python
class Solution:
    def expectNumber(self, scores: List[int]) -> int:
```

tab: C

```c


int expectNumber(int* scores, int scoresSize){

}
```

tab: C#

```csharp
public class Solution {
    public int ExpectNumber(int[] scores) {

    }
}
```

tab: JavaScript

```javascript
/**
 * @param {number[]} scores
 * @return {number}
 */
var expectNumber = function(scores) {

};
```

tab: TypeScript

```typescript
function expectNumber(scores: number[]): number {

};
```

tab: PHP

```php
class Solution {

    /**
     * @param Integer[] $scores
     * @return Integer
     */
    function expectNumber($scores) {

    }
}
```

tab: Swift

```swift
class Solution {
    func expectNumber(_ scores: [Int]) -> Int {

    }
}
```

tab: Kotlin

```kotlin
class Solution {
    fun expectNumber(scores: IntArray): Int {

    }
}
```

tab: Dart

```dart
class Solution {
  int expectNumber(List<int> scores) {

  }
}
```

tab: Go

```go
func expectNumber(scores []int) int {

}
```

tab: Ruby

```ruby
# @param {Integer[]} scores
# @return {Integer}
def expect_number(scores)

end
```

tab: Scala

```scala
object Solution {
    def expectNumber(scores: Array[Int]): Int = {

    }
}
```

tab: Rust

```rust
impl Solution {
    pub fn expect_number(scores: Vec<i32>) -> i32 {

    }
}
```

tab: Racket

```racket
(define/contract (expect-number scores)
  (-> (listof exact-integer?) exact-integer?)

  )
```

tab: Erlang

```erlang
-spec expect_number(Scores :: [integer()]) -> integer().
expect_number(Scores) ->
  .
```

tab: Elixir

```elixir
defmodule Solution do
  @spec expect_number(scores :: [integer]) :: integer
  def expect_number(scores) do

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
          
