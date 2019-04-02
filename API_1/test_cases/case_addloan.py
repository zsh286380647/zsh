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
from API_1.common.get_data import repalce
from API_1.common.do_mysql import DoMysql
import json


data_addloan = DoExcel(project_path.cases_path, "新增项目")
case_addloan = data_addloan.read_excel()#获取excel充值的数据
my_log = MyLog()
# COOKIES = None
@ddt
class CaseAddloan(unittest.TestCase):
    def setUp(self):
        print("=======用例开始=======")

    def tearDown(self):
        print("=======用例结束=======\n")

    @data(*case_addloan)
    @unpack
    def test_dat(self,case_id,case_name,case_module,method,url,parames,sql,expect_result): #接收用例的 序号,路径,参数,期望结果


        #替换loan_id,mobilephone,pwd
        print('值1:', parames)
        parames = repalce(parames)
        print('值2:',parames)
        # if parames.find("loanid")!=-1: #如果"loanid"在params中
        #     parames = parames.replace("loanid",str(getattr(GetData,"loanid")))
        res = Request().http_request(url=url, parames=eval(parames), cookies=GetData.COOKIES, method=method)  # 发起请求
        if sql != None:
            SQL = eval(sql)
            loanid = DoMysql().do_mysql(SQL["sql"],1)[0]#查询数据库,得到int类型的当前的loanid
            setattr(GetData,"loanid",str(loanid))    ####重点str:将GetData的属性loanid修改为上面查询到的loanid的数值
        if res.cookies:  #如果有res.cookies,则替换GetData的属性值
            COOKIES = setattr(GetData,'COOKIES',res.cookies)
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
            data_addloan.write_excel(case_id + 1, 10, result) #写入是否通过
            data_addloan.write_excel(case_id + 1, 9, res.text)  #写入实际结果








