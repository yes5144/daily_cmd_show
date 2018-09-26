# -*- coding: utf8 -*-
import MySQLdb
import datetime
import time
from multiprocessing import Pool

# 新建数据库
# create database mxshop;
#
# 新建测试表
# create table table_iin (id int primary key auto_increment, `in` int, time datetime);
#
# 授权用户
# grant all on mxshop.* to mxshop_user@localhost identified by 'mxshop_pass';

def insert(io):
    time_now = datetime.datetime.now()
    print io, time_now
    conn = MySQLdb.connect(user="mxshop_user", passwd="mxshop_pass", host="localhost", db="mxshop")
    cur = conn.cursor()
    # sql = "insert into table_in (`in`, `time`) values ('%s','%s');"
    # cur.execute(sql%(io,time_now))
    sql = "update table_in set `time`='%s' where `in`='%s';"
    cur.execute(sql % (time_now, io))
    # sql = 'show databases;'
    # print cur.execute(sql)
    cur.close()
    conn.commit()
    time_end = datetime.datetime.now()
    print '\033[41mTask     %s runs %s seconds.\033[0m' % (io, (time_end - time_now))
    # time.sleep(2)

print 'Parent process begin'
i = 1
while i < 5:
    p = Pool()
    for n in range(1, 313):
        p.apply_async(insert, args=(n,))
    #    if n == 5:
    #        break
    print '\033[42mWaiting for all subpro done\033[0m'
    p.close()
    p.join()
    # time.sleep(3)
    print '\033[32m %s all done\033[0m' % i
    i += 1
