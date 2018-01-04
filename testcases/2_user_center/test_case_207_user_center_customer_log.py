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


class TestCase207UserCenterCustomerLog(unittest.TestCase):
    # 测试个人中心 - 帮助 - 业务日志 - 客户管理日志（新增客户、修改客户信息、删除客户、修改密码、重置密码、转移客户）
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

    def test_user_center_customer_log(self):
        self.base_page.open_page()
        self.log_in_base.log_in()
        user_account = self.log_in_base.get_log_in_account()

        # 点击客户管理
        new_customer_data = ['新增的客户', 'new_1226']

        current_handle = self.driver.get_current_window_handle()
        self.user_center_page.click_customer_mangement()
        self.base_page.change_windows_handle(current_handle)

        # 新增客户按钮
        self.user_center_page.click_add_new_customer_buttons()
        # 点击切换到frame
        self.user_center_page.switch_to_add_new_customer_frame()
        # 填写用户名称和账号
        self.user_center_page.add_user_name_and_user_account(new_customer_data)
        self.driver.default_frame()
        # 点击确定
        self.user_center_page.click_ensure_button()

        # 搜索新增的用户
        self.user_center_page.search_user_in_customer_management(new_customer_data[1])

        # 修改用户信息 - 点击编辑
        self.user_center_page.click_edit_customer_button()
        # 点击保存
        self.user_center_page.click_ensure_button()

        # 点击重置密码
        self.user_center_page.click_reset_password_button()
        # 点击保存
        self.user_center_page.click_ensure_button()

        # 点击转移客户
        self.user_center_page.click_transfer_customer_button()
        # 点击保存
        self.user_center_page.click_ensure_button()

        # 点击删除客户
        self.user_center_page.click_delete_customer_button()
        # 点击保存
        self.user_center_page.click_ensure_button()

        # 进入帮助 - 业务日志页面
        self.user_center_page.click_user_center_button()
        # 点击帮助
        self.user_center_page.click_help_button()
        # 切换到业务日志的frame里面
        self.user_center_page.switch_to_business_frame()

        # 查询 客户管理 - 新增客户
        self.user_center_page.select_customer_management_condition()
        self.user_center_page.select_add_new_customer_log()
        # 点击搜索
        self.user_center_page.click_search_button_in_business_log()

        operation_01 = self.user_center_page.get_operation_in_business_log()
        target_account_01 = self.user_center_page.get_target_account_in_business_log()
        operation_platform_01 = self.user_center_page.get_operation_platform_in_business_log()
        desc_01 = self.user_center_page.get_desc_in_business_log()

        self.assertEqual(" " + user_account, operation_01)
        self.assertEqual(new_customer_data[1], target_account_01)
        self.assertEqual('网页端', operation_platform_01)
        web_desc_01 = "用户%s执行添加客户操作" % user_account
        self.assertEqual(web_desc_01, desc_01)

        # 查询修改用户信息
        self.user_center_page.select_edit_customer_log()
        # 点击搜索
        self.user_center_page.click_search_button_in_business_log()

        operation_02 = self.user_center_page.get_operation_in_business_log()
        target_account_02 = self.user_center_page.get_target_account_in_business_log()
        operation_platform_02 = self.user_center_page.get_operation_platform_in_business_log()
        desc_02 = self.user_center_page.get_desc_in_business_log()

        self.assertEqual(" " + user_account, operation_02)
        self.assertEqual(new_customer_data[1], target_account_02)
        self.assertEqual('网页端', operation_platform_02)
        web_desc_02 = "用户%s执行修改用户信息操作" % user_account
        self.assertEqual(web_desc_02, desc_02)

        # 查询删除用户信息
        self.user_center_page.select_delete_customer_log()
        # 点击搜索
        self.user_center_page.click_search_button_in_business_log()

        operation_03 = self.user_center_page.get_operation_in_business_log()
        target_account_03 = self.user_center_page.get_target_account_in_business_log()
        operation_platform_03 = self.user_center_page.get_operation_platform_in_business_log()
        desc_03 = self.user_center_page.get_desc_in_business_log()

        self.assertEqual(" " + user_account, operation_03)
        self.assertEqual(new_customer_data[1], target_account_03)
        self.assertEqual('网页端', operation_platform_03)
        web_desc_03 = "用户%s执行删除用户信息操作" % user_account
        self.assertEqual(web_desc_03, desc_03)

        # 查询重置密码信息
        self.user_center_page.select_reset_password_log()
        # 点击搜索
        self.user_center_page.click_search_button_in_business_log()

        operation_04 = self.user_center_page.get_operation_in_business_log()
        target_account_04 = self.user_center_page.get_target_account_in_business_log()
        operation_platform_04 = self.user_center_page.get_operation_platform_in_business_log()
        desc_04 = self.user_center_page.get_desc_in_business_log()

        self.assertEqual(" " + user_account, operation_04)
        self.assertEqual(new_customer_data[1], target_account_04)
        self.assertEqual('网页端', operation_platform_04)
        web_desc_04 = "用户%s执行重置密码操作" % user_account
        self.assertEqual(web_desc_04, desc_04)

        # 查询转移客户信息
        self.user_center_page.select_transfer_customer_log()
        # 点击搜索
        self.user_center_page.click_search_button_in_business_log()

        operation_05 = self.user_center_page.get_operation_in_business_log()
        target_account_05 = self.user_center_page.get_target_account_in_business_log()
        operation_platform_05 = self.user_center_page.get_operation_platform_in_business_log()
        desc_05 = self.user_center_page.get_desc_in_business_log()

        self.assertEqual(" " + user_account, operation_05)
        self.assertEqual(new_customer_data[1], target_account_05)
        self.assertEqual('网页端', operation_platform_05)
        web_desc_05 = "对用户%s从%s到%s执行转移客户操作" % (new_customer_data[1], user_account, user_account)
        self.assertEqual(web_desc_05, desc_05)

        self.driver.default_frame()
