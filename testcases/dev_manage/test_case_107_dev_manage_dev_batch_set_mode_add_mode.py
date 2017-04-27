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


# 设备管理-设备批量操作-设置工作模式-新建工作模板

# author:孙燕妮

class TestCase107DevManageDevBatchSetModeAddMode(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.dev_manage_page = DevManagePage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.log_in_base = LogInBase(self.driver, self.base_url)
        self.dev_manage_page_read_csv = DevManagePageReadCsv()
        self.driver.set_window_max()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_dev_manage_dev_batch_set_mode_add_mode(self):
        '''测试设备管理-设备批量操作-设置工作模式-新建工作模板'''

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

        # 全选设备
        self.dev_manage_page.select_all_check_box()

        csv_file = self.dev_manage_page_read_csv.read_csv('add_mode.csv')
        csv_data = csv.reader(csv_file)

        for row in csv_data:
            mode_info = {
                "model_name": row[0],
                "mode_type": row[1],
                "is_cycle": row[2],
                "cycle_time": row[3]
            }

            # 点击本次查询全部设置工作模式
            self.dev_manage_page.click_all_set_mode()

            self.driver.wait()

            # 新建工作模板
            self.dev_manage_page.add_mode(mode_info["model_name"], mode_info["mode_type"], mode_info["is_cycle"],
                                          mode_info["cycle_time"])

            # 添加自定义
            self.dev_manage_page.add_model_add_define()

            # 关闭设置工作模式弹框
            self.dev_manage_page.close_set_mode()

        csv_file.close()

        # 点击本次查询全部设置工作模式
        self.dev_manage_page.click_all_set_mode()

        self.driver.wait()

        # 进入工作模式模板管理
        self.dev_manage_page.mode_manage()

        # 删除新增模板
        self.dev_manage_page.del_mode()
        self.dev_manage_page.del_mode()

        # 退出登录
        self.account_center_page_navi_bar.dev_manage_usr_logout()
