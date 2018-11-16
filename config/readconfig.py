
# _*_ coding:utf-8 _*_
import configparser
filename="C:/Users/DD/PycharmProjects/FastTest/config/config.ini"
class readConfig():
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(filename,encoding="utf-8")
    def getconfigvalue(self,section,name):
        value = self.cf.get(section,name)
        return value


