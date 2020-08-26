# -*- coding:utf-8  -*-
#@Time      :2020/8/27 01:29
#@Author    : Sun
#@File      :readyaml.py


import os
import yaml

class ReadYaml:
    def __init__(self,filename):
        projectPath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        self.filename = os.path.join(projectPath,'Data') + '/' + filename

    def get_yaml_data(self):
        with open(self.filename, mode='r', encoding='utf_8') as f:
            return yaml.safe_load(f)
if __name__ == '__main__':
    data = ReadYaml('login.yaml').get_yaml_data()
    print(data)

