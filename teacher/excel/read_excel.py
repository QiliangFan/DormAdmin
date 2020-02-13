from traceback import print_exc

import xlrd
from django.db.models import Q
from xlrd.sheet import Cell, Sheet

from DormBackend.models import Student, StuAccount, Room, Teacher, ManagerAccount, InspectionHistory
from .parse_ceil import *


def read_excel_student(filename):
    print(filename)
    wb = xlrd.open_workbook(filename)
    for ws in wb.sheets():
        stu_id_list = []
        stu_name_list = []
        room_list = []
        college_list = []

        print(ws.ncols)
        for c in range(ws.ncols):
            col_list:list = ws.col(c)

            try:
                while col_list[0].value == "":
                    col_list.pop(0)
                if str(col_list[0].value).strip("").startswith("学号"):
                    stu_id_list = [str(item.value).replace(".0", "") for item in col_list[1:]]
                elif str(col_list[0].value).strip().startswith("姓名"):
                    stu_name_list = [item.value for item in col_list[1:]]
                elif len(room_list)==0 and str(col_list[0].value).strip().startswith("宿舍"):
                    room_list = [str(item.value).replace(".0", "") for item in col_list[1:]]
                elif str(col_list[0].value).strip().startswith("学院"):
                    college_list = [item.value for item in col_list[1:]]
            except :
                print_exc()
                continue

        print("stu_id_list:", len(stu_id_list))
        print("stu_name_list:", len(stu_name_list))
        print("room_list:", len(room_list))
        print("college_list:", len(college_list))

        last_room = ""
        for i in range(max(len(stu_id_list), len(stu_name_list), len(room_list), len(college_list))):
            try:
                stu_id = stu_id_list[i].strip()
                stu_name = stu_name_list[i].strip()
                room = room_list[i].strip()
                print(stu_id, stu_name, room)

                if len(stu_id) == 0:
                    continue            # 跳过为空的学号
                if len(room) == 0:  # 跳过没有宿舍的
                    room = last_room
                elif not room[0].isdigit():       # 跳过宿舍不在校内的
                    continue
                elif room.count("-") == 2:
                    continue                    # 跳过单间号不准确的
                last_room = room
                if len(college_list) == 0:
                    college = "软件学院"
                    detail = "本科生"
                else:
                    college, detail = parse_college(college_list[i].strip())

                build, door_id, room_id, singleRoom_id = parse_dorm(room)

                if Student.objects.filter(Q(stu_id=stu_id)):
                    student = Student.objects.filter(stu_id=stu_id).first()
                    account = StuAccount.objects.filter(account_name=student).first()
                else:
                    student = Student()
                    account = StuAccount()
                room = Room.objects.filter(Q(build=build)&
                                           Q(door_id=door_id)&
                                           Q(room_id=room_id)&
                                           Q(singleRoom_id=singleRoom_id)).first()


                student.room = room
                room.capacity += 1
                student.stu_id = stu_id
                student.name = stu_name
                student.college = college
                student.detail = detail
                student.save()

                account.account_name = student
                account.pwd = "123456"
                room.save()
                account.save()
            except :
                print_exc()
                continue


def read_excel_student_del(filename):
    print(filename)
    wb = xlrd.open_workbook(filename)
    for ws in wb.sheets():
        stu_id_list = []
        stu_name_list = []
        room_list = []
        college_list = []

        print(ws.ncols)
        for c in range(ws.ncols):
            col_list: list = ws.col(c)

            try:
                while col_list[0].value == "":
                    col_list.pop(0)
                if col_list[0].value.startswith("学号"):
                    stu_id_list = [str(item.value).replace(".0", "") for item in col_list[1:]]
                elif col_list[0].value.startswith("姓名"):
                    stu_name_list = [item.value for item in col_list[1:]]
                elif len(room_list) == 0 and col_list[0].value.startswith("宿舍"):
                    room_list = [str(item.value).replace(".0", "") for item in col_list[1:]]
                elif col_list[0].value.startswith("学院"):
                    college_list = [item.value for item in col_list[1:]]
            except:
                continue

        print("stu_id_list:", len(stu_id_list))
        print("stu_name_list:", len(stu_name_list))
        print("room_list:", len(room_list))
        print("college_list:", len(college_list))

        lastroom = ""
        for i in range(max(len(stu_id_list), len(stu_name_list), len(room_list), len(college_list))):
            try:
                stu_id = stu_id_list[i].strip()
                stu_name = stu_name_list[i].strip()
                room = room_list[i].strip()

                if len(stu_id) == 0:
                    continue  # 跳过为空的学号
                if len(room) == 0:  # 跳过没有宿舍的
                    room = lastroom
                elif not room[0].isnumeric():  # 跳过宿舍不在校内的
                    continue
                elif room.count("-") == 2:
                    continue                    # 跳过单间号不准确的

                lastroom = room
                if len(college_list) == 0:
                    college = "软件学院"
                    detail = ""
                else:

                    college, detail = parse_college(college_list[i].strip())

                build, door_id, room_id, singleRoom_id = parse_dorm(room)

                if Student.objects.filter(Q(stu_id=stu_id)).first():
                    student = Student.objects.filter(stu_id=stu_id).first()
                    account = StuAccount.objects.filter(account_name=student)
                else:
                    continue
                room = Room.objects.filter(Q(build=build) &
                                           Q(door_id=door_id) &
                                           Q(room_id=room_id) &
                                           Q(singleRoom_id=singleRoom_id)).first()

                student.room = room
                room.capacity -= 1
                student.stu_id = stu_id
                student.name = stu_name
                student.college = college
                student.detail = detail
                student.delete()

                account.account_name = student
                account.pwd = "123456"
                room.save()
                account.delete()
            except:
                continue


