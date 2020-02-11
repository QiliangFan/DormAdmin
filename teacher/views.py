from django.db.models import Q
from django.http import HttpRequest
from django.shortcuts import render

from DormBackend.models import Teacher, ManagerAccount, InspectionHistory, Student


def index(request: HttpRequest):
    return render(request, "teacher/index.html", {})


def space(request: HttpRequest):
    is_login = request.COOKIES["is_login"]
    account = request.COOKIES["account"]
    tea = Teacher.objects.filter(tea_id=account).first()
    return render(request, "teacher/space.html", {"tea":tea})


def dormmanage(request: HttpRequest):
    return render(request, "teacher/dormmange.html", {})


def targetsearch(request: HttpRequest):
    return render(request, "teacher/targetsearch.html", {})


def inspection_history(request: HttpRequest):
    cookie = request.COOKIES
    account = cookie["account"]
    level = cookie["level"]

    tea = Teacher.objects.filter(tea_id=account).first()
    data = {
        "college": tea.college,
        "level": level
    }
    print("data:", data)
    return render(request, "teacher/components/inspection_history.html", data)


def inspection_history_search(request: HttpRequest):
    print(request.GET.dict())
    print(request.COOKIES)
    data = request.GET.dict()
    cookie = request.COOKIES

    level = cookie["level"]
    account = cookie["account"]

    start_time = data["start_time"]
    end_time = data["end_time"]
    campus = data["campus"]
    only_see = data["only_see"]
    if only_see == "全部" or only_see == "":
        only_see = ""

    if campus != "":  # 对学院进行筛选
        if only_see != "":  # 对detail进行筛选
            stu_list = Student.objects.filter(Q(campus=campus)&Q(detail=only_see))
            room_list = []
            room_id_list = []
            for stu_item in stu_list:
                room_list.append(stu_item.room)
                room_id_list.append(stu_item.room.id)
            result = InspectionHistory.objects.filter(Q(date__gt=start_time)&Q(date__lt=end_time)&Q(room_id__in=room_id_list))
            result = list(result)
        else:  # 不对进行detail筛选
            stu_list = Student.objects.filter(Q(campus=campus))
            room_list = []
            room_id_list = []
            for stu_item in stu_list:
                room_list.append(stu_item.room)
                room_id_list.append(stu_item.room.id)
            result = InspectionHistory.objects.filter(
                Q(date__gt=start_time) & Q(date__lt=end_time) & Q(room_id__in=room_id_list))
            result = list(result)
    else:  # 不对学院进行筛选
        stu_list = Student.objects.all()
        room_list = []
        room_id_list = []
        for stu_item in stu_list:
            room_list.append(stu_item.room)
            room_id_list.append(stu_item.room.id)
        result = InspectionHistory.objects.filter(
            Q(date__gt=start_time) & Q(date__lt=end_time) & Q(room_id__in=room_id_list))
        result = list(result)

    return render(request, "teacher/table/inspection_history_table.html", {"history": result})


def inspection_warning(request: HttpRequest):
    return render(request, "teacher/components/inspection_warning.html", {})


def add_inspection_history(request: HttpRequest):
    return render(request, "teacher/components/add_inspection_history.html", {})


def manage_bed(request: HttpRequest):
    return render(request, "teacher/components/manage_bed.html", {})


def del_dorm_information(request: HttpRequest):
    return render(request, "teacher/components/del_dorm_information.html", {})


def modify_self_information(request: HttpRequest):
    data = request.POST.dict()
    tea_id = data["tea_id"]
    name = data["name"]
    tel = data["tel"]
    pwd = data["pwd"]
    tea = Teacher.objects.filter(Q(tea_id=tea_id) & Q(name=name) ).first()
    tea.name = name
    tea.tel = tel
    tea.save()
    if len(pwd) > 0:            # 提供了新密码
        ManagerAccount.objects.filter(account_name=tea_id).update(pwd=pwd)
    return render(request, "teacher/space.html", {"status": "success", "tea": tea})


def accountmanage(request: HttpRequest):
    return render(request, "teacher/accountmanage.html", {})


def delete_account(request: HttpRequest):
    return render(request, "teacher/components/accountmanage/delete_account.html", {})


def import_first_level_manage_account(request: HttpRequest):
    return render(request, "teacher/components/accountmanage/import_first_level_manage_account.html", {})


def import_second_level_manage_account(request: HttpRequest):
    return render(request, "teacher/components/accountmanage/import_second_level_manage_account.html", {})


def import_student_account(request: HttpRequest):
    return render(request, "teacher/components/accountmanage/import_student_account.html", {})


def reset_account(request: HttpRequest):
    return render(request, "teacher/components/accountmanage/reset_account.html", {})