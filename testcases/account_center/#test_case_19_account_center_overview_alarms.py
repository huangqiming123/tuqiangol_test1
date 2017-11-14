import unittest
from time import sleep
from automate_driver.automate_driver_server import AutomateDriverServer
from model.assert_text import AssertText
from pages.account_center.account_center_details_page import AccountCenterDetailsPage
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer
from pages.login.login_page import LoginPage


# 账户中心-账户详情-账户总览   告警
# author:zhangao

class TestCase19AccountCenterOverviewAlarm(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriverServer(choose='chrome')
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.account_center_page_details = AccountCenterDetailsPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.driver.set_window_max()
        self.log_in_base = LogInBaseServer(self.driver, self.base_url)
        self.assert_text = AssertText()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_account_center_overview_set_up_landmark(self):
        # 打开途强在线首页-登录页
        self.base_page.open_page()
        # 登录账号
        self.log_in_base.log_in()
        self.account_center_page_navi_bar.click_account_center_button()
        sleep(2)
        account_center_handle = self.driver.get_current_window_handle()
        # 点击告警
        self.account_center_page_details.account_center_iframe()
        self.account_center_page_details.account_overview('告警')
        self.driver.default_frame()

        all_handles = self.driver.get_all_window_handles()
        for handle in all_handles:
            if handle != account_center_handle:
                self.driver.switch_to_window(handle)
                sleep(2)
                expect_url = self.driver.get_current_url()
                actual_url = self.base_url + '/deviceReport/statisticalReport?modularId=alarmDdetails'
                self.assertEqual(expect_url, actual_url, '点击告警后，实际的url和期望的不一样！')
                sleep(2)

                actual_text = self.account_center_page_details.get_actual_text_after_click_alarms()
                self.assertEqual(self.assert_text.account_center_page_alarm_details_text(), actual_text,
                                 '点击告警后，页面没有跳转到告警总览页面上')

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
