import unittest

from automate_driver.automate_driver_server import AutomateDriverServer
from model.connect_sql import ConnectSql
from pages.account_center.account_center_operation_log_page import AccountCenterOperationLogPage
from pages.account_center.account_center_page_read_csv import AccountCenterPageReadCsv
from pages.account_center.user_center import UserCenterPage
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer
from pages.help.help_page import HelpPage
from pages.help.help_page_sql import HelpPageSql
from pages.login.login_page import LoginPage


class TestCase209UserCenterAlarmSetUpLog(unittest.TestCase):
    # 测试个人中心 - 帮助 - 业务日志 - 告警设置（推送设置）
    def setUp(self):
        self.driver = AutomateDriverServer()
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.help_page = HelpPage(self.driver, self.base_url)
        self.account_center_page_operation_log = AccountCenterOperationLogPage(self.driver, self.base_url)
        self.help_page_sql = HelpPageSql()
        self.account_center_page_read_csv = AccountCenterPageReadCsv()
        self.connect_sql = ConnectSql()
        self.log_in_base = LogInBaseServer(self.driver, self.base_page)
        self.user_center_page = UserCenterPage(self.driver, self.base_url)
        self.driver.set_window_max()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_user_center_alarm_set_up_log(self):
        self.base_page.open_page()
        self.log_in_base.log_in()
        user_account = self.log_in_base.get_log_in_account()

        # 点击设置 - 告警设置
        self.user_center_page.click_set_up_and_alarm_set_up()
        # 点击推送设置
        self.user_center_page.click_push_set_up()
        # 切换到告警设置的frame里
        self.user_center_page.switch_to_alarm_set_up_frame()

        # 获取第一个告警类型的名称、和状态
        alarm_name = self.user_center_page.get_first_alarm_name()
        alarm_status = self.user_center_page.get_first_alarm_status()
        # 点击第一个告警类型
        self.user_center_page.click_first_alarm_type()
        alarm_status_01 = self.user_center_page.get_first_alarm_status()

        if alarm_status == True:
            self.assertEqual(False, alarm_status_01)
        else:
            self.assertEqual(True, alarm_status_01)
        self.driver.default_frame()

        # 进入帮助 - 业务日志页面
        self.user_center_page.click_user_center_button()
        # 点击帮助
        self.user_center_page.click_help_button()
        # 切换到业务日志的frame里面
        self.user_center_page.switch_to_business_frame()

        # 选择查询告警设置
        self.user_center_page.select_alarm_set_up_search()

        operation_01 = self.user_center_page.get_operation_in_business_log()
        target_account_01 = self.user_center_page.get_target_account_in_business_log()
        operation_platform_01 = self.user_center_page.get_operation_platform_in_business_log()
        desc_01 = self.user_center_page.get_desc_in_business_log()

        self.assertEqual(' ' + user_account, operation_01)
        self.assertEqual(user_account, target_account_01)
        self.assertEqual('网页端', operation_platform_01)

        if alarm_status_01 == True:
            web_desc_01 = "%s开启%s" % (user_account, alarm_name)
            self.assertEqual(desc_01, web_desc_01)

        if alarm_status_01 == False:
            web_desc_01 = "%s关闭%s" % (user_account, alarm_name)
            self.assertEqual(desc_01, web_desc_01)

        self.driver.default_frame()
