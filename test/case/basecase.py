import unittest,requests,json,sys,ast
from lib.read_excel import *
from lib.case_log import *
from config.config import *
class BaseCase(unittest.TestCase):
    r =readexcel()
    @classmethod
    def setUpClass(cls):
        print(cls.__name__)
        if cls.__name__!="BaseCase":
            cls.data_list=cls.r.excel_to_list(data_file,cls.__name__)
            print(cls.__name__)
    def get_case_data(self,case_name):
        return self.r.get_test_data(self.data_list,case_name)
    def send_request(self,case_data):
        case_name =self.get_case_data("case_name")
        url=case_data.get("url")
        # url1=case_data[“url”]
        method=case_data.get("method")
        headers=case_data.get("headers")

        args=case_data.get("args")
        data_type = case_data.get('data_type')
        expect_res = case_data.get('expect_res')
        # print(url,method,headers,args,data_type,expect_res)
        if method.upper() == 'GET':
            logging.info("get data")
            response = requests.get(url,headers=headers,params=args)
            print(response.text)
            log_case_info(case_name,url,args, expect_res, requests.json())
        elif data_type.upper() == 'JSON':
            logging.info("post json data")
            response = requests.post(url, json=json.loads(args))
            log_case_info(case_name, url, args, expect_res, response.json())
            print(response.text)
            self.assertIn(expect_res,response.text)
        elif data_type.upper() == 'FORM':
            logging.info("post form data")
            response = requests.post(url, headers=headers, data=args)
            log_case_info(case_name, url, args, expect_res, requests.json())
            print(response.text)
            self.assertIn(expect_res,response.text)
        else:
            print("""暂不支持该数据类型""")
if __name__ == '__main__':
    unittest.main()