import unittest
from time import sleep

from automate_driver.automate_driver_server import AutomateDriverServer
from model.assert_text import AssertText
from model.connect_sql import ConnectSql
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.account_center.account_center_operation_log_page import AccountCenterOperationLogPage
from pages.account_center.account_center_page_read_csv import AccountCenterPageReadCsv
from pages.account_center.search_sql import SearchSql
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer


# 帮助栏 业务日志 客户管理分页功能

class TestCase42CustManagerPaging(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriverServer()
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.log_in_base = LogInBaseServer(self.driver, self.base_url)
        self.account_center_page_operation_log = AccountCenterOperationLogPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.connect_sql = ConnectSql()
        self.account_center_page_read_csv = AccountCenterPageReadCsv()
        self.search_sql = SearchSql()
        self.assert_text = AssertText()
        self.driver.set_window_max()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_case_016_cust_manager_paging(self):
        self.base_page.open_page()
        self.log_in_base.log_in_jimitest()
        self.log_in_base.click_account_center_button()
        # 点击招呼栏-业务日志
        self.account_center_page_operation_log.click_help_button()
        self.account_center_page_operation_log.click_business_log()
        # 判断当前页面是否正确跳转至业务日志页面
        expect_url = self.base_url + "/userFeedback/toHelp"
        self.assertEqual(expect_url, self.driver.get_current_url(), "当前页面跳转错误")

        # 点击客户管理
        self.account_center_page_operation_log.log_cust_modify()

        # 选择条件搜索
        self.account_center_page_navi_bar.switch_to_cust_oper_frame()
        sleep(10)
        # 获取页面有多少页
        page_number = self.account_center_page_operation_log.count_cust_busi_log_numss()
        if page_number == 0:
            self.assertIn(self.assert_text.account_center_page_no_data_text(),
                          self.account_center_page_navi_bar.get_no_data_in_cust_manage())

        elif page_number == 1:
            self.assertEqual('active', self.account_center_page_navi_bar.get_up_page_class_name_in_cust_manage())
            self.assertEqual('active', self.account_center_page_navi_bar.get_next_page_class_name_in_cust_manage())

        else:
            # 循环点击每一页
            for n in range(page_number):
                self.account_center_page_navi_bar.click_per_page_in_dev_oper(n)
                if (n + 1) < page_number:
                    self.assertEqual(10, self.account_center_page_navi_bar.get_per_page_in_cust_oper())

        # 分别点击每页 20 30 50 和 100
        sleep(2)
        # self.account_center_page_navi_bar.click_per_numbers_in_dev_operation()
