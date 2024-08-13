---
tags:
  - leetcode/problem
questionId: LCP 66
title: 最小展台数量
translatedTitle: 最小展台数量
titleSlug: 600YaG
aliases:
  - 最小展台数量
  - 600YaG
  - 最小展台数量
lcLinks:
  - https://leetcode.cn/problems/600YaG/
lcTopics:
  - '[[array]]'
  - '[[hash-table]]'
  - '[[string]]'
  - '[[counting]]'
lcDifficulty: Easy
lcAcRate: 77.5%
similarQuestions: []
grade: ⭐⭐⭐⭐⭐
likes: 9
dislikes: 0
favorites: []
solutions: []
notes: []
---

**Nav:** << previous: [[LCP 65.舒适的湿度]] | next: [[LCP 67.装饰树]] >>

---

## Description

~~~tabs
tab: English

No description

---

[submissions](https://leetcode.com/problems/600YaG/submissions/) | [solutions](https://leetcode.com/problems/600YaG/solutions/)


tab: 中文

力扣嘉年华将举办一系列展览活动，后勤部将负责为每场展览提供所需要的展台。
已知后勤部得到了一份需求清单，记录了近期展览所需要的展台类型， `demand[i][j]` 表示第 `i` 天展览时第 `j` 个展台的类型。
在满足每一天展台需求的基础上，请返回后勤部需要准备的 **最小** 展台数量。

**注意：**
- 同一展台在不同天中可以重复使用。

**示例 1：**
>输入：`demand = ["acd","bed","accd"]`
>
>输出：`6`
>
>解释：
>第 `0` 天需要展台 `a、c、d`；
>第 `1` 天需要展台 `b、e、d`；
>第 `2` 天需要展台 `a、c、c、d`；
>因此，后勤部准备 `abccde` 的展台，可以满足每天的展览需求;

**示例 2：**
>输入：`demand = ["abc","ab","ac","b"]`
>
>输出：`3`


**提示：**
- `1 <= demand.length,demand[i].length <= 100`
- `demand[i][j]` 仅为小写字母

---

[提交记录](https://leetcode.cn/problems/600YaG/submissions/) | [题解](https://leetcode.cn/problems/600YaG/solution/)


~~~

## Code Snippets

~~~tabs
tab: C++

```cpp
class Solution {
public:
    int minNumBooths(vector<string>& demand) {

    }
};
```

tab: Java

```java
class Solution {
    public int minNumBooths(String[] demand) {

    }
}
```

tab: Python

```python
class Solution(object):
    def minNumBooths(self, demand):
        """
        :type demand: List[str]
        :rtype: int
        """
```

tab: Python3

```python
class Solution:
    def minNumBooths(self, demand: List[str]) -> int:
```

tab: C

```c


int minNumBooths(char** demand, int demandSize){

}
```

tab: C#

```csharp
public class Solution {
    public int MinNumBooths(string[] demand) {

    }
}
```

tab: JavaScript

```javascript
/**
 * @param {string[]} demand
 * @return {number}
 */
var minNumBooths = function(demand) {

};
```

tab: TypeScript

```typescript
function minNumBooths(demand: string[]): number {

};
```

tab: PHP

```php
class Solution {

    /**
     * @param String[] $demand
     * @return Integer
     */
    function minNumBooths($demand) {

    }
}
```

tab: Swift

```swift
class Solution {
    func minNumBooths(_ demand: [String]) -> Int {

    }
}
```

tab: Kotlin

```kotlin
class Solution {
    fun minNumBooths(demand: Array<String>): Int {

    }
}
```

tab: Dart

```dart
class Solution {
  int minNumBooths(List<String> demand) {

  }
}
```

tab: Go

```go
func minNumBooths(demand []string) int {

}
```

tab: Ruby

```ruby
# @param {String[]} demand
# @return {Integer}
def min_num_booths(demand)

end
```

tab: Scala

```scala
object Solution {
    def minNumBooths(demand: Array[String]): Int = {

    }
}
```

tab: Rust

```rust
impl Solution {
    pub fn min_num_booths(demand: Vec<String>) -> i32 {

    }
}
```

tab: Racket

```racket
(define/contract (min-num-booths demand)
  (-> (listof string?) exact-integer?)

  )
```

tab: Erlang

```erlang
-spec min_num_booths(Demand :: [unicode:unicode_binary()]) -> integer().
min_num_booths(Demand) ->
  .
```

tab: Elixir

```elixir
defmodule Solution do
  @spec min_num_booths(demand :: [String.t]) :: integer
  def min_num_booths(demand) do

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
          
