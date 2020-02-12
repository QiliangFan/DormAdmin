import json
import sys
import traceback

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, JsonResponse

# Create your views here.

from DormBackend.models import Student, StuAccount, Teacher, ManagerAccount
from PROPATH import PROJECT
from logs.log import Log


def index(request: HttpRequest):
    return render(request, "index.html", {})


def login(request: HttpRequest):
    data = request.POST.dict()
    print(data)
    account = data["account"]
    password = data["password"]
    user_type = data["type"]
    Log.i(__name__, account + "尝试登录...")
    try:
        if user_type == "student":       # 学生登录
            stu = Student.objects.filter(stu_id=account).first()
            _account = StuAccount.objects.filter(account_name_id=stu.id).first()
            _pwd = _account.pwd
            if _pwd == password:    # 密码正确
                obj = redirect("/stu_index")
                obj.set_cookie("account", account)
                obj.set_cookie("is_login", True)
                return obj

        else:                       # 教师登录
            tea = Teacher.objects.filter(tea_id=account).first()
            _account = ManagerAccount.objects.filter(account_name_id=tea.id).first()
            _pwd = _account.pwd
            if _pwd == password:
                obj = redirect("/teacher/index")
                obj.set_cookie("account", account)
                obj.set_cookie("is_login", True)
                obj.set_cookie("level", _account.level)
                return obj
    except Exception:
        traceback.print_exc()
        Log.i(__name__, account + "账号错误, 登录失败...")
        return render(request, "index.html", {"status": "account_error"})
    finally:
        Log.i(__name__, account + "密码错误, 登录失败...")
    return render(request, "index.html", {"status": "password_error"})


def logout(request: HttpRequest):
    obj = redirect("/index")
    obj.set_cookie("is_login", "false")
    return obj


def server_error(request: HttpRequest):
    return JsonResponse({
        "status": "后台出现错误",
        "advice": "重新启动程序"
    })