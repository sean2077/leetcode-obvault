---
tags:
  - leetcode/problem
questionId: LCP 63
title: 弹珠游戏
translatedTitle: 弹珠游戏
titleSlug: EXvqDp
aliases:
  - 弹珠游戏
  - EXvqDp
  - 弹珠游戏
lcLinks:
  - https://leetcode.cn/problems/EXvqDp/
lcTopics:
  - '[[depth-first-search]]'
  - '[[breadth-first-search]]'
  - '[[graph]]'
  - '[[topological-sort]]'
  - '[[memoization]]'
  - '[[array]]'
  - '[[dynamic-programming]]'
  - '[[matrix]]'
lcDifficulty: Medium
lcAcRate: 27.7%
similarQuestions: []
grade: ⭐⭐⭐⭐⭐
likes: 17
dislikes: 0
favorites: []
solutions: []
notes: []
---

**Nav:** << previous: [[LCP 62.交通枢纽]] | next: [[LCP 64.二叉树灯饰]] >>

---

## Description

~~~tabs
tab: English

No description

---

[submissions](https://leetcode.com/problems/EXvqDp/submissions/) | [solutions](https://leetcode.com/problems/EXvqDp/solutions/)


tab: 中文

欢迎各位来到「力扣嘉年华」，接下来将为各位介绍在活动中广受好评的弹珠游戏。

`N*M` 大小的弹珠盘的初始状态信息记录于一维字符串型数组 `plate` 中，数组中的每个元素为仅由 `"O"`、`"W"`、`"E"`、`"."` 组成的字符串。其中：
- `"O"` 表示弹珠洞（弹珠到达后会落入洞中，并停止前进）；
- `"W"` 表示逆时针转向器（弹珠经过时方向将逆时针旋转 90 度）；
- `"E"` 表示顺时针转向器（弹珠经过时方向将顺时针旋转 90 度）；
- `"."` 表示空白区域（弹珠可通行）。

游戏规则要求仅能在边缘位置的 **空白区域** 处（弹珠盘的四角除外）沿 **与边缘垂直** 的方向打入弹珠，并且打入后的每颗弹珠最多能 **前进** `num` 步。请返回符合上述要求且可以使弹珠最终入洞的所有打入位置。你可以 **按任意顺序** 返回答案。

**注意：**
- 若弹珠已到达弹珠盘边缘并且仍沿着出界方向继续前进，则将直接出界。

**示例 1：**
> 输入：
>`num = 4`
>`plate = ["..E.",".EOW","..W."]`
> 
> 输出：`[[2,1]]`
> 
> 解释：
> 在 `[2,1]` 处打入弹珠，弹珠前进 1 步后遇到转向器，前进方向顺时针旋转 90 度，再前进 1 步进入洞中。
![b054955158a99167b8d51da0e22a54da.gif](https://pic.leetcode-cn.com/1630392649-BoQncz-b054955158a99167b8d51da0e22a54da.gif){:width="300px"}

**示例 2：**
> 输入：
>`num = 5`
>`plate = [".....","..E..",".WO..","....."]`
> 
> 输出：`[[0,1],[1,0],[2,4],[3,2]]`
> 
> 解释：
> 在 `[0,1]` 处打入弹珠，弹珠前进 2 步，遇到转向器后前进方向逆时针旋转 90 度，再前进 1 步进入洞中。
> 在 `[1,0]` 处打入弹珠，弹珠前进 2 步，遇到转向器后前进方向顺时针旋转 90 度，再前进 1 步进入洞中。
> 在 `[2,4]` 处打入弹珠，弹珠前进 2 步后进入洞中。
> 在 `[3,2]` 处打入弹珠，弹珠前进 1 步后进入洞中。
![b44e9963239ae368badf3d00b7563087.gif](https://pic.leetcode-cn.com/1630392625-rckbdy-b44e9963239ae368badf3d00b7563087.gif){:width="350px"}


**示例 3：**
> 输入：
>`num = 3`
>`plate = [".....","....O","....O","....."]`
> 
> 输出：`[]`
> 
> 解释：
> 由于弹珠被击中后只能前进 3 步，且不能在弹珠洞和弹珠盘四角打入弹珠，故不存在能让弹珠入洞的打入位置。


**提示：**
- `1 <= num <= 10^6`
- `1 <= plate.length, plate[i].length <= 1000`
- `plate[i][j]` 仅包含 `"O"`、`"W"`、`"E"`、`"."` 

---

[提交记录](https://leetcode.cn/problems/EXvqDp/submissions/) | [题解](https://leetcode.cn/problems/EXvqDp/solution/)


~~~

## Code Snippets

~~~tabs
tab: C++

```cpp
class Solution {
public:
    vector<vector<int>> ballGame(int num, vector<string>& plate) {

    }
};
```

tab: Java

```java
class Solution {
    public int[][] ballGame(int num, String[] plate) {

    }
}
```

tab: Python

```python
class Solution(object):
    def ballGame(self, num, plate):
        """
        :type num: int
        :type plate: List[str]
        :rtype: List[List[int]]
        """
```

tab: Python3

```python
class Solution:
    def ballGame(self, num: int, plate: List[str]) -> List[List[int]]:
```

tab: C

```c


/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** ballGame(int num, char** plate, int plateSize, int* returnSize, int** returnColumnSizes){

}
```

tab: C#

```csharp
public class Solution {
    public int[][] BallGame(int num, string[] plate) {

    }
}
```

tab: JavaScript

```javascript
/**
 * @param {number} num
 * @param {string[]} plate
 * @return {number[][]}
 */
var ballGame = function(num, plate) {

};
```

tab: TypeScript

```typescript
function ballGame(num: number, plate: string[]): number[][] {

};
```

tab: PHP

```php
class Solution {

    /**
     * @param Integer $num
     * @param String[] $plate
     * @return Integer[][]
     */
    function ballGame($num, $plate) {

    }
}
```

tab: Swift

```swift
class Solution {
    func ballGame(_ num: Int, _ plate: [String]) -> [[Int]] {

    }
}
```

tab: Kotlin

```kotlin
class Solution {
    fun ballGame(num: Int, plate: Array<String>): Array<IntArray> {

    }
}
```

tab: Dart

```dart
class Solution {
  List<List<int>> ballGame(int num, List<String> plate) {

  }
}
```

tab: Go

```go
func ballGame(num int, plate []string) [][]int {

}
```

tab: Ruby

```ruby
# @param {Integer} num
# @param {String[]} plate
# @return {Integer[][]}
def ball_game(num, plate)

end
```

tab: Scala

```scala
object Solution {
    def ballGame(num: Int, plate: Array[String]): Array[Array[Int]] = {

    }
}
```

tab: Rust

```rust
impl Solution {
    pub fn ball_game(num: i32, plate: Vec<String>) -> Vec<Vec<i32>> {

    }
}
```

tab: Racket

```racket
(define/contract (ball-game num plate)
  (-> exact-integer? (listof string?) (listof (listof exact-integer?)))

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
          
