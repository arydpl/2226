import unittest,requests
import json,ddt
from lib import read_excel
from lib.case_log import log_case_info
from config.config import *
def read():
    r = read_excel.readexcel()
    l = r.excel_to_list(data_file,"test_user_login")
    t = []
    for i in range(len(l)):
        t.append(l[i]["case_name"])
    return t
@ddt.ddt()
class MyTestCase(unittest.TestCase):
    @ddt.data(*read())
    def test_login(self, name):
        r = read_excel.readexcel()
        l = r.excel_to_list(data_file, "test_user_login")
        login1 = r.get_test_data(l, name)
        url = login1.get("url")
        # 获取到的是个字符串格式
        args = login1.get("args")
        a = json.loads(args)
        res = login1.get("expect_res")
        r = requests.post(url, json=a)
        # 将字符串转成字典
        print(args)
        log_case_info(name,url,a,res,r.text)
        self.assertIn(res, r.text)
if __name__ == '__main__':
    unittest.main()
