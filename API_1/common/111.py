# -*- coding:utf-8 -*-
# @Time:2019/3/13/00130:03
# @Author:tata
# @Email:286380647@qq.com
# @File:111.py
# @Software:PyCharm Community Edition

from API_1.common import project_path
from API_1.common.do_excel import DoExcel
# a = project_path.cases_path
# print(a,type(a))
# a = DoExcel(project_path.cases_path,"test")
# b = a.read_excel()
# print(b)

from openpyxl import Workbook
from openpyxl import load_workbook
import requests
import json
# http://47.107.168.87:8080/futureloan/mvc/api/member/register
# 登陆帐号
url_1 = 'http://47.107.168.87:8080/futureloan/mvc/api/member/login'
param_1 = {"mobilephone":"13636760373","pwd":"123456"}
res = requests.post(url_1, param_1)
print(res.text)

# url_1 = 'http://120.78.128.25:8080/futureloan/mvc/api/member/login'
# param_1 = {"mobilephone":"13636760373","pwd":"123456"}
# res = requests.post(url_1, param_1)
# print(res.text)
# print(res.cookies)
# print(res.status_code)
# print(res.headers)


# print(json.loads(res.text))
# print(res.text)
# print(a.status_code)#状态码
# print(a.cookies)
# print(a.headers)   #响应头
# print(a.request.headers)  #请求头

# # 充值
# url_2 = 'http://47.107.168.87:8080/futureloan/mvc/api/member/recharge'
# param_2 = {"mobilephone":"13636760373","amount":"1"}
# b = requests.get(url_2, param_2, cookies = res.cookies)
# print(b.text)
#
# # 取现
# url_3 = 'http://47.107.168.87:8080/futureloan/mvc/api/member/withdraw'
# param_3= {"mobilephone":"13636760373","amount":"是"}
# b = requests.get(url_3, param_3, cookies = res.cookies)
# print(b.text)

#获取用户列表
# url_4 = 'http://47.107.168.87:8080/futureloan/mvc/api/member/list'
# b = requests.get(url_4,cookies = res.cookies)
# print(b.text)



# 新增项目（add）
# url_4 = 'http://47.107.168.87:8080/futureloan/mvc/api/loan/add'
# param_4= {"memberId":"1123564",
#           "title":"卖老婆",
#           "amount":"10000",
#           "loanRate":"18.0",
#           "loanTerm":"30",
#           "loanDateType":"2",
#           "repaymemtWay":"4",
#           "biddingDays":"1"}
# b = requests.post(url_4, param_4, cookies = res.cookies)
# print(b.text)

#审核
# url_5 = 'http://47.107.168.87:8080/futureloan/mvc/api/loan/audit'
# param_5={"id":'17757','status':'4'}
# b = requests.get(url_5, param_5,cookies = res.cookies)
# print(b.text)

#投资、竞标（bidLoan）
# url_6 = 'http://47.107.168.87:8080/futureloan/mvc/api/member/bidLoan'
# param_6= {'memberId':'1123888','password':'123456','loanId':17527,'amount':None}
# b = requests.get(url_6, param_6, cookies = res.cookies)
# print(b.text)

# import sys
# print(sys.path)
# sys.path.append("./")
# print(sys.path)