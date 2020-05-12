import xlrd
import os
import random
from random import shuffle
from testapp.Connect_database import Conn


class ExcelRead(object):
    def __init__(self, table):
        self.table = table
        self.columns = self.table.ncols
        self.rows = self.table.nrows  # 获取总行数

    def list_data(self, li):
        if self.rows <= 1:
            print(u"excel行数小于等于1")
        else:
            for i in range(1, self.rows):
                values = self.table.row_values(i)
                li.append(values)

            return li

    def handle_uploaded_file(self, tables):
        conn = Conn()  # 连接
        conn = conn.con()
        for li in tables:
            sql = '''INSERT INTO [dbo].[data0]
           ([海关编号],[商品序号] ,[商品编号],[商品名称],[商品规格型号],[第一法定计量单位]
           ,[申报日期] ,[实征从价关税率] ,[应征从价关税率],[每项商品需要监管证件]
           ,[产销国],[经营单位编号],[经营单位名称],[货主单位代码],[货主单位名称]
           ,[申报单位代码],[申报单位名称],[监管方式],[实征从量关税税率]
           ,[应征从量关税税率],[实征从价增值税率],[应征从价增值税率]
           ,[实征从价消费税率],[应征从价消费税率],[实征从量消费税税率]
           ,[应征从量消费税税率],[实征从价反倾销税税率],[应征从价反倾销税税率]
           ,[关税完税价],[第一法定数量]) VALUES
           {}'''.format(tuple(li))
            print("sql---{}".format(sql))
            self.insert(conn, sql)

    def handle_csv_file(self, file_tag):
        return "等会阿鹏在这个方法里写"

    def insert(self, conn, sql):  # 数据库查询类，sql为查询语句
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        cursor.close()



