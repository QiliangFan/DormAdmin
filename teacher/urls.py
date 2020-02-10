from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from teacher.views import *

urlpatterns = [
    url(r'index$', index)
    ,url(r'space$', space)
    ,url(r'dormmanage$', dormmanage)
    ,url(r'targetsearch$', targetsearch)
    ,url(r'inspection_history$', inspection_history)
    ,url(r'inspection_history_search$', inspection_history_search)
    ,url(r'inspection_warning$', inspection_warning)
    ,url(r"add_inspection_history$", add_inspection_history)
    ,url(r"manage_bed$", manage_bed)
]