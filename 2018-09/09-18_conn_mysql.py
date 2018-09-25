#!/usr/bin/env python
# coding: utf8
# author: channel
# 1006793841@qq.com

# from setting import *
# settings.py  字典，格式如:
hk_db = {'host':'147.152.11.6',
        'port':3309,
        'user':'mxshop',
         'passwd':'mxshop',
         'charset':'utf8'}
import MySQLdb

def create_conn(dbInfo):
    try:
        db = MySQLdb.connect(host=dbInfo["host"], port=dbInfo["port"], user=dbInfo["user"], passwd=dbInfo["passwd"], charset=dbInfo["charset"])
        cursor = db.cursor()
        cursor.execute('select version()')
        version_data = cursor.fetchone()
        print "ok DatabaseVersion: %s" % version_data
        db.close()

    except MySQLdb.Warning,w:
        print  '\033[32mWarning db host: %s %s\033[0m' % (dbInfo["host"], dbInfo["port"])
    except MySQLdb.Error, e:
        print  '\033[31mCant conn db host: %s %s\033[0m' % (dbInfo["host"], dbInfo["port"])

dbInfos = [hk_db]
if __name__ == "__main__":
    for dbInfo in dbInfos:
        if type(dbInfo).__name__ == 'dict':
            create_conn(dbInfo)
        else:
            print 'error'
            continue