def read_excel_student_reset(filename:str):
    print(filename)
    wb = xlrd.open_workbook(filename)
    for ws in wb.sheets():
        stu_id_list = []
        stu_name_list = []
        room_list = []
        college_list = []

        print(ws.ncols)
        for c in range(ws.ncols):
            col_list: list = ws.col(c)

            try:
                while col_list[0].value == "":
                    col_list.pop(0)
                if col_list[0].value.startswith("学号"):
                    stu_id_list = [str(item.value).replace(".0", "") for item in col_list[1:]]
                elif col_list[0].value.startswith("姓名"):
                    stu_name_list = [item.value for item in col_list[1:]]
                elif len(room_list) == 0 and col_list[0].value.startswith("宿舍"):
                    room_list = [str(item.value).replace(".0", "") for item in col_list[1:]]
                elif col_list[0].value.startswith("学院"):
                    college_list = [item.value for item in col_list[1:]]
            except:
                continue

        print("stu_id_list:", len(stu_id_list))
        print("stu_name_list:", len(stu_name_list))
        print("room_list:", len(room_list))
        print("college_list:", len(college_list))

        lastroom = ""
        for i in range(max(len(stu_id_list), len(stu_name_list), len(room_list), len(college_list))):
            try:
                stu_id = stu_id_list[i].strip()
                stu_name = stu_name_list[i].strip()
                room = room_list[i].strip()

                if len(stu_id) == 0:
                    continue  # 跳过为空的学号
                if len(room) == 0:  # 跳过没有宿舍的
                    room = lastroom
                elif not room[0].isnumeric():  # 跳过宿舍不在校内的
                    continue
                elif room.count("-") == 2:
                    continue                    # 跳过单间号不准确的

                lastroom = room
                if Student.objects.filter(Q(stu_id=stu_id)).first():
                    student = Student.objects.filter(stu_id=stu_id).first()
                    account = StuAccount.objects.filter(account_name=student).first()
                else:
                    continue
                account.pwd = "123456"
                account.save()
            except:
                continue


def read_excel_teacher(filename:str, level:str):
    print(filename)
    wb = xlrd.open_workbook(filename)
    for ws in wb.sheets():
        tea_id_list = []
        tea_name_list = []
        tel_list = []
        college_list = []

        print(ws.ncols)
        for c in range(ws.ncols):
            col_list: list = ws.col(c)
            print(col_list)

            try:
                while col_list[0].value == "":
                    col_list.pop(0)
                if col_list[0].value.startswith("教工号"):
                    tea_id_list = [str(item.value).replace(".0", "") for item in col_list[1:]]
                elif col_list[0].value.startswith("姓名"):
                    tea_name_list = [item.value for item in col_list[1:]]
                elif col_list[0].value.startswith("学院"):
                    college_list = [str(item.value).replace(".0", "") for item in col_list[1:]]
                elif col_list[0].value.startswith("电话"):
                    tel_list = [item.value for item in col_list[1:]]
            except:
                print_exc()
                continue

        print("tea_id_list:", len(tea_id_list))
        print("tea_name_list:", len(tea_name_list))
        print("tel_list:", len(tel_list))
        print("college_list:", len(college_list))

        for i in range(max(len(tea_id_list), len(tea_name_list), len(tel_list), len(college_list))):
            try:
                tea_id = tea_id_list[i].strip()
                tea_name = tea_name_list[i].strip()
                college = college_list[i].strip()

                if len(tea_id) == 0:
                    continue  # 跳过为空的学号
                if len(college) == 0:  # 跳过没有学院的
                    continue
                if len(tel_list) == 0:
                    tel = ""
                else:
                    tel = tel_list[i]

                if Teacher.objects.filter(Q(tea_id=tea_id)).first():
                    continue
                else:
                    teacher = Teacher()
                    account = ManagerAccount()


                teacher.tea_id = tea_id
                teacher.name = tea_name
                teacher.college = college
                teacher.tel = tel
                teacher.save()

                account.account_name = teacher
                account.pwd = "123456"
                account.level = level
                account.save()
            except:
                print_exc()
                continue


