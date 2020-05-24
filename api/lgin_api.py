# 导包
import requests

class TestLoginApi:
    # 魔法方法默认执行
    def __init__(self):
        # 实例化
        self.denglu = requests.Session()
        # 登录的url
        self.login_url = "http://ihrm-test.itheima.net/api/sys/login"
        # 获取部门信息的url
        self.huoqu_url = "http://ihrm-test.itheima.net/api/company/department"
        # 部门添加的url
        self.tianjia_url = "http://ihrm-test.itheima.net/api/company/department"
    def login(self,json):
        respons = self.denglu.post(self.login_url,
                                   json=json)
        return respons
    def close(self):
        return self.denglu.close()
    def get_api(self):
        return self.denglu.get(self.huoqu_url)
    def jiajia_api(self,json):
        return self.denglu.post(self.tianjia_url,
                                   json=json)
