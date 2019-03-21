#定义日志方法

import logging
import os
import time
class Logger():
    def __init__(self,level):

        if level == "info":
            setloglevel = logging.INFO
        elif level == "debug":
            setloglevel = logging.DEBUG
        elif level == "warning":
            setloglevel = logging.WARNING
        elif level == "error":
            setloglevel = logging.ERROR
        elif level =="critical":
            setloglevel = logging.CRITICIAL
        #确定日志位置和名称
        self.filename = os.path.join("{0}.log".format(time.strftime("%Y-%m-%d")))
        self.logpath = os.path.join(os.path.abspath("../"),"log")
        self.path = os.path.join(self.logpath,self.filename)
        # print(self.path)
        #创建一个logger
        self.logger = logging.getLogger("David")
        # logging.basicConfig(level=logging.DEBUG,format='')

        self.logger.setLevel(logging.DEBUG)
        #创建一个handler,用于写入日志文件
        fh = logging.FileHandler(self.path)
        fh.setLevel(setloglevel)

        #创建一个handler,用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        #定义输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        #给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)


    def getLog(self):
        return self.logger

# logger = Logger('info').getLog()
# logger.debug("this is a debug message!")
# logger.info("this is a info message!")