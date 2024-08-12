---
tags:
  - leetcode/problem
questionId: LCP 18
title: 早餐组合
translatedTitle: 早餐组合
titleSlug: 2vYnGI
aliases:
  - 早餐组合
  - 2vYnGI
  - 早餐组合
lcLink: https://leetcode.com/problems/2vYnGI/
lcTopics:
  - '[[array]]'
  - '[[two-pointers]]'
  - '[[binary-search]]'
  - '[[sorting]]'
lcDifficulty: Easy
lcAcRate: 30.9%
similarQuestions: []
grade: ⭐⭐⭐⭐⭐
likes: 91
dislikes: 0
favorites: []
solutions: []
notes: []
cssclasses: []
created: 2024-08-13 00:10
updated:
---

**Nav:** << previous: [[LCP 17.nGK0Fy]] | next: [[LCP 19.UlBDOe]] >>

---

## Description

~~~tabs
tab: English

No description

---

[submissions](https://leetcode.com/problems/2vYnGI/submissions/) | [solutions](https://leetcode.com/problems/2vYnGI/solutions/)


tab: 中文

小扣在秋日市集选择了一家早餐摊位，一维整型数组 `staple` 中记录了每种主食的价格，一维整型数组 `drinks` 中记录了每种饮料的价格。小扣的计划选择一份主食和一款饮料，且花费不超过 `x` 元。请返回小扣共有多少种购买方案。

注意：答案需要以 `1e9 + 7 (1000000007)` 为底取模，如：计算初始结果为：`1000000008`，请返回 `1`

**示例 1：**
>输入：`staple = [10,20,5], drinks = [5,5,2], x = 15`
>
>输出：`6`
>
>解释：小扣有 6 种购买方案，所选主食与所选饮料在数组中对应的下标分别是：
>第 1 种方案：staple[0] + drinks[0] = 10 + 5 = 15；
>第 2 种方案：staple[0] + drinks[1] = 10 + 5 = 15；
>第 3 种方案：staple[0] + drinks[2] = 10 + 2 = 12；
>第 4 种方案：staple[2] + drinks[0] = 5 + 5 = 10；
>第 5 种方案：staple[2] + drinks[1] = 5 + 5 = 10；
>第 6 种方案：staple[2] + drinks[2] = 5 + 2 = 7。

**示例 2：**
>输入：`staple = [2,1,1], drinks = [8,9,5,1], x = 9`
>
>输出：`8`
>
>解释：小扣有 8 种购买方案，所选主食与所选饮料在数组中对应的下标分别是：
>第 1 种方案：staple[0] + drinks[2] = 2 + 5 = 7；
>第 2 种方案：staple[0] + drinks[3] = 2 + 1 = 3；
>第 3 种方案：staple[1] + drinks[0] = 1 + 8 = 9；
>第 4 种方案：staple[1] + drinks[2] = 1 + 5 = 6；
>第 5 种方案：staple[1] + drinks[3] = 1 + 1 = 2；
>第 6 种方案：staple[2] + drinks[0] = 1 + 8 = 9；
>第 7 种方案：staple[2] + drinks[2] = 1 + 5 = 6；
>第 8 种方案：staple[2] + drinks[3] = 1 + 1 = 2；

**提示：**
+ `1 <= staple.length <= 10^5`
+ `1 <= drinks.length <= 10^5`
+ `1 <= staple[i],drinks[i] <= 10^5`
+ `1 <= x <= 2*10^5`

---

[提交记录](https://leetcode.cn/problems/2vYnGI/submissions/) | [题解](https://leetcode.cn/problems/2vYnGI/solution/)


~~~

## Code Snippets

~~~tabs
tab: C++

```cpp
class Solution {
public:
    int breakfastNumber(vector<int>& staple, vector<int>& drinks, int x) {

    }
};
```

tab: Java

```java
class Solution {
    public int breakfastNumber(int[] staple, int[] drinks, int x) {

    }
}
```

tab: Python

```python
class Solution(object):
    def breakfastNumber(self, staple, drinks, x):
        """
        :type staple: List[int]
        :type drinks: List[int]
        :type x: int
        :rtype: int
        """
```

tab: Python3

```python
class Solution:
    def breakfastNumber(self, staple: List[int], drinks: List[int], x: int) -> int:
```

tab: C

```c


int breakfastNumber(int* staple, int stapleSize, int* drinks, int drinksSize, int x){

}
```

tab: C#

```csharp
public class Solution {
    public int BreakfastNumber(int[] staple, int[] drinks, int x) {

    }
}
```

tab: JavaScript

```javascript
/**
 * @param {number[]} staple
 * @param {number[]} drinks
 * @param {number} x
 * @return {number}
 */
var breakfastNumber = function(staple, drinks, x) {

};
```

tab: TypeScript

```typescript
function breakfastNumber(staple: number[], drinks: number[], x: number): number {

};
```

tab: PHP

```php
class Solution {

    /**
     * @param Integer[] $staple
     * @param Integer[] $drinks
     * @param Integer $x
     * @return Integer
     */
    function breakfastNumber($staple, $drinks, $x) {

    }
}
```

tab: Swift

```swift
class Solution {
    func breakfastNumber(_ staple: [Int], _ drinks: [Int], _ x: Int) -> Int {

    }
}
```

tab: Kotlin

```kotlin
class Solution {
    fun breakfastNumber(staple: IntArray, drinks: IntArray, x: Int): Int {

    }
}
```

tab: Dart

```dart
class Solution {
  int breakfastNumber(List<int> staple, List<int> drinks, int x) {

  }
}
```

tab: Go

```go
func breakfastNumber(staple []int, drinks []int, x int) int {

}
```

tab: Ruby

```ruby
# @param {Integer[]} staple
# @param {Integer[]} drinks
# @param {Integer} x
# @return {Integer}
def breakfast_number(staple, drinks, x)

end
```

tab: Scala

```scala
object Solution {
    def breakfastNumber(staple: Array[Int], drinks: Array[Int], x: Int): Int = {

    }
}
```

tab: Rust

```rust
impl Solution {
    pub fn breakfast_number(staple: Vec<i32>, drinks: Vec<i32>, x: i32) -> i32 {

    }
}
```

tab: Racket

```racket
(define/contract (breakfast-number staple drinks x)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer? exact-integer?)

  )
```

tab: Erlang

```erlang
-spec breakfast_number(Staple :: [integer()], Drinks :: [integer()], X :: integer()) -> integer().
breakfast_number(Staple, Drinks, X) ->
  .
```

tab: Elixir

```elixir
defmodule Solution do
  @spec breakfast_number(staple :: [integer], drinks :: [integer], x :: integer) :: integer
  def breakfast_number(staple, drinks, x) do

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
          
