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


class TestCase2103UserSearchUserRelation(unittest.TestCase):
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

    def test_case_2103_user_search_user_relation(self):
        # 打开途强在线首页-登录页
        self.base_page.open_page()
        self.log_in_base.log_in()
        self.log_in_base.click_account_center_button()
        self.global_dev_search_page.click_easy_search()
        # 关闭
        self.global_dev_search_page.close_search()
        sleep(2)

        self.global_dev_search_page.click_easy_search()

        # 选择用户搜索
        self.global_dev_search_page.click_dev_search()
        self.global_dev_search_page.click_search_buttons()

        user_name = self.global_dev_search_page.get_user_name_in_user_search()
        user_type = self.global_dev_search_page.get_user_type_in_user_search()
        user_account = self.global_dev_search_page.get_user_account_in_user_search()

        self.global_dev_search_page.click_detail_in_user_search()
        # 验证用户信息
        self.global_dev_search_page.swith_to_search_frame()
        user_name_in_user_detail = self.global_account_search_page.get_user_name_in_user_detail()
        self.assertEqual(user_name, user_name_in_user_detail)

        user_type_in_user_detail = self.global_account_search_page.get_user_type_in_user_detail()
        self.assertEqual(user_type, " " + user_type_in_user_detail)

        user_account_in_user_detail = self.global_account_search_page.get_user_account_in_user_detail()
        self.assertEqual(user_account, user_account_in_user_detail)

        dev_number_in_user_detail = self.global_account_search_page.get_dev_number_in_user_detail()

        # 分别点击控制台、重置密码、查看
        # 点击查看
        current_handle = self.driver.get_current_window_handle()
        self.global_account_search_page.click_look_button_in_user_detail()
        all_handles = self.driver.get_all_window_handles()
        for handle in all_handles:
            if handle != current_handle:
                self.driver.switch_to_window(handle)

                expect_url = self.driver.base_url + '/device/toDeviceManage'
                self.assertEqual(self.driver.get_current_url(), expect_url)

                get_total_dev_number = self.global_account_search_page.get_dev_total_number_in_dev_manage_page()
                self.assertEqual(dev_number_in_user_detail, str(get_total_dev_number))
                self.driver.close_current_page()

                self.driver.switch_to_window(current_handle)

        # 点控制台
        current_handle = self.driver.get_current_window_handle()
        self.global_dev_search_page.swith_to_search_frame()
        self.global_account_search_page.click_console_button_in_user_detail()
        all_handles = self.driver.get_all_window_handles()
        for handle in all_handles:
            if handle != current_handle:
                self.driver.switch_to_window(handle)

                expect_url = self.driver.base_url + '/console'
                self.assertEqual(self.driver.get_current_url(), expect_url)
                self.driver.close_current_page()
                self.driver.switch_to_window(current_handle)

        # 点击重置密码
        self.global_dev_search_page.swith_to_search_frame()
        self.global_account_search_page.click_reset_password_button_in_user_detail()
        # 点击关闭
        self.global_account_search_page.click_close_button()

        # 点击重置密码
        self.global_account_search_page.click_reset_password_button_in_user_detail()
        # 点击取消
        self.global_account_search_page.click_cancel_button()

        # 点击重置密码
        self.global_account_search_page.click_reset_password_button_in_user_detail()
        # 点击确定
        self.global_account_search_page.click_ensuer_button()
        sleep(4)
        self.driver.default_frame()
        self.global_account_search_page.click_close_button()
