import csv
import unittest

import pymysql

from automate_driver.automate_driver import AutomateDriver
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.base.base_page import BasePage
from pages.dev_manage.dev_manage_page import DevManagePage

from pages.login.login_page import LoginPage


# 设备管理-设备搜索-by imei

# author:孙燕妮

class TestCase086DevManageDevSearchByIMEI(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.dev_manage_page = DevManagePage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.driver.set_window_max()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_dev_manage_dev_search_by_imei(self):
        '''测试设备管理-设备搜索-by imei'''

        # 打开途强在线首页-登录页
        self.base_page.open_page()

        # 登录
        self.login_page.user_login("test_007", "jimi123")
        self.driver.wait()

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

        # 获取当前登录用户的设备列表中共有多少设备
        login_dev_num = self.dev_manage_page.get_login_acc_dev_stock()

        # 统计设备列表的设备总数
        login_dev_count = self.dev_manage_page.count_curr_dev_num()

        # 验证当前登录用户的设备数与库存数是否一致
        self.assertEqual(int(login_dev_num),login_dev_count,"当前登录用户的设备数与库存数不一致")


        csv_file = open(r"E:\git\tuqiangol_test\data\dev_manage\acc_select.csv",
                        'r',
                        encoding='utf8')
        csv_data = csv.reader(csv_file)

        for row in csv_data:
            select_info = {
                "account": row[0]
            }

            # 左侧客户列表中搜索客户并选中
            self.dev_manage_page.search_acc(select_info["account"])
            self.driver.wait()

            # 获取当前选中账户的库存
            stock_num = self.dev_manage_page.get_curr_acc_dev_stock()

            # 统计当前选中账户设备列表的设备个数
            stock_count = self.dev_manage_page.count_curr_dev_num()

            # 验证当前选中账户的设备数与库存数是否一致
            self.assertEqual(int(stock_num),stock_count,"当前选中账户的设备数与库存数不一致")


        csv_file.close()


        # 退出登录
        self.account_center_page_navi_bar.dev_manage_usr_logout()

