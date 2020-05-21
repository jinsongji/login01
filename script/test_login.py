import unittest
from api.login_api import login
import requests


class Test(unittest.TestCase):

    def test_01_login_success(self):
        response = login({"mobile": "13800000002", "password": "123456"})
        print(response.json())
        self.assertEqual(True, response.json().get("success"))

    def test_02_username_not(self):
        response = login({"mobile": "13900000002", "password": "123456"})
        print(response.json())
        self.assertEqual(False, response.json().get("success"))

    def test_03_password_ererr(self):
        response = login({"mobile": "13800000002", "password": "1234567"})
        print(response.json())
        self.assertEqual(False, response.json().get("success"))

    def test_04_username_null(self):
        response = login({"mobile": "", "password": "123456"})
        print(response.json())
        self.assertEqual(False, response.json().get("success"))

    def test_05_password_null(self):
        response = login({"mobile": "13800000002", "password": ""})
        print(response.json())
        self.assertEqual(False, response.json().get("success"))

    def test_06_username_fu(self):
        response = login({"mobile": "1380000+0002", "password": "123456"})
        print(response.json())
        self.assertEqual(False, response.json().get("success"))

    def test_07_more_params(self):
        response = login({"mobile": "13800000002", "password": "123456", "more_params": "more_params"})
        print(response.json())
        self.assertEqual(True, response.json().get("success"))

    def test_08_uername_null(self):
        response = login({"password": "123456"})
        print(response.json())
        self.assertEqual(False, response.json().get("success"))

    def test_09_password_null(self):
        response = login({"mobile": "13800000002"})
        print(response.json())
        self.assertEqual(False, response.json().get("success"))

    def test_10_null(self):
        response = login(None)
        print(response.json())
        self.assertEqual(False, response.json().get("success"))
