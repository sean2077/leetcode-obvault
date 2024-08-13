---
tags:
  - leetcode/problem
questionId: LCP 68
title: 美观的花束
translatedTitle: 美观的花束
titleSlug: 1GxJYY
aliases:
  - 美观的花束
  - 1GxJYY
  - 美观的花束
lcLinks:
  - https://leetcode.cn/problems/1GxJYY/
lcTopics:
  - '[[array]]'
  - '[[sliding-window]]'
lcDifficulty: Medium
lcAcRate: 52.7%
similarQuestions: []
grade: ⭐⭐⭐⭐⭐
likes: 18
dislikes: 0
favorites: []
solutions: []
notes: []
---

**Nav:** << previous: [[LCP 67.装饰树]] | next: [[LCP 69.Hello LeetCode!]] >>

---

## Description

~~~tabs
tab: English

No description

---

[submissions](https://leetcode.com/problems/1GxJYY/submissions/) | [solutions](https://leetcode.com/problems/1GxJYY/solutions/)


tab: 中文

力扣嘉年华的花店中从左至右摆放了一排鲜花，记录于整型一维矩阵 `flowers` 中每个数字表示该位置所种鲜花的品种编号。你可以选择一段区间的鲜花做成插花，且不能丢弃。
在你选择的插花中，如果每一品种的鲜花数量都不超过 `cnt` 朵，那么我们认为这束插花是 「美观的」。
> - 例如：`[5,5,5,6,6]` 中品种为 `5` 的花有 `3` 朵， 品种为 `6` 的花有 `2` 朵，**每一品种** 的数量均不超过 `3`

请返回在这一排鲜花中，共有多少种可选择的区间，使得插花是「美观的」。

**注意：**
- 答案需要以 `1e9 + 7 (1000000007)` 为底取模，如：计算初始结果为：`1000000008`，请返回 `1`

**示例 1：**
>输入：`flowers = [1,2,3,2], cnt = 1`
>
>输出：`8`
>
>解释：相同的鲜花不超过 `1` 朵，共有 `8` 种花束是美观的；
>长度为 `1` 的区间 `[1]、[2]、[3]、[2]` 均满足条件，共 `4` 种可选择区间
>长度为 `2` 的区间 `[1,2]、[2,3]、[3,2]` 均满足条件，共 `3` 种可选择区间
>长度为 `3` 的区间 `[1,2,3]` 满足条件，共 `1` 种可选择区间。
>区间 `[2,3,2],[1,2,3,2]` 都包含了 `2` 朵鲜花 `2` ，不满足条件。
>返回总数 `4+3+1 = 8`

**示例 2：**
>输入：`flowers = [5,3,3,3], cnt = 2`
>
>输出：`8`

**提示：**
- `1 <= flowers.length <= 10^5`
- `1 <= flowers[i] <= 10^5`
- `1 <= cnt <= 10^5`

---

[提交记录](https://leetcode.cn/problems/1GxJYY/submissions/) | [题解](https://leetcode.cn/problems/1GxJYY/solution/)


~~~

## Code Snippets

~~~tabs
tab: C++

```cpp
class Solution {
public:
    int beautifulBouquet(vector<int>& flowers, int cnt) {

    }
};
```

tab: Java

```java
class Solution {
    public int beautifulBouquet(int[] flowers, int cnt) {

    }
}
```

tab: Python

```python
class Solution(object):
    def beautifulBouquet(self, flowers, cnt):
        """
        :type flowers: List[int]
        :type cnt: int
        :rtype: int
        """
```

tab: Python3

```python
class Solution:
    def beautifulBouquet(self, flowers: List[int], cnt: int) -> int:
```

tab: C

```c


int beautifulBouquet(int* flowers, int flowersSize, int cnt){

}
```

tab: C#

```csharp
public class Solution {
    public int BeautifulBouquet(int[] flowers, int cnt) {

    }
}
```

tab: JavaScript

```javascript
/**
 * @param {number[]} flowers
 * @param {number} cnt
 * @return {number}
 */
var beautifulBouquet = function(flowers, cnt) {

};
```

tab: TypeScript

```typescript
function beautifulBouquet(flowers: number[], cnt: number): number {

};
```

tab: PHP

```php
class Solution {

    /**
     * @param Integer[] $flowers
     * @param Integer $cnt
     * @return Integer
     */
    function beautifulBouquet($flowers, $cnt) {

    }
}
```

tab: Swift

```swift
class Solution {
    func beautifulBouquet(_ flowers: [Int], _ cnt: Int) -> Int {

    }
}
```

tab: Kotlin

```kotlin
class Solution {
    fun beautifulBouquet(flowers: IntArray, cnt: Int): Int {

    }
}
```

tab: Dart

```dart
class Solution {
  int beautifulBouquet(List<int> flowers, int cnt) {

  }
}
```

tab: Go

```go
func beautifulBouquet(flowers []int, cnt int) int {

}
```

tab: Ruby

```ruby
# @param {Integer[]} flowers
# @param {Integer} cnt
# @return {Integer}
def beautiful_bouquet(flowers, cnt)

end
```

tab: Scala

```scala
object Solution {
    def beautifulBouquet(flowers: Array[Int], cnt: Int): Int = {

    }
}
```

tab: Rust

```rust
impl Solution {
    pub fn beautiful_bouquet(flowers: Vec<i32>, cnt: i32) -> i32 {

    }
}
```

tab: Racket

```racket
(define/contract (beautiful-bouquet flowers cnt)
  (-> (listof exact-integer?) exact-integer? exact-integer?)

  )
```

tab: Erlang

```erlang
-spec beautiful_bouquet(Flowers :: [integer()], Cnt :: integer()) -> integer().
beautiful_bouquet(Flowers, Cnt) ->
  .
```

tab: Elixir

```elixir
defmodule Solution do
  @spec beautiful_bouquet(flowers :: [integer], cnt :: integer) :: integer
  def beautiful_bouquet(flowers, cnt) do

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
          
