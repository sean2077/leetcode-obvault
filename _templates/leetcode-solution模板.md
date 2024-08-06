<%-*
const dstRoot = "Problems/";

// 获取当前的路径
let path = tp.file.folder(true);
// 如果是以 Problems/{question}/xxx.md 的形式命名的文件, 提取 question
let question = '';
if (path.includes(dstRoot)) {
    question = path.split(dstRoot)[1].split("/")[0];
    question = `"[[${question}]]"`;
}
_%>

---
tags:
  - leetcode/solution
question: <% question %>
desc: 
program_language: 
time_complexity: 
space_complexity: 
grade: ⭐⭐⭐
relative_links: 
cssclasses: 
created: <% tp.date.now("YYYY-MM-DD HH:mm") %>
updated: 
---
