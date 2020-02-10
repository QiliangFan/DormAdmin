from django.db import models

# Create your models here.
from django.db.models import Model


class Student(models.Model):
    stu_id = models.CharField(max_length=32, null=True, default="")
    emergence_tel = models.CharField(max_length=16, null=True, default="")
    tel = models.CharField(max_length=16, null=True, default="")
    tutor = models.ForeignKey("Teacher", on_delete=models.SET_NULL, null=True)
    college = models.CharField(max_length=32, null=True, default="")  # 学院
    major = models.CharField(max_length=32, null=True, default="")  # 专业
    room = models.ForeignKey("Room", on_delete=models.SET_NULL, null=True)


class Teacher(models.Model):
    tea_id = models.CharField(max_length=32, null=True, default="")
    name = models.CharField(max_length=16, null=True, default="")
    college = models.CharField(max_length=32, null=True, default="")
    tel = models.CharField(max_length=16, null=True, default="")


class Room(models.Model):
    room_id = models.CharField(max_length=32, null=True, default="")
    build = models.CharField(max_length=32, null=True, default="")
    result = models.CharField(max_length=32, null=True, default="")  # 检查结果
    comment = models.CharField(max_length=32, null=True, default="")  # 备注
    capacity = models.IntegerField(default=0)

class Account(models.Model):
    account_name = models.ForeignKey("Teacher", on_delete=models.CASCADE)
    pwd = models.CharField(max_length=32, default="123456")
    level = models.IntegerField( default="1")