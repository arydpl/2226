#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/4/26 15:05
# Author    : litianzhou
# @File     : config.py
# @Software : PyCharm
import logging
import os
import time
from optparse import OptionParser
today = time.strftime('%Y%m%d', time.localtime())
now = time.strftime('%Y%m%d_%H%M%S', time.localtime())
# 项目路径
prj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path =os.path.join(prj_path,"data")
test_path =os.path.join(prj_path,"test")
test_case_path = os.path.join(prj_path,"test","case") # 用例目录

# log_file = os.path.join(prj_path,"log" ,'log.txt')
log_file = os.path.join(prj_path, 'log', 'log_{}.txt'.format(today))
report_file = os.path.join(prj_path, 'report', 'report_{}.html'.format(now))
# report_file = os.path.join(prj_path, 'report',"report.html")

print(report_file)
data_file=os.path.join(prj_path,"data","test_user_data.xlsx")
test_list_file = os.path.join(prj_path, 'test', 'test_list.txt')
last_fails_file = os.path.join(prj_path, 'last_fails.pickle')

# log文件配置
logging.basicConfig(
     level=logging.DEBUG,  # log level
     format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',  # log格式
     datefmt='%Y-%m-%d %H:%M:%S',  # 日期格式
     filename=log_file,  # 日志输出文件
     # encoding='utf-8',
     filemode='a') # 追加模式

# 数据库配置
db_host = '127.0.0.1'
db_port = 3306
db_user = 'root'
db_passwd = 'root'
db = 'xzs'

# 邮件配置
smtp_server = 'smtp.qq.com'
smtp_user = '3513543733@qq.com'
smtp_password = 'pdpvdzdmbuprdaih'
sender = smtp_user # 发件人
receiver = "3513543733@qq.com" # 收件人
subject = '接口测试报告' # 邮件主题
send_email_after_run = False  # 发送邮件


# 命令行选项
parser = OptionParser()
parser.add_option('--collect_only', action='store_true', dest='collect_only', help='仅收集测试用例')
parser.add_option('--tag', action='store', dest='tag',  default='level1', help='根据标签生成测试套件')
parser.add_option('--rerun_fails', dest='rerun_fails', action='store_true', help='重新运行失败的用例')

parser.add_option('--test_list', action='store_true', dest='test_list', help='运行test/testlist.txt列表指定用例')
# parser.add_option('--test_suite', action='store', dest='test_suite', help='运行指定的TestSuite')
# 应用选项(使生效)
(options, args) = parser.parse_args()


if __name__ == '__main__': # 测试
 logging.info("接口测试")




