---
tags:
  - leetcode/problem
questionId: LCP 74
title: 最强祝福力场
translatedTitle: 最强祝福力场
titleSlug: xepqZ5
aliases:
  - 最强祝福力场
  - xepqZ5
  - 最强祝福力场
lcLink: https://leetcode.com/problems/xepqZ5/
lcTopics: []
lcDifficulty: Medium
lcAcRate: 32.4%
similarQuestions: []
grade: ⭐⭐⭐⭐⭐
likes: 28
dislikes: 0
favorites: []
solutions: []
notes: []
cssclasses: []
created: 2024-08-13 00:10
updated:
---

**Nav:** << previous: [[LCP 73.0Zeoeg]] | next: [[LCP 75.rdmXM7]] >>

---

## Description

~~~tabs
tab: English

No description

---

[submissions](https://leetcode.com/problems/xepqZ5/submissions/) | [solutions](https://leetcode.com/problems/xepqZ5/solutions/)


tab: 中文

小扣在探索丛林的过程中，无意间发现了传说中“落寞的黄金之都”。而在这片建筑废墟的地带中，小扣使用探测仪监测到了存在某种带有「祝福」效果的力场。
经过不断的勘测记录，小扣将所有力场的分布都记录了下来。`forceField[i] = [x,y,side]` 表示第 `i` 片力场将覆盖以坐标 `(x,y)` 为中心，边长为 `side` 的正方形区域。

若任意一点的 **力场强度** 等于覆盖该点的力场数量，请求出在这片地带中 **力场强度** 最强处的 **力场强度**。

**注意：** 
- 力场范围的边缘同样被力场覆盖。

**示例 1：**
>输入：
>`forceField = [[0,0,1],[1,0,1]]`
>
>输出：`2`
>
>解释：如图所示，（0.5, 0) 处力场强度最强为 2， （0.5，-0.5）处力场强度同样是 2。
![image.png](https://pic.leetcode.cn/1681805536-zGfghe-image.png){:width=400px}


**示例 2：**
>输入：
>`forceField = [[4,4,6],[7,5,3],[1,6,2],[5,6,3]]`
>
>输出：`3`
>
>解释：如下图所示，
>`forceField[0]、forceField[1]、forceField[3]` 重叠的区域力场强度最大，返回 `3`
![image.png](https://pic.leetcode.cn/1681805437-HQkyZS-image.png){:width=500px}



**提示：**
- `1 <= forceField.length <= 100`
- `forceField[i].length == 3`
- `0 <= forceField[i][0], forceField[i][1] <= 10^9`
- `1 <= forceField[i][2] <= 10^9`

---

[提交记录](https://leetcode.cn/problems/xepqZ5/submissions/) | [题解](https://leetcode.cn/problems/xepqZ5/solution/)


~~~

## Code Snippets

~~~tabs
tab: C++

```cpp
class Solution {
public:
    int fieldOfGreatestBlessing(vector<vector<int>>& forceField) {

    }
};
```

tab: Java

```java
class Solution {
    public int fieldOfGreatestBlessing(int[][] forceField) {

    }
}
```

tab: Python

```python
class Solution(object):
    def fieldOfGreatestBlessing(self, forceField):
        """
        :type forceField: List[List[int]]
        :rtype: int
        """
```

tab: Python3

```python
class Solution:
    def fieldOfGreatestBlessing(self, forceField: List[List[int]]) -> int:
```

tab: C

```c
int fieldOfGreatestBlessing(int** forceField, int forceFieldSize, int* forceFieldColSize){

}
```

tab: C#

```csharp
public class Solution {
    public int FieldOfGreatestBlessing(int[][] forceField) {

    }
}
```

tab: JavaScript

```javascript
/**
 * @param {number[][]} forceField
 * @return {number}
 */
var fieldOfGreatestBlessing = function(forceField) {

};
```

tab: TypeScript

```typescript
function fieldOfGreatestBlessing(forceField: number[][]): number {

};
```

tab: PHP

```php
class Solution {

    /**
     * @param Integer[][] $forceField
     * @return Integer
     */
    function fieldOfGreatestBlessing($forceField) {

    }
}
```

tab: Swift

```swift
class Solution {
    func fieldOfGreatestBlessing(_ forceField: [[Int]]) -> Int {

    }
}
```

tab: Kotlin

```kotlin
class Solution {
    fun fieldOfGreatestBlessing(forceField: Array<IntArray>): Int {

    }
}
```

tab: Dart

```dart
class Solution {
  int fieldOfGreatestBlessing(List<List<int>> forceField) {

  }
}
```

tab: Go

```go
func fieldOfGreatestBlessing(forceField [][]int) int {

}
```

tab: Ruby

```ruby
# @param {Integer[][]} force_field
# @return {Integer}
def field_of_greatest_blessing(force_field)

end
```

tab: Scala

```scala
object Solution {
    def fieldOfGreatestBlessing(forceField: Array[Array[Int]]): Int = {

    }
}
```

tab: Rust

```rust
impl Solution {
    pub fn field_of_greatest_blessing(force_field: Vec<Vec<i32>>) -> i32 {

    }
}
```

tab: Racket

```racket
(define/contract (field-of-greatest-blessing forceField)
  (-> (listof (listof exact-integer?)) exact-integer?)

  )
```

tab: Erlang

```erlang
-spec field_of_greatest_blessing(ForceField :: [[integer()]]) -> integer().
field_of_greatest_blessing(ForceField) ->
  .
```

tab: Elixir

```elixir
defmodule Solution do
  @spec field_of_greatest_blessing(force_field :: [[integer]]) :: integer
  def field_of_greatest_blessing(force_field) do

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
          
