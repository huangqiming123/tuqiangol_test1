import unittest
from automate_driver.automate_driver_server import AutomateDriverServer
from pages.base.base_page_server import BasePageServer
from pages.login.login_page import LoginPage


class TestCase108LoginTester(unittest.TestCase):
    # 测试体验账号
    def setUp(self):
        self.driver = AutomateDriverServer()
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.driver.set_window_max()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_log_in_tester(self):
        # 打开页面
        self.base_page.open_page()
        # 点击体验账号
        self.login_page.click_tester_button()
        # 断言url
        actual_url = self.driver.get_current_url()
        expect_url = self.base_url + "/nomalUserCenter"
        self.assertEqual(expect_url, actual_url, "登录成功后页面跳转错误")

        # 断言登录的账号
        user_account = self.login_page.get_user_account_tester()
        self.assertEqual('taste', user_account)

        # 点击个人中心
        self.login_page.click_user_center()
        # 点击退出系统
        self.login_page.click_log_out_system()
        # 点击确定
        self.login_page.click_ensure()

        self.assertEqual(self.base_url + "/", self.driver.get_current_url(), "退出系统失败")
