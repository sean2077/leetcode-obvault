---
tags:
  - leetcode/problem
questionId: LCP 64
title: 二叉树灯饰
translatedTitle: 二叉树灯饰
titleSlug: U7WvvU
aliases:
  - 二叉树灯饰
  - U7WvvU
  - 二叉树灯饰
lcLinks:
  - https://leetcode.cn/problems/U7WvvU/
lcTopics:
  - '[[tree]]'
  - '[[depth-first-search]]'
  - '[[dynamic-programming]]'
  - '[[binary-tree]]'
lcDifficulty: Medium
lcAcRate: 37.8%
similarQuestions: []
grade: ⭐⭐⭐⭐⭐
likes: 22
dislikes: 0
favorites: []
solutions: []
notes: []
---

**Nav:** << previous: [[LCP 63.弹珠游戏]] | next: [[LCP 65.舒适的湿度]] >>

---

## Description

~~~tabs
tab: English

No description

---

[submissions](https://leetcode.com/problems/U7WvvU/submissions/) | [solutions](https://leetcode.com/problems/U7WvvU/solutions/)


tab: 中文

<p>「力扣嘉年华」的中心广场放置了一个巨型的二叉树形状的装饰树。每个节点上均有一盏灯和三个开关。节点值为&nbsp;<code>0</code> 表示灯处于「关闭」状态，节点值为 <code>1</code>&nbsp;表示灯处于「开启」状态。每个节点上的三个开关各自功能如下：</p>

<ul>
	<li>开关 <code>1</code>：切换当前节点的灯的状态；</li>
	<li>开关 <code>2</code>：切换 <strong>以当前节点为根</strong>&nbsp;的子树中，所有节点上的灯的状态；</li>
	<li>开关 <code>3</code>：切换 <strong>当前节点及其左右子节点</strong>（若存在的话） 上的灯的状态；</li>
</ul>

<p>给定该装饰的初始状态 <code>root</code>，请返回最少需要操作多少次开关，可以关闭所有节点的灯。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>root = [1,1,0,null,null,null,1]
<strong>输出：</strong>2
<strong>解释：</strong>以下是最佳的方案之一，如图所示
<img alt="" src="https://pic.leetcode-cn.com/1629357030-GSbzpY-b71b95bf405e3b223e00b2820a062ba4.gif" style="width: 300px; height: 225px;" />
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>root = [1,1,1,1,null,null,1]
<strong>输出：</strong>1
<strong>解释：</strong>以下是最佳的方案，如图所示
<img alt="" src="https://pic.leetcode-cn.com/1629356950-HZsKZC-a4091b6448a0089b4d9e8f0390ff9ac6.gif" style="width: 300px; height: 225px;" />
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>root = [0,null,0]
<strong>输出：</strong>0
<strong>解释：</strong>无需操作开关，当前所有节点上的灯均已关闭
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= 节点个数 &lt;= 10^5</code></li>
	<li><code>0 &lt;= Node.val &lt;= 1</code></li>
</ul>


---

[提交记录](https://leetcode.cn/problems/U7WvvU/submissions/) | [题解](https://leetcode.cn/problems/U7WvvU/solution/)


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
    int closeLampInTree(TreeNode* root) {

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
    public int closeLampInTree(TreeNode root) {

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
    def closeLampInTree(self, root):
        """
        :type root: TreeNode
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
    def closeLampInTree(self, root: TreeNode) -> int:
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


int closeLampInTree(struct TreeNode* root){

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
    public int CloseLampInTree(TreeNode root) {

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
 * @return {number}
 */
var closeLampInTree = function(root) {

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

function closeLampInTree(root: TreeNode | null): number {

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
     * @return Integer
     */
    function closeLampInTree($root) {

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
    func closeLampInTree(_ root: TreeNode?) -> Int {

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
    fun closeLampInTree(root: TreeNode?): Int {

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
  int closeLampInTree(TreeNode? root) {

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
func closeLampInTree(root *TreeNode) int {

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
# @return {Integer}
def close_lamp_in_tree(root)

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
    def closeLampInTree(root: TreeNode): Int = {

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
    pub fn close_lamp_in_tree(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {

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

(define/contract (close-lamp-in-tree root)
  (-> (or/c tree-node? #f) exact-integer?)

  )
```

tab: Erlang

```erlang
%% Definition for a binary tree node.
%%
%% -record(tree_node, {val = 0 :: integer(),
%%                     left = null  :: 'null' | #tree_node{},
%%                     right = null :: 'null' | #tree_node{}}).

-spec close_lamp_in_tree(Root :: #tree_node{} | null) -> integer().
close_lamp_in_tree(Root) ->
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
  @spec close_lamp_in_tree(root :: TreeNode.t | nil) :: integer
  def close_lamp_in_tree(root) do

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
          
