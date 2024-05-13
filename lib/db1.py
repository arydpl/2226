#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/4/19 16:12
# Author    : litianzhou
# @File     : db1.py
# @Software : PyCharm
import logging
import pymysql
import sys
# 提升一级到目根目录下
sys.path.append("..")
from config.config import *
def conn():
    con=pymysql.connect(host=db_host,port=db_port,
                         user=db_user,password=db_passwd,
                         db=db,charset="utf8")
    return con
# 封装数据库查询操作
def query_db(sql):
 con = conn()
 # 建立游标
 cursor = con.cursor()
 logging.debug(sql)
  # 执行sql
 cursor.execute(sql)
# 获取所有查询结果
 result = cursor.fetchone()
 logging.debug(result)
# 关闭游标
 cursor.close()
 # 关闭连接
 con.close()
 # 返回结果
 return result
# 封装更改数据库操作
def change_db(sql):
    con = conn()
    cursor = con.cursor()
    try:
        cursor.execute(sql)
        logging.debug(sql)
        # 如果成功就提交
        con.commit()
    except Exception as e:
        logging.error(str(e))
    except:
        # 如果失败就回滚
        con.rollback()
    finally:
         cursor.close()
         con.close()
# 封装常用数据库操作
def check_user(name):
     rel = query_db("select * from t_user where user_name = '{}'".format(name))
     # 三目运算符
     return True if rel else False
def add_user(name, ps):
     change_db("insert into t_user (user_name, password) values ('{}','{}')".format(name,ps))
     print("add")
def del_user(name):
     change_db("delete from t_user where user_name='{}'".format(name))
     print("删除")











