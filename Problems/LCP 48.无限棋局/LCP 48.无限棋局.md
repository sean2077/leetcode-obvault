---
tags:
  - leetcode/problem
questionId: LCP 48
title: 无限棋局
translatedTitle: 无限棋局
titleSlug: fsa7oZ
aliases:
  - 无限棋局
  - fsa7oZ
  - 无限棋局
lcLinks:
  - https://leetcode.cn/problems/fsa7oZ/
lcTopics:
  - '[[array]]'
  - '[[math]]'
  - '[[enumeration]]'
  - '[[game-theory]]'
lcDifficulty: Hard
lcAcRate: 27.6%
similarQuestions: []
grade: ⭐⭐⭐⭐⭐
likes: 12
dislikes: 0
favorites: []
solutions: []
notes: []
---

**Nav:** << previous: [[LCP 47.入场安检]] | next: [[LCP 49.环形闯关游戏]] >>

---

## Description

~~~tabs
tab: English

No description

---

[submissions](https://leetcode.com/problems/fsa7oZ/submissions/) | [solutions](https://leetcode.com/problems/fsa7oZ/solutions/)


tab: 中文

小力正在通过残局练习来备战「力扣挑战赛」中的「五子棋」项目，他想请你能帮他预测当前残局的输赢情况。棋盘中的棋子分布信息记录于二维数组 `pieces` 中，其中 `pieces[i] = [x,y,color]` 表示第 `i` 枚棋子的横坐标为 `x`，纵坐标为 `y`，棋子颜色为 `color`(`0` 表示黑棋，`1` 表示白棋)。假如黑棋先行，并且黑棋和白棋都按最优策略落子，请你求出当前棋局在三步（按 **黑、白、黑** 的落子顺序）之内的输赢情况（三步之内先构成同行、列或对角线连续同颜色的至少 5 颗即为获胜）：
- 黑棋胜, 请返回 `"Black"`
- 白棋胜, 请返回 `"White"`
- 仍无胜者, 请返回 `"None"`

**注意：** 
- 和传统的五子棋项目不同，「力扣挑战赛」中的「五子棋」项目 **不存在边界限制**，即可在 **任意位置** 落子；
- 黑棋和白棋均按 3 步内的输赢情况进行最优策略的选择
- 测试数据保证所给棋局目前无胜者；
- 测试数据保证不会存在坐标一样的棋子。

**示例 1：**
> 输入：
> `pieces = [[0,0,1],[1,1,1],[2,2,0]]`
>
> 输出：`"None"`
>
> 解释：无论黑、白棋以何种方式落子，三步以内都不会产生胜者。

**示例 2：**
> 输入：
> `pieces = [[1,2,1],[1,4,1],[1,5,1],[2,1,0],[2,3,0],[2,4,0],[3,2,1],[3,4,0],[4,2,1],[5,2,1]]`
>
> 输出：`"Black"`
>
> 解释：三步之内黑棋必胜，以下是一种可能的落子情况：
>![902b87df29998b1c181146c8fdb3a4b6.gif](https://pic.leetcode-cn.com/1629800639-KabOfY-902b87df29998b1c181146c8fdb3a4b6.gif){:width="300px"}



**提示：**
- `0 <= pieces.length <= 1000`
- `pieces[i].length = 3`
- `-10^9 <= pieces[i][0], pieces[i][1] <=10^9` 
- `0 <= pieces[i][2] <=1`


---

[提交记录](https://leetcode.cn/problems/fsa7oZ/submissions/) | [题解](https://leetcode.cn/problems/fsa7oZ/solution/)


~~~

## Code Snippets

~~~tabs
tab: C++

```cpp
class Solution {
public:
    string gobang(vector<vector<int>>& pieces) {

    }
};
```

tab: Java

```java
class Solution {
    public String gobang(int[][] pieces) {

    }
}
```

tab: Python

```python
class Solution(object):
    def gobang(self, pieces):
        """
        :type pieces: List[List[int]]
        :rtype: str
        """
```

tab: Python3

```python
class Solution:
    def gobang(self, pieces: List[List[int]]) -> str:
```

tab: C

```c


char* gobang(int** pieces, int piecesSize, int* piecesColSize){

}
```

tab: C#

```csharp
public class Solution {
    public string Gobang(int[][] pieces) {

    }
}
```

tab: JavaScript

```javascript
/**
 * @param {number[][]} pieces
 * @return {string}
 */
var gobang = function(pieces) {

};
```

tab: TypeScript

```typescript
function gobang(pieces: number[][]): string {

};
```

tab: PHP

```php
class Solution {

    /**
     * @param Integer[][] $pieces
     * @return String
     */
    function gobang($pieces) {

    }
}
```

tab: Swift

```swift
class Solution {
    func gobang(_ pieces: [[Int]]) -> String {

    }
}
```

tab: Kotlin

```kotlin
class Solution {
    fun gobang(pieces: Array<IntArray>): String {

    }
}
```

tab: Dart

```dart
class Solution {
  String gobang(List<List<int>> pieces) {

  }
}
```

tab: Go

```go
func gobang(pieces [][]int) string {

}
```

tab: Ruby

```ruby
# @param {Integer[][]} pieces
# @return {String}
def gobang(pieces)

end
```

tab: Scala

```scala
object Solution {
    def gobang(pieces: Array[Array[Int]]): String = {

    }
}
```

tab: Rust

```rust
impl Solution {
    pub fn gobang(pieces: Vec<Vec<i32>>) -> String {

    }
}
```

tab: Racket

```racket
(define/contract (gobang pieces)
  (-> (listof (listof exact-integer?)) string?)

  )
```

tab: Erlang

```erlang
-spec gobang(Pieces :: [[integer()]]) -> unicode:unicode_binary().
gobang(Pieces) ->
  .
```

tab: Elixir

```elixir
defmodule Solution do
  @spec gobang(pieces :: [[integer]]) :: String.t
  def gobang(pieces) do

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
          
