---
tags:
  - leetcode/problem
questionId: LCP 33
title: 蓄水
translatedTitle: 蓄水
titleSlug: o8SXZn
aliases:
  - 蓄水
  - o8SXZn
  - 蓄水
lcLinks:
  - https://leetcode.cn/problems/o8SXZn/
lcTopics:
  - '[[greedy]]'
  - '[[array]]'
  - '[[heap-priority-queue]]'
lcDifficulty: Easy
lcAcRate: 34.9%
similarQuestions: []
grade: ⭐⭐⭐⭐⭐
likes: 216
dislikes: 0
favorites: []
solutions: []
notes: []
---

**Nav:** << previous: [[LCP 32.批量处理任务]] | next: [[LCP 34.二叉树染色]] >>

---

## Description

~~~tabs
tab: English

No description

---

[submissions](https://leetcode.com/problems/o8SXZn/submissions/) | [solutions](https://leetcode.com/problems/o8SXZn/solutions/)


tab: 中文

给定 N 个无限容量且初始均空的水缸，每个水缸配有一个水桶用来打水，第 `i` 个水缸配备的水桶容量记作 `bucket[i]`。小扣有以下两种操作：
-  升级水桶：选择任意一个水桶，使其容量增加为 `bucket[i]+1`
-  蓄水：将全部水桶接满水，倒入各自对应的水缸

每个水缸对应最低蓄水量记作 `vat[i]`，返回小扣至少需要多少次操作可以完成所有水缸蓄水要求。

注意：实际蓄水量 **达到或超过** 最低蓄水量，即完成蓄水要求。

**示例 1：**
>输入：`bucket = [1,3], vat = [6,8]`
>
>输出：`4`
>
>解释：
>第 1 次操作升级 bucket[0]；
>第 2 ~ 4 次操作均选择蓄水，即可完成蓄水要求。
![vat1.gif](https://pic.leetcode-cn.com/1616122992-RkDxoL-vat1.gif)



**示例 2：**
>输入：`bucket = [9,0,1], vat = [0,2,2]`
>
>输出：`3`
>
>解释：
>第 1 次操作均选择升级 bucket[1]
>第 2~3 次操作选择蓄水，即可完成蓄水要求。

**提示：**
- `1 <= bucket.length == vat.length <= 100`
- `0 <= bucket[i], vat[i] <= 10^4`


---

[提交记录](https://leetcode.cn/problems/o8SXZn/submissions/) | [题解](https://leetcode.cn/problems/o8SXZn/solution/)


~~~

## Code Snippets

~~~tabs
tab: C++

```cpp
class Solution {
public:
    int storeWater(vector<int>& bucket, vector<int>& vat) {

    }
};
```

tab: Java

```java
class Solution {
    public int storeWater(int[] bucket, int[] vat) {

    }
}
```

tab: Python

```python
class Solution(object):
    def storeWater(self, bucket, vat):
        """
        :type bucket: List[int]
        :type vat: List[int]
        :rtype: int
        """
```

tab: Python3

```python
class Solution:
    def storeWater(self, bucket: List[int], vat: List[int]) -> int:
```

tab: C

```c


int storeWater(int* bucket, int bucketSize, int* vat, int vatSize){

}
```

tab: C#

```csharp
public class Solution {
    public int StoreWater(int[] bucket, int[] vat) {

    }
}
```

tab: JavaScript

```javascript
/**
 * @param {number[]} bucket
 * @param {number[]} vat
 * @return {number}
 */
var storeWater = function(bucket, vat) {

};
```

tab: TypeScript

```typescript
function storeWater(bucket: number[], vat: number[]): number {

};
```

tab: PHP

```php
class Solution {

    /**
     * @param Integer[] $bucket
     * @param Integer[] $vat
     * @return Integer
     */
    function storeWater($bucket, $vat) {

    }
}
```

tab: Swift

```swift
class Solution {
    func storeWater(_ bucket: [Int], _ vat: [Int]) -> Int {

    }
}
```

tab: Kotlin

```kotlin
class Solution {
    fun storeWater(bucket: IntArray, vat: IntArray): Int {

    }
}
```

tab: Go

```go
func storeWater(bucket []int, vat []int) int {

}
```

tab: Ruby

```ruby
# @param {Integer[]} bucket
# @param {Integer[]} vat
# @return {Integer}
def store_water(bucket, vat)

end
```

tab: Scala

```scala
object Solution {
    def storeWater(bucket: Array[Int], vat: Array[Int]): Int = {

    }
}
```

tab: Rust

```rust
impl Solution {
    pub fn store_water(bucket: Vec<i32>, vat: Vec<i32>) -> i32 {

    }
}
```

tab: Racket

```racket
(define/contract (store-water bucket vat)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)

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
          
