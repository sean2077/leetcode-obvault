---
tags:
  - leetcode/problem
questionId: LCP 40
title: 心算挑战
translatedTitle: 心算挑战
titleSlug: uOAnQW
aliases:
  - 心算挑战
  - uOAnQW
  - 心算挑战
lcLink: https://leetcode.com/problems/uOAnQW/
lcTopics:
  - '[[greedy]]'
  - '[[array]]'
  - '[[sorting]]'
lcDifficulty: Easy
lcAcRate: 40.5%
similarQuestions: []
grade: ⭐⭐⭐⭐⭐
likes: 116
dislikes: 0
favorites: []
solutions: []
notes: []
cssclasses: []
created: 2024-08-13 00:10
updated:
---

**Nav:** << previous: [[LCP 39.0jQkd0]] | next: [[LCP 41.fHi6rV]] >>

---

## Description

~~~tabs
tab: English

No description

---

[submissions](https://leetcode.com/problems/uOAnQW/submissions/) | [solutions](https://leetcode.com/problems/uOAnQW/solutions/)


tab: 中文

「力扣挑战赛」心算项目的挑战比赛中，要求选手从 `N` 张卡牌中选出 `cnt` 张卡牌，若这 `cnt` 张卡牌数字总和为偶数，则选手成绩「有效」且得分为 `cnt` 张卡牌数字总和。
给定数组 `cards` 和 `cnt`，其中 `cards[i]` 表示第 `i` 张卡牌上的数字。 请帮参赛选手计算最大的有效得分。若不存在获取有效得分的卡牌方案，则返回 0。

**示例 1：**
>输入：`cards = [1,2,8,9], cnt = 3`
>
>输出：`18`
>
>解释：选择数字为 1、8、9 的这三张卡牌，此时可获得最大的有效得分 1+8+9=18。

**示例 2：**
>输入：`cards = [3,3,1], cnt = 1`
>
>输出：`0`
>
>解释：不存在获取有效得分的卡牌方案。

**提示：**
- `1 <= cnt <= cards.length <= 10^5`
- `1 <= cards[i] <= 1000`




---

[提交记录](https://leetcode.cn/problems/uOAnQW/submissions/) | [题解](https://leetcode.cn/problems/uOAnQW/solution/)


~~~

## Code Snippets

~~~tabs
tab: C++

```cpp
class Solution {
public:
    int maxmiumScore(vector<int>& cards, int cnt) {

    }
};
```

tab: Java

```java
class Solution {
    public int maxmiumScore(int[] cards, int cnt) {

    }
}
```

tab: Python

```python
class Solution(object):
    def maxmiumScore(self, cards, cnt):
        """
        :type cards: List[int]
        :type cnt: int
        :rtype: int
        """
```

tab: Python3

```python
class Solution:
    def maxmiumScore(self, cards: List[int], cnt: int) -> int:
```

tab: C

```c


int maxmiumScore(int* cards, int cardsSize, int cnt){

}
```

tab: C#

```csharp
public class Solution {
    public int MaxmiumScore(int[] cards, int cnt) {

    }
}
```

tab: JavaScript

```javascript
/**
 * @param {number[]} cards
 * @param {number} cnt
 * @return {number}
 */
var maxmiumScore = function(cards, cnt) {

};
```

tab: TypeScript

```typescript
function maxmiumScore(cards: number[], cnt: number): number {

};
```

tab: PHP

```php
class Solution {

    /**
     * @param Integer[] $cards
     * @param Integer $cnt
     * @return Integer
     */
    function maxmiumScore($cards, $cnt) {

    }
}
```

tab: Swift

```swift
class Solution {
    func maxmiumScore(_ cards: [Int], _ cnt: Int) -> Int {

    }
}
```

tab: Kotlin

```kotlin
class Solution {
    fun maxmiumScore(cards: IntArray, cnt: Int): Int {

    }
}
```

tab: Dart

```dart
class Solution {
  int maxmiumScore(List<int> cards, int cnt) {

  }
}
```

tab: Go

```go
func maxmiumScore(cards []int, cnt int) int {

}
```

tab: Ruby

```ruby
# @param {Integer[]} cards
# @param {Integer} cnt
# @return {Integer}
def maxmium_score(cards, cnt)

end
```

tab: Scala

```scala
object Solution {
    def maxmiumScore(cards: Array[Int], cnt: Int): Int = {

    }
}
```

tab: Rust

```rust
impl Solution {
    pub fn maxmium_score(cards: Vec<i32>, cnt: i32) -> i32 {

    }
}
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
          
