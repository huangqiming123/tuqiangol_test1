import unittest
from time import sleep

from automate_driver.automate_driver import AutomateDriver
from model.assert_text import AssertText
from model.connect_sql import ConnectSql
from pages.account_center.account_center_navi_bar_pages import AccountCenterNaviBarPages
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.global_search.global_account_search_page import GlobalAccountSearchPage
from pages.global_search.global_dev_search_page import GlobalDevSearchPage
from pages.global_search.global_search_page_read_csv import GlobleSearchPageReadCsv
from pages.global_search.search_sql import SearchSql


class TestCase1102GlobSearchAppUserOperation(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.global_dev_search_page = GlobalDevSearchPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPages(self.driver, self.base_url)
        self.driver.set_window_max()
        self.global_account_search_page = GlobalAccountSearchPage(self.driver, self.base_url)
        self.log_in_base = LogInBase(self.driver, self.base_url)
        self.global_search_page_read_csv = GlobleSearchPageReadCsv()
        self.search_sql = SearchSql()
        self.driver.wait(1)
        self.connect_sql = ConnectSql()
        self.assert_text = AssertText()
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_case_1102_global_search_app_user_operation(self):
        # 打开途强在线首页-登录页
        self.base_page.open_page()
        self.base_page.click_chinese_button()
        self.log_in_base.log_in_jimitest()
        self.log_in_base.click_account_center_button()
        self.global_dev_search_page.click_easy_search()
        # 关闭
        self.global_dev_search_page.close_search()
        sleep(2)

        self.global_dev_search_page.click_easy_search()
        self.global_dev_search_page.select_search_app_user()

        # 点击搜索
        self.global_dev_search_page.click_search_button()

        # 点击控制台
        current_handle = self.driver.get_current_window_handle()
        self.global_dev_search_page.click_console_button()
        all_handles = self.driver.get_all_window_handles()
        for handle in all_handles:
            if handle != current_handle:
                self.driver.switch_to_window(handle)

                self.assertEqual(self.base_url + '/console', self.driver.get_current_url())
                self.driver.close_current_page()
                sleep(2)
                self.driver.switch_to_window(current_handle)

        # 获取第一个app用户的详情
        app_user_name = self.global_dev_search_page.get_app_user_name_in_app_search()
        app_user_type = self.global_dev_search_page.get_app_user_type_in_app_search()
        app_user_account = self.global_dev_search_page.get_app_user_account_in_app_search()
        app_user_phone = self.global_dev_search_page.get_app_user_phone_in_app_search()
        app_user_dev_number = self.global_dev_search_page.get_app_user_dev_number_in_app_search()
        # 点击详情
        self.global_dev_search_page.click_detail_in_app_user_search()

        # 获取app用户详情页面的用户数据
        app_name_in_detail = self.global_dev_search_page.get_app_name_in_detail()
        self.assertEqual(app_user_name, app_name_in_detail)

        app_type_in_detail = self.global_dev_search_page.get_app_type_in_detail()
        self.assertEqual(app_user_type, app_type_in_detail)

        app_account_in_detail = self.global_dev_search_page.get_app_account_in_detail()
        self.assertEqual(app_user_account, app_account_in_detail)

        app_phone_in_detail = self.global_dev_search_page.get_app_phone_in_detail()
        self.assertEqual(app_user_phone, app_phone_in_detail)

        app_dev_number_in_detail = self.global_dev_search_page.get_app_dev_number_in_detail()
        self.assertEqual(app_user_dev_number, app_dev_number_in_detail)

        app_dev_number_in_detail_by_list = self.global_dev_search_page.get_app_dev_number_in_detail_by_list()
        self.assertEqual(str(app_dev_number_in_detail_by_list), app_dev_number_in_detail)

        self.assertEqual(str(app_dev_number_in_detail_by_list), app_user_dev_number)

        # 重置密码
        self.global_dev_search_page.return_app_user_list()
        # 点击重置密码
        self.global_dev_search_page.click_reset_password_button()
        # 点击关闭
        self.global_dev_search_page.close_button()

        # 点击重置密码
        self.global_dev_search_page.click_reset_password_button()
        # 点击关闭
        self.global_dev_search_page.cancel_button()

        # 点击重置密码
        self.global_dev_search_page.click_reset_password_button()
        # 点击关闭
        self.global_dev_search_page.ensure_button()

        get_text = self.global_dev_search_page.get_text_after_succeed()
        self.assertEqual(self.assert_text.account_center_page_operation_done(), get_text)
