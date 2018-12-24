import unittest
from svoc.page.loginpage import Login


class login(unittest.TestCase):
    """
    登录模块：各种登录情况
    TODO:错误判断元素
    TODO:获取登录账号
    """
    def __init__(self):
        self.user = 1860000000
        self.pwd = 123456
    def loginRight(self):

        try:
            self.login=Login()
            self.login(self.user,self.pwd)
        except Exception:
            raise ValueError("error")
        try:
            self.assertEqual(self.login.driver.find_element_by_css_selector(err).text," ")
            print("Test case passed")
        except :
            print("Test case failed")