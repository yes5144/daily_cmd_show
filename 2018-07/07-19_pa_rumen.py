#!/usr/bin/env python
# coding: utf8
# 1006793841@qq.com
# this is python2.7

# 原文链接：https://blog.csdn.net/datacastle/article/details/78812471
import requests
from lxml import etree
import time
import random

url = 'https://movie.douban.com/subject/1292052/'
data = requests.get(url).text
s=etree.HTML(data)

# file=s.xpath('元素的Xpath信息/text()')
# //*[@id="content"]/h1/span[1]
film=s.xpath('//*[@id="content"]/h1/span[1]/text()')
print(film)

director=s.xpath('//*[@id="info"]/span[1]/span[2]/a/text()')    #导演
actor1=s.xpath('//*[@id="info"]/span[3]/span[2]/a[1]/text()')  #主演1
actor2=s.xpath('//*[@id="info"]/span[3]/span[2]/a[2]/text()')  #主演2
actor3=s.xpath('//*[@id="info"]/span[3]/span[2]/a[3]/text()')  #主演3
f_time =s.xpath('//*[@id="info"]/span[13]/text()')   #电影片长

print('电影名称：',film)
print('导演：',director)
print('主演：',actor1)
print('片长：',f_time)


# requests.request()
# requests.get()
# requests.head()
# requests.post()
# requests.put()
# requests.patch()
# requests.delete()

