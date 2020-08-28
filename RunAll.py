# -*- coding:utf-8  -*-
#@Time      :2020/8/26 21:59
#@Author    : Sun
#@File      :RunAll.py

import pytest
import allure
import os
from Config.conf import XML_PATH
from Config.conf import HTML_PATH


if __name__ == '__main__':
    args = ['-s','-q']
    pytest.main(args)
    args = ['-s', '--alluredir', XML_PATH]
    # pytest.main(args)
    # os.system(f'cp environment.properties {XML_PATH}')
    # os.system(f'allure generate {XML_PATH} -o {HTML_PATH} --clean')