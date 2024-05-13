import requests,unittest

class xzs_login(object):
    def login(self,user,ps):
        self.url = "http://192.168.55.1:8000/api/user/login"
        self.header = {
            "Content-Type": "application/json"
        }
        self.data = {"userName":user,"password":ps,"remember":False}
        r = requests.post(url=self.url,headers=self.header,json=self.data)
        return r.text
if __name__ == '__main__':
    unittest.main()