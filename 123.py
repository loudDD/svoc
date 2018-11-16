
from readExcel.readexcel import readExcel
from page.basepage import POM
from selenium import webdriver



a = readExcel()
baseaction = POM()
line = a.get_lines()

for i in range(1,line):
    number = readExcel().getnum(i)
    title = readExcel().gettitle(i)
    action = str(readExcel().getact(i))
    typ = readExcel().gettype(i)
    data = readExcel().getdata(i)
    text = str(readExcel().getvalue(i))
    expect = readExcel().getexpect(i)

    if action =="send_keys":
        element = baseaction.findelement(typ, data)
        print(element)
        print(typ)
        print(data)
        print(text)
        baseaction.send_keys(element=element, text=text)


        result = ""
        if result == expect:
            print("用例%s" % (number) + title + "测试结果:" + "测试通过")
        else:
            print("用例%s" % (number) + title + "测试结果:" + "测试失败")
    elif action=="click":
        element = baseaction.findelement(typ, data)
        baseaction.click(element)
        result = ""
        if result == expect:
            print("用例%s" % (number) + title + "测试结果:" + "测试通过")
        else:
            print("用例%s" % (number) + title + "测试结果:" + "测试失败")
    else:
        print("方法未识别")
