var software_options = [
    "本科生",
    "研究生",
    "全部"
];

var biology_options = [
    "泰达籍",
    "生科籍",
    "全部"
];

var physics_options = [
    "泰达籍",
    "物理籍",
    "临时",
    "全部"
];

var environment_options = [
    "全部"
];

var medicine_options = [
    "全部"
];


$(function () {
    // 改变学院时触发事件:
    $("#campus").change(function () {
        console.log($("#campus").val())
        switch ($("#campus").val()) {
            case "软件学院": {
                console.log("???")
                $("#only_see").empty()
                for (let i in software_options) {
                    $("#only_see").append($("<option value='" + software_options[i] + "'>" + software_options[i] + "</option>"))
                }
                break;
            }
            case "生物学院": {
                $("#only_see").empty()
                for (let i in biology_options) {
                    $("#only_see").append("<option value='" + biology_options[i] + "'>" + biology_options[i] + "</option>")
                }
                break;
                break;
            }
            case "物理学院": {
                $("#only_see").empty()
                for (let i in physics_options) {
                    $("#only_see").append("<option value='" + physics_options[i] + "'>" + physics_options[i] + "</option>")
                }
                break;
            }
            case "环境工程与工程学院": {
                $("#only_see").empty()
                for (let i in environment_options) {
                    $("#only_see").append("<option value='" + environment_options[i] + "'>" + environment_options[i] + "</option>")
                }
                break;
            }
            case "药学院": {
                $("#only_see").empty()
                for (let i in medicine_options) {
                    $("#only_see").append("<option value='" + medicine_options[i] + "'>" + medicine_options[i] + "</option>")
                }
                break;
            }
            default: {
                $("#only_see").empty()
            }

        }
    })

});

function inspection_history_search() {
    var start_time = $("#start_time").val();
    var end_time = $("#end_time").val();
    var campus = $("#campus").val();
    if (campus == "...") campus = "";
    var only_see = $("#only_see").val() ? $("#only_see").val() : "";
    console.log(start_time, end_time, campus, only_see);

    window.location.href = "/teacher/inspection_history_search?start_time=" + start_time +
        "&end_time=" + end_time + "&campus=" + campus + "&only_see=" + only_see;
}