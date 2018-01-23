import unittest
from time import sleep

from automate_driver.automate_driver_server import AutomateDriverServer
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer
from pages.login.login_page import LoginPage

__author__ = ''

class TestCase105LoginWithRememberMe(unittest.TestCase):
    # 测试记住密码
    def setUp(self):
        self.driver = AutomateDriverServer()
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.log_in_base = LogInBaseServer(self.driver, self.base_url)
        self.driver.set_window_max()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_login_with_remember_me(self):
        # 打开途强在线首页-登录页
        self.base_page.open_page()
        self.log_in_base.log_in()
        # 点账户中心
        current_handle = self.driver.get_current_window_handle()
        self.account_center_page_navi_bar.click_account_center_button()
        self.base_page.change_windows_handle(current_handle)

        # 判断登录成功后跳转页面是否正确
        actual_url = self.driver.get_current_url()
        expect_url = self.base_url + "/customer/toAccountCenter"
        self.assertEqual(expect_url, actual_url, "登录成功后页面跳转错误")

        sleep(1)
        # 成功退出系统
        self.account_center_page_navi_bar.usr_logout()
        # 判断是否成功退出系统
        self.assertEqual(self.base_url + "/", self.driver.get_current_url(), "退出系统失败")
        # 验证退出系统后“记住我”是否是已勾选状态
        box_status = self.login_page.check_remember_me()
        self.assertEqual(True, box_status, '记住密码失败')

        # 点击登录按钮
        self.login_page.click_log_in_button()
        # 点账户中心
        current_handle = self.driver.get_current_window_handle()
        self.account_center_page_navi_bar.click_account_center_button()
        self.base_page.change_windows_handle(current_handle)

        actual_url = self.driver.get_current_url()
        expect_url = self.base_url + "/customer/toAccountCenter"
        self.assertEqual(expect_url, actual_url, "登录成功后页面跳转错误")

        # 再次退出
        # 成功退出系统
        self.account_center_page_navi_bar.usr_logout()
        # 判断是否成功退出系统
        self.assertEqual(self.base_url + "/", self.driver.get_current_url(), "退出系统失败")
        # 验证退出系统后“记住我”是否是已勾选状态
        box_status = self.login_page.check_remember_me()
        self.assertEqual(True, box_status, '记住密码失败')

        # 点击记住我的框，取消登录时记住我
        self.account_center_page_navi_bar.click_remember_me_button()
        box_status = self.login_page.check_remember_me()
        self.assertEqual(False, box_status, '记住密码失败')

        # 点击登录按钮
        self.login_page.click_log_in_button()
        # 点账户中心
        current_handle = self.driver.get_current_window_handle()
        self.account_center_page_navi_bar.click_account_center_button()
        self.base_page.change_windows_handle(current_handle)

        actual_url = self.driver.get_current_url()
        expect_url = self.base_url + "/customer/toAccountCenter"
        self.assertEqual(expect_url, actual_url, "登录成功后页面跳转错误")

        self.account_center_page_navi_bar.usr_logout()
        # 判断是否成功退出系统
        self.assertEqual(self.base_url + "/", self.driver.get_current_url(), "退出系统失败")
        # 验证退出系统后“记住我”是否是已勾选状态
        box_status = self.login_page.check_remember_me()
        self.assertEqual(False, box_status, '记住密码失败')
