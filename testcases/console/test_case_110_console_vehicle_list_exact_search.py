import csv
import unittest

import pymysql

from automate_driver.automate_driver import AutomateDriver
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.console.console_page import ConsolePage
from pages.console.console_page_read_csv import ConsolePageReadCsv
from pages.dev_manage.dev_manage_page import DevManagePage

from pages.login.login_page import LoginPage


# 控制台-车辆列表-精确搜索

# author:孙燕妮

class TestCase110ConsoleVehicleListExactSearch(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.dev_manage_page = DevManagePage(self.driver, self.base_url)
        self.console_page = ConsolePage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.log_in_base = LogInBase(self.driver, self.base_url)
        self.console_page_read_csv = ConsolePageReadCsv()
        self.driver.set_window_max()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_console_vehicle_list_exact_search(self):
        '''测试控制台-车辆列表-精确搜索'''

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

        csv_file = self.console_page_read_csv.read_csv('search_dev_by_imei.csv')
        csv_data = csv.reader(csv_file)

        for row in csv_data:
            search_info = {
                "user": row[0],
                "imei": row[1]
            }

            # 客户列表搜索客户user
            self.console_page.search_user(search_info["user"])

            # 车辆列表输入imei搜索设备
            self.console_page.search_dev(search_info["imei"])

            # 获取搜索结果id--imei
            imei = self.console_page.get_dev_imei_search_result()

            # 验证获取的imei与搜素输入的imei是否一致
            self.assertEqual(search_info["imei"], imei, "获取的imei与搜素输入的imei不一致")

        csv_file.close()

        # 退出登录
        self.account_center_page_navi_bar.usr_logout()
