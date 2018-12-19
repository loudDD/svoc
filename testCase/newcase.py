"""通过遍历excel中没行的值，生成另类测试用例。缺陷：所有结果在一条用例中"""

import unittest

from svoc.page.basepage import POM
from svoc.readExcel.readexcel import readExcel
from svoc.config.readconfig import readConfig

casepath = readConfig().getconfigvalue("path","casepath")


baseact = POM()


class Test(unittest.TestCase):
    """
    继承unittest
    """
    zuozhe="david"

    def demo(self,i):
        def case(i):
            #测试用例
            print(i)
            # setattr(case,'__doc__',str[i])
            return case


def test_all(self,line):
    for i in range(1,line):
        # runorno = str(readExcel().getrunOrno(i))
        # if runorno == "no":
        #     continue
        setattr(Test, 'test_'+str(i+1), Test.demo(i))
        Test.demo(self,i)


if __name__== "__main__":
    lines = readExcel().get_lines()
    print(lines)
    # testall(lines)
    testall(lines)
    suit = unittest.TestSuite(unittest.makeSuite(testall(lines)))
    fp = open("123.html","wb")
    runner = unittest.TextTestRunner(fp)
    runner.run(suit)
    fp.close()
