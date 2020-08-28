# -*- coding:utf-8  -*-
#@Time      :2020/8/26 22:13
#@Author    : Sun
#@File      :logger.py

"""
封装log方法
1、logger： 提供日志接口，供应用程序调用。logger最常用的操作有两大类：配置和发送日志消息。
2、handler：将日志记录发送到合适的目的，比如文件、socket等等。一个logger对象可以通过addhandler方法添加0到N个handler，每个hangdler又可以定义不同的日志级别，以实现日志分级过滤。
3、filter：提供了一种优雅的方式决定一个日志记录是否发送到handler。
4、formatter：指定日志记录的输出格式。formatter的构造方法需要两个参数：消息的格式字符串和日期字符串，这两个参数是可选的。
"""

import logging
import os
import time
from Config.conf import LOG_PATH

# curpath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# logpath = os.path.join(curpath,'Log')
# print(logpath)
if not os.path.exists(LOG_PATH):os.mkdir(LOG_PATH)

class Mylog:
    def __init__(self):
        #日志文件命名
        self.logname = os.path.join(LOG_PATH,'%s.log'%time.strftime('%Y-%m-%d %H-%M-%S'))
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        #日志输出格式
        self.format = logging.Formatter(("%(asctime)s - %(filename)s -  %(levelname)s - %(message)s"))

    def console(self,level,message):
        #创建一个FileHandler，用于写到本地
        fh = logging.FileHandler(self.logname,'a',encoding='utf_8')
        fh.setLevel(logging.INFO)
        fh.setFormatter(self.format)
        self.logger.addHandler(fh)

        #创建一个StreamHandler 用于输出到控制台
        sh = logging.StreamHandler()
        sh.setLevel(logging.DEBUG)
        sh.setFormatter(self.format)
        self.logger.addHandler(sh)

        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        #这两行是为了避免日志输出重复问题
        self.logger.removeHandler(fh)
        self.logger.removeHandler(sh)
        fh.close()

    def debug(self,message):
        self.console('debug',message)

    def info(self,message):
        self.console('info',message)

    def warning(self,message):
        self.console('warning',message)

    def error(self,message):
        self.console('error',message)

if __name__ == '__main__':
    Mylog().info('这个是debug信息')