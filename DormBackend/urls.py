from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from DormBackend.views import *
from student import views as sv

urlpatterns = [
    url(r'^index$', index),
    url(r'^db_config$', db_config),
    url(r'^config$', config),
    url(r'^student_info$', sv.student_info),
    url(r'^change_stu_info$', sv.change_stu_info),
    url(r'^mate_info$', sv.mate_info),
    url(r'^clean_info$', sv.clean_info),
]