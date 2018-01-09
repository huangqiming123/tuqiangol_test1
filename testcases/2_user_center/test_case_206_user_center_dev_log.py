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


class TestCase206UserCenterDevLog(unittest.TestCase):
    # 测试个人中心 - 帮助 - 业务日志 - 设备管理日志（设备修改和设备分配）
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

    def test_user_center_dev_log(self):
        self.base_page.open_page()
        self.log_in_base.log_in()
        user_account = self.log_in_base.get_log_in_account()

        # 点击设备管理
        current_handle = self.driver.get_current_window_handle()
        self.user_center_page.click_dev_management_button()
        sleep(3)
        self.base_page.change_windows_handle(current_handle)
        # 获取列表第一个imei号
        sleep(3)
        imei = self.user_center_page.get_dev_list_first_imei()
        # 点击编辑
        self.user_center_page.click_edit_dev_button()
        # 点击确定
        self.user_center_page.click_ensure_button()

        # 销售
        self.user_center_page.click_sale_button()

        # 进入帮助 - 业务日志页面
        current_handle_01 = self.driver.get_current_window_handle()
        self.user_center_page.click_user_center_button()
        self.base_page.change_windows_handle(current_handle_01)
        # 点击帮助
        self.user_center_page.click_help_button()
        # 切换到业务日志的frame里面
        self.user_center_page.switch_to_business_frame()

        self.user_center_page.click_search_button_in_business_log()

        # 获取第一条数据的操作人、目标账号、操作平台、描述
        sleep(3)
        operation = self.user_center_page.get_operation_in_business_log()
        target_account = self.user_center_page.get_target_account_in_business_log()
        operation_platform = self.user_center_page.get_operation_platform_in_business_log()
        desc = self.user_center_page.get_desc_in_business_log()
        self.assertEqual(' ' + user_account, operation)
        self.assertEqual(target_account, user_account)
        self.assertEqual('网页端', operation_platform)

        web_desc = "%s修改设备%s" % (user_account, imei)
        self.assertEqual(web_desc, desc)

        # 选择设备分配搜索
        self.user_center_page.search_dev_sale_in_business_log()
        # 点击搜索
        self.user_center_page.click_search_button_in_business_log()

        operation_01 = self.user_center_page.get_operation_in_business_log()
        target_account_01 = self.user_center_page.get_target_account_in_business_log()
        operation_platform_01 = self.user_center_page.get_operation_platform_in_business_log()
        desc_01 = self.user_center_page.get_desc_in_business_log()

        self.assertEqual(' ' + user_account, operation_01)
        self.assertEqual(target_account_01, user_account)
        self.assertEqual('网页端', operation_platform_01)

        web_desc_01 = "%s将设备%s从%s分配给%s" % (user_account, imei, user_account, user_account)
        self.assertEqual(web_desc_01, desc_01)
        self.driver.default_frame()
