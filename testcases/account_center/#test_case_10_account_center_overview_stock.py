import unittest
from time import sleep

from automate_driver.automate_driver_server import AutomateDriverServer
from model.assert_text import AssertText
from model.connect_sql import ConnectSql
from pages.account_center.account_center_change_page import AccountCenterChangePage
from pages.account_center.account_center_details_page import AccountCenterDetailsPage
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer
from pages.login.login_page import LoginPage


# 账户中心-账户详情-账户总览  包括：库存
# author:zhangao

class TestCase10AccountCenterOverviewStock(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriverServer(choose='chrome')
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.account_center_page_details = AccountCenterDetailsPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.driver.set_window_max()
        self.connect_sql = ConnectSql()
        self.log_in_base = LogInBaseServer(self.driver, self.base_url)
        self.account_center_change_page = AccountCenterChangePage(self.driver, self.base_page)
        self.assert_text = AssertText()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_account_center_overview_stock(self):
        # 打开途强在线首页-登录页
        self.base_page.open_page()
        # 登录账号
        self.log_in_base.log_in()
        account = self.log_in_base.get_log_in_account()
        self.account_center_page_navi_bar.click_account_center_button()

        # 拖拽页面到库存显示的
        self.account_center_change_page.switch_kucun_dev_enable()
        self.account_center_change_page.switch_to_kucun_dev_frame()

        kucun_account = self.account_center_change_page.get_account_in_kuncun_frame()
        self.driver.default_frame()
