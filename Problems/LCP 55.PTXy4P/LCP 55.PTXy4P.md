---
tags:
  - leetcode/problem
questionId: LCP 55
title: 采集果实
translatedTitle: 采集果实
titleSlug: PTXy4P
aliases:
  - 采集果实
  - PTXy4P
  - 采集果实
lcLinks:
  - https://leetcode.cn/problems/PTXy4P/
lcTopics:
  - '[[array]]'
lcDifficulty: Easy
lcAcRate: 73.8%
similarQuestions: []
grade: ⭐⭐⭐⭐⭐
likes: 10
dislikes: 0
favorites: []
solutions: []
notes: []
cssclasses: []
created: 2024-08-13 00:28
updated:
---

**Nav:** << previous: [[LCP 54.s5kipK]] | next: [[LCP 56.6UEx57]] >>

---

## Description

~~~tabs
tab: English

No description

---

[submissions](https://leetcode.com/problems/PTXy4P/submissions/) | [solutions](https://leetcode.com/problems/PTXy4P/solutions/)


tab: 中文

欢迎各位勇者来到力扣新手村，本次训练内容为「采集果实」。

在新手村中，各位勇者需要采集一些果实来制作药剂。`time[i]` 表示勇者每次采集 `1～limit` 颗第 `i` 种类型的果实需要的时间（即每次最多可以采集 `limit` 颗果实）。

当前勇者需要完成「采集若干批果实」的任务， `fruits[j] = [type, num]` 表示第 `j` 批需要采集 `num` 颗 `type` 类型的果实。采集规则如下：
- 按 `fruits` 给定的顺序**依次**采集每一批次
- 采集完当前批次的果实才能开始采集下一批次
- 勇者完成当前批次的采集后将**清空背包**（即多余的果实将清空）

请计算并返回勇者完成采集任务最少需要的时间。


**示例 1：**
>输入：`time = [2,3,2], fruits = [[0,2],[1,4],[2,1]], limit = 3`
>
>输出：`10`
>
>解释：
>由于单次最多采集 3 颗
>第 0 批需要采集 2 颗第 0 类型果实，需要采集 1 次，耗时为 2\*1=2
>第 1 批需要采集 4 颗第 1 类型果实，需要采集 2 次，耗时为 3\*2=6
>第 2 批需要采集 1 颗第 2 类型果实，需要采集 1 次，耗时为 2\*1=2
>返回总耗时 2+6+2=10

**示例 2：**
>输入：`time = [1], fruits = [[0,3],[0,5]], limit = 2`
>
>输出：`5`
>
>解释：
>由于单次最多采集 2 颗
>第 0 批需要采集 3 颗第 0 类型果实，需要采集 2 次，耗时为 1\*2=2
>第 1 批需要采集 5 颗第 0 类型果实，需要采集 3 次，耗时为 1\*3=3
>需按照顺序依次采集，返回 2+3=5

**提示：**
- `1 <= time.length <= 100`
- `1 <= time[i] <= 100`
- `1 <= fruits.length <= 10^3`
- `0 <= fruits[i][0] < time.length`
- `1 <= fruits[i][1] < 10^3`
- `1 <= limit <= 100`

---

[提交记录](https://leetcode.cn/problems/PTXy4P/submissions/) | [题解](https://leetcode.cn/problems/PTXy4P/solution/)


~~~

## Code Snippets

~~~tabs
tab: C++

```cpp
class Solution {
public:
    int getMinimumTime(vector<int>& time, vector<vector<int>>& fruits, int limit) {

    }
};
```

tab: Java

```java
class Solution {
    public int getMinimumTime(int[] time, int[][] fruits, int limit) {

    }
}
```

tab: Python

```python
class Solution(object):
    def getMinimumTime(self, time, fruits, limit):
        """
        :type time: List[int]
        :type fruits: List[List[int]]
        :type limit: int
        :rtype: int
        """
```

tab: Python3

```python
class Solution:
    def getMinimumTime(self, time: List[int], fruits: List[List[int]], limit: int) -> int:
```

tab: C

```c


int getMinimumTime(int* time, int timeSize, int** fruits, int fruitsSize, int* fruitsColSize, int limit){

}
```

tab: C#

```csharp
public class Solution {
    public int GetMinimumTime(int[] time, int[][] fruits, int limit) {

    }
}
```

tab: JavaScript

```javascript
/**
 * @param {number[]} time
 * @param {number[][]} fruits
 * @param {number} limit
 * @return {number}
 */
var getMinimumTime = function(time, fruits, limit) {

};
```

tab: TypeScript

```typescript
function getMinimumTime(time: number[], fruits: number[][], limit: number): number {

};
```

tab: PHP

```php
class Solution {

    /**
     * @param Integer[] $time
     * @param Integer[][] $fruits
     * @param Integer $limit
     * @return Integer
     */
    function getMinimumTime($time, $fruits, $limit) {

    }
}
```

tab: Swift

```swift
class Solution {
    func getMinimumTime(_ time: [Int], _ fruits: [[Int]], _ limit: Int) -> Int {

    }
}
```

tab: Kotlin

```kotlin
class Solution {
    fun getMinimumTime(time: IntArray, fruits: Array<IntArray>, limit: Int): Int {

    }
}
```

tab: Go

```go
func getMinimumTime(time []int, fruits [][]int, limit int) int {

}
```

tab: Ruby

```ruby
# @param {Integer[]} time
# @param {Integer[][]} fruits
# @param {Integer} limit
# @return {Integer}
def get_minimum_time(time, fruits, limit)

end
```

tab: Scala

```scala
object Solution {
    def getMinimumTime(time: Array[Int], fruits: Array[Array[Int]], limit: Int): Int = {

    }
}
```

tab: Rust

```rust
impl Solution {
    pub fn get_minimum_time(time: Vec<i32>, fruits: Vec<Vec<i32>>, limit: i32) -> i32 {

    }
}
```

tab: Racket

```racket
(define/contract (get-minimum-time time fruits limit)
  (-> (listof exact-integer?) (listof (listof exact-integer?)) exact-integer? exact-integer?)

  )
```

tab: Erlang

```erlang
-spec get_minimum_time(Time :: [integer()], Fruits :: [[integer()]], Limit :: integer()) -> integer().
get_minimum_time(Time, Fruits, Limit) ->
  .
```

tab: Elixir

```elixir
defmodule Solution do
  @spec get_minimum_time(time :: [integer], fruits :: [[integer]], limit :: integer) :: integer
  def get_minimum_time(time, fruits, limit) do

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
          
