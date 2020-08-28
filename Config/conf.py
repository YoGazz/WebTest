# -*- coding:utf-8  -*-
#@Time      :2020/8/28 23:38
#@Author    : Sun
#@File      :conf.py

import os
from selenium.webdriver.common.by import By

#项目目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

#配置文件目录
INI_PATH = os.path.join(BASE_DIR,'Config','config.ini')

#报告目录
REPORT_PATH = os.path.join(BASE_DIR,'Report')
XML_PATH = os.path.join(REPORT_PATH,'xml')
HTML_PATH = os.path.join(REPORT_PATH,'html')

#截图目录
SCREENSHOT_DIR = os.path.join(BASE_DIR,'Screenshots/')

#日志目录
LOG_PATH = os.path.join(BASE_DIR,'Log')


if __name__ == '__main__':
    print(BASE_DIR)
    print(INI_PATH)
    print(SCREENSHOT_DIR)
