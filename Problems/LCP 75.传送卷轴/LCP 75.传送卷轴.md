---
tags:
  - leetcode/problem
questionId: LCP 75
title: 传送卷轴
translatedTitle: 传送卷轴
titleSlug: rdmXM7
aliases:
  - 传送卷轴
  - rdmXM7
  - 传送卷轴
lcLinks:
  - https://leetcode.cn/problems/rdmXM7/
lcTopics: []
lcDifficulty: Hard
lcAcRate: 39.1%
similarQuestions: []
grade: ⭐⭐⭐⭐⭐
likes: 10
dislikes: 0
favorites: []
solutions: []
notes: []
---

**Nav:** << previous: [[LCP 74.最强祝福力场]] | next: [[LCP 76.魔法棋盘]] >>

---

## Description

~~~tabs
tab: English

No description

---

[submissions](https://leetcode.com/problems/rdmXM7/submissions/) | [solutions](https://leetcode.com/problems/rdmXM7/solutions/)


tab: 中文

随着不断的深入，小扣来到了守护者之森寻找的魔法水晶。首先，他必须先通过守护者的考验。

考验的区域是一个正方形的迷宫，`maze[i][j]` 表示在迷宫 `i` 行 `j` 列的地形：
- 若为 `.` ，表示可以到达的空地；
- 若为 `#` ，表示不可到达的墙壁；
- 若为 `S` ，表示小扣的初始位置；
- 若为 `T` ，表示魔法水晶的位置。

小扣每次可以向 上、下、左、右 相邻的位置移动一格。而守护者拥有一份「传送魔法卷轴」，使用规则如下：
- 魔法需要在小扣位于 **空地** 时才能释放，发动后卷轴消失；；
- 发动后，小扣会被传送到水平或者竖直的镜像位置，且目标位置不得为墙壁(如下图所示)；
![image.png](https://pic.leetcode.cn/1681789509-wTekFu-image.png){:width=400px}

在使用卷轴后，小扣将被「附加负面效果」，因此小扣需要尽可能缩短传送后到达魔法水晶的距离。而守护者的目标是阻止小扣到达魔法水晶的位置；如果无法阻止，则尽可能 **增加** 小扣传送后到达魔法水晶的距离。
假设小扣和守护者都按最优策略行事，返回小扣需要在 「附加负面效果」的情况下 **最少** 移动多少次才能到达魔法水晶。如果无法到达，返回 `-1`。

**注意：**
- 守护者可以不使用卷轴；
- 传送后的镜像位置可能与原位置相同。

**示例 1：**
>输入：`maze = [".....","##S..","...#.","T.#..","###.."]`
>
>输出：`7`
>
>解释：如下图所示：
>守护者释放魔法的两个最佳的位置为 [2,0] 或 [3,1]：
>若小扣经过 [2,0]，守护者在该位置释放魔法，
>小扣被传送至 [2,4] 处且加上负面效果，此时小扣还需要移动 7 次才能到达魔法水晶；
>若小扣经过 [3,1]，守护者在该位置释放魔法，
>小扣被传送至 [3,3] 处且加上负面效果，此时小扣还需要移动 9 次才能到达魔法水晶；
>因此小扣负面效果下最少需要移动 7 次才能到达魔法水晶。
![image.png](https://pic.leetcode.cn/1681714676-gksEMT-image.png){:width=300px}


**示例 2：**
>输入：`maze = [".#..","..##",".#S.",".#.T"]`
>
>输出：`-1`
>
>解释：如下图所示。
>若小扣向下移动至 [3,2]，守护者使其传送至 [0,2]，小扣将无法到达魔法水晶；
>若小扣向右移动至 [2,3]，守护者使其传送至 [2,0]，小扣将无法到达魔法水晶；
![image.png](https://pic.leetcode.cn/1681714693-LsxKAh-image.png){:width=300px}


**示例 3：**
>输入：`maze = ["S###.","..###","#..##","##..#","###.T"]`
>
>输出：`5`
>
>解释：如下图所示：
>守护者需要小扣在空地才能释放，因此初始无法将其从 [0,0] 传送至 [0,4];
>当小扣移动至 [2,1] 时，释放卷轴将其传送至水平方向的镜像位置 [2,1]（为原位置）
>而后小扣需要移动 5 次到达魔法水晶
![image.png](https://pic.leetcode.cn/1681800985-KrSdru-image.png){:width=300px}

**提示：**
- `4 <= maze.length == maze[i].length <= 200`
- `maze[i][j]` 仅包含 `"."`、`"#"`、`"S"`、`"T"`

---

[提交记录](https://leetcode.cn/problems/rdmXM7/submissions/) | [题解](https://leetcode.cn/problems/rdmXM7/solution/)


~~~

## Code Snippets

~~~tabs
tab: C++

```cpp
class Solution {
public:
    int challengeOfTheKeeper(vector<string>& maze) {

    }
};
```

tab: Java

```java
class Solution {
    public int challengeOfTheKeeper(String[] maze) {

    }
}
```

tab: Python

```python
class Solution(object):
    def challengeOfTheKeeper(self, maze):
        """
        :type maze: List[str]
        :rtype: int
        """
```

tab: Python3

```python
class Solution:
    def challengeOfTheKeeper(self, maze: List[str]) -> int:
```

tab: C

```c
int challengeOfTheKeeper(char** maze, int mazeSize){

}
```

tab: C#

```csharp
public class Solution {
    public int ChallengeOfTheKeeper(string[] maze) {

    }
}
```

tab: JavaScript

```javascript
/**
 * @param {string[]} maze
 * @return {number}
 */
var challengeOfTheKeeper = function(maze) {

};
```

tab: TypeScript

```typescript
function challengeOfTheKeeper(maze: string[]): number {

};
```

tab: PHP

```php
class Solution {

    /**
     * @param String[] $maze
     * @return Integer
     */
    function challengeOfTheKeeper($maze) {

    }
}
```

tab: Swift

```swift
class Solution {
    func challengeOfTheKeeper(_ maze: [String]) -> Int {

    }
}
```

tab: Kotlin

```kotlin
class Solution {
    fun challengeOfTheKeeper(maze: Array<String>): Int {

    }
}
```

tab: Dart

```dart
class Solution {
  int challengeOfTheKeeper(List<String> maze) {

  }
}
```

tab: Go

```go
func challengeOfTheKeeper(maze []string) int {

}
```

tab: Ruby

```ruby
# @param {String[]} maze
# @return {Integer}
def challenge_of_the_keeper(maze)

end
```

tab: Scala

```scala
object Solution {
    def challengeOfTheKeeper(maze: Array[String]): Int = {

    }
}
```

tab: Rust

```rust
impl Solution {
    pub fn challenge_of_the_keeper(maze: Vec<String>) -> i32 {

    }
}
```

tab: Racket

```racket
(define/contract (challenge-of-the-keeper maze)
  (-> (listof string?) exact-integer?)

  )
```

tab: Erlang

```erlang
-spec challenge_of_the_keeper(Maze :: [unicode:unicode_binary()]) -> integer().
challenge_of_the_keeper(Maze) ->
  .
```

tab: Elixir

```elixir
defmodule Solution do
  @spec challenge_of_the_keeper(maze :: [String.t]) :: integer
  def challenge_of_the_keeper(maze) do

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
          
