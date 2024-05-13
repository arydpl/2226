import unittest,requests
from lib import xzs_login
class MyTestCase(unittest.TestCase):
    url = "http://192.168.55.99:8000/api/user/login"
    header = {
        "content-type": "application/json"
    }
    def test_login_ok(self):
        data={"userName":"student","password":"123456","remember":False}
        r = requests.post(url=self.url,headers=self.header,json=data)
        #print(r.text)
        self.assertIn("成功",r.text)
    def test_login_err(self):
        data={"userName":"","password":"123456","remember":False}
        r = requests.post(url=self.url,headers=self.header,json=data)
        self.assertIn("用户名或密码错误",r.text)

if __name__ == '__main__':
    unittest.main()
