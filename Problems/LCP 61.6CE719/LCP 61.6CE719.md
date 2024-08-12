---
tags:
  - leetcode/problem
questionId: LCP 61
title: 气温变化趋势
translatedTitle: 气温变化趋势
titleSlug: 6CE719
aliases:
  - 气温变化趋势
  - 6CE719
  - 气温变化趋势
lcLinks:
  - https://leetcode.cn/problems/6CE719/
lcTopics:
  - '[[array]]'
lcDifficulty: Easy
lcAcRate: 70.4%
similarQuestions: []
grade: ⭐⭐⭐⭐⭐
likes: 33
dislikes: 0
favorites: []
solutions: []
notes: []
cssclasses: []
created: 2024-08-13 00:28
updated:
---

**Nav:** << previous: [[LCP 60.WInSav]] | next: [[LCP 62.D9PW8w]] >>

---

## Description

~~~tabs
tab: English

No description

---

[submissions](https://leetcode.com/problems/6CE719/submissions/) | [solutions](https://leetcode.com/problems/6CE719/solutions/)


tab: 中文

力扣城计划在两地设立「力扣嘉年华」的分会场，气象小组正在分析两地区的气温变化趋势，对于第 `i ~ (i+1)` 天的气温变化趋势，将根据以下规则判断：
- 若第 `i+1` 天的气温 **高于** 第 `i` 天，为 **上升** 趋势
- 若第 `i+1` 天的气温 **等于** 第 `i` 天，为 **平稳** 趋势
- 若第 `i+1` 天的气温 **低于** 第 `i` 天，为 **下降** 趋势

已知 `temperatureA[i]` 和 `temperatureB[i]` 分别表示第 `i` 天两地区的气温。
组委会希望找到一段天数尽可能多，且两地气温变化趋势相同的时间举办嘉年华活动。请分析并返回两地气温变化趋势**相同的最大连续天数**。
> 即最大的 `n`，使得第 `i~i+n` 天之间，两地气温变化趋势相同

**示例 1：**
>输入：
>`temperatureA = [21,18,18,18,31]`
>`temperatureB = [34,32,16,16,17]`
>
>输出：`2`
>
>解释：如下表所示， 第 `2～4` 天两地气温变化趋势相同，且持续时间最长，因此返回 `4-2=2`
![image.png](https://pic.leetcode-cn.com/1663902654-hlrSvs-image.png){:width=1000px}


**示例 2：**
>输入：
>`temperatureA = [5,10,16,-6,15,11,3]`
>`temperatureB = [16,22,23,23,25,3,-16]`
>
>输出：`3`

**提示：**
- `2 <= temperatureA.length == temperatureB.length <= 1000`
- `-20 <= temperatureA[i], temperatureB[i] <= 40`


---

[提交记录](https://leetcode.cn/problems/6CE719/submissions/) | [题解](https://leetcode.cn/problems/6CE719/solution/)


~~~

## Code Snippets

~~~tabs
tab: C++

```cpp
class Solution {
public:
    int temperatureTrend(vector<int>& temperatureA, vector<int>& temperatureB) {
        
    }
};
```

tab: Java

```java
class Solution {
    public int temperatureTrend(int[] temperatureA, int[] temperatureB) {
        
    }
}
```

tab: Python

```python
class Solution(object):
    def temperatureTrend(self, temperatureA, temperatureB):
        """
        :type temperatureA: List[int]
        :type temperatureB: List[int]
        :rtype: int
        """
        
```

tab: Python3

```python
class Solution:
    def temperatureTrend(self, temperatureA: List[int], temperatureB: List[int]) -> int:
        
```

tab: C

```c
int temperatureTrend(int* temperatureA, int temperatureASize, int* temperatureB, int temperatureBSize) {
    
}
```

tab: C#

```csharp
public class Solution {
    public int TemperatureTrend(int[] temperatureA, int[] temperatureB) {

    }
}
```

tab: JavaScript

```javascript
/**
 * @param {number[]} temperatureA
 * @param {number[]} temperatureB
 * @return {number}
 */
var temperatureTrend = function(temperatureA, temperatureB) {
    
};
```

tab: TypeScript

```typescript
function temperatureTrend(temperatureA: number[], temperatureB: number[]): number {

};
```

tab: PHP

```php
class Solution {

    /**
     * @param Integer[] $temperatureA
     * @param Integer[] $temperatureB
     * @return Integer
     */
    function temperatureTrend($temperatureA, $temperatureB) {

    }
}
```

tab: Swift

```swift
class Solution {
    func temperatureTrend(_ temperatureA: [Int], _ temperatureB: [Int]) -> Int {

    }
}
```

tab: Kotlin

```kotlin
class Solution {
    fun temperatureTrend(temperatureA: IntArray, temperatureB: IntArray): Int {

    }
}
```

tab: Dart

```dart
class Solution {
  int temperatureTrend(List<int> temperatureA, List<int> temperatureB) {

  }
}
```

tab: Go

```go
func temperatureTrend(temperatureA []int, temperatureB []int) int {
    
}
```

tab: Ruby

```ruby
# @param {Integer[]} temperature_a
# @param {Integer[]} temperature_b
# @return {Integer}
def temperature_trend(temperature_a, temperature_b)

end
```

tab: Scala

```scala
object Solution {
    def temperatureTrend(temperatureA: Array[Int], temperatureB: Array[Int]): Int = {

    }
}
```

tab: Rust

```rust
impl Solution {
    pub fn temperature_trend(temperature_a: Vec<i32>, temperature_b: Vec<i32>) -> i32 {

    }
}
```

tab: Racket

```racket
(define/contract (temperature-trend temperatureA temperatureB)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)

  )
```

tab: Erlang

```erlang
-spec temperature_trend(TemperatureA :: [integer()], TemperatureB :: [integer()]) -> integer().
temperature_trend(TemperatureA, TemperatureB) ->
  .
```

tab: Elixir

```elixir
defmodule Solution do
  @spec temperature_trend(temperature_a :: [integer], temperature_b :: [integer]) :: integer
  def temperature_trend(temperature_a, temperature_b) do

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
          
