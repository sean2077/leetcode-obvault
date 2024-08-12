---
tags:
  - leetcode/problem
questionId: LCP 42
title: 玩具套圈
translatedTitle: 玩具套圈
titleSlug: vFjcfV
aliases:
  - 玩具套圈
  - vFjcfV
  - 玩具套圈
lcLinks:
  - https://leetcode.cn/problems/vFjcfV/
lcTopics:
  - '[[geometry]]'
  - '[[array]]'
  - '[[hash-table]]'
  - '[[math]]'
  - '[[binary-search]]'
  - '[[sorting]]'
lcDifficulty: Hard
lcAcRate: 28.8%
similarQuestions: []
grade: ⭐⭐⭐⭐⭐
likes: 14
dislikes: 0
favorites: []
solutions: []
notes: []
cssclasses: []
created: 2024-08-13 00:28
updated:
---

**Nav:** << previous: [[LCP 41.fHi6rV]] | next: [[LCP 43.Y1VbOX]] >>

---

## Description

~~~tabs
tab: English

No description

---

[submissions](https://leetcode.com/problems/vFjcfV/submissions/) | [solutions](https://leetcode.com/problems/vFjcfV/solutions/)


tab: 中文

「力扣挑战赛」场地外，小力组织了一个套玩具的游戏。所有的玩具摆在平地上，`toys[i]` 以 `[xi,yi,ri]` 的形式记录了第 `i` 个玩具的坐标 `(xi,yi)` 和半径 `ri`。小扣试玩了一下，他扔了若干个半径均为 `r` 的圈，`circles[j]` 记录了第 `j` 个圈的坐标 `(xj,yj)`。套圈的规则如下：
- 若一个玩具被某个圈完整覆盖了（即玩具的任意部分均在圈内或者圈上），则该玩具被套中。
- 若一个玩具被多个圈同时套中，最终仅计算为套中一个玩具

请帮助小扣计算，他成功套中了多少玩具。

**注意：**
- 输入数据保证任意两个玩具的圆心不会重合，但玩具之间可能存在重叠。


**示例 1：**

> 输入：`toys = [[3,3,1],[3,2,1]], circles = [[4,3]], r = 2`
>
> 输出：`1`
> 
> 解释： 如图所示，仅套中一个玩具
![image.png](https://pic.leetcode-cn.com/1629194140-ydKiGF-image.png)


**示例 2：**

> 输入：`toys = [[1,3,2],[4,3,1],[7,1,2]], circles = [[1,0],[3,3]], r = 4`
>
> 输出：`2`
> 
> 解释： 如图所示，套中两个玩具
![image.png](https://pic.leetcode-cn.com/1629194157-RiOAuy-image.png){:width="400px"}



**提示：** 
- `1 <= toys.length <= 10^4`
- `0 <= toys[i][0], toys[i][1] <= 10^9`
- `1 <= circles.length <= 10^4`
- `0 <= circles[i][0], circles[i][1] <= 10^9`
- `1 <= toys[i][2], r <= 10`


---

[提交记录](https://leetcode.cn/problems/vFjcfV/submissions/) | [题解](https://leetcode.cn/problems/vFjcfV/solution/)


~~~

## Code Snippets

~~~tabs
tab: C++

```cpp
class Solution {
public:
    int circleGame(vector<vector<int>>& toys, vector<vector<int>>& circles, int r) {

    }
};
```

tab: Java

```java
class Solution {
    public int circleGame(int[][] toys, int[][] circles, int r) {

    }
}
```

tab: Python

```python
class Solution(object):
    def circleGame(self, toys, circles, r):
        """
        :type toys: List[List[int]]
        :type circles: List[List[int]]
        :type r: int
        :rtype: int
        """
```

tab: Python3

```python
class Solution:
    def circleGame(self, toys: List[List[int]], circles: List[List[int]], r: int) -> int:
```

tab: C

```c


int circleGame(int** toys, int toysSize, int* toysColSize, int** circles, int circlesSize, int* circlesColSize, int r){

}
```

tab: C#

```csharp
public class Solution {
    public int CircleGame(int[][] toys, int[][] circles, int r) {

    }
}
```

tab: JavaScript

```javascript
/**
 * @param {number[][]} toys
 * @param {number[][]} circles
 * @param {number} r
 * @return {number}
 */
var circleGame = function(toys, circles, r) {

};
```

tab: TypeScript

```typescript
function circleGame(toys: number[][], circles: number[][], r: number): number {

};
```

tab: PHP

```php
class Solution {

    /**
     * @param Integer[][] $toys
     * @param Integer[][] $circles
     * @param Integer $r
     * @return Integer
     */
    function circleGame($toys, $circles, $r) {

    }
}
```

tab: Swift

```swift
class Solution {
    func circleGame(_ toys: [[Int]], _ circles: [[Int]], _ r: Int) -> Int {

    }
}
```

tab: Kotlin

```kotlin
class Solution {
    fun circleGame(toys: Array<IntArray>, circles: Array<IntArray>, r: Int): Int {

    }
}
```

tab: Dart

```dart
class Solution {
  int circleGame(List<List<int>> toys, List<List<int>> circles, int r) {

  }
}
```

tab: Go

```go
func circleGame(toys [][]int, circles [][]int, r int) int {

}
```

tab: Ruby

```ruby
# @param {Integer[][]} toys
# @param {Integer[][]} circles
# @param {Integer} r
# @return {Integer}
def circle_game(toys, circles, r)

end
```

tab: Scala

```scala
object Solution {
    def circleGame(toys: Array[Array[Int]], circles: Array[Array[Int]], r: Int): Int = {

    }
}
```

tab: Rust

```rust
impl Solution {
    pub fn circle_game(toys: Vec<Vec<i32>>, circles: Vec<Vec<i32>>, r: i32) -> i32 {

    }
}
```

tab: Racket

```racket
(define/contract (circle-game toys circles r)
  (-> (listof (listof exact-integer?)) (listof (listof exact-integer?)) exact-integer? exact-integer?)

  )
```

tab: Erlang

```erlang
-spec circle_game(Toys :: [[integer()]], Circles :: [[integer()]], R :: integer()) -> integer().
circle_game(Toys, Circles, R) ->
  .
```

tab: Elixir

```elixir
defmodule Solution do
  @spec circle_game(toys :: [[integer]], circles :: [[integer]], r :: integer) :: integer
  def circle_game(toys, circles, r) do

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
          
