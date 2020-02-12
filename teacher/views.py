from traceback import print_exc

from django.db.models import Q
from django.http import HttpRequest
from django.shortcuts import render

from DormBackend.models import Teacher, ManagerAccount, InspectionHistory, Student, Room, Warning, StuAccount


def targetsearch_result(request: HttpRequest):
    print(request.POST)
    campus = request.POST["campus"]
    build = request.POST["build"]
    room_id = request.POST["room_id"]

    room_list = Room.objects.all()

    if (build != '1') and (build != '2') and (build != '3') and build != 'build':  # 4-7公寓
        door_id = request.POST["door_id"]
        singleRoom_id = request.POST["singleRoom_id"]
        if door_id != 'door_id':
            room_list = room_list.filter(Q(door_id=door_id))
        if singleRoom_id != 'singleRoom_id':
            room_list = room_list.filter(Q(singleRoom_id=singleRoom_id))

    if build != 'build':
        room_list = room_list.filter(Q(build=build))
    if room_id != '':
        room_list = room_list.filter(Q(room_id=room_id))

    # print(room_list)
    # for i in room_list:
    #     print(i.room_id)

    stu = Student.objects.all()
    if campus != 'campus':
        stu = stu.filter(college=campus)
    stu = stu.filter(room__in=room_list)

    # for i in stu:
    #     print(i.stu_id)

    context = {"stu": stu}
    return render(request, "teacher/targetsearch_result.html", context)


def index(request: HttpRequest):
    return render(request, "teacher/index.html", {})


def space(request: HttpRequest):
    is_login = request.COOKIES["is_login"]
    account = request.COOKIES["account"]
    tea = Teacher.objects.filter(tea_id=account).first()
    return render(request, "teacher/space.html", {"tea": tea})


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
        "level"  : level
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
            stu_list = Student.objects.filter(Q(campus=campus) & Q(detail=only_see))
            room_list = []
            room_id_list = []
            for stu_item in stu_list:
                room_list.append(stu_item.room)
                room_id_list.append(stu_item.room.id)
            result = InspectionHistory.objects.filter(
                Q(date__gte=start_time) & Q(date__lte=end_time) & Q(room_id__in=room_id_list))
            result = list(result)
        else:  # 不对进行detail筛选
            stu_list = Student.objects.filter(Q(campus=campus))
            room_list = []
            room_id_list = []
            for stu_item in stu_list:
                room_list.append(stu_item.room)
                room_id_list.append(stu_item.room.id)
            result = InspectionHistory.objects.filter(
                Q(date__gte=start_time) & Q(date__lte=end_time) & Q(room_id__in=room_id_list))
            result = list(result)
    else:  # 不对学院进行筛选
        room_list = Room.objects.all()
        room_id_list = []
        for room_item in room_list:
            room_id_list.append(room_item.id)
        print("2020-01-01" <= "2020")
        result = InspectionHistory.objects.filter(
            Q(date__gte=start_time) & Q(date__lte=end_time) & Q(room_id__in=room_id_list))
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
    tea = Teacher.objects.filter(Q(tea_id=tea_id) & Q(name=name)).first()
    tea.name = name
    tea.tel = tel
    tea.save()
    if len(pwd) > 0:  # 提供了新密码
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


# form view

def form_add_inspection_history(request: HttpRequest):
    data = request.POST.dict()
    print("form_data->", data)
    build = data["build"]
    door_id = data["door_id"]
    singleRoom_id = data["singleRoom_id"]
    room_id = data["room_id"]
    result = data["result"]
    commment = data["comment"]
    ih = InspectionHistory()
    room = Room.objects.filter(
        Q(build=build) & Q(door_id=door_id) & Q(singleRoom_id=singleRoom_id) & Q(room_id=room_id)).first()
    try:
        ih.room_id = room.id
    except AttributeError:
        print_exc()
        return render(request, "teacher/components/add_inspection_history.html", {"status": "room_not_found"})
    ih.comment = commment
    ih.result = result
    ih.save()
    return render(request, "teacher/components/add_inspection_history.html", {"status": "ok"})


