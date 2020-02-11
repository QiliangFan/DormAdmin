from django.conf.urls import url

from teacher.views import *

urlpatterns = [
    url(r'^index$', index)
    , url(r'^space$', space)
    , url(r'^dormmanage$', dormmanage)
    , url(r'^targetsearch$', targetsearch)
    , url(r'^inspection_history$', inspection_history)
    , url(r'^inspection_history_search$', inspection_history_search)
    , url(r'^inspection_warning$', inspection_warning)
    , url(r"^add_inspection_history$", add_inspection_history)
    , url(r"^manage_bed$", manage_bed)
    , url(r'^del_dorm_information$', del_dorm_information)
    , url(r'^modify_self_information$', modify_self_information)
    , url(r'^accountmanage$', accountmanage)
    , url(r'^delete_account$', delete_account)
    , url(r'^import_first_level_manage_account$', import_first_level_manage_account)
    , url(r'^import_second_level_manage_account$', import_second_level_manage_account)
    , url(r'^import_student_account$', import_student_account)
    , url(r'^reset_account$', reset_account)

    # 表单路由
    , url(r"^form_add_inspection_history$", form_add_inspection_history)
    , url(r"^file_add_inspection_history$", file_add_inspection_history)
    , url(r"^form_inspection_warning$", form_inspection_warnings)
    , url(r"^form_del_dorm_information$", form_del_dorm_information)
    , url(r"^file_del_dorm_information$", file_del_dorm_information)
    , url(r"^form_manage_bed$", form_manage_bed)
    , url(r"^file_manage_bed$", file_manage_bed)
    , url(r'^form_delete_account$', form_delete_account)
    , url(r'^file_delete_account$', file_delete_account)
    , url(r'^form_import_first_level_manage_account$', form_import_first_level_manage_account)
    , url(r"^file_import_first_level_manage_account$", file_import_first_level_manage_account)
    , url(r'^form_import_second_level_manage_account$', form_import_second_level_manage_account)
    , url(r'^file_import_second_level_manage_account$', file_import_second_level_manage_account)
    , url(r'^form_import_student_account$', form_import_student_account)
    , url(r'^file_import_student_account$', file_import_student_account)
    , url(r'^form_reset_account$', form_reset_account)
    , url(r'^file_reset_account$', file_reset_account)

]
