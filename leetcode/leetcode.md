---
tags: 
aliases:
  - LeetCode
cssclasses:
  - noyaml
---

# LeetCode Dashboard


```dataviewjs
// Table header
const header = ["ID", "Title", "Title (CN)", "Topics", "Difficulty", "AC Rate", "Rating", "Solutions", "Notes", "Favorites"];

// Get initial data
let initialData = dv.pages("#leetcode/problem")
    .sort((p) => [parseInt(p.questionId) || 100000000, p.questionId])
    .map((p) => [p.file.link, p.title, p.translatedTitle, p.lcTopics, p.lcDifficulty, p.lcAcRate, p.grade, p.solutions, p.notes, p.favorites])
    .array();

dv.paragraph("\n");

// Root container
const rootContainer = this.container;

// Create filter container
const filterContainer = dv.el("div", "", {
    attr: {
        style: "display: flex; justify-content: center; align-items: center; gap: 10px; margin-bottom: 10px; flex-wrap: wrap;"
    }
});

// Helper function to create select element
const createSelect = (label, options, container) => {
    dv.el("span", label, { container, attr: { style: "margin-left: 10px;" } });
    const select = dv.el("select", "", { container });
    options.forEach(opt => {
        const value = typeof opt === "string" ? opt : opt.value;
        const text = typeof opt === "string" ? opt : opt.text;
        dv.el("option", text, { 
            container: select, 
            attr: { value: value === text ? "" : value }
        });
    });
    return select;
};

// Create filter selectors
const allTopics = Array.from(new Set(dv.pages("#leetcode/topic").sort(p => p.title).map(p => p.file.name)));
const topicSelect = createSelect("Topic:", ["All Topics", ...allTopics], filterContainer);

const difficultySelect = createSelect("Difficulty:", [
    { text: "All", value: "" },
    { text: "Easy", value: "Easy" },
    { text: "Medium", value: "Medium" },
    { text: "Hard", value: "Hard" }
], filterContainer);

const gradeSelect = createSelect("Rating:", [
    { text: "All", value: "" },
    { text: "⭐⭐⭐⭐⭐", value: "⭐⭐⭐⭐⭐" },
    { text: "⭐⭐⭐⭐", value: "⭐⭐⭐⭐" },
    { text: "⭐⭐⭐", value: "⭐⭐⭐" },
    { text: "⭐⭐", value: "⭐⭐" },
    { text: "⭐", value: "⭐" }
], filterContainer);

const hasSolutionSelect = createSelect("Solutions:", [
    { text: "All", value: "All" },
    { text: "Has Solutions", value: "Has Solutions" },
    { text: "No Solutions", value: "No Solutions" }
], filterContainer);

const isFavoriteSelect = createSelect("Favorites:", [
    { text: "All", value: "All" },
    { text: "Favorited", value: "Favorited" },
    { text: "Not Favorited", value: "Not Favorited" }
], filterContainer);

// Filter function
function filterData(data) {
    return data.filter(item => {
        const topicMatch = !topicSelect.value || (item[3] && item[3].some(t => t.fileName() === topicSelect.value));
        const difficultyMatch = !difficultySelect.value || item[4] === difficultySelect.value;
        const gradeMatch = !gradeSelect.value || item[6] === gradeSelect.value;
        const solutions = item[7]?.length || 0;
        const solutionMatch = hasSolutionSelect.value === "All" ||
            (hasSolutionSelect.value === "Has Solutions" && solutions > 0) ||
            (hasSolutionSelect.value === "No Solutions" && solutions === 0);
        const favorites = item[9]?.length || 0;
        const favoriteMatch = isFavoriteSelect.value === "All" || 
            (isFavoriteSelect.value === "Favorited" && favorites > 0) ||
            (isFavoriteSelect.value === "Not Favorited" && favorites === 0);
        return topicMatch && difficultyMatch && gradeMatch && solutionMatch && favoriteMatch; 
    });
}

let data = filterData(initialData);

// Update table function
function updateTable() {
    data = filterData(initialData);
    global.pageNum = 0; // Reset to first page when filtering
    renderTable();
}

// Add event listeners to selectors
[topicSelect, difficultySelect, hasSolutionSelect, isFavoriteSelect, gradeSelect].forEach(select => {
    select.addEventListener("change", updateTable);
});

// Initialize page state
if (!global.pageNum) {
    global.pageNum = 0;
}
let pageSize = 10;

// Cache frequently used values
let totalPages = Math.ceil(data.length / pageSize);

// Create control container
const controlContainer = dv.el("div", "", {
    container: rootContainer,
    attr: {
        style: "display: flex; justify-content: center; align-items: center; gap: 10px; margin-bottom: 10px; flex-wrap: wrap;"
    },
});

// Helper function to create buttons
const createButton = (text, onClick) => {
    return dv.el("button", text, {
        container: controlContainer,
        attr: { style: "padding: 5px 10px; cursor: pointer;" },
        onclick: onClick
    });
};

// Navigation buttons
createButton("First", () => {
    global.pageNum = 0;
    renderTable();
});
createButton("‹‹ 10", () => {
    global.pageNum = Math.max(global.pageNum - 10, 0);
    renderTable();
});
createButton("‹ Prev", () => {
    global.pageNum = Math.max(global.pageNum - 1, 0);
    renderTable();
});

const pageInfo = dv.el("span", "", { 
    container: controlContainer,
    attr: { style: "margin: 0 5px; min-width: 120px; text-align: center;" }
});

createButton("Next ›", () => {
    global.pageNum = Math.min(global.pageNum + 1, totalPages - 1);
    renderTable();
});
createButton("10 ››", () => {
    global.pageNum = Math.min(global.pageNum + 10, totalPages - 1);
    renderTable();
});
createButton("Last", () => {
    global.pageNum = totalPages - 1;
    renderTable();
});

// Page jump control
dv.el("span", "Go to", { 
    container: controlContainer,
    attr: { style: "margin-left: 15px;" }
});
const pageInput = dv.el("input", "", {
    container: controlContainer,
    attr: {
        type: "number",
        min: "1",
        max: totalPages.toString(),
        value: (global.pageNum + 1).toString(),
        style: "width: 50px; text-align: center; margin: 0 5px;"
    }
});
dv.el("span", "page", { container: controlContainer });

pageInput.addEventListener("change", (e) => {
    const newPage = Math.min(Math.max(1, parseInt(e.target.value) || 1), totalPages) - 1;
    global.pageNum = newPage;
    renderTable();
});

// Page size control
dv.el("span", "Show", { 
    container: controlContainer,
    attr: { style: "margin-left: 15px;" }
});
const pageSizeInput = dv.el("input", "", {
    container: controlContainer,
    attr: {
        type: "number",
        min: "1",
        value: pageSize.toString(),
        style: "width: 50px; text-align: center; margin: 0 5px;"
    }
});
dv.el("span", "items", { container: controlContainer });

pageSizeInput.addEventListener("change", (e) => {
    const newSize = Math.max(1, parseInt(e.target.value) || 10);
    pageSize = newSize;
    global.pageNum = 0;
    renderTable();
});

// Total items display
const totalItems = dv.el("span", "", { 
    container: controlContainer,
    attr: { style: "margin-left: 15px; font-weight: 500;" }
});

// Table rendering function
function renderTable(remove = true) {
    // Remove old table if exists
    if (remove && rootContainer.lastChild) {
        rootContainer.lastChild.remove();
    }
    
    // Recalculate total pages based on current data
    totalPages = Math.ceil(data.length / pageSize);
    
    // Ensure current page is valid
    if (global.pageNum >= totalPages && totalPages > 0) {
        global.pageNum = totalPages - 1;
    }
    
    const startIndex = global.pageNum * pageSize;
    const endIndex = Math.min(startIndex + pageSize, data.length);
    
    // Render table
    dv.table(header, data.slice(startIndex, endIndex));
    
    // Update controls
    pageInfo.innerText = `Page ${global.pageNum + 1} of ${totalPages || 1}`;
    totalItems.innerText = `Total: ${data.length} items`;
    pageInput.value = (global.pageNum + 1).toString();
    pageInput.max = (totalPages || 1).toString();
}

// Initial render
renderTable(false);

```
