#定义日志方法

import logging
import os
import yaml

class Logger():
    def __init__(self):
        #创建一个logger
        self.logger = logging.getLogger(logger)
        path = os.path.join(os.path.abspath("./"),'config.yaml')
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                config = yaml.load(f)
                logging.config.dictConfig(config)
        else:
            logging.basicConfig(level=default_level)
        # logging.basicConfig(level=logging.DEBUG,format='')

        self.logger.setLevel(logging.DEBUG)
        #创建一个handler,用于写入日志文件
        fh = logging.FileHandler(logName)
        fh.setLevel(logging.DEBUG)

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

        self.logger.error(exc_info = True)

    def getLog(self):
        return self.logger

logger = Logger().getLog()
logger.debug("this is a debug message!")
logger.info("this is a info message!")