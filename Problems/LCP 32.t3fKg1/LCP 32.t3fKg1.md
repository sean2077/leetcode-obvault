---
tags:
  - leetcode/problem
questionId: LCP 32
title: 批量处理任务
translatedTitle: 批量处理任务
titleSlug: t3fKg1
aliases:
  - 批量处理任务
  - t3fKg1
  - 批量处理任务
lcLinks:
  - https://leetcode.cn/problems/t3fKg1/
lcTopics:
  - '[[greedy]]'
  - '[[array]]'
  - '[[heap-priority-queue]]'
lcDifficulty: Hard
lcAcRate: 40.3%
similarQuestions: []
grade: ⭐⭐⭐⭐⭐
likes: 49
dislikes: 0
favorites: []
solutions: []
notes: []
cssclasses: []
created: 2024-08-13 00:28
updated:
---

**Nav:** << previous: [[LCP 31.Db3wC1]] | next: [[LCP 33.o8SXZn]] >>

---

## Description

~~~tabs
tab: English

No description

---

[submissions](https://leetcode.com/problems/t3fKg1/submissions/) | [solutions](https://leetcode.com/problems/t3fKg1/solutions/)


tab: 中文

某实验室计算机待处理任务以 `[start,end,period]` 格式记于二维数组 `tasks`，表示完成该任务的时间范围为起始时间 `start` 至结束时间 `end` 之间，需要计算机投入 `period` 的时长，注意：
1. `period` 可为不连续时间
2. 首尾时间均包含在内

处于开机状态的计算机可同时处理任意多个任务，请返回电脑最少开机多久，可处理完所有任务。

**示例 1：**
>输入：`tasks = [[1,3,2],[2,5,3],[5,6,2]]`
>
>输出：`4`
>
>解释：
>tasks[0] 选择时间点 2、3；
>tasks[1] 选择时间点 2、3、5；
>tasks[2] 选择时间点 5、6；
>因此计算机仅需在时间点 2、3、5、6 四个时刻保持开机即可完成任务。

**示例 2：**
>输入：`tasks = [[2,3,1],[5,5,1],[5,6,2]]`
>
>输出：`3`
>
>解释：
>tasks[0] 选择时间点 2 或 3；
>tasks[1] 选择时间点 5；
>tasks[2] 选择时间点 5、6；
>因此计算机仅需在时间点 2、5、6 或 3、5、6 三个时刻保持开机即可完成任务。

**提示：**
- `2 <= tasks.length <= 10^5`
- `tasks[i].length == 3`
- `0 <= tasks[i][0] <= tasks[i][1] <= 10^9`
- `1 <= tasks[i][2] <= tasks[i][1]-tasks[i][0] + 1`

---

[提交记录](https://leetcode.cn/problems/t3fKg1/submissions/) | [题解](https://leetcode.cn/problems/t3fKg1/solution/)


~~~

## Code Snippets

~~~tabs
tab: C++

```cpp
class Solution {
public:
    int processTasks(vector<vector<int>>& tasks) {

    }
};
```

tab: Java

```java
class Solution {
    public int processTasks(int[][] tasks) {

    }
}
```

tab: Python

```python
class Solution(object):
    def processTasks(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: int
        """
```

tab: Python3

```python
class Solution:
    def processTasks(self, tasks: List[List[int]]) -> int:
```

tab: C

```c


int processTasks(int** tasks, int tasksSize, int* tasksColSize){

}
```

tab: C#

```csharp
public class Solution {
    public int ProcessTasks(int[][] tasks) {

    }
}
```

tab: JavaScript

```javascript
/**
 * @param {number[][]} tasks
 * @return {number}
 */
var processTasks = function(tasks) {

};
```

tab: TypeScript

```typescript
function processTasks(tasks: number[][]): number {

};
```

tab: PHP

```php
class Solution {

    /**
     * @param Integer[][] $tasks
     * @return Integer
     */
    function processTasks($tasks) {

    }
}
```

tab: Swift

```swift
class Solution {
    func processTasks(_ tasks: [[Int]]) -> Int {

    }
}
```

tab: Kotlin

```kotlin
class Solution {
    fun processTasks(tasks: Array<IntArray>): Int {

    }
}
```

tab: Dart

```dart
class Solution {
  int processTasks(List<List<int>> tasks) {

  }
}
```

tab: Go

```go
func processTasks(tasks [][]int) int {

}
```

tab: Ruby

```ruby
# @param {Integer[][]} tasks
# @return {Integer}
def process_tasks(tasks)

end
```

tab: Scala

```scala
object Solution {
    def processTasks(tasks: Array[Array[Int]]): Int = {

    }
}
```

tab: Rust

```rust
impl Solution {
    pub fn process_tasks(tasks: Vec<Vec<i32>>) -> i32 {

    }
}
```

tab: Racket

```racket
(define/contract (process-tasks tasks)
  (-> (listof (listof exact-integer?)) exact-integer?)

  )
```

tab: Erlang

```erlang
-spec process_tasks(Tasks :: [[integer()]]) -> integer().
process_tasks(Tasks) ->
  .
```

tab: Elixir

```elixir
defmodule Solution do
  @spec process_tasks(tasks :: [[integer]]) :: integer
  def process_tasks(tasks) do

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
          
