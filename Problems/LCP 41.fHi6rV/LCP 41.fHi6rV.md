---
tags:
  - leetcode/problem
questionId: LCP 41
title: 黑白翻转棋
translatedTitle: 黑白翻转棋
titleSlug: fHi6rV
aliases:
  - 黑白翻转棋
  - fHi6rV
  - 黑白翻转棋
lcLink: https://leetcode.com/problems/fHi6rV/
lcTopics:
  - '[[breadth-first-search]]'
  - '[[array]]'
  - '[[matrix]]'
lcDifficulty: Medium
lcAcRate: 68.3%
similarQuestions: []
grade: ⭐⭐⭐⭐⭐
likes: 80
dislikes: 0
favorites: []
solutions: []
notes: []
cssclasses: []
created: 2024-08-13 00:10
updated:
---

**Nav:** << previous: [[LCP 40.uOAnQW]] | next: [[LCP 42.vFjcfV]] >>

---

## Description

~~~tabs
tab: English

No description

---

[submissions](https://leetcode.com/problems/fHi6rV/submissions/) | [solutions](https://leetcode.com/problems/fHi6rV/solutions/)


tab: 中文

在 `n*m` 大小的棋盘中，有黑白两种棋子，黑棋记作字母 `"X"`, 白棋记作字母 `"O"`，空余位置记作 `"."`。当落下的棋子与其他相同颜色的棋子在行、列或对角线完全包围（中间不存在空白位置）另一种颜色的棋子，则可以翻转这些棋子的颜色。



![1.gif](https://pic.leetcode-cn.com/1630396029-eTgzpN-6da662e67368466a96d203f67bb6e793.gif){:height=170px}![2.gif](https://pic.leetcode-cn.com/1630396240-nMvdcc-8e4261afe9f60e05a4f740694b439b6b.gif){:height=170px}![3.gif](https://pic.leetcode-cn.com/1630396291-kEtzLL-6fcb682daeecb5c3f56eb88b23c81d33.gif){:height=170px}

「力扣挑战赛」黑白翻转棋项目中，将提供给选手一个未形成可翻转棋子的棋盘残局，其状态记作 `chessboard`。若下一步可放置一枚黑棋，请问选手最多能翻转多少枚白棋。

**注意：**
- 若翻转白棋成黑棋后，棋盘上仍存在可以翻转的白棋，将可以 **继续** 翻转白棋
- 输入数据保证初始棋盘状态无可以翻转的棋子且存在空余位置

**示例 1：**
> 输入：`chessboard = ["....X.","....X.","XOOO..","......","......"]`
> 
> 输出：`3`
> 
> 解释：
> 可以选择下在 `[2,4]` 处，能够翻转白方三枚棋子。

**示例 2：**
> 输入：`chessboard = [".X.",".O.","XO."]`
> 
> 输出：`2`
> 
> 解释：
> 可以选择下在 `[2,2]` 处，能够翻转白方两枚棋子。
![2126c1d21b1b9a9924c639d449cc6e65.gif](https://pic.leetcode-cn.com/1626683255-OBtBud-2126c1d21b1b9a9924c639d449cc6e65.gif)

**示例 3：**
> 输入：`chessboard = [".......",".......",".......","X......",".O.....","..O....","....OOX"]`
> 
> 输出：`4`
> 
> 解释：
> 可以选择下在 `[6,3]` 处，能够翻转白方四枚棋子。
![803f2f04098b6174397d6c696f54d709.gif](https://pic.leetcode-cn.com/1630393770-Puyked-803f2f04098b6174397d6c696f54d709.gif)



**提示：**
- `1 <= chessboard.length, chessboard[i].length <= 8`
- `chessboard[i]` 仅包含 `"."、"O"` 和 `"X"`

---

[提交记录](https://leetcode.cn/problems/fHi6rV/submissions/) | [题解](https://leetcode.cn/problems/fHi6rV/solution/)


~~~

## Code Snippets

~~~tabs
tab: C++

```cpp
class Solution {
public:
    int flipChess(vector<string>& chessboard) {

    }
};
```

tab: Java

```java
class Solution {
    public int flipChess(String[] chessboard) {

    }
}
```

tab: Python

```python
class Solution(object):
    def flipChess(self, chessboard):
        """
        :type chessboard: List[str]
        :rtype: int
        """
```

tab: Python3

```python
class Solution:
    def flipChess(self, chessboard: List[str]) -> int:
```

tab: C

```c


int flipChess(char** chessboard, int chessboardSize){

}
```

tab: C#

```csharp
public class Solution {
    public int FlipChess(string[] chessboard) {

    }
}
```

tab: JavaScript

```javascript
/**
 * @param {string[]} chessboard
 * @return {number}
 */
var flipChess = function(chessboard) {

};
```

tab: TypeScript

```typescript
function flipChess(chessboard: string[]): number {

};
```

tab: PHP

```php
class Solution {

    /**
     * @param String[] $chessboard
     * @return Integer
     */
    function flipChess($chessboard) {

    }
}
```

tab: Swift

```swift
class Solution {
    func flipChess(_ chessboard: [String]) -> Int {

    }
}
```

tab: Kotlin

```kotlin
class Solution {
    fun flipChess(chessboard: Array<String>): Int {

    }
}
```

tab: Dart

```dart
class Solution {
  int flipChess(List<String> chessboard) {

  }
}
```

tab: Go

```go
func flipChess(chessboard []string) int {

}
```

tab: Ruby

```ruby
# @param {String[]} chessboard
# @return {Integer}
def flip_chess(chessboard)

end
```

tab: Scala

```scala
object Solution {
    def flipChess(chessboard: Array[String]): Int = {

    }
}
```

tab: Rust

```rust
impl Solution {
    pub fn flip_chess(chessboard: Vec<String>) -> i32 {

    }
}
```

tab: Racket

```racket
(define/contract (flip-chess chessboard)
  (-> (listof string?) exact-integer?)

  )
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
          
