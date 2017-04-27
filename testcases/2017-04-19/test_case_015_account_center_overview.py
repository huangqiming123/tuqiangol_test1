import csv
import unittest

from automate_driver.automate_driver import AutomateDriver
from pages.account_center.account_center_details_page import AccountCenterDetailsPage
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.base.base_page import BasePage
from pages.login.login_page import LoginPage


# 账户中心-账户详情-账户总览
# author:孙燕妮

class TestCase015AccountCenterOverview(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.account_center_page_details = AccountCenterDetailsPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.driver.set_window_max()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_account_center_overview(self):
        '''通过csv测试账户详情-账户总览'''


        # 打开途强在线首页-登录页
        self.base_page.open_page()

        # 登录账号
        self.login_page.user_login("test_007","jimi123")

        self.driver.wait()

        # 获取当前窗口句柄
        account_center_handle = self.driver.get_current_window_handle()

        csv_file = open(r"E:\git\tuqiangol_test\data\account_center\account_overview.csv",
                        'r',
                        encoding='utf8')
        csv_data = csv.reader(csv_file)

        for row in csv_data:
            link_info = {
                "link_name": row[0],
                "link_url": row[1],
            }

            # 点击账户总览页面的各个模块，并验证所跳转的页面正确
            self.account_center_page_details.account_overview(link_info["link_name"])
            self.driver.wait()
            expect_url = link_info["link_url"]

            # 获取当前所有窗口句柄
            all_handles = self.driver.get_all_window_handles()
            for handle in all_handles:
                if handle != account_center_handle:
                    self.driver.switch_to_window(handle)
                    self.driver.wait(1)
                    current_url = self.driver.get_current_url()

                    self.assertEqual(expect_url,current_url,link_info["link_name"] + "页面跳转错误!")
                    # 关闭当前窗口
                    self.driver.close_current_page()
                    # 回到账户中心窗口
                    self.driver.switch_to_window(account_center_handle)
                    self.driver.wait()


        csv_file.close()

        # 点击告警车辆，验证页面是否弹出报警管理框
        self.account_center_page_details.account_overview("告警车辆")
        alarm_title = self.driver.get_element("x,//*[@id='alarmMessage']/div[1]/h5").text
        self.assertIn("报警管理",alarm_title,"页面未弹出报警管理框")

        # 退出登录
        self.account_center_page_navi_bar.usr_logout()