import json
import os
import threading
from traceback import print_exc
from logs.log import Log
import eel
import pymysql


def start_django():
    # 判断操作系统类型
    sys_name: str = os.name.upper()
    if sys_name.startswith("NT"):  # windows系列
        os.system("python manage.py runserver 8000")
    elif sys_name.startswith("POSIX"):  # unix linux 系列
        os.system("python3 manage.py runserver 8000")


def start_eel(is_config:bool):
    # 启动的函数调用放在最后,port=0表示使用随机端口,size=(宽,高)
    if is_config:
        eel.start('db.html?is_config=1', port=8001, size=(1024, 796))
    else:
        eel.start('db.html?is_config=0', port=8001, size=(1024, 796))


def define_config():
    global value_dic
    value_dic = {}


def set_config(value: bool):
    value_dic["is_config"] = value


def get_config():
    try:
        result = value_dic["is_config"]
    except:
        result = True
    return result


define_config()

if __name__ == "__main__":
    # html文件所在文件夹
    eel.init('DormFrontend')
    # 检测数据库配置
    Log.i(__name__, "开始检查数据库配置")
    fp = open("config/db.json", "r+")
    db_config = json.load(fp=fp)
    DB_NAME = db_config["DB_NAME"]
    USER_NAME = db_config["USER_NAME"]
    PASS_WORD = db_config["PASS_WORD"]
    HOST = db_config["HOST"]
    PORT = db_config["PORT"]
    if len(DB_NAME) == 0 or \
        len(USER_NAME) == 0 or \
        len(PASS_WORD) == 0 or \
        len(HOST) == 0 or \
        len(PORT) == 0:             # 数据库未配置成功
        set_config(False)
        Log.w(__name__, "数据库未配置成功")

    first = True
    while first or get_config():
        first = False
        # 调用线程
        try:
            Log.i(__name__, "开始启动django")
            django = threading.Thread(target=start_django)
            django.setDaemon(True)
            django.start()
        except pymysql.err.InternalError:
            print_exc()
            Log.e(__name__, "数据库配置错误, django启动失败")
            set_config(False)

        Log.i(__name__, "开始尝试启动EEL")
        eel_t = threading.Thread(target=start_eel, args=(get_config(),))
        eel_t.start()

        Log.i(__name__, "EEL启动成功")
        eel_t.join()


