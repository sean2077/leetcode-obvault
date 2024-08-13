---
tags:
  - leetcode/problem
questionId: LCP 22
title: 黑白方格画
translatedTitle: 黑白方格画
titleSlug: ccw6C7
aliases:
  - 黑白方格画
  - ccw6C7
  - 黑白方格画
lcLinks:
  - https://leetcode.cn/problems/ccw6C7/
lcTopics:
  - '[[math]]'
lcDifficulty: Easy
lcAcRate: 35.4%
similarQuestions: []
grade: ⭐⭐⭐⭐⭐
likes: 74
dislikes: 0
favorites: []
solutions: []
notes: []
---

**Nav:** << previous: [[LCP 21.追逐游戏]] | next: [[LCP 23.魔术排列]] >>

---

## Description

~~~tabs
tab: English

No description

---

[submissions](https://leetcode.com/problems/ccw6C7/submissions/) | [solutions](https://leetcode.com/problems/ccw6C7/solutions/)


tab: 中文

小扣注意到秋日市集上有一个创作黑白方格画的摊位。摊主给每个顾客提供一个固定在墙上的白色画板，画板不能转动。画板上有 `n * n` 的网格。绘画规则为，小扣可以选择任意多行以及任意多列的格子涂成黑色（选择的整行、整列均需涂成黑色），所选行数、列数均可为 0。

小扣希望最终的成品上需要有 `k` 个黑色格子，请返回小扣共有多少种涂色方案。

注意：两个方案中任意一个相同位置的格子颜色不同，就视为不同的方案。

**示例 1：**
>输入：`n = 2, k = 2`
>
>输出：`4`
> 
>解释：一共有四种不同的方案：
>第一种方案：涂第一列；
>第二种方案：涂第二列；
>第三种方案：涂第一行；
>第四种方案：涂第二行。

**示例 2：**
>输入：`n = 2, k = 1`
> 
>输出：`0`
> 
>解释：不可行，因为第一次涂色至少会涂两个黑格。

**示例 3：**
>输入：`n = 2, k = 4`
> 
>输出：`1`
>
>解释：共有 2*2=4 个格子，仅有一种涂色方案。

**限制：**
- `1 <= n <= 6`
- `0 <= k <= n * n`




---

[提交记录](https://leetcode.cn/problems/ccw6C7/submissions/) | [题解](https://leetcode.cn/problems/ccw6C7/solution/)


~~~

## Code Snippets

~~~tabs
tab: C++

```cpp
class Solution {
public:
    int paintingPlan(int n, int k) {

    }
};
```

tab: Java

```java
class Solution {
    public int paintingPlan(int n, int k) {

    }
}
```

tab: Python

```python
class Solution(object):
    def paintingPlan(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
```

tab: Python3

```python
class Solution:
    def paintingPlan(self, n: int, k: int) -> int:
```

tab: C

```c


int paintingPlan(int n, int k){

}
```

tab: C#

```csharp
public class Solution {
    public int PaintingPlan(int n, int k) {

    }
}
```

tab: JavaScript

```javascript
/**
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var paintingPlan = function(n, k) {

};
```

tab: TypeScript

```typescript
function paintingPlan(n: number, k: number): number {

};
```

tab: PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $k
     * @return Integer
     */
    function paintingPlan($n, $k) {

    }
}
```

tab: Swift

```swift
class Solution {
    func paintingPlan(_ n: Int, _ k: Int) -> Int {

    }
}
```

tab: Kotlin

```kotlin
class Solution {
    fun paintingPlan(n: Int, k: Int): Int {

    }
}
```

tab: Dart

```dart
class Solution {
  int paintingPlan(int n, int k) {

  }
}
```

tab: Go

```go
func paintingPlan(n int, k int) int {

}
```

tab: Ruby

```ruby
# @param {Integer} n
# @param {Integer} k
# @return {Integer}
def painting_plan(n, k)

end
```

tab: Scala

```scala
object Solution {
    def paintingPlan(n: Int, k: Int): Int = {

    }
}
```

tab: Rust

```rust
impl Solution {
    pub fn painting_plan(n: i32, k: i32) -> i32 {

    }
}
```

tab: Racket

```racket
(define/contract (painting-plan n k)
  (-> exact-integer? exact-integer? exact-integer?)

  )
```

tab: Erlang

```erlang
-spec painting_plan(N :: integer(), K :: integer()) -> integer().
painting_plan(N, K) ->
  .
```

tab: Elixir

```elixir
defmodule Solution do
  @spec painting_plan(n :: integer, k :: integer) :: integer
  def painting_plan(n, k) do

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
          
