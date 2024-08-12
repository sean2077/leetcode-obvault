---
tags:
  - leetcode/problem
questionId: LCP 57
title: 打地鼠
translatedTitle: 打地鼠
titleSlug: ZbAuEH
aliases:
  - 打地鼠
  - ZbAuEH
  - 打地鼠
lcLink: https://leetcode.com/problems/ZbAuEH/
lcTopics:
  - '[[array]]'
  - '[[dynamic-programming]]'
  - '[[matrix]]'
  - '[[sorting]]'
lcDifficulty: Hard
lcAcRate: 28.1%
similarQuestions: []
grade: ⭐⭐⭐⭐⭐
likes: 14
dislikes: 0
favorites: []
solutions: []
notes: []
cssclasses: []
created: 2024-08-13 00:10
updated:
---

**Nav:** << previous: [[LCP 56.6UEx57]] | next: [[LCP 58.De4qBB]] >>

---

## Description

~~~tabs
tab: English

No description

---

[submissions](https://leetcode.com/problems/ZbAuEH/submissions/) | [solutions](https://leetcode.com/problems/ZbAuEH/solutions/)


tab: 中文

欢迎各位勇者来到力扣城，本次试炼主题为「打地鼠」。
![middle_img_v2_d5d09656-0616-4a80-845e-ece461c5ba9g.png](https://pic.leetcode-cn.com/1650273183-nZIijm-middle_img_v2_d5d09656-0616-4a80-845e-ece461c5ba9g.png){:height="200px"}
勇者面前有一个大小为 `3*3` 的打地鼠游戏机，地鼠将随机出现在各个位置，`moles[i] = [t,x,y]` 表示在第 `t` 秒会有地鼠出现在 `(x,y)` 位置上，并于第 `t+1` 秒该地鼠消失。

勇者有一把可敲打地鼠的锤子，初始时刻（即第 `0` 秒）锤子位于正中间的格子 `(1,1)`，锤子的使用规则如下：
- 锤子每经过 `1` 秒可以往上、下、左、右中的一个方向移动一格，也可以不移动
- 锤子只可敲击所在格子的地鼠，**敲击不耗时**

请返回勇者**最多**能够敲击多少只地鼠。

**注意：** 
- 输入用例保证在相同时间相同位置最多仅有一只地鼠


**示例 1：**
>输入： `moles = [[1,1,0],[2,0,1],[4,2,2]]`
>
>输出： `2`
>
>解释：
>第 0 秒，锤子位于 (1,1)
>第 1 秒，锤子移动至 (1,0) 并敲击地鼠
>第 2 秒，锤子移动至 (2,0)
>第 3 秒，锤子移动至 (2,1)
>第 4 秒，锤子移动至 (2,2) 并敲击地鼠
>因此勇者最多可敲击 2 只地鼠


**示例 2：**
>输入：`moles = [[2,0,2],[5,2,0],[4,1,0],[1,2,1],[3,0,2]]`
>
>输出：`3`
>
>解释：
>第 0 秒，锤子位于 (1,1)
>第 1 秒，锤子移动至 (2,1) 并敲击地鼠
>第 2 秒，锤子移动至 (1,1)
>第 3 秒，锤子移动至 (1,0)
>第 4 秒，锤子在 (1,0) 不移动并敲击地鼠
>第 5 秒，锤子移动至 (2,0) 并敲击地鼠
>因此勇者最多可敲击 3 只地鼠


**示例 3：**
>输入：`moles = [[0,1,0],[0,0,1]]`
>
>输出：`0`
>
>解释：
>第 0 秒，锤子初始位于 (1,1)，此时并不能敲击 (1,0)、(0,1) 位置处的地鼠


**提示：**
+ `1 <= moles.length <= 10^5`
+ `moles[i].length == 3`
+ `0 <= moles[i][0] <= 10^9`
+ `0 <= moles[i][1], moles[i][2] < 3`


---

[提交记录](https://leetcode.cn/problems/ZbAuEH/submissions/) | [题解](https://leetcode.cn/problems/ZbAuEH/solution/)


~~~

## Code Snippets

~~~tabs
tab: C++

```cpp
class Solution {
public:
    int getMaximumNumber(vector<vector<int>>& moles) {

    }
};
```

tab: Java

```java
class Solution {
    public int getMaximumNumber(int[][] moles) {

    }
}
```

tab: Python

```python
class Solution(object):
    def getMaximumNumber(self, moles):
        """
        :type moles: List[List[int]]
        :rtype: int
        """
```

tab: Python3

```python
class Solution:
    def getMaximumNumber(self, moles: List[List[int]]) -> int:
```

tab: C

```c


int getMaximumNumber(int** moles, int molesSize, int* molesColSize){

}
```

tab: C#

```csharp
public class Solution {
    public int GetMaximumNumber(int[][] moles) {

    }
}
```

tab: JavaScript

```javascript
/**
 * @param {number[][]} moles
 * @return {number}
 */
var getMaximumNumber = function(moles) {

};
```

tab: TypeScript

```typescript
function getMaximumNumber(moles: number[][]): number {

};
```

tab: PHP

```php
class Solution {

    /**
     * @param Integer[][] $moles
     * @return Integer
     */
    function getMaximumNumber($moles) {

    }
}
```

tab: Swift

```swift
class Solution {
    func getMaximumNumber(_ moles: [[Int]]) -> Int {

    }
}
```

tab: Kotlin

```kotlin
class Solution {
    fun getMaximumNumber(moles: Array<IntArray>): Int {

    }
}
```

tab: Dart

```dart
class Solution {
  int getMaximumNumber(List<List<int>> moles) {

  }
}
```

tab: Go

```go
func getMaximumNumber(moles [][]int) int {

}
```

tab: Ruby

```ruby
# @param {Integer[][]} moles
# @return {Integer}
def get_maximum_number(moles)

end
```

tab: Scala

```scala
object Solution {
    def getMaximumNumber(moles: Array[Array[Int]]): Int = {

    }
}
```

tab: Rust

```rust
impl Solution {
    pub fn get_maximum_number(moles: Vec<Vec<i32>>) -> i32 {

    }
}
```

tab: Racket

```racket
(define/contract (get-maximum-number moles)
  (-> (listof (listof exact-integer?)) exact-integer?)

  )
```

tab: Erlang

```erlang
-spec get_maximum_number(Moles :: [[integer()]]) -> integer().
get_maximum_number(Moles) ->
  .
```

tab: Elixir

```elixir
defmodule Solution do
  @spec get_maximum_number(moles :: [[integer]]) :: integer
  def get_maximum_number(moles) do

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
          
