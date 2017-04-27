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


# 控制台-当前选中客户设备的各类数据统计验证

# author:孙燕妮

class TestCase108ConsoleDevInfoCountWithSelectUser(unittest.TestCase):
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

    def test_console_dev_info_count_with_select_user(self):
        '''测试控制台-当前选中客户设备的各类数据统计验证'''

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

        csv_file = self.console_page_read_csv.read_csv('search_acc.csv')
        csv_data = csv.reader(csv_file)

        for row in csv_data:
            search_info = {
                "keyword": row[0]
            }

            # 客户列表搜索客户keyword
            self.console_page.search_user(search_info["keyword"])

            # 获取当前选中账户的库存
            dev_info = self.console_page.get_curr_acc_dev_info()
            dev_stock = dev_info["库存"]

            # 点击“全部”
            self.console_page.click_all()

            # 获取当前选中客户的设备列表“全部”设备数
            all_num = self.console_page.get_all_dev_num()

            # 验证库存与“全部”设备数是否一致
            self.assertEqual(int(dev_stock), all_num, "库存与“全部”设备数不一致")

            # 统计“全部”设备列表的设备总数
            count_all = self.console_page.count_all_group_dev()

            # 验证全部设备数与实际设备数是否一致
            self.assertEqual(all_num, count_all, "全部设备数与实际设备数不一致")

            # 点击“在线”
            self.console_page.click_online()

            # 获取当前登录账户的“在线”设备数
            online_num = self.console_page.get_online_dev_num()

            # 统计当前“在线”列表设备总数
            count_online = self.console_page.count_all_group_dev()

            # 验证在线设备数与实际在线设备数是否一致
            self.assertEqual(online_num, count_online, "在线设备数与实际在线设备数不一致")

            # 点击“离线”
            self.console_page.click_offline()

            # 获取当前登录账户的“离线”设备数
            offline_num = self.console_page.get_offline_dev_num()

            # 统计当前“离线”列表设备总数
            count_offline = self.console_page.count_all_group_dev()

            # 验证离线设备数与实际离线设备数是否一致
            self.assertEqual(offline_num, count_offline, "离线设备数与实际离线设备数不一致")

            # 点击“未激活”
            self.console_page.click_noactive()

            # 获取当前登录账户的“未激活”设备数
            noactive_num = self.console_page.get_noactive_dev_num()

            # 统计当前“未激活”列表设备总数
            count_noactive = self.console_page.count_all_group_dev()

            # 验证未激活设备数与实际未激活设备数是否一致
            self.assertEqual(noactive_num, count_noactive, "未激活设备数与实际未激活设备数不一致")

        csv_file.close()

        # 退出登录
        self.account_center_page_navi_bar.usr_logout()
