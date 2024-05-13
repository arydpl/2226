#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/4/27 8:46
# Author    : litianzhou
# @File     : send_email_base.py
# @Software : PyCharm
# 用于建立smtp连接
import smtplib
# 邮件需要专门的MIME格式
from email.mime.text import MIMEText
# plain指普通文本格式邮件内容
msg = MIMEText('哈哈哈哈哈', 'plain', 'utf-8')
# 发件人
msg['From'] = '3513543733@qq.com'
# 收件人
msg['To'] = '3513543733@qq.com'
# 邮件的标题
msg['Subject'] = '邮件标题——今天又是欺负犯困的一天'

smtp = smtplib.SMTP_SSL('smtp.qq.com')
smtp.login('3513543733@qq.com', 'pdpvdzdmbuprdaih')
smtp.sendmail('3513543733@qq.com',"3513543733@qq.com", msg.as_string())
smtp.quit()




