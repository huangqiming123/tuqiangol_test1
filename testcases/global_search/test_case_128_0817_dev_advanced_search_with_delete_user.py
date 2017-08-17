import csv
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


class TestCase128DevAdvancedSearchWithDeleteUser(unittest.TestCase):
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

    def test_case_dev_advanced_search_with_delete_user(self):
        # 打开途强在线首页-登录页
        self.base_page.open_page()
        self.log_in_base.log_in()

        self.global_account_search_page.click_cust_manager_button()
        csv_file = self.global_search_page_read_csv.read_csv('new_user_info.csv')
        csv_data = csv.reader(csv_file)

        is_header = True
        for row in csv_data:
            if is_header:
                is_header = False
                continue
            add_data = {
                'account_type': row[0],
                'account_name': row[1],
                'account': row[2]
            }
            self.global_account_search_page.click_add_new_user_button()
            self.global_account_search_page.click_close_add_user_page()
            self.global_account_search_page.click_add_new_user_button()
            self.global_account_search_page.switch_to_add_user_frame()
            self.global_account_search_page.add_data_to_add_new_user(add_data)
            # 删除
            self.global_account_search_page.search_user_by_account_in_cust_manage(add_data['account'])

            self.log_in_base.click_account_center_button()
            self.global_dev_search_page.click_easy_search()
            # 关闭
            self.global_dev_search_page.close_search()
            sleep(2)
            self.global_dev_search_page.click_easy_search()
            # 选择设备搜索--高级搜索
            self.global_dev_search_page.swith_to_search_frame()
            self.global_dev_search_page.click_advanced_search_button()

            # 搜索已经删除的用户名称
            self.global_dev_search_page.click_search_button_in_dev_advanced_search_page()
            # 输入删除的用户名称搜索
            self.global_dev_search_page.add_user_name_to_search_in_dev_advanced_search_page(add_data['account'])

            get_text = self.global_dev_search_page.get_text_after_click_search_button_in_dev_advanced_search_page()
            self.assertIn(self.assert_text.account_center_page_no_data_text(), get_text)
            break
        csv_file.close()
