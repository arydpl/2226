import unittest,requests
from lib.db1 import *
name = "test2"
noname = "peter"
class MyTestCase(unittest.TestCase):
    url="http://192.168.55.99:8000/api/student/user/register"
    def test_reg_ok(self):
        # 检查noname是否已经在数据库中
        print(check_user(noname))
        if check_user(noname):
            # 如果已经存在就删除
            del_user(noname)
        data={"userName":noname,"password":"123456","userLevel":1}
        r = requests.post(url=self.url,json=data)
        # 预期结果
        result={"code":1,"message":"成功","response":None}
        self.assertDictEqual(result,r.json())
        #验证数据库中name是否已经存在了
        self.assertTrue(check_user(noname))
        # 清理
        del_user(noname)

    def test_reg_err(self):
        #检查name是否已经在数据库中
        if not check_user(name):
            # 如果没有就添加进入
            add_user(name,"123456")
        data = {"userName": name, "password": "123456", "userLevel": 1}
        r = requests.post(url=self.url, json=data)
        # 预期结果
        result = {"code":2,"message":"用户已存在","response":None}
        self.assertDictEqual(result, r.json())
if __name__ == '__main__':
    unittest.main()
