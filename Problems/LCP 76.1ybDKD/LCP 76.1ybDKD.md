---
tags:
  - leetcode/problem
questionId: LCP 76
title: 魔法棋盘
translatedTitle: 魔法棋盘
titleSlug: 1ybDKD
aliases:
  - 魔法棋盘
  - 1ybDKD
  - 魔法棋盘
lcLinks:
  - https://leetcode.cn/problems/1ybDKD/
lcTopics: []
lcDifficulty: Hard
lcAcRate: 38.6%
similarQuestions: []
grade: ⭐⭐⭐⭐⭐
likes: 6
dislikes: 0
favorites: []
solutions: []
notes: []
cssclasses: []
created: 2024-08-13 00:28
updated:
---

**Nav:** << previous: [[LCP 75.rdmXM7]] | next: [[LCP 77.W2ZX4X]] >>

---

## Description

~~~tabs
tab: English

No description

---

[submissions](https://leetcode.com/problems/1ybDKD/submissions/) | [solutions](https://leetcode.com/problems/1ybDKD/solutions/)


tab: 中文

在大小为 `n * m` 的棋盘中，有两种不同的棋子：黑色，红色。当两颗颜色不同的棋子同时满足以下两种情况时，将会产生魔法共鸣：
- 两颗异色棋子在同一行或者同一列
- 两颗异色棋子之间恰好只有一颗棋子
    > 注：异色棋子之间可以有空位

由于棋盘上被施加了魔法禁制，棋盘上的部分格子变成问号。`chessboard[i][j]` 表示棋盘第 `i` 行 `j` 列的状态：
- 若为 `.` ，表示当前格子确定为空
- 若为 `B` ，表示当前格子确定为 黑棋
- 若为 `R` ，表示当前格子确定为 红棋
- 若为 `?` ，表示当前格子待定

现在，探险家小扣的任务是确定所有问号位置的状态（留空/放黑棋/放红棋），使最终的棋盘上，任意两颗棋子间都 **无法** 产生共鸣。请返回可以满足上述条件的放置方案数量。

**示例1：**
> 输入：`n = 3, m = 3, chessboard = ["..R","..B","?R?"]`
>
> 输出：`5`
>
> 解释：给定的棋盘如图：
>![image.png](https://pic.leetcode.cn/1681714583-unbRox-image.png){:height=150px}
> 所有符合题意的最终局面如图：
>![image.png](https://pic.leetcode.cn/1681714596-beaOHK-image.png){:height=150px}

**示例2：**
> 输入：`n = 3, m = 3, chessboard = ["?R?","B?B","?R?"]`
>
> 输出：`105`

**提示：**
- `n == chessboard.length`
- `m == chessboard[i].length`
- `1 <= n*m <= 30`
- `chessboard` 中仅包含 `"."、"B"、"R"、"?"`

---

[提交记录](https://leetcode.cn/problems/1ybDKD/submissions/) | [题解](https://leetcode.cn/problems/1ybDKD/solution/)


~~~

## Code Snippets

~~~tabs
tab: C++

```cpp
class Solution {
public:
    long long getSchemeCount(int n, int m, vector<string>& chessboard) {

    }
};
```

tab: Java

```java
class Solution {
    public long getSchemeCount(int n, int m, String[] chessboard) {

    }
}
```

tab: Python

```python
class Solution(object):
    def getSchemeCount(self, n, m, chessboard):
        """
        :type n: int
        :type m: int
        :type chessboard: List[str]
        :rtype: int
        """
```

tab: Python3

```python
class Solution:
    def getSchemeCount(self, n: int, m: int, chessboard: List[str]) -> int:
```

tab: C

```c
long long getSchemeCount(int n, int m, char** chessboard, int chessboardSize){

}
```

tab: C#

```csharp
public class Solution {
    public long GetSchemeCount(int n, int m, string[] chessboard) {

    }
}
```

tab: JavaScript

```javascript
/**
 * @param {number} n
 * @param {number} m
 * @param {string[]} chessboard
 * @return {number}
 */
var getSchemeCount = function(n, m, chessboard) {

};
```

tab: TypeScript

```typescript
function getSchemeCount(n: number, m: number, chessboard: string[]): number {

};
```

tab: PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $m
     * @param String[] $chessboard
     * @return Integer
     */
    function getSchemeCount($n, $m, $chessboard) {

    }
}
```

tab: Swift

```swift
class Solution {
    func getSchemeCount(_ n: Int, _ m: Int, _ chessboard: [String]) -> Int {

    }
}
```

tab: Kotlin

```kotlin
class Solution {
    fun getSchemeCount(n: Int, m: Int, chessboard: Array<String>): Long {

    }
}
```

tab: Dart

```dart
class Solution {
  int getSchemeCount(int n, int m, List<String> chessboard) {

  }
}
```

tab: Go

```go
func getSchemeCount(n int, m int, chessboard []string) int64 {

}
```

tab: Ruby

```ruby
# @param {Integer} n
# @param {Integer} m
# @param {String[]} chessboard
# @return {Integer}
def get_scheme_count(n, m, chessboard)

end
```

tab: Scala

```scala
object Solution {
    def getSchemeCount(n: Int, m: Int, chessboard: Array[String]): Long = {

    }
}
```

tab: Rust

```rust
impl Solution {
    pub fn get_scheme_count(n: i32, m: i32, chessboard: Vec<String>) -> i64 {

    }
}
```

tab: Racket

```racket
(define/contract (get-scheme-count n m chessboard)
  (-> exact-integer? exact-integer? (listof string?) exact-integer?)

  )
```

tab: Erlang

```erlang
-spec get_scheme_count(N :: integer(), M :: integer(), Chessboard :: [unicode:unicode_binary()]) -> integer().
get_scheme_count(N, M, Chessboard) ->
  .
```

tab: Elixir

```elixir
defmodule Solution do
  @spec get_scheme_count(n :: integer, m :: integer, chessboard :: [String.t]) :: integer
  def get_scheme_count(n, m, chessboard) do

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
          
