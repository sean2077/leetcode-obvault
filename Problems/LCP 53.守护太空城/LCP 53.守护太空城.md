---
tags:
  - leetcode/problem
questionId: LCP 53
title: 守护太空城
translatedTitle: 守护太空城
titleSlug: EJvmW4
aliases:
  - 守护太空城
  - EJvmW4
  - 守护太空城
lcLinks:
  - https://leetcode.cn/problems/EJvmW4/
lcTopics:
  - '[[bit-manipulation]]'
  - '[[array]]'
  - '[[dynamic-programming]]'
  - '[[bitmask]]'
lcDifficulty: Hard
lcAcRate: 47.2%
similarQuestions: []
grade: ⭐⭐⭐⭐⭐
likes: 11
dislikes: 0
favorites: []
solutions: []
notes: []
---

**Nav:** << previous: [[LCP 52.二叉搜索树染色]] | next: [[LCP 54.夺回据点]] >>

---

## Description

~~~tabs
tab: English

No description

---

[submissions](https://leetcode.com/problems/EJvmW4/submissions/) | [solutions](https://leetcode.com/problems/EJvmW4/solutions/)


tab: 中文

<p>各位勇者请注意，力扣太空城发布陨石雨红色预警。</p>

<p>太空城中的一些舱室将要受到陨石雨的冲击，这些舱室按照编号 <code>0 ~ N</code>&nbsp;的顺序依次排列。为了阻挡陨石损毁舱室，太空城可以使用能量展开防护屏障，具体消耗如下：</p>

<ul>
	<li>选择一个舱室开启屏障，能量消耗为 <code>2</code></li>
	<li>选择相邻两个舱室开启联合屏障，能量消耗为 <code>3</code></li>
	<li>对于已开启的&nbsp;<strong>一个&nbsp;</strong>屏障，<strong>多维持一时刻</strong>，能量消耗为 <code>1</code></li>
</ul>

<p>已知陨石雨的影响范围和到达时刻，<code>time[i]</code>&nbsp;和 <code>position[i]</code>&nbsp;分别表示该陨石的到达时刻和冲击位置。请返回太空舱能够守护所有舱室所需要的最少能量。</p>

<p><strong>注意：</strong></p>

<ul>
	<li>同一时间，一个舱室不能被多个屏障覆盖</li>
	<li>陨石雨仅在到达时刻对冲击位置处的舱室有影响</li>
</ul>

<p><strong>示例 1：</strong></p>

<pre>
输入：time = [1,2,1], position = [6,3,3]

输出：5

解释：时刻 1，分别开启编号 3、6 舱室的屏障，能量消耗 2*2 = 4。时刻 2，维持编号 3 舱室的屏障，能量消耗 1。因此，最少需要能量 5。
</pre>

<p>&nbsp;</p>

<p><strong>示例 2：</strong></p>

<pre>
输入：time = [1,1,1,2,2,3,5], position = [1,2,3,1,2,1,3]

输出：9

解释：时刻 1，开启编号 1、2 舱室的联合屏障，能量消耗 3。时刻 1，开启编号 3 舱室的屏障，能量消耗 2 。时刻 2，维持编号 1、2 舱室的联合屏障，能量消耗 1。时刻 3，维持编号 1、2 舱室的联合屏障，能量消耗 1。时刻 5，重新开启编号 3 舱室的屏障，能量消耗 2。因此，最少需要能量 9。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= time.length == position.length &lt;= 500</code></li>
	<li><code>1 &lt;= time[i] &lt;= 5</code></li>
	<li><code>0 &lt;= position[i] &lt;= 100</code></li>
</ul>


---

[提交记录](https://leetcode.cn/problems/EJvmW4/submissions/) | [题解](https://leetcode.cn/problems/EJvmW4/solution/)


~~~

## Code Snippets

~~~tabs
tab: C++

```cpp
class Solution {
public:
    int defendSpaceCity(vector<int>& time, vector<int>& position) {

    }
};
```

tab: Java

```java
class Solution {
    public int defendSpaceCity(int[] time, int[] position) {

    }
}
```

tab: Python

```python
class Solution(object):
    def defendSpaceCity(self, time, position):
        """
        :type time: List[int]
        :type position: List[int]
        :rtype: int
        """
```

tab: Python3

```python
class Solution:
    def defendSpaceCity(self, time: List[int], position: List[int]) -> int:
```

tab: C

```c


int defendSpaceCity(int* time, int timeSize, int* position, int positionSize){

}
```

tab: C#

```csharp
public class Solution {
    public int DefendSpaceCity(int[] time, int[] position) {

    }
}
```

tab: JavaScript

```javascript
/**
 * @param {number[]} time
 * @param {number[]} position
 * @return {number}
 */
var defendSpaceCity = function(time, position) {

};
```

tab: TypeScript

```typescript
function defendSpaceCity(time: number[], position: number[]): number {

};
```

tab: PHP

```php
class Solution {

    /**
     * @param Integer[] $time
     * @param Integer[] $position
     * @return Integer
     */
    function defendSpaceCity($time, $position) {

    }
}
```

tab: Swift

```swift
class Solution {
    func defendSpaceCity(_ time: [Int], _ position: [Int]) -> Int {

    }
}
```

tab: Kotlin

```kotlin
class Solution {
    fun defendSpaceCity(time: IntArray, position: IntArray): Int {

    }
}
```

tab: Dart

```dart
class Solution {
  int defendSpaceCity(List<int> time, List<int> position) {

  }
}
```

tab: Go

```go
func defendSpaceCity(time []int, position []int) int {

}
```

tab: Ruby

```ruby
# @param {Integer[]} time
# @param {Integer[]} position
# @return {Integer}
def defend_space_city(time, position)

end
```

tab: Scala

```scala
object Solution {
    def defendSpaceCity(time: Array[Int], position: Array[Int]): Int = {

    }
}
```

tab: Rust

```rust
impl Solution {
    pub fn defend_space_city(time: Vec<i32>, position: Vec<i32>) -> i32 {

    }
}
```

tab: Racket

```racket
(define/contract (defend-space-city time position)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)

  )
```

tab: Erlang

```erlang
-spec defend_space_city(Time :: [integer()], Position :: [integer()]) -> integer().
defend_space_city(Time, Position) ->
  .
```

tab: Elixir

```elixir
defmodule Solution do
  @spec defend_space_city(time :: [integer], position :: [integer]) :: integer
  def defend_space_city(time, position) do

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
          
