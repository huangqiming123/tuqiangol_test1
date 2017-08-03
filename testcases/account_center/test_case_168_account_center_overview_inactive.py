import unittest
from time import sleep
from automate_driver.automate_driver_server import AutomateDriverServer
from model.assert_text import AssertText
from pages.account_center.account_center_details_page import AccountCenterDetailsPage
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer
from pages.login.login_page import LoginPage


# 账户中心-账户详情-账户总览   未激活
# author:zhangao

class TestCase168AccountCenterOverviewInactive(unittest.TestCase):
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

    def test_account_center_overview_inactive(self):
        # 打开途强在线首页-登录页
        self.base_page.open_page()
        # 登录账号
        self.log_in_base.log_in()
        self.account_center_page_navi_bar.click_account_center_button()
        sleep(2)
        account_center_handle = self.driver.get_current_window_handle()

        self.account_center_page_details.account_center_iframe()
        actual_total_inctive = self.account_center_page_details.get_actual_total_inactve()
        # 点击未激活
        self.account_center_page_details.account_overview('未激活')
        self.driver.default_frame()

        all_handles = self.driver.get_all_window_handles()
        for handle in all_handles:
            if handle != account_center_handle:
                self.driver.switch_to_window(handle)
                sleep(2)
                expect_url = self.driver.get_current_url()
                actual_url = self.base_url + '/device/toDeviceManage?statusFlag=inactive&lowerDevFlag=1'
                self.assertEqual(expect_url, actual_url, '点击未激活后，实际的url和期望的不一样！')
                sleep(2)
                self.account_center_page_details.click_more_in_dev_manage()
                self.assertEqual(self.assert_text.account_center_page_activing_text(), self.driver.get_text(
                    'x,//*[@id="allDev"]/div[2]/div[1]/div/div[6]/div[6]/div[2]/div/div/span[2]'))
                self.assertEqual(True, self.driver.get_element('x,//*[@id="lowerFlag"]/div/input').is_selected())

                expect_total_inactive = self.account_center_page_details.get_total_dev_number_after_ckick_all_dev_number()
                self.assertEqual(actual_total_inctive, str(expect_total_inactive), '账号总览统计未激活数量错误')

                # 验证清空按钮
                self.account_center_page_details.click_clear_all_button()
                lower_user_input_value = self.account_center_page_details.get_lower_input_value()
                self.assertEqual(False, lower_user_input_value)
                get_text = self.account_center_page_details.click_active_get_text()
                self.assertEqual(self.assert_text.account_center_page_active_status_text(), get_text)
                # 点搜索
                self.account_center_page_details.click_search_button()
                lower_user_input_value_again = self.account_center_page_details.get_lower_input_value()
                self.assertEqual(False, lower_user_input_value_again)
                get_text = self.account_center_page_details.click_active_get_text()
                self.assertEqual(self.assert_text.account_center_page_active_status_text(), get_text)

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
