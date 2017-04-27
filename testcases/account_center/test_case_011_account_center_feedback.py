import csv
import unittest

from automate_driver.automate_driver import AutomateDriver
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.account_center.account_center_page_read_csv import AccountCenterPageReadCsv
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.login.login_page import LoginPage


# 账户中心招呼栏帮助-意见反馈
# author:孙燕妮

class TestCase011AccountCenterFeedback(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.log_in_base = LogInBase(self.driver, self.base_url)
        self.account_center_page_read_csv = AccountCenterPageReadCsv()
        self.driver.set_window_max()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_account_center_feedback(self):
        '''测试招呼栏帮助-意见反馈功能'''
        # 打开途强在线首页-登录页
        self.base_page.open_page()
        # 登录账号
        self.log_in_base.log_in()
        self.driver.wait()
        # 招呼栏帮助
        self.account_center_page_navi_bar.to_help()
        # 判断是否进入帮助页面
        expect_url = self.base_url + '/userFeedback/toHelp'
        self.assertEqual(expect_url, self.driver.get_current_url(), "帮助页面跳转错误")

        csv_file = self.account_center_page_read_csv.read_csv('help_feedback.csv')
        csv_data = csv.reader(csv_file)

        for row in csv_data:
            feedback_data = {
                "suggest_type": row[0],
                "suggest_content": row[1],
                "contact": row[2],
                "phone": row[3]
            }

            # 提交意见反馈
            submit_status = self.account_center_page_navi_bar.help_feedback(feedback_data["suggest_type"],
                                                                            feedback_data["suggest_content"],
                                                                            feedback_data["contact"],
                                                                            feedback_data["phone"])

            # 判断反馈意见提交状态是否成功
            expect_status = '感谢你的反馈意见'
            self.assertEqual(expect_status, submit_status, "提交状态有误")

        csv_file.close()

        # 退出登录
        self.account_center_page_navi_bar.usr_logout()
