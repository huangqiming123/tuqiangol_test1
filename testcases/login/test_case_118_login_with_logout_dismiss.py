import unittest
from automate_driver.automate_driver_server import AutomateDriverServer
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer
from pages.login.login_page import LoginPage


# 成功登录的用户取消退出
# author:孙燕妮

class TestCase003LoginWithLogoutDismiss(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriverServer()
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.log_in_base = LogInBaseServer(self.driver, self.base_url)
        self.driver.set_window_max()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_login_and_logout_dismiss(self):
        '''测试成功登录的用户取消退出'''
        # 打开途强在线首页-登录页
        self.base_page.open_page()
        # 输入用户信息进行登录
        self.log_in_base.log_in()
        # 点账户中心
        self.account_center_page_navi_bar.click_account_center_button()
        # 判断登录成功后跳转页面是否正确
        actual_url = self.driver.get_current_url()
        expect_url = self.base_url + "/customer/toAccountCenter"
        self.assertEqual(expect_url, actual_url, "登录成功后页面跳转错误")
        # 成功退出系统
        self.account_center_page_navi_bar.usr_logout_dismiss()
        # 判断是否仍停留在当前账户首页，并未退出系统
        self.assertEqual(self.base_url + "/customer/toAccountCenter#", self.driver.get_current_url(), "取消退出系统失败")
