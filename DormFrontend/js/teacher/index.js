$(function () {
    check_level();


});

function check_level() {
    data = [];
    cookie = document.cookie.split("; ")
    cookie.forEach(function (item) {
        temp = item.split("=")
        data[temp[0]] = temp[1];
    })
    console.log(data)

    if(data["level"] == "1") {
        $("#add_inspection_history").hover(function () {
            $("#add_inspection_history").addClass("hover-disable");
            $("#add_inspection_history").attr("href", "#");
        });

        $("#inspection_warning").hover(function () {
            $("#inspection_warning").addClass("hover-disable");
            $("#inspection_warning").attr("href", "#");
        });
    }
}