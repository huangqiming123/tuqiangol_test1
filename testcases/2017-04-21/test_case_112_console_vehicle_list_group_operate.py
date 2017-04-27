import csv
import unittest

import pymysql

from automate_driver.automate_driver import AutomateDriver
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.base.base_page import BasePage
from pages.console.console_page import ConsolePage
from pages.dev_manage.dev_manage_page import DevManagePage

from pages.login.login_page import LoginPage


# 控制台-车辆列表-分组操作（新增，修改，删除）

# author:孙燕妮

class TestCase112ConsoleVehicleListGroupOperate(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.dev_manage_page = DevManagePage(self.driver, self.base_url)
        self.console_page = ConsolePage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.driver.set_window_max()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_console_vehicle_list_group_operate(self):
        '''测试控制台-车辆列表-分组操作（新增，修改，删除）'''

        # 打开途强在线首页-登录页
        self.base_page.open_page()

        # 登录
        self.login_page.user_login("test_007", "jimi123")

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

        # 折叠默认组
        self.console_page.fold_default_group()

        # 获取当前分组总数
        group_num_01 = self.console_page.count_group_num()

        # 取消新增分组
        self.console_page.dis_add_group("测试")
        self.driver.wait(1)

        # 新增分组
        self.console_page.add_group("测试测试")
        self.driver.wait(1)

        # 获取当前分组总数
        group_num_02 = self.console_page.count_group_num()

        # 验证是否成功新增分组
        self.assertEqual(group_num_01 + 1, group_num_02, "分组新增失败")

        # 修改分组
        self.console_page.edit_group("test_test")

        # 获取操作状态
        status = self.console_page.get_edit_group_status()

        # 验证是否操作成功
        self.assertIn("操作成功", status, "操作失败")

        # 删除分组

        self.console_page.del_group()

        # 获取当前分组总数
        group_num_03 = self.console_page.count_group_num()

        # 验证是否删除成功
        self.assertEqual(group_num_02 - 1, group_num_03, "删除分组失败")

        # 退出登录
        self.account_center_page_navi_bar.usr_logout()
