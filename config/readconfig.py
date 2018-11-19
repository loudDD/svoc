
# _*_ coding:utf-8 _*_
import configparser
import os

projectpath = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
configpath = os.path.join(projectpath, r"config\config.ini")


class readConfig():
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(configpath)

        self.cf.set("path", "xlrdpath", os.path.join(projectpath, r"excel\testcases.xlsx"))
        self.cf.set("path", "casepath", os.path.join(projectpath, r"testCase"))
        self.cf.set("path", "reportpath", os.path.join(projectpath, r"report"))
        self.cf.write(open(configpath,"r+"))
    def getconfigvalue(self,section,name):
        value = self.cf.get(section,name)
        return value


if __name__=="__main__":
    readConfig()