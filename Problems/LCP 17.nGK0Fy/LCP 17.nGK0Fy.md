---
tags:
  - leetcode/problem
questionId: LCP 17
title: 速算机器人
translatedTitle: 速算机器人
titleSlug: nGK0Fy
aliases:
  - 速算机器人
  - nGK0Fy
  - 速算机器人
lcLink: https://leetcode.com/problems/nGK0Fy/
lcTopics:
  - '[[math]]'
  - '[[string]]'
  - '[[simulation]]'
lcDifficulty: Easy
lcAcRate: 79.9%
similarQuestions: []
grade: ⭐⭐⭐⭐⭐
likes: 47
dislikes: 0
favorites: []
solutions: []
notes: []
cssclasses: []
created: 2024-08-13 00:10
updated:
---

**Nav:** << previous: [[LCP 16.you-le-yuan-de-you-lan-ji-hua]] | next: [[LCP 18.2vYnGI]] >>

---

## Description

~~~tabs
tab: English

No description

---

[submissions](https://leetcode.com/problems/nGK0Fy/submissions/) | [solutions](https://leetcode.com/problems/nGK0Fy/solutions/)


tab: 中文

小扣在秋日市集发现了一款速算机器人。店家对机器人说出两个数字（记作 `x` 和 `y`），请小扣说出计算指令：
- `"A"` 运算：使 `x = 2 * x + y`；
- `"B"` 运算：使 `y = 2 * y + x`。

在本次游戏中，店家说出的数字为 `x = 1` 和 `y = 0`，小扣说出的计算指令记作仅由大写字母 `A`、`B` 组成的字符串 `s`，字符串中字符的顺序表示计算顺序，请返回最终 `x` 与 `y` 的和为多少。

**示例 1：**
>输入：`s = "AB"`
> 
>输出：`4`
> 
>解释：
>经过一次 A 运算后，x = 2, y = 0。
>再经过一次 B 运算，x = 2, y = 2。
>最终 x 与 y 之和为 4。

**提示：**
- `0 <= s.length <= 10`
- `s` 由 `'A'` 和 `'B'` 组成




---

[提交记录](https://leetcode.cn/problems/nGK0Fy/submissions/) | [题解](https://leetcode.cn/problems/nGK0Fy/solution/)


~~~

## Code Snippets

~~~tabs
tab: C++

```cpp
class Solution {
public:
    int calculate(string s) {

    }
};
```

tab: Java

```java
class Solution {
    public int calculate(String s) {

    }
}
```

tab: Python

```python
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
```

tab: Python3

```python
class Solution:
    def calculate(self, s: str) -> int:
```

tab: C

```c


int calculate(char* s){

}
```

tab: C#

```csharp
public class Solution {
    public int Calculate(string s) {

    }
}
```

tab: JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var calculate = function(s) {

};
```

tab: TypeScript

```typescript
function calculate(s: string): number {

};
```

tab: PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function calculate($s) {

    }
}
```

tab: Swift

```swift
class Solution {
    func calculate(_ s: String) -> Int {

    }
}
```

tab: Kotlin

```kotlin
class Solution {
    fun calculate(s: String): Int {

    }
}
```

tab: Dart

```dart
class Solution {
  int calculate(String s) {

  }
}
```

tab: Go

```go
func calculate(s string) int {

}
```

tab: Ruby

```ruby
# @param {String} s
# @return {Integer}
def calculate(s)

end
```

tab: Scala

```scala
object Solution {
    def calculate(s: String): Int = {

    }
}
```

tab: Rust

```rust
impl Solution {
    pub fn calculate(s: String) -> i32 {

    }
}
```

tab: Racket

```racket
(define/contract (calculate s)
  (-> string? exact-integer?)

  )
```

tab: Erlang

```erlang
-spec calculate(S :: unicode:unicode_binary()) -> integer().
calculate(S) ->
  .
```

tab: Elixir

```elixir
defmodule Solution do
  @spec calculate(s :: String.t) :: integer
  def calculate(s) do

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
          