def read_excel_teacher_delete(filename:str):
    print(filename)
    wb = xlrd.open_workbook(filename)
    for ws in wb.sheets():
        tea_id_list = []
        tea_name_list = []
        tel_list = []
        college_list = []

        print(ws.ncols)
        for c in range(ws.ncols):
            col_list: list = ws.col(c)

            try:
                while col_list[0].value == "":
                    col_list.pop(0)
                if col_list[0].value.startswith("教工号"):
                    tea_id_list = [str(item.value).replace(".0", "") for item in col_list[1:]]
                elif col_list[0].value.startswith("姓名"):
                    tea_name_list = [item.value for item in col_list[1:]]
                elif col_list[0].value.startswith("学院"):
                    college_list = [str(item.value).replace(".0", "") for item in col_list[1:]]
                elif col_list[0].value.startswith("电话"):
                    tel_list = [item.value for item in col_list[1:]]
            except:
                continue

        print("tea_id_list:", len(tea_id_list))
        print("tea_name_list:", len(tea_name_list))
        print("tel_list:", len(tel_list))
        print("college_list:", len(college_list))

        for i in range(max(len(tea_id_list), len(tea_name_list), len(tel_list), len(college_list))):
            try:
                tea_id = tea_id_list[i].strip()
                tea_name = tea_name_list[i].strip()
                college = college_list[i].strip()

                if len(tea_id) == 0:
                    continue  # 跳过为空的学号
                if len(college) == 0:  # 跳过没有学院的
                    continue
                if len(tel_list) == 0:
                    tel = ""
                else:
                    tel = tel_list[i]

                if Teacher.objects.filter(Q(tea_id=tea_id)).first():
                    teacher = Teacher.objects.filter(tea_id = tea_id).first()
                else:
                    continue

                account = ManagerAccount.objects.filter(account_name=teacher).delete()
                teacher.delete()
            except:
                continue


def read_excel_teacher_reset(filename:str):
    print(filename)
    wb = xlrd.open_workbook(filename)
    for ws in wb.sheets():
        tea_id_list = []
        tea_name_list = []
        tel_list = []
        college_list = []

        print(ws.ncols)
        for c in range(ws.ncols):
            col_list: list = ws.col(c)

            try:
                while col_list[0].value == "":
                    col_list.pop(0)
                if col_list[0].value.startswith("教工号"):
                    tea_id_list = [str(item.value).replace(".0", "") for item in col_list[1:]]
                elif col_list[0].value.startswith("姓名"):
                    tea_name_list = [item.value for item in col_list[1:]]
                elif col_list[0].value.startswith("学院"):
                    college_list = [str(item.value).replace(".0", "") for item in col_list[1:]]
                elif col_list[0].value.startswith("电话"):
                    tel_list = [item.value for item in col_list[1:]]
            except:
                continue

        print("tea_id_list:", len(tea_id_list))
        print("tea_name_list:", len(tea_name_list))
        print("tel_list:", len(tel_list))
        print("college_list:", len(college_list))

        for i in range(max(len(tea_id_list), len(tea_name_list), len(tel_list), len(college_list))):
            try:
                tea_id = tea_id_list[i].strip()
                tea_name = tea_name_list[i].strip()
                college = college_list[i].strip()

                if len(tea_id) == 0:
                    continue  # 跳过为空的学号
                if len(college) == 0:  # 跳过没有学院的
                    continue
                if len(tel_list) == 0:
                    tel = ""
                else:
                    tel = tel_list[i]

                if Teacher.objects.filter(Q(tea_id=tea_id)).first():
                    teacher = Teacher.objects.filter(tea_id = tea_id).first()
                else:
                    continue

                account = ManagerAccount.objects.filter(account_name=teacher).first()
                account.pwd = "123456"
                account.save()
            except:
                print_exc()
                continue


