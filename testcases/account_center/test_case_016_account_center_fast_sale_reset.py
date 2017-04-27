import csv
import unittest

from automate_driver.automate_driver import AutomateDriver
from model.connect_sql import ConnectSql
from pages.account_center.account_center_details_page import AccountCenterDetailsPage
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.account_center.account_center_operation_log_page import AccountCenterOperationLogPage
from pages.account_center.account_center_page_read_csv import AccountCenterPageReadCsv
from pages.account_center.search_sql import SearchSql
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.login.login_page import LoginPage


# 账户中心-账户详情-快捷销售-删除设备、重置
# author:孙燕妮

class TestCase016AccountCenterFastSaleReset(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.account_center_page_operation_log = AccountCenterOperationLogPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.account_center_page_details = AccountCenterDetailsPage(self.driver, self.base_url)
        self.driver.set_window_max()
        self.account_center_page_read_csv = AccountCenterPageReadCsv()
        self.connect_sql = ConnectSql()
        self.search_sql = SearchSql()
        self.log_in_base = LogInBase(self.driver, self.base_page)
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_account_center_fast_sale_reset(self):
        '''通过csv测试账户详情-快捷销售-删除设备、重置功能'''
        csv_file = self.account_center_page_read_csv.read_csv('fast_sale_exact_find_and_sale.csv')
        csv_data = csv.reader(csv_file)

        # 打开途强在线首页-登录页
        self.base_page.open_page()
        # 登录账号
        self.log_in_base.log_in()
        self.driver.wait()

        for row in csv_data:
            search_account = {
                "account": row[0],
                "device_imei": row[1],
                "imei_count": row[2],
                "selected_dev": row[2],
                "account_expired_time": row[3]
            }
            # 进入快捷销售页面
            self.account_center_page_details.fast_sales()
            # 查找账户
            self.account_center_page_details.fast_sales_find_account(search_account["account"])
            # 输入设备imei精确查找设备并添加
            self.account_center_page_details.fast_sales_find_and_add_device(search_account["device_imei"])
            # 验证已选设备计数是否准确
            dev_num = self.account_center_page_details.get_selected_device_num()
            expect_dev_num = search_account["selected_dev"]
            self.assertEqual(expect_dev_num, dev_num, "已选设备个数不准确")
            # 删除列表中的设备
            self.account_center_page_details.delete_list_device()
            # 重置
            self.account_center_page_details.reset_device()
        csv_file.close()
        # 退出登录
        self.account_center_page_navi_bar.usr_logout()
