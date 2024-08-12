---
tags:
  - leetcode/problem
questionId: LCS 02
title: 完成一半题目
translatedTitle: 完成一半题目
titleSlug: WqXACV
aliases:
  - 完成一半题目
  - WqXACV
  - 完成一半题目
lcLink: https://leetcode.com/problems/WqXACV/
lcTopics:
  - '[[greedy]]'
  - '[[array]]'
  - '[[hash-table]]'
  - '[[sorting]]'
lcDifficulty: Easy
lcAcRate: 64.6%
similarQuestions: []
grade: ⭐⭐⭐⭐⭐
likes: 21
dislikes: 0
favorites: []
solutions: []
notes: []
cssclasses: []
created: 2024-08-13 00:10
updated:
---

**Nav:** << previous: [[LCS 01.Ju9Xwi]] | next: [[LCS 03.YesdPw]] >>

---

## Description

~~~tabs
tab: English

No description

---

[submissions](https://leetcode.com/problems/WqXACV/submissions/) | [solutions](https://leetcode.com/problems/WqXACV/solutions/)


tab: 中文

有 `N` 位扣友参加了微软与力扣举办了「以扣会友」线下活动。主办方提供了 `2*N` 道题目，整型数组 `questions` 中每个数字对应了每道题目所涉及的知识点类型。
若每位扣友选择不同的一题，请返回被选的 `N` 道题目至少包含多少种知识点类型。


**示例 1：**
>输入：`questions = [2,1,6,2]`
>
>输出：`1`
>
>解释：有 2 位扣友在 4 道题目中选择 2 题。
> 可选择完成知识点类型为 2 的题目时，此时仅一种知识点类型
> 因此至少包含 1 种知识点类型。

**示例 2：**
>输入：`questions = [1,5,1,3,4,5,2,5,3,3,8,6]`
>
>输出：`2`
>
>解释：有 6 位扣友在 12 道题目中选择题目，需要选择 6 题。
> 选择完成知识点类型为 3、5 的题目，因此至少包含 2 种知识点类型。



**提示：**
- `questions.length == 2*n`
- `2 <= questions.length <= 10^5`
- `1 <= questions[i] <= 1000`

---

[提交记录](https://leetcode.cn/problems/WqXACV/submissions/) | [题解](https://leetcode.cn/problems/WqXACV/solution/)


~~~

## Code Snippets

~~~tabs
tab: C++

```cpp
class Solution {
public:
    int halfQuestions(vector<int>& questions) {

    }
};
```

tab: Java

```java
class Solution {
    public int halfQuestions(int[] questions) {

    }
}
```

tab: Python

```python
class Solution(object):
    def halfQuestions(self, questions):
        """
        :type questions: List[int]
        :rtype: int
        """
```

tab: Python3

```python
class Solution:
    def halfQuestions(self, questions: List[int]) -> int:
```

tab: C

```c


int halfQuestions(int* questions, int questionsSize){

}
```

tab: C#

```csharp
public class Solution {
    public int HalfQuestions(int[] questions) {

    }
}
```

tab: JavaScript

```javascript
/**
 * @param {number[]} questions
 * @return {number}
 */
var halfQuestions = function(questions) {

};
```

tab: TypeScript

```typescript
function halfQuestions(questions: number[]): number {

};
```

tab: PHP

```php
class Solution {

    /**
     * @param Integer[] $questions
     * @return Integer
     */
    function halfQuestions($questions) {

    }
}
```

tab: Swift

```swift
class Solution {
    func halfQuestions(_ questions: [Int]) -> Int {

    }
}
```

tab: Kotlin

```kotlin
class Solution {
    fun halfQuestions(questions: IntArray): Int {

    }
}
```

tab: Dart

```dart
class Solution {
  int halfQuestions(List<int> questions) {

  }
}
```

tab: Go

```go
func halfQuestions(questions []int) int {

}
```

tab: Ruby

```ruby
# @param {Integer[]} questions
# @return {Integer}
def half_questions(questions)

end
```

tab: Scala

```scala
object Solution {
    def halfQuestions(questions: Array[Int]): Int = {

    }
}
```

tab: Rust

```rust
impl Solution {
    pub fn half_questions(questions: Vec<i32>) -> i32 {

    }
}
```

tab: Racket

```racket
(define/contract (half-questions questions)
  (-> (listof exact-integer?) exact-integer?)

  )
```

tab: Erlang

```erlang
-spec half_questions(Questions :: [integer()]) -> integer().
half_questions(Questions) ->
  .
```

tab: Elixir

```elixir
defmodule Solution do
  @spec half_questions(questions :: [integer]) :: integer
  def half_questions(questions) do

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
          
