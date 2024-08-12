---
tags:
  - leetcode/problem
questionId: LCP 81
title: 与非的谜题
translatedTitle: 与非的谜题
titleSlug: ryfUiz
aliases:
  - 与非的谜题
  - ryfUiz
  - 与非的谜题
lcLinks:
  - https://leetcode.cn/problems/ryfUiz/
lcTopics: []
lcDifficulty: Hard
lcAcRate: 47.6%
similarQuestions: []
grade: ⭐⭐⭐⭐⭐
likes: 5
dislikes: 0
favorites: []
solutions: []
notes: []
cssclasses: []
created: 2024-08-13 00:28
updated:
---

**Nav:** << previous: [[LCP 80.qoQAMX]] | next: [[LCP 82.cnHoX6]] >>

---

## Description

~~~tabs
tab: English

No description

---

[submissions](https://leetcode.com/problems/ryfUiz/submissions/) | [solutions](https://leetcode.com/problems/ryfUiz/solutions/)


tab: 中文

在永恒之森中，封存着有关万灵之树线索的卷轴，只要探险队通过最后的考验，便可以获取前往万灵之树的线索。

探险队需要从一段不断变化的谜题数组中找到最终的密码，初始的谜题为长度为 `n` 的数组 `arr`（下标从 0 开始），数组中的数字代表了 `k` 位二进制数。
破解谜题的过程中，需要使用 `与非（NAND）` 运算方式，`operations[i] = [type,x,y]` 表示第 `i` 次进行的谜题操作信息：
- 若 `type = 0`，表示修改操作，将谜题数组中下标 `x` 的数字变化为 `y`；
- 若 `type = 1`，表示运算操作，将数字 `y` 进行 `x*n` 次「与非」操作，第 `i` 次与非操作为 `y = y NAND arr[i%n]`；
    > 运算操作结果即：`y NAND arr[0%n] NAND arr[1%n] NAND arr[2%n] ... NAND arr[(x*n-1)%n]`

最后，将所有运算操作的结果按顺序逐一进行 `异或（XOR）`运算，从而得到最终解开封印的密码。请返回最终解开封印的密码。

**注意:**
- 「与非」（NAND）的操作为：先进行 `与` 操作，后进行 `非` 操作。
    > 例如：两个三位二进制数`2`和`3`，其与非结果为 `NOT ((010) AND (011)) = (101) = 5`

**示例 1：**
> 输入: 
> `k = 3`
> `arr = [1,2]`
> `operations = [[1,2,3],[0,0,3],[1,2,2]]`
>
> 输出: `2`
>
> 解释：
> 初始的谜题数组为 [1,2]，二进制位数为 3，
> 第 0 次进行运算操作，将数字 3(011) 进行 2\*2 次「与非」运算，
> 运算操作结果为 `3 NAND 1 NAND 2 NAND 1 NAND 2 = 5`
> 第 1 次进行修改操作，谜题数组的第 `0` 个数字变化为 `3`，谜题变成 `[3,2]`
> 第 2 次进行运算操作，将数字 2(010) 进行 2\*2 次「与非」运算，
> 运算操作结果为 `2 NAND 3 NAND 2 NAND 3 NAND 2 = 7`
> 所有运算操作结果进行「异或」运算为 `5 XOR 7 = 2`
> 因此得到的最终密码为 `2`。

**示例 2：**
> 输入:
> `k = 4`
> `arr = [4,6,4,7,10,9,11]`
> `operations = [[1,5,7],[1,7,14],[0,6,7],[1,6,5]]`
> 输出: `9`
> 解释: 
> 初始的谜题数组为 [4,6,4,7,10,9,11],
> 第 0 次进行运算操作，运算操作结果为 5；
> 第 1 次进行运算操作，运算操作结果为 5；
> 第 2 次进行修改操作，修改后谜题数组为 [4, 6, 4, 7, 10, 9, 7]；
> 第 3 次进行运算操作，运算操作结果为 9；
> 所有运算操作结果进行「异或」运算为 `5 XOR 5 XOR 9 = 9`；
> 因此得到的最终密码为 `9`。

**提示:**
- `1 <= arr.length, operations.length <= 10^4`
- `1 <= k <= 30`
- `0 <= arr[i] < 2^k`
- 若 `type = 0`，`0 <= x < arr.length` 且 `0 <= y < 2^k`
- 若 `type = 1`，`1 <= x < 10^9` 且 `0 <= y < 2^k`
- 保证存在 `type = 1` 的操作


---

[提交记录](https://leetcode.cn/problems/ryfUiz/submissions/) | [题解](https://leetcode.cn/problems/ryfUiz/solution/)


~~~

## Code Snippets

~~~tabs
tab: C++

```cpp
class Solution {
public:
    int getNandResult(int k, vector<int>& arr, vector<vector<int>>& operations) {

    }
};
```

tab: Java

```java
class Solution {
    public int getNandResult(int k, int[] arr, int[][] operations) {

    }
}
```

tab: Python

```python
class Solution(object):
    def getNandResult(self, k, arr, operations):
        """
        :type k: int
        :type arr: List[int]
        :type operations: List[List[int]]
        :rtype: int
        """
```

tab: Python3

```python
class Solution:
    def getNandResult(self, k: int, arr: List[int], operations: List[List[int]]) -> int:
```

tab: C

```c
int getNandResult(int k, int* arr, int arrSize, int** operations, int operationsSize, int* operationsColSize){

}
```

tab: C#

```csharp
public class Solution {
    public int GetNandResult(int k, int[] arr, int[][] operations) {

    }
}
```

tab: JavaScript

```javascript
/**
 * @param {number} k
 * @param {number[]} arr
 * @param {number[][]} operations
 * @return {number}
 */
var getNandResult = function(k, arr, operations) {

};
```

tab: TypeScript

```typescript
function getNandResult(k: number, arr: number[], operations: number[][]): number {

};
```

tab: PHP

```php
class Solution {

    /**
     * @param Integer $k
     * @param Integer[] $arr
     * @param Integer[][] $operations
     * @return Integer
     */
    function getNandResult($k, $arr, $operations) {

    }
}
```

tab: Swift

```swift
class Solution {
    func getNandResult(_ k: Int, _ arr: [Int], _ operations: [[Int]]) -> Int {

    }
}
```

tab: Kotlin

```kotlin
class Solution {
    fun getNandResult(k: Int, arr: IntArray, operations: Array<IntArray>): Int {

    }
}
```

tab: Dart

```dart
class Solution {
  int getNandResult(int k, List<int> arr, List<List<int>> operations) {

  }
}
```

tab: Go

```go
func getNandResult(k int, arr []int, operations [][]int) int {

}
```

tab: Ruby

```ruby
# @param {Integer} k
# @param {Integer[]} arr
# @param {Integer[][]} operations
# @return {Integer}
def get_nand_result(k, arr, operations)

end
```

tab: Scala

```scala
object Solution {
    def getNandResult(k: Int, arr: Array[Int], operations: Array[Array[Int]]): Int = {

    }
}
```

tab: Rust

```rust
impl Solution {
    pub fn get_nand_result(k: i32, arr: Vec<i32>, operations: Vec<Vec<i32>>) -> i32 {

    }
}
```

tab: Racket

```racket
(define/contract (get-nand-result k arr operations)
  (-> exact-integer? (listof exact-integer?) (listof (listof exact-integer?)) exact-integer?)

  )
```

tab: Erlang

```erlang
-spec get_nand_result(K :: integer(), Arr :: [integer()], Operations :: [[integer()]]) -> integer().
get_nand_result(K, Arr, Operations) ->
  .
```

tab: Elixir

```elixir
defmodule Solution do
  @spec get_nand_result(k :: integer, arr :: [integer], operations :: [[integer]]) :: integer
  def get_nand_result(k, arr, operations) do

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
          
