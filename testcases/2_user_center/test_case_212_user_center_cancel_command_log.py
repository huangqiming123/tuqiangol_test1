import unittest
from time import sleep

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


class TestCase212UserCenterCancelCommandLog(unittest.TestCase):
    # 测试个人中心 - 帮助 - 业务日志 - 取消指令日志
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

    def test_user_center_cancel_command_log(self):
        self.base_page.open_page()
        self.log_in_base.log_in_jimitest()
        user_account = self.log_in_base.get_log_in_account()

        # 点击设置 - 指令管理
        self.user_center_page.click_set_up_and_command_set_up()
        # 点击下发指令管理
        self.user_center_page.click_issued_command_management()
        sleep(3)
        # 搜索待发送的指令记录
        self.user_center_page.search_to_be_sent_command()

        # 获取第一条指令的信息
        command_info = self.user_center_page.get_command_info_first_command_record()
        command_imei = self.user_center_page.get_command_imei_first_command_record()

        # 选择第一条记录，选中取消指令
        self.user_center_page.select_first_command_record_and_cancel()

        self.user_center_page.click_user_center_button()
        # 点击帮助
        self.user_center_page.click_help_button()
        # 切换到业务日志的frame里面
        self.user_center_page.switch_to_business_frame()

        # 搜索取消指令
        self.user_center_page.select_cancel_command_log()
        # 点击搜索
        self.user_center_page.click_search_button_in_business_log()

        # 获取第一条日志的记录
        operation = self.user_center_page.get_operation_in_business_log()
        target_account = self.user_center_page.get_target_account_in_business_log()
        operation_platform = self.user_center_page.get_operation_platform_in_business_log()
        desc = self.user_center_page.get_desc_in_business_log()

        # 断言
        self.assertEqual(operation + " ", ' ' + user_account)
        self.assertEqual(target_account + ' ', user_account)
        self.assertEqual('网页端', operation_platform)

        desc_01 = "%s取消设备%s 指令%s" % (operation, command_imei, command_info)
        self.assertEqual(desc_01, " " + desc)
