---
tags:
  - leetcode/problem
questionId: LCP 80
title: 生物进化录
translatedTitle: 生物进化录
titleSlug: qoQAMX
aliases:
  - 生物进化录
  - qoQAMX
  - 生物进化录
lcLink: https://leetcode.com/problems/qoQAMX/
lcTopics: []
lcDifficulty: Hard
lcAcRate: 52.6%
similarQuestions: []
grade: ⭐⭐⭐⭐⭐
likes: 4
dislikes: 0
favorites: []
solutions: []
notes: []
cssclasses: []
created: 2024-08-13 00:10
updated:
---

**Nav:** << previous: [[LCP 79.kjpLFZ]] | next: [[LCP 81.ryfUiz]] >>

---

## Description

~~~tabs
tab: English

No description

---

[submissions](https://leetcode.com/problems/qoQAMX/submissions/) | [solutions](https://leetcode.com/problems/qoQAMX/solutions/)


tab: 中文

在永恒之森中，存在着一本生物进化录，以 **一个树形结构** 记载了所有生物的演化过程。经过观察并整理了各节点间的关系，`parents[i]` 表示编号 `i` 节点的父节点编号(根节点的父节点为 `-1`)。

为了探索和记录其中的演化规律，队伍中的炼金术师提出了一种方法，可以以字符串的形式将其复刻下来，规则如下：
- 初始只有一个根节点，表示演化的起点，依次记录 `01` 字符串中的字符，
- 如果记录 `0`，则在当前节点下添加一个子节点，并将指针指向新添加的子节点；
- 如果记录 `1`，则将指针回退到当前节点的父节点处。

现在需要应用上述的记录方法，复刻下它的演化过程。请返回能够复刻演化过程的字符串中， **字典序最小** 的 `01` 字符串。

**注意：**
- 节点指针最终可以停在任何节点上，不一定要回到根节点。

**示例 1：**
> 输入：`parents = [-1,0,0,2]`
>
> 输出：`"00110"`
>
>解释：树结构如下图所示，共存在 2 种记录方案：
>第 1 种方案为：0(记录编号 1 的节点) -> 1(回退至节点 0) -> 0(记录编号 2 的节点) -> 0((记录编号 3 的节点))
>第 2 种方案为：0(记录编号 2 的节点) -> 0(记录编号 3 的节点) -> 1(回退至节点 2) -> 1(回退至节点 0) -> 0(记录编号 1 的节点)
>返回字典序更小的 `"00110"`
![image.png](https://pic.leetcode.cn/1682319485-cRVudI-image.png){:width=120px}![进化 (3).gif](https://pic.leetcode.cn/1682412701-waHdnm-%E8%BF%9B%E5%8C%96%20\(3\).gif){:width=320px}



**示例 2：**
> 输入：`parents = [-1,0,0,1,2,2]`
>
> 输出：`"00101100"`

**提示：**

- `1 <= parents.length <= 10^4`
- `-1 <= parents[i] < i` (即父节点编号小于子节点)

---

[提交记录](https://leetcode.cn/problems/qoQAMX/submissions/) | [题解](https://leetcode.cn/problems/qoQAMX/solution/)


~~~

## Code Snippets

~~~tabs
tab: C++

```cpp
class Solution {
public:
    string evolutionaryRecord(vector<int>& parents) {

    }
};
```

tab: Java

```java
class Solution {
    public String evolutionaryRecord(int[] parents) {

    }
}
```

tab: Python

```python
class Solution(object):
    def evolutionaryRecord(self, parents):
        """
        :type parents: List[int]
        :rtype: str
        """
```

tab: Python3

```python
class Solution:
    def evolutionaryRecord(self, parents: List[int]) -> str:
```

tab: C

```c
char* evolutionaryRecord(int* parents, int parentsSize){

}
```

tab: C#

```csharp
public class Solution {
    public string EvolutionaryRecord(int[] parents) {

    }
}
```

tab: JavaScript

```javascript
/**
 * @param {number[]} parents
 * @return {string}
 */
var evolutionaryRecord = function(parents) {

};
```

tab: TypeScript

```typescript
function evolutionaryRecord(parents: number[]): string {

};
```

tab: PHP

```php
class Solution {

    /**
     * @param Integer[] $parents
     * @return String
     */
    function evolutionaryRecord($parents) {

    }
}
```

tab: Swift

```swift
class Solution {
    func evolutionaryRecord(_ parents: [Int]) -> String {

    }
}
```

tab: Kotlin

```kotlin
class Solution {
    fun evolutionaryRecord(parents: IntArray): String {

    }
}
```

tab: Dart

```dart
class Solution {
  String evolutionaryRecord(List<int> parents) {

  }
}
```

tab: Go

```go
func evolutionaryRecord(parents []int) string {

}
```

tab: Ruby

```ruby
# @param {Integer[]} parents
# @return {String}
def evolutionary_record(parents)

end
```

tab: Scala

```scala
object Solution {
    def evolutionaryRecord(parents: Array[Int]): String = {

    }
}
```

tab: Rust

```rust
impl Solution {
    pub fn evolutionary_record(parents: Vec<i32>) -> String {

    }
}
```

tab: Racket

```racket
(define/contract (evolutionary-record parents)
  (-> (listof exact-integer?) string?)

  )
```

tab: Erlang

```erlang
-spec evolutionary_record(Parents :: [integer()]) -> unicode:unicode_binary().
evolutionary_record(Parents) ->
  .
```

tab: Elixir

```elixir
defmodule Solution do
  @spec evolutionary_record(parents :: [integer]) :: String.t
  def evolutionary_record(parents) do

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
          
