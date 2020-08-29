# -*- coding:utf-8  -*-
#@Time      :2020/8/27 21:47
#@Author    : Sun
#@File      :bugpage.py

import time
from Common.base import BasePage
from selenium.webdriver.common.by import By

class BugPage(BasePage):
    Doc = '测试模块--提交Bug功能--'
    test_ele = (By.XPATH,'//*[@id="mainmenu"]/ul/li[4]/a')
    bug_ele = (By.XPATH,'//*[@id="modulemenu"]/ul/li[2]/a')
    submitbug_ele = (By.XPATH,'//*[@id="createActionMenu"]/a')
    products_ele = (By.XPATH,'//*[@id="product_chosen"]/a/span')
    modules_ele = (By.CSS_SELECTOR,'#module_chosen')
    modules_chose_ele = (By.XPATH,'//*[@id="module_chosen"]/div/ul/li[5]')
    projects_ele = (By.CSS_SELECTOR,'#project_chosen')
    chose_project_ele = (By.XPATH,'//*[@id="project_chosen"]/div/ul/li')
    banben_ele = (By.CSS_SELECTOR,'#openedBuild_chosen')
    chose_ele = (By.XPATH,'//*[@id="openedBuild_chosen"]/div/ul/li')
    datetime_ele = (By.CSS_SELECTOR,'#deadline')
    bugtitle_ele = (By.CSS_SELECTOR,'#title')
    buggrade_ele= (By.XPATH,'//*[@id="dataform"]/table/tbody/tr[5]/td/div/div[2]/div/div[1]/button')
    chose_buggrade01_ele = (By.XPATH, '//*[@id="dataform"]/table/tbody/tr[5]/td/div/div[2]/div/div[1]/ul/li[1]/a/span')
    chose_buggrade02_ele = (By.XPATH, '//*[@id="dataform"]/table/tbody/tr[5]/td/div/div[2]/div/div[1]/ul/li[2]/a/span')
    chose_buggrade03_ele = (By.XPATH, '//*[@id="dataform"]/table/tbody/tr[5]/td/div/div[2]/div/div[1]/ul/li[3]/a/span')
    chose_buggrade04_ele = (By.XPATH, '//*[@id="dataform"]/table/tbody/tr[5]/td/div/div[2]/div/div[1]/ul/li[4]/a/span')
    bug_content = (By.XPATH,'/html/body/p[1]')
    save_ele = (By.CSS_SELECTOR,'#submit')
    ceshi_ele = (By.CSS_SELECTOR,'#active')
    title_ele = (By.XPATH,'//*[@id="bugList"]/tbody/tr/td[4]/a')

    def submit_bug(self,titel):
        self.click(self.test_ele,doc=self.Doc)
        self.click(self.bug_ele,doc=self.Doc)
        self.click(self.submitbug_ele,doc=self.Doc)
        self.click(self.modules_ele,doc=self.Doc)
        self.click(self.modules_chose_ele,doc=self.Doc)
        # self.click(self.products_ele,doc=self.Doc)
        # self.click(self.chose_project_ele,doc=self.Doc)
        self.click(self.banben_ele,doc=self.Doc)
        self.click(self.chose_ele,doc=self.Doc)
        self.click(self.datetime_ele,doc=self.Doc)
        self.send(self.bugtitle_ele,titel,doc=self.Doc)
        self.click(self.buggrade_ele,doc=self.Doc)
        self.click(self.chose_buggrade01_ele,doc=self.Doc)
        # self.driver.switch_to_frame(self.driver.find_element_by_class_name('//*[@id="dataform"]/table/tbody/tr[6]/td/div[2]/div[2]/iframe'))
        # self.send(self.bug_content,content,doc=self.Doc)
        # self.driver.switch_to_default_content()
        self.click(self.save_ele)

    def submitbug_result(self,title):
        try:
            r = self.find(self.title_ele).text
            assert r == title
            return title
        except:
            return False

