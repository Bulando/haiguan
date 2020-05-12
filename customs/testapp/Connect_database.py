# ！/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/4/25 13:24
# @Author : Zhou
# @Site : 
# @File : Connect_database.py
# @Software : PyCharm
# ---------------------------
import pymssql
import decimal
import traceback  # 跟踪报错

decimal.__version__


class Conn:  # 连接数据库类
    def __init__(self):
        self.server = 'DESKTOP-ODK8S4F'
        self.user = 'sa'
        self.password = '123456'
        self.database = 'HaiguanBeta'

    def con(self):
        # noinspection PyBroadException
        try:
            # connect = pyodbc.connect('SQL Server Native Client 11.0', 'DESKTOP-O2CM7MK', 'sa', 'sqlserver', 'HaiguanBeta')  # 服务器名,账户,密码,数据库名,建立连接
            connect = pymssql.connect(server=self.server,
                                      user=self.user, password=self.password,
                                      database=self.database)  # 服务器名,账户,密码,数据库名,建立连接
            if connect:
                print("数据库连接成功!")
            return connect
        except Exception as e:  # 捕获全部异常
            traceback.print_exc()


if __name__ == '__main__':
    conn = Conn()  # 连接
    conn = conn.con()
