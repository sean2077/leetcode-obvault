---
tags:
  - leetcode/problem
questionId: LCP 31
title: 变换的迷宫
translatedTitle: 变换的迷宫
titleSlug: Db3wC1
aliases:
  - 变换的迷宫
  - Db3wC1
  - 变换的迷宫
lcLinks:
  - https://leetcode.cn/problems/Db3wC1/
lcTopics:
  - '[[depth-first-search]]'
  - '[[breadth-first-search]]'
  - '[[array]]'
  - '[[dynamic-programming]]'
  - '[[matrix]]'
lcDifficulty: Hard
lcAcRate: 30.0%
similarQuestions: []
grade: ⭐⭐⭐⭐⭐
likes: 39
dislikes: 0
favorites: []
solutions: []
notes: []
cssclasses: []
created: 2024-08-13 00:28
updated:
---

**Nav:** << previous: [[LCP 30.p0NxJO]] | next: [[LCP 32.t3fKg1]] >>

---

## Description

~~~tabs
tab: English

No description

---

[submissions](https://leetcode.com/problems/Db3wC1/submissions/) | [solutions](https://leetcode.com/problems/Db3wC1/solutions/)


tab: 中文

某解密游戏中，有一个 N\*M 的迷宫，迷宫地形会随时间变化而改变，迷宫出口一直位于 `(n-1,m-1)` 位置。迷宫变化规律记录于 `maze` 中，`maze[i]` 表示 `i` 时刻迷宫的地形状态，`"."` 表示可通行空地，`"#"` 表示陷阱。

地形图初始状态记作 `maze[0]`，此时小力位于起点 `(0,0)`。此后每一时刻可选择往上、下、左、右其一方向走一步，或者停留在原地。

小力背包有以下两个魔法卷轴（卷轴使用一次后消失）：
+ 临时消除术：将指定位置在下一个时刻变为空地；
+ 永久消除术：将指定位置永久变为空地。

请判断在迷宫变化结束前（含最后时刻），小力能否在不经过任意陷阱的情况下到达迷宫出口呢？

**注意： 输入数据保证起点和终点在所有时刻均为空地。**

**示例 1：**
>输入：`maze = [[".#.","#.."],["...",".#."],[".##",".#."],["..#",".#."]]`
>
>输出：`true`
>
>解释：
![maze.gif](https://pic.leetcode-cn.com/1615892239-SCIjyf-maze.gif)


**示例 2：**
>输入：`maze = [[".#.","..."],["...","..."]]`
>
>输出：`false`
>
>解释：由于时间不够，小力无法到达终点逃出迷宫。

**示例 3：**
>输入：`maze = [["...","...","..."],[".##","###","##."],[".##","###","##."],[".##","###","##."],[".##","###","##."],[".##","###","##."],[".##","###","##."]]`
>
>输出：`false`
>
>解释：由于道路不通，小力无法到达终点逃出迷宫。

**提示：**
- `1 <= maze.length <= 100`
- `1 <= maze[i].length, maze[i][j].length <= 50`
- `maze[i][j]` 仅包含 `"."`、`"#"`

---

[提交记录](https://leetcode.cn/problems/Db3wC1/submissions/) | [题解](https://leetcode.cn/problems/Db3wC1/solution/)


~~~

## Code Snippets

~~~tabs
tab: C++

```cpp
class Solution {
public:
    bool escapeMaze(vector<vector<string>>& maze) {

    }
};
```

tab: Java

```java
class Solution {
    public boolean escapeMaze(List<List<String>> maze) {

    }
}
```

tab: Python

```python
class Solution(object):
    def escapeMaze(self, maze):
        """
        :type maze: List[List[str]]
        :rtype: bool
        """
```

tab: Python3

```python
class Solution:
    def escapeMaze(self, maze: List[List[str]]) -> bool:
```

tab: C

```c


bool escapeMaze(char*** maze, int mazeSize, int* mazeColSize){

}
```

tab: C#

```csharp
public class Solution {
    public bool EscapeMaze(string[][] maze) {

    }
}
```

tab: JavaScript

```javascript
/**
 * @param {string[][]} maze
 * @return {boolean}
 */
var escapeMaze = function(maze) {

};
```

tab: TypeScript

```typescript
function escapeMaze(maze: string[][]): boolean {

};
```

tab: PHP

```php
class Solution {

    /**
     * @param String[][] $maze
     * @return Boolean
     */
    function escapeMaze($maze) {

    }
}
```

tab: Swift

```swift
class Solution {
    func escapeMaze(_ maze: [[String]]) -> Bool {

    }
}
```

tab: Kotlin

```kotlin
class Solution {
    fun escapeMaze(maze: Array<Array<String>>): Boolean {

    }
}
```

tab: Go

```go
func escapeMaze(maze [][]string) bool {

}
```

tab: Ruby

```ruby
# @param {String[][]} maze
# @return {Boolean}
def escape_maze(maze)

end
```

tab: Scala

```scala
object Solution {
    def escapeMaze(maze: Array[Array[String]]): Boolean = {

    }
}
```

tab: Rust

```rust
impl Solution {
    pub fn escape_maze(maze: Vec<Vec<String>>) -> bool {

    }
}
```

tab: Racket

```racket
(define/contract (escape-maze maze)
  (-> (listof (listof string?)) boolean?)

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
          
