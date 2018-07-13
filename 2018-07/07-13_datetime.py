#!/usr/bin/env python
# coding: utf8
# author: channel
# 1006793841@qq.com
#

import datetime
i = datetime.datetime.now()
print "当前的日期和时间是：%s" % i
print "ISO格式的日期和时间：%s" % i.isoformat()
print ""

today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
now_time = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")

print today
print yesterday
print now_time


import time
# time.sleep(3)
# 打印时间戳，UNIX和Windows只支持到2038年
print time.time()
# 打印本地时间
print time.localtime()
print time.localtime(time.time())
# 获取格式化时间
print time.asctime()
print time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime())
