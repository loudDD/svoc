from svoc.config.readconfig import readConfig
import unittest
import time
from HTMLTestRunner import HTMLTestRunner

casepath = readConfig().getconfigvalue("path","casepath")
reportpath = readConfig().getconfigvalue("path","reportpath")
def run():
    case = unittest.defaultTestLoader.discover(casepath,pattern="test*.py")
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = reportpath + "\\" + now + "自动化测试结果.html"
    fp = open(filename,"wb")
    runner = HTMLTestRunner(stream=fp,title="测试报告",description="用例执行情况")
    runner.run(case)

    fp.close()
if __name__ =="__main__":
    run()