---
tags:
  - leetcode/problem
questionId: LCP 28
title: 采购方案
translatedTitle: 采购方案
titleSlug: 4xy4Wx
aliases:
  - 采购方案
  - 4xy4Wx
  - 采购方案
lcLinks:
  - https://leetcode.cn/problems/4xy4Wx/
lcTopics:
  - '[[array]]'
  - '[[two-pointers]]'
  - '[[binary-search]]'
  - '[[sorting]]'
lcDifficulty: Easy
lcAcRate: 32.5%
similarQuestions: []
grade: ⭐⭐⭐⭐⭐
likes: 60
dislikes: 0
favorites: []
solutions: []
notes: []
cssclasses: []
created: 2024-08-13 00:28
updated:
---

**Nav:** << previous: [[LCP 27.IQvJ9i]] | next: [[LCP 29.SNJvJP]] >>

---

## Description

~~~tabs
tab: English

No description

---

[submissions](https://leetcode.com/problems/4xy4Wx/submissions/) | [solutions](https://leetcode.com/problems/4xy4Wx/solutions/)


tab: 中文

小力将 N 个零件的报价存于数组 `nums`。小力预算为 `target`，假定小力仅购买两个零件，要求购买零件的花费不超过预算，请问他有多少种采购方案。

注意：答案需要以 `1e9 + 7 (1000000007)` 为底取模，如：计算初始结果为：`1000000008`，请返回 `1`


**示例 1：**
>输入：`nums = [2,5,3,5], target = 6`
>
>输出：`1`
>
>解释：预算内仅能购买 nums[0] 与 nums[2]。

**示例 2：**
>输入：`nums = [2,2,1,9], target = 10`
>
>输出：`4`
>
>解释：符合预算的采购方案如下：
>nums[0] + nums[1] = 4
>nums[0] + nums[2] = 3
>nums[1] + nums[2] = 3
>nums[2] + nums[3] = 10

**提示：**
- `2 <= nums.length <= 10^5`
- `1 <= nums[i], target <= 10^5`


---

[提交记录](https://leetcode.cn/problems/4xy4Wx/submissions/) | [题解](https://leetcode.cn/problems/4xy4Wx/solution/)


~~~

## Code Snippets

~~~tabs
tab: C++

```cpp
class Solution {
public:
    int purchasePlans(vector<int>& nums, int target) {

    }
};
```

tab: Java

```java
class Solution {
    public int purchasePlans(int[] nums, int target) {

    }
}
```

tab: Python

```python
class Solution(object):
    def purchasePlans(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
```

tab: Python3

```python
class Solution:
    def purchasePlans(self, nums: List[int], target: int) -> int:
```

tab: C

```c


int purchasePlans(int* nums, int numsSize, int target){

}
```

tab: C#

```csharp
public class Solution {
    public int PurchasePlans(int[] nums, int target) {

    }
}
```

tab: JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var purchasePlans = function(nums, target) {

};
```

tab: TypeScript

```typescript
function purchasePlans(nums: number[], target: number): number {

};
```

tab: PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer
     */
    function purchasePlans($nums, $target) {

    }
}
```

tab: Swift

```swift
class Solution {
    func purchasePlans(_ nums: [Int], _ target: Int) -> Int {

    }
}
```

tab: Kotlin

```kotlin
class Solution {
    fun purchasePlans(nums: IntArray, target: Int): Int {

    }
}
```

tab: Dart

```dart
class Solution {
  int purchasePlans(List<int> nums, int target) {

  }
}
```

tab: Go

```go
func purchasePlans(nums []int, target int) int {

}
```

tab: Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer}
def purchase_plans(nums, target)

end
```

tab: Scala

```scala
object Solution {
    def purchasePlans(nums: Array[Int], target: Int): Int = {

    }
}
```

tab: Rust

```rust
impl Solution {
    pub fn purchase_plans(nums: Vec<i32>, target: i32) -> i32 {

    }
}
```

tab: Racket

```racket
(define/contract (purchase-plans nums target)
  (-> (listof exact-integer?) exact-integer? exact-integer?)

  )
```

tab: Erlang

```erlang
-spec purchase_plans(Nums :: [integer()], Target :: integer()) -> integer().
purchase_plans(Nums, Target) ->
  .
```

tab: Elixir

```elixir
defmodule Solution do
  @spec purchase_plans(nums :: [integer], target :: integer) :: integer
  def purchase_plans(nums, target) do

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
          
