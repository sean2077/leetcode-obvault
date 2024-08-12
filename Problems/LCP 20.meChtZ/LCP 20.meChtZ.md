---
tags:
  - leetcode/problem
questionId: LCP 20
title: 快速公交
translatedTitle: 快速公交
titleSlug: meChtZ
aliases:
  - 快速公交
  - meChtZ
  - 快速公交
lcLink: https://leetcode.com/problems/meChtZ/
lcTopics:
  - '[[memoization]]'
  - '[[array]]'
  - '[[dynamic-programming]]'
lcDifficulty: Hard
lcAcRate: 36.9%
similarQuestions: []
grade: ⭐⭐⭐⭐⭐
likes: 47
dislikes: 0
favorites: []
solutions: []
notes: []
cssclasses: []
created: 2024-08-13 00:10
updated:
---

**Nav:** << previous: [[LCP 19.UlBDOe]] | next: [[LCP 21.Za25hA]] >>

---

## Description

~~~tabs
tab: English

No description

---

[submissions](https://leetcode.com/problems/meChtZ/submissions/) | [solutions](https://leetcode.com/problems/meChtZ/solutions/)


tab: 中文

小扣打算去秋日市集，由于游客较多，小扣的移动速度受到了人流影响：
- 小扣从 `x` 号站点移动至 `x + 1` 号站点需要花费的时间为 `inc`；
- 小扣从 `x` 号站点移动至 `x - 1` 号站点需要花费的时间为 `dec`。

现有 `m` 辆公交车，编号为 `0` 到 `m-1`。小扣也可以通过搭乘编号为 `i` 的公交车，从 `x` 号站点移动至 `jump[i]*x` 号站点，耗时仅为 `cost[i]`。小扣可以搭乘任意编号的公交车且搭乘公交次数不限。

假定小扣起始站点记作 `0`，秋日市集站点记作 `target`，请返回小扣抵达秋日市集最少需要花费多少时间。由于数字较大，最终答案需要对 1000000007 (1e9 + 7) 取模。

注意：小扣可在移动过程中到达编号大于 `target` 的站点。

**示例 1：**
>输入：`target = 31, inc =  5, dec = 3, jump = [6], cost = [10]`
>
>输出：`33`
>
>解释：
>小扣步行至 1 号站点，花费时间为 5；
>小扣从 1 号站台搭乘 0 号公交至 6 * 1 = 6 站台，花费时间为 10；
>小扣从 6 号站台步行至 5 号站台，花费时间为 3；
>小扣从 5 号站台搭乘 0 号公交至 6 * 5 = 30 站台，花费时间为 10；
>小扣从 30 号站台步行至 31 号站台，花费时间为 5；
>最终小扣花费总时间为 33。


**示例 2：**
>输入：`target = 612, inc =  4, dec = 5, jump = [3,6,8,11,5,10,4], cost = [4,7,6,3,7,6,4]`
>
>输出：`26`
>
>解释：
>小扣步行至 1 号站点，花费时间为 4；
>小扣从 1 号站台搭乘 0 号公交至 3 * 1 = 3 站台，花费时间为 4；
>小扣从 3 号站台搭乘 3 号公交至 11 * 3 = 33 站台，花费时间为 3；
>小扣从 33 号站台步行至 34 站台，花费时间为 4；
>小扣从 34 号站台搭乘 0 号公交至 3 * 34 = 102 站台，花费时间为 4；
>小扣从 102 号站台搭乘 1 号公交至 6 * 102 = 612 站台，花费时间为 7； 
>最终小扣花费总时间为 26。


**提示：**
- `1 <= target <= 10^9`
- `1 <= jump.length, cost.length <= 10`
- `2 <= jump[i] <= 10^6`
- `1 <= inc, dec, cost[i] <= 10^6`

---

[提交记录](https://leetcode.cn/problems/meChtZ/submissions/) | [题解](https://leetcode.cn/problems/meChtZ/solution/)


~~~

## Code Snippets

~~~tabs
tab: C++

```cpp
class Solution {
public:
    int busRapidTransit(int target, int inc, int dec, vector<int>& jump, vector<int>& cost) {

    }
};
```

tab: Java

```java
class Solution {
    public int busRapidTransit(int target, int inc, int dec, int[] jump, int[] cost) {

    }
}
```

tab: Python

```python
class Solution(object):
    def busRapidTransit(self, target, inc, dec, jump, cost):
        """
        :type target: int
        :type inc: int
        :type dec: int
        :type jump: List[int]
        :type cost: List[int]
        :rtype: int
        """
```

tab: Python3

```python
class Solution:
    def busRapidTransit(self, target: int, inc: int, dec: int, jump: List[int], cost: List[int]) -> int:
```

tab: C

```c


int busRapidTransit(int target, int inc, int dec, int* jump, int jumpSize, int* cost, int costSize){

}
```

tab: C#

```csharp
public class Solution {
    public int BusRapidTransit(int target, int inc, int dec, int[] jump, int[] cost) {

    }
}
```

tab: JavaScript

```javascript
/**
 * @param {number} target
 * @param {number} inc
 * @param {number} dec
 * @param {number[]} jump
 * @param {number[]} cost
 * @return {number}
 */
var busRapidTransit = function(target, inc, dec, jump, cost) {

};
```

tab: TypeScript

```typescript
function busRapidTransit(target: number, inc: number, dec: number, jump: number[], cost: number[]): number {

};
```

tab: PHP

```php
class Solution {

    /**
     * @param Integer $target
     * @param Integer $inc
     * @param Integer $dec
     * @param Integer[] $jump
     * @param Integer[] $cost
     * @return Integer
     */
    function busRapidTransit($target, $inc, $dec, $jump, $cost) {

    }
}
```

tab: Swift

```swift
class Solution {
    func busRapidTransit(_ target: Int, _ inc: Int, _ dec: Int, _ jump: [Int], _ cost: [Int]) -> Int {

    }
}
```

tab: Kotlin

```kotlin
class Solution {
    fun busRapidTransit(target: Int, inc: Int, dec: Int, jump: IntArray, cost: IntArray): Int {

    }
}
```

tab: Dart

```dart
class Solution {
  int busRapidTransit(int target, int inc, int dec, List<int> jump, List<int> cost) {

  }
}
```

tab: Go

```go
func busRapidTransit(target int, inc int, dec int, jump []int, cost []int) int {

}
```

tab: Ruby

```ruby
# @param {Integer} target
# @param {Integer} inc
# @param {Integer} dec
# @param {Integer[]} jump
# @param {Integer[]} cost
# @return {Integer}
def bus_rapid_transit(target, inc, dec, jump, cost)

end
```

tab: Scala

```scala
object Solution {
    def busRapidTransit(target: Int, inc: Int, dec: Int, jump: Array[Int], cost: Array[Int]): Int = {

    }
}
```

tab: Rust

```rust
impl Solution {
    pub fn bus_rapid_transit(target: i32, inc: i32, dec: i32, jump: Vec<i32>, cost: Vec<i32>) -> i32 {

    }
}
```

tab: Racket

```racket
(define/contract (bus-rapid-transit target inc dec jump cost)
  (-> exact-integer? exact-integer? exact-integer? (listof exact-integer?) (listof exact-integer?) exact-integer?)

  )
```

tab: Erlang

```erlang
-spec bus_rapid_transit(Target :: integer(), Inc :: integer(), Dec :: integer(), Jump :: [integer()], Cost :: [integer()]) -> integer().
bus_rapid_transit(Target, Inc, Dec, Jump, Cost) ->
  .
```

tab: Elixir

```elixir
defmodule Solution do
  @spec bus_rapid_transit(target :: integer, inc :: integer, dec :: integer, jump :: [integer], cost :: [integer]) :: integer
  def bus_rapid_transit(target, inc, dec, jump, cost) do

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
          
