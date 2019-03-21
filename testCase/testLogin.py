# -*- coding: utf-8 -*
"""
测试不同情况登录
"""
import os
import sys
sys.path.append(os.path.abspath("./"))
from page.loginpage import LoginPage
from public.logger import Logger
import unittest
import ddt
import time

# from public.readYaml import readYaml


@ddt.ddt
class Test_LoginModule(unittest.TestCase):

    logger = Logger("info").getLog()
    def setUp(self):
        print("开始测试")


    @ddt.file_data(r"C:\Users\loudDD\GitProject\svoc\svoc\public\accout.yaml")
    @ddt.unpack
    def test_login(self,**data):
        try:
            username = data.get("username")
            pwd = data.get("pwd")
            result = data.get("result")
            self.case = LoginPage()
            self.case.login(username,pwd)
            self.assertTrue(result == self.case.driver.current_url)
            self.logger.info("pass")
        except Exception as e:
            self.filename = os.path.join("{0}screenshot.png".format(time.strftime("%Y-%m-%d")))
            self.imgpath = os.path.join(os.path.abspath("../"), "screenshot")
            self.path = os.path.join(self.imgpath, self.filename)
            self.case.screen(self.path)
            self.logger.critical((e,"已截图",self.filename))#需要括号括起来，以达到传入一个元素（多个信息）

    def tearDown(self):
        self.case.driver.quit()
        print('测试结束')
if __name__ == '__main__':
    unittest.main()