def file_add_inspection_history(request: HttpRequest):
    return render(request, "teacher/components/add_inspection_history.html", {})


def form_inspection_warnings(request: HttpRequest):
    data = request.POST.dict()
    print(data)
    print(request.COOKIES)

    account = request.COOKIES["account"]

    build = data["build"]
    door_id = data["door_id"]
    singleRoom_id = data["singleRoom_id"]
    room_id = data["room_id"]
    warning = data["warning"]
    comment = data["comment"]
    room = Room.objects.filter(Q(build=build) &
                               Q(door_id=door_id) &
                               Q(singleRoom_id=singleRoom_id) &
                               Q(room_id=room_id)).first()
    w = Warning()
    try:
        w.room_id = room.id
        w.comment = comment
        w.level = warning
        w.sponsor = account
        w.save()
    except AttributeError:
        print_exc()
        return render(request, "teacher/components/inspection_warning.html", {"status": "room_not_found"})
    return render(request, "teacher/components/inspection_warning.html", {"status": "ok"})


def form_del_dorm_information(request: HttpRequest):
    data = request.POST.dict()
    print(data)
    id = data["id"]
    stu = Student.objects.filter(Q(stu_id=id)).first()
    try:
        stu.room.capacity -= 1
        stu.room.save()
        stu.room_id = ""
        stu.save()
    except AttributeError:
        print_exc()
        return render(request, "teacher/components/del_dorm_information.html", {"status": "stu_not_found"})

    return render(request, "teacher/components/del_dorm_information.html", {"status": "ok"})


def file_del_dorm_information(request: HttpRequest):
    return render(request, "teacher/components/del_dorm_information.html", {})


def form_manage_bed(request: HttpRequest):
    data = request.POST.dict()
    cookie = request.COOKIES
    print(data)
    print(cookie)
    stu_id = data["stu_id"]
    build = data["build"]
    door_id = data["door_id"]
    singleRoom_id = data["singleRoom_id"]
    room_id = data["room_id"]

    stu = Student.objects.filter(Q(stu_id=stu_id)).first()
    try:
        stu_room = stu.room
    except AttributeError:
        print_exc()
        return render(request, "teacher/components/manage_bed.html", {"status": "stu_not_found"})

    try:
        dst_room = Room.objects.filter(
            Q(build=build) & Q(door_id=door_id) & Q(singleRoom_id=singleRoom_id) & Q(room_id=room_id)).first()
        print("房间id:", dst_room.id)
        stu.room = dst_room
        stu.save()
    except AttributeError:
        print_exc()
        return render(request, "teacher/components/manage_bed.html", {"status": "room_not_found"})

    return render(request, "teacher/components/manage_bed.html", {"status": "ok"})


def file_manage_bed(request: HttpRequest):
    return render(request, "teacher/components/manage_bed.html", {})


def form_delete_account(request: HttpRequest):
    data = request.POST.dict()
    cookie = request.COOKIES
    print(data)
    print(cookie)
    stu = Student.objects.filter(Q(stu_id=id)).first()
    tea = Teacher.objects.filter(Q(tea_id=id)).first()
    if stu:  # 删除学生信息和账号
        StuAccount.objects.filter(Q(account_name=stu.stu_id)).delete()
        stu.delete()
    elif tea:
        ManagerAccount.objects.filter(Q(account_name=tea.tea_id)).delete()
        tea.delete()
    else:
        return render(request, "teacher/components/accountmanage/delete_account.html", {"status": "id_not_found"})
    return render(request, "teacher/components/accountmanage/delete_account.html", {"status": "ok"})


