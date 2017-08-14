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


class TestCase113UserSearchPagingFunction(unittest.TestCase):
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

    def test_user_search_paging_function(self):
        # 打开途强在线首页-登录页
        self.base_page.open_page()
        self.base_page.click_chinese_button()
        self.log_in_base.log_in()
        self.log_in_base.click_account_center_button()
        current_account = self.log_in_base.get_log_in_account()
        self.global_dev_search_page.click_easy_search()
        # 关闭
        self.global_dev_search_page.close_search()
        sleep(2)

        self.global_dev_search_page.click_easy_search()
        self.global_dev_search_page.click_dev_search()
        self.global_account_search_page.switch_to_search_user_frame()
        self.global_account_search_page.click_search_user_button()

        # 获取页面总共有多少页
        total_number = self.global_account_search_page.get_total_number_after_click_search_user_button()

        if total_number == 0:
            self.assertIn(self.assert_text.account_center_page_no_data_text(),
                          self.global_account_search_page.get_no_data_text_in_user_search())
        elif total_number == 1:
            up_page_state = self.global_account_search_page.get_up_page_state_in_search_user()
            self.assertEqual('active', up_page_state)
            next_page_state = self.global_account_search_page.get_next_page_state_in_search_user()
            self.assertEqual('active', next_page_state)
        else:
            for n in range(total_number):
                self.global_account_search_page.click_per_page(n)

        if total_number != 0:
            self.global_account_search_page.click_per_number()
