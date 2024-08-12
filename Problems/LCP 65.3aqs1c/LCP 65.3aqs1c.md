---
tags:
  - leetcode/problem
questionId: LCP 65
title: 舒适的湿度
translatedTitle: 舒适的湿度
titleSlug: 3aqs1c
aliases:
  - 舒适的湿度
  - 3aqs1c
  - 舒适的湿度
lcLinks:
  - https://leetcode.cn/problems/3aqs1c/
lcTopics:
  - '[[array]]'
  - '[[dynamic-programming]]'
lcDifficulty: Hard
lcAcRate: 47.5%
similarQuestions: []
grade: ⭐⭐⭐⭐⭐
likes: 15
dislikes: 0
favorites: []
solutions: []
notes: []
cssclasses: []
created: 2024-08-13 00:28
updated:
---

**Nav:** << previous: [[LCP 64.U7WvvU]] | next: [[LCP 66.600YaG]] >>

---

## Description

~~~tabs
tab: English

No description

---

[submissions](https://leetcode.com/problems/3aqs1c/submissions/) | [solutions](https://leetcode.com/problems/3aqs1c/solutions/)


tab: 中文

力扣嘉年华为了确保更舒适的游览环境条件，在会场的各处设置了湿度调节装置，这些调节装置受控于总控室中的一台控制器。
控制器中已经预设了一些调节指令，整数数组`operate[i]` 表示第 `i` 条指令增加空气湿度的大小。现在你可以将任意数量的指令修改为降低湿度（变化的数值不变），以确保湿度尽可能的适宜：
- 控制器会选择 **一段连续的指令** ，从而进行湿度调节的操作；
- 这段指令最终对湿度影响的绝对值，即为当前操作的「不适宜度」
- 在控制器所有可能的操作中，**最大** 的「不适宜度」即为「整体不适宜度」

请返回在所有修改指令的方案中，可以得到的 **最小** 「整体不适宜度」。

**示例 1：**
> 输入：`operate = [5,3,7]`
>
> 输出：`8`
>
> 解释：对于方案 `2` 的 `[5,3,-7]`
>操作指令 `[5],[3],[-7]` 的「不适宜度」分别为 `5,3,7`
>操作指令 `[5,3],[3,-7]` 的「不适宜度」分别为 `8,4`
>操作指令 `[5,3,-7]` 的「不适宜度」为 `1`，
>因此对于方案 `[5,3,-7]`的「整体不适宜度」为 `8`，其余方案的「整体不适宜度」均不小于 `8`，如下表所示：
![image.png](https://pic.leetcode-cn.com/1663902759-dgDCxn-image.png){:width=650px}

**示例 2：**
> 输入：`operate = [20,10]`
>
> 输出：`20`

**提示：**
- `1 <= operate.length <= 1000`
- `1 <= operate[i] <= 1000`

---

[提交记录](https://leetcode.cn/problems/3aqs1c/submissions/) | [题解](https://leetcode.cn/problems/3aqs1c/solution/)


~~~

## Code Snippets

~~~tabs
tab: C++

```cpp
class Solution {
public:
    int unSuitability(vector<int>& operate) {

    }
};
```

tab: Java

```java
class Solution {
    public int unSuitability(int[] operate) {

    }
}
```

tab: Python

```python
class Solution(object):
    def unSuitability(self, operate):
        """
        :type operate: List[int]
        :rtype: int
        """
```

tab: Python3

```python
class Solution:
    def unSuitability(self, operate: List[int]) -> int:
```

tab: C

```c


int unSuitability(int* operate, int operateSize){

}
```

tab: C#

```csharp
public class Solution {
    public int UnSuitability(int[] operate) {

    }
}
```

tab: JavaScript

```javascript
/**
 * @param {number[]} operate
 * @return {number}
 */
var unSuitability = function(operate) {

};
```

tab: TypeScript

```typescript
function unSuitability(operate: number[]): number {

};
```

tab: PHP

```php
class Solution {

    /**
     * @param Integer[] $operate
     * @return Integer
     */
    function unSuitability($operate) {

    }
}
```

tab: Swift

```swift
class Solution {
    func unSuitability(_ operate: [Int]) -> Int {

    }
}
```

tab: Kotlin

```kotlin
class Solution {
    fun unSuitability(operate: IntArray): Int {

    }
}
```

tab: Dart

```dart
class Solution {
  int unSuitability(List<int> operate) {

  }
}
```

tab: Go

```go
func unSuitability(operate []int) int {

}
```

tab: Ruby

```ruby
# @param {Integer[]} operate
# @return {Integer}
def un_suitability(operate)

end
```

tab: Scala

```scala
object Solution {
    def unSuitability(operate: Array[Int]): Int = {

    }
}
```

tab: Rust

```rust
impl Solution {
    pub fn un_suitability(operate: Vec<i32>) -> i32 {

    }
}
```

tab: Racket

```racket
(define/contract (un-suitability operate)
  (-> (listof exact-integer?) exact-integer?)

  )
```

tab: Erlang

```erlang
-spec un_suitability(Operate :: [integer()]) -> integer().
un_suitability(Operate) ->
  .
```

tab: Elixir

```elixir
defmodule Solution do
  @spec un_suitability(operate :: [integer]) :: integer
  def un_suitability(operate) do

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
          
