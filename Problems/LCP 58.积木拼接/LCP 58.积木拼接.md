---
tags:
  - leetcode/problem
questionId: LCP 58
title: 积木拼接
translatedTitle: 积木拼接
titleSlug: De4qBB
aliases:
  - 积木拼接
  - De4qBB
  - 积木拼接
lcLinks:
  - https://leetcode.cn/problems/De4qBB/
lcTopics:
  - '[[array]]'
  - '[[backtracking]]'
  - '[[matrix]]'
lcDifficulty: Hard
lcAcRate: 37.7%
similarQuestions: []
grade: ⭐⭐⭐⭐⭐
likes: 5
dislikes: 0
favorites: []
solutions: []
notes: []
---

**Nav:** << previous: [[LCP 57.打地鼠]] | next: [[LCP 59.搭桥过河]] >>

---

## Description

~~~tabs
tab: English

No description

---

[submissions](https://leetcode.com/problems/De4qBB/submissions/) | [solutions](https://leetcode.com/problems/De4qBB/solutions/)


tab: 中文

欢迎各位勇者来到力扣城，本次试炼主题为「积木拼接」。
勇者面前有 `6` 片积木（厚度均为 1），每片积木的形状记录于二维字符串数组 `shapes` 中，`shapes[i]` 表示第 `i` 片积木，其中 `1` 表示积木对应位置无空缺，`0` 表示积木对应位置有空缺。
例如 `["010","111","010"]` 对应积木形状为
![image.png](https://pic.leetcode-cn.com/1616125620-nXMCxX-image.png)

拼接积木的规则如下：
- 积木片可以旋转、翻面
- 积木片边缘必须完全吻合才能拼接在一起
- **每片积木片 `shapes[i]` 的中心点在拼接时必须处于正方体对应面的中心点**

例如 `3*3`、`4*4` 的积木片的中心点如图所示（红色点）：
![middle_img_v2_c2d91eb5-9beb-4c06-9726-f7dae149d86g.png](https://pic.leetcode-cn.com/1650509082-wObiEp-middle_img_v2_c2d91eb5-9beb-4c06-9726-f7dae149d86g.png){:height="150px"}


请返回这 6 片积木能否拼接成一个**严丝合缝的正方体**且每片积木正好对应正方体的一个面。

**注意：**
- 输入确保每片积木均无空心情况（即输入数据保证对于大小 `N*N` 的 `shapes[i]`，内部的 `(N-2)*(N-2)` 的区域必然均为 1）
- 输入确保每片积木的所有 `1` 位置均连通

**示例 1：**
>输入：`shapes = [["000","110","000"],["110","011","000"],["110","011","110"],["000","010","111"],["011","111","011"],["011","010","000"]]`
>
>输出：`true`
>
>解释：
![cube.gif](https://pic.leetcode-cn.com/1616125823-hkXAeN-cube.gif)

**示例 2：**
>输入：`shapes = [["101","111","000"],["000","010","111"],["010","011","000"],["010","111","010"],["101","111","010"],["000","010","011"]]`
>
>输出：`false`
>
>解释： 
>由于每片积木片的中心点在拼接时必须处于正方体对应面的中心点，积木片 `["010","011","000"]` 不能作为 `["100","110","000"]` 使用，因此无法构成正方体


**提示：**
- `shapes.length == 6`
- `shapes[i].length == shapes[j].length`
- `shapes[i].length == shapes[i][j].length`
- `3 <= shapes[i].length <= 10`







---

[提交记录](https://leetcode.cn/problems/De4qBB/submissions/) | [题解](https://leetcode.cn/problems/De4qBB/solution/)


~~~

## Code Snippets

~~~tabs
tab: C++

```cpp
class Solution {
public:
    bool composeCube(vector<vector<string>>& shapes) {

    }
};
```

tab: Java

```java
class Solution {
    public boolean composeCube(String[][] shapes) {

    }
}
```

tab: Python

```python
class Solution(object):
    def composeCube(self, shapes):
        """
        :type shapes: List[List[str]]
        :rtype: bool
        """
```

tab: Python3

```python
class Solution:
    def composeCube(self, shapes: List[List[str]]) -> bool:
```

tab: C

```c


bool composeCube(char*** shapes, int shapesSize, int* shapesColSize){

}
```

tab: C#

```csharp
public class Solution {
    public bool ComposeCube(string[][] shapes) {

    }
}
```

tab: JavaScript

```javascript
/**
 * @param {string[][]} shapes
 * @return {boolean}
 */
var composeCube = function(shapes) {

};
```

tab: TypeScript

```typescript
function composeCube(shapes: string[][]): boolean {

};
```

tab: PHP

```php
class Solution {

    /**
     * @param String[][] $shapes
     * @return Boolean
     */
    function composeCube($shapes) {

    }
}
```

tab: Swift

```swift
class Solution {
    func composeCube(_ shapes: [[String]]) -> Bool {

    }
}
```

tab: Kotlin

```kotlin
class Solution {
    fun composeCube(shapes: Array<Array<String>>): Boolean {

    }
}
```

tab: Dart

```dart
class Solution {
  bool composeCube(List<List<String>> shapes) {

  }
}
```

tab: Go

```go
func composeCube(shapes [][]string) bool {

}
```

tab: Ruby

```ruby
# @param {String[][]} shapes
# @return {Boolean}
def compose_cube(shapes)

end
```

tab: Scala

```scala
object Solution {
    def composeCube(shapes: Array[Array[String]]): Boolean = {

    }
}
```

tab: Rust

```rust
impl Solution {
    pub fn compose_cube(shapes: Vec<Vec<String>>) -> bool {

    }
}
```

tab: Racket

```racket
(define/contract (compose-cube shapes)
  (-> (listof (listof string?)) boolean?)

  )
```

tab: Erlang

```erlang
-spec compose_cube(Shapes :: [[unicode:unicode_binary()]]) -> boolean().
compose_cube(Shapes) ->
  .
```

tab: Elixir

```elixir
defmodule Solution do
  @spec compose_cube(shapes :: [[String.t]]) :: boolean
  def compose_cube(shapes) do

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
          
