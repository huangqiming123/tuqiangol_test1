import csv
import unittest
from time import sleep

from automate_driver.automate_driver_server import AutomateDriverServer
from model.assert_text import AssertText
from model.assert_text2 import AssertText2
from pages.account_center.account_center_details_page import AccountCenterDetailsPage
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.account_center.account_center_page_read_csv import AccountCenterPageReadCsv
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer
from pages.login.login_page import LoginPage


# 账户中心-账户详情-记住默认选项
# author:戴招利

class TestCase380821AccountCenterPageMemorizationDefaultOption(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriverServer()
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.account_center_page_details = AccountCenterDetailsPage(self.driver, self.base_url)
        self.assert_text = AssertText()
        self.assert_text2 = AssertText2()
        self.driver.set_window_max()
        self.account_center_page_read_csv = AccountCenterPageReadCsv()
        self.log_in_base = LogInBaseServer(self.driver, self.base_page)
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_memorization_default_option(self):
        '''记住默认选项功能'''

        # 打开途强在线首页-登录页
        self.base_page.open_page()
        # 登录账号
        self.log_in_base.log_in_with_csv("dzltest", "jimi123")
        self.driver.wait(1)
        self.account_center_page_navi_bar.click_account_center_button()

        csv_file = self.account_center_page_read_csv.read_csv('memorization_defaule_option.csv')
        csv_data = csv.reader(csv_file)
        for row in csv_data:
            data = {
                "page": row[0],
                "state_true": row[1],
                "state_false": row[2]

            }

            # 账户总览为记住默认选项
            self.account_center_page_details.account_center_iframe()
            # 点击账户总览或快速销售页面
            self.account_center_page_details.select_overview_or_sell_page(data["page"])
            self.account_center_page_details.click_memorization_default_option()
            state = self.account_center_page_details.get_memorization_default_option_state()
            self.assertEqual(data["state_true"], str(state["overview_state"]), "账户总览记住默认选项状态与期望不一致")
            self.assertEqual(data["state_false"], str(state["sell_state"]), "快速销售记住默认选项状态与期望不一致")
            print(state)
            sleep(2)
            self.driver.default_frame()
            self.account_center_page_navi_bar.usr_logout()

            # 验证记住默认选项页面是否正确
            self.log_in_base.log_in_with_csv("dzltest", "jimi123")
            self.driver.wait(1)
            self.account_center_page_navi_bar.click_account_center_button()
            if data["page"] == "账户总览" or data["page"] == "":
                self.assertEqual(self.assert_text2.account_center_download_app_text(),
                                 self.account_center_page_details.get_download_app_hint(), "提示不一致,不是在账户总览页")
            elif data["page"] == "快速销售":
                self.assertEqual(self.assert_text2.account_center_fast_sale_typeface(),
                                 self.account_center_page_details.get_fast_sale_typeface(), "提示不一致,不是在快速销售页")

        # 账号中心设置记住，在快速销售页退出，验证
        self.account_center_page_details.account_center_iframe()
        self.account_center_page_details.click_account_pandect()
        self.account_center_page_details.click_memorization_default_option()
        state = self.account_center_page_details.get_memorization_default_option_state()
        self.assertEqual(True, state["overview_state"], "账户总览记住默认选项状态与期望不一致")
        self.assertEqual(False, state["sell_state"], "快速销售记住默认选项状态与期望不一致")
        self.account_center_page_details.fast_sales()
        self.driver.default_frame()

        self.account_center_page_navi_bar.usr_logout()
        self.log_in_base.log_in_with_csv("dzltest", "jimi123")
        sleep(1)
        self.account_center_page_navi_bar.click_account_center_button()
        self.assertEqual(self.assert_text2.account_center_download_app_text(),
                         self.account_center_page_details.get_download_app_hint(), "提示不一致，不是在账户总览页")

        csv_file.close()
        # 退出登录
        # self.account_center_page_navi_bar.usr_logout()
