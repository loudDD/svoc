<<<<<<< HEAD
# _*_ coding:utf-8 _*_
import configparser
filename="C:/Users/DD/PycharmProjects/FastTest/config/config.ini"
class readConfig():
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(filename,encoding="utf-8")
=======
import configparser

class readConfig():
    def __init__(self,filename):
        self.cf = configparser.ConfigParser()
        self.cf.read(filename)
>>>>>>> 18e09ec6ee5064675d078c4efa307a9bd20baf60
    def getconfigvalue(self,section,name):
        value = self.cf.get(section,name)
        return value


