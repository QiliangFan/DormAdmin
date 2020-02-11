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
    ,url(r'del_dorm_information$', del_dorm_information)
    ,url(r'modify_self_information$', modify_self_information)
    ,url(r'accountmanage$', accountmanage)
    ,url(r'delete_account$', delete_account)
    ,url(r'import_first_level_manage_account$', import_first_level_manage_account)
    ,url(r'import_second_level_manage_account$', import_second_level_manage_account)
    ,url(r'import_student_account$', import_student_account)
    ,url(r'reset_account$', reset_account)
]