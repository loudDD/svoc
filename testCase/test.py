import unittest
from time import sleep
from svoc.page.basepage import POM
from svoc.config.readconfig import readConfig
from svoc.readExcel.readexcel import readExcel


lines = readExcel().get_lines()
baseact = POM()

class testsvoc(unittest.TestCase):
    def setUp(self):
        print("测试开始")
    def test_svoc(self):

        for i in range(1,lines):
            number = int(readExcel().getnum(i))
            title = str(readExcel().gettitle(i))
            action = str(readExcel().getact(i))
            typ = str(readExcel().gettype(i))
            data = str(readExcel().getdata(i))
            time = int(readExcel().gettime(i))
            text = readExcel().getvalue(i)
            if type(text)==float:
                text = str(round(readExcel().getvalue(i)))
            expect = str(readExcel().getexpect(i))
            print(text)
            print(type(text))
            if action == "send_keys":
                element = baseact.findelement(typ,data)
                baseact.send_keys(element,text)
                result = ""
                if result == expect:
                    print("用例%s" %( number) + title + "测试结果:" + "测试通过" )
                else:
                    print("用例%s" % (number) + title + "测试结果:" + "测试失败")
            elif action == "click":
                element = baseact.findelement(type,data)
                baseact.click(element)
                result = ""
                if result == expect:
                    print("用例%s" %( number) + title + "测试结果:" + "测试通过" )
                else:
                    print("用例%s" % (number) + title + "测试结果:" + "测试失败")
            else:
                print("方法未识别")
            sleep(time)

            sleep(3)

