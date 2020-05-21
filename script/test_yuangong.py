import unittest
import requests
from api.login_api import login


class TestYuan(unittest.TestCase):



    def test_01_yuan(self):
        # 登录
        response = login({"mobile": "13800000002", "password": "123456"})
        print(response.json())
        # 添加员工
        aa_url = "http://ihrm-test.itheima.net/api/sys/user"
        token = response.json().get("data")
        aa = requests.post(aa_url,
                      headers={"Content-Type": "application/json", "Authorization": "Bearer " + token},
                      json={
                          "username": "大幅度发06",
                          "mobile": "18709098997",
                          "timeOfEntry": "2020-05-05",
                          "formOfEmployment": 1,
                          "workNumber": "1234123",
                          "departmentName": "测试部",
                          "departmentId": "1063678149528784896",
                          "correctionTime": "2020-05-17T16:00:00.000Z"
                      })
        print(aa.json())
        # 查询员工
        response = aa.json().get("data").get("id")
        bb_url = aa_url + "/" + response
        bb =requests.get(bb_url,
                     headers={"Content-Type": "application/json", "Authorization": "Bearer " + token})
        print(bb.json())

        cc =requests.put(bb_url,
                     json={"username":"发的发的发2033"},
                     headers={"Content-Type": "application/json", "Authorization": "Bearer " + token})
        print(cc.json())

        dd =requests.delete(bb_url,
                            headers={"Content-Type": "application/json", "Authorization": "Bearer " + token})
        print(dd.json())