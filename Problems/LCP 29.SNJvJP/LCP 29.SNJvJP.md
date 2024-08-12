---
tags:
  - leetcode/problem
questionId: LCP 29
title: 乐团站位
translatedTitle: 乐团站位
titleSlug: SNJvJP
aliases:
  - 乐团站位
  - SNJvJP
  - 乐团站位
lcLink: https://leetcode.com/problems/SNJvJP/
lcTopics:
  - '[[math]]'
lcDifficulty: Medium
lcAcRate: 21.4%
similarQuestions: []
grade: ⭐⭐⭐⭐⭐
likes: 73
dislikes: 0
favorites: []
solutions: []
notes: []
cssclasses: []
created: 2024-08-13 00:10
updated:
---

**Nav:** << previous: [[LCP 28.4xy4Wx]] | next: [[LCP 30.p0NxJO]] >>

---

## Description

~~~tabs
tab: English

No description

---

[submissions](https://leetcode.com/problems/SNJvJP/submissions/) | [solutions](https://leetcode.com/problems/SNJvJP/solutions/)


tab: 中文

某乐团的演出场地可视作 `num * num` 的二维矩阵 `grid`（左上角坐标为 `[0,0]`)，每个位置站有一位成员。乐团共有 `9` 种乐器，乐器编号为 `1~9`，每位成员持有 `1` 个乐器。

为保证声乐混合效果，成员站位规则为：自 `grid` 左上角开始顺时针螺旋形向内循环以 `1，2，...，9` 循环重复排列。例如当 num = `5` 时，站位如图所示

![image.png](https://pic.leetcode-cn.com/1616125411-WOblWH-image.png)


请返回位于场地坐标 [`Xpos`,`Ypos`] 的成员所持乐器编号。

**示例 1：**
>输入：`num = 3, Xpos = 0, Ypos = 2`
>
>输出：`3`
>
>解释：
![image.png](https://pic.leetcode-cn.com/1616125437-WUOwsu-image.png)


**示例 2：**
>输入：`num = 4, Xpos = 1, Ypos = 2`
>
>输出：`5`
>
>解释：
![image.png](https://pic.leetcode-cn.com/1616125453-IIDpxg-image.png)


**提示：**
- `1 <= num <= 10^9`
- `0 <= Xpos, Ypos < num`

---

[提交记录](https://leetcode.cn/problems/SNJvJP/submissions/) | [题解](https://leetcode.cn/problems/SNJvJP/solution/)


~~~

## Code Snippets

~~~tabs
tab: C++

```cpp
class Solution {
public:
    int orchestraLayout(int num, int xPos, int yPos) {

    }
};
```

tab: Java

```java
class Solution {
    public int orchestraLayout(int num, int xPos, int yPos) {

    }
}
```

tab: Python

```python
class Solution(object):
    def orchestraLayout(self, num, xPos, yPos):
        """
        :type num: int
        :type xPos: int
        :type yPos: int
        :rtype: int
        """
```

tab: Python3

```python
class Solution:
    def orchestraLayout(self, num: int, xPos: int, yPos: int) -> int:
```

tab: C

```c


int orchestraLayout(int num, int xPos, int yPos){

}
```

tab: C#

```csharp
public class Solution {
    public int OrchestraLayout(int num, int xPos, int yPos) {

    }
}
```

tab: JavaScript

```javascript
/**
 * @param {number} num
 * @param {number} xPos
 * @param {number} yPos
 * @return {number}
 */
var orchestraLayout = function(num, xPos, yPos) {

};
```

tab: TypeScript

```typescript
function orchestraLayout(num: number, xPos: number, yPos: number): number {

};
```

tab: PHP

```php
class Solution {

    /**
     * @param Integer $num
     * @param Integer $xPos
     * @param Integer $yPos
     * @return Integer
     */
    function orchestraLayout($num, $xPos, $yPos) {

    }
}
```

tab: Swift

```swift
class Solution {
    func orchestraLayout(_ num: Int, _ xPos: Int, _ yPos: Int) -> Int {

    }
}
```

tab: Kotlin

```kotlin
class Solution {
    fun orchestraLayout(num: Int, xPos: Int, yPos: Int): Int {

    }
}
```

tab: Dart

```dart
class Solution {
  int orchestraLayout(int num, int xPos, int yPos) {

  }
}
```

tab: Go

```go
func orchestraLayout(num int, xPos int, yPos int) int {

}
```

tab: Ruby

```ruby
# @param {Integer} num
# @param {Integer} x_pos
# @param {Integer} y_pos
# @return {Integer}
def orchestra_layout(num, x_pos, y_pos)

end
```

tab: Scala

```scala
object Solution {
    def orchestraLayout(num: Int, xPos: Int, yPos: Int): Int = {

    }
}
```

tab: Rust

```rust
impl Solution {
    pub fn orchestra_layout(num: i32, x_pos: i32, y_pos: i32) -> i32 {

    }
}
```

tab: Racket

```racket
(define/contract (orchestra-layout num xPos yPos)
  (-> exact-integer? exact-integer? exact-integer? exact-integer?)

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
          
