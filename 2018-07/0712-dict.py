#!/usr/bin/env python
# coding: utf8
# author: channel
# 1006793841@qq.com
#

# define a dict
mysql_info = {'user':'root','password':'root','port':3306}
# print key user value
print mysql_info['user']
# type() return type
print type(mysql_info['password'])
# mysql_info.items()
# mysql_info.keys()
# mysql_info.values()
for k in mysql_info:
    print "\033[32mthis is dict.key\033[0m",k
    print type(k).__name__
