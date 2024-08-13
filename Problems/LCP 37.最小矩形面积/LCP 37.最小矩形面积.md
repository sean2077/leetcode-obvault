---
tags:
  - leetcode/problem
questionId: LCP 37
title: 最小矩形面积
translatedTitle: 最小矩形面积
titleSlug: zui-xiao-ju-xing-mian-ji
aliases:
  - 最小矩形面积
  - zui-xiao-ju-xing-mian-ji
  - 最小矩形面积
lcLinks:
  - https://leetcode.cn/problems/zui-xiao-ju-xing-mian-ji/
lcTopics:
  - '[[greedy]]'
  - '[[geometry]]'
  - '[[array]]'
  - '[[math]]'
  - '[[combinatorics]]'
  - '[[sorting]]'
lcDifficulty: Hard
lcAcRate: 24.8%
similarQuestions: []
grade: ⭐⭐⭐⭐⭐
likes: 25
dislikes: 0
favorites: []
solutions: []
notes: []
---

**Nav:** << previous: [[LCP 36.最多牌组数]] | next: [[LCP 38.守卫城堡]] >>

---

## Description

~~~tabs
tab: English

No description

---

[submissions](https://leetcode.com/problems/zui-xiao-ju-xing-mian-ji/submissions/) | [solutions](https://leetcode.com/problems/zui-xiao-ju-xing-mian-ji/solutions/)


tab: 中文

二维平面上有 $N$ 条直线，形式为 `y = kx + b`，其中 `k`、`b`为整数 且 `k > 0`。所有直线以 `[k,b]` 的形式存于二维数组 `lines` 中，不存在重合的两条直线。两两直线之间可能存在一个交点，最多会有 $C_N^2$ 个交点。我们用一个平行于坐标轴的矩形覆盖所有的交点，请问这个矩形最小面积是多少。若直线之间无交点、仅有一个交点或所有交点均在同一条平行坐标轴的直线上，则返回0。

注意：返回结果是浮点数，与标准答案 **绝对误差或相对误差** 在 10^-4 以内的结果都被视为正确结果


**示例 1：**
> 输入：`lines = [[2,3],[3,0],[4,1]]`
>
> 输出：`48.00000`
>
> 解释：三条直线的三个交点为 (3, 9) (1, 5) 和 (-1, -3)。最小覆盖矩形左下角为 (-1, -3) 右上角为 (3,9)，面积为 48


**示例 2：**
> 输入：`lines = [[1,1],[2,3]]`
>
> 输出：`0.00000`
>
> 解释：仅有一个交点 (-2，-1）


**限制：**
+ `1 <= lines.length <= 10^5 且 lines[i].length == 2`
+ `1 <= lines[0] <= 10000`
+ `-10000 <= lines[1] <= 10000`
+ `与标准答案绝对误差或相对误差在 10^-4 以内的结果都被视为正确结果`

---

[提交记录](https://leetcode.cn/problems/zui-xiao-ju-xing-mian-ji/submissions/) | [题解](https://leetcode.cn/problems/zui-xiao-ju-xing-mian-ji/solution/)


~~~

## Code Snippets

~~~tabs
tab: C++

```cpp
class Solution {
public:
    double minRecSize(vector<vector<int>>& lines) {

    }
};
```

tab: Java

```java
class Solution {
    public double minRecSize(int[][] lines) {

    }
}
```

tab: Python

```python
class Solution(object):
    def minRecSize(self, lines):
        """
        :type lines: List[List[int]]
        :rtype: float
        """
```

tab: Python3

```python
class Solution:
    def minRecSize(self, lines: List[List[int]]) -> float:
```

tab: C

```c


double minRecSize(int** lines, int linesSize, int* linesColSize){

}

```

tab: C#

```csharp
public class Solution {
    public double MinRecSize(int[][] lines) {

    }
}
```

tab: JavaScript

```javascript
/**
 * @param {number[][]} lines
 * @return {number}
 */
var minRecSize = function(lines) {

};
```

tab: PHP

```php
class Solution {

    /**
     * @param Integer[][] $lines
     * @return Float
     */
    function minRecSize($lines) {

    }
}
```

tab: Swift

```swift
class Solution {
    func minRecSize(_ lines: [[Int]]) -> Double {

    }
}
```

tab: Kotlin

```kotlin
class Solution {
    fun minRecSize(lines: Array<IntArray>): Double {

    }
}
```

tab: Dart

```dart
class Solution {
  double minRecSize(List<List<int>> lines) {

  }
}
```

tab: Go

```go
func minRecSize(lines [][]int) float64 {

}
```

tab: Ruby

```ruby
# @param {Integer[][]} lines
# @return {Float}
def min_rec_size(lines)

end
```

tab: Scala

```scala
object Solution {
    def minRecSize(lines: Array[Array[Int]]): Double = {

    }
}
```

tab: Rust

```rust
impl Solution {
    pub fn min_rec_size(lines: Vec<Vec<i32>>) -> f64 {

    }
}
```

tab: Racket

```racket
(define/contract (min-rec-size lines)
  (-> (listof (listof exact-integer?)) flonum?)

  )
```

tab: Erlang

```erlang
-spec min_rec_size(Lines :: [[integer()]]) -> float().
min_rec_size(Lines) ->
  .
```

tab: Elixir

```elixir
defmodule Solution do
  @spec min_rec_size(lines :: [[integer]]) :: float
  def min_rec_size(lines) do

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
          
