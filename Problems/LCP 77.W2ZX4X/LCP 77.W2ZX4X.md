---
tags:
  - leetcode/problem
questionId: LCP 77
title: 符文储备
translatedTitle: 符文储备
titleSlug: W2ZX4X
aliases:
  - 符文储备
  - W2ZX4X
  - 符文储备
lcLinks:
  - https://leetcode.cn/problems/W2ZX4X/
lcTopics: []
lcDifficulty: Easy
lcAcRate: 68.5%
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

**Nav:** << previous: [[LCP 76.1ybDKD]] | next: [[LCP 78.Nsibyl]] >>

---

## Description

~~~tabs
tab: English

No description

---

[submissions](https://leetcode.com/problems/W2ZX4X/submissions/) | [solutions](https://leetcode.com/problems/W2ZX4X/solutions/)


tab: 中文

远征队在出发前需要携带一些「符文」，作为后续的冒险储备。`runes[i]` 表示第 `i` 枚符文的魔力值。

他们将从中选取若干符文进行携带，并对这些符文进行重新排列，以确保任意相邻的两块符文之间的魔力值相差不超过 `1`。

请返回他们能够携带的符文 **最大数量**。

**示例 1：**
>输入：`runes = [1,3,5,4,1,7]`
>
>输出：`3`
>
>解释：最佳的选择方案为[3,5,4]
>将其排列为 [3,4,5] 后，任意相邻的两块符文魔力值均不超过 `1`，携带数量为 `3`
>其他满足条件的方案为 [1,1] 和 [7]，数量均小于 3。
>因此返回可携带的最大数量 `3`。

**示例 2：**
>输入：`runes = [1,1,3,3,2,4]`
>
>输出：`6`
>
>解释：排列为 [1,1,2,3,3,4]，可携带所有的符文

**提示：**
- `1 <= runes.length <= 10^4`
- `0 <= runes[i] <= 10^4`


---

[提交记录](https://leetcode.cn/problems/W2ZX4X/submissions/) | [题解](https://leetcode.cn/problems/W2ZX4X/solution/)


~~~

## Code Snippets

~~~tabs
tab: C++

```cpp
class Solution {
public:
    int runeReserve(vector<int>& runes) {

    }
};
```

tab: Java

```java
class Solution {
    public int runeReserve(int[] runes) {

    }
}
```

tab: Python

```python
class Solution(object):
    def runeReserve(self, runes):
        """
        :type runes: List[int]
        :rtype: int
        """
```

tab: Python3

```python
class Solution:
    def runeReserve(self, runes: List[int]) -> int:
```

tab: C

```c
int runeReserve(int* runes, int runesSize){

}
```

tab: C#

```csharp
public class Solution {
    public int RuneReserve(int[] runes) {

    }
}
```

tab: JavaScript

```javascript
/**
 * @param {number[]} runes
 * @return {number}
 */
var runeReserve = function(runes) {

};
```

tab: TypeScript

```typescript
function runeReserve(runes: number[]): number {

};
```

tab: PHP

```php
class Solution {

    /**
     * @param Integer[] $runes
     * @return Integer
     */
    function runeReserve($runes) {

    }
}
```

tab: Swift

```swift
class Solution {
    func runeReserve(_ runes: [Int]) -> Int {

    }
}
```

tab: Kotlin

```kotlin
class Solution {
    fun runeReserve(runes: IntArray): Int {

    }
}
```

tab: Dart

```dart
class Solution {
  int runeReserve(List<int> runes) {

  }
}
```

tab: Go

```go
func runeReserve(runes []int) int {

}
```

tab: Ruby

```ruby
# @param {Integer[]} runes
# @return {Integer}
def rune_reserve(runes)

end
```

tab: Scala

```scala
object Solution {
    def runeReserve(runes: Array[Int]): Int = {

    }
}
```

tab: Rust

```rust
impl Solution {
    pub fn rune_reserve(runes: Vec<i32>) -> i32 {

    }
}
```

tab: Racket

```racket
(define/contract (rune-reserve runes)
  (-> (listof exact-integer?) exact-integer?)

  )
```

tab: Erlang

```erlang
-spec rune_reserve(Runes :: [integer()]) -> integer().
rune_reserve(Runes) ->
  .
```

tab: Elixir

```elixir
defmodule Solution do
  @spec rune_reserve(runes :: [integer]) :: integer
  def rune_reserve(runes) do

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
          
