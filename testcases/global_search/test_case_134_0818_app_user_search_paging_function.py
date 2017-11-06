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


class TestCase134AppUserSearchPagingFunction(unittest.TestCase):
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
        self.assert_text = AssertText()
        self.driver.wait(1)
        self.connect_sql = ConnectSql()
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_case_app_user_search_paging_function(self):
        # 打开途强在线首页-登录页
        self.base_page.open_page()
        self.log_in_base.log_in_jimitest()
        self.log_in_base.click_account_center_button()
        self.global_dev_search_page.click_easy_search()
        # 关闭
        self.global_dev_search_page.close_search()
        sleep(2)
        self.global_dev_search_page.click_easy_search()
        self.global_dev_search_page.click_app_account_search()
        # 点击搜索
        self.global_dev_search_page.click_search_buttonss()

        # 获取页面的总数
        self.global_dev_search_page.swith_to_search_frame()
        total_page = self.global_dev_search_page.get_total_page_after_click_app_search()
        if total_page[0] == 0:
            text = self.global_dev_search_page.get_no_data_text_in_app_user_search()
            self.assertIn(self.assert_text.account_center_page_no_data_text(), text)

        elif total_page[0] == 1:
            get_previous_page_class = self.global_dev_search_page.get_previous_page_class_in_app_user_search()
            self.assertEqual('active', get_previous_page_class)

            get_next_page_class = self.global_dev_search_page.get_next_page_class_in_app_user_search()
            self.assertEqual('active', get_next_page_class)

            list = [20, 30, 50, 100]
            for m in list:
                self.global_dev_search_page.click_per_page_number()
                total_page_again = self.global_dev_search_page.get_total_page_after_click_app_search()
                self.assertEqual(total_page, total_page_again)

        else:
            for n in range(total_page[0]):
                self.global_dev_search_page.click_per_page(n)
                get_per_first_number = self.global_dev_search_page.get_per_frist_number_in_dev_searchs()
                self.assertEqual(get_per_first_number, str(10 * (n + 1) - 9))