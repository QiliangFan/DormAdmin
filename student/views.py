from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpRequest
from DormBackend import models
from rest_framework.decorators import api_view
import traceback


# 获取用户个人信息
def student_info(request: HttpRequest):
    stu = models.Student.objects.get(stu_id='1712982')
    context = {"stu": stu, "info_fun_name": 'student_info'}
    return render(request, "StudentFronted/space.html", context)


# 修改用户个人信息
@api_view(["POST"])
def change_stu_info(request: HttpRequest):
    request.encoding = 'utf-8'
    try:
        print(request.POST)
        stu_id = request.POST["stu_id"]
        stu = models.Student.objects.get(stu_id=stu_id)
        stu.tel = request.POST["tel"]
        stu.emergence_tel = request.POST["emergence_tel"]
        stu.home_address = request.POST["home_address"]
        stu.save()
        context = {"stu": stu, "info_fun_name": 'student_info', "status": 'ok'}
        return render(request, "StudentFronted/space.html", context)
    except Exception as e:
        traceback.print_exc()
        return JsonResponse({
            "status": "error"
        })


# 获取用户舍友信息
def mate_info(request: HttpRequest):
    stu = models.Student.objects.get(stu_id='1712982')
    room = stu.room
    mate = models.Student.objects.filter(room=room)
    context = {"mate": mate, "status": 'ok'}
    return render(request, "StudentFronted/roommate.html", context)


# 获取宿舍卫生情况
def clean_info(request: HttpRequest):
    stu = models.Student.objects.get(stu_id='1712982')
    room = stu.room
    clean = models.InspectionHistory.objects.filter(room=room)
    context = {"clean": clean, "status": 'ok'}
    return render(request, "StudentFronted/clean.html", context)

