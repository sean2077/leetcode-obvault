---
tags:
  - leetcode/problem
questionId: LCP 47
title: 入场安检
translatedTitle: 入场安检
titleSlug: oPs9Bm
aliases:
  - 入场安检
  - oPs9Bm
  - 入场安检
lcLink: https://leetcode.com/problems/oPs9Bm/
lcTopics:
  - '[[array]]'
  - '[[dynamic-programming]]'
lcDifficulty: Hard
lcAcRate: 48.2%
similarQuestions: []
grade: ⭐⭐⭐⭐⭐
likes: 18
dislikes: 0
favorites: []
solutions: []
notes: []
cssclasses: []
created: 2024-08-13 00:10
updated:
---

**Nav:** << previous: [[LCP 46.05ZEDJ]] | next: [[LCP 48.fsa7oZ]] >>

---

## Description

~~~tabs
tab: English

No description

---

[submissions](https://leetcode.com/problems/oPs9Bm/submissions/) | [solutions](https://leetcode.com/problems/oPs9Bm/solutions/)


tab: 中文

「力扣挑战赛」 的入场仪式马上就要开始了，由于安保工作的需要，设置了可容纳人数总和为 `M` 的 `N` 个安检室，`capacities[i]` 记录第 `i` 个安检室可容纳人数。安检室拥有两种类型：
- 先进先出：在安检室中的所有观众中，最早进入安检室的观众最先离开
- 后进先出：在安检室中的所有观众中，最晚进入安检室的观众最先离开

![c24754f1a5ff56989340ba5004dc5eda.gif](https://pic.leetcode-cn.com/1628843202-cdFPSt-c24754f1a5ff56989340ba5004dc5eda.gif)



恰好 `M+1` 位入场的观众（编号从 0 开始）需要排队**依次**入场安检， 入场安检的规则如下：
- 观众需要先进入编号 `0` 的安检室
- 当观众将进入编号 `i` 的安检室时（`0 <= i < N`)，
    - 若安检室未到达可容纳人数上限，该观众可直接进入；
    - 若安检室已到达可容纳人数上限，在该观众进入安检室之前需根据当前安检室类型选择一位观众离开后才能进入；
- 当观众离开编号 `i` 的安检室时 （`0 <= i < N-1`)，将进入编号 `i+1` 的安检室接受安检。

若可以任意设定每个安检室的类型，请问有多少种设定安检室类型的方案可以使得编号 `k` 的观众第一个通过最后一个安检室入场。


**注意：** 
- 观众不可主动离开安检室，只有当安检室容纳人数达到上限，且又有新观众需要进入时，才可根据安检室的类型选择一位观众离开；
- 由于方案数可能过大，请将答案对 `1000000007` 取模后返回。


**示例 1：**
> 输入：`capacities = [2,2,3], k = 2`
>
> 输出：`2`
> 解释：
> 存在两种设定的 `2` 种方案：
> - 方案 1：将编号为 `0` 、`1` 的实验室设置为 **后进先出** 的类型，编号为 `2` 的实验室设置为 **先进先出** 的类型；
> - 方案 2：将编号为 `0` 、`1` 的实验室设置为 **先进先出** 的类型，编号为 `2` 的实验室设置为 **后进先出** 的类型。
>
> 以下是方案 1 的示意图：
>![c60e38199a225ad62f13b954872edf9b.gif](https://pic.leetcode-cn.com/1628841618-bFKsnt-c60e38199a225ad62f13b954872edf9b.gif)



**示例 2：**
> 输入：`capacities = [3,3], k = 3`
>
> 输出：`0`

**示例 3：**
> 输入：`capacities = [4,3,2,2], k = 6`
>
> 输出：`2`

**提示:**
+ `1 <= capacities.length <= 200`
+ `1 <= capacities[i] <= 200`
+ `0 <= k <= sum(capacities)`


---

[提交记录](https://leetcode.cn/problems/oPs9Bm/submissions/) | [题解](https://leetcode.cn/problems/oPs9Bm/solution/)


~~~

## Code Snippets

~~~tabs
tab: C++

```cpp
class Solution {
public:
    int securityCheck(vector<int>& capacities, int k) {

    }
};
```

tab: Java

```java
class Solution {
    public int securityCheck(int[] capacities, int k) {

    }
}
```

tab: Python

```python
class Solution(object):
    def securityCheck(self, capacities, k):
        """
        :type capacities: List[int]
        :type k: int
        :rtype: int
        """
```

tab: Python3

```python
class Solution:
    def securityCheck(self, capacities: List[int], k: int) -> int:
```

tab: C

```c


int securityCheck(int* capacities, int capacitiesSize, int k){

}
```

tab: C#

```csharp
public class Solution {
    public int SecurityCheck(int[] capacities, int k) {

    }
}
```

tab: JavaScript

```javascript
/**
 * @param {number[]} capacities
 * @param {number} k
 * @return {number}
 */
var securityCheck = function(capacities, k) {

};
```

tab: TypeScript

```typescript
function securityCheck(capacities: number[], k: number): number {

};
```

tab: PHP

```php
class Solution {

    /**
     * @param Integer[] $capacities
     * @param Integer $k
     * @return Integer
     */
    function securityCheck($capacities, $k) {

    }
}
```

tab: Swift

```swift
class Solution {
    func securityCheck(_ capacities: [Int], _ k: Int) -> Int {

    }
}
```

tab: Kotlin

```kotlin
class Solution {
    fun securityCheck(capacities: IntArray, k: Int): Int {

    }
}
```

tab: Dart

```dart
class Solution {
  int securityCheck(List<int> capacities, int k) {

  }
}
```

tab: Go

```go
func securityCheck(capacities []int, k int) int {

}
```

tab: Ruby

```ruby
# @param {Integer[]} capacities
# @param {Integer} k
# @return {Integer}
def security_check(capacities, k)

end
```

tab: Scala

```scala
object Solution {
    def securityCheck(capacities: Array[Int], k: Int): Int = {

    }
}
```

tab: Rust

```rust
impl Solution {
    pub fn security_check(capacities: Vec<i32>, k: i32) -> i32 {

    }
}
```

tab: Racket

```racket
(define/contract (security-check capacities k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)

  )
```

tab: Erlang

```erlang
-spec security_check(Capacities :: [integer()], K :: integer()) -> integer().
security_check(Capacities, K) ->
  .
```

tab: Elixir

```elixir
defmodule Solution do
  @spec security_check(capacities :: [integer], k :: integer) :: integer
  def security_check(capacities, k) do

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
          
