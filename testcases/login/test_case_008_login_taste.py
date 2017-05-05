import unittest

from automate_driver.automate_driver import AutomateDriver
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.base.base_page import BasePage
from pages.login.login_page import LoginPage


# 登录页我要体验
# author:孙燕妮

class TestCase008LoginTaste(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.driver.set_window_max()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_login_taste(self):
        '''测试我要体验功能'''
        # 打开途强在线首页-登录页
        self.base_page.open_page()
        # 点击我要体验
        self.login_page.taste()
        # 判断登入的页面是否正确
        self.assertEqual(self.base_url + "/index", self.driver.get_current_url(), "体验账号登入跳转页面错误")
        # 验证体检账号的四个权限
        self.assertEqual(5, self.login_page.get_number_permission_after_click_tester_button())
        self.assertEqual(' 控制台', self.login_page.get_first_text_after_log_in_tester_account())
        self.assertEqual(' 统计报表', self.login_page.get_second_text_after_log_in_tester_account())
        self.assertEqual(' 安全区域', self.login_page.get_third_text_after_log_in_tester_account())
        self.assertEqual(' 设备管理', self.login_page.get_four_text_after_log_in_tester_account())
        self.assertEqual(' 设备分布', self.login_page.get_fifth_text_after_log_in_tester_account())
        # 退出体验账号
        self.account_center_page_navi_bar.taste_usr_logout()
        # 判断是否成功退出到登录页
        self.assertEqual(self.base_url + "/", self.driver.get_current_url(), "退出系统失败")
