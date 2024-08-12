---
tags:
  - leetcode/problem
questionId: LCP 35
title: 电动车游城市
translatedTitle: 电动车游城市
titleSlug: DFPeFJ
aliases:
  - 电动车游城市
  - DFPeFJ
  - 电动车游城市
lcLinks:
  - https://leetcode.cn/problems/DFPeFJ/
lcTopics:
  - '[[graph]]'
  - '[[shortest-path]]'
  - '[[heap-priority-queue]]'
lcDifficulty: Hard
lcAcRate: 50.9%
similarQuestions: []
grade: ⭐⭐⭐⭐⭐
likes: 45
dislikes: 0
favorites: []
solutions: []
notes: []
cssclasses: []
created: 2024-08-13 00:28
updated:
---

**Nav:** << previous: [[LCP 34.er-cha-shu-ran-se-UGC]] | next: [[LCP 36.Up5XYM]] >>

---

## Description

~~~tabs
tab: English

No description

---

[submissions](https://leetcode.com/problems/DFPeFJ/submissions/) | [solutions](https://leetcode.com/problems/DFPeFJ/solutions/)


tab: 中文

小明的电动车电量充满时可行驶距离为 `cnt`，每行驶 1 单位距离消耗 1 单位电量，且花费 1 单位时间。小明想选择电动车作为代步工具。地图上共有 N 个景点，景点编号为 0 ~ N-1。他将地图信息以 `[城市 A 编号,城市 B 编号,两城市间距离]` 格式整理在在二维数组 `paths`，表示城市 A、B 间存在双向通路。初始状态，电动车电量为 0。每个城市都设有充电桩，`charge[i]` 表示第 i 个城市每充 1 单位电量需要花费的单位时间。请返回小明最少需要花费多少单位时间从起点城市 `start` 抵达终点城市 `end`。


**示例 1：**
>输入：`paths = [[1,3,3],[3,2,1],[2,1,3],[0,1,4],[3,0,5]], cnt = 6, start = 1, end = 0, charge = [2,10,4,1]`
>
>输出：`43`
>
>解释：最佳路线为：1->3->0。
>在城市 1 仅充 3 单位电至城市 3，然后在城市 3 充 5 单位电，行驶至城市 5。
>充电用时共 3\*10 + 5\*1= 35
>行驶用时 3 + 5 = 8，此时总用时最短 43。
![image.png](https://pic.leetcode-cn.com/1616125304-mzVxIV-image.png)




**示例 2：**
>输入：`paths = [[0,4,2],[4,3,5],[3,0,5],[0,1,5],[3,2,4],[1,2,8]], cnt = 8, start = 0, end = 2, charge = [4,1,1,3,2]`
>
>输出：`38`
>
>解释：最佳路线为：0->4->3->2。
>城市 0 充电 2 单位，行驶至城市 4 充电 8 单位，行驶至城市 3 充电 1 单位，最终行驶至城市 2。
>充电用时 4\*2+2\*8+3\*1 = 27
>行驶用时 2+5+4 = 11，总用时最短 38。

**提示：**
- `1 <= paths.length <= 200`
- `paths[i].length == 3`
- `2 <= charge.length == n <= 100`
- `0 <= path[i][0],path[i][1],start,end < n`
- `1 <= cnt <= 100`
- `1 <= path[i][2] <= cnt`
- `1 <= charge[i] <= 100`
- 题目保证所有城市相互可以到达

---

[提交记录](https://leetcode.cn/problems/DFPeFJ/submissions/) | [题解](https://leetcode.cn/problems/DFPeFJ/solution/)


~~~

## Code Snippets

~~~tabs
tab: C++

```cpp
class Solution {
public:
    int electricCarPlan(vector<vector<int>>& paths, int cnt, int start, int end, vector<int>& charge) {

    }
};
```

tab: Java

```java
class Solution {
    public int electricCarPlan(int[][] paths, int cnt, int start, int end, int[] charge) {

    }
}
```

tab: Python

```python
class Solution(object):
    def electricCarPlan(self, paths, cnt, start, end, charge):
        """
        :type paths: List[List[int]]
        :type cnt: int
        :type start: int
        :type end: int
        :type charge: List[int]
        :rtype: int
        """
```

tab: Python3

```python
class Solution:
    def electricCarPlan(self, paths: List[List[int]], cnt: int, start: int, end: int, charge: List[int]) -> int:
```

tab: C

```c


int electricCarPlan(int** paths, int pathsSize, int* pathsColSize, int cnt, int start, int end, int* charge, int chargeSize){

}
```

tab: C#

```csharp
public class Solution {
    public int ElectricCarPlan(int[][] paths, int cnt, int start, int end, int[] charge) {

    }
}
```

tab: JavaScript

```javascript
/**
 * @param {number[][]} paths
 * @param {number} cnt
 * @param {number} start
 * @param {number} end
 * @param {number[]} charge
 * @return {number}
 */
var electricCarPlan = function(paths, cnt, start, end, charge) {

};
```

tab: TypeScript

```typescript
function electricCarPlan(paths: number[][], cnt: number, start: number, end: number, charge: number[]): number {

};
```

tab: PHP

```php
class Solution {

    /**
     * @param Integer[][] $paths
     * @param Integer $cnt
     * @param Integer $start
     * @param Integer $end
     * @param Integer[] $charge
     * @return Integer
     */
    function electricCarPlan($paths, $cnt, $start, $end, $charge) {

    }
}
```

tab: Swift

```swift
class Solution {
    func electricCarPlan(_ paths: [[Int]], _ cnt: Int, _ start: Int, _ end: Int, _ charge: [Int]) -> Int {

    }
}
```

tab: Kotlin

```kotlin
class Solution {
    fun electricCarPlan(paths: Array<IntArray>, cnt: Int, start: Int, end: Int, charge: IntArray): Int {

    }
}
```

tab: Dart

```dart
class Solution {
  int electricCarPlan(List<List<int>> paths, int cnt, int start, int end, List<int> charge) {

  }
}
```

tab: Go

```go
func electricCarPlan(paths [][]int, cnt int, start int, end int, charge []int) int {

}
```

tab: Ruby

```ruby
# @param {Integer[][]} paths
# @param {Integer} cnt
# @param {Integer} start
# @param {Integer} end
# @param {Integer[]} charge
# @return {Integer}
def electric_car_plan(paths, cnt, start, end, charge)

end
```

tab: Scala

```scala
object Solution {
    def electricCarPlan(paths: Array[Array[Int]], cnt: Int, start: Int, end: Int, charge: Array[Int]): Int = {

    }
}
```

tab: Rust

```rust
impl Solution {
    pub fn electric_car_plan(paths: Vec<Vec<i32>>, cnt: i32, start: i32, end: i32, charge: Vec<i32>) -> i32 {

    }
}
```

tab: Racket

```racket
(define/contract (electric-car-plan paths cnt start end charge)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer? exact-integer? (listof exact-integer?) exact-integer?)

  )
```

tab: Erlang

```erlang
-spec electric_car_plan(Paths :: [[integer()]], Cnt :: integer(), Start :: integer(), End :: integer(), Charge :: [integer()]) -> integer().
electric_car_plan(Paths, Cnt, Start, End, Charge) ->
  .
```

tab: Elixir

```elixir
defmodule Solution do
  @spec electric_car_plan(paths :: [[integer]], cnt :: integer, start :: integer, end :: integer, charge :: [integer]) :: integer
  def electric_car_plan(paths, cnt, start, end, charge) do

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
          
