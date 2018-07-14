#!/usr/bin/env python
# coding: utf8
# author: channel
# 1006793841@qq.com
#

import os
import time
import sys
import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate

def sendmail(f_from, f_to, f_cclist, alert_info, f_subject):
    From = f_from
    To = f_to
    # smtp.qq.com 需要使用SSL
    server = smtplib.SMTP_SSL("smtp.qq.com", port=465)
    # server = smtplib.SMTP("smtp.qq.com", port=465)
    server.login("122222222@qq.com","邮箱授权码")
    main_msg = MIMEMultipart()

    text_msg = MIMEText("您好。<br><br><br><br>"
                           + alert_info.title() +
                           "<br> channel <br>"
                           "xx技术股份有限公司 <br>"
                           "手机: xx<br>"
                           "座机：xxx<br>"
                           "邮箱：xxxx@xx.com<br>"
                           "地址：xxxx<br>"
                           "邮编：130011<br>"
                           "=======================<br>"
                           "",'HTML','utf-8')
    main_msg.attach(text_msg)
    # 设置根容器属性
    main_msg['From'] = From
    main_msg['To'] = To
    main_msg['Cc'] = ",".join(f_cclist)
    main_msg['Subject'] = f_subject
    main_msg['Date'] = formatdate(localtime=True)
    # f_cclist为完整的需要接收邮件的列表，原本只存放抄送列表，这里需要添加上收件人
    f_cclist.append(To)
    # 得到格式化后的完整文本
    fullText = main_msg.as_string()

    # 用smtp发送邮件
    try:
        server.sendmail(From, f_cclist, fullText)
    finally:
        server.quit()

if __name__ == "__main__":
    #sys.setdefaultencoding('utf-8')
    message= [
    'Usage:',
    '      sendmail.py "topic" "mail body text" "mail to"',
    'Examples of usage:',
    '      sendmail.py "topic" "hello world" "11111111@qq.com"',
    ]
    try:
        topic = str(sys.argv[1]).encode("utf-8")
        alert = str(sys.argv[2]).encode("utf-8")
        mailto = str(sys.argv[3]).encode("utf-8")
    except IndexError:
        for line in message:
            print line+'\n'
        sys.exit()
    cclist=[]
    #clist =[]
    sendmail("122222222@qq.com",mailto,cclist,alert,topic)

# ./sendmail.py "topic" "hello world" "11111111@qq.com"
