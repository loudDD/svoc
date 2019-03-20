"""读取config.ini文件：先得到项目根目录，再合成各种路径写到ini文件中"""
# _*_ coding:utf-8 _*_
import configparser
import os

projectpath = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
configpath = os.path.join(projectpath, r"public\config.ini")


class readConfig():
    """定义类"""
    def __init__(self):
        """初始化，并写ini文件"""
        self.cf = configparser.ConfigParser()
        self.cf.read(configpath)

        self.cf.set("path", "xlrdpath", os.path.join(projectpath, r"excel\testcases.xlsx"))
        self.cf.set("path", "casepath", os.path.join(projectpath, r"testCase"))
        self.cf.set("path", "reportpath", os.path.join(projectpath, r"report"))
        self.cf.write(open(configpath, "r+"))
    def getconfigvalue(self, section, name):
        """根据section和value获得值"""
        value = self.cf.get(section, name)
        return value
