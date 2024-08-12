---
tags:
  - leetcode/problem
questionId: LCP 78
title: 城墙防线
translatedTitle: 城墙防线
titleSlug: Nsibyl
aliases:
  - 城墙防线
  - Nsibyl
  - 城墙防线
lcLink: https://leetcode.com/problems/Nsibyl/
lcTopics: []
lcDifficulty: Medium
lcAcRate: 45.3%
similarQuestions: []
grade: ⭐⭐⭐⭐⭐
likes: 7
dislikes: 0
favorites: []
solutions: []
notes: []
cssclasses: []
created: 2024-08-13 00:10
updated:
---

**Nav:** << previous: [[LCP 77.W2ZX4X]] | next: [[LCP 79.kjpLFZ]] >>

---

## Description

~~~tabs
tab: English

No description

---

[submissions](https://leetcode.com/problems/Nsibyl/submissions/) | [solutions](https://leetcode.com/problems/Nsibyl/solutions/)


tab: 中文

在探险营地间，小扣意外发现了一片城墙遗迹，在探索期间，却不巧遇到迁徙中的兽群向他迎面冲来。情急之下小扣吹响了他的苍蓝笛，随着笛声响起，遗迹中的城墙逐渐发生了横向膨胀。
已知 `rampart[i] = [x,y]` 表示第 `i` 段城墙的初始所在区间。当城墙发生膨胀时，将遵循以下规则：
- 所有的城墙会同时膨胀相等的长度；
- 每个城墙可以向左、向右或向两个方向膨胀。

小扣为了确保自身的安全，需要在所有城墙均无重叠的情况下，让城墙尽可能的膨胀。请返回城墙可以膨胀的 **最大值** 。

**注意：**
- 初始情况下，所有城墙均不重叠，且 `rampart` 中的元素升序排列；
- 两侧的城墙可以向外无限膨胀。

**示例 1：**
>输入：`rampart = [[0,3],[4,5],[7,9]]`
>
>输出：`3`
>
>解释：如下图所示：
>`rampart[0]` 向左侧膨胀 3 个单位；
>`rampart[2]` 向右侧膨胀 3 个单位；
>`rampart[1]` 向左侧膨胀 1 个单位，向右膨胀 2 个单位。
>不存在膨胀更多的方案，返回 3。
![image.png](https://pic.leetcode.cn/1681717918-tWywrp-image.png){:width=750px}

**示例 2：**
>输入：`rampart = [[1,2],[5,8],[11,15],[18,25]]`
>
>输出：`4`

**提示：**
- `3 <= rampart.length <= 10^4`
- `rampart[i].length == 2`
- `0 <= rampart[i][0] < rampart[i][1] <= rampart[i+1][0] <= 10^8`

---

[提交记录](https://leetcode.cn/problems/Nsibyl/submissions/) | [题解](https://leetcode.cn/problems/Nsibyl/solution/)


~~~

## Code Snippets

~~~tabs
tab: C++

```cpp
class Solution {
public:
    int rampartDefensiveLine(vector<vector<int>>& rampart) {

    }
};
```

tab: Java

```java
class Solution {
    public int rampartDefensiveLine(int[][] rampart) {

    }
}
```

tab: Python

```python
class Solution(object):
    def rampartDefensiveLine(self, rampart):
        """
        :type rampart: List[List[int]]
        :rtype: int
        """
```

tab: Python3

```python
class Solution:
    def rampartDefensiveLine(self, rampart: List[List[int]]) -> int:
```

tab: C

```c
int rampartDefensiveLine(int** rampart, int rampartSize, int* rampartColSize){

}
```

tab: C#

```csharp
public class Solution {
    public int RampartDefensiveLine(int[][] rampart) {

    }
}
```

tab: JavaScript

```javascript
/**
 * @param {number[][]} rampart
 * @return {number}
 */
var rampartDefensiveLine = function(rampart) {

};
```

tab: TypeScript

```typescript
function rampartDefensiveLine(rampart: number[][]): number {

};
```

tab: PHP

```php
class Solution {

    /**
     * @param Integer[][] $rampart
     * @return Integer
     */
    function rampartDefensiveLine($rampart) {

    }
}
```

tab: Swift

```swift
class Solution {
    func rampartDefensiveLine(_ rampart: [[Int]]) -> Int {

    }
}
```

tab: Kotlin

```kotlin
class Solution {
    fun rampartDefensiveLine(rampart: Array<IntArray>): Int {

    }
}
```

tab: Dart

```dart
class Solution {
  int rampartDefensiveLine(List<List<int>> rampart) {

  }
}
```

tab: Go

```go
func rampartDefensiveLine(rampart [][]int) int {

}
```

tab: Ruby

```ruby
# @param {Integer[][]} rampart
# @return {Integer}
def rampart_defensive_line(rampart)

end
```

tab: Scala

```scala
object Solution {
    def rampartDefensiveLine(rampart: Array[Array[Int]]): Int = {

    }
}
```

tab: Rust

```rust
impl Solution {
    pub fn rampart_defensive_line(rampart: Vec<Vec<i32>>) -> i32 {

    }
}
```

tab: Racket

```racket
(define/contract (rampart-defensive-line rampart)
  (-> (listof (listof exact-integer?)) exact-integer?)

  )
```

tab: Erlang

```erlang
-spec rampart_defensive_line(Rampart :: [[integer()]]) -> integer().
rampart_defensive_line(Rampart) ->
  .
```

tab: Elixir

```elixir
defmodule Solution do
  @spec rampart_defensive_line(rampart :: [[integer]]) :: integer
  def rampart_defensive_line(rampart) do

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
          
