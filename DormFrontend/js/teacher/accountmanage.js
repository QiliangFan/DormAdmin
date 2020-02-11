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
        $("#import_student_account").hover(function () {
            $("#import_student_account").addClass("hover-disable");
            $("#import_student_account").attr("href", "#");
        });

        $("#import_first_level_manage_account").hover(function () {
            $("#import_first_level_manage_account").addClass("hover-disable");
            $("#import_first_level_manage_account").attr("href", "#");
        });

        $("#import_second_level_manage_account").hover(function () {
            $("#import_second_level_manage_account").addClass("hover-disable");
            $("#import_second_level_manage_account").attr("href", "#");
        });

        $("#delte_account").hover(function () {
            $("#delte_account").addClass("hover-disable");
            $("#delte_account").attr("href", "#");
        });

        $("#reset_account").hover(function () {
            $("#reset_account").addClass("hover-disable");
            $("#reset_account").attr("href", "#");
        });
    }
}