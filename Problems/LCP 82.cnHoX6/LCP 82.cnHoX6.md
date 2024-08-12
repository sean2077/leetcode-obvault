---
tags:
  - leetcode/problem
questionId: LCP 82
title: 万灵之树
translatedTitle: 万灵之树
titleSlug: cnHoX6
aliases:
  - 万灵之树
  - cnHoX6
  - 万灵之树
lcLink: https://leetcode.com/problems/cnHoX6/
lcTopics: []
lcDifficulty: Hard
lcAcRate: 19.6%
similarQuestions: []
grade: ⭐⭐⭐⭐⭐
likes: 13
dislikes: 0
favorites: []
solutions: []
notes: []
cssclasses: []
created: 2024-08-13 00:10
updated:
---

**Nav:** << previous: [[LCP 81.ryfUiz]] | next: [[LCR 001.xoh6Oh]] >>

---

## Description

~~~tabs
tab: English

No description

---

[submissions](https://leetcode.com/problems/cnHoX6/submissions/) | [solutions](https://leetcode.com/problems/cnHoX6/solutions/)


tab: 中文

探险家小扣终于来到了万灵之树前，挑战最后的谜题。
已知小扣拥有足够数量的链接节点和 `n` 颗幻境宝石，`gem[i]` 表示第 `i` 颗宝石的数值。现在小扣需要使用这些链接节点和宝石组合成一颗二叉树，其组装规则为：
- 链接节点将作为二叉树中的非叶子节点，且每个链接节点必须拥有 `2` 个子节点；
- 幻境宝石将作为二叉树中的叶子节点，所有的幻境宝石都必须被使用。

能量首先进入根节点，而后将按如下规则进行移动和记录：
- 若能量首次到达该节点时：
    - 记录数字 `1`；
    - 若该节点为叶节点，将额外记录该叶节点的数值；
- 若存在未到达的子节点，则选取未到达的一个子节点（优先选取左子节点）进入；
- 若无子节点或所有子节点均到达过，此时记录 `9`，并回到当前节点的父节点（若存在）。

如果最终记下的数依序连接成一个整数 `num`，满足 $num \mod~p=target$，则视为解开谜题。
请问有多少种二叉树的组装方案，可以使得最终记录下的数字可以解开谜题

**注意：**
- 两棵结构不同的二叉树，作为不同的组装方案
- 两棵结构相同的二叉树且存在某个相同位置处的宝石编号不同，也作为不同的组装方案
- 可能存在数值相同的两颗宝石

**示例 1：**
> 输入：`gem = [2,3]`
> `p = 100000007`
> `target = 11391299`
>
> 输出：`1`
>
> 解释：
> 包含 `2` 个叶节点的结构只有一种。
> 假设 B、C 节点的值分别为 3、2，对应 target 为 11391299，如下图所示。
> 11391299 % 100000007 = 11391299，满足条件;
> 假设 B、C 节点的值分别为 2、3，对应 target 为 11291399;
> 11291399 % 100000007 = 11291399，不满足条件；
> 因此只存在 1 种方案，返回 1
![万灵 (1).gif](https://pic.leetcode.cn/1682397079-evMssw-%E4%B8%87%E7%81%B5%20\(1\).gif){:height=300px}


**示例 2：**
> 输入：`gem = [3,21,3]`
> `p = 7`
> `target = 5`
>
> 输出：`4`
>
> 解释：
包含 `3` 个叶节点树结构有两种，列举如下：
满足条件的组合有四种情况：
> 当结构为下图（1）时：叶子节点的值为 [3,3,21] 或 [3,3,21]，得到的整数为 `11139139912199`。
> 当结构为下图（2）时：叶子节点的值为 [21,3,3] 或 [21,3,3]，得到的整数为 `11219113913999`。
![image.png](https://pic.leetcode.cn/1682322894-vfqJIV-image.png){:width=500px}


**提示：**
- `1 <= gem.length <= 9`
- `0 <= gem[i] <= 10^9`
- `1 <= p <= 10^9`，保证 $p$ 为素数。
- `0 <= target < p`
- 存在 2 组 `gem.length == 9` 的用例

---

[提交记录](https://leetcode.cn/problems/cnHoX6/submissions/) | [题解](https://leetcode.cn/problems/cnHoX6/solution/)


~~~

## Code Snippets

~~~tabs
tab: C++

```cpp
class Solution {
public:
    int treeOfInfiniteSouls(vector<int>& gem, int p, int target) {

    }
};
```

tab: Java

```java
class Solution {
    public int treeOfInfiniteSouls(int[] gem, int p, int target) {

    }
}
```

tab: Python

```python
class Solution(object):
    def treeOfInfiniteSouls(self, gem, p, target):
        """
        :type gem: List[int]
        :type p: int
        :type target: int
        :rtype: int
        """
```

tab: Python3

```python
class Solution:
    def treeOfInfiniteSouls(self, gem: List[int], p: int, target: int) -> int:
```

tab: C

```c
int treeOfInfiniteSouls(int* gem, int gemSize, int p, int target){

}
```

tab: C#

```csharp
public class Solution {
    public int TreeOfInfiniteSouls(int[] gem, int p, int target) {

    }
}
```

tab: JavaScript

```javascript
/**
 * @param {number[]} gem
 * @param {number} p
 * @param {number} target
 * @return {number}
 */
var treeOfInfiniteSouls = function(gem, p, target) {

};
```

tab: TypeScript

```typescript
function treeOfInfiniteSouls(gem: number[], p: number, target: number): number {

};
```

tab: PHP

```php
class Solution {

    /**
     * @param Integer[] $gem
     * @param Integer $p
     * @param Integer $target
     * @return Integer
     */
    function treeOfInfiniteSouls($gem, $p, $target) {

    }
}
```

tab: Swift

```swift
class Solution {
    func treeOfInfiniteSouls(_ gem: [Int], _ p: Int, _ target: Int) -> Int {

    }
}
```

tab: Kotlin

```kotlin
class Solution {
    fun treeOfInfiniteSouls(gem: IntArray, p: Int, target: Int): Int {

    }
}
```

tab: Dart

```dart
class Solution {
  int treeOfInfiniteSouls(List<int> gem, int p, int target) {

  }
}
```

tab: Go

```go
func treeOfInfiniteSouls(gem []int, p int, target int) int {

}
```

tab: Ruby

```ruby
# @param {Integer[]} gem
# @param {Integer} p
# @param {Integer} target
# @return {Integer}
def tree_of_infinite_souls(gem, p, target)

end
```

tab: Scala

```scala
object Solution {
    def treeOfInfiniteSouls(gem: Array[Int], p: Int, target: Int): Int = {

    }
}
```

tab: Rust

```rust
impl Solution {
    pub fn tree_of_infinite_souls(gem: Vec<i32>, p: i32, target: i32) -> i32 {

    }
}
```

tab: Racket

```racket
(define/contract (tree-of-infinite-souls gem p target)
  (-> (listof exact-integer?) exact-integer? exact-integer? exact-integer?)

  )
```

tab: Erlang

```erlang
-spec tree_of_infinite_souls(Gem :: [integer()], P :: integer(), Target :: integer()) -> integer().
tree_of_infinite_souls(Gem, P, Target) ->
  .
```

tab: Elixir

```elixir
defmodule Solution do
  @spec tree_of_infinite_souls(gem :: [integer], p :: integer, target :: integer) :: integer
  def tree_of_infinite_souls(gem, p, target) do

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
          
