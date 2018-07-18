#!/usr/bin/env python
# coding: utf8
# 1006793841@qq.com
#
# 原文链接：https://blog.csdn.net/datacastle/article/details/78812575
# https://movie.douban.com/tag/#/?sort=T&range=0,10&tags=%E5%8A%B1%E5%BF%97
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"}

# #第二页
# https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=&start=20
#
# #第三页
# https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=&start=40
#
# #第四页
# https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=&start=60

import requests
import json
import time
import random

for a in range(2):
    url_visit = "https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=&start={}".format(a*20)
    # file = requests.get(url_visit)
    # print file   # 只打印出response 200
    file_json = requests.get(url_visit).json()
    # print file_json
    time.sleep(random.uniform(2,5))

    for i in range(2):
        dict = file_json['data'][i]
        urlname = dict['url']
        title = dict['title']
        rate = dict['rate']
        cast = dict['casts']

        # print "this is urlname", type(urlname),urlname
        # print "this is title", type(title),title
        # print "rate",type(rate),rate
        # print "cast",type(cast),cast
        # print "join_cast",type("  ".join(cast)), "  ".join(cast)
        # print len(cast)
        # for i in cast:
        #     print "this is list cast", i
        print u"{} {} {} {}\n".format(title,rate," ".join(cast),urlname)  # 网页有中文，遇到Unicode编码问题


###################################################################
# random的常用方法
# >>> random.random()        # Random float x, 0.0 <= x < 1.0
# 0.37444887175646646
# >>> random.uniform(1, 10)  # Random float x, 1.0 <= x < 10.0
# 1.1800146073117523
# >>> random.randint(1, 10)  # Integer from 1 to 10, endpoints included
# 7
# >>> random.randrange(0, 101, 2)  # Even integer from 0 to 100
# 26
# >>> random.choice('abcdefghij')  # Choose a random element
# 'c'
# >>> items = [1, 2, 3, 4, 5, 6, 7]
# >>> random.shuffle(items)
# >>> items
# [7, 3, 2, 5, 6, 4, 1]
# >>> random.sample([1, 2, 3, 4, 5],  3)  # Choose 3 elements
# [4, 1, 5]
