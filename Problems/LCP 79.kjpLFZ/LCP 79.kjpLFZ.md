---
tags:
  - leetcode/problem
questionId: LCP 79
title: 提取咒文
translatedTitle: 提取咒文
titleSlug: kjpLFZ
aliases:
  - 提取咒文
  - kjpLFZ
  - 提取咒文
lcLink: https://leetcode.com/problems/kjpLFZ/
lcTopics: []
lcDifficulty: Medium
lcAcRate: 30.3%
similarQuestions: []
grade: ⭐⭐⭐⭐⭐
likes: 6
dislikes: 0
favorites: []
solutions: []
notes: []
cssclasses: []
created: 2024-08-13 00:10
updated:
---

**Nav:** << previous: [[LCP 78.Nsibyl]] | next: [[LCP 80.qoQAMX]] >>

---

## Description

~~~tabs
tab: English

No description

---

[submissions](https://leetcode.com/problems/kjpLFZ/submissions/) | [solutions](https://leetcode.com/problems/kjpLFZ/solutions/)


tab: 中文

随着兽群逐渐远去，一座大升降机缓缓的从地下升到了远征队面前。借由这台升降机，他们将能够到达地底的永恒至森。
在升降机的操作台上，是一个由魔法符号组成的矩阵，为了便于辨识，我们用小写字母来表示。 `matrix[i][j]` 表示矩阵第 `i` 行 `j` 列的字母。该矩阵上有一个提取装置，可以对所在位置的字母提取。
提取装置初始位于矩阵的左上角 `[0,0]`，可以通过每次操作移动到上、下、左、右相邻的 1 格位置中。提取装置每次移动或每次提取均记为一次操作。

远征队需要按照顺序，从矩阵中逐一取出字母以组成 `mantra`，才能够成功的启动升降机。请返回他们 **最少** 需要消耗的操作次数。如果无法完成提取，返回 `-1`。

**注意：**
- 提取装置可对同一位置的字母重复提取，每次提取一个
- 提取字母时，需按词语顺序依次提取

**示例 1：**
>输入：`matrix = ["sd","ep"], mantra = "speed"`
>
>输出：`10`
>
>解释：如下图所示
![矩阵 (2).gif](https://pic.leetcode-cn.com/1646288670-OTlvAl-%E7%9F%A9%E9%98%B5%20\(2\).gif)

**示例 2：**
>输入：`matrix = ["abc","daf","geg"]， mantra = "sad"`
>
>输出：`-1`
>
>解释：矩阵中不存在 `s` ，无法提取词语

**提示：**
- `0 < matrix.length, matrix[i].length <= 100`
- `0 < mantra.length <= 100`
- `matrix 和 mantra` 仅由小写字母组成

---

[提交记录](https://leetcode.cn/problems/kjpLFZ/submissions/) | [题解](https://leetcode.cn/problems/kjpLFZ/solution/)


~~~

## Code Snippets

~~~tabs
tab: C++

```cpp
class Solution {
public:
    int extractMantra(vector<string>& matrix, string mantra) {

    }
};
```

tab: Java

```java
class Solution {
    public int extractMantra(String[] matrix, String mantra) {

    }
}
```

tab: Python

```python
class Solution(object):
    def extractMantra(self, matrix, mantra):
        """
        :type matrix: List[str]
        :type mantra: str
        :rtype: int
        """
```

tab: Python3

```python
class Solution:
    def extractMantra(self, matrix: List[str], mantra: str) -> int:
```

tab: C

```c
int extractMantra(char** matrix, int matrixSize, char* mantra){

}
```

tab: C#

```csharp
public class Solution {
    public int ExtractMantra(string[] matrix, string mantra) {

    }
}
```

tab: JavaScript

```javascript
/**
 * @param {string[]} matrix
 * @param {string} mantra
 * @return {number}
 */
var extractMantra = function(matrix, mantra) {

};
```

tab: TypeScript

```typescript
function extractMantra(matrix: string[], mantra: string): number {

};
```

tab: PHP

```php
class Solution {

    /**
     * @param String[] $matrix
     * @param String $mantra
     * @return Integer
     */
    function extractMantra($matrix, $mantra) {

    }
}
```

tab: Swift

```swift
class Solution {
    func extractMantra(_ matrix: [String], _ mantra: String) -> Int {

    }
}
```

tab: Kotlin

```kotlin
class Solution {
    fun extractMantra(matrix: Array<String>, mantra: String): Int {

    }
}
```

tab: Dart

```dart
class Solution {
  int extractMantra(List<String> matrix, String mantra) {

  }
}
```

tab: Go

```go
func extractMantra(matrix []string, mantra string) int {

}
```

tab: Ruby

```ruby
# @param {String[]} matrix
# @param {String} mantra
# @return {Integer}
def extract_mantra(matrix, mantra)

end
```

tab: Scala

```scala
object Solution {
    def extractMantra(matrix: Array[String], mantra: String): Int = {

    }
}
```

tab: Rust

```rust
impl Solution {
    pub fn extract_mantra(matrix: Vec<String>, mantra: String) -> i32 {

    }
}
```

tab: Racket

```racket
(define/contract (extract-mantra matrix mantra)
  (-> (listof string?) string? exact-integer?)

  )
```

tab: Erlang

```erlang
-spec extract_mantra(Matrix :: [unicode:unicode_binary()], Mantra :: unicode:unicode_binary()) -> integer().
extract_mantra(Matrix, Mantra) ->
  .
```

tab: Elixir

```elixir
defmodule Solution do
  @spec extract_mantra(matrix :: [String.t], mantra :: String.t) :: integer
  def extract_mantra(matrix, mantra) do

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
          
