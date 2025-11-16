
/**
 * Create a paginated table with navigation controls
 * @param {HTMLElement} container - The container element
 * @param {Array<string>} header - Table header columns
 * @param {Array<Array>} data - Table data rows
 * @param {number} pageSize - Number of rows per page (default: 10)
 */
function pagingTable(container, header, data, pageSize = 10) {
    // Initialize page state
    if (!global.pageNum) {
        global.pageNum = 0;
    }

    // Cache frequently used values
    const totalPages = Math.ceil(data.length / pageSize);

    // Create control container
    const controlContainer = dv.el("div", "", {
        container: container,
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
        if (remove && container.lastChild) {
            container.lastChild.remove();
        }

        const startIndex = global.pageNum * pageSize;
        const endIndex = Math.min(startIndex + pageSize, data.length);
        const currentTotalPages = Math.ceil(data.length / pageSize);

        // Render table
        dv.table(header, data.slice(startIndex, endIndex));

        // Update controls
        pageInfo.innerText = `Page ${global.pageNum + 1} of ${currentTotalPages}`;
        totalItems.innerText = `Total: ${data.length} items`;
        pageInput.value = (global.pageNum + 1).toString();
        pageInput.max = currentTotalPages.toString();
    }

    // Initial render
    renderTable(false);
}

// Execute with input parameters
pagingTable(input.container, input.header, input.data, input.pageSize);