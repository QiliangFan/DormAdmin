/*
    登录权限验证
 */

data = []
cookie = document.cookie.split("; ");
cookie.forEach(function (item) {
    temp = item.split("=");
    data[temp[0]] = temp[1];
})
console.log("logined:", data["is_login"])
if (data["is_login"] == 'False' || data["is_login"] == undefined) {   // 对登录状态进行检查, 未登录则立即返回登录页面
    window.location.href = "/index";
}


/*
    分页
    tbody 的 id 应该设置为 divide_page_table
    四个按钮分别是:
    #first
    #previous
    #next
    #last
*/


var item_list = [];
var cur_page = 0;
var max_page = 0;
var itemnumber_per_page = 0;
var total_number = 0;
var start_offset = 0;
var end_offset = 0;

function init(list, __itemnumber_per_page) {
    item_list = list;
    total_number = list.length;
    itemnumber_per_page = __itemnumber_per_page;
    max_page = Math.ceil(total_number / itemnumber_per_page);

    if (cur_page < max_page - 1) {
        end_offset = start_offset + itemnumber_per_page - 1;
    } else {
        end_offset = start_offset + total_number % itemnumber_per_page - 1;
    }

    $("#first").attr("disabled", "disabled");
    $("#previous").attr("disabled", "disabled");
    if (cur_page >= max_page - 1) {
        $("#next").attr("disabled", "disabled");
        $("#last").attr("disabled", "disabled");
    }

}

function first() {
    cur_page = 0;
    start_offset = 0;
    end_offset = 0;
    if (cur_page < max_page - 1) {
        end_offset = start_offset + itemnumber_per_page - 1;
    } else {
        end_offset = start_offset + total_number % itemnumber_per_page - 1;
    }

    $("#first").attr("disabled", "disabled");
    $("#previous").attr("disabled", "disabled");
    $("#next").removeAttr("disabled")
    $("#last").removeAttr("disabled")

    refresh()
}

function previous() {
    cur_page--;
    start_offset = cur_page * itemnumber_per_page;
    if (cur_page < max_page - 1) {
        end_offset = start_offset + itemnumber_per_page - 1;
    } else {
        end_offset = start_offset + total_number % itemnumber_per_page - 1;
    }

    if (cur_page == 0) {
        $("#first").attr("disabled", "disabled");
        $("#previous").attr("disabled", "disabled");
    }
    $("#next").removeAttr("disabled");
    $("#last").removeAttr("disabled");

    refresh()
}

function next() {
    cur_page++;
    start_offset = cur_page * itemnumber_per_page;
    if (cur_page < max_page - 1) {
        end_offset = start_offset + itemnumber_per_page - 1;
    } else {
        end_offset = start_offset + total_number % itemnumber_per_page - 1;
    }
    if (cur_page == max_page - 1) {
        $("#next").attr("disabled", "disabled");
        $("#last").attr("disabled", "disabled");
    }
    $("#first").removeAttr("disabled");
    $("#previous").removeAttr("disabled");

    refresh()
}

function last() {
    cur_page = max_page - 1;
    start_offset = cur_page * itemnumber_per_page;
    if (cur_page < max_page - 1) {
        end_offset = start_offset + itemnumber_per_page - 1;
    } else {
        end_offset = start_offset + total_number % itemnumber_per_page - 1;
    }

    $("#first").removeAttr("disabled");
    $("#previous").removeAttr("disabled");
    $("#next").attr("disabled", "disabled");
    $("#last").attr("disabled", "disabled");

    refresh()
}