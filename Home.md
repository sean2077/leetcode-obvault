---
tags: 
aliases:
  - LeetCode
cssclasses:
  - noyaml
---

# LeetCode 题库


```dataviewjs
// 表头
const header = ["题号", "标题", "标题(中)", "分类", "难度", "通过率", "评分", "解法", "笔记", "收藏"];

// 获取初始数据
let initialData = dv.pages("#leetcode/problem")
    .sort((p) => [parseInt(p.questionId) || 100000000, p.questionId])
    .map((p) => [p.file.link, p.title, p.translatedTitle, p.lcTopics, p.lcDifficulty, p.lcAcRate, p.grade, p.solutions, p.notes, p.favorites])
    .array();

dv.paragraph("\n");

// 根容器
let rootContainer = this.container;

/// 创建检索容器
const filterContainer = dv.el("div", "", {
    attr: {
        style: "display: flex; justify-content: center; align-items: center; gap: 10px; margin-bottom: 10px;"
    }
});
// 创建分类选择器
const allTopics = Array.from(new Set(dv.pages("#leetcode/topic").sort(p => p.title).map(p => p.file.name)));
dv.el("span", "选择分类：", { container: filterContainer });
const topicSelect = dv.el("select", "", { container: filterContainer });
dv.el("option", "所有分类", { container: topicSelect, attr: { value: "" } });
allTopics.forEach(topic => { dv.el("option", topic, { container: topicSelect, attr: { value: topic } }); });
// 创建难度选择器
dv.el("span", "选择难度：", { container: filterContainer });
const difficultySelect = dv.el("select", "", { container: filterContainer });
["所有难度", "Easy", "Medium", "Hard"].forEach(diff => { dv.el("option", diff, { container: difficultySelect, attr: { value: diff === "所有难度" ? "" : diff } }); });
// 创建评分选择器
dv.el("span", "选择评分：", { container: filterContainer });
const gradeSelect = dv.el("select", "", { container: filterContainer });
["所有评分", "⭐⭐⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐", "⭐⭐", "⭐"].forEach(grade => { dv.el("option", grade, { container: gradeSelect, attr: { value: grade === "所有评分" ? "" : grade } }); });
// 创建是否有解法选择器
dv.el("span", "是否有解法：", { container: filterContainer });
const hasSolutionSelect = dv.el("select", "", { container: filterContainer });
["全部", "有解法", "无解法"].forEach(option => { dv.el("option", option, { container: hasSolutionSelect, attr: { value: option } }); });
// 创建是否收藏选择器
dv.el("span", "是否收藏：", { container: filterContainer });
const isFavoriteSelect = dv.el("select", "", { container: filterContainer });
["全部", "已收藏", "未收藏"].forEach(option => { dv.el("option", option, { container: isFavoriteSelect, attr: { value: option } }); });

// 筛选函数
function filterData(data) {
    return data.filter(item => {
        const topicMatch = !topicSelect.value || (item[3] && item[3].some(t => t.fileName() === topicSelect.value));
        const difficultyMatch = !difficultySelect.value || item[4] === difficultySelect.value;
        const gradeMatch = !gradeSelect.value || item[6] === gradeSelect.value;
        const solutions = item[7]?.length || 0;
        const solutionMatch = hasSolutionSelect.value === "全部" ||
            (hasSolutionSelect.value === "有解法" && solutions > 0) ||
            (hasSolutionSelect.value === "无解法" && solutions === 0);
        const favorites = item[9]?.length || 0 ;
        const favoriteMatch = isFavoriteSelect.value === "全部" || 
            (isFavoriteSelect.value === "已收藏" && favorites > 0) ||
            (isFavoriteSelect.value === "未收藏" && favorites === 0);
        return topicMatch && difficultyMatch && gradeMatch && solutionMatch && favoriteMatch; 
    });
}
let data = filterData(initialData);
// 更新表格函数
async function updateTable(evt) {
    evt.preventDefault();
    data = filterData(initialData);
    renderTable();
}
// 为选择器添加事件监听器
[topicSelect, difficultySelect, hasSolutionSelect, isFavoriteSelect, gradeSelect].forEach(select => {
    select.addEventListener("change", updateTable);
});


// 初始化或获取当前页码
if (!global.pageNum) {
    global.pageNum = 0;
}
let pageSize = 10;

/// 创建控制容器
const controlContainer = dv.el("div", "", {
    container: rootContainer,
    attr: {
        style: "display: flex; justify-content: center; align-items: center; gap: 10px; margin-bottom: 10px;"
    },
});
// 创建控制按钮
const createButton = (text, onClick) => {
    return dv.el("button", text, {
        container: controlContainer,
        attr: { style: "padding: 5px 10px;" },
        onclick: onClick
    });
};
createButton("首页", () => {
    global.pageNum = 0;
    renderTable();
});
createButton("上十页", () => {
    global.pageNum = Math.max(global.pageNum - 10, 0);
    renderTable();
});
createButton("上一页", () => {
    global.pageNum = Math.max(global.pageNum - 1, 0);
    renderTable();
});

const pageInfo = dv.el("span", "", { container: controlContainer });

createButton("下一页", () => {
    global.pageNum = Math.min(global.pageNum + 1, Math.ceil(data.length / pageSize) - 1);
    renderTable();
});
createButton("下十页", () => {
    global.pageNum = Math.min(global.pageNum + 10, Math.ceil(data.length / pageSize) - 1);
    renderTable();
});
createButton("尾页", () => {
    global.pageNum = Math.ceil(data.length / pageSize) - 1;
    renderTable();
});
// 选择页码
dv.el("span", "跳转至", { container: controlContainer });
const pageInput = dv.el("input", "", {
    container: controlContainer,
    attr: {
        type: "number",
        value: global.pageNum + 1,
        style: "width: 50px; text-align: center; margin: 0 5px;"
    }
});
dv.el("span", "页", { container: controlContainer });
pageInput.onchange = (e) => {
    global.pageNum = Math.min(Math.max(0, e.target.value - 1), Math.ceil(data.length / pageSize) - 1);
    renderTable();
};
// 每页大小
dv.el("span", "每页", { container: controlContainer });
const pageSizeInput = dv.el("input", "", {
    container: controlContainer,
    attr: {
        type: "number",
        value: pageSize,
        style: "width: 50px; text-align: center; margin: 0 5px;"
    }
});
dv.el("span", "条", { container: controlContainer });
pageSizeInput.onchange = (e) => {
    pageSize = e.target.value;
    global.pageNum = 0;
    renderTable();
};
// 共多少项
const totalItems = dv.el("span", `共 ${data.length} 项`, { container: controlContainer });

// 渲染表格函数
function renderTable(remove = true) {
    if (remove) rootContainer.lastChild.remove(); // 移除上一次的表格
    const startIndex = global.pageNum * pageSize;
    const endIndex = startIndex + pageSize;
    dv.table(header, data.slice(startIndex, endIndex));
    pageInfo.innerText = ` 第 ${global.pageNum + 1} 页，共 ${Math.ceil(data.length / pageSize)} 页 `;
    totalItems.innerText = ` 共 ${data.length} 项 `;
}

// 初始渲染
renderTable(false);

```
