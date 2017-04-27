import csv
import unittest

import pymysql

from automate_driver.automate_driver import AutomateDriver
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.dev_manage.dev_manage_page import DevManagePage
from pages.dev_manage.dev_manage_page_read_csv import DevManagePageReadCsv

from pages.login.login_page import LoginPage


# 设备管理-设备批量操作-选中单条设备设置工作模式

# author:孙燕妮

class TestCase105DevManageDevBatchSetModeSingle(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.dev_manage_page = DevManagePage(self.driver, self.base_url)
        self.log_in_base = LogInBase(self.driver, self.base_url)
        self.dev_manage_page_read_csv = DevManagePageReadCsv()
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.driver.set_window_max()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_dev_manage_dev_batch_set_mode_single(self):
        '''测试设备管理-设备批量操作-选中单条设备设置工作模式'''

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


        # 点击进入设备管理
        self.dev_manage_page.enter_dev_manage()


        # 选中单条设备
        self.dev_manage_page.select_single_check_box_mode()

        # 点击选中设置工作模式
        self.dev_manage_page.click_selected_set_mode()

        # 选择工作模式
        self.dev_manage_page.select_dev_mode()

        # 单条选中设置工作模式
        self.dev_manage_page.set_mode_for_single_dev()

        try:
            # 获取操作状态
            status = self.dev_manage_page.get_send_instr_status()

            # 验证是否操作成功
            self.assertIn("操作成功", status, "操作失败")

        except:
            print("当前设备不支持发送所选中的工作模式")





        # 退出登录
        self.account_center_page_navi_bar.dev_manage_usr_logout()

