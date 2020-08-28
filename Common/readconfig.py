# -*- coding:utf-8  -*-
#@Time      :2020/8/29 00:09
#@Author    : Sun
#@File      :readconfig.py
import os
import configparser
from Config.conf import INI_PATH


HOST = 'HOST'

class ReadConfig:
    '''配置文件'''
    def __init__(self):
        if not os.path.exists(INI_PATH):
            raise FileNotFoundError(f"配置文件{INI_PATH}不存在")
        self.config = configparser.RawConfigParser()    # 当有%的符号时请使用Raw读取
        self.config.read(INI_PATH, encoding="utf_8")

    def _get(self,section, option):
        '''获取'''
        return self.config.get(section, option)

    def _set(self,section, option, value):
        '''更新'''
        self.config.set(section, option, value)
        with open(INI_PATH,mode='w',encoding="utf_8") as f:
            self.config.write(f)

    @property
    def url(self):
        return self._get(HOST, HOST)

ini = ReadConfig()

if __name__ == '__main__':
    print(ini.url)





