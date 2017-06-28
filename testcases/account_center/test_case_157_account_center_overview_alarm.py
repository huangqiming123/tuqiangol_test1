import unittest
from time import sleep

from automate_driver.automate_driver_server import AutomateDriverServer
from model.assert_text import AssertText
from pages.account_center.account_center_details_page import AccountCenterDetailsPage
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer
from pages.login.login_page import LoginPage


# 账户中心-账户详情-账户总览   围栏
# author:zhangao

class TestCase157AccountCenterOverviewAlarm(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriverServer()
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

    def test_account_center_overview_alarm(self):
        # 打开途强在线首页-登录页
        self.base_page.open_page()
        # 登录账号
        self.log_in_base.log_in()
        sleep(2)
        account_center_handle = self.driver.get_current_window_handle()
        # 点击库存
        self.account_center_page_details.account_overview('围栏')
        all_handles = self.driver.get_all_window_handles()
        for handle in all_handles:
            if handle != account_center_handle:
                self.driver.switch_to_window(handle)
                sleep(2)
                expect_url = self.driver.get_current_url()
                actual_url = self.base_url + '/safearea/geozonemap?flag=0'
                self.assertEqual(expect_url, actual_url, '点击围栏后，实际的url和期望的不一样！')
                actual_text = self.account_center_page_details.get_actual_text_after_click_alarm()
                self.assertEqual(self.assert_text.account_center_page_area_alarm_text(), actual_text,
                                 '点击围栏后，页面没有跳转到围栏设置页面')

                # 验证区域预警有没有被选中
                value = self.account_center_page_details.click_safearea_get_vaule()
                self.assertEqual('active', value)

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
        self.account_center_page_navi_bar.usr_logout()
