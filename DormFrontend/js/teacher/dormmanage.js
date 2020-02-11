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
        $("#del_dorm_information").hover(function () {
            $("#del_dorm_information").addClass("hover-disable");
            $("#del_dorm_information").attr("href", "#");
        });

        $("#manage_bed").hover(function () {
            $("#manage_bed").addClass("hover-disable");
            $("#manage_bed").attr("href", "#");
        });
    }
}