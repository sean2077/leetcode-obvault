
function pagingTable(container, header, data, pageSize = 10) {
    // 初始化或获取当前页码
    if (!global.pageNum) {
        global.pageNum = 0;
    }

    // 创建控制容器
    const controlContainer = dv.el("div", "", {
        container: container,
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
        // 清除旧数据
        if (remove) container.lastChild.remove();
        const startIndex = global.pageNum * pageSize;
        const endIndex = startIndex + pageSize;
        dv.table(header, data.slice(startIndex, endIndex));
        pageInfo.innerText = ` 第 ${global.pageNum + 1} 页，共 ${Math.ceil(data.length / pageSize)} 页 `;
        totalItems.innerText = ` 共 ${data.length} 项 `;
    }

    // 初始渲染
    renderTable(false);
}

pagingTable(input.container, input.header, input.data, input.pageSize);