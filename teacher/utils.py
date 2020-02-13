####
# 管理端excel上传功能
#
####
from traceback import print_exc

from xlrd import open_workbook
from typing import List
import simplejson
from teacher.excel import read_excel

from DormBackend.models import Room
from PROPATH import PROJECT
from teacher.excel.read_excel import read_excel_manage_bed


def import_student(file_name: str):
    read_excel.read_excel_student(file_name)


def update_dorm(file_name: str):
    with open(file_name, "r") as fp:
        data:dict = simplejson.load(fp=fp)
    for build, item in data.items():
        door_num = item.get("door_num", 0)
        storey = item.get("storey", 0)
        room_per_storey = item.get("room_per_storey", 0)
        if door_num > 0:        # 有小单间
            for i in range(1, storey+1):
                for j in range(1, door_num + 1):
                    for k in range(1, room_per_storey+1):
                        for l in range(1, 5):
                            room_id = str(i) + "{0:0>2}".format(k)
                            room = Room()
                            room.capacity = 0
                            room.room_id = room_id
                            room.door_id = j
                            room.singleRoom_id = l
                            room.build = build
                            room.save()

        else:                   # 无小单间
            for i in  range(1, storey+1):
                for k in range(1, room_per_storey+1):
                    room_id = str(i) + "{0:0>2}".format(k)
                    room =Room()
                    room.capacity = 0
                    room.build = build
                    room.room_id = room_id
                    room.save()


def import_teacher(file_name: str, level: str):
    read_excel.read_excel_teacher(file_name, level)


def delete_all_account(file_name):
    try:
        read_excel.read_excel_student_del(file_name)
    except :
        print_exc()
    try:
        read_excel.read_excel_teacher_delete(file_name)
    except :
        print_exc()


def reset_all_account(file_name):
    try:
        read_excel.read_excel_student_reset(file_name)
    except :
        print_exc()
    try:
        read_excel.read_excel_teacher_reset(file_name)
    except :
        print_exc()


def add_inspection(file_name):
    read_excel.read_excel_add_inspection(file_name)


def manage_bed_util(file_name):
    read_excel_manage_bed(file_name)

if __name__ == "__main__":
    # read_excel("1.xls")
    # update_dorm("./files/dorm.json")
    pass