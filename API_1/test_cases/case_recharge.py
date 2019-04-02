# -*- coding:utf-8 -*-
# @Time:2019/3/11/001112:09
# @Author:tata
# @Email:286380647@qq.com
# @File:case_login_regist.py
# @Software:PyCharm Community Edition
from API_1.common.http_request import Request
from API_1.common.do_excel import DoExcel
import unittest
from ddt import ddt,data,unpack
from API_1.common import project_path
from API_1.common.logging_ import MyLog
from API_1.common.get_data import GetData
from API_1.common.do_mysql import DoMysql
import json




data_racharge = DoExcel(project_path.cases_path, "充值")
case_racharge = data_racharge.read_excel()#获取excel充值的数据
my_log = MyLog()
# COOKIES = None
@ddt
class CaseRacharge(unittest.TestCase):
    def setUp(self):
        print("=======用例开始=======")

    def tearDown(self):
        print("=======用例结束=======\n")

    @data(*case_racharge)
    @unpack
    def test_dat(self,case_id,case_name,case_module,method,url,parames,sql,expect_result): #接收用例的 序号,路径,参数,期望结果
        # global COOKIES
        if sql is not None: #充值前的金额
            before_amount = DoMysql().do_mysql(eval(sql)["sql"])[0]

        par = eval(parames)  #将获取得到excel的请求数据转化为字典,用于下面的传参
        res = Request().http_request(url=url, parames=par, cookies=GetData.COOKIES, method=method)  # 发起请求
        if res.cookies:  #如果有cookies,则将该cookies替换为GetData里面的COOKIES属性
            COOKIES = setattr(GetData,'COOKIES',res.cookies)
        # A_R = json.loads(actual_result)  #实际结果==>把json格式转化为字典
        # E_R = json.loads(expect_result)  #期望结果==>把json格式转化为字典
        my_log.info("正在执行第[{}]条用例,[{}]模块:[{}]".format(case_id,case_module,case_name))
        print("标题为:",case_name)
        print(res.text)
        try:
            if sql is not None:
                after_amount = DoMysql().do_mysql(eval(sql)["sql"])[0]# 充值后的金额
                recharge_amount = int(eval(parames)["amount"])
                expect_amount = before_amount+recharge_amount  #期望的充值后的金额
                # print(after_amount,expect_amount)
                self.assertEqual(expect_amount,after_amount)
            if expect_result.find("expect_amount") > -1:
                expect_result = expect_result.replace("expect_amount",str(expect_amount))
                print(expect_result)
            # self.assertEqual(A_R,E_R)#
            self.assertEqual(expect_result,res.text)  #关键字断言
            result = "pass"
            print("用例通过")
        except AssertionError as e:
            result = "false"
            print("用例不通过,错误为:",e)
            raise e
        finally:
            my_log.info("用例结果:{}".format(result))
            data_racharge.write_excel(case_id + 1, 10, result) #写入是否通过
            data_racharge.write_excel(case_id + 1, 9, res.text)  #写入实际结果