def form_import_first_level_manage_account(request: HttpRequest):
    data = request.POST.dict()
    cookie = request.COOKIES
    print(data)
    print(cookie)
    id = data["id"]
    college = data["college"]
    if college == "...": campus = ""
    name = data["name"]
    try:
        teacher = Teacher.objects.filter(Q(tea_id=id)).first()
        if teacher:
            return render(request, "teacher/components/accountmanage/import_first_level_manage_account.html",
                          {"status": "id_exist"})
        teacher = Teacher()
        teacher.tea_id = id
        teacher.college = college
        teacher.name = name
        account = ManagerAccount()
        account.account_name = id
        account.pwd = "123456"
        account.level = '0'
        teacher.save()
        account.save()
    except:
        print_exc()
        pass
    return render(request, "teacher/components/accountmanage/import_first_level_manage_account.html", {"status": "ok"})


def form_import_second_level_manage_account(request: HttpRequest):
    data = request.POST.dict()
    cookie = request.COOKIES
    print(data)
    print(cookie)
    id = data["id"]
    college = data["college"]
    if college == "...": college = ""
    name = data["name"]
    try:
        teacher = Teacher.objects.filter(Q(tea_id=id)).first()
        if teacher:
            return render(request, "teacher/components/accountmanage/import_first_level_manage_account.html",
                          {"status": "id_exist"})
        teacher = Teacher()
        teacher.tea_id = id
        teacher.college = college
        teacher.name = name
        account = ManagerAccount()
        account.account_name = id
        account.pwd = "123456"
        account.level = '0'
        teacher.save()
        account.save()
    except:
        print_exc()
        pass
    return render(request, "teacher/components/accountmanage/import_second_level_manage_account.html", {"status": "ok"})


def form_import_student_account(request: HttpRequest):
    data = request.POST.dict()
    cookie = request.COOKIES
    print(data)
    print(cookie)
    level = cookie["level"]

    id = data["id"]
    college = data["college"]
    if college == "...": college = ""
    name = data["name"]
    try:
        student = Student.objects.filter(Q(stu_id=id)).first()
        if student:
            return render(request, "teacher/components/accountmanage/import_student_account.html",
                          {"status": "id_exist"})
        student = Student()
        student.stu_id = id
        student.college = college
        student.name = name
        account = StuAccount()
        account.account_name = id
        account.pwd = "123456"
        student.save()
        account.save()
    except:
        print_exc()
        pass
    return render(request, "teacher/components/accountmanage/import_student_account.html", {})


def form_reset_account(request: HttpRequest):
    data = request.POST.dict()
    cookie = request.COOKIES
    print(data)
    print(cookie)
    level = cookie["level"]
    if level == "1":
        return render(request, "teacher/components/accountmanage/reset_account.html", {})
    id = data["id"]
    not_found = 0
    try:
        ManagerAccount.objects.filter(Q(account_name=id)).update(pwd="123456")
    except :
        not_found += 1
    try:
        StuAccount.objects.filter(account_name=id).update(pwd="123456")
    except :
        not_found += 1

    print("not_found:" , not_found)
    if not_found == 2:
        return render(request, "teacher/components/accountmanage/reset_account.html", {"status": "id_not_found"})
    return render(request, "teacher/components/accountmanage/reset_account.html", {"status": "ok"})


def file_delete_account(request: HttpRequest):
    return render(request, "teacher/components/accountmanage/delete_account.html", {})


def file_import_first_level_manage_account(request: HttpRequest):
    return render(request, "teacher/components/accountmanage/import_first_level_manage_account.html", {})


def file_import_second_level_manage_account(request: HttpRequest):
    return render(request, "teacher/components/accountmanage/import_second_level_manage_account.html", {})


def file_import_student_account(request: HttpRequest):
    return render(request, "teacher/components/accountmanage/import_student_account.html", {})


def file_reset_account(request: HttpRequest):
    return render(request, "teacher/components/accountmanage/reset_account.html", {})
