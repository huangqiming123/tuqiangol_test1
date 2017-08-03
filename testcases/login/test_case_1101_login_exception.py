import unittest
from time import sleep

from automate_driver.automate_driver_server import AutomateDriverServer
from model.assert_text import AssertText
from model.connect_sql import ConnectSql
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.base.base_page_server import BasePageServer
from pages.login.log_in_page_read_csv import LogInPageReadCsv
from pages.login.login_page import LoginPage


# 验证异常登录
class TestCase1101LoginException(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriverServer()
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.log_in_read_csv = LogInPageReadCsv()
        self.connect_sql = ConnectSql()
        self.assert_text = AssertText()
        self.driver.set_window_max()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_case_101_login_exception(self):
        # 异常登录
        self.base_page.open_page()
        sleep(2)
        # 第一种 密码和账号都为空
        self.login_page.account_input('')
        self.login_page.password_input('')
        self.login_page.login_button_click()
        sleep(2)

        self.assertEqual(self.assert_text.log_in_page_account_or_password_not_null(),
                         self.login_page.get_exception_text())

        # 第二种 密码 和 账号一个不为空
        self.login_page.account_input('jimitest')
        self.login_page.password_input('')
        self.login_page.login_button_click()
        sleep(2)
        self.assertEqual(self.assert_text.log_in_page_account_or_password_not_null(),
                         self.login_page.get_exception_text())

        self.login_page.account_input('')
        self.login_page.password_input('jimi123')
        self.login_page.login_button_click()
        sleep(2)
        self.assertEqual(self.assert_text.log_in_page_account_or_password_not_null(),
                         self.login_page.get_exception_text())

        # 第三种 账号不存在
        self.login_page.account_input('fdsafasfd')
        self.login_page.password_input('jimi123')
        self.login_page.login_button_click()
        sleep(2)
        self.assertEqual(self.assert_text.log_in_page_account_not_exist(), self.login_page.get_exception_text())

        # 第四种 密码错误
        self.login_page.account_input('jimitest')
        self.login_page.password_input('jimi123222')
        self.login_page.login_button_click()
        sleep(2)
        self.assertEqual(self.assert_text.log_in_page_password_error(), self.login_page.get_exception_text())
