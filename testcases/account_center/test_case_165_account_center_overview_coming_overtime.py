import unittest
from time import sleep
from automate_driver.automate_driver_server import AutomateDriverServer
from pages.account_center.account_center_details_page import AccountCenterDetailsPage
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer
from pages.login.login_page import LoginPage


# 账户中心-账户详情-账户总览   即将到期
# author:zhangao

class TestCase165AccountCenterOverviewComingOvertime(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriverServer()
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.account_center_page_details = AccountCenterDetailsPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.driver.set_window_max()
        self.log_in_base = LogInBaseServer(self.driver, self.base_url)
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_account_center_overview_coming_overtime(self):
        # 打开途强在线首页-登录页
        self.base_page.open_page()
        # 登录账号
        self.log_in_base.log_in()
        sleep(2)
        number = self.account_center_page_details.get_coming_overtime_number()
        account_center_handle = self.driver.get_current_window_handle()
        # 点击库存
        self.account_center_page_details.account_overview('即将到期')
        all_handles = self.driver.get_all_window_handles()
        for handle in all_handles:
            if handle != account_center_handle:
                self.driver.switch_to_window(handle)
                sleep(2)
                expect_url = self.driver.get_current_url()
                actual_url = self.base_url + '/device/toDeviceManage?statusFlag=aboutToExpirate&lowerDevFlag=1'
                self.assertEqual(expect_url, actual_url, '点击即将到期后，实际的url和期望的不一样！')
                sleep(2)

                get_text = self.account_center_page_details.click_coming_overtime_get_text()
                self.assertEqual('即将过期', get_text)

                self.assertEqual(True, self.driver.get_element('x,//*[@id="lowerFlag"]/div/input').is_selected())

                self.assertEqual(number,
                                 str(
                                     self.account_center_page_details.get_total_dev_number_after_ckick_all_dev_number()))
                self.driver.close_current_page()
                # 回到账户中心窗口
                self.driver.switch_to_window(account_center_handle)
                self.driver.wait()

        # 退出登录
        self.account_center_page_navi_bar.usr_logout()
