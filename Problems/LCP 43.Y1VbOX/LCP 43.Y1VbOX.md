---
tags:
  - leetcode/problem
questionId: LCP 43
title: 十字路口的交通
translatedTitle: 十字路口的交通
titleSlug: Y1VbOX
aliases:
  - 十字路口的交通
  - Y1VbOX
  - 十字路口的交通
lcLinks:
  - https://leetcode.cn/problems/Y1VbOX/
lcTopics:
  - '[[array]]'
  - '[[string]]'
  - '[[dynamic-programming]]'
lcDifficulty: Hard
lcAcRate: 52.2%
similarQuestions: []
grade: ⭐⭐⭐⭐⭐
likes: 18
dislikes: 0
favorites: []
solutions: []
notes: []
cssclasses: []
created: 2024-08-13 00:28
updated:
---

**Nav:** << previous: [[LCP 42.vFjcfV]] | next: [[LCP 44.sZ59z6]] >>

---

## Description

~~~tabs
tab: English

No description

---

[submissions](https://leetcode.com/problems/Y1VbOX/submissions/) | [solutions](https://leetcode.com/problems/Y1VbOX/solutions/)


tab: 中文

前往「力扣挑战赛」场馆的道路上，有一个拥堵的十字路口，该十字路口由两条双向两车道的路交叉构成。由于信号灯故障，交警需要手动指挥拥堵车辆。假定路口没有新的来车且一辆车从一个车道驶入另一个车道所需的时间恰好为一秒钟，长度为 4 的一维字符串数组 `directions` 中按照 **东、南、西、北** 顺序记录了四个方向从最靠近路口到最远离路口的车辆计划开往的方向。其中：
- `"E"` 表示向东行驶；
- `"S"` 表示向南行驶；
- `"W"` 表示向西行驶；
- `"N"` 表示向北行驶。

交警每秒钟只能指挥各个车道距离路口最近的一辆车，且每次指挥需要满足如下规则：
- 同一秒钟内，一个方向的车道只允许驶出一辆车；
- 同一秒钟内，一个方向的车道只允许驶入一辆车；
- 同一秒钟内，车辆的行驶路线不可相交。

请返回最少需要几秒钟，该十字路口等候的车辆才能全部走完。

各个车道驶出的车辆可能的行驶路线如图所示：


![图片.png](https://pic.leetcode-cn.com/1630393755-gyPeMM-%E5%9B%BE%E7%89%87.png){:height="350px"}

**注意：**
- 测试数据保证不会出现掉头行驶指令，即某一方向的行驶车辆计划开往的方向不会是当前车辆所在的车道的方向;
- 表示堵塞车辆行驶方向的字符串仅用大写字母 `"E"`，`"N"`，`"W"`，`"S"` 表示。

**示例 1：**
>输入：`directions = ["W","N","ES","W"]`
>
>输出：`2`
>
>解释：
>第 1 秒：东西方向排在最前的车先行，剩余车辆状态 `["","N","S","W"]`；
>第 2 秒：南、西、北方向的车行驶，路口无等待车辆；
>因此最少需要 2 秒，返回 2。

**示例 2：**
>输入：`directions = ["NS","WE","SE","EW"]`
>
>输出：`3`
>
>解释：
>第 1 秒：四个方向排在最前的车均可驶出；
>第 2 秒：东南方向的车驶出，剩余车辆状态 `["","","E","W"]`；
>第 3 秒：西北方向的车驶出。


**提示：**
- `directions.length = 4`
- `0 <= directions[i].length <= 20`


---

[提交记录](https://leetcode.cn/problems/Y1VbOX/submissions/) | [题解](https://leetcode.cn/problems/Y1VbOX/solution/)


~~~

## Code Snippets

~~~tabs
tab: C++

```cpp
class Solution {
public:
    int trafficCommand(vector<string>& directions) {

    }
};
```

tab: Java

```java
class Solution {
    public int trafficCommand(String[] directions) {

    }
}
```

tab: Python

```python
class Solution(object):
    def trafficCommand(self, directions):
        """
        :type directions: List[str]
        :rtype: int
        """
```

tab: Python3

```python
class Solution:
    def trafficCommand(self, directions: List[str]) -> int:
```

tab: C

```c


int trafficCommand(char** directions, int directionsSize){

}
```

tab: C#

```csharp
public class Solution {
    public int TrafficCommand(string[] directions) {

    }
}
```

tab: JavaScript

```javascript
/**
 * @param {string[]} directions
 * @return {number}
 */
var trafficCommand = function(directions) {

};
```

tab: TypeScript

```typescript
function trafficCommand(directions: string[]): number {

};
```

tab: PHP

```php
class Solution {

    /**
     * @param String[] $directions
     * @return Integer
     */
    function trafficCommand($directions) {

    }
}
```

tab: Swift

```swift
class Solution {
    func trafficCommand(_ directions: [String]) -> Int {

    }
}
```

tab: Kotlin

```kotlin
class Solution {
    fun trafficCommand(directions: Array<String>): Int {

    }
}
```

tab: Dart

```dart
class Solution {
  int trafficCommand(List<String> directions) {

  }
}
```

tab: Go

```go
func trafficCommand(directions []string) int {

}
```

tab: Ruby

```ruby
# @param {String[]} directions
# @return {Integer}
def traffic_command(directions)

end
```

tab: Scala

```scala
object Solution {
    def trafficCommand(directions: Array[String]): Int = {

    }
}
```

tab: Rust

```rust
impl Solution {
    pub fn traffic_command(directions: Vec<String>) -> i32 {

    }
}
```

tab: Racket

```racket
(define/contract (traffic-command directions)
  (-> (listof string?) exact-integer?)

  )
```

tab: Erlang

```erlang
-spec traffic_command(Directions :: [unicode:unicode_binary()]) -> integer().
traffic_command(Directions) ->
  .
```

tab: Elixir

```elixir
defmodule Solution do
  @spec traffic_command(directions :: [String.t]) :: integer
  def traffic_command(directions) do

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
          
