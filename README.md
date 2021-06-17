# web-UI 自动化测试示例

---

## 框架设计

- pytest
- selenium
- POM 模型

---

## 目录结构

    Common                 ——公共类
    Config                 ——各种固定配置
    Data                   ——测试数据存放路径
    TestCase               ——测试用例
    conf.py                ——各种固定配置
    conftest.py            ——pytest胶水文件
    pytest.ini             ——pytest配置文件

---

## 运行

- `cd 项目目录`

* MacOS 系统或 Linux 系统

- 在命令行输入`sh run_mac.sh`即可运行

* Windows 系统

- 在命令行输入`run_mac.bat`即可运行


# allure参数说明


- allure --alluredir

- allure generate
    - -c 生成报告前删除上一次生成的报告
    - -o 指定生成的报告目录
- allure open


### Python+Selenium+pytest+allure(Page Object模式)

#### 为什么要搭建这个框架

- 目前工作中有很多重复性的工作，我希望吧这个框架应用到实际项目，更高效的完成自己的任务
- 为了以后工作在需要时，方便我使用

#### 什么是page object？为什么要使用page object？

- Page Object模式，创建一个对象来对应页面的一个应用。因此，我们可以为每个页面定义一个类，并为每个页面的属性和操作构建模型。这就相当于在测试脚本和被测的页面功能中分离出一层，屏蔽了定位器、底层处理元素的方法和业务逻辑，取而代之的是，Page Object会提供一系列的API来处理页面功能

#### page obeject分层设计好处：
- 底层封装，避免重复代码，减少代码量
- 页面层元素抓取，单个页面写一个脚本（模块），修改元素定位方便，便于元素定位的维护工作
- 用例层只做用例设计的事情，调用page页面模块的方法，简单粗暴
- 可以便于多人同时并行开发工作，也可以调用别人写的page页面模块
