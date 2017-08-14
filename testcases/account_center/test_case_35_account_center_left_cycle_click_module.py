import csv
import unittest
from time import sleep

from automate_driver.automate_driver_server import AutomateDriverServer
from model.assert_text import AssertText
from model.assert_text2 import AssertText2
from pages.account_center.account_center_details_page import AccountCenterDetailsPage
from pages.account_center.account_center_msg_center_page import AccountCenterMsgCenterPage
from pages.account_center.account_center_page_read_csv import AccountCenterPageReadCsv
from pages.account_center.account_center_setting_home_page import AccountCenterSettingHomePage
from pages.account_center.account_center_visual_account_page import AccountCenterVisualAccountPage
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer


# 账户中心--我的账号--循环点击左侧模块
# author:戴招利
class TestCase1109AccountCenterLeftCycleClickModule(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriverServer()
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.visual_account_page = AccountCenterVisualAccountPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.account_center_page_details = AccountCenterDetailsPage(self.driver, self.base_url)
        self.account_center_page_msg_center = AccountCenterMsgCenterPage(self.driver, self.base_url)
        self.account_center_page_visual_account = AccountCenterVisualAccountPage(self.driver, self.base_url)
        self.account_center_page_home_page_setting = AccountCenterSettingHomePage(self.driver, self.base_url)
        self.account_center_page_read_csv = AccountCenterPageReadCsv()
        self.log_in_base = LogInBaseServer(self.driver, self.base_page)
        self.assert_text = AssertText()
        self.assert_text2 = AssertText2()
        self.base_page.open_page()
        self.driver.set_window_max()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_left_cycle_click_module(self):
        '''我的账号下循环点击模块'''

        # 登录
        self.log_in_base.log_in()
        sleep(1)
        self.account_center_page_navi_bar.click_account_center_button()

        for i in range(5):
            # 点击账户详情
            self.account_center_page_details.click_account_details()

            text = self.account_center_page_details.get_memorization_default_options_text()
            self.assertIn(self.assert_text2.account_center_memorization_default_options(), text, "点击账户详情,页面有误")
            print(text)

            # 点击虚拟账号
            self.account_center_page_msg_center.enter_msg_center()

            self.account_center_page_msg_center.message_center_iframe()
            msg_center_title = self.account_center_page_msg_center.get_msg_center_title()
            self.driver.default_frame()
            self.assertIn(self.assert_text.account_center_page_message_center_text(), msg_center_title, "点击消息中心,页面有误")
            print(msg_center_title)

            # 虚拟账户管理
            self.account_center_page_visual_account.enter_visual_account()

            self.account_center_page_visual_account.visual_account_iframe()
            visual_account_title = self.account_center_page_visual_account.get_visual_account_title()
            self.assertIn(self.assert_text.account_center_page_virtual_account_manager(), visual_account_title,
                          "点击虚拟账户管理，页面有误!")
            self.driver.default_frame()
            print(visual_account_title)

            # 设备型号设置
            self.account_center_page_details.click_facility_Model_number_setting()

            title = self.account_center_page_details.get_facility_Model_number_setting_title()
            self.assertIn(self.assert_text2.account_center_facility_Model_number_title(), title,
                          "点击设备型号设置，页面有误!")
            print(title)

            # 默认首页设置
            self.account_center_page_home_page_setting.click_home_page_setting()

            text = self.account_center_page_home_page_setting.get_default_home_setting_title()
            self.assertIn(self.assert_text2.account_center_default_home_setting_title(), text,
                          "点击默认首页设置，页面有误!")
            print(text)
