#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/4/28 14:36
# Author    : litianzhou
# @File     : send_email.py
# @Software : PyCharm
import smtplib
#邮件需要专门的MIME格式
from email.mime.text import MIMEText
# 混合MIME格式,支持上传附件
from email.mime.multipart import MIMEMultipart
# 用于使用中文邮件主题
from email.header import Header
from config.config import *
def send_email(report_file):
# 1.编写邮件内容
# 获取附件文件
    with open(report_file, encoding='utf-8') as f:
        email_body = f.read() # 读取附件文件内容


    msg = MIMEMultipart() # 混合MIME格式(支持上传附件)
    msg.attach(MIMEText(email_body, 'html', 'utf-8')) # 添加html格式邮件正文(会丢失css格式)
# 2.组装Email头(发件人,收件人,主题)

    msg["From"] = sender

    msg["To"] = receiver

    msg["Subject"] = Header(subject,"utf-8")

    # 3.构造附件1,传送当前目录下的 report.html 文件
    att1 = MIMEText(open(report_file, 'rb').read(), 'base64', 'utf-8') # 二进制格式打开
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename="report.html"' # filename附件显示的名字
    msg.attach(att1)
    try:
        # 4.连接smtp服务器并发送邮件
        smtp = smtplib.SMTP_SSL(smtp_server)
        smtp.login(smtp_user,smtp_password)
        smtp.sendmail(sender,receiver, msg.as_string())
        logging.info("========发送邮件成功========")
    except Exception as e:
        logging.error(str(e))
    finally:
        smtp.quit()
if __name__ == '__main__':
    send_email("report.html")