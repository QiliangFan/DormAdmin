from django.db import models

# Create your models here.
from django.db.models import Model


class Student(models.Model):
    stu_id = models.CharField(max_length=32, null=True, default="")
    emergence_tel = models.CharField(max_length=16, null=True, default="")
    tel = models.CharField(max_length=16, null=True, default="")
    tutor = models.ForeignKey("Teacher", on_delete=models.SET_NULL, null=True)
    college = models.CharField(max_length=32, null=True, default="")  # 学院
    detail = models.CharField(max_length=32, null=True, default="")  # 具体信息
    room = models.ForeignKey("Room", on_delete=models.SET_NULL, null=True)
    home_address = models.TextField(null=True, default="")
    name = models.CharField(max_length=32, null=True, default="")


class Teacher(models.Model):
    tea_id = models.CharField(max_length=32, null=True, default="")
    name = models.CharField(max_length=16, null=True, default="")
    college = models.CharField(max_length=32, null=True, default="")
    tel = models.CharField(max_length=16, null=True, default="")


class Room(models.Model):
    room_id = models.CharField(max_length=32, null=True, default="")
    build = models.CharField(max_length=32, null=True, default="")
    door_id = models.CharField(max_length=32, null=True,default="")
    singleRoom_id = models.CharField(max_length=32, null=True,default="")
    capacity = models.IntegerField(default=0)   # 实际已住


class ManagerAccount(models.Model):
    account_name = models.ForeignKey("Teacher", on_delete=models.CASCADE)
    pwd = models.CharField(max_length=32, default="123456")
    level = models.IntegerField( default="1")


class StuAccount(models.Model):
    account_name = models.ForeignKey("Student", on_delete=models.CASCADE)
    pwd = models.CharField(max_length=32, default="123456")


class InspectionHistory(models.Model):
    year = models.IntegerField(default=2020)
    month = models.IntegerField(default=1)
    day = models.IntegerField(default=1)
    date = models.DateTimeField(auto_now=True)
    room = models.ForeignKey("Room", on_delete=models.CASCADE)
    result = models.CharField(max_length=32, null=True, default="")  # 检查结果
    comment = models.CharField(max_length=32, null=True, default="")  # 备注


class Warning(models.Model):
    sponsor = models.ForeignKey("Teacher", on_delete=models.SET_NULL, null=True)
    room = models.ForeignKey("Room", on_delete=models.CASCADE, null=True)
    level = models.CharField(max_length=32, null=True, default="")
    comment = models.CharField(max_length=512, null=True, default="")