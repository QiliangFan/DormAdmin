from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from DormBackend.views import *
from student import views as sv
from teacher import urls as tea_url

urlpatterns = [
    url(r'^index$', index)
    , url(r'^student_info$', sv.student_info)
    , url(r'^change_stu_info$', sv.change_stu_info)
    , url(r'^mate_info$', sv.mate_info)
    , url(r'^clean_info$', sv.clean_info)
    , url(r"^stu_index$", sv.stu_index)
    , url(r'^login$', login)
    , url(r'^logout$', logout)
    , url(r"^teacher/", include(tea_url))
    , url(r'^warn_info$', sv.warn_info)
]
