# 28、需求：对TPshop项目进行前台登录设计脚本
# 要求：
# 1. 使用unittest框架
# 2. 使用Fixture(setup、tearDown)
# 3. 浏览器最大化、隐式等待30秒
# 4. 使用断言判断登录用户是否为admin，不是则截屏保存图片
# 5. 图片命名格式为脚本执行时间(年月日时分秒)
from selenium import webdriver
import time
import unittest


class DengLu(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.user = webdriver.Chrome()
        cls.user.get("http://localhost/")
        cls.user.maximize_window()
        cls.user.implicitly_wait(30)


    @classmethod
    def tearDownClass(cls):
        cls.user.quit()

    def yhm(self):
        self.user.find_element_by_css_selector('.red').click()
        self.user.find_element_by_css_selector('#username').send_keys("admin")
        if self.user.find_element_by_css_selector('#username').text == "admin":
            self.assertIn("admin", self.user.find_element_by_css_selector('#username').text)
        else:
            cc = "./test-{}.png".format(time.strftime("%Y%m%d%H%M%S"))
            self.user.get_screenshot_as_file(cc)
