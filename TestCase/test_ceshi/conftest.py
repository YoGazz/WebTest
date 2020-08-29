# -*- coding:utf-8  -*-
#@Time      :2020/8/27 22:05
#@Author    : Sun
#@File      :conftest.py

import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from Common.base import BasePage

driver = None

@pytest.fixture(scope='class', autouse=True)
def drivers(request):
    global driver
    if driver is None:
        #设置selenium无界面模式
        opt = webdriver.ChromeOptions()
        opt.set_headless()
        # 专门应对无头浏览器中不能最大化屏幕的方案
        opt.add_argument("--window-size=1920,1050")
        driver = webdriver.Chrome(options=opt)

    def fn():
        driver.quit()

    request.addfinalizer(fn)
    return driver
