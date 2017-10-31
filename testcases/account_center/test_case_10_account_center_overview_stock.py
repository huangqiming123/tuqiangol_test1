import unittest
from time import sleep

from automate_driver.automate_driver_server import AutomateDriverServer
from model.assert_text import AssertText
from model.connect_sql import ConnectSql
from pages.account_center.account_center_details_page import AccountCenterDetailsPage
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer
from pages.login.login_page import LoginPage


# 账户中心-账户详情-账户总览  包括：库存
# author:zhangao

class TestCase10AccountCenterOverviewStock(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriverServer(choose='chrome')
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.account_center_page_details = AccountCenterDetailsPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.driver.set_window_max()
        self.connect_sql = ConnectSql()
        self.log_in_base = LogInBaseServer(self.driver, self.base_url)
        self.assert_text = AssertText()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_account_center_overview_stock(self):
        # 打开途强在线首页-登录页
        self.base_page.open_page()
        # 登录账号
        self.log_in_base.log_in()
        # self.log_in_base.log_in_with_csv("kankan111","jimi123")
        self.account_center_page_navi_bar.click_account_center_button()
        sleep(2)
        self.account_center_page_details.account_center_iframe()
        # current_account = self.log_in_base.get_log_in_account()
        account_center_handle = self.driver.get_current_window_handle()
        expect_total = self.account_center_page_details.get_current_account_all_equipment()

        # 点击库存
        self.account_center_page_details.account_overview('库存')
        self.driver.default_frame()

        all_handles = self.driver.get_all_window_handles()
        for handle in all_handles:
            if handle != account_center_handle:
                self.driver.switch_to_window(handle)
                sleep(2)
                expect_url = self.driver.get_current_url()
                actual_url = self.base_url + '/device/toDeviceManage'
                self.assertEqual(expect_url, actual_url, '点击库存后，实际的url和期望的不一样！')

                # 判断包涵下级的input框未被勾选上
                input_value = self.account_center_page_navi_bar.check_next_user_input_value()
                self.assertEqual(False, input_value)
                sleep(3)
                actual_total = self.account_center_page_details.get_actual_current_account_all_equipment()
                self.assertEqual(expect_total, str(actual_total), '当前用户库存的总数和实际不一致！')

                # 验证清空按钮
                self.account_center_page_details.click_clear_all_button()
                lower_user_input_value = self.account_center_page_details.get_lower_input_value()
                self.assertEqual(False, lower_user_input_value)
                # 点搜索
                self.account_center_page_details.click_search_button()
                lower_user_input_value_again = self.account_center_page_details.get_lower_input_value()
                self.assertEqual(False, lower_user_input_value_again)

                # 查看控制台告警设置能否打开
                self.account_center_page_navi_bar.click_alarm_button_in_console()
                # 断言
                get_text = self.account_center_page_navi_bar.get_text_after_click_alarm_button()
                self.assertEqual(self.assert_text.account_center_page_alarm_manager_text(), get_text)
                self.account_center_page_navi_bar.close_alarm_in_console()

                self.driver.close_current_page()
                # 回到账户中心窗口
                self.driver.switch_to_window(account_center_handle)
                self.driver.wait()
        # 退出登录
                # self.account_center_page_navi_bar.usr_logout()
