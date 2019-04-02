# -*- coding:utf-8 -*-
# @Time:2019/3/12/001223:48
# @Author:tata
# @Email:286380647@qq.com
# @File:project_path.py
# @Software:PyCharm Community Edition

import os
project_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]  #API文件的路径

cases_path = os.path.join(project_path,"test_cases","py14.xlsx")  #用例的路径
conf_path = os.path.join(project_path,"test_cases","log.conf")  #用例的路径
test_log_path = os.path.join(project_path,"test_result","test_log","test.log")#日志的路径
test_report_path = os.path.join(project_path,"test_result","test_report")#测试报告的文件夹路径


if __name__ == '__main__':
    print(test_log_path)

