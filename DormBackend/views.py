from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


# Create your views here.
def index(request: HttpRequest):
    return render(request, "index.html", {})


def db_config(request: HttpRequest):
    return render(request, "db_config.html", {})


