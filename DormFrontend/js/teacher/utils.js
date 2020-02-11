data = []
cookie = document.cookie.split("; ");
cookie.forEach(function (item) {
    temp = item.split("=");
    data[temp[0]] = temp[1];
})
console.log("logined:", data["is_login"])
if(data["is_login"] == 'False' || data["is_login"] == undefined){   // 对登录状态进行检查, 未登录则立即返回登录页面
    window.location.href = "/index";
}