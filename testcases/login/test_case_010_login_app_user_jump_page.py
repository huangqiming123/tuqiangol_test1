import csv
import unittest
from automate_driver.automate_driver_server import AutomateDriverServer
from model.assert_text import AssertText
from pages.account_center.account_center_details_page import AccountCenterDetailsPage
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.base.base_page_server import BasePageServer
from pages.login.log_in_page_read_csv import LogInPageReadCsv
from pages.login.login_page import LoginPage


# 首页-app账号--各模块跳转页面
# author:戴招利

class TestCase010AppUserJumpPage(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriverServer()
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.account_center_page_details = AccountCenterDetailsPage(self.driver, self.base_url)
        self.log_in_read_csv = LogInPageReadCsv()
        self.assert_text = AssertText()
        self.driver.set_window_max()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_app_account_jump_page(self):
        '''通过csv测试app首页跳转页面'''

        # 打开途强在线首页-登录页
        self.base_page.open_page()

        # 登录账号
        self.login_page.user_login("18665948719", "jimi123")
        self.driver.wait(1)

        # 获取当前窗口句柄
        account_center_handle = self.driver.get_current_window_handle()

        csv_file = self.log_in_read_csv.read_csv('login_app_user_jump_page.csv')
        csv_data = csv.reader(csv_file)

        for row in csv_data:
            link_info = {
                "link_name": row[0],
                "link_url": row[1],
            }

            # 点击首页的各个模块，并验证所跳转的页面正确
            self.login_page.login_page_account_overview(link_info["link_name"])
            self.driver.wait()
            expect_url = self.base_url + link_info["link_url"]

            # 获取当前所有窗口句柄
            all_handles = self.driver.get_all_window_handles()
            for handle in all_handles:
                if handle != account_center_handle:
                    self.driver.switch_to_window(handle)
                    self.driver.wait(1)
                    current_url = self.driver.get_current_url()

                    self.assertEqual(expect_url, current_url, link_info["link_name"] + "页面跳转错误!")
                    # 关闭当前窗口
                    self.driver.close_current_page()
                    # 回到账户中心窗口
                    self.driver.switch_to_window(account_center_handle)
                    self.driver.wait()

        csv_file.close()

        # 点击告警车辆，验证页面是否弹出报警管理框
        self.login_page.login_page_account_overview("告警车辆")
        alarm_title = self.driver.get_element("x,//*[@id='alarmMessage']/div[1]/h5").text
        self.assertIn(self.assert_text.account_center_page_alarm_manager_text(), alarm_title, "页面未弹出报警管理框")

        # 退出登录
        self.account_center_page_navi_bar.app_usr_logout()
