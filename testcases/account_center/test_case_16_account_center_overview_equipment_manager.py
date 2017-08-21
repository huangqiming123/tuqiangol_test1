import unittest
from time import sleep
from automate_driver.automate_driver_server import AutomateDriverServer
from model.assert_text import AssertText
from model.assert_text2 import AssertText2
from model.connect_sql import ConnectSql
from pages.account_center.account_center_details_page import AccountCenterDetailsPage
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer
from pages.login.login_page import LoginPage


# 账户中心-账户详情-账户总览   设置管理
# author:zhangao

class TestCase16AccountCenterOverviewEquipmentManager(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriverServer()
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.account_center_page_details = AccountCenterDetailsPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.driver.set_window_max()
        self.log_in_base = LogInBaseServer(self.driver, self.base_url)
        self.connect_sql = ConnectSql()
        self.assert_text = AssertText()
        self.assert_text2 = AssertText2()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_account_center_overview_equipment_manager(self):
        # 打开途强在线首页-登录页
        self.base_page.open_page()
        # 登录账号
        self.log_in_base.log_in()
        self.account_center_page_navi_bar.click_account_center_button()
        # self.account_center_page_details.account_center_iframe()
        current_account = self.log_in_base.get_log_in_account()
        sleep(2)
        account_center_handle = self.driver.get_current_window_handle()
        # 点击库存
        self.account_center_page_details.account_center_iframe()
        self.account_center_page_details.account_overview('设备管理')
        self.driver.default_frame()

        all_handles = self.driver.get_all_window_handles()
        for handle in all_handles:
            if handle != account_center_handle:
                self.driver.switch_to_window(handle)
                sleep(2)
                expect_url = self.driver.get_current_url()
                actual_url = self.base_url + '/device/toDeviceManage'
                self.assertEqual(expect_url, actual_url, '点击设备管理后，实际的url和期望的不一样！')

                # 验证文本
                # text = self.account_center_page_details.click_dev_manage_get_text()
                text = self.account_center_page_details.click_dev_manage_get_text()
                print(text)
                self.assertEqual(" " + self.assert_text2.account_center_page_contains_lower_dev_text(), text)

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
