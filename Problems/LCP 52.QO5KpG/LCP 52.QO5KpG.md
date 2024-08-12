---
tags:
  - leetcode/problem
questionId: LCP 52
title: 二叉搜索树染色
translatedTitle: 二叉搜索树染色
titleSlug: QO5KpG
aliases:
  - 二叉搜索树染色
  - QO5KpG
  - 二叉搜索树染色
lcLinks:
  - https://leetcode.cn/problems/QO5KpG/
lcTopics:
  - '[[tree]]'
  - '[[segment-tree]]'
  - '[[binary-search-tree]]'
  - '[[array]]'
  - '[[binary-search]]'
  - '[[binary-tree]]'
  - '[[ordered-set]]'
lcDifficulty: Medium
lcAcRate: 29.9%
similarQuestions: []
grade: ⭐⭐⭐⭐⭐
likes: 32
dislikes: 0
favorites: []
solutions: []
notes: []
cssclasses: []
created: 2024-08-13 00:28
updated:
---

**Nav:** << previous: [[LCP 51.UEcfPD]] | next: [[LCP 53.EJvmW4]] >>

---

## Description

~~~tabs
tab: English

No description

---

[submissions](https://leetcode.com/problems/QO5KpG/submissions/) | [solutions](https://leetcode.com/problems/QO5KpG/solutions/)


tab: 中文

欢迎各位勇者来到力扣城，本次试炼主题为「二叉搜索树染色」。

每位勇士面前设有一个**二叉搜索树**的模型，模型的根节点为 `root`，树上的各个节点值均不重复。初始时，所有节点均为蓝色。现在按顺序对这棵二叉树进行若干次操作， `ops[i] = [type, x, y]` 表示第 `i` 次操作为：
+ `type` 等于 0 时，将节点值范围在 `[x, y]` 的节点均染蓝
+ `type` 等于 1 时，将节点值范围在 `[x, y]` 的节点均染红

请返回完成所有染色后，该二叉树中红色节点的数量。


**注意：**
+ 题目保证对于每个操作的 `x`、`y` 值定出现在二叉搜索树节点中

**示例 1：**
>输入：`root = [1,null,2,null,3,null,4,null,5], ops = [[1,2,4],[1,1,3],[0,3,5]]`
>
>输出：`2`
>
>解释：
>第 0 次操作，将值为 2、3、4 的节点染红；
>第 1 次操作，将值为 1、2、3 的节点染红；
>第 2 次操作，将值为 3、4、5 的节点染蓝；
>因此，最终值为 1、2 的节点为红色节点，返回数量 2
![image.png](https://pic.leetcode-cn.com/1649833948-arSlXd-image.png){:width=230px}


**示例 2：**
>输入：`root = [4,2,7,1,null,5,null,null,null,null,6]` 
>`ops = [[0,2,2],[1,1,5],[0,4,5],[1,5,7]]`
>
>输出：`5`
>
>解释：
>第 0 次操作，将值为 2 的节点染蓝；
>第 1 次操作，将值为 1、2、4、5 的节点染红；
>第 2 次操作，将值为 4、5 的节点染蓝；
>第 3 次操作，将值为 5、6、7 的节点染红；
>因此，最终值为 1、2、5、6、7 的节点为红色节点，返回数量 5
![image.png](https://pic.leetcode-cn.com/1649833763-BljEbP-image.png){:width=230px}

**提示：**
+ `1 <= 二叉树节点数量 <= 10^5`
+ `1 <= ops.length <= 10^5`
+ `ops[i].length == 3`
+ `ops[i][0]` 仅为 `0` or `1`
+ `0 <= ops[i][1] <= ops[i][2] <= 10^9`
+ `0 <= 节点值 <= 10^9`


---

[提交记录](https://leetcode.cn/problems/QO5KpG/submissions/) | [题解](https://leetcode.cn/problems/QO5KpG/solution/)


~~~

## Code Snippets

~~~tabs
tab: C++

```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int getNumber(TreeNode* root, vector<vector<int>>& ops) {

    }
};
```

tab: Java

```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public int getNumber(TreeNode root, int[][] ops) {

    }
}
```

tab: Python

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def getNumber(self, root, ops):
        """
        :type root: Optional[TreeNode]
        :type ops: List[List[int]]
        :rtype: int
        """
```

tab: Python3

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def getNumber(self, root: Optional[TreeNode], ops: List[List[int]]) -> int:
```

tab: C

```c
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */


int getNumber(struct TreeNode* root, int** ops, int opsSize, int* opsColSize){

}
```

tab: C#

```csharp
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public int GetNumber(TreeNode root, int[][] ops) {

    }
}
```

tab: JavaScript

```javascript
/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number[][]} ops
 * @return {number}
 */
var getNumber = function(root, ops) {

};
```

tab: TypeScript

```typescript
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function getNumber(root: TreeNode | null, ops: number[][]): number {

};
```

tab: PHP

```php
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     public $val = null;
 *     public $left = null;
 *     public $right = null;
 *     function __construct($value) { $this->val = $value; }
 * }
 */
class Solution {

    /**
     * @param TreeNode $root
     * @param Integer[][] $ops
     * @return Integer
     */
    function getNumber($root, $ops) {

    }
}
```

tab: Swift

```swift
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public var val: Int
 *     public var left: TreeNode?
 *     public var right: TreeNode?
 *     public init(_ val: Int) {
 *         self.val = val
 *         self.left = nil
 *         self.right = nil
 *     }
 * }
 */
class Solution {
    func getNumber(_ root: TreeNode?, _ ops: [[Int]]) -> Int {

    }
}
```

tab: Kotlin

```kotlin
/**
 * Example:
 * var ti = TreeNode(5)
 * var v = ti.`val`
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */
class Solution {
    fun getNumber(root: TreeNode?, ops: Array<IntArray>): Int {

    }
}
```

tab: Dart

```dart
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *   int val;
 *   TreeNode? left;
 *   TreeNode? right;
 *   TreeNode([this.val = 0, this.left, this.right]);
 * }
 */
class Solution {
  int getNumber(TreeNode? root, List<List<int>> ops) {

  }
}
```

tab: Go

```go
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func getNumber(root *TreeNode, ops [][]int) int {

}
```

tab: Ruby

```ruby
# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end
# @param {TreeNode} root
# @param {Integer[][]} ops
# @return {Integer}
def get_number(root, ops)

end
```

tab: Scala

```scala
/**
 * Definition for a binary tree node.
 * class TreeNode(var _value: Int) {
 *   var value: Int = _value
 *   var left: TreeNode = null
 *   var right: TreeNode = null
 * }
 */
object Solution {
    def getNumber(root: TreeNode, ops: Array[Array[Int]]): Int = {

    }
}
```

tab: Rust

```rust
// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
//
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }
use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn get_number(root: Option<Rc<RefCell<TreeNode>>>, ops: Vec<Vec<i32>>) -> i32 {

    }
}
```

tab: Racket

```racket
; Definition for a binary tree node.
#|

; val : integer?
; left : (or/c tree-node? #f)
; right : (or/c tree-node? #f)
(struct tree-node
  (val left right) #:mutable #:transparent)

; constructor
(define (make-tree-node [val 0])
  (tree-node val #f #f))

|#

(define/contract (get-number root ops)
  (-> (or/c tree-node? #f) (listof (listof exact-integer?)) exact-integer?)

  )
```

tab: Erlang

```erlang
%% Definition for a binary tree node.
%%
%% -record(tree_node, {val = 0 :: integer(),
%%                     left = null  :: 'null' | #tree_node{},
%%                     right = null :: 'null' | #tree_node{}}).

-spec get_number(Root :: #tree_node{} | null, Ops :: [[integer()]]) -> integer().
get_number(Root, Ops) ->
  .
```

tab: Elixir

```elixir
# Definition for a binary tree node.
#
# defmodule TreeNode do
#   @type t :: %__MODULE__{
#           val: integer,
#           left: TreeNode.t() | nil,
#           right: TreeNode.t() | nil
#         }
#   defstruct val: 0, left: nil, right: nil
# end

defmodule Solution do
  @spec get_number(root :: TreeNode.t | nil, ops :: [[integer]]) :: integer
  def get_number(root, ops) do

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
          
