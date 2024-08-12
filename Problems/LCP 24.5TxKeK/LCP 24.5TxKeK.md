---
tags:
  - leetcode/problem
questionId: LCP 24
title: 数字游戏
translatedTitle: 数字游戏
titleSlug: 5TxKeK
aliases:
  - 数字游戏
  - 5TxKeK
  - 数字游戏
lcLinks:
  - https://leetcode.cn/problems/5TxKeK/
lcTopics:
  - '[[array]]'
  - '[[math]]'
  - '[[heap-priority-queue]]'
lcDifficulty: Hard
lcAcRate: 59.0%
similarQuestions: []
grade: ⭐⭐⭐⭐⭐
likes: 91
dislikes: 0
favorites: []
solutions: []
notes: []
cssclasses: []
created: 2024-08-13 00:28
updated:
---

**Nav:** << previous: [[LCP 23.er94lq]] | next: [[LCP 25.Uh984O]] >>

---

## Description

~~~tabs
tab: English

No description

---

[submissions](https://leetcode.com/problems/5TxKeK/submissions/) | [solutions](https://leetcode.com/problems/5TxKeK/solutions/)


tab: 中文

小扣在秋日市集入口处发现了一个数字游戏。主办方共有 `N` 个计数器，计数器编号为 `0 ~ N-1`。每个计数器上分别显示了一个数字，小扣按计数器编号升序将所显示的数字记于数组 `nums`。每个计数器上有两个按钮，分别可以实现将显示数字加一或减一。小扣每一次操作可以选择一个计数器，按下加一或减一按钮。

主办方请小扣回答出一个长度为 `N` 的数组，第 `i` 个元素(0 <= i < N)表示将 `0~i` 号计数器 **初始** 所示数字操作成满足所有条件 `nums[a]+1 == nums[a+1],(0 <= a < i)` 的最小操作数。回答正确方可进入秋日市集。

由于答案可能很大，请将每个最小操作数对 `1,000,000,007` 取余。


**示例 1：**
>输入：`nums = [3,4,5,1,6,7]`
>
>输出：`[0,0,0,5,6,7]`
>
>解释：
>i = 0，[3] 无需操作
>i = 1，[3,4] 无需操作；
>i = 2，[3,4,5] 无需操作；
>i = 3，将 [3,4,5,1] 操作成 [3,4,5,6], 最少 5 次操作；
>i = 4，将 [3,4,5,1,6] 操作成 [3,4,5,6,7], 最少 6 次操作；
>i = 5，将 [3,4,5,1,6,7] 操作成 [3,4,5,6,7,8]，最少 7 次操作；
>返回 [0,0,0,5,6,7]。


**示例 2：**
>输入：`nums = [1,2,3,4,5]`
>
>输出：`[0,0,0,0,0]`
>
>解释：对于任意计数器编号 i 都无需操作。

**示例 3：**
>输入：`nums = [1,1,1,2,3,4]`
>
>输出：`[0,1,2,3,3,3]`
>
>解释：
>i = 0，无需操作；
>i = 1，将 [1,1] 操作成 [1,2] 或 [0,1] 最少 1 次操作；
>i = 2，将 [1,1,1] 操作成 [1,2,3] 或 [0,1,2]，最少 2 次操作；
>i = 3，将 [1,1,1,2] 操作成 [1,2,3,4] 或 [0,1,2,3]，最少 3 次操作；
>i = 4，将 [1,1,1,2,3] 操作成 [-1,0,1,2,3]，最少 3 次操作；
>i = 5，将 [1,1,1,2,3,4] 操作成 [-1,0,1,2,3,4]，最少 3 次操作；
>返回 [0,1,2,3,3,3]。


**提示：**
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^3`



---

[提交记录](https://leetcode.cn/problems/5TxKeK/submissions/) | [题解](https://leetcode.cn/problems/5TxKeK/solution/)


~~~

## Code Snippets

~~~tabs
tab: C++

```cpp
class Solution {
public:
    vector<int> numsGame(vector<int>& nums) {

    }
};
```

tab: Java

```java
class Solution {
    public int[] numsGame(int[] nums) {

    }
}
```

tab: Python

```python
class Solution(object):
    def numsGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
```

tab: Python3

```python
class Solution:
    def numsGame(self, nums: List[int]) -> List[int]:
```

tab: C

```c


/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* numsGame(int* nums, int numsSize, int* returnSize){

}
```

tab: C#

```csharp
public class Solution {
    public int[] NumsGame(int[] nums) {

    }
}
```

tab: JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var numsGame = function(nums) {

};
```

tab: TypeScript

```typescript
function numsGame(nums: number[]): number[] {

};
```

tab: PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function numsGame($nums) {

    }
}
```

tab: Swift

```swift
class Solution {
    func numsGame(_ nums: [Int]) -> [Int] {

    }
}
```

tab: Kotlin

```kotlin
class Solution {
    fun numsGame(nums: IntArray): IntArray {

    }
}
```

tab: Dart

```dart
class Solution {
  List<int> numsGame(List<int> nums) {

  }
}
```

tab: Go

```go
func numsGame(nums []int) []int {

}
```

tab: Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer[]}
def nums_game(nums)

end
```

tab: Scala

```scala
object Solution {
    def numsGame(nums: Array[Int]): Array[Int] = {

    }
}
```

tab: Rust

```rust
impl Solution {
    pub fn nums_game(nums: Vec<i32>) -> Vec<i32> {

    }
}
```

tab: Racket

```racket
(define/contract (nums-game nums)
  (-> (listof exact-integer?) (listof exact-integer?))

  )
```

tab: Erlang

```erlang
-spec nums_game(Nums :: [integer()]) -> [integer()].
nums_game(Nums) ->
  .
```

tab: Elixir

```elixir
defmodule Solution do
  @spec nums_game(nums :: [integer]) :: [integer]
  def nums_game(nums) do

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
          
