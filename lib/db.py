#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/4/19 16:12
# Author    : litianzhou
# @File     : db.py
# @Software : PyCharm
import pymysql
def conn():
    con=pymysql.connect(host="localhost",port=3306,
                         user="root",password='root',
                         db="p2p add产品",charset="utf8")
    return con
# 封装数据库查询操作
def query_db(sql):
 con = conn()
 # 建立游标
 cursor = con.cursor()
  # 执行sql
 cursor.execute(sql)
# 获取所有查询结果
 result = cursor.fetchone()
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
        # 如果成功就提交
        con.commit()
    except:
        # 如果失败就回滚
        con.rollback()
    finally:
         cursor.close()
         con.close()
# 封装常用数据库操作
def check_product(num):
     rel = query_db("select * from product where proNum = '{}'".format(num))
     # 三目运算符
     return True if rel else False
def add_product(num,name,limit,annual):
     change_db("insert into product (proNum, proName,proLimit,annualized) values ('{}','{}','{}','{}')".format(num,name,limit,annual))
     # print("add")
def del_product(num):
     change_db("delete from product where proNum='{}'".format(num))
     # print("删除")











