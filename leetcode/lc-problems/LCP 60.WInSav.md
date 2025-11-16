---
tags:
  - leetcode/problem
questionId: "LCP 60"
title: 力扣泡泡龙
translatedTitle: 力扣泡泡龙
titleSlug: WInSav
aliases:
  - 力扣泡泡龙
  - WInSav
  - 力扣泡泡龙
lcLinks:
  - https://leetcode.com/problems/WInSav/
  - https://leetcode.cn/problems/WInSav/
lcTopics:
lcDifficulty: Hard
lcAcRate: 20.8%
similarQuestions:
grade: ⭐⭐⭐⭐⭐
likes: 16
dislikes: 0
favorites: []
created: 2025-11-16 12:09
updated: 2025-11-16 12:09
---

**Nav:** << previous: [[LCP 59.NfY1m5|LCP 59.搭桥过河]] | next: [[LCP 61.6CE719|LCP 61.气温变化趋势]] >>

---

## Description

欢迎各位勇者来到力扣城，本次试炼主题为「力扣泡泡龙」。

游戏初始状态的泡泡形如二叉树 `root`，每个节点值对应了该泡泡的分值。勇者最多可以击破一个节点泡泡，要求满足：
- 被击破的节点泡泡 **至多** 只有一个子节点泡泡
- 当被击破的节点泡泡有子节点泡泡时，则子节点泡泡将取代被击破泡泡的位置
    > 注：即整棵子树泡泡上移

请问在击破一个节点泡泡操作或无击破操作后，二叉泡泡树的最大「层和」是多少。

**注意：**
- 「层和」为同一高度的所有节点的分值之和

**示例 1：**
> 输入：`root = [6,0,3,null,8]`
>
> 输出：`11`
>
> 解释：勇者的最佳方案如图所示
>![image.png](https://pic.leetcode-cn.com/1648180809-XSWPLu-image.png){:height="100px"}



**示例 2：**
> 输入：`root = [5,6,2,4,null,null,1,3,5]`
>
> 输出：`9`
>
> 解释：勇者击破 6 节点，此时「层和」最大为 3+5+1 = 9
>![image.png](https://pic.leetcode-cn.com/1648180769-TLpYop-image.png){:height="200px"}



**示例 3：**
> 输入：`root = [-5,1,7]`
>
> 输出：`8`
>
> 解释：勇者不击破节点，「层和」最大为 1+7 = 8


**提示**：
- `2 <= 树中节点个数 <= 10^5`
- `-10000 <= 树中节点的值 <= 10000`



---

[提交记录](https://leetcode.cn/problems/WInSav/submissions/) | [题解](https://leetcode.cn/problems/WInSav/solution/)


## Solutions & Notes

```base
properties:
  note.updated:
    displayName: Last Updated
  note.relative_links:
    displayName: Related Links
  note.desc:
    displayName: Description
  note.grade:
    displayName: Rating
  note.program_language:
    displayName: Language
  note.time_complexity:
    displayName: TC
  note.space_complexity:
    displayName: SC
views:
  - type: table
    name: Solutions & Notes
    filters:
      and:
        - file.hasLink(this.file)
        - file.tags.containsAny("leetcode/solution", "leetcode/note")
    order:
      - file.name
      - desc
      - program_language
      - time_complexity
      - space_complexity
      - grade
      - relative_links
      - updated
    sort:
      - property: grade
        direction: ASC
      - property: time_complexity
        direction: ASC
      - property: program_language
        direction: ASC
    columnSize:
      file.name: 104
      note.space_complexity: 65
      note.grade: 126

```

## Similar Problems

```base
properties:
  note.lcTopics:
    displayName: Topics
  note.lcAcRate:
    displayName: AC Rate
  note.favorites:
    displayName: Favorites
  note.grade:
    displayName: Rating
  note.translatedTitle:
    displayName: Title (CN)
  note.lcDifficulty:
    displayName: Difficulty
views:
  - type: table
    name: Similar Problems
    filters:
      and:
        - file.hasLink(this.file)
        - similarQuestions.contains(this.file)
    order:
      - file.name
      - translatedTitle
      - lcTopics
      - lcDifficulty
      - lcAcRate
      - grade
      - favorites
    sort:
      - property: file.name
        direction: ASC
      - property: lcTopics
        direction: DESC
    columnSize:
      note.translatedTitle: 240
      note.lcTopics: 347
      note.lcAcRate: 75
      note.grade: 122

```