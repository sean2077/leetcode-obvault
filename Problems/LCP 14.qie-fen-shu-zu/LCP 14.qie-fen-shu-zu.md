---
tags:
  - leetcode/problem
questionId: LCP 14
title: 切分数组
translatedTitle: 切分数组
titleSlug: qie-fen-shu-zu
aliases:
  - 切分数组
  - qie-fen-shu-zu
  - 切分数组
lcLinks:
  - https://leetcode.cn/problems/qie-fen-shu-zu/
lcTopics:
  - '[[array]]'
  - '[[math]]'
  - '[[dynamic-programming]]'
  - '[[number-theory]]'
lcDifficulty: Hard
lcAcRate: 24.6%
similarQuestions: []
grade: ⭐⭐⭐⭐⭐
likes: 62
dislikes: 0
favorites: []
solutions: []
notes: []
cssclasses: []
created: 2024-08-13 00:28
updated:
---

**Nav:** << previous: [[LCP 13.xun-bao]] | next: [[LCP 15.you-le-yuan-de-mi-gong]] >>

---

## Description

~~~tabs
tab: English

No description

---

[submissions](https://leetcode.com/problems/qie-fen-shu-zu/submissions/) | [solutions](https://leetcode.com/problems/qie-fen-shu-zu/solutions/)


tab: 中文

<p>给定一个整数数组 <code>nums</code> ，小李想将 <code>nums</code> 切割成若干个非空子数组，使得每个子数组最左边的数和最右边的数的最大公约数大于 1 。为了减少他的工作量，请求出最少可以切成多少个子数组。</p>

<p><strong>示例 1：</strong></p>

<blockquote>
<p>输入：<code>nums = [2,3,3,2,3,3]</code></p>

<p>输出：<code>2</code></p>

<p>解释：最优切割为 [2,3,3,2] 和 [3,3] 。第一个子数组头尾数字的最大公约数为 2 ，第二个子数组头尾数字的最大公约数为 3 。</p>
</blockquote>

<p><strong>示例 2：</strong></p>

<blockquote>
<p>输入：<code>nums = [2,3,5,7]</code></p>

<p>输出：<code>4</code></p>

<p>解释：只有一种可行的切割：[2], [3], [5], [7]</p>
</blockquote>

<p><strong>限制：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10^5</code></li>
	<li><code>2 &lt;= nums[i] &lt;= 10^6</code></li>
</ul>


---

[提交记录](https://leetcode.cn/problems/qie-fen-shu-zu/submissions/) | [题解](https://leetcode.cn/problems/qie-fen-shu-zu/solution/)


~~~

## Code Snippets

~~~tabs
tab: C++

```cpp
class Solution {
public:
    int splitArray(vector<int>& nums) {

    }
};
```

tab: Java

```java
class Solution {
    public int splitArray(int[] nums) {

    }
}
```

tab: Python

```python
class Solution(object):
    def splitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
```

tab: Python3

```python
class Solution:
    def splitArray(self, nums: List[int]) -> int:
```

tab: C

```c


int splitArray(int* nums, int numsSize){

}

```

tab: C#

```csharp
public class Solution {
    public int SplitArray(int[] nums) {

    }
}
```

tab: JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var splitArray = function(nums) {

};
```

tab: TypeScript

```typescript
function splitArray(nums: number[]): number {

};
```

tab: PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function splitArray($nums) {

    }
}
```

tab: Swift

```swift
class Solution {
    func splitArray(_ nums: [Int]) -> Int {

    }
}
```

tab: Kotlin

```kotlin
class Solution {
    fun splitArray(nums: IntArray): Int {

    }
}
```

tab: Dart

```dart
class Solution {
  int splitArray(List<int> nums) {

  }
}
```

tab: Go

```go
func splitArray(nums []int) int {

}
```

tab: Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def split_array(nums)

end
```

tab: Scala

```scala
object Solution {
    def splitArray(nums: Array[Int]): Int = {

    }
}
```

tab: Rust

```rust
impl Solution {
    pub fn split_array(nums: Vec<i32>) -> i32 {

    }
}
```

tab: Racket

```racket
(define/contract (split-array nums)
  (-> (listof exact-integer?) exact-integer?)

  )
```

tab: Erlang

```erlang
-spec split_array(Nums :: [integer()]) -> integer().
split_array(Nums) ->
  .
```

tab: Elixir

```elixir
defmodule Solution do
  @spec split_array(nums :: [integer]) :: integer
  def split_array(nums) do

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
          
