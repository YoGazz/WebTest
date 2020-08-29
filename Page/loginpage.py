# -*- coding:utf-8  -*-
#@Time      :2020/8/26 22:52
#@Author    : Sun
#@File      :loginpage.py

from selenium import webdriver
from Common.base import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    Doc =  u'登录模块--登录功能--'
    user_ele = (By.CSS_SELECTOR,'#account')
    password_ele = (By.CSS_SELECTOR,'[name="password"]')
    submit_ele = (By.CSS_SELECTOR,'#submit')
    result_ele = (By.CSS_SELECTOR,'#userMenu > a')
    keep_login_ele = (By.CSS_SELECTOR,'#keepLoginon')
    forget_ele = (By.CSS_SELECTOR,'#login-form > form > table > tbody > tr:nth-child(4) > td > ')
    resufe_ele = (By.CSS_SELECTOR,'.btn')


    def set_name(self,user):
        # self.log.info('输入用户名')
        # self.wait_element(self.user_ele,doc=self.Doc)
        self.send(self.user_ele,user,doc=self.Doc)
        return self

    def set_password(self,password):
        # self.log.info('输入密码')
        self.send(self.password_ele,password,doc=self.Doc)
        return self

    def keep_login(self):
        self.click(self.keep_login_ele,doc=self.Doc)
        return self

    def forget_password(self):
        self.click(self.forget_ele,doc=self.Doc)
        return self

    def submit(self):
        # self.log.info('点击登录')
        self.click(self.submit_ele,doc=self.Doc)
        return self

    def login(self,user,password):
        self.set_name(user).set_password(password).keep_login().submit()
        return self

    def login_result(self):
        # self.log.info('获取登录结果')
        try:
            r = self.find(self.result_ele,doc=self.Doc).text
            print(f'当前登录用户为{r}')
            return r
        except:
            return False

    def forget(self):
        self.forget_password()
        return self

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('http://58.87.64.140:8088/zentao/user-login-L3plbnRhby8=.html')
    login = LoginPage(driver)
    login.set_name('admin3333')
    login.set_password('123')


