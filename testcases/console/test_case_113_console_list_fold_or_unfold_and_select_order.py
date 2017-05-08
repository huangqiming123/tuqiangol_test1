import unittest
from time import sleep

from automate_driver.automate_driver_server import AutomateDriverServer
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage

from pages.base.base_page_server import BasePageServer

from pages.base.lon_in_base_server import LogInBaseServer
from pages.console.console_page import ConsolePage

from pages.dev_manage.dev_manage_page import DevManagePage


# 控制台-列表折叠/展开、车辆列表排序方式选择

# author:孙燕妮

class TestCase113ConsoleListFoldOrUnfoldAndSelectOrder(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriverServer()
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.dev_manage_page = DevManagePage(self.driver, self.base_url)
        self.console_page = ConsolePage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.log_in_base = LogInBaseServer(self.driver, self.base_url)
        self.driver.set_window_max()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_console_list_fold_or_unfold_and_select_order(self):
        '''测试控制台-列表折叠/展开、车辆列表排序方式选择'''

        # 打开途强在线首页-登录页
        self.base_page.open_page()

        # 登录
        self.log_in_base.log_in()

        # 获取当前窗口句柄
        account_center_handle = self.driver.get_current_window_handle()

        # 点击进入控制台
        self.dev_manage_page.enter_console()

        # 获取当前所有窗口句柄
        all_handles = self.driver.get_all_window_handles()
        for handle in all_handles:
            if handle != account_center_handle:
                # 切换到账户中心窗口
                self.driver.switch_to_window(account_center_handle)
                self.driver.wait(1)
                # 关闭账户中心窗口
                self.driver.close_current_page()
                # 回到控制台窗口
                self.driver.switch_to_window(handle)
                self.driver.wait()

        # 选择排序方式
        sleep(3)
        # 点击收起客户列表
        self.console_page.cust_list_fold_or_unfold()
        self.driver.wait(1)
        # 截图
        self.driver.insert_img("客户列表收起截图")
        self.driver.wait(1)

        # 点击展开客户列表
        self.console_page.cust_list_fold_or_unfold()

        # 点击收起车辆列表
        self.console_page.dev_list_fold_or_unfold()
        self.driver.wait(1)
        # 截图
        self.driver.insert_img("车辆列表收起截图")
        self.driver.wait(1)

        # 点击展开车辆列表
        self.console_page.dev_list_fold_or_unfold()
        self.driver.wait(1)

        # 退出登录
        self.account_center_page_navi_bar.usr_logout()
