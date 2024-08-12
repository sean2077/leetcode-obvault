---
tags:
  - leetcode/problem
questionId: LCP 73
title: 探险营地
translatedTitle: 探险营地
titleSlug: 0Zeoeg
aliases:
  - 探险营地
  - 0Zeoeg
  - 探险营地
lcLink: https://leetcode.com/problems/0Zeoeg/
lcTopics: []
lcDifficulty: Medium
lcAcRate: 45.8%
similarQuestions: []
grade: ⭐⭐⭐⭐⭐
likes: 3
dislikes: 0
favorites: []
solutions: []
notes: []
cssclasses: []
created: 2024-08-13 00:10
updated:
---

**Nav:** << previous: [[LCP 72.hqCnmP]] | next: [[LCP 74.xepqZ5]] >>

---

## Description

~~~tabs
tab: English

No description

---

[submissions](https://leetcode.com/problems/0Zeoeg/submissions/) | [solutions](https://leetcode.com/problems/0Zeoeg/solutions/)


tab: 中文

探险家小扣的行动轨迹，都将保存在记录仪中。`expeditions[i]` 表示小扣第 `i` 次探险记录，用一个字符串数组表示。其中的每个「营地」由大小写字母组成，通过子串 `->` 连接。
> 例："Leet->code->Campsite"，表示到访了 "Leet"、"code"、"Campsite" 三个营地。

`expeditions[0]` 包含了初始小扣已知的所有营地；对于之后的第 `i` 次探险(即 `expeditions[i]` 且 i > 0)，如果记录中包含了之前均没出现的营地，则表示小扣 **新发现** 的营地。

请你找出小扣发现新营地最多且索引最小的那次探险，并返回对应的记录索引。如果所有探险记录都没有发现新的营地，返回 `-1`

**注意：**
- 大小写不同的营地视为不同的营地；
- 营地的名称长度均大于 `0`。

**示例 1：**
>输入：`expeditions = ["leet->code","leet->code->Campsite->Leet","leet->code->leet->courier"]`
>
>输出：`1`
>
>解释：
>初始已知的所有营地为 "leet" 和 "code"
>第 1 次，到访了 "leet"、"code"、"Campsite"、"Leet"，新发现营地 2 处："Campsite"、"Leet"
>第 2 次，到访了 "leet"、"code"、"courier"，新发现营地 1 处："courier"
>第 1 次探险发现的新营地数量最多，因此返回 `1`

**示例 2：**
>输入：`expeditions = ["Alice->Dex","","Dex"]`
>
>输出：`-1`
>
>解释：
>初始已知的所有营地为 "Alice" 和 "Dex"
>第 1 次，未到访任何营地；
>第 2 次，到访了 "Dex"，未新发现营地；
>因为两次探险均未发现新的营地，返回 `-1`

**示例 3：**
>输入：`expeditions = ["","Gryffindor->Slytherin->Gryffindor","Hogwarts->Hufflepuff->Ravenclaw"]`
>
>输出：`2`
>
>解释：
>初始未发现任何营地；
>第 1 次，到访 "Gryffindor"、"Slytherin" 营地，其中重复到访 "Gryffindor" 两次，
>因此新发现营地为 2 处："Gryffindor"、"Slytherin"
>第 2 次，到访 "Hogwarts"、"Hufflepuff"、"Ravenclaw" 营地；
>新发现营地 3 处："Hogwarts"、"Hufflepuff"、"Ravenclaw"；
>第 2 次探险发现的新营地数量最多，因此返回 `2`

**提示：**
- `1 <= expeditions.length <= 1000`
- `0 <= expeditions[i].length <= 1000`
- 探险记录中只包含大小写字母和子串"->"

---

[提交记录](https://leetcode.cn/problems/0Zeoeg/submissions/) | [题解](https://leetcode.cn/problems/0Zeoeg/solution/)


~~~

## Code Snippets

~~~tabs
tab: C++

```cpp
class Solution {
public:
    int adventureCamp(vector<string>& expeditions) {

    }
};
```

tab: Java

```java
class Solution {
    public int adventureCamp(String[] expeditions) {

    }
}
```

tab: Python

```python
class Solution(object):
    def adventureCamp(self, expeditions):
        """
        :type expeditions: List[str]
        :rtype: int
        """
```

tab: Python3

```python
class Solution:
    def adventureCamp(self, expeditions: List[str]) -> int:
```

tab: C

```c
int adventureCamp(char** expeditions, int expeditionsSize){

}
```

tab: C#

```csharp
public class Solution {
    public int AdventureCamp(string[] expeditions) {

    }
}
```

tab: JavaScript

```javascript
/**
 * @param {string[]} expeditions
 * @return {number}
 */
var adventureCamp = function(expeditions) {

};
```

tab: TypeScript

```typescript
function adventureCamp(expeditions: string[]): number {

};
```

tab: PHP

```php
class Solution {

    /**
     * @param String[] $expeditions
     * @return Integer
     */
    function adventureCamp($expeditions) {

    }
}
```

tab: Swift

```swift
class Solution {
    func adventureCamp(_ expeditions: [String]) -> Int {

    }
}
```

tab: Kotlin

```kotlin
class Solution {
    fun adventureCamp(expeditions: Array<String>): Int {

    }
}
```

tab: Dart

```dart
class Solution {
  int adventureCamp(List<String> expeditions) {

  }
}
```

tab: Go

```go
func adventureCamp(expeditions []string) int {

}
```

tab: Ruby

```ruby
# @param {String[]} expeditions
# @return {Integer}
def adventure_camp(expeditions)

end
```

tab: Scala

```scala
object Solution {
    def adventureCamp(expeditions: Array[String]): Int = {

    }
}
```

tab: Rust

```rust
impl Solution {
    pub fn adventure_camp(expeditions: Vec<String>) -> i32 {

    }
}
```

tab: Racket

```racket
(define/contract (adventure-camp expeditions)
  (-> (listof string?) exact-integer?)

  )
```

tab: Erlang

```erlang
-spec adventure_camp(Expeditions :: [unicode:unicode_binary()]) -> integer().
adventure_camp(Expeditions) ->
  .
```

tab: Elixir

```elixir
defmodule Solution do
  @spec adventure_camp(expeditions :: [String.t]) :: integer
  def adventure_camp(expeditions) do

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
          
