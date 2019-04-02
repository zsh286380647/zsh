# -*- coding:utf-8 -*-
# @Time:2019/3/19/001917:27
# @Author:tata
# @Email:286380647@qq.com
# @File:case_bidload.py
# @Software:PyCharm Community Edition
from API_1.common.http_request import Request
from API_1.common.do_excel import DoExcel
import unittest
from ddt import ddt,data,unpack
from API_1.common import project_path
from API_1.common.logging_ import MyLog
import json
import requests
from API_1.common.do_mysql import DoMysql



# 1：投资增加数据库的校验，可以写断言也可以写会数据库检查的结果到Excel
# 2：充值的请求 检查正常充值后的数据库检查  写回检查结果  期望值的leaveamount是可以做参数化的
# 3:所有用例的正常用例的手机号码 memberid 都把数据写到GetData这个类里面去或者是写到配置文件里面去

data_bidload = DoExcel(project_path.cases_path, "投资")
case_bidload = data_bidload.read_excel()#获取excel充值的数据
my_log = MyLog()
COOKIES = None
@ddt
class CaseBidload(unittest.TestCase):
    def setUp(self):
        print("=======用例开始=======")

    def tearDown(self):
        print("=======用例结束=======\n")

    @data(*case_bidload)
    @unpack
    def test_dat(self,case_id,case_name,case_module,method,url,parames,sql,expect_result): #接收用例的 序号,路径,参数,期望结果
        global COOKIES

        if sql is not None:  #投资前的金额
            sql_1 = eval(sql)["sql"]
            before_amount = DoMysql().do_mysql(sql_1,1)[0]
            # print(type(before_amount),before_amount)
        par = eval(parames)  #将获取得到excel的请求数据转化为字典,用于下面的传参
        res = Request().http_request(url=url, parames=par, cookies=COOKIES, method=method)  # 发起请求,投资
        if sql is not None:  #投资后的金额
            sql_1 = eval(sql)["sql"]
            after_amount = DoMysql().do_mysql(sql_1,1)[0]
            # print(type(after_amount),after_amount)
        if res.cookies:
            COOKIES = res.cookies
        # A_R = json.loads(actual_result)  #实际结果==>把json格式转化为字典
        # E_R = json.loads(expect_result)  #期望结果==>把json格式转化为字典
        my_log.info("正在执行第[{}]条用例,[{}]模块:[{}]".format(case_id,case_module,case_name))
        print("标题为:",case_name)

        try:
            # self.assertEqual(A_R,E_R)#
            self.assertIn(expect_result,res.text)  #关键字断言
            if sql is not None: #如果有查询语句,则执行下列
                expect_amount = before_amount - after_amount #期望投资金额
                invest_amount = int(eval(parames)["amount"])#数据库实际投资金额
                # print(type(expect_amount),expect_amount)
                # print(type(invest_amount),invest_amount)
                self.assertEqual(expect_amount,invest_amount) #期望金额和实际金额是否相匹配
            result = "pass"
            print("用例通过")
        except AssertionError as e:
            result = "false"
            print("用例不通过,错误为:",e)
            raise e
        finally:
            my_log.info("用例结果:{}".format(result))
            data_bidload.write_excel(case_id + 1, 10, result) #写入是否通过
            data_bidload.write_excel(case_id + 1, 9, res.text)  #写入实际结果