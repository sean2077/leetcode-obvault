---
tags:
  - leetcode/problem
questionId: LCP 71
title: 集水器
translatedTitle: 集水器
titleSlug: kskhHQ
aliases:
  - 集水器
  - kskhHQ
  - 集水器
lcLinks:
  - https://leetcode.cn/problems/kskhHQ/
lcTopics:
  - '[[union-find]]'
  - '[[array]]'
  - '[[matrix]]'
lcDifficulty: Hard
lcAcRate: 57.9%
similarQuestions: []
grade: ⭐⭐⭐⭐⭐
likes: 8
dislikes: 0
favorites: []
solutions: []
notes: []
cssclasses: []
created: 2024-08-13 00:28
updated:
---

**Nav:** << previous: [[LCP 70.XxZZjK]] | next: [[LCP 72.hqCnmP]] >>

---

## Description

~~~tabs
tab: English

No description

---

[submissions](https://leetcode.com/problems/kskhHQ/submissions/) | [solutions](https://leetcode.com/problems/kskhHQ/solutions/)


tab: 中文

字符串数组 `shape` 描述了一个二维平面中的矩阵形式的集水器，`shape[i][j]` 表示集水器的第 `i` 行 `j` 列为：
- `'l'`表示向左倾斜的隔板（即从左上到右下）；
- `'r'`表示向右倾斜的隔板（即从左下到右上）；
- `'.'` 表示此位置没有隔板
![image.png](https://pic.leetcode-cn.com/1664424667-wMnPja-image.png){:width=200px}

已知当隔板构成存储容器可以存水，每个方格代表的蓄水量为 `2`。集水器初始浸泡在水中，除内部密闭空间外，所有位置均被水填满。
现将其从水中竖直向上取出，请返回集水器最终的蓄水量。

**注意：**
- 隔板具有良好的透气性，因此空气可以穿过隔板，但水无法穿过

**示例 1：**
> 输入：
> `shape = ["....rl","l.lr.r",".l..r.","..lr.."]`
>
> 输出：`18`
>
> 解释：如下图所示，由于空气会穿过隔板，因此红框区域没有水
![image.png](https://pic.leetcode-cn.com/1664436239-eyYxeP-image.png){:width="280px"}


**示例 2：**
> 输入：
> `shape = [".rlrlrlrl","ll..rl..r",".llrrllrr","..lr..lr."]`
> 输出：`18`
>
> 解释：如图所示。由于红框右侧未闭合，因此多余的水会从该处流走。
![image.png](https://pic.leetcode-cn.com/1664436082-SibVMv-image.png){:width="400px"}


**示例 3：**
> 输入：
> `shape = ["rlrr","llrl","llr."]`
> 输出：`6`
>
> 解释：如图所示。
![image.png](https://pic.leetcode-cn.com/1664424855-dwpUHO-image.png){:width="230px"}




**示例 4：**
> 输入：
> `shape = ["...rl...","..r..l..",".r.rl.l.","r.r..l.l","l.l..rl.",".l.lr.r.","..l..r..","...lr..."]`
>
> 输出：`30`
>
> 解释：如下图所示。由于中间为内部密闭空间，无法蓄水。
![image.png](https://pic.leetcode-cn.com/1664424894-mClEXh-image.png){:width="350px"}


**提示**：
- `1 <= shape.length <= 50`
- `1 <= shape[i].length <= 50`
- `shape[i][j]` 仅为 `'l'`、`'r'` 或 `'.'`


---

[提交记录](https://leetcode.cn/problems/kskhHQ/submissions/) | [题解](https://leetcode.cn/problems/kskhHQ/solution/)


~~~

## Code Snippets

~~~tabs
tab: C++

```cpp
class Solution {
public:
    int reservoir(vector<string>& shape) {

    }
};
```

tab: Java

```java
class Solution {
    public int reservoir(String[] shape) {

    }
}
```

tab: Python

```python
class Solution(object):
    def reservoir(self, shape):
        """
        :type shape: List[str]
        :rtype: int
        """
```

tab: Python3

```python
class Solution:
    def reservoir(self, shape: List[str]) -> int:
```

tab: C

```c


int reservoir(char** shape, int shapeSize){

}
```

tab: C#

```csharp
public class Solution {
    public int Reservoir(string[] shape) {

    }
}
```

tab: JavaScript

```javascript
/**
 * @param {string[]} shape
 * @return {number}
 */
var reservoir = function(shape) {

};
```

tab: TypeScript

```typescript
function reservoir(shape: string[]): number {

};
```

tab: PHP

```php
class Solution {

    /**
     * @param String[] $shape
     * @return Integer
     */
    function reservoir($shape) {

    }
}
```

tab: Swift

```swift
class Solution {
    func reservoir(_ shape: [String]) -> Int {

    }
}
```

tab: Kotlin

```kotlin
class Solution {
    fun reservoir(shape: Array<String>): Int {

    }
}
```

tab: Dart

```dart
class Solution {
  int reservoir(List<String> shape) {

  }
}
```

tab: Go

```go
func reservoir(shape []string) int {

}
```

tab: Ruby

```ruby
# @param {String[]} shape
# @return {Integer}
def reservoir(shape)

end
```

tab: Scala

```scala
object Solution {
    def reservoir(shape: Array[String]): Int = {

    }
}
```

tab: Rust

```rust
impl Solution {
    pub fn reservoir(shape: Vec<String>) -> i32 {

    }
}
```

tab: Racket

```racket
(define/contract (reservoir shape)
  (-> (listof string?) exact-integer?)

  )
```

tab: Erlang

```erlang
-spec reservoir(Shape :: [unicode:unicode_binary()]) -> integer().
reservoir(Shape) ->
  .
```

tab: Elixir

```elixir
defmodule Solution do
  @spec reservoir(shape :: [String.t]) :: integer
  def reservoir(shape) do

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
          
