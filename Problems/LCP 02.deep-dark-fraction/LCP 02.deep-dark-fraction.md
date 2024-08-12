---
tags:
  - leetcode/problem
questionId: LCP 02
title: Deep Dark Fraction
translatedTitle: 分式化简
titleSlug: deep-dark-fraction
aliases:
  - Deep Dark Fraction
  - deep-dark-fraction
  - 分式化简
lcLink: https://leetcode.com/problems/deep-dark-fraction/
lcTopics:
  - '[[array]]'
  - '[[math]]'
  - '[[number-theory]]'
  - '[[simulation]]'
lcDifficulty: Easy
lcAcRate: 70.3%
similarQuestions: []
grade: ⭐⭐⭐⭐⭐
likes: 134
dislikes: 0
favorites: []
solutions: []
notes: []
cssclasses: []
created: 2024-08-13 00:10
updated:
---

**Nav:** << previous: [[LCP 01.guess-numbers]] | next: [[LCP 03.programmable-robot]] >>

---

## Description

~~~tabs
tab: English

No description

---

[submissions](https://leetcode.com/problems/deep-dark-fraction/submissions/) | [solutions](https://leetcode.com/problems/deep-dark-fraction/solutions/)


tab: 中文

<p>有一个同学在学习分式。他需要将一个连分数化成最简分数，你能帮助他吗？</p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/09/09/fraction_example_1.jpg" style="height: 195px; width: 480px;" /></p>

<p>连分数是形如上图的分式。在本题中，所有系数都是大于等于0的整数。</p>

<p> </p>

<p>输入的<code>cont</code>代表连分数的系数（<code>cont[0]</code>代表上图的<code>a<sub>0</sub></code>，以此类推）。返回一个长度为2的数组<code>[n, m]</code>，使得连分数的值等于<code>n / m</code>，且<code>n, m</code>最大公约数为1。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>cont = [3, 2, 0, 2]
<strong>输出：</strong>[13, 4]
<strong>解释：</strong>原连分数等价于3 + (1 / (2 + (1 / (0 + 1 / 2))))。注意[26, 8], [-13, -4]都不是正确答案。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>cont = [0, 0, 3]
<strong>输出：</strong>[3, 1]
<strong>解释：</strong>如果答案是整数，令分母为1即可。</pre>

<p> </p>

<p><strong>限制：</strong></p>

<ol>
	<li><code>cont[i] >= 0</code></li>
	<li><code>1 <= cont的长度 <= 10</code></li>
	<li><code>cont</code>最后一个元素不等于0</li>
	<li>答案的<code>n, m</code>的取值都能被32位int整型存下（即不超过<code>2 ^ 31 - 1</code>）。</li>
</ol>


---

[提交记录](https://leetcode.cn/problems/deep-dark-fraction/submissions/) | [题解](https://leetcode.cn/problems/deep-dark-fraction/solution/)


~~~

## Code Snippets

~~~tabs
tab: C++

```cpp
class Solution {
public:
    vector<int> fraction(vector<int>& cont) {

    }
};
```

tab: Java

```java
class Solution {
    public int[] fraction(int[] cont) {

    }
}
```

tab: Python

```python
class Solution(object):
    def fraction(self, cont):
        """
        :type cont: List[int]
        :rtype: List[int]
        """
```

tab: Python3

```python
class Solution:
    def fraction(self, cont: List[int]) -> List[int]:
```

tab: C

```c


/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* fraction(int* cont, int contSize, int* returnSize){

}

```

tab: JavaScript

```javascript
/**
 * @param {number[]} cont
 * @return {number[]}
 */
var fraction = function(cont) {

};
```

tab: TypeScript

```typescript
function fraction(cont: number[]): number[] {

};
```

tab: Dart

```dart
class Solution {
  List<int> fraction(List<int> cont) {

  }
}
```

tab: Go

```go
func fraction(cont []int) []int {

}
```

tab: Racket

```racket
(define/contract (fraction cont)
  (-> (listof exact-integer?) (listof exact-integer?))

  )
```

tab: Erlang

```erlang
-spec fraction(Cont :: [integer()]) -> [integer()].
fraction(Cont) ->
  .
```

tab: Elixir

```elixir
defmodule Solution do
  @spec fraction(cont :: [integer]) :: [integer]
  def fraction(cont) do

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
          
