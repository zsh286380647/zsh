# -*- coding: utf-8 -*-
# @Time    : 2019/3/18 21:07
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : get_data.py
from API_1.common import project_path
import re
class GetData:
    '''可以用来动态的更改 删除 获取数据'''
    COOKIES=None
    # loanid = None
    leaveamount = None
    normal_user = "13636760373"
    normal_pwd = "123456"
    normal_member_id = '1123564'

def repalce(target):
    p = '#(.*?)#'
    while re.search(p, target):
        res = re.search(p, target)
        key = res.group(1)
        value = getattr(GetData, key)
        target = re.sub(p, value, target, count=1)
    return target
if __name__ == '__main__':
    a = setattr(GetData,"loanid","2222")
    print(repalce('{"mobilephone":"#normal_user#","pwd":"#normal_pwd#"}'))
    print(repalce("{'id':'#loanid#','status':'4'}"))
#类属性
# print(GetData.COOKIE)
# print(GetData().COOKIE)
#类的反射可以动态的查看，增加，删除，更改类里面的属性
#利用反射的方法来拿值
# print(getattr(GetData,'COOKIE'))#第一个参数是类名  第二个参数是属性的参数名
# print(hasattr(GetData,'COOKIE'))#第一个参数是类名  第二个参数是属性的参数名 返回值是布尔值
# print(setattr(GetData,'COOKIE','123456'))
# #第一个参数是类名  第二个参数是属性的参数名 第三个你要设置的新值
# print(getattr(GetData,'COOKIE'))
#
# print(delattr(GetData,'COOKIE'))#删除类的某个属性  #第一个参数是类名  第二个参数是属性的参数名
# #不常用
# print(getattr(GetData,'COOKIE'))

