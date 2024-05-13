#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/4/27 9:36
# Author    : litianzhou
# @File     : send_email_att.py
# @Software : PyCharm
import smtplib
#邮件需要专门的MIME格式
from email.mime.text import MIMEText
# 混合MIME格式,支持上传附件
from email.mime.multipart import MIMEMultipart
# 用于使用中文邮件主题
from email.header import Header
# 1.编写邮件内容
# 获取附件文件
with open('report.html', encoding='utf-8') as f:
    email_body = f.read() # 读取附件文件内容
msg = MIMEMultipart() # 混合MIME格式(支持上传附件)
msg.attach(MIMEText(email_body, 'html', 'utf-8')) # 添加html格式邮件正文(会丢失css格式)
# 2.组装Email头(发件人,收件人,主题)

msg["From"] = "3513543733@qq.com"
msg["To"] = "3513543733@qq.com"
msg["Subject"] = Header("接口测试报告","utf-8")

# 3.构造附件1,传送当前目录下的 report.html 文件
att1 = MIMEText(open('report.html', 'rb').read(), 'base64', 'utf-8') # 二进制格式打开
att1["Content-Type"] = 'application/octet-stream'
att1["Content-Disposition"] = 'attachment; filename="report.html"' # filename附件显示的名字
msg.attach(att1)

# 4.连接smtp服务器并发送邮件
smtp = smtplib.SMTP_SSL("smtp.qq.com")
smtp.login("3513543733@qq.com","pdpvdzdmbuprdaih")
smtp.sendmail("3513543733@qq.com","3513543733@qq.com", msg.as_string())
smtp.quit()