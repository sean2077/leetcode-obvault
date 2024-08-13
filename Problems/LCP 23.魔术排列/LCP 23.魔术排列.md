---
tags:
  - leetcode/problem
questionId: LCP 23
title: 魔术排列
translatedTitle: 魔术排列
titleSlug: er94lq
aliases:
  - 魔术排列
  - er94lq
  - 魔术排列
lcLinks:
  - https://leetcode.cn/problems/er94lq/
lcTopics:
  - '[[queue]]'
  - '[[array]]'
  - '[[simulation]]'
lcDifficulty: Medium
lcAcRate: 37.7%
similarQuestions: []
grade: ⭐⭐⭐⭐⭐
likes: 24
dislikes: 0
favorites: []
solutions: []
notes: []
---

**Nav:** << previous: [[LCP 22.黑白方格画]] | next: [[LCP 24.数字游戏]] >>

---

## Description

~~~tabs
tab: English

No description

---

[submissions](https://leetcode.com/problems/er94lq/submissions/) | [solutions](https://leetcode.com/problems/er94lq/solutions/)


tab: 中文

秋日市集上，魔术师邀请小扣与他互动。魔术师的道具为分别写有数字 `1~N` 的 `N` 张卡牌，然后请小扣思考一个 `N` 张卡牌的排列 `target`。

魔术师的目标是找到一个数字 k（k >= 1），使得初始排列顺序为 `1~N` 的卡牌经过特殊的洗牌方式最终变成小扣所想的排列 `target`，特殊的洗牌方式为：
- 第一步，魔术师将当前位于 **偶数位置** 的卡牌（下标自 1 开始），保持 **当前排列顺序** 放在位于 **奇数位置** 的卡牌之前。例如：将当前排列 [1,2,3,4,5] 位于偶数位置的 [2,4] 置于奇数位置的 [1,3,5] 前，排列变为 [2,4,1,3,5]；
- 第二步，若当前卡牌数量小于等于 `k`，则魔术师按排列顺序取走全部卡牌；若当前卡牌数量大于 `k`，则取走前 `k` 张卡牌，剩余卡牌继续重复这两个步骤，直至所有卡牌全部被取走；

卡牌按照魔术师取走顺序构成的新排列为「魔术取数排列」，请返回是否存在这个数字 k 使得「魔术取数排列」恰好就是 `target`，从而让小扣感到大吃一惊。

**示例 1：**
>输入：`target = [2,4,3,1,5]`
>
>输出：`true`
>
>解释：排列 target 长度为 5，初始排列为：1,2,3,4,5。我们选择 k = 2：
>第一次：将当前排列 [1,2,3,4,5] 位于偶数位置的 [2,4] 置于奇数位置的 [1,3,5] 前，排列变为 [2,4,1,3,5]。取走前 2 张卡牌 2,4，剩余 [1,3,5]；
>第二次：将当前排列 [1,3,5] 位于偶数位置的 [3] 置于奇数位置的 [1,5] 前，排列变为 [3,1,5]。取走前 2 张 3,1，剩余 [5]；
>第三次：当前排列为 [5]，全部取出。
>最后，数字按照取出顺序构成的「魔术取数排列」2,4,3,1,5 恰好为 target。

**示例 2：**
>输入：`target = [5,4,3,2,1]`
>
>输出：`false`
>
>解释：无法找到一个数字 k 可以使「魔术取数排列」恰好为 target。


**提示：**
- `1 <= target.length = N <= 5000`
- 题目保证 `target` 是 `1~N` 的一个排列。

---

[提交记录](https://leetcode.cn/problems/er94lq/submissions/) | [题解](https://leetcode.cn/problems/er94lq/solution/)


~~~

## Code Snippets

~~~tabs
tab: C++

```cpp
class Solution {
public:
    bool isMagic(vector<int>& target) {

    }
};
```

tab: Java

```java
class Solution {
    public boolean isMagic(int[] target) {

    }
}
```

tab: Python

```python
class Solution(object):
    def isMagic(self, target):
        """
        :type target: List[int]
        :rtype: bool
        """
```

tab: Python3

```python
class Solution:
    def isMagic(self, target: List[int]) -> bool:
```

tab: C

```c


bool isMagic(int* target, int targetSize){

}
```

tab: C#

```csharp
public class Solution {
    public bool IsMagic(int[] target) {

    }
}
```

tab: JavaScript

```javascript
/**
 * @param {number[]} target
 * @return {boolean}
 */
var isMagic = function(target) {

};
```

tab: PHP

```php
class Solution {

    /**
     * @param Integer[] $target
     * @return Boolean
     */
    function isMagic($target) {

    }
}
```

tab: Swift

```swift
class Solution {
    func isMagic(_ target: [Int]) -> Bool {

    }
}
```

tab: Kotlin

```kotlin
class Solution {
    fun isMagic(target: IntArray): Boolean {

    }
}
```

tab: Dart

```dart
class Solution {
  bool isMagic(List<int> target) {

  }
}
```

tab: Go

```go
func isMagic(target []int) bool {

}
```

tab: Ruby

```ruby
# @param {Integer[]} target
# @return {Boolean}
def is_magic(target)

end
```

tab: Scala

```scala
object Solution {
    def isMagic(target: Array[Int]): Boolean = {

    }
}
```

tab: Rust

```rust
impl Solution {
    pub fn is_magic(target: Vec<i32>) -> bool {

    }
}
```

tab: Racket

```racket
(define/contract (is-magic target)
  (-> (listof exact-integer?) boolean?)

  )
```

tab: Erlang

```erlang
-spec is_magic(Target :: [integer()]) -> boolean().
is_magic(Target) ->
  .
```

tab: Elixir

```elixir
defmodule Solution do
  @spec is_magic(target :: [integer]) :: boolean
  def is_magic(target) do

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
          
