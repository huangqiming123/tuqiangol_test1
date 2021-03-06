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


class TestCase123DevSearchPagingFunction(unittest.TestCase):
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

    def test_case_dev_search_paging_function(self):
        # 打开途强在线首页-登录页
        self.base_page.open_page()

        self.log_in_base.log_in()
        self.log_in_base.click_account_center_button()
        self.global_dev_search_page.click_easy_search()
        # 关闭
        self.global_dev_search_page.close_search()
        sleep(2)
        self.global_dev_search_page.click_easy_search()
        self.global_dev_search_page.click_dev_searchs()
        # 选择设备搜索
        # self.global_dev_search_page.click_search_buttons()
        sleep(5)
        self.global_dev_search_page.swith_to_search_frame()
        # 获取设备有多少个分页
        total_page = self.global_dev_search_page.get_total_page_number_after_search_dev()
        if total_page[0] == 0:
            text = self.global_dev_search_page.get_no_data_text_in_search_dev()
            self.assertIn(self.assert_text.account_center_page_no_data_text(), text)

        elif total_page[0] == 1:
            up_page_class = self.global_dev_search_page.get_up_page_class_active_in_dev_search()
            self.assertEqual('active', up_page_class)

            next_page_class = self.global_dev_search_page.get_next_page_class_active_in_dev_search()
            self.assertEqual('active', next_page_class)

        else:
            for n in range(total_page[0]):
                self.global_dev_search_page.click_per_page(n)
                get_per_first_number = self.global_dev_search_page.get_per_frist_number_in_dev_search()
                self.assertEqual(get_per_first_number, str(10 * (n + 1) - 9))

            # 点击每页20条
            list = [20, 30, 50, 100]
            for m in list:
                self.global_dev_search_page.click_per_page_number()
                page_number = self.global_dev_search_page.get_page_number_in_dev_search()
                if int(total_page[1] % m) != 0:
                    a = int(total_page[1] / m) + 1
                else:
                    a = int(total_page[1] / m)
                self.assertEqual(a, page_number)
