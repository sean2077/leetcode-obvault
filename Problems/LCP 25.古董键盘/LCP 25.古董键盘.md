---
tags:
  - leetcode/problem
questionId: LCP 25
title: 古董键盘
translatedTitle: 古董键盘
titleSlug: Uh984O
aliases:
  - 古董键盘
  - Uh984O
  - 古董键盘
lcLinks:
  - https://leetcode.cn/problems/Uh984O/
lcTopics:
  - '[[math]]'
  - '[[dynamic-programming]]'
  - '[[combinatorics]]'
lcDifficulty: Hard
lcAcRate: 38.5%
similarQuestions: []
grade: ⭐⭐⭐⭐⭐
likes: 37
dislikes: 0
favorites: []
solutions: []
notes: []
---

**Nav:** << previous: [[LCP 24.数字游戏]] | next: [[LCP 26.导航装置]] >>

---

## Description

~~~tabs
tab: English

No description

---

[submissions](https://leetcode.com/problems/Uh984O/submissions/) | [solutions](https://leetcode.com/problems/Uh984O/solutions/)


tab: 中文

小扣在秋日市集购买了一个古董键盘。由于古董键盘年久失修，键盘上只有 26 个字母 **a~z** 可以按下，且每个字母最多仅能被按 `k` 次。

小扣随机按了 `n` 次按键，请返回小扣总共有可能按出多少种内容。由于数字较大，最终答案需要对 1000000007 (1e9 + 7) 取模。


**示例 1：**
>输入：`k = 1, n = 1`
> 
>输出：`26`
> 
>解释：由于只能按一次按键，所有可能的字符串为 "a", "b", ... "z" 

**示例 2：**
>输入：`k = 1, n = 2`
> 
>输出：`650`
> 
>解释：由于只能按两次按键，且每个键最多只能按一次，所有可能的字符串（按字典序排序）为 "ab", "ac", ... "zy" 

**提示：**
- `1 <= k <= 5`
- `1 <= n <= 26*k`
 



---

[提交记录](https://leetcode.cn/problems/Uh984O/submissions/) | [题解](https://leetcode.cn/problems/Uh984O/solution/)


~~~

## Code Snippets

~~~tabs
tab: C++

```cpp
class Solution {
public:
    int keyboard(int k, int n) {

    }
};
```

tab: Java

```java
class Solution {
    public int keyboard(int k, int n) {

    }
}
```

tab: Python

```python
class Solution(object):
    def keyboard(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: int
        """
```

tab: Python3

```python
class Solution:
    def keyboard(self, k: int, n: int) -> int:
```

tab: C

```c


int keyboard(int k, int n){

}
```

tab: C#

```csharp
public class Solution {
    public int Keyboard(int k, int n) {

    }
}
```

tab: JavaScript

```javascript
/**
 * @param {number} k
 * @param {number} n
 * @return {number}
 */
var keyboard = function(k, n) {

};
```

tab: TypeScript

```typescript
function keyboard(k: number, n: number): number {

};
```

tab: PHP

```php
class Solution {

    /**
     * @param Integer $k
     * @param Integer $n
     * @return Integer
     */
    function keyboard($k, $n) {

    }
}
```

tab: Swift

```swift
class Solution {
    func keyboard(_ k: Int, _ n: Int) -> Int {

    }
}
```

tab: Kotlin

```kotlin
class Solution {
    fun keyboard(k: Int, n: Int): Int {

    }
}
```

tab: Dart

```dart
class Solution {
  int keyboard(int k, int n) {

  }
}
```

tab: Go

```go
func keyboard(k int, n int) int {

}
```

tab: Ruby

```ruby
# @param {Integer} k
# @param {Integer} n
# @return {Integer}
def keyboard(k, n)

end
```

tab: Scala

```scala
object Solution {
    def keyboard(k: Int, n: Int): Int = {

    }
}
```

tab: Rust

```rust
impl Solution {
    pub fn keyboard(k: i32, n: i32) -> i32 {

    }
}
```

tab: Racket

```racket
(define/contract (keyboard k n)
  (-> exact-integer? exact-integer? exact-integer?)

  )
```

tab: Erlang

```erlang
-spec keyboard(K :: integer(), N :: integer()) -> integer().
keyboard(K, N) ->
  .
```

tab: Elixir

```elixir
defmodule Solution do
  @spec keyboard(k :: integer, n :: integer) :: integer
  def keyboard(k, n) do

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
          
