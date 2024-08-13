---
tags:
  - leetcode/problem
questionId: LCP 46
title: 志愿者调配
translatedTitle: 志愿者调配
titleSlug: 05ZEDJ
aliases:
  - 志愿者调配
  - 05ZEDJ
  - 志愿者调配
lcLinks:
  - https://leetcode.cn/problems/05ZEDJ/
lcTopics:
  - '[[graph]]'
  - '[[array]]'
  - '[[math]]'
lcDifficulty: Medium
lcAcRate: 46.9%
similarQuestions: []
grade: ⭐⭐⭐⭐⭐
likes: 12
dislikes: 0
favorites: []
solutions: []
notes: []
---

**Nav:** << previous: [[LCP 45.自行车炫技赛场]] | next: [[LCP 47.入场安检]] >>

---

## Description

~~~tabs
tab: English

No description

---

[submissions](https://leetcode.com/problems/05ZEDJ/submissions/) | [solutions](https://leetcode.com/problems/05ZEDJ/solutions/)


tab: 中文

「力扣挑战赛」有 `n` 个比赛场馆（场馆编号从 `0` 开始），场馆之间的通道分布情况记录于二维数组 `edges` 中，`edges[i]= [x, y]` 表示第 `i` 条通道连接场馆 `x` 和场馆 `y`(即两个场馆相邻)。初始每个场馆中都有一定人数的志愿者（不同场馆人数可能不同），后续 `m` 天每天均会根据赛事热度进行志愿者人数调配。调配方案分为如下三种：
1. 将编号为 `idx` 的场馆内的志愿者人数减半；
2. 将编号为 `idx` 的场馆相邻的场馆的志愿者人数都加上编号为 `idx` 的场馆的志愿者人数；
3. 将编号为 `idx` 的场馆相邻的场馆的志愿者人数都减去编号为 `idx` 的场馆的志愿者人数。

所有的调配信息记录于数组 `plans` 中，`plans[i] = [num,idx]` 表示第 `i` 天对编号 `idx` 的场馆执行了第 `num` 种调配方案。
在比赛结束后对调配方案进行复盘时，不慎将第 `0` 个场馆的**最终**志愿者人数丢失，只保留了**初始**所有场馆的志愿者总人数 `totalNum` ，以及记录了第 `1 ~ n-1` 个场馆的**最终**志愿者人数的一维数组 `finalCnt`。请你根据现有的信息求出初始每个场馆的志愿者人数，并按场馆编号顺序返回志愿者人数列表。

**注意：**
- 测试数据保证当某场馆进行第一种调配时，该场馆的志愿者人数一定为偶数；
- 测试数据保证当某场馆进行第三种调配时，该场馆的相邻场馆志愿者人数不为负数；
- 测试数据保证比赛开始时每个场馆的志愿者人数都不超过 `10^9`；
- 测试数据保证给定的场馆间的道路分布情况中不会出现自环、重边的情况。


**示例 1：**
>![image.png](https://pic.leetcode-cn.com/1630061228-gnZsOz-image.png)
> 输入：
>`finalCnt = [1,16], totalNum = 21, edges = [[0,1],[1,2]], plans = [[2,1],[1,0],[3,0]]`
>
> 输出：`[5,7,9]`
>
> 解释：
> ![image.png](https://pic.leetcode-cn.com/1630061300-WuVkeF-image.png){:height=200}


**示例 2 ：**
> 输入：
>`finalCnt = [4,13,4,3,8], totalNum = 54, edges = [[0,3],[1,3],[4,3],[2,3],[2,5]], plans = [[1,1],[3,3],[2,5],[1,0]]`
>
> 输出：`[10,16,9,4,7,8]`



**提示：**
- `2 <= n <= 5*10^4`
- `1 <= edges.length <= min((n * (n - 1)) / 2, 5*10^4)`
- `0 <= edges[i][0], edges[i][1] < n`
- `1 <= plans.length <= 10`
- `1 <= plans[i][0] <=3`
- `0 <= plans[i][1] < n`
- `finalCnt.length = n-1`
- `0 <= finalCnt[i] < 10^9`
- `0 <= totalNum < 5*10^13`


---

[提交记录](https://leetcode.cn/problems/05ZEDJ/submissions/) | [题解](https://leetcode.cn/problems/05ZEDJ/solution/)


~~~

## Code Snippets

~~~tabs
tab: C++

```cpp
class Solution {
public:
    vector<int> volunteerDeployment(vector<int>& finalCnt, long long totalNum, vector<vector<int>>& edges, vector<vector<int>>& plans) {

    }
};
```

tab: Java

```java
class Solution {
    public int[] volunteerDeployment(int[] finalCnt, long totalNum, int[][] edges, int[][] plans) {

    }
}
```

tab: Python

```python
class Solution(object):
    def volunteerDeployment(self, finalCnt, totalNum, edges, plans):
        """
        :type finalCnt: List[int]
        :type totalNum: int
        :type edges: List[List[int]]
        :type plans: List[List[int]]
        :rtype: List[int]
        """
```

tab: Python3

```python
class Solution:
    def volunteerDeployment(self, finalCnt: List[int], totalNum: int, edges: List[List[int]], plans: List[List[int]]) -> List[int]:
```

tab: C

```c


/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* volunteerDeployment(int* finalCnt, int finalCntSize, long long totalNum, int** edges, int edgesSize, int* edgesColSize, int** plans, int plansSize, int* plansColSize, int* returnSize){

}
```

tab: C#

```csharp
public class Solution {
    public int[] VolunteerDeployment(int[] finalCnt, long totalNum, int[][] edges, int[][] plans) {

    }
}
```

tab: JavaScript

```javascript
/**
 * @param {number[]} finalCnt
 * @param {number} totalNum
 * @param {number[][]} edges
 * @param {number[][]} plans
 * @return {number[]}
 */
var volunteerDeployment = function(finalCnt, totalNum, edges, plans) {

};
```

tab: TypeScript

```typescript
function volunteerDeployment(finalCnt: number[], totalNum: number, edges: number[][], plans: number[][]): number[] {

};
```

tab: PHP

```php
class Solution {

    /**
     * @param Integer[] $finalCnt
     * @param Integer $totalNum
     * @param Integer[][] $edges
     * @param Integer[][] $plans
     * @return Integer[]
     */
    function volunteerDeployment($finalCnt, $totalNum, $edges, $plans) {

    }
}
```

tab: Swift

```swift
class Solution {
    func volunteerDeployment(_ finalCnt: [Int], _ totalNum: Int, _ edges: [[Int]], _ plans: [[Int]]) -> [Int] {

    }
}
```

tab: Kotlin

```kotlin
class Solution {
    fun volunteerDeployment(finalCnt: IntArray, totalNum: Long, edges: Array<IntArray>, plans: Array<IntArray>): IntArray {

    }
}
```

tab: Dart

```dart
class Solution {
  List<int> volunteerDeployment(List<int> finalCnt, int totalNum, List<List<int>> edges, List<List<int>> plans) {

  }
}
```

tab: Go

```go
func volunteerDeployment(finalCnt []int, totalNum int64, edges [][]int, plans [][]int) []int {

}
```

tab: Ruby

```ruby
# @param {Integer[]} final_cnt
# @param {Integer} total_num
# @param {Integer[][]} edges
# @param {Integer[][]} plans
# @return {Integer[]}
def volunteer_deployment(final_cnt, total_num, edges, plans)

end
```

tab: Scala

```scala
object Solution {
    def volunteerDeployment(finalCnt: Array[Int], totalNum: Long, edges: Array[Array[Int]], plans: Array[Array[Int]]): Array[Int] = {

    }
}
```

tab: Rust

```rust
impl Solution {
    pub fn volunteer_deployment(final_cnt: Vec<i32>, total_num: i64, edges: Vec<Vec<i32>>, plans: Vec<Vec<i32>>) -> Vec<i32> {

    }
}
```

tab: Racket

```racket
(define/contract (volunteer-deployment finalCnt totalNum edges plans)
  (-> (listof exact-integer?) exact-integer? (listof (listof exact-integer?)) (listof (listof exact-integer?)) (listof exact-integer?))

  )
```

tab: Erlang

```erlang
-spec volunteer_deployment(FinalCnt :: [integer()], TotalNum :: integer(), Edges :: [[integer()]], Plans :: [[integer()]]) -> [integer()].
volunteer_deployment(FinalCnt, TotalNum, Edges, Plans) ->
  .
```

tab: Elixir

```elixir
defmodule Solution do
  @spec volunteer_deployment(final_cnt :: [integer], total_num :: integer, edges :: [[integer]], plans :: [[integer]]) :: [integer]
  def volunteer_deployment(final_cnt, total_num, edges, plans) do

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
          
