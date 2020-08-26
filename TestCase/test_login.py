# -*- coding:utf-8  -*-
#@Time      :2020/8/26 23:16
#@Author    : Sun
#@File      :test_login.py

from selenium import webdriver
from Page.loginpage import LoginPage
from Common.readyaml import ReadYaml
import pytest
import allure

# with open('./Data/login.yaml',encoding='utf_8') as f:
#     Logindata = yaml.safe_load(f)



@allure.feature('登录模块')
class TestLogin:
    '''
    测试登录功能
    '''
    ready = ReadYaml('login.yaml')
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://58.87.64.140:8088/zentao/user-login-L3plbnRhby8=.html')
        self.loginzentao = LoginPage(self.driver)

    def teardown(self):
        self.driver.quit()

    # @pytest.mark.parametrize('user,password',[
    #     ('admin','1234'),
    #     ('admin','45678'),
    #     ('admin','Zbj2495550.')
    # ])
    @allure.severity('blocker')
    @allure.story('输入用户名密码，登录')
    @pytest.mark.parametrize('user,password',ready.get_yaml_data())
    def test_login(self,user,password):
        self.loginzentao.login(user,password)
        result = self.loginzentao.login_result()
        print(f'获取到的结果是{result}')
        assert result

if __name__ == '__main__':
    pytest.main('-q')
