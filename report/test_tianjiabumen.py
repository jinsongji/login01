# 导包
import logging
import requests
import unittest
from api.lgin_api import TestLoginApi
import utils
from api.tianjia_api import TestBuMen
# 定义类
class TestTianJia(unittest.TestCase):
    def setUp(self):
        self.aa = TestLoginApi()
        self.bb = TestBuMen()

    def tearDown(self):
        self.aa.close()

    def test_01_renwu(self):
        # 实例化
        # denglu = requests.Session()
        # 发送登录请求post
        json = {"mobile": "13800000002", "password": "123456"}
        respons = self.aa.login(json)
        # 打印登录的json数据
        logging.info("登录的结果为01:{}".format(respons.json()))
        # print("登录的结果为:", respons.json())
        # 断言登录的结果
        utils.duanyan(200,True,10000,"操作成功",respons,self)
        # self.assertEqual(200, respons.status_code)
        # self.assertEqual(True, respons.json().get("success"))
        # self.assertEqual(10000, respons.json().get("code"))
        # self.assertIn("操作成功", respons.json().get("message"))

        # 获取部门信息
        # 发送get请求
        respons = self.aa.get_api()
        # 打印get数据
        logging.info("获取部门的结果为01:{}".format(respons.json()))
        # print("获取部门信息的结果为:", respons.text)
        # 断言登录的结果
        utils.duanyan(200, True, 10000, "操作成功", respons, self)
        # self.assertEqual(200, respons.status_code)
        # self.assertEqual(True, respons.json().get("success"))
        # self.assertEqual(10000, respons.json().get("code"))
        # self.assertIn("操作成功", respons.json().get("message"))

        # 部门添加
        # 发送post请求
        # json = {"name": "一人之下04",
        #         "code": "9879",
        #         "manager": "1",
        #         "introduce": "菜鸟部",
        #         "pid": "1260120712836886528"}
        respons = self.aa.jiajia_api(self.bb.wanmei("一人之下65","98147"))
        # 打印部门添加的json数据
        logging.info("部门添加的结果为01:{}".format(respons.json()))
        # print("部门添加结果为:", respons.json())
        # 断言登录的结果
        utils.duanyan(200, True, 10000, "操作成功", respons, self)
        # self.assertEqual(200, respons.status_code)
        # self.assertEqual(True, respons.json().get("success"))
        # self.assertEqual(10000, respons.json().get("code"))
        # self.assertIn("操作成功", respons.json().get("message"))

    def test_02_is_none(self):
        # 发送登录请求post
        json = {"mobile": "13800000002", "password": "123456"}
        respons = self.aa.login(json)
        # 打印登录的json数据
        logging.info("登录的结果为02:{}".format(respons.json()))
        # print("登录的结果为:", respons.json())
        # 部门添加
        # 发送post请求
        json = None
        respons = self.aa.jiajia_api(json)

        # 打印部门添加的json数据
        logging.info("部门添加的结果为02:{}".format(respons.json()))
        # print("部门添加结果为02:", respons.json())
        # 断言登录的结果
        utils.duanyan(200, False, 99999, "抱歉，系统繁忙，请稍后重试！", respons, self)
        # self.assertEqual(200, respons.status_code)
        # self.assertEqual(False, respons.json().get("success"))
        # self.assertEqual(99999, respons.json().get("code"))
        # self.assertIn("抱歉，系统繁忙，请稍后重试！", respons.json().get("message"))

    def test_03_name_is_none(self):
        # 发送登录请求post
        json = {"mobile": "13800000002", "password": "123456"}
        respons = self.aa.login(json)
        # 打印登录的json数据
        logging.info("登录的结果为03:{}".format(respons.json()))
        # print("登录的结果为:", respons.json())
        # 部门添加
        # 发送post请求
        # json = {
        #         "code": "9878",
        #         "manager": "1",
        #         "introduce": "菜鸟部",
        #         "pid": "1260120712836886528"}
        respons = self.aa.jiajia_api(self.bb.que_name("654412"))
        # 打印部门添加的json数据
        logging.info("部门添加的结果为03:{}".format(respons.json()))
        # print("部门添加结果为03:", respons.json())
        # 断言登录的结果
        utils.duanyan(200, True, 10000, "操作成功", respons, self)
        # self.assertEqual(200, respons.status_code)
        # self.assertEqual(True, respons.json().get("success"))
        # self.assertEqual(10000, respons.json().get("code"))
        # self.assertIn("操作成功", respons.json().get("message"))
    def test_04_code_is_none(self):
        # 发送登录请求post
        json = {"mobile": "13800000002", "password": "123456"}
        respons = self.aa.login(json)
        # 打印登录的json数据
        logging.info("登录的结果为04:{}".format(respons.json()))
        # print("登录的结果为:", respons.json())
        # 部门添加
        # 发送post请求
        # json = {
        #         "name": "一人之上01",
        #         "manager": "1",
        #         "introduce": "菜鸟部",
        #         "pid": "1260120712836886528"}
        respons = self.aa.jiajia_api(self.bb.que_code("一人之下82222"))
        # 打印部门添加的json数据
        logging.info("部门添加的结果为04:{}".format(respons.json()))
        # print("部门添加结果为04:", respons.json())
        # 断言登录的结果
        utils.duanyan(200, True, 10000, "操作成功", respons, self)
        # self.assertEqual(200, respons.status_code)
        # self.assertEqual(True, respons.json().get("success"))
        # self.assertEqual(10000, respons.json().get("code"))
        # self.assertIn("操作成功", respons.json().get("message"))