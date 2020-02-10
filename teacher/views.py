from django.http import HttpRequest
from django.shortcuts import render


def index(request: HttpRequest):
    return render(request, "teacher/index.html", {})


def space(request: HttpRequest):
    return render(request, "teacher/space.html", {})


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