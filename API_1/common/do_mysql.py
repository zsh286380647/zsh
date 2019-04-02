# -*- coding:utf-8 -*-
# @Time:2019/3/20/002023:00
# @Author:tata
# @Email:286380647@qq.com
# @File:do_mysql.py
# @Software:PyCharm Community Edition

from mysql import connector
from API_1.common.configparser_ import ConF
from API_1.common import project_path

class DoMysql:
    def do_mysql(self,select,flag = 1):
        """
        :param select: sql查询语句
        :param flag: 1:代表读取一条查询语句,2代表读取全部
        :return: 返回查询结果
        """
        #第一步:数据库信息,进行连接
        db_config = ConF(project_path.conf_path).read_other("mysql","mysql_info")
        cnn = connector.connect(**db_config)#连接
        #第二步:获取游标  获取数据库权限
        cursor = cnn.cursor()
        # 第三步:操作数据表
        cursor.execute(select) #执行语句
        if flag == 1:
            res = cursor.fetchone() #取得结果
        else:
            res = cursor.fetchall()
        cursor.close()
        cnn.close()
        return res

if __name__ == '__main__':
    # select = "select * from member where MobilePhone=13636760373 or MobilePhone = 18688773467"
    select = "select max(Id) from loan where MemberID=1123564"
    select_1 = "SELECT LeaveAmount FROM member WHERE MobilePhone = '13636760373'"
    a = DoMysql().do_mysql(select_1,1)
    print(a[0])
