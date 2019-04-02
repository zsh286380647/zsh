# -*- coding:utf-8 -*-
# @Time:2019/2/28/002811:34
# @Author:tata
# @Email:286380647@qq.com
# @File:tata_homework8_logging.py
# @Software:PyCharm Community Edition
import logging
from API_1.common.configparser_ import ConF
from API_1.common import project_path
class MyLog:
    def __init__(self):
        #可在log.conf文件里修改对应参数
        cf = ConF(project_path.conf_path)
        self.logger_name = cf.read_str("log",'logger_name')#收集器的名字
        self.logger_level = cf.read_str("log","logger_level") #收集器的收集的等级
        self.file_name = cf.read_str("log","file_name")#输出的日志文件名
        self.file_level = cf.read_str("log","file_level")#日志文件的输出等级
        self.stream_level = cf.read_str("log","stream_level")#控制台的输出等级
        self.formatter = cf.read_str("log","formatter")#日志的格式

    def my_log(self,level,msg):
        #新建一个日志收集器
        my_log = logging.getLogger(self.logger_name)
        my_log.setLevel(self.logger_level)
        #设置格式
        formatter = logging.Formatter(self.formatter)

        #输出控制台
        ch = logging.StreamHandler()
        ch.setLevel(self.stream_level)
        ch.setFormatter(formatter)
        #输出到文件
        fh = logging.FileHandler(project_path.test_log_path,encoding="utf-8")
        fh.setLevel(self.file_level)
        fh.setFormatter(formatter)

        #对接
        my_log.addHandler(ch)
        my_log.addHandler(fh)

        if level == "DEBUG":
            my_log.debug(msg)
        if level=="INFO":
            my_log.info(msg)
        if level == "WARNING":
            my_log.warning(msg)
        if level == "ERROR":
            my_log.error(msg)
        if level == 'CRITICAL':
            my_log.critical(msg)
        # 去掉日志的重复 每次收集完毕之后 记得移除掉日志收集器
        my_log.removeHandler(ch)
        my_log.removeHandler(fh)
        fh.close()
    def debug(self,msg):
        self.my_log("DEBUG",msg)
    def info(self,msg):
        self.my_log("INFO",msg)
    def warning(self,msg):
        self.my_log("WARNING",msg)
    def error(self, msg):
        self.my_log("ERROR", msg)
    def critical(self,msg):
        self.my_log("CRITICAL",msg)


if __name__ == '__main__':
    log = MyLog()
    log.debug("嘿嘿")
    log.critical("哈哈哈")
