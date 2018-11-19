"""读取excel文件，通过函数固定获取个属性"""
import xlrd
from config.readconfig import readConfig

file = readConfig()
FILEPATH = file.getconfigvalue("path", "xlrdPath")


class readExcel():
    """定义类"""
    def __init__(self):
        """确定文件位置和sheet名称"""
        self.file = xlrd.open_workbook(FILEPATH)
        self.sheetname = self.file.sheet_by_index(0)
        self.rows = self.sheetname.get_rows()

    def get_lines(self):
        """获取excel总行数"""
        value = self.sheetname.nrows
        return value

    def getnum(self, row):
        """获取用例编号"""
        # for i in self.rows:
        #     row = i
        #     value = self.sheetname.cell(row,col).value
        value = self.sheetname.cell(row, 0).value
        return value

    def gettitle(self, row):
        """获取用例标题"""
        value = self.sheetname.cell(row, 1).value
        return value

    def getact(self, row):
        """获取操作"""
        value = self.sheetname.cell(row, 2).value
        return value

    def gettype(self, row):
        """获取定位方式"""
        value = self.sheetname.cell(row, 3).value
        return value

    def getdata(self, row):
        """获取定位元素"""
        value = self.sheetname.cell(row, 4).value
        return value

    def getvalue(self, row):
        """获取传入值,为空，则标识操作为click，test.py中判断"""
        value = self.sheetname.cell(row, 5).value
        return value

    def getsleep(self, row):
        """获取sleep时间"""
        value = self.sheetname.cell(row, 6).value
        return value

    def getrunOrno(self, row):
        """确定是否运行yes/no"""
        value = self.sheetname.cell(row, 7).value
        return value
    def getexpect(self, row):
        """获取预期结果，需更新"""
        value = self.sheetname.cell(row, 8).value
        return value
