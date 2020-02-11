from django.db.models import Q
from django.http import HttpRequest
from django.shortcuts import render

from DormBackend.models import Teacher, ManagerAccount


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
    return render(request, "teacher/components/inspection_history.html", {})


def inspection_history_search(request: HttpRequest):
    print(request.GET.dict())
    return render(request, "teacher/table/inspection_history_table.html", {})


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