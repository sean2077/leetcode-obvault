---
tags:
  - leetcode/problem
questionId: LCS 03
title: 主题空间
translatedTitle: 主题空间
titleSlug: YesdPw
aliases:
  - 主题空间
  - YesdPw
  - 主题空间
lcLink: https://leetcode.com/problems/YesdPw/
lcTopics:
  - '[[depth-first-search]]'
  - '[[breadth-first-search]]'
  - '[[union-find]]'
  - '[[array]]'
  - '[[matrix]]'
lcDifficulty: Medium
lcAcRate: 41.1%
similarQuestions: []
grade: ⭐⭐⭐⭐⭐
likes: 14
dislikes: 0
favorites: []
solutions: []
notes: []
cssclasses: []
created: 2024-08-13 00:10
updated:
---

**Nav:** << previous: [[LCS 02.WqXACV]] | next: [[面试题 01.01.is-unique-lcci]] >>

---

## Description

~~~tabs
tab: English

No description

---

[submissions](https://leetcode.com/problems/YesdPw/submissions/) | [solutions](https://leetcode.com/problems/YesdPw/solutions/)


tab: 中文

「以扣会友」线下活动所在场地由若干主题空间与走廊组成，场地的地图记作由一维字符串型数组 `grid`，字符串中仅包含 `"0"～"5"` 这 6 个字符。地图上每一个字符代表面积为 1 的区域，其中 `"0"` 表示走廊，其他字符表示主题空间。相同且连续（连续指上、下、左、右四个方向连接）的字符组成同一个主题空间。

假如整个 `grid` 区域的外侧均为走廊。请问，不与走廊直接相邻的主题空间的最大面积是多少？如果不存在这样的空间请返回 `0`。

**示例 1:**
>输入：`grid = ["110","231","221"]`
>
>输出：`1`
>
>解释：4 个主题空间中，只有 1 个不与走廊相邻，面积为 1。
>![image.png](https://pic.leetcode-cn.com/1613708145-rscctN-image.png)


**示例 2:**
>输入：`grid = ["11111100000","21243101111","21224101221","11111101111"]`
>
>输出：`3`
>
>解释：8 个主题空间中，有 5 个不与走廊相邻，面积分别为 3、1、1、1、2，最大面积为 3。
>![image.png](https://pic.leetcode-cn.com/1613707985-KJyiXJ-image.png)


**提示：**
- `1 <= grid.length <= 500`
- `1 <= grid[i].length <= 500`
- `grid[i][j]` 仅可能是 `"0"～"5"`



---

[提交记录](https://leetcode.cn/problems/YesdPw/submissions/) | [题解](https://leetcode.cn/problems/YesdPw/solution/)


~~~

## Code Snippets

~~~tabs
tab: C++

```cpp
class Solution {
public:
    int largestArea(vector<string>& grid) {

    }
};
```

tab: Java

```java
class Solution {
    public int largestArea(String[] grid) {

    }
}
```

tab: Python

```python
class Solution(object):
    def largestArea(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
```

tab: Python3

```python
class Solution:
    def largestArea(self, grid: List[str]) -> int:
```

tab: C

```c


int largestArea(char** grid, int gridSize){

}
```

tab: C#

```csharp
public class Solution {
    public int LargestArea(string[] grid) {

    }
}
```

tab: JavaScript

```javascript
/**
 * @param {string[]} grid
 * @return {number}
 */
var largestArea = function(grid) {

};
```

tab: TypeScript

```typescript
function largestArea(grid: string[]): number {

};
```

tab: PHP

```php
class Solution {

    /**
     * @param String[] $grid
     * @return Integer
     */
    function largestArea($grid) {

    }
}
```

tab: Swift

```swift
class Solution {
    func largestArea(_ grid: [String]) -> Int {

    }
}
```

tab: Kotlin

```kotlin
class Solution {
    fun largestArea(grid: Array<String>): Int {

    }
}
```

tab: Dart

```dart
class Solution {
  int largestArea(List<String> grid) {

  }
}
```

tab: Go

```go
func largestArea(grid []string) int {

}
```

tab: Ruby

```ruby
# @param {String[]} grid
# @return {Integer}
def largest_area(grid)

end
```

tab: Scala

```scala
object Solution {
    def largestArea(grid: Array[String]): Int = {

    }
}
```

tab: Rust

```rust
impl Solution {
    pub fn largest_area(grid: Vec<String>) -> i32 {

    }
}
```

tab: Racket

```racket
(define/contract (largest-area grid)
  (-> (listof string?) exact-integer?)

  )
```

tab: Erlang

```erlang
-spec largest_area(Grid :: [unicode:unicode_binary()]) -> integer().
largest_area(Grid) ->
  .
```

tab: Elixir

```elixir
defmodule Solution do
  @spec largest_area(grid :: [String.t]) :: integer
  def largest_area(grid) do

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
          
