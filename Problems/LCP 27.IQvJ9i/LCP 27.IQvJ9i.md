---
tags:
  - leetcode/problem
questionId: LCP 27
title: 黑盒光线反射
translatedTitle: 黑盒光线反射
titleSlug: IQvJ9i
aliases:
  - 黑盒光线反射
  - IQvJ9i
  - 黑盒光线反射
lcLink: https://leetcode.com/problems/IQvJ9i/
lcTopics:
  - '[[design]]'
  - '[[segment-tree]]'
  - '[[math]]'
  - '[[ordered-set]]'
lcDifficulty: Hard
lcAcRate: 35.0%
similarQuestions: []
grade: ⭐⭐⭐⭐⭐
likes: 21
dislikes: 0
favorites: []
solutions: []
notes: []
cssclasses: []
created: 2024-08-13 00:10
updated:
---

**Nav:** << previous: [[LCP 26.hSRGyL]] | next: [[LCP 28.4xy4Wx]] >>

---

## Description

~~~tabs
tab: English

No description

---

[submissions](https://leetcode.com/problems/IQvJ9i/submissions/) | [solutions](https://leetcode.com/problems/IQvJ9i/solutions/)


tab: 中文

秋日市集上有个奇怪的黑盒，黑盒的主视图为 n\*m 的矩形。从黑盒的主视图来看，黑盒的上面和下面各均匀分布有 m 个小孔，黑盒的左面和右面各均匀分布有 n 个小孔。黑盒左上角小孔序号为 0，按顺时针编号，总共有 2*(m+n) 个小孔。每个小孔均可以打开或者关闭，初始时，所有小孔均处于关闭状态。每个小孔上的盖子均为镜面材质。例如一个 2\*3 的黑盒主视图与其小孔分布如图所示:

![image.png](https://pic.leetcode-cn.com/1598951281-ZCBrif-image.png){:height="200px"}

店长告诉小扣，这里是「几何学的快问快答」，店长可能有两种操作：

- `open(int index, int direction)` - 若小孔处于关闭状态，则打开小孔，照入光线；否则直接照入光线；
- `close(int index)` - 关闭处于打开状态小孔，店长保证不会关闭已处于关闭状态的小孔；

其中：
- `index`： 表示小孔序号
- `direction`：`1` 表示光线沿 $y=x$ 方向，`-1` 表示光线沿 $y=-x$ 方向。

![image.png](https://pic.leetcode-cn.com/1599620810-HdOlMi-image.png){:height="200px"}


当光线照至边界时：若边界上的小孔为开启状态，则光线会射出；否则，光线会在小孔之间进行反射。特别地：
1. 若光线射向未打开的拐角（黑盒顶点），则光线会原路反射回去；
2. 光线自拐角处的小孔照入时，只有一种入射方向（如自序号为 0 的小孔照入方向只能为 `-1`）

![image.png](https://pic.leetcode-cn.com/1598953840-DLiAsf-image.png){:height="200px"}

请帮助小扣判断并返回店长每次照入的光线从几号小孔射出。


**示例 1：**
>输入：
>`["BlackBox","open","open","open","close","open"]`
>`[[2,3],[6,-1],[4,-1],[0,-1],[6],[0,-1]]`
>
>输出：`[null,6,4,6,null,4]`
>
>解释：
>BlackBox b = BlackBox(2,3); // 新建一个 2x3 的黑盒
>b.open(6,-1) // 打开 6 号小孔，并沿 y=-x 方向照入光线，光线至 0 号小孔反射，从 6 号小孔射出
>b.open(4,-1) // 打开 4 号小孔，并沿 y=-x 方向照入光线，光线轨迹为 4-2-8-2-4，从 4 号小孔射出
>b.open(0,-1) // 打开 0 号小孔，并沿 y=-x 方向照入光线，由于 6 号小孔为开启状态，光线从 6 号小孔射出
>b.close(6) // 关闭 6 号小孔
>b.shoot(0,-1) // 从 0 号小孔沿 y=-x 方向照入光线，由于 6 号小孔为关闭状态，4 号小孔为开启状态，光线轨迹为 0-6-4，从 4 号小孔射出

**示例 2：**
>输入：
>`["BlackBox","open","open","open","open","close","open","close","open"]`
>`[[3,3],[1,-1],[5,1],[11,-1],[11,1],[1],[11,1],[5],[11,-1]]`
>
>输出：`[null,1,1,5,1,null,5,null,11]`
>
>解释：
>
>![image.png](https://pic.leetcode-cn.com/1599204202-yGDMVk-image.png){:height="300px"}
>
>BlackBox b = BlackBox(3,3); // 新建一个 3x3 的黑盒
>b.open(1,-1) // 打开 1 号小孔，并沿 y=-x 方向照入光线，光线轨迹为 1-5-7-11-1，从 1 号小孔射出
>b.open(5,1) // 打开 5 号小孔，并沿 y=x 方向照入光线，光线轨迹为 5-7-11-1，从 1 号小孔射出
>b.open(11,-1) // 打开 11 号小孔，并沿逆 y=-x 方向照入光线，光线轨迹为 11-7-5，从 5 号小孔射出
>b.open(11,1) // 从 11 号小孔沿 y=x 方向照入光线，光线轨迹为 11-1，从 1 号小孔射出
>b.close(1) // 关闭 1 号小孔
>b.open(11,1) // 从 11 号小孔沿 y=x 方向照入光线，光线轨迹为 11-1-5，从 5 号小孔射出
>b.close(5) // 关闭 5 号小孔
>b.open(11,-1) // 从 11 号小孔沿 y=-x 方向照入光线，光线轨迹为 11-1-5-7-11，从 11 号小孔射出



**提示：**
- `1 <= n, m <= 10000`
- `1 <= 操作次数 <= 10000`
- `direction` 仅为 `1` 或 `-1`
- `0 <= index < 2*(m+n)`


---

[提交记录](https://leetcode.cn/problems/IQvJ9i/submissions/) | [题解](https://leetcode.cn/problems/IQvJ9i/solution/)


~~~

## Code Snippets

~~~tabs
tab: C++

```cpp
class BlackBox {
public:
    BlackBox(int n, int m) {

    }
    
    int open(int index, int direction) {

    }
    
    void close(int index) {

    }
};

/**
 * Your BlackBox object will be instantiated and called as such:
 * BlackBox* obj = new BlackBox(n, m);
 * int param_1 = obj->open(index,direction);
 * obj->close(index);
 */
```

tab: Java

```java
class BlackBox {

    public BlackBox(int n, int m) {

    }
    
    public int open(int index, int direction) {

    }
    
    public void close(int index) {

    }
}

/**
 * Your BlackBox object will be instantiated and called as such:
 * BlackBox obj = new BlackBox(n, m);
 * int param_1 = obj.open(index,direction);
 * obj.close(index);
 */
```

tab: Python

```python
class BlackBox(object):

    def __init__(self, n, m):
        """
        :type n: int
        :type m: int
        """


    def open(self, index, direction):
        """
        :type index: int
        :type direction: int
        :rtype: int
        """


    def close(self, index):
        """
        :type index: int
        :rtype: None
        """



# Your BlackBox object will be instantiated and called as such:
# obj = BlackBox(n, m)
# param_1 = obj.open(index,direction)
# obj.close(index)
```

tab: Python3

```python
class BlackBox:

    def __init__(self, n: int, m: int):


    def open(self, index: int, direction: int) -> int:


    def close(self, index: int) -> None:



# Your BlackBox object will be instantiated and called as such:
# obj = BlackBox(n, m)
# param_1 = obj.open(index,direction)
# obj.close(index)
```

tab: C

```c



typedef struct {

} BlackBox;


BlackBox* blackBoxCreate(int n, int m) {

}

int blackBoxOpen(BlackBox* obj, int index, int direction) {

}

void blackBoxClose(BlackBox* obj, int index) {

}

void blackBoxFree(BlackBox* obj) {

}

/**
 * Your BlackBox struct will be instantiated and called as such:
 * BlackBox* obj = blackBoxCreate(n, m);
 * int param_1 = blackBoxOpen(obj, index, direction);
 
 * blackBoxClose(obj, index);
 
 * blackBoxFree(obj);
*/
```

tab: C#

```csharp
public class BlackBox {

    public BlackBox(int n, int m) {

    }
    
    public int Open(int index, int direction) {

    }
    
    public void Close(int index) {

    }
}

/**
 * Your BlackBox object will be instantiated and called as such:
 * BlackBox obj = new BlackBox(n, m);
 * int param_1 = obj.Open(index,direction);
 * obj.Close(index);
 */
```

tab: JavaScript

```javascript
/**
 * @param {number} n
 * @param {number} m
 */
var BlackBox = function(n, m) {

};

/** 
 * @param {number} index 
 * @param {number} direction
 * @return {number}
 */
BlackBox.prototype.open = function(index, direction) {

};

/** 
 * @param {number} index
 * @return {void}
 */
BlackBox.prototype.close = function(index) {

};

/**
 * Your BlackBox object will be instantiated and called as such:
 * var obj = new BlackBox(n, m)
 * var param_1 = obj.open(index,direction)
 * obj.close(index)
 */
```

tab: TypeScript

```typescript
class BlackBox {
    constructor(n: number, m: number) {

    }

    open(index: number, direction: number): number {

    }

    close(index: number): void {

    }
}

/**
 * Your BlackBox object will be instantiated and called as such:
 * var obj = new BlackBox(n, m)
 * var param_1 = obj.open(index,direction)
 * obj.close(index)
 */
```

tab: PHP

```php
class BlackBox {
    /**
     * @param Integer $n
     * @param Integer $m
     */
    function __construct($n, $m) {

    }

    /**
     * @param Integer $index
     * @param Integer $direction
     * @return Integer
     */
    function open($index, $direction) {

    }

    /**
     * @param Integer $index
     * @return NULL
     */
    function close($index) {

    }
}

/**
 * Your BlackBox object will be instantiated and called as such:
 * $obj = BlackBox($n, $m);
 * $ret_1 = $obj->open($index, $direction);
 * $obj->close($index);
 */
```

tab: Swift

```swift

class BlackBox {

    init(_ n: Int, _ m: Int) {

    }
    
    func open(_ index: Int, _ direction: Int) -> Int {

    }
    
    func close(_ index: Int) {

    }
}

/**
 * Your BlackBox object will be instantiated and called as such:
 * let obj = BlackBox(n, m)
 * let ret_1: Int = obj.open(index, direction)
 * obj.close(index)
 */
```

tab: Kotlin

```kotlin
class BlackBox(n: Int, m: Int) {

    fun open(index: Int, direction: Int): Int {

    }

    fun close(index: Int) {

    }

}

/**
 * Your BlackBox object will be instantiated and called as such:
 * var obj = BlackBox(n, m)
 * var param_1 = obj.open(index,direction)
 * obj.close(index)
 */
```

tab: Dart

```dart
class BlackBox {

  BlackBox(int n, int m) {

  }
  
  int open(int index, int direction) {

  }
  
  void close(int index) {

  }
}

/**
 * Your BlackBox object will be instantiated and called as such:
 * BlackBox obj = BlackBox(n, m);
 * int param1 = obj.open(index,direction);
 * obj.close(index);
 */
```

tab: Go

```go
type BlackBox struct {

}


func Constructor(n int, m int) BlackBox {

}


func (this *BlackBox) Open(index int, direction int) int {

}


func (this *BlackBox) Close(index int)  {

}


/**
 * Your BlackBox object will be instantiated and called as such:
 * obj := Constructor(n, m);
 * param_1 := obj.Open(index,direction);
 * obj.Close(index);
 */
```

tab: Ruby

```ruby
class BlackBox

=begin
    :type n: Integer
    :type m: Integer
=end
    def initialize(n, m)

    end


=begin
    :type index: Integer
    :type direction: Integer
    :rtype: Integer
=end
    def open(index, direction)

    end


=begin
    :type index: Integer
    :rtype: Void
=end
    def close(index)

    end


end

# Your BlackBox object will be instantiated and called as such:
# obj = BlackBox.new(n, m)
# param_1 = obj.open(index, direction)
# obj.close(index)
```

tab: Scala

```scala
class BlackBox(_n: Int, _m: Int) {

    def open(index: Int, direction: Int): Int = {

    }

    def close(index: Int) {

    }

}

/**
 * Your BlackBox object will be instantiated and called as such:
 * var obj = new BlackBox(n, m)
 * var param_1 = obj.open(index,direction)
 * obj.close(index)
 */
```

tab: Rust

```rust
struct BlackBox {

}


/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl BlackBox {

    fn new(n: i32, m: i32) -> Self {

    }
    
    fn open(&self, index: i32, direction: i32) -> i32 {

    }
    
    fn close(&self, index: i32) {

    }
}

/**
 * Your BlackBox object will be instantiated and called as such:
 * let obj = BlackBox::new(n, m);
 * let ret_1: i32 = obj.open(index, direction);
 * obj.close(index);
 */
```

tab: Racket

```racket
(define black-box%
  (class object%
    (super-new)

    ; n : exact-integer?

    ; m : exact-integer?
    (init-field
      n
      m)
    
    ; open : exact-integer? exact-integer? -> exact-integer?
    (define/public (open index direction)

      )
    ; close : exact-integer? -> void?
    (define/public (close index)

      )))

;; Your black-box% object will be instantiated and called as such:
;; (define obj (new black-box% [n n] [m m]))
;; (define param_1 (send obj open index direction))
;; (send obj close index)
```

tab: Erlang

```erlang
-spec black_box_init_(N :: integer(), M :: integer()) -> any().
black_box_init_(N, M) ->
  .

-spec black_box_open(Index :: integer(), Direction :: integer()) -> integer().
black_box_open(Index, Direction) ->
  .

-spec black_box_close(Index :: integer()) -> any().
black_box_close(Index) ->
  .


%% Your functions will be called as such:
%% black_box_init_(N, M),
%% Param_1 = black_box_open(Index, Direction),
%% black_box_close(Index),

%% black_box_init_ will be called before every test case, in which you can do some necessary initializations.
```

tab: Elixir

```elixir
defmodule BlackBox do
  @spec init_(n :: integer, m :: integer) :: any
  def init_(n, m) do

  end

  @spec open(index :: integer, direction :: integer) :: integer
  def open(index, direction) do

  end

  @spec close(index :: integer) :: any
  def close(index) do

  end
end

# Your functions will be called as such:
# BlackBox.init_(n, m)
# param_1 = BlackBox.open(index, direction)
# BlackBox.close(index)

# BlackBox.init_ will be called before every test case, in which you can do some necessary initializations.
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
          
