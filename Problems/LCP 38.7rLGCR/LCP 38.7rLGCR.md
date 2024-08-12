---
tags:
  - leetcode/problem
questionId: LCP 38
title: 守卫城堡
translatedTitle: 守卫城堡
titleSlug: 7rLGCR
aliases:
  - 守卫城堡
  - 7rLGCR
  - 守卫城堡
lcLink: https://leetcode.com/problems/7rLGCR/
lcTopics:
  - '[[array]]'
  - '[[dynamic-programming]]'
  - '[[matrix]]'
lcDifficulty: Hard
lcAcRate: 56.2%
similarQuestions: []
grade: ⭐⭐⭐⭐⭐
likes: 12
dislikes: 0
favorites: []
solutions: []
notes: []
cssclasses: []
created: 2024-08-13 00:10
updated:
---

**Nav:** << previous: [[LCP 37.zui-xiao-ju-xing-mian-ji]] | next: [[LCP 39.0jQkd0]] >>

---

## Description

~~~tabs
tab: English

No description

---

[submissions](https://leetcode.com/problems/7rLGCR/submissions/) | [solutions](https://leetcode.com/problems/7rLGCR/solutions/)


tab: 中文

城堡守卫游戏的胜利条件为使恶魔无法从出生点到达城堡。游戏地图可视作 `2*N` 的方格图，记作字符串数组 `grid`，其中：
- `"."` 表示恶魔可随意通行的平地；
- `"#"` 表示恶魔不可通过的障碍物，玩家可通过在 **平地** 上设置障碍物，即将  `"."` 变为 `"#"` 以阻挡恶魔前进；
- `"S"` 表示恶魔出生点，将有大量的恶魔该点生成，恶魔可向上/向下/向左/向右移动，且无法移动至地图外；
- `"P"` 表示瞬移点，移动到 `"P"` 点的恶魔可被传送至任意一个 `"P"` 点，也可选择不传送；
- `"C"` 表示城堡。

然而在游戏中用于建造障碍物的金钱是有限的，请返回玩家最少需要放置几个障碍物才能获得胜利。若无论怎样放置障碍物均无法获胜，请返回 `-1`。

**注意：**
- 地图上可能有一个或多个出生点
- 地图上有且只有一个城堡

**示例 1**
>输入：`grid = ["S.C.P#P.", ".....#.S"]`
>
>输出：`3`
>
>解释：至少需要放置三个障碍物
![image.png](https://pic.leetcode-cn.com/1614828255-uuNdNJ-image.png)


**示例 2：**
>输入：`grid = ["SP#P..P#PC#.S", "..#P..P####.#"]`
>
>输出：`-1`
>
>解释：无论怎样修筑障碍物，均无法阻挡最左侧出生的恶魔到达城堡位置
![image.png](https://pic.leetcode-cn.com/1614828208-oFlpVs-image.png)

**示例 3：**
>输入：`grid = ["SP#.C.#PS", "P.#...#.P"]`
>
>输出：`0`
>
>解释：无需放置障碍物即可获得胜利
![image.png](https://pic.leetcode-cn.com/1614828242-oveClu-image.png)

**示例 4：**
>输入：`grid = ["CP.#.P.", "...S..S"]`
>
>输出：`4`
>
>解释：至少需要放置 4 个障碍物，示意图为放置方法之一
![image.png](https://pic.leetcode-cn.com/1614828218-sIAYkb-image.png)


**提示：**
- `grid.length == 2`
- `2 <= grid[0].length == grid[1].length <= 10^4`
- `grid[i][j]` 仅包含字符 `"."`、`"#"`、`"C"`、`"P"`、`"S"`


---

[提交记录](https://leetcode.cn/problems/7rLGCR/submissions/) | [题解](https://leetcode.cn/problems/7rLGCR/solution/)


~~~

## Code Snippets

~~~tabs
tab: C++

```cpp
class Solution {
public:
    int guardCastle(vector<string>& grid) {

    }
};
```

tab: Java

```java
class Solution {
    public int guardCastle(String[] grid) {

    }
}
```

tab: Python

```python
class Solution(object):
    def guardCastle(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
```

tab: Python3

```python
class Solution:
    def guardCastle(self, grid: List[str]) -> int:
```

tab: C

```c


int guardCastle(char** grid, int gridSize){

}
```

tab: C#

```csharp
public class Solution {
    public int GuardCastle(string[] grid) {

    }
}
```

tab: JavaScript

```javascript
/**
 * @param {string[]} grid
 * @return {number}
 */
var guardCastle = function(grid) {

};
```

tab: TypeScript

```typescript
function guardCastle(grid: string[]): number {

};
```

tab: PHP

```php
class Solution {

    /**
     * @param String[] $grid
     * @return Integer
     */
    function guardCastle($grid) {

    }
}
```

tab: Swift

```swift
class Solution {
    func guardCastle(_ grid: [String]) -> Int {

    }
}
```

tab: Kotlin

```kotlin
class Solution {
    fun guardCastle(grid: Array<String>): Int {

    }
}
```

tab: Dart

```dart
class Solution {
  int guardCastle(List<String> grid) {

  }
}
```

tab: Go

```go
func guardCastle(grid []string) int {

}
```

tab: Ruby

```ruby
# @param {String[]} grid
# @return {Integer}
def guard_castle(grid)

end
```

tab: Scala

```scala
object Solution {
    def guardCastle(grid: Array[String]): Int = {

    }
}
```

tab: Rust

```rust
impl Solution {
    pub fn guard_castle(grid: Vec<String>) -> i32 {

    }
}
```

tab: Racket

```racket
(define/contract (guard-castle grid)
  (-> (listof string?) exact-integer?)

  )
```

tab: Erlang

```erlang
-spec guard_castle(Grid :: [unicode:unicode_binary()]) -> integer().
guard_castle(Grid) ->
  .
```

tab: Elixir

```elixir
defmodule Solution do
  @spec guard_castle(grid :: [String.t]) :: integer
  def guard_castle(grid) do

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
          
