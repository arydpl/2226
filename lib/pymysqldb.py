import pymysql
try:
    # 创建一个连接
    conn=pymysql.connect(host="localhost",port=3306,
                         user="root",password='root',
                         database="xzs",charset="utf8")
    # 创建一个游标
    cursor = conn.cursor()
    # 利用游标对数据库进行操作
    cursor.execute("select * from t_user where id=1")
    # 获取利用游标操作的数据
    data = cursor.fetchone()
    print(data)
except Exception as e:
    print("出错啦！错误信息为：{}".format(e))
finally:
    # 关闭游标
    if cursor:cursor.close()
    # 关闭连接
    if conn:conn.close()
