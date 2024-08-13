---
tags:
  - leetcode/problem
questionId: LCP 39
title: 无人机方阵
translatedTitle: 无人机方阵
titleSlug: 0jQkd0
aliases:
  - 无人机方阵
  - 0jQkd0
  - 无人机方阵
lcLinks:
  - https://leetcode.cn/problems/0jQkd0/
lcTopics:
  - '[[array]]'
  - '[[hash-table]]'
  - '[[counting]]'
  - '[[matrix]]'
lcDifficulty: Easy
lcAcRate: 55.7%
similarQuestions: []
grade: ⭐⭐⭐⭐⭐
likes: 14
dislikes: 0
favorites: []
solutions: []
notes: []
---

**Nav:** << previous: [[LCP 38.守卫城堡]] | next: [[LCP 40.心算挑战]] >>

---

## Description

~~~tabs
tab: English

No description

---

[submissions](https://leetcode.com/problems/0jQkd0/submissions/) | [solutions](https://leetcode.com/problems/0jQkd0/solutions/)


tab: 中文

在 「力扣挑战赛」 开幕式的压轴节目 「无人机方阵」中，每一架无人机展示一种灯光颜色。 无人机方阵通过两种操作进行颜色图案变换：
- 调整无人机的位置布局
- 切换无人机展示的灯光颜色


给定两个大小均为 `N*M` 的二维数组 `source` 和 `target` 表示无人机方阵表演的两种颜色图案，由于无人机切换灯光颜色的耗能很大，请返回从 `source` 到 `target` 最少需要多少架无人机切换灯光颜色。


**注意：** 调整无人机的位置布局时无人机的位置可以随意变动。


**示例 1：**
> 输入：`source = [[1,3],[5,4]], target = [[3,1],[6,5]]`
>
> 输出：`1`
>
> 解释：
> 最佳方案为
将 `[0,1]` 处的无人机移动至 `[0,0]` 处；
将 `[0,0]` 处的无人机移动至 `[0,1]` 处；
将 `[1,0]` 处的无人机移动至 `[1,1]` 处；
将 `[1,1]` 处的无人机移动至 `[1,0]` 处，其灯光颜色切换为颜色编号为 `6` 的灯光；
因此从`source` 到 `target` 所需要的最少灯光切换次数为 1。
>![8819ccdd664e91c78cde3bba3c701986.gif](https://pic.leetcode-cn.com/1628823765-uCDaux-8819ccdd664e91c78cde3bba3c701986.gif){:height=300px}





**示例 2：**
> 输入：`source = [[1,2,3],[3,4,5]], target = [[1,3,5],[2,3,4]]`
>
> 输出：`0`
> 解释：
> 仅需调整无人机的位置布局，便可完成图案切换。因此不需要无人机切换颜色


**提示：**
`n == source.length == target.length`
`m == source[i].length == target[i].length`
`1 <= n, m <=100`
`1 <= source[i][j], target[i][j] <=10^4`





---

[提交记录](https://leetcode.cn/problems/0jQkd0/submissions/) | [题解](https://leetcode.cn/problems/0jQkd0/solution/)


~~~

## Code Snippets

~~~tabs
tab: C++

```cpp
class Solution {
public:
    int minimumSwitchingTimes(vector<vector<int>>& source, vector<vector<int>>& target) {

    }
};
```

tab: Java

```java
class Solution {
    public int minimumSwitchingTimes(int[][] source, int[][] target) {

    }
}
```

tab: Python

```python
class Solution(object):
    def minimumSwitchingTimes(self, source, target):
        """
        :type source: List[List[int]]
        :type target: List[List[int]]
        :rtype: int
        """
```

tab: Python3

```python
class Solution:
    def minimumSwitchingTimes(self, source: List[List[int]], target: List[List[int]]) -> int:
```

tab: C

```c


int minimumSwitchingTimes(int** source, int sourceSize, int* sourceColSize, int** target, int targetSize, int* targetColSize){

}
```

tab: C#

```csharp
public class Solution {
    public int MinimumSwitchingTimes(int[][] source, int[][] target) {

    }
}
```

tab: JavaScript

```javascript
/**
 * @param {number[][]} source
 * @param {number[][]} target
 * @return {number}
 */
var minimumSwitchingTimes = function(source, target) {

};
```

tab: TypeScript

```typescript
function minimumSwitchingTimes(source: number[][], target: number[][]): number {

};
```

tab: PHP

```php
class Solution {

    /**
     * @param Integer[][] $source
     * @param Integer[][] $target
     * @return Integer
     */
    function minimumSwitchingTimes($source, $target) {

    }
}
```

tab: Swift

```swift
class Solution {
    func minimumSwitchingTimes(_ source: [[Int]], _ target: [[Int]]) -> Int {

    }
}
```

tab: Kotlin

```kotlin
class Solution {
    fun minimumSwitchingTimes(source: Array<IntArray>, target: Array<IntArray>): Int {

    }
}
```

tab: Dart

```dart
class Solution {
  int minimumSwitchingTimes(List<List<int>> source, List<List<int>> target) {

  }
}
```

tab: Go

```go
func minimumSwitchingTimes(source [][]int, target [][]int) int {

}
```

tab: Ruby

```ruby
# @param {Integer[][]} source
# @param {Integer[][]} target
# @return {Integer}
def minimum_switching_times(source, target)

end
```

tab: Scala

```scala
object Solution {
    def minimumSwitchingTimes(source: Array[Array[Int]], target: Array[Array[Int]]): Int = {

    }
}
```

tab: Rust

```rust
impl Solution {
    pub fn minimum_switching_times(source: Vec<Vec<i32>>, target: Vec<Vec<i32>>) -> i32 {

    }
}
```

tab: Racket

```racket
(define/contract (minimum-switching-times source target)
  (-> (listof (listof exact-integer?)) (listof (listof exact-integer?)) exact-integer?)

  )
```

tab: Erlang

```erlang
-spec minimum_switching_times(Source :: [[integer()]], Target :: [[integer()]]) -> integer().
minimum_switching_times(Source, Target) ->
  .
```

tab: Elixir

```elixir
defmodule Solution do
  @spec minimum_switching_times(source :: [[integer]], target :: [[integer]]) :: integer
  def minimum_switching_times(source, target) do

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
          