def read_excel_add_inspection(filename:str):
    print(filename)
    wb = xlrd.open_workbook(filename)
    for ws in wb.sheets():
        room_list = []
        result_list = []
        comment_list = []

        print(ws.ncols)
        for c in range(ws.ncols):
            col_list: list = ws.col(c)

            try:
                while col_list[0].value == "":
                    col_list.pop(0)
                if str(col_list[0].value).strip("").startswith("宿舍"):
                    room_list = [str(item.value).replace(".0", "") for item in col_list[1:]]
                elif str(col_list[0].value).strip().startswith("结果"):
                    result_list = [item.value for item in col_list[1:]]
                elif str(col_list[0].value).strip().startswith("备注"):
                    comment_list = [item.value for item in col_list[1:]]
            except:
                print_exc()
                continue
        for i in range(max(len(room_list), len(result_list), len(comment_list))):
            try:
                result = result_list[i].strip()
                comment = comment_list[i].strip()
                room = room_list[i].strip()

                build, door_id, room_id, singleRoom_id = parse_dorm(room)

                if Room.objects.filter(Q(build=build)&Q(door_id=door_id)&Q(room_id=room_id)&Q(singleRoom_id=singleRoom_id)).first():
                    room = Room.objects.filter(Q(build=build) & Q(door_id=door_id) & Q(room_id=room_id) & Q(singleRoom_id=singleRoom_id)).first()
                else:
                    continue
                inspection = InspectionHistory()

                inspection.room = room
                inspection.result = result
                inspection.comment = comment
                inspection.save()
            except:
                print_exc()
                continue


def read_excel_manage_bed(filename:str):
    print(filename)
    wb = xlrd.open_workbook(filename)
    for ws in wb.sheets():
        stu_id_list = []
        stu_name_list = []
        room_list = []
        college_list = []

        print(ws.ncols)
        for c in range(ws.ncols):
            col_list: list = ws.col(c)

            try:
                while col_list[0].value == "":
                    col_list.pop(0)
                if str(col_list[0].value).strip("").startswith("学号"):
                    stu_id_list = [str(item.value).replace(".0", "") for item in col_list[1:]]
                elif str(col_list[0].value).strip().startswith("姓名"):
                    stu_name_list = [item.value for item in col_list[1:]]
                elif len(room_list) == 0 and str(col_list[0].value).strip().startswith("宿舍"):
                    room_list = [str(item.value).replace(".0", "") for item in col_list[1:]]
                elif str(col_list[0].value).strip().startswith("学院"):
                    college_list = [item.value for item in col_list[1:]]
            except:
                print_exc()
                continue

        print("stu_id_list:", len(stu_id_list))
        print("stu_name_list:", len(stu_name_list))
        print("room_list:", len(room_list))
        print("college_list:", len(college_list))

        for i in range(max(len(stu_id_list), len(stu_name_list), len(room_list), len(college_list))):
            try:
                stu_id = stu_id_list[i].strip()
                stu_name = stu_name_list[i].strip()
                room = room_list[i].strip()

                if len(stu_id) == 0:
                    continue  # 跳过为空的学号
                if len(room) == 0:  # 跳过没有宿舍的
                    continue
                elif not room[0].isdigit():  # 跳过宿舍不在校内的
                    continue
                elif room.count("-") == 2:
                    continue  # 跳过单间号不准确的

                if len(college_list) == 0:
                    college = "软件学院"
                    detail = "本科生"
                else:
                    college, detail = parse_college(college_list[i].strip())

                build, door_id, room_id, singleRoom_id = parse_dorm(room)

                if Student.objects.filter(Q(stu_id=stu_id)):
                    student = Student.objects.filter(stu_id=stu_id).first()
                    account = StuAccount.objects.filter(account_name=student).first()
                else:
                    continue
                room = Room.objects.filter(Q(build=build) &
                                           Q(door_id=door_id) &
                                           Q(room_id=room_id) &
                                           Q(singleRoom_id=singleRoom_id)).first()

                if student.room:
                    student.room.capacity -= 1
                    student.room.save()

                student.room = room

                room.capacity += 1
                student.stu_id = stu_id
                student.name = stu_name
                student.college = college
                student.detail = detail
                student.save()
            except:
                print_exc()
                continue
