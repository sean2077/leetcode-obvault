---
tags:
  - leetcode/problem
questionId: LCP 01
title: Guess Numbers
translatedTitle: 猜数字
titleSlug: guess-numbers
aliases:
  - Guess Numbers
  - guess-numbers
  - 猜数字
lcLinks:
  - https://leetcode.cn/problems/guess-numbers/
lcTopics:
  - '[[array]]'
lcDifficulty: Easy
lcAcRate: 84.6%
similarQuestions: []
grade: ⭐⭐⭐⭐⭐
likes: 160
dislikes: 0
favorites: []
solutions: []
notes: []
---

**Nav:** << previous: [[100392.time-taken-to-mark-all-nodes]] | next: [[LCP 02.分式化简]] >>

---

## Description

~~~tabs
tab: English

No description

---

[submissions](https://leetcode.com/problems/guess-numbers/submissions/) | [solutions](https://leetcode.com/problems/guess-numbers/solutions/)


tab: 中文

<p>小A 和 小B 在玩猜数字。小B 每次从 1, 2, 3 中随机选择一个，小A 每次也从 1, 2, 3 中选择一个猜。他们一共进行三次这个游戏，请返回 小A 猜对了几次？</p>

<p>输入的<code>guess</code>数组为 小A 每次的猜测，<code>answer</code>数组为 小B 每次的选择。<code>guess</code>和<code>answer</code>的长度都等于3。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>guess = [1,2,3], answer = [1,2,3]
<strong>输出：</strong>3
<strong>解释：</strong>小A 每次都猜对了。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>guess = [2,2,3], answer = [3,2,1]
<strong>输出：</strong>1
<strong>解释：</strong>小A 只猜对了第二次。</pre>

<p> </p>

<p><strong>限制：</strong></p>

<ol>
	<li><code>guess</code> 的长度 = 3</li>
	<li><code>answer</code> 的长度 = 3</li>
	<li><code>guess</code> 的元素取值为 <code>{1, 2, 3}</code> 之一。</li>
	<li><code>answer</code> 的元素取值为 <code>{1, 2, 3}</code> 之一。</li>
</ol>


---

[提交记录](https://leetcode.cn/problems/guess-numbers/submissions/) | [题解](https://leetcode.cn/problems/guess-numbers/solution/)


~~~

## Code Snippets

~~~tabs
tab: C++

```cpp
class Solution {
public:
    int game(vector<int>& guess, vector<int>& answer) {

    }
};
```

tab: Java

```java
class Solution {
    public int game(int[] guess, int[] answer) {

    }
}
```

tab: Python

```python
class Solution(object):
    def game(self, guess, answer):
        """
        :type guess: List[int]
        :type answer: List[int]
        :rtype: int
        """
```

tab: Python3

```python
class Solution:
    def game(self, guess: List[int], answer: List[int]) -> int:
```

tab: C

```c


int game(int* guess, int guessSize, int* answer, int answerSize){

}

```

tab: JavaScript

```javascript
/**
 * @param {number[]} guess
 * @param {number[]} answer
 * @return {number}
 */
var game = function(guess, answer) {

};
```

tab: TypeScript

```typescript
function game(guess: number[], answer: number[]): number {

};
```

tab: Dart

```dart
class Solution {
  int game(List<int> guess, List<int> answer) {

  }
}
```

tab: Go

```go
func game(guess []int, answer []int) int {

}
```

tab: Racket

```racket
(define/contract (game guess answer)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)

  )
```

tab: Erlang

```erlang
-spec game(Guess :: [integer()], Answer :: [integer()]) -> integer().
game(Guess, Answer) ->
  .
```

tab: Elixir

```elixir
defmodule Solution do
  @spec game(guess :: [integer], answer :: [integer]) :: integer
  def game(guess, answer) do

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
          
