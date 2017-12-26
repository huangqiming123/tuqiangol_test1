import unittest
from time import sleep

from automate_driver.automate_driver_server import AutomateDriverServer
from model.assert_text import AssertText
from model.assert_text2 import AssertText2
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.account_center.account_center_page_read_csv import AccountCenterPageReadCsv
from pages.account_center.account_center_setting_home_page import AccountCenterSettingHomePage
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer


class TestCase302SetUpDefaultHomePageNoSetting(unittest.TestCase):
    # 测试未设置过默认首页的账号登录显示的默认首页
    def setUp(self):
        self.driver = AutomateDriverServer()
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.account_center_page_home_page_setting = AccountCenterSettingHomePage(self.driver, self.base_url)
        self.assert_text2 = AssertText2()
        self.account_center_page_read_csv = AccountCenterPageReadCsv()
        self.log_in_base = LogInBaseServer(self.driver, self.base_url)
        self.assert_text = AssertText()
        self.base_page.open_page()
        self.driver.set_window_max()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_no_setting_default_home_page(self):
        '''没有设置默认首页验证'''

        self.log_in_base.log_in_with_csv("zcs001", "jimi123")
        self.account_center_page_navi_bar.click_account_center_button()
        # 点击默认首页设置
        self.account_center_page_home_page_setting.click_home_page_setting()

        # 取列表数据
        all_state = self.account_center_page_home_page_setting.get_home_page_list_all_state()
        for i in all_state:
            self.assertEqual(self.assert_text2.account_center_home_page_no_setting_state(), i, "并不是全部为默认设置")

        sleep(2)
        # 退出
        self.account_center_page_navi_bar.usr_logout()
        # 登录
        self.log_in_base.log_in_with_csv("zcs001", "jimi123")
        expect_url = self.driver.get_current_url()
        actual_url = self.base_url + "/customer/toAccountCenter"
        self.assertEqual(expect_url, actual_url, "未设置默认首页，登陆后并不是进入账户中心页")
