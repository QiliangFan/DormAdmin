import time
import PROPATH

class Log:
    def __init__(self):
        pass

    @classmethod
    def i(cls,tag:str, msg: str):
        with open(PROPATH.PROJECT + "logs/" + cls.cur_day() + ".txt", "+a") as fp:
            print(cls.cur_time(), "INTRO",tag, msg,file=fp)

    @classmethod
    def w(cls,tag:str, msg: str):
        with open(PROPATH.PROJECT + "logs/" + cls.cur_day() + ".txt", "+a") as fp:
            print(cls.cur_time(), "WARNING", tag, msg, file=fp)

    @classmethod
    def e(cls, tag:str, msg: str):
        with open(PROPATH.PROJECT + "logs/" + cls.cur_day() + ".txt", "+a") as fp:
            print(cls.cur_time(), "ERROR", tag, msg, file=fp)

    @classmethod
    def cur_time(cls):
        return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

    @classmethod
    def cur_day(cls):
        return time.strftime("%Y-%m-%d", time.localtime(time.time()))