import json
import os
import sys
import threading
from time import sleep
from traceback import print_exc
from logs.log import Log
import eel
import pymysql


def start_django():
    # 判断操作系统类型
    sys_name: str = os.name.upper()
    if sys_name.startswith("NT"):  # windows系列
        # os.system("python manage.py makemigrations")
        # os.system("python manage.py migrate")
        os.system("python manage.py runserver 8000")
    elif sys_name.startswith("POSIX"):  # unix linux 系列
        # os.system("python3 manage.py makemigrations")
        # os.system("python3 manage.py migrate")
        os.system("python3 manage.py runserver 8000")


def start_eel():
    # 启动的函数调用放在最后,port=0表示使用随机端口,size=(宽,高)
    eel.start('db.html', port=8001, size=(1024, 800))


if __name__ == "__main__":
    # html文件所在文件夹
    eel.init('DormFrontend')
    # 检测数据库配置
    Log.i(__name__, "开始检查数据库配置")


    # 调用线程
    try:
        Log.i(__name__, "开始启动django")
        django = threading.Thread(target=start_django)
        django.setDaemon(True)
        django.start()
    except pymysql.err.InternalError:
        print_exc()
        Log.e(__name__, "数据库配置错误, django启动失败")
        sys.exit(0)

    sleep(2)
    Log.i(__name__, "开始尝试启动EEL")
    eel_t = threading.Thread(target=start_eel)
    eel_t.start()
    Log.i(__name__, "EEL启动成功")
    eel_t.join()



