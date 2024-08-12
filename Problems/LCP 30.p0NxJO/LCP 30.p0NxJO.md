---
tags:
  - leetcode/problem
questionId: LCP 30
title: 魔塔游戏
translatedTitle: 魔塔游戏
titleSlug: p0NxJO
aliases:
  - 魔塔游戏
  - p0NxJO
  - 魔塔游戏
lcLink: https://leetcode.com/problems/p0NxJO/
lcTopics:
  - '[[greedy]]'
  - '[[array]]'
  - '[[heap-priority-queue]]'
lcDifficulty: Medium
lcAcRate: 46.0%
similarQuestions: []
grade: ⭐⭐⭐⭐⭐
likes: 118
dislikes: 0
favorites: []
solutions: []
notes: []
cssclasses: []
created: 2024-08-13 00:10
updated:
---

**Nav:** << previous: [[LCP 29.SNJvJP]] | next: [[LCP 31.Db3wC1]] >>

---

## Description

~~~tabs
tab: English

No description

---

[submissions](https://leetcode.com/problems/p0NxJO/submissions/) | [solutions](https://leetcode.com/problems/p0NxJO/solutions/)


tab: 中文

小扣当前位于魔塔游戏第一层，共有 `N` 个房间，编号为 `0 ~ N-1`。每个房间的补血道具/怪物对于血量影响记于数组 `nums`，其中正数表示道具补血数值，即血量增加对应数值；负数表示怪物造成伤害值，即血量减少对应数值；`0` 表示房间对血量无影响。

**小扣初始血量为 1，且无上限**。假定小扣原计划按房间编号升序访问所有房间补血/打怪，**为保证血量始终为正值**，小扣需对房间访问顺序进行调整，**每次仅能将一个怪物房间（负数的房间）调整至访问顺序末尾**。请返回小扣最少需要调整几次，才能顺利访问所有房间。若调整顺序也无法访问完全部房间，请返回 -1。


**示例 1：**
>输入：`nums = [100,100,100,-250,-60,-140,-50,-50,100,150]`
>
>输出：`1`
>
>解释：初始血量为 1。至少需要将 nums[3] 调整至访问顺序末尾以满足要求。

**示例 2：**
>输入：`nums = [-200,-300,400,0]`
>
>输出：`-1`
>
>解释：调整访问顺序也无法完成全部房间的访问。

**提示：**
- `1 <= nums.length <= 10^5`
- `-10^5 <= nums[i] <= 10^5`

---

[提交记录](https://leetcode.cn/problems/p0NxJO/submissions/) | [题解](https://leetcode.cn/problems/p0NxJO/solution/)


~~~

## Code Snippets

~~~tabs
tab: C++

```cpp
class Solution {
public:
    int magicTower(vector<int>& nums) {

    }
};
```

tab: Java

```java
class Solution {
    public int magicTower(int[] nums) {

    }
}
```

tab: Python

```python
class Solution(object):
    def magicTower(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
```

tab: Python3

```python
class Solution:
    def magicTower(self, nums: List[int]) -> int:
```

tab: C

```c


int magicTower(int* nums, int numsSize){

}
```

tab: C#

```csharp
public class Solution {
    public int MagicTower(int[] nums) {

    }
}
```

tab: JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var magicTower = function(nums) {

};
```

tab: TypeScript

```typescript
function magicTower(nums: number[]): number {

};
```

tab: PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function magicTower($nums) {

    }
}
```

tab: Swift

```swift
class Solution {
    func magicTower(_ nums: [Int]) -> Int {

    }
}
```

tab: Kotlin

```kotlin
class Solution {
    fun magicTower(nums: IntArray): Int {

    }
}
```

tab: Go

```go
func magicTower(nums []int) int {

}
```

tab: Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def magic_tower(nums)

end
```

tab: Scala

```scala
object Solution {
    def magicTower(nums: Array[Int]): Int = {

    }
}
```

tab: Rust

```rust
impl Solution {
    pub fn magic_tower(nums: Vec<i32>) -> i32 {

    }
}
```

tab: Racket

```racket
(define/contract (magic-tower nums)
  (-> (listof exact-integer?) exact-integer?)

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
          
