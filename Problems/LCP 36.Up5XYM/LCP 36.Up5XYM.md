---
tags:
  - leetcode/problem
questionId: LCP 36
title: 最多牌组数
translatedTitle: 最多牌组数
titleSlug: Up5XYM
aliases:
  - 最多牌组数
  - Up5XYM
  - 最多牌组数
lcLinks:
  - https://leetcode.cn/problems/Up5XYM/
lcTopics:
  - '[[array]]'
  - '[[dynamic-programming]]'
  - '[[sorting]]'
lcDifficulty: Hard
lcAcRate: 34.4%
similarQuestions: []
grade: ⭐⭐⭐⭐⭐
likes: 31
dislikes: 0
favorites: []
solutions: []
notes: []
cssclasses: []
created: 2024-08-13 00:28
updated:
---

**Nav:** << previous: [[LCP 35.DFPeFJ]] | next: [[LCP 37.zui-xiao-ju-xing-mian-ji]] >>

---

## Description

~~~tabs
tab: English

No description

---

[submissions](https://leetcode.com/problems/Up5XYM/submissions/) | [solutions](https://leetcode.com/problems/Up5XYM/solutions/)


tab: 中文

麻将的游戏规则中，共有两种方式凑成「一组牌」：
- 顺子：三张牌面数字连续的麻将，例如 [4,5,6]
- 刻子：三张牌面数字相同的麻将，例如 [10,10,10]

给定若干数字作为麻将牌的数值（记作一维数组 `tiles`），请返回所给 `tiles` 最多可组成的牌组数。

注意：凑成牌组时，每张牌仅能使用一次。

**示例 1：**
>输入：`tiles = [2,2,2,3,4]`
>
>输出：`1`
>
>解释：最多可以组合出 [2,2,2] 或者 [2,3,4] 其中一组牌。

**示例 2：**
>输入：`tiles = [2,2,2,3,4,1,3]`
>
>输出：`2`
>
>解释：最多可以组合出 [1,2,3] 与 [2,3,4] 两组牌。

**提示：**
- `1 <= tiles.length <= 10^5`
- `1 <= tiles[i] <= 10^9`

---

[提交记录](https://leetcode.cn/problems/Up5XYM/submissions/) | [题解](https://leetcode.cn/problems/Up5XYM/solution/)


~~~

## Code Snippets

~~~tabs
tab: C++

```cpp
class Solution {
public:
    int maxGroupNumber(vector<int>& tiles) {

    }
};
```

tab: Java

```java
class Solution {
    public int maxGroupNumber(int[] tiles) {

    }
}
```

tab: Python

```python
class Solution(object):
    def maxGroupNumber(self, tiles):
        """
        :type tiles: List[int]
        :rtype: int
        """
```

tab: Python3

```python
class Solution:
    def maxGroupNumber(self, tiles: List[int]) -> int:
```

tab: C

```c


int maxGroupNumber(int* tiles, int tilesSize){

}
```

tab: C#

```csharp
public class Solution {
    public int MaxGroupNumber(int[] tiles) {

    }
}
```

tab: JavaScript

```javascript
/**
 * @param {number[]} tiles
 * @return {number}
 */
var maxGroupNumber = function(tiles) {

};
```

tab: TypeScript

```typescript
function maxGroupNumber(tiles: number[]): number {

};
```

tab: PHP

```php
class Solution {

    /**
     * @param Integer[] $tiles
     * @return Integer
     */
    function maxGroupNumber($tiles) {

    }
}
```

tab: Swift

```swift
class Solution {
    func maxGroupNumber(_ tiles: [Int]) -> Int {

    }
}
```

tab: Kotlin

```kotlin
class Solution {
    fun maxGroupNumber(tiles: IntArray): Int {

    }
}
```

tab: Go

```go
func maxGroupNumber(tiles []int) int {

}
```

tab: Ruby

```ruby
# @param {Integer[]} tiles
# @return {Integer}
def max_group_number(tiles)

end
```

tab: Scala

```scala
object Solution {
    def maxGroupNumber(tiles: Array[Int]): Int = {

    }
}
```

tab: Rust

```rust
impl Solution {
    pub fn max_group_number(tiles: Vec<i32>) -> i32 {

    }
}
```

tab: Racket

```racket
(define/contract (max-group-number tiles)
  (-> (listof exact-integer?) exact-integer?)

  )
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
          
