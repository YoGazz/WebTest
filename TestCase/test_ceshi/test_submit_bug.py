# -*- coding:utf-8  -*-
#@Time      :2020/8/27 22:25
#@Author    : Sun
#@File      :test_submit_bug.py
from Page.TestPage.bugpage import BugPage
from Page.loginpage import LoginPage
from Common.readconfig import ini
from selenium import webdriver
import pytest

class TestSubmitBug:

    @pytest.fixture(scope='function',autouse=True)
    def open_index(self,drivers,user='admin',password='Zbj2495550.'):
        self.loginzentao = LoginPage(drivers)
        self.loginzentao.get_url(ini.url)
        self.loginzentao.login(user,password)

    def test_submitbug(self,drivers,title='第四个bug'):
        self.bug = BugPage(drivers)
        self.bug.submit_bug(title)
        result = self.bug.submitbug_result(title)
        print(f'获取到的结果是{result}')
        assert result
