---
tags:
  - leetcode/problem
questionId: LCP 06
title: 拿硬币
translatedTitle: 拿硬币
titleSlug: na-ying-bi
aliases:
  - 拿硬币
  - na-ying-bi
  - 拿硬币
lcLink: https://leetcode.com/problems/na-ying-bi/
lcTopics:
  - '[[array]]'
  - '[[math]]'
lcDifficulty: Easy
lcAcRate: 84.9%
similarQuestions: []
grade: ⭐⭐⭐⭐⭐
likes: 127
dislikes: 0
favorites: []
solutions: []
notes: []
cssclasses: []
created: 2024-08-13 00:10
updated:
---

**Nav:** << previous: [[LCP 05.coin-bonus]] | next: [[LCP 07.chuan-di-xin-xi]] >>

---

## Description

~~~tabs
tab: English

No description

---

[submissions](https://leetcode.com/problems/na-ying-bi/submissions/) | [solutions](https://leetcode.com/problems/na-ying-bi/solutions/)


tab: 中文

<p>桌上有 <code>n</code> 堆力扣币，每堆的数量保存在数组 <code>coins</code> 中。我们每次可以选择任意一堆，拿走其中的一枚或者两枚，求拿完所有力扣币的最少次数。</p>

<p><strong>示例 1：</strong></p>

<blockquote>
<p>输入：<code>[4,2,1]</code></p>

<p>输出：<code>4</code></p>

<p>解释：第一堆力扣币最少需要拿 2 次，第二堆最少需要拿 1 次，第三堆最少需要拿 1 次，总共 4 次即可拿完。</p>
</blockquote>

<p><strong>示例 2：</strong></p>

<blockquote>
<p>输入：<code>[2,3,10]</code></p>

<p>输出：<code>8</code></p>
</blockquote>

<p><strong>限制：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 4</code></li>
	<li><code>1 &lt;= coins[i] &lt;= 10</code></li>
</ul>


---

[提交记录](https://leetcode.cn/problems/na-ying-bi/submissions/) | [题解](https://leetcode.cn/problems/na-ying-bi/solution/)


~~~

## Code Snippets

~~~tabs
tab: C++

```cpp
class Solution {
public:
    int minCount(vector<int>& coins) {

    }
};
```

tab: Java

```java
class Solution {
    public int minCount(int[] coins) {

    }
}
```

tab: Python

```python
class Solution(object):
    def minCount(self, coins):
        """
        :type coins: List[int]
        :rtype: int
        """
```

tab: Python3

```python
class Solution:
    def minCount(self, coins: List[int]) -> int:
```

tab: C

```c


int minCount(int* coins, int coinsSize){

}

```

tab: C#

```csharp
public class Solution {
    public int MinCount(int[] coins) {

    }
}
```

tab: JavaScript

```javascript
/**
 * @param {number[]} coins
 * @return {number}
 */
var minCount = function(coins) {

};
```

tab: TypeScript

```typescript
function minCount(coins: number[]): number {

};
```

tab: PHP

```php
class Solution {

    /**
     * @param Integer[] $coins
     * @return Integer
     */
    function minCount($coins) {

    }
}
```

tab: Swift

```swift
class Solution {
    func minCount(_ coins: [Int]) -> Int {

    }
}
```

tab: Kotlin

```kotlin
class Solution {
    fun minCount(coins: IntArray): Int {

    }
}
```

tab: Dart

```dart
class Solution {
  int minCount(List<int> coins) {

  }
}
```

tab: Go

```go
func minCount(coins []int) int {

}
```

tab: Ruby

```ruby
# @param {Integer[]} coins
# @return {Integer}
def min_count(coins)

end
```

tab: Scala

```scala
object Solution {
    def minCount(coins: Array[Int]): Int = {

    }
}
```

tab: Rust

```rust
impl Solution {
    pub fn min_count(coins: Vec<i32>) -> i32 {

    }
}
```

tab: Racket

```racket
(define/contract (min-count coins)
  (-> (listof exact-integer?) exact-integer?)

  )
```

tab: Erlang

```erlang
-spec min_count(Coins :: [integer()]) -> integer().
min_count(Coins) ->
  .
```

tab: Elixir

```elixir
defmodule Solution do
  @spec min_count(coins :: [integer]) :: integer
  def min_count(coins) do

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
          
