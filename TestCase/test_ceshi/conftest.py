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
        driver = webdriver.Chrome()
        # driver.maximize_window()

    def fn():
        driver.quit()

    request.addfinalizer(fn)
    return driver
