---
tags:
  - leetcode/problem
questionId: LCP 72
title: 补给马车
translatedTitle: 补给马车
titleSlug: hqCnmP
aliases:
  - 补给马车
  - hqCnmP
  - 补给马车
lcLinks:
  - https://leetcode.cn/problems/hqCnmP/
lcTopics: []
lcDifficulty: Easy
lcAcRate: 67.8%
similarQuestions: []
grade: ⭐⭐⭐⭐⭐
likes: 10
dislikes: 0
favorites: []
solutions: []
notes: []
---

**Nav:** << previous: [[LCP 71.集水器]] | next: [[LCP 73.探险营地]] >>

---

## Description

~~~tabs
tab: English

No description

---

[submissions](https://leetcode.com/problems/hqCnmP/submissions/) | [solutions](https://leetcode.com/problems/hqCnmP/solutions/)


tab: 中文

远征队即将开启未知的冒险之旅，不过在此之前，将对补给车队进行最后的检查。`supplies[i]` 表示编号为 `i` 的补给马车装载的物资数量。
考虑到车队过长容易被野兽偷袭，他们决定将车队的长度变为原来的一半（向下取整），计划为：
- 找出车队中 **物资之和最小** 两辆 **相邻** 马车，将它们车辆的物资整合为一辆。若存在多组物资之和相同的马车，则取编号最小的两辆马车进行整合；
- 重复上述操作直到车队长度符合要求。

请返回车队长度符合要求后，物资的分布情况。

**示例 1：**
>输入：`supplies = [7,3,6,1,8]`
>
>输出：`[10,15]`
>
>解释：
> 第 1 次合并，符合条件的两辆马车为 6,1，合并后的车队为 [7,3,7,8]；
> 第 2 次合并，符合条件的两辆马车为 (7,3) 和 (3,7)，取编号最小的 (7,3)，合并后的车队为 [10,7,8]；
> 第 3 次合并，符合条件的两辆马车为 7,8，合并后的车队为 [10,15]；
>返回 `[10,15]`

**示例 2：**
>输入：`supplies = [1,3,1,5]`
>
>输出：`[5,5]`

**解释：**
- `2 <= supplies.length <= 1000`
- `1 <= supplies[i] <= 1000`

---

[提交记录](https://leetcode.cn/problems/hqCnmP/submissions/) | [题解](https://leetcode.cn/problems/hqCnmP/solution/)


~~~

## Code Snippets

~~~tabs
tab: C++

```cpp
class Solution {
public:
    vector<int> supplyWagon(vector<int>& supplies) {

    }
};
```

tab: Java

```java
class Solution {
    public int[] supplyWagon(int[] supplies) {

    }
}
```

tab: Python

```python
class Solution(object):
    def supplyWagon(self, supplies):
        """
        :type supplies: List[int]
        :rtype: List[int]
        """
```

tab: Python3

```python
class Solution:
    def supplyWagon(self, supplies: List[int]) -> List[int]:
```

tab: C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* supplyWagon(int* supplies, int suppliesSize, int* returnSize){

}
```

tab: C#

```csharp
public class Solution {
    public int[] SupplyWagon(int[] supplies) {

    }
}
```

tab: JavaScript

```javascript
/**
 * @param {number[]} supplies
 * @return {number[]}
 */
var supplyWagon = function(supplies) {

};
```

tab: TypeScript

```typescript
function supplyWagon(supplies: number[]): number[] {

};
```

tab: PHP

```php
class Solution {

    /**
     * @param Integer[] $supplies
     * @return Integer[]
     */
    function supplyWagon($supplies) {

    }
}
```

tab: Swift

```swift
class Solution {
    func supplyWagon(_ supplies: [Int]) -> [Int] {

    }
}
```

tab: Kotlin

```kotlin
class Solution {
    fun supplyWagon(supplies: IntArray): IntArray {

    }
}
```

tab: Dart

```dart
class Solution {
  List<int> supplyWagon(List<int> supplies) {

  }
}
```

tab: Go

```go
func supplyWagon(supplies []int) []int {

}
```

tab: Ruby

```ruby
# @param {Integer[]} supplies
# @return {Integer[]}
def supply_wagon(supplies)

end
```

tab: Scala

```scala
object Solution {
    def supplyWagon(supplies: Array[Int]): Array[Int] = {

    }
}
```

tab: Rust

```rust
impl Solution {
    pub fn supply_wagon(supplies: Vec<i32>) -> Vec<i32> {

    }
}
```

tab: Racket

```racket
(define/contract (supply-wagon supplies)
  (-> (listof exact-integer?) (listof exact-integer?))

  )
```

tab: Erlang

```erlang
-spec supply_wagon(Supplies :: [integer()]) -> [integer()].
supply_wagon(Supplies) ->
  .
```

tab: Elixir

```elixir
defmodule Solution do
  @spec supply_wagon(supplies :: [integer]) :: [integer]
  def supply_wagon(supplies) do

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
          
