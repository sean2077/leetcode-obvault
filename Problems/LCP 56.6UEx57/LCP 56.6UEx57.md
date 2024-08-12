---
tags:
  - leetcode/problem
questionId: LCP 56
title: 信物传送
translatedTitle: 信物传送
titleSlug: 6UEx57
aliases:
  - 信物传送
  - 6UEx57
  - 信物传送
lcLinks:
  - https://leetcode.cn/problems/6UEx57/
lcTopics:
  - '[[breadth-first-search]]'
  - '[[graph]]'
  - '[[array]]'
  - '[[matrix]]'
  - '[[shortest-path]]'
  - '[[heap-priority-queue]]'
lcDifficulty: Medium
lcAcRate: 46.1%
similarQuestions: []
grade: ⭐⭐⭐⭐⭐
likes: 22
dislikes: 0
favorites: []
solutions: []
notes: []
cssclasses: []
created: 2024-08-13 00:28
updated:
---

**Nav:** << previous: [[LCP 55.PTXy4P]] | next: [[LCP 57.ZbAuEH]] >>

---

## Description

~~~tabs
tab: English

No description

---

[submissions](https://leetcode.com/problems/6UEx57/submissions/) | [solutions](https://leetcode.com/problems/6UEx57/solutions/)


tab: 中文

欢迎各位勇者来到力扣城，本次试炼主题为「信物传送」。

本次试炼场地设有若干传送带，`matrix[i][j]` 表示第 `i` 行 `j` 列的传送带运作方向，`"^","v","<",">"` 这四种符号分别表示 **上、下、左、右** 四个方向。信物会随传送带的方向移动。勇者**每一次**施法操作，可**临时**变更一处传送带的方向，在物品经过后传送带恢复原方向。
![lcp (2).gif](https://pic.leetcode-cn.com/1649835246-vfupSL-lcp%20\(2\).gif){:width=300px}

通关信物初始位于坐标 `start`处，勇者需要将其移动到坐标 `end` 处，请返回勇者施法操作的最少次数。



**注意：**
- `start` 和 `end` 的格式均为 `[i,j]`

**示例 1:**
> 输入：`matrix = [">>v","v^<","<><"], start = [0,1], end = [2,0]`
>
> 输出：`1`
>
> 解释：
> 如上图所示
> 当信物移动到 `[1,1]` 时，勇者施法一次将 `[1,1]` 的传送方向 `^` 从变更为 `<`
> 从而信物移动到 `[1,0]`，后续到达 `end` 位置
> 因此勇者最少需要施法操作 1 次

**示例 2:**
> 输入：`matrix = [">>v",">>v","^<<"], start = [0,0], end = [1,1]`
>
> 输出：`0`
>
> 解释：勇者无需施法，信物将自动传送至 `end` 位置

**示例 3:**
> 输入：`matrix = [">^^>","<^v>","^v^<"], start = [0,0], end = [1,3]`
>
> 输出：`3`

**提示：**
- `matrix` 中仅包含 `'^'、'v'、'<'、'>'`
- `0 < matrix.length <= 100`
- `0 < matrix[i].length <= 100`
- `0 <= start[0],end[0] < matrix.length`
- `0 <= start[1],end[1] < matrix[i].length`



---

[提交记录](https://leetcode.cn/problems/6UEx57/submissions/) | [题解](https://leetcode.cn/problems/6UEx57/solution/)


~~~

## Code Snippets

~~~tabs
tab: C++

```cpp
class Solution {
public:
    int conveyorBelt(vector<string>& matrix, vector<int>& start, vector<int>& end) {

    }
};
```

tab: Java

```java
class Solution {
    public int conveyorBelt(String[] matrix, int[] start, int[] end) {

    }
}
```

tab: Python

```python
class Solution(object):
    def conveyorBelt(self, matrix, start, end):
        """
        :type matrix: List[str]
        :type start: List[int]
        :type end: List[int]
        :rtype: int
        """
```

tab: Python3

```python
class Solution:
    def conveyorBelt(self, matrix: List[str], start: List[int], end: List[int]) -> int:
```

tab: C

```c


int conveyorBelt(char** matrix, int matrixSize, int* start, int startSize, int* end, int endSize){

}
```

tab: C#

```csharp
public class Solution {
    public int ConveyorBelt(string[] matrix, int[] start, int[] end) {

    }
}
```

tab: JavaScript

```javascript
/**
 * @param {string[]} matrix
 * @param {number[]} start
 * @param {number[]} end
 * @return {number}
 */
var conveyorBelt = function(matrix, start, end) {

};
```

tab: TypeScript

```typescript
function conveyorBelt(matrix: string[], start: number[], end: number[]): number {

};
```

tab: PHP

```php
class Solution {

    /**
     * @param String[] $matrix
     * @param Integer[] $start
     * @param Integer[] $end
     * @return Integer
     */
    function conveyorBelt($matrix, $start, $end) {

    }
}
```

tab: Swift

```swift
class Solution {
    func conveyorBelt(_ matrix: [String], _ start: [Int], _ end: [Int]) -> Int {

    }
}
```

tab: Kotlin

```kotlin
class Solution {
    fun conveyorBelt(matrix: Array<String>, start: IntArray, end: IntArray): Int {

    }
}
```

tab: Dart

```dart
class Solution {
  int conveyorBelt(List<String> matrix, List<int> start, List<int> end) {

  }
}
```

tab: Go

```go
func conveyorBelt(matrix []string, start []int, end []int) int {

}
```

tab: Ruby

```ruby
# @param {String[]} matrix
# @param {Integer[]} start
# @param {Integer[]} end
# @return {Integer}
def conveyor_belt(matrix, start, end)

end
```

tab: Scala

```scala
object Solution {
    def conveyorBelt(matrix: Array[String], start: Array[Int], end: Array[Int]): Int = {

    }
}
```

tab: Rust

```rust
impl Solution {
    pub fn conveyor_belt(matrix: Vec<String>, start: Vec<i32>, end: Vec<i32>) -> i32 {

    }
}
```

tab: Racket

```racket
(define/contract (conveyor-belt matrix start end)
  (-> (listof string?) (listof exact-integer?) (listof exact-integer?) exact-integer?)

  )
```

tab: Erlang

```erlang
-spec conveyor_belt(Matrix :: [unicode:unicode_binary()], Start :: [integer()], End :: [integer()]) -> integer().
conveyor_belt(Matrix, Start, End) ->
  .
```

tab: Elixir

```elixir
defmodule Solution do
  @spec conveyor_belt(matrix :: [String.t], start :: [integer], end :: [integer]) :: integer
  def conveyor_belt(matrix, start, end) do

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
          
