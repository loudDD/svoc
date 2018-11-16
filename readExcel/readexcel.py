import xlrd
from config.readconfig import readConfig

file = readConfig()
filepath = file.getconfigvalue("path","xlrdpath")

class readExcel():
    def __init__(self):
        self.file = xlrd.open_workbook(filepath)
        self.sheetname = self.file.sheet_by_index(0)
        self.rows = self.sheetname.get_rows()

    def get_lines(self):
        value = self.sheetname.nrows
        return value

    def getnum(self,row):
        # for i in self.rows:
        #     row = i
        #     value = self.sheetname.cell(row,col).value
        value = self.sheetname.cell(row,0).value
        return value
    def gettitle(self,row):
        value = self.sheetname.cell(row,1).value
        return value
    def getact(self,row):
        value = self.sheetname.cell(row,2).value
        return value
    def gettype(self,row):
        value = self.sheetname.cell(row,3).value
        return value
    def getdata(self,row):
        value = self.sheetname.cell(row,4).value
        return value
    def getvalue(self,row):
        value = self.sheetname.cell(row,5).value
        return value
    def getsleep(self,row):
        value = self.sheetname.cell(row,6).value
        return value
    def getrunOrno(self,row):
        value = self.sheetname.cell(row,7).value
        return value
    def getexpect(self,row):
        value = self.sheetname.cell(row,8).value
        return value

