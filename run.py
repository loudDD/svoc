"""
run文件：读取用例路径，报告路径，通过报告路径+自定义文件名生成最终报告位置
使用unittest.defaultTestLoader.discover来发现用例路径中的用例
HTMLtestrunner生成最终报告
"""
import sys
import os
sys.path.insert(0,os.path.abspath(os.path.dirname(os.getcwd())))
import unittest
import time
from HTMLTestRunner import HTMLTestRunner
from svoc.config.readconfig import readConfig

CASEPATH = readConfig().getconfigvalue("path", "CasePath")
REPORTPATH = readConfig().getconfigvalue("path", "ReportPath")

def run():
    """定义具体操作"""
    case = unittest.defaultTestLoader.discover(CASEPATH, pattern="test*.py")
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = REPORTPATH + "\\" + now + "自动化测试结果.html"
    fp = open(filename, "wb")
    runner = HTMLTestRunner(stream=fp, title="测试报告", description="用例执行情况")
    runner.run(case)

    fp.close()


if __name__ == "__main__":
    # 自己调用则运行
    run()
