import json
import sys

from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


# Create your views here.
from PROPATH import PROJECT
from logs.log import Log


def index(request: HttpRequest):
    return render(request, "index.html", {})


def db_config(request: HttpRequest):
    with open(PROJECT + "config/db.json", "r") as fp:
        data = json.load(fp=fp)
    return render(request, "db_config.html", data)


def config(request: HttpRequest):
    Log.w(__name__, "数据库配置完成, 关闭应用.")
    data = request.POST.dict()
    with open(PROJECT + "config/db.json", "w") as fp:
        json.dump(data, fp=fp, indent=4, ensure_ascii=False)
    return render(request, "restart.html", {})