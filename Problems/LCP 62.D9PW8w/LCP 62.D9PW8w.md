---
tags:
  - leetcode/problem
questionId: LCP 62
title: 交通枢纽
translatedTitle: 交通枢纽
titleSlug: D9PW8w
aliases:
  - 交通枢纽
  - D9PW8w
  - 交通枢纽
lcLinks:
  - https://leetcode.cn/problems/D9PW8w/
lcTopics:
  - '[[graph]]'
lcDifficulty: Medium
lcAcRate: 63.5%
similarQuestions: []
grade: ⭐⭐⭐⭐⭐
likes: 11
dislikes: 0
favorites: []
solutions: []
notes: []
cssclasses: []
created: 2024-08-13 00:28
updated:
---

**Nav:** << previous: [[LCP 61.6CE719]] | next: [[LCP 63.EXvqDp]] >>

---

## Description

~~~tabs
tab: English

No description

---

[submissions](https://leetcode.com/problems/D9PW8w/submissions/) | [solutions](https://leetcode.com/problems/D9PW8w/solutions/)


tab: 中文

为了缓解「力扣嘉年华」期间的人流压力，组委会在活动期间开设了一些交通专线。`path[i] = [a, b]` 表示有一条从地点 `a`通往地点 `b` 的 **单向** 交通专线。
若存在一个地点，满足以下要求，我们则称之为 **交通枢纽**：
- 所有地点（除自身外）均有一条 **单向** 专线 **直接** 通往该地点；
- 该地点不存在任何 **通往其他地点** 的单向专线。

请返回交通专线的 **交通枢纽**。若不存在，则返回 `-1`。

**注意：**
- 对于任意一个地点，至少被一条专线连通。

**示例 1：**
>输入：`path = [[0,1],[0,3],[1,3],[2,0],[2,3]]`
>
>输出：`3`
>
>解释：如下图所示：
> 地点 `0,1,2` 各有一条通往地点 `3` 的交通专线，
> 且地点 `3` 不存在任何**通往其他地点**的交通专线。
>![image.png](https://pic.leetcode-cn.com/1663902572-yOlUCr-image.png){:width=200px}


**示例 2：**
>输入：`path = [[0,3],[1,0],[1,3],[2,0],[3,0],[3,2]]`
>
>输出：`-1`
>
>解释：如下图所示：不存在满足 **交通枢纽** 的地点。
>![image.png](https://pic.leetcode-cn.com/1663902595-McsEkY-image.png){:width=200px}

**提示：**
- `1 <= path.length <= 1000`
- `0 <= path[i][0], path[i][1] <= 1000`
- `path[i][0]` 与 `path[i][1]` 不相等

---

[提交记录](https://leetcode.cn/problems/D9PW8w/submissions/) | [题解](https://leetcode.cn/problems/D9PW8w/solution/)


~~~

## Code Snippets

~~~tabs
tab: C++

```cpp
class Solution {
public:
    int transportationHub(vector<vector<int>>& path) {

    }
};
```

tab: Java

```java
class Solution {
    public int transportationHub(int[][] path) {

    }
}
```

tab: Python

```python
class Solution(object):
    def transportationHub(self, path):
        """
        :type path: List[List[int]]
        :rtype: int
        """
```

tab: Python3

```python
class Solution:
    def transportationHub(self, path: List[List[int]]) -> int:
```

tab: C

```c


int transportationHub(int** path, int pathSize, int* pathColSize){

}
```

tab: C#

```csharp
public class Solution {
    public int TransportationHub(int[][] path) {

    }
}
```

tab: JavaScript

```javascript
/**
 * @param {number[][]} path
 * @return {number}
 */
var transportationHub = function(path) {

};
```

tab: TypeScript

```typescript
function transportationHub(path: number[][]): number {

};
```

tab: PHP

```php
class Solution {

    /**
     * @param Integer[][] $path
     * @return Integer
     */
    function transportationHub($path) {

    }
}
```

tab: Swift

```swift
class Solution {
    func transportationHub(_ path: [[Int]]) -> Int {

    }
}
```

tab: Kotlin

```kotlin
class Solution {
    fun transportationHub(path: Array<IntArray>): Int {

    }
}
```

tab: Dart

```dart
class Solution {
  int transportationHub(List<List<int>> path) {

  }
}
```

tab: Go

```go
func transportationHub(path [][]int) int {

}
```

tab: Ruby

```ruby
# @param {Integer[][]} path
# @return {Integer}
def transportation_hub(path)

end
```

tab: Scala

```scala
object Solution {
    def transportationHub(path: Array[Array[Int]]): Int = {

    }
}
```

tab: Rust

```rust
impl Solution {
    pub fn transportation_hub(path: Vec<Vec<i32>>) -> i32 {

    }
}
```

tab: Racket

```racket
(define/contract (transportation-hub path)
  (-> (listof (listof exact-integer?)) exact-integer?)

  )
```

tab: Erlang

```erlang
-spec transportation_hub(Path :: [[integer()]]) -> integer().
transportation_hub(Path) ->
  .
```

tab: Elixir

```elixir
defmodule Solution do
  @spec transportation_hub(path :: [[integer]]) :: integer
  def transportation_hub(path) do

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
          
