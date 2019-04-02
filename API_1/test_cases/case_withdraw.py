# -*- coding:utf-8 -*-
# @Time:2019/3/19/001917:27
# @Author:tata
# @Email:286380647@qq.com
# @File:case_withdraw.py
# @Software:PyCharm Community Edition
from API_1.common.http_request import Request
from API_1.common.do_excel import DoExcel
import unittest
from ddt import ddt,data,unpack
from API_1.common import project_path
from API_1.common.logging_ import MyLog
import json
import requests


data_withdraw = DoExcel(project_path.cases_path, "提现")
case_withdraw = data_withdraw.read_excel()#获取excel充值的数据
my_log = MyLog()
COOKIES = None
@ddt
class CaseWithdraw(unittest.TestCase):
    def setUp(self):
        print("=======用例开始=======")

    def tearDown(self):
        print("=======用例结束=======\n")

    @data(*case_withdraw)
    @unpack
    def test_dat(self,case_id,case_name,case_module,method,url,parames,sql,expect_result): #接收用例的 序号,路径,参数,期望结果
        global COOKIES
        par = eval(parames)  #将获取得到excel的请求数据转化为字典,用于下面的传参
        res = Request().http_request(url=url, parames=par, cookies=COOKIES, method=method)  # 发起请求
        if res.cookies:
            COOKIES = res.cookies
        # A_R = json.loads(actual_result)  #实际结果==>把json格式转化为字典
        # E_R = json.loads(expect_result)  #期望结果==>把json格式转化为字典
        my_log.info("正在执行第[{}]条用例,[{}]模块:[{}]".format(case_id,case_module,case_name))
        print("标题为:",case_name)

        try:
            # self.assertEqual(A_R,E_R)#
            self.assertIn(expect_result,res.text)  #关键字断言
            result = "pass"
            print("用例通过")
        except AssertionError as e:
            result = "false"
            print("用例不通过,错误为:",e)
            raise e
        finally:
            my_log.info("用例结果:{}".format(result))
            data_withdraw.write_excel(case_id + 1, 10, result) #写入是否通过
            data_withdraw.write_excel(case_id + 1, 9, res.text)  #写入实际结果