#!/usr/bin/env python
# coding: utf8
# author: channel
# 1006793841@qq.com
#
# 链接：https: // www.zhihu.com / question / 28661987 / answer / 41816092

import MySQLdb
import xlrd
# 打开excel
data = xlrd.open_workbook('testpython.xls')
# 根据名字拿到excel的某个表
table = data.sheet_by_name('Sheet1')
# 行数
nrows = table.nrows
for rownum in range(1, nrows):
    row = table.row_values(rownum)
    print len(row)

    # 打开数据库连接
    db = MySQLdb.connect("localhost", "root", "", "pythonmysql")
    # 链接资源
    cursor = db.cursor()

    # SQL 插入语句
    sql = 'insert into pyuser (username,password, email, qq) values("%s", "%s","%s","%s")' % \
          (row[0], row[1], row[2], row[3])
    print sql
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        db.rollback()
    # 关闭数据库连接
    db.close()
