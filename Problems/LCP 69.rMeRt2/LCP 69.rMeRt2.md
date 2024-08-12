---
tags:
  - leetcode/problem
questionId: LCP 69
title: Hello LeetCode!
translatedTitle: Hello LeetCode!
titleSlug: rMeRt2
aliases:
  - Hello LeetCode!
  - rMeRt2
  - Hello LeetCode!
lcLinks:
  - https://leetcode.cn/problems/rMeRt2/
lcTopics:
  - '[[bit-manipulation]]'
  - '[[array]]'
  - '[[string]]'
  - '[[dynamic-programming]]'
  - '[[bitmask]]'
lcDifficulty: Hard
lcAcRate: 37.2%
similarQuestions: []
grade: ⭐⭐⭐⭐⭐
likes: 19
dislikes: 0
favorites: []
solutions: []
notes: []
cssclasses: []
created: 2024-08-13 00:28
updated:
---

**Nav:** << previous: [[LCP 68.1GxJYY]] | next: [[LCP 70.XxZZjK]] >>

---

## Description

~~~tabs
tab: English

No description

---

[submissions](https://leetcode.com/problems/rMeRt2/submissions/) | [solutions](https://leetcode.com/problems/rMeRt2/solutions/)


tab: 中文

力扣嘉年华同样准备了纪念品展位，参观者只需要集齐 `helloleetcode` 的 `13` 张字母卡片即可获得力扣纪念章。

在展位上有一些由字母卡片拼成的单词，`words[i][j]` 表示第 `i` 个单词的第 `j` 个字母。

你可以从这些单词中取出一些卡片，但每次拿取卡片都需要消耗游戏代币，规则如下：

- 从一个单词中取一个字母所需要的代币数量，为该字母左边和右边字母数量之积

- 可以从一个单词中多次取字母，每个字母仅可被取一次

> 例如：从 `example` 中取出字母 `a`，需要消耗代币 `2*4=8`，字母取出后单词变为 `exmple`；
再从中取出字母 `m`，需要消耗代币 `2*3=6`，字母取出后单词变为 `exple`；

请返回取得 `helloleetcode` 这些字母需要消耗代币的 **最少** 数量。如果无法取得，返回 `-1`。

**注意：**
- 取出字母的顺序没有要求
- 取出的所有字母恰好可以拼成 `helloleetcode` 

**示例 1：**
>输入：`words = ["hold","engineer","cost","level"]`
>
>输出：`5`
>
>解释：最优方法为：
>从 `hold` 依次取出 `h`、`o`、`l`、`d`， 代价均为 `0`
>从 `engineer` 依次取出第 `1` 个 `e` 与最后一个 `e`， 代价为 `0` 和 `5*1=5`
>从 `cost` 取出 `c`、`o`、`t`， 代价均为 `0`
>从 `level` 依次取出 `l`、`l`、`e`、`e`， 代价均为 `0`
>所有字母恰好可以拼成 `helloleetcode`，因此最小的代价为 `5`

**示例 2：**
>输入：`words = ["hello","leetcode"]`
>
>输出：`0`

**提示：**
+ `n == words.length`
+ `m == words[i].length`
+ `1 <= n <= 24`
+ `1 <= m <= 8`
+ `words[i][j]` 仅为小写字母

---

[提交记录](https://leetcode.cn/problems/rMeRt2/submissions/) | [题解](https://leetcode.cn/problems/rMeRt2/solution/)


~~~

## Code Snippets

~~~tabs
tab: C++

```cpp
class Solution {
public:
    int Leetcode(vector<string>& words) {

    }
};
```

tab: Java

```java
class Solution {
    public int Leetcode(String[] words) {

    }
}
```

tab: Python

```python
class Solution(object):
    def Leetcode(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
```

tab: Python3

```python
class Solution:
    def Leetcode(self, words: List[str]) -> int:
```

tab: C

```c


int Leetcode(char** words, int wordsSize){

}
```

tab: C#

```csharp
public class Solution {
    public int Leetcode(string[] words) {

    }
}
```

tab: JavaScript

```javascript
/**
 * @param {string[]} words
 * @return {number}
 */
var Leetcode = function(words) {

};
```

tab: TypeScript

```typescript
function Leetcode(words: string[]): number {

};
```

tab: PHP

```php
class Solution {

    /**
     * @param String[] $words
     * @return Integer
     */
    function Leetcode($words) {

    }
}
```

tab: Swift

```swift
class Solution {
    func Leetcode(_ words: [String]) -> Int {

    }
}
```

tab: Kotlin

```kotlin
class Solution {
    fun Leetcode(words: Array<String>): Int {

    }
}
```

tab: Dart

```dart
class Solution {
  int Leetcode(List<String> words) {

  }
}
```

tab: Go

```go
func Leetcode(words []string) int {

}
```

tab: Ruby

```ruby
# @param {String[]} words
# @return {Integer}
def leetcode(words)

end
```

tab: Scala

```scala
object Solution {
    def Leetcode(words: Array[String]): Int = {

    }
}
```

tab: Rust

```rust
impl Solution {
    pub fn leetcode(words: Vec<String>) -> i32 {

    }
}
```

tab: Racket

```racket
(define/contract (leetcode words)
  (-> (listof string?) exact-integer?)

  )
```

tab: Erlang

```erlang
-spec leetcode(Words :: [unicode:unicode_binary()]) -> integer().
leetcode(Words) ->
  .
```

tab: Elixir

```elixir
defmodule Solution do
  @spec leetcode(words :: [String.t]) :: integer
  def leetcode(words) do

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
          
