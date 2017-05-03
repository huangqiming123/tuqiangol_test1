import unittest
from time import sleep

from automate_driver.automate_driver import AutomateDriver
from pages.account_center.account_center_details_page import AccountCenterDetailsPage
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.login.login_page import LoginPage


# 账户中心-账户详情-账户总览   已激活
# author:zhangao

class TestCase167AccountCenterOverviewActived(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.account_center_page_details = AccountCenterDetailsPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.driver.set_window_max()
        self.log_in_base = LogInBase(self.driver,self.base_url)
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_account_center_overview_actived(self):
        # 打开途强在线首页-登录页
        self.base_page.open_page()
        # 登录账号
        self.log_in_base.log_in()
        sleep(2)
        account_center_handle = self.driver.get_current_window_handle()
        actual_total_actived = self.account_center_page_details.get_actual_total_actved()
        # 点击库存
        self.account_center_page_details.account_overview('已激活')
        all_handles = self.driver.get_all_window_handles()
        for handle in all_handles:
            if handle != account_center_handle:
                self.driver.switch_to_window(handle)
                sleep(2)
                expect_url = self.driver.get_current_url()
                actual_url = self.base_url + '/device/toDevices?flag=activated'
                self.assertEqual(expect_url, actual_url, '点击已激活后，实际的url和期望的不一样！')
                sleep(2)

                expect_total_actived = self.account_center_page_details.get_total_all_actived_equipment()
                self.assertEqual(actual_total_actived, str(expect_total_actived), '账号总览统计激活数量错误')
                self.driver.close_current_page()
                # 回到账户中心窗口
                self.driver.switch_to_window(account_center_handle)
                self.driver.wait()

        # 退出登录
        self.account_center_page_navi_bar.usr_logout()