import csv
import unittest
from automate_driver.automate_driver_server import AutomateDriverServer
from model.assert_text import AssertText
from pages.account_center.account_center_page_read_csv import AccountCenterPageReadCsv
from pages.account_center.account_center_visual_account_page import AccountCenterVisualAccountPage
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer


# 账户中心-虚拟账户管理---添加虚拟用户异常验证
# author:戴招利
class TestCase33AccountCenterAddVisualEditException(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriverServer()
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.visual_account_page = AccountCenterVisualAccountPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.account_center_page_read_csv = AccountCenterPageReadCsv()
        self.log_in_base = LogInBaseServer(self.driver, self.base_page)
        self.assert_text = AssertText()
        self.base_page.open_page()
        self.driver.set_window_max()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def test_add_visual_account_exception_validation(self):
        '''添加虚拟用户验证'''

        data = ["jimitest", "dzltest", "xnzh_cs01"]

        # 登录
        self.log_in_base.log_in()
        self.account_center_page_navi_bar.click_account_center_button()
        # 进入虚拟账户管理
        self.visual_account_page.enter_visual_account()
        # 添加虚拟账号、保存
        for i in range(len(data)):
            self.visual_account_page.add_visual_account(data[i], "jimi123")
            self.visual_account_page.save_add_info()
            self.visual_account_page.dis_save_add_info()
            self.driver.wait(1)
            self.assertEqual(self.assert_text.account_center_page_account_exist(),
                             self.visual_account_page.get_save_status(), "在添加虚拟账号中可以添加已存在的账号！")
            self.driver.wait(1)
            # 退出登录
            # self.account_center_page_navi_bar.usr_logout()

    def tearDown(self):
        self.driver.quit_browser()
