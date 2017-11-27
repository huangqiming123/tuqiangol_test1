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


class TestCase115UserSearchUserInfo(unittest.TestCase):
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

    def test_case_user_search_user_info(self):
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
        # self.global_dev_search_page.click_dev_search()
        self.global_dev_search_page.click_user_search_buttons()

        user_name = self.global_dev_search_page.get_user_name_in_user_search()
        user_type = self.global_dev_search_page.get_user_type_in_user_search()
        user_account = self.global_dev_search_page.get_user_account_in_user_search()

        # 点用户详情
        self.global_dev_search_page.click_detail_in_user_search()

        # 用户信息
        self.global_dev_search_page.click_user_info_in_user_detail()
        # 获取用户信息中用户名称，用户类型、用户账号、上级用户
        user_name_in_detail = self.global_dev_search_page.get_user_name_in_detail()
        self.assertIn(user_name, user_name_in_detail)

        # user_type_in_detail = self.global_dev_search_page.get_user_type_in_detail()
        # self.assertEqual(user_type, user_type_in_detail)

        uesr_account_in_detail = self.global_dev_search_page.get_user_account_in_detail()
        self.assertEqual(user_account, uesr_account_in_detail)
        user_account_input_value = self.global_dev_search_page.get_user_account_input_value_in_detail()
        self.assertEqual('true', user_account_input_value)

        get_up_user_name = self.global_dev_search_page.get_up_user_name_in_detail()
        get_up_user_input_value = self.global_dev_search_page.get_up_user_input_value_in_detail()
        self.assertEqual('true', get_up_user_input_value)
