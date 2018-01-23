import unittest
from automate_driver.automate_driver_server import AutomateDriverServer
from pages.account_center.user_center import UserCenterPage
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer
from pages.login.login_page import LoginPage

__author__ = ''

class TestCase211UserCenterLogout(unittest.TestCase):
    # 测试退出登录
    def setUp(self):
        self.driver = AutomateDriverServer()
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.log_in_base = LogInBaseServer(self.driver, self.base_page)
        self.user_center_page = UserCenterPage(self.driver, self.base_url)
        self.driver.set_window_max()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_user_center_logout(self):
        self.base_page.open_page()
        self.log_in_base.log_in()

        # 点击退出登录
        self.user_center_page.click_user_center_button()
        # 点击退出登录按钮
        self.user_center_page.click_logout_button()
        # 点击取消
        self.user_center_page.click_cancel_button()

        # 点击退出登录
        self.user_center_page.click_user_center_button()
        # 点击退出登录按钮
        self.user_center_page.click_logout_button()
        # 点击取消
        self.user_center_page.click_close_button()

        # 点击退出登录
        self.user_center_page.click_user_center_button()
        # 点击退出登录按钮
        self.user_center_page.click_logout_button()
        # 点击取消
        self.user_center_page.click_ensure_button()
