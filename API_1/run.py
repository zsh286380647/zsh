# -*- coding:utf-8 -*-
# @Time:2019/3/13/001311:39
# @Author:tata
# @Email:286380647@qq.com
# @File:run.py
# @Software:PyCharm Community Edition

import sys
sys.path.append("./")
import unittest
# import HTMLTestRunnerNew
from API_1.ext import HTMLTestRunnerNew
from API_1.test_cases import case_login_regist ,case_recharge,case_bidloan,case_withdraw,case_addloan
from API_1.common import project_path
# from API_1.common.logging_ import MyLog

suite = unittest.TestSuite() #容器
loader = unittest.TestLoader() #加载
suite.addTest(loader.loadTestsFromModule(case_login_regist))
# suite.addTest(loader.loadTestsFromModule(case_recharge))
# suite.addTest(loader.loadTestsFromModule(case_bidloan))
# suite.addTest(loader.loadTestsFromModule(case_withdraw))
# suite.addTest(loader.loadTestsFromModule(case_addloan))


with open(project_path.test_report_path+"/测试结果.html","wb") as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                              verbosity=2,
                                              title="第一个测试",
                                              description="测试数学类",
                                              tester="踏踏")
    runner.run(suite)



