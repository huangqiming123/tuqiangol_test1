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


class TestCase104GlobSearchCheckMarkedWords(unittest.TestCase):
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
        self.assert_text = AssertText()
        self.search_sql = SearchSql()
        self.driver.wait(1)
        self.connect_sql = ConnectSql()
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_case_1101_global_search_check_marked_words(self):
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

        get_dev_search_marked_words = self.global_dev_search_page.get_dev_search_marked_words()
        self.assertEqual(self.assert_text.glob_search_page_search_dev_text(), get_dev_search_marked_words)

        # 选择搜索用户
        self.global_dev_search_page.select_search_user()
        get_user_search_marked_words = self.global_dev_search_page.get_dev_search_marked_words()
        self.assertEqual(self.assert_text.glob_search_page_search_account_text(), get_user_search_marked_words)

        # 选择搜索app用户
        self.global_dev_search_page.select_search_app_user()
        get_user_search_marked_words = self.global_dev_search_page.get_dev_search_marked_words()
        self.assertEqual(self.assert_text.glob_search_page_search_account_text(), get_user_search_marked_words)
