---
tags:
  - leetcode/problem
questionId: LCS 01
title: 下载插件
translatedTitle: 下载插件
titleSlug: Ju9Xwi
aliases:
  - 下载插件
  - Ju9Xwi
  - 下载插件
lcLinks:
  - https://leetcode.cn/problems/Ju9Xwi/
lcTopics:
  - '[[greedy]]'
  - '[[math]]'
  - '[[dynamic-programming]]'
lcDifficulty: Easy
lcAcRate: 53.6%
similarQuestions: []
grade: ⭐⭐⭐⭐⭐
likes: 48
dislikes: 0
favorites: []
solutions: []
notes: []
---

**Nav:** << previous: [[LCR 194.二叉树的最近公共祖先]] | next: [[LCS 02.完成一半题目]] >>

---

## Description

~~~tabs
tab: English

No description

---

[submissions](https://leetcode.com/problems/Ju9Xwi/submissions/) | [solutions](https://leetcode.com/problems/Ju9Xwi/solutions/)


tab: 中文

小扣打算给自己的 **VS code** 安装使用插件，初始状态下带宽每分钟可以完成 `1` 个插件的下载。假定每分钟选择以下两种策略之一:
- 使用当前带宽下载插件
- 将带宽加倍（下载插件数量随之加倍）

请返回小扣完成下载 `n` 个插件最少需要多少分钟。

注意：实际的下载的插件数量可以超过 `n` 个


**示例 1：**
>输入：`n = 2`
>
>输出：`2`
>
>解释：
> 以下两个方案，都能实现 2 分钟内下载 2 个插件
>- 方案一：第一分钟带宽加倍，带宽可每分钟下载 2 个插件；第二分钟下载 2 个插件
>- 方案二：第一分钟下载 1 个插件，第二分钟下载 1 个插件

**示例 2：**
>输入：`n = 4`
>
>输出：`3`
>
>解释：
> 最少需要 3 分钟可完成 4 个插件的下载，以下是其中一种方案:
> 第一分钟带宽加倍，带宽可每分钟下载 2 个插件;
> 第二分钟下载 2 个插件;
> 第三分钟下载 2 个插件。



**提示：**
- `1 <= n <= 10^5`


---

[提交记录](https://leetcode.cn/problems/Ju9Xwi/submissions/) | [题解](https://leetcode.cn/problems/Ju9Xwi/solution/)


~~~

## Code Snippets

~~~tabs
tab: C++

```cpp
class Solution {
public:
    int leastMinutes(int n) {

    }
};
```

tab: Java

```java
class Solution {
    public int leastMinutes(int n) {

    }
}
```

tab: Python

```python
class Solution(object):
    def leastMinutes(self, n):
        """
        :type n: int
        :rtype: int
        """
```

tab: Python3

```python
class Solution:
    def leastMinutes(self, n: int) -> int:
```

tab: C

```c


int leastMinutes(int n){

}
```

tab: C#

```csharp
public class Solution {
    public int LeastMinutes(int n) {

    }
}
```

tab: JavaScript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var leastMinutes = function(n) {

};
```

tab: TypeScript

```typescript
function leastMinutes(n: number): number {

};
```

tab: PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function leastMinutes($n) {

    }
}
```

tab: Swift

```swift
class Solution {
    func leastMinutes(_ n: Int) -> Int {

    }
}
```

tab: Kotlin

```kotlin
class Solution {
    fun leastMinutes(n: Int): Int {

    }
}
```

tab: Dart

```dart
class Solution {
  int leastMinutes(int n) {

  }
}
```

tab: Go

```go
func leastMinutes(n int) int {

}
```

tab: Ruby

```ruby
# @param {Integer} n
# @return {Integer}
def least_minutes(n)

end
```

tab: Scala

```scala
object Solution {
    def leastMinutes(n: Int): Int = {

    }
}
```

tab: Rust

```rust
impl Solution {
    pub fn least_minutes(n: i32) -> i32 {

    }
}
```

tab: Racket

```racket
(define/contract (least-minutes n)
  (-> exact-integer? exact-integer?)

  )
```

tab: Erlang

```erlang
-spec least_minutes(N :: integer()) -> integer().
least_minutes(N) ->
  .
```

tab: Elixir

```elixir
defmodule Solution do
  @spec least_minutes(n :: integer) :: integer
  def least_minutes(n) do

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
          
