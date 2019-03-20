"""
测试不同情况登录
"""

from page.loginpage import Login
#from public.logger import Logger
import unittest
import ddt

# from public.readYaml import readYaml


@ddt.ddt
class loginTest(unittest.TestCase):

    def setUp(self):
        print("开始测试")
    def tearDown(self):
        print('测试结束')

    @ddt.file_data(r"C:\Users\loudDD\GitProject\svoc\svoc\public\accout.yaml")
    @ddt.unpack
    def test_login(self,**data):
        username = data.get("username")
        pwd = data.get("pwd")
        result = data.get("result")
        case = Login()
        case.login(username,pwd)

        if self.assertTrue(result==case.driver.current_url):
            print("测试通过")
        else:
            print('测试失败')
            print(type(result),123)
            print(type(case.driver.current_url))

if __name__ == '__main__':
    unittest.main()