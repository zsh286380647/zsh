# -*- coding:utf-8 -*-
# @Time:2019/2/19/001918:11
# @Author:tata
# @Email:286380647@qq.com
# @File:tata_homework5_request.py
# @Software:PyCharm Community Edition

# 2：编写一个类：你们自行去设计，要求写一个类，
#    初始化函数 对象函数 包含 根据你不同的选择完成get请求 OR post请求 ，
#    其中url 需要做参数化，并且最后要拿到响应结果

import requests

class Request:
    def http_request(self,url, parames ,cookies=None, method ="get"):
        if method.lower() == "get":
            res = requests.get(url,parames,cookies = cookies)
            return res
        if method.lower() == "post":
            res = requests.post(url,parames,cookies = cookies)
            return res


if __name__ == '__main__':
    # http://47.107.168.87:8080/futureloan/mvc/api/member/register
    url = 'http://47.107.168.87:8080/futureloan/mvc/api/member/register'
    para = {"mobilephone":"13612344678","pwd":"123456"}
    a = Request().http_request(url,para)
    print(a)
