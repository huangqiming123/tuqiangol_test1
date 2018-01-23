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

__author__ = ''

class TestCase208UserCenterSafeAreaLog(unittest.TestCase):
    # 测试个人中心 - 帮助 - 业务日志 - 安全区域管理日志（编辑、删除、关联、删除关联）
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

    def test_user_center_safe_area_log(self):
        self.base_page.open_page()
        self.log_in_base.log_in()
        user_account = self.log_in_base.get_log_in_account()

        # 点击安全区域
        current_handle = self.driver.get_current_window_handle()
        self.user_center_page.click_safe_area_button()
        self.base_page.change_windows_handle(current_handle)

        # 搜索平台围栏
        self.user_center_page.search_platform_fence()
        # 获取第一个围栏的名称
        fence_name = self.user_center_page.get_first_fence_name()

        # 点击编辑
        self.user_center_page.click_edit_fence_button()
        # 点击保存
        self.user_center_page.click_ensure_button()

        # 点击关联
        self.user_center_page.click_relevance_fence_button()
        # 选择设备进行关联
        imei_01 = self.user_center_page.click_dev_relevance_fence()
        # 点击保存
        self.user_center_page.click_ensure_button()

        # 取消关联
        self.user_center_page.click_relevance_fence_button()
        # 选择设备进行关联
        imei_02 = self.user_center_page.click_dev_relevance_fence()
        # 点击保存
        self.user_center_page.click_ensure_button()

        # 进入帮助 - 业务日志页面
        self.user_center_page.click_user_center_button()
        # 点击帮助
        self.user_center_page.click_help_button()
        # 切换到业务日志的frame里面
        self.user_center_page.switch_to_business_frame()

        # 选择安全区域查询 - 新增、编辑
        self.user_center_page.select_safe_area_search()
        self.user_center_page.select_edit_safe_area_search()
        sleep(5)

        operation_01 = self.user_center_page.get_operation_in_business_log()
        target_account_01 = self.user_center_page.get_target_account_in_business_log()
        operation_platform_01 = self.user_center_page.get_operation_platform_in_business_log()
        desc_01 = self.user_center_page.get_desc_in_business_log()

        self.assertEqual(operation_01, ' ' + user_account)
        self.assertEqual(target_account_01, user_account)
        self.assertEqual('网页端', operation_platform_01)
        web_desc_01 = "用户修改了(%s)围栏信息" % (fence_name)
        self.assertEqual(desc_01, web_desc_01)

        # 选择关联设备
        self.user_center_page.select_relevant_safe_area_search()
        sleep(5)

        operation_02 = self.user_center_page.get_operation_in_business_log_02()
        target_account_02 = self.user_center_page.get_target_account_in_business_log_02()
        operation_platform_02 = self.user_center_page.get_operation_platform_in_business_log_02()
        desc_02 = self.user_center_page.get_desc_in_business_log_02()

        self.assertEqual(operation_02, ' ' + user_account)
        self.assertEqual(target_account_02, user_account)
        self.assertEqual('网页端', operation_platform_02)
        web_desc_02 = "%s关联设备%s与区域信息%s" % (user_account, imei_01, fence_name)
        self.assertEqual(desc_02, web_desc_02)

        self.driver.default_frame()
