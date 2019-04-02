# -*- coding:utf-8 -*-
# @Time:2019/2/25/002522:12
# @Author:tata
 # @File:tata_homework7_configparser.py
# @Software:PyCharm Community Edition

from configparser import ConfigParser
from API_1.common import project_path


class ConF:
    """配置类,用于读取各种数据类型"""
    def __init__(self,file_name):
        self.file_name = file_name
        self.cf = ConfigParser()

    def read_int(self,menu_1,menu_2):
        #读取整数

        self.cf.read(self.file_name,encoding="utf-8")
        value = self.cf.getint(menu_1,menu_2)
        return value

    def read_float(self,menu_1,menu_2):
        #读取浮点数
        self.cf.read(self.file_name,encoding="utf-8")
        value = self.cf.getfloat(menu_1,menu_2)
        return value

    def read_bool(self,menu_1,menu_2):
        #读取布尔值
        self.cf.read(self.file_name,encoding="utf-8")
        value = self.cf.getboolean(menu_1,menu_2)
        return value
    def read_str(self,menu_1,menu_2):
        #读取字符串
        self.cf.read(self.file_name, encoding="utf-8")
        value = self.cf[menu_1][menu_2]
        return value

    def read_other(self,menu_1,menu_2):
        #读取list tuple dict
        self.cf.read(self.file_name,encoding="utf-8")
        value = eval(self.cf[menu_1][menu_2])
        return value

if __name__ == '__main__':
    c = ConF(project_path.conf_path)
    value_1 = c.read_str("case","button")
    print("类型:",type(value_1),"值:",value_1)


