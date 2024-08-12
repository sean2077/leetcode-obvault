---
tags:
  - leetcode/problem
questionId: LCP 45
title: 自行车炫技赛场
translatedTitle: 自行车炫技赛场
titleSlug: kplEvH
aliases:
  - 自行车炫技赛场
  - kplEvH
  - 自行车炫技赛场
lcLinks:
  - https://leetcode.cn/problems/kplEvH/
lcTopics:
  - '[[depth-first-search]]'
  - '[[breadth-first-search]]'
  - '[[memoization]]'
  - '[[array]]'
  - '[[dynamic-programming]]'
  - '[[matrix]]'
lcDifficulty: Medium
lcAcRate: 30.9%
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

**Nav:** << previous: [[LCP 44.sZ59z6]] | next: [[LCP 46.05ZEDJ]] >>

---

## Description

~~~tabs
tab: English

No description

---

[submissions](https://leetcode.com/problems/kplEvH/submissions/) | [solutions](https://leetcode.com/problems/kplEvH/solutions/)


tab: 中文

「力扣挑战赛」中 `N*M` 大小的自行车炫技赛场的场地由一片连绵起伏的上下坡组成，场地的高度值记录于二维数组 `terrain` 中，场地的减速值记录于二维数组 `obstacle` 中。
- 若选手骑着自行车从高度为 `h1` 且减速值为 `o1` 的位置到高度为 `h2` 且减速值为 `o2` 的相邻位置（上下左右四个方向），速度变化值为 `h1-h2-o2`（负值减速，正值增速）。

选手初始位于坐标 `position` 处且初始速度为 1，请问选手可以刚好到其他哪些位置时速度依旧为 1。请以二维数组形式返回这些位置。若有多个位置则按行坐标升序排列，若有多个位置行坐标相同则按列坐标升序排列。

**注意：** 骑行过程中速度不能为零或负值

**示例 1：**
> 输入：`position = [0,0], terrain = [[0,0],[0,0]], obstacle = [[0,0],[0,0]]`
> 
> 输出：`[[0,1],[1,0],[1,1]]`
> 
> 解释：
> 由于当前场地属于平地，根据上面的规则，选手从`[0,0]`的位置出发都能刚好在其他处的位置速度为 1。

**示例 2：**
> 输入：`position = [1,1], terrain = [[5,0],[0,6]], obstacle = [[0,6],[7,0]]`
> 
> 输出：`[[0,1]]`
> 
> 解释：
> 选手从 `[1,1]` 处的位置出发，到 `[0,1]` 处的位置时恰好速度为 1。


**提示：**
- `n == terrain.length == obstacle.length`
- `m == terrain[i].length == obstacle[i].length`
- `1 <= n <= 100`
- `1 <= m <= 100`
- `0 <= terrain[i][j], obstacle[i][j] <= 100`
- `position.length == 2`
- `0 <= position[0] < n`
- `0 <= position[1] < m`

---

[提交记录](https://leetcode.cn/problems/kplEvH/submissions/) | [题解](https://leetcode.cn/problems/kplEvH/solution/)


~~~

## Code Snippets

~~~tabs
tab: C++

```cpp
class Solution {
public:
    vector<vector<int>> bicycleYard(vector<int>& position, vector<vector<int>>& terrain, vector<vector<int>>& obstacle) {

    }
};
```

tab: Java

```java
class Solution {
    public int[][] bicycleYard(int[] position, int[][] terrain, int[][] obstacle) {

    }
}
```

tab: Python

```python
class Solution(object):
    def bicycleYard(self, position, terrain, obstacle):
        """
        :type position: List[int]
        :type terrain: List[List[int]]
        :type obstacle: List[List[int]]
        :rtype: List[List[int]]
        """
```

tab: Python3

```python
class Solution:
    def bicycleYard(self, position: List[int], terrain: List[List[int]], obstacle: List[List[int]]) -> List[List[int]]:
```

tab: C

```c


/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** bicycleYard(int* position, int positionSize, int** terrain, int terrainSize, int* terrainColSize, int** obstacle, int obstacleSize, int* obstacleColSize, int* returnSize, int** returnColumnSizes){

}
```

tab: C#

```csharp
public class Solution {
    public int[][] BicycleYard(int[] position, int[][] terrain, int[][] obstacle) {

    }
}
```

tab: JavaScript

```javascript
/**
 * @param {number[]} position
 * @param {number[][]} terrain
 * @param {number[][]} obstacle
 * @return {number[][]}
 */
var bicycleYard = function(position, terrain, obstacle) {

};
```

tab: TypeScript

```typescript
function bicycleYard(position: number[], terrain: number[][], obstacle: number[][]): number[][] {

};
```

tab: PHP

```php
class Solution {

    /**
     * @param Integer[] $position
     * @param Integer[][] $terrain
     * @param Integer[][] $obstacle
     * @return Integer[][]
     */
    function bicycleYard($position, $terrain, $obstacle) {

    }
}
```

tab: Swift

```swift
class Solution {
    func bicycleYard(_ position: [Int], _ terrain: [[Int]], _ obstacle: [[Int]]) -> [[Int]] {

    }
}
```

tab: Kotlin

```kotlin
class Solution {
    fun bicycleYard(position: IntArray, terrain: Array<IntArray>, obstacle: Array<IntArray>): Array<IntArray> {

    }
}
```

tab: Dart

```dart
class Solution {
  List<List<int>> bicycleYard(List<int> position, List<List<int>> terrain, List<List<int>> obstacle) {

  }
}
```

tab: Go

```go
func bicycleYard(position []int, terrain [][]int, obstacle [][]int) [][]int {

}
```

tab: Ruby

```ruby
# @param {Integer[]} position
# @param {Integer[][]} terrain
# @param {Integer[][]} obstacle
# @return {Integer[][]}
def bicycle_yard(position, terrain, obstacle)

end
```

tab: Scala

```scala
object Solution {
    def bicycleYard(position: Array[Int], terrain: Array[Array[Int]], obstacle: Array[Array[Int]]): Array[Array[Int]] = {

    }
}
```

tab: Rust

```rust
impl Solution {
    pub fn bicycle_yard(position: Vec<i32>, terrain: Vec<Vec<i32>>, obstacle: Vec<Vec<i32>>) -> Vec<Vec<i32>> {

    }
}
```

tab: Racket

```racket
(define/contract (bicycle-yard position terrain obstacle)
  (-> (listof exact-integer?) (listof (listof exact-integer?)) (listof (listof exact-integer?)) (listof (listof exact-integer?)))

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
          
