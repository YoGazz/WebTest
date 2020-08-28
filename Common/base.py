# -*- coding:utf-8  -*-
#@Time      :2020/8/26 22:00
#@Author    : Sun
#@File      :base.py

import os
import time
import allure
import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from Common.logger import Mylog
from Config.conf import SCREENSHOT_DIR


"""
selenium基类
本文件存放了selenium基类的封装方法
"""


class BasePage:
    def __init__(self,driver:webdriver.Chrome):
        # 必须外部传入driver  同一个driver经历多个页面
        '''
        二次封装
        1、封装基本函数--执行日志、异常处理、失败截图
        2、所有页面公有的部分
        3、与业务无关
        '''
        self.log = Mylog()
        self.driver = driver
        self.time = 10
        self.timeout = 1

    def get_url(self, url):
        """打开网址并验证"""
        self.driver.maximize_window()
        self.driver.set_page_load_timeout(60)
        try:
            self.driver.get(url)
            self.driver.implicitly_wait(10)
            self.log.info("打开网页：%s" % url)
        except TimeoutException:
            raise TimeoutException("打开%s超时请检查网络或网址服务器" % url)

    def save_screenshot(self,doc=""):
        """
             截图操作
             1.图片名称:模块名_页面名称_操作名称_年-月-日_时分秒.png
             2.filepath=指的图片保存目录/model(页面功能名称)_当前时间到秒.png
        """
        # Projectpath = os.path.dirname(os.path.dirname(__file__))
        # screenpath = Projectpath + '/Screenshots/'
        if not os.path.exists(SCREENSHOT_DIR):os.mkdir(SCREENSHOT_DIR)
        rq = time.strftime('%Y-%m-%d %H-%M-%S')
        screenname = SCREENSHOT_DIR + doc + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screenname)
            with open(screenname,mode='rb') as f:
                file = f.read()
            allure.attach(file,doc,allure.attachment_type.PNG)
            self.log.info(f'开始截图保存，保存路径{SCREENSHOT_DIR}')
        except Exception as e:
            self.log.error(f'截图出现异常，{e}')


    def wait_element(self,locator,doc=''):
        self.log.info(f'等待元素{locator}可见')
        try:
            time_start = datetime.datetime.now()
            WebDriverWait(self.driver,self.timeout,self.time).until(EC.presence_of_element_located(locator))
            time_end = datetime.datetime.now()
            time_wait = (time_end - time_start).seconds
            self.log.info(f'{doc}:元素{locator}可见，等待时长为{time_wait}')
        except:
            self.log.error('等待元素失效')
            self.save_screenshot(doc)
            raise


    def find(self,locator,doc=''):
        '''定位到元素，返回元素对象，未定为到，Timeout返回异常，locator必须传元祖类型:('id','kw')'''
        self.log.info(f'{doc}:查找元素:{locator}')
        try:
            ele = WebDriverWait(self.driver,self.time,self.timeout).until(lambda x:x.find_element(*locator))
            return ele
        except:
            self.log.error("查找元素失败")
            self.save_screenshot(doc)
            raise

    def finds(self,locator,doc=''):
        '''定位到元素，返回元素对象，未定为到，Timeout返回异常，locator必须传元祖类型:('id','kw')'''
        self.log.info(f'{doc}:查找元素:{locator}')
        try:
            eles = WebDriverWait(self.driver,self.timeout,self.t).until(lambda x:x.find_elements(*locator))
            return eles
        except:
            self.log.error("查找元素失败")
            self.save_screenshot(doc)
            raise


    #输入操作
    def send(self,locator,text,doc=''):
        ele = self.find(locator,doc)
        self.log.info(f'{doc}:元素{locator}中输入{text}')
        try:
            ele.clear()
            ele.send_keys(text)
        except:
            self.log.error('输入操作失败')
            self.take_screenshot(doc)
            raise

    #清除操作
    def clear(self,locator,doc=''):
        ele = self.find(locator,doc)
        self.log.info(f'{doc}清除元素：{locator}')
        try:
            ele.clear()
        except:
            self.log.error('清除操作元素失败')
            self.take_screenshot(doc)
            raise

    def click(self,locator,doc=''):
        ele = self.find(locator,doc)
        self.log.info(f'{doc}:点击元素{locator}')
        try:
            ele.click()
        except:
            self.log.error('点击元素操作失败')
            self.take_screenshot(doc)
            raise


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('http://58.87.64.140:8088/zentao/user-login-L3plbnRhby8=.html')

    #
    base = BasePage(driver)
    user_ele = (By.CSS_SELECTOR, '#account')
    password_ele = (By.CSS_SELECTOR, '[name="password"]')
    submit_ele = (By.CSS_SELECTOR, '#ubmit')
    base.send(user_ele, 'hahah', "登录页面_登录操作")
    base.send(password_ele, 'Zbj2495550.', "登录页面_登录操作")
    base.click(submit_ele, "登录页面_登录操作")



