"""通过遍历excel中没行的值，生成另类测试用例。缺陷：所有结果在一条用例中"""

import unittest
from time import sleep
from page.basepage import POM
from readExcel.readexcel import readExcel


lines = readExcel().get_lines()
baseact = POM()


class testsvoc(unittest.TestCase):
    """
    继承unittest
    """

    def setUp(self):
        print("测试开始")

    def test_svoc(self,):
        """测试用例
        """
        for i in range(1, lines):
            runorno = str(readExcel().getrunOrno(i))
            if runorno == "no":
                continue
            number = readExcel().getnum(i)
            title = str(readExcel().gettitle(i))
            action = str(readExcel().getact(i))
            typ = str(readExcel().gettype(i))
            data = str(readExcel().getdata(i))
            tim = readExcel().getsleep(i)

            text = readExcel().getvalue(i)

            if isinstance(text, float):
                text = str(round(readExcel().getvalue(i)))
            expect = str(readExcel().getexpect(i))
            if action == "send_keys":
                element = baseact.findelement(typ, data)
                baseact.send_keys(element, text)
                result = ""
                if result == expect:
                    print("用例%s"%(number) + title+"测试结果:" + "测试通过")
                else:
                    print("用例%s"%(number) + title + "测试结果:" + "测试失败")
            elif action == "click":
                element = baseact.findelement(typ, data)
                baseact.click(element)
                result = ""
                if result == expect:
                    print("用例%s"%(number) + title + "测试结果:" + "测试通过")
                else:
                    print("用例%s" % (number) + title + "测试结果:" + "测试失败")
            else:
                print("方法未识别")
            if tim == "":
                sleep(0)
            else:
                sleep(int(round(tim)))
