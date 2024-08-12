---
tags:
  - leetcode/problem
questionId: LCP 51
title: 烹饪料理
translatedTitle: 烹饪料理
titleSlug: UEcfPD
aliases:
  - 烹饪料理
  - UEcfPD
  - 烹饪料理
lcLink: https://leetcode.com/problems/UEcfPD/
lcTopics:
  - '[[bit-manipulation]]'
  - '[[array]]'
  - '[[backtracking]]'
  - '[[enumeration]]'
lcDifficulty: Easy
lcAcRate: 49.8%
similarQuestions: []
grade: ⭐⭐⭐⭐⭐
likes: 35
dislikes: 0
favorites: []
solutions: []
notes: []
cssclasses: []
created: 2024-08-13 00:10
updated:
---

**Nav:** << previous: [[LCP 50.WHnhjV]] | next: [[LCP 52.QO5KpG]] >>

---

## Description

~~~tabs
tab: English

No description

---

[submissions](https://leetcode.com/problems/UEcfPD/submissions/) | [solutions](https://leetcode.com/problems/UEcfPD/solutions/)


tab: 中文

欢迎各位勇者来到力扣城，城内设有烹饪锅供勇者制作料理，为自己恢复状态。

勇者背包内共有编号为 `0 ~ 4` 的五种食材，其中 `materials[j]` 表示第 `j` 种食材的数量。通过这些食材可以制作若干料理，`cookbooks[i][j]` 表示制作第 `i` 种料理需要第 `j` 种食材的数量，而 `attribute[i] = [x,y]` 表示第 `i` 道料理的美味度 `x` 和饱腹感 `y`。

在饱腹感不小于 `limit` 的情况下，请返回勇者可获得的最大美味度。如果无法满足饱腹感要求，则返回 `-1`。

**注意：**
- 每种料理只能制作一次。


**示例 1：**
>输入：`materials = [3,2,4,1,2]`
>`cookbooks = [[1,1,0,1,2],[2,1,4,0,0],[3,2,4,1,0]]`
>`attribute = [[3,2],[2,4],[7,6]]`
>`limit = 5`
>
>输出：`7`
>
>解释：
>食材数量可以满足以下两种方案：
>方案一：制作料理 0 和料理 1，可获得饱腹感 2+4、美味度 3+2
>方案二：仅制作料理 2， 可饱腹感为 6、美味度为 7
>因此在满足饱腹感的要求下，可获得最高美味度 7

**示例 2：**
>输入：`materials = [10,10,10,10,10]`
>`cookbooks = [[1,1,1,1,1],[3,3,3,3,3],[10,10,10,10,10]]`
>`attribute = [[5,5],[6,6],[10,10]]`
>`limit = 1`
>
>输出：`11`
>
>解释：通过制作料理 0 和 1，可满足饱腹感，并获得最高美味度 11

**提示：**
+ `materials.length == 5`
+ `1 <= cookbooks.length == attribute.length <= 8`
+ `cookbooks[i].length == 5`
+ `attribute[i].length == 2`
+ `0 <= materials[i], cookbooks[i][j], attribute[i][j] <= 20`
+ `1 <= limit <= 100`


---

[提交记录](https://leetcode.cn/problems/UEcfPD/submissions/) | [题解](https://leetcode.cn/problems/UEcfPD/solution/)


~~~

## Code Snippets

~~~tabs
tab: C++

```cpp
class Solution {
public:
    int perfectMenu(vector<int>& materials, vector<vector<int>>& cookbooks, vector<vector<int>>& attribute, int limit) {

    }
};
```

tab: Java

```java
class Solution {
    public int perfectMenu(int[] materials, int[][] cookbooks, int[][] attribute, int limit) {

    }
}
```

tab: Python

```python
class Solution(object):
    def perfectMenu(self, materials, cookbooks, attribute, limit):
        """
        :type materials: List[int]
        :type cookbooks: List[List[int]]
        :type attribute: List[List[int]]
        :type limit: int
        :rtype: int
        """
```

tab: Python3

```python
class Solution:
    def perfectMenu(self, materials: List[int], cookbooks: List[List[int]], attribute: List[List[int]], limit: int) -> int:
```

tab: C

```c


int perfectMenu(int* materials, int materialsSize, int** cookbooks, int cookbooksSize, int* cookbooksColSize, int** attribute, int attributeSize, int* attributeColSize, int limit){

}
```

tab: C#

```csharp
public class Solution {
    public int PerfectMenu(int[] materials, int[][] cookbooks, int[][] attribute, int limit) {

    }
}
```

tab: JavaScript

```javascript
/**
 * @param {number[]} materials
 * @param {number[][]} cookbooks
 * @param {number[][]} attribute
 * @param {number} limit
 * @return {number}
 */
var perfectMenu = function(materials, cookbooks, attribute, limit) {

};
```

tab: TypeScript

```typescript
function perfectMenu(materials: number[], cookbooks: number[][], attribute: number[][], limit: number): number {

};
```

tab: PHP

```php
class Solution {

    /**
     * @param Integer[] $materials
     * @param Integer[][] $cookbooks
     * @param Integer[][] $attribute
     * @param Integer $limit
     * @return Integer
     */
    function perfectMenu($materials, $cookbooks, $attribute, $limit) {

    }
}
```

tab: Swift

```swift
class Solution {
    func perfectMenu(_ materials: [Int], _ cookbooks: [[Int]], _ attribute: [[Int]], _ limit: Int) -> Int {

    }
}
```

tab: Kotlin

```kotlin
class Solution {
    fun perfectMenu(materials: IntArray, cookbooks: Array<IntArray>, attribute: Array<IntArray>, limit: Int): Int {

    }
}
```

tab: Dart

```dart
class Solution {
  int perfectMenu(List<int> materials, List<List<int>> cookbooks, List<List<int>> attribute, int limit) {

  }
}
```

tab: Go

```go
func perfectMenu(materials []int, cookbooks [][]int, attribute [][]int, limit int) int {

}
```

tab: Ruby

```ruby
# @param {Integer[]} materials
# @param {Integer[][]} cookbooks
# @param {Integer[][]} attribute
# @param {Integer} limit
# @return {Integer}
def perfect_menu(materials, cookbooks, attribute, limit)

end
```

tab: Scala

```scala
object Solution {
    def perfectMenu(materials: Array[Int], cookbooks: Array[Array[Int]], attribute: Array[Array[Int]], limit: Int): Int = {

    }
}
```

tab: Rust

```rust
impl Solution {
    pub fn perfect_menu(materials: Vec<i32>, cookbooks: Vec<Vec<i32>>, attribute: Vec<Vec<i32>>, limit: i32) -> i32 {

    }
}
```

tab: Racket

```racket
(define/contract (perfect-menu materials cookbooks attribute limit)
  (-> (listof exact-integer?) (listof (listof exact-integer?)) (listof (listof exact-integer?)) exact-integer? exact-integer?)

  )
```

tab: Erlang

```erlang
-spec perfect_menu(Materials :: [integer()], Cookbooks :: [[integer()]], Attribute :: [[integer()]], Limit :: integer()) -> integer().
perfect_menu(Materials, Cookbooks, Attribute, Limit) ->
  .
```

tab: Elixir

```elixir
defmodule Solution do
  @spec perfect_menu(materials :: [integer], cookbooks :: [[integer]], attribute :: [[integer]], limit :: integer) :: integer
  def perfect_menu(materials, cookbooks, attribute, limit) do

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
          
