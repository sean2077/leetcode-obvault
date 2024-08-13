---
tags:
  - leetcode/problem
questionId: LCP 19
title: 秋叶收藏集
translatedTitle: 秋叶收藏集
titleSlug: UlBDOe
aliases:
  - 秋叶收藏集
  - UlBDOe
  - 秋叶收藏集
lcLinks:
  - https://leetcode.cn/problems/UlBDOe/
lcTopics:
  - '[[string]]'
  - '[[dynamic-programming]]'
lcDifficulty: Medium
lcAcRate: 51.7%
similarQuestions: []
grade: ⭐⭐⭐⭐⭐
likes: 238
dislikes: 0
favorites: []
solutions: []
notes: []
---

**Nav:** << previous: [[LCP 18.早餐组合]] | next: [[LCP 20.快速公交]] >>

---

## Description

~~~tabs
tab: English

No description

---

[submissions](https://leetcode.com/problems/UlBDOe/submissions/) | [solutions](https://leetcode.com/problems/UlBDOe/solutions/)


tab: 中文

小扣出去秋游，途中收集了一些红叶和黄叶，他利用这些叶子初步整理了一份秋叶收藏集 `leaves`， 字符串 `leaves` 仅包含小写字符 `r` 和 `y`， 其中字符 `r` 表示一片红叶，字符 `y` 表示一片黄叶。
出于美观整齐的考虑，小扣想要将收藏集中树叶的排列调整成「红、黄、红」三部分。每部分树叶数量可以不相等，但均需大于等于 1。每次调整操作，小扣可以将一片红叶替换成黄叶或者将一片黄叶替换成红叶。请问小扣最少需要多少次调整操作才能将秋叶收藏集调整完毕。

**示例 1：**
>输入：`leaves = "rrryyyrryyyrr"`
>
>输出：`2`
>
>解释：调整两次，将中间的两片红叶替换成黄叶，得到 "rrryyyyyyyyrr"

**示例 2：**
>输入：`leaves = "ryr"`
>
>输出：`0`
>
>解释：已符合要求，不需要额外操作

**提示：**
- `3 <= leaves.length <= 10^5`
- `leaves` 中只包含字符 `'r'` 和字符 `'y'`

---

[提交记录](https://leetcode.cn/problems/UlBDOe/submissions/) | [题解](https://leetcode.cn/problems/UlBDOe/solution/)


~~~

## Code Snippets

~~~tabs
tab: C++

```cpp
class Solution {
public:
    int minimumOperations(string leaves) {

    }
};
```

tab: Java

```java
class Solution {
    public int minimumOperations(String leaves) {

    }
}
```

tab: Python

```python
class Solution(object):
    def minimumOperations(self, leaves):
        """
        :type leaves: str
        :rtype: int
        """
```

tab: Python3

```python
class Solution:
    def minimumOperations(self, leaves: str) -> int:
```

tab: C

```c


int minimumOperations(char* leaves){

}
```

tab: C#

```csharp
public class Solution {
    public int MinimumOperations(string leaves) {

    }
}
```

tab: JavaScript

```javascript
/**
 * @param {string} leaves
 * @return {number}
 */
var minimumOperations = function(leaves) {

};
```

tab: TypeScript

```typescript
function minimumOperations(leaves: string): number {

};
```

tab: PHP

```php
class Solution {

    /**
     * @param String $leaves
     * @return Integer
     */
    function minimumOperations($leaves) {

    }
}
```

tab: Swift

```swift
class Solution {
    func minimumOperations(_ leaves: String) -> Int {

    }
}
```

tab: Kotlin

```kotlin
class Solution {
    fun minimumOperations(leaves: String): Int {

    }
}
```

tab: Dart

```dart
class Solution {
  int minimumOperations(String leaves) {

  }
}
```

tab: Go

```go
func minimumOperations(leaves string) int {

}
```

tab: Ruby

```ruby
# @param {String} leaves
# @return {Integer}
def minimum_operations(leaves)

end
```

tab: Scala

```scala
object Solution {
    def minimumOperations(leaves: String): Int = {

    }
}
```

tab: Rust

```rust
impl Solution {
    pub fn minimum_operations(leaves: String) -> i32 {

    }
}
```

tab: Racket

```racket
(define/contract (minimum-operations leaves)
  (-> string? exact-integer?)

  )
```

tab: Erlang

```erlang
-spec minimum_operations(Leaves :: unicode:unicode_binary()) -> integer().
minimum_operations(Leaves) ->
  .
```

tab: Elixir

```elixir
defmodule Solution do
  @spec minimum_operations(leaves :: String.t) :: integer
  def minimum_operations(leaves) do

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
          
