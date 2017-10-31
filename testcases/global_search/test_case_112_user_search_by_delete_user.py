import csv
import unittest
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


class TestCase112UserSearchByDeleteUser(unittest.TestCase):
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

    def test_user_search_by_delete_user(self):
        # 打开途强在线首页-登录页
        self.base_page.open_page()
        self.log_in_base.log_in()
        # 分别新建 销售、代理商、用户并删除，然后搜索
        # 点击客户管理

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
            self.global_dev_search_page.swith_to_search_frame()
            self.global_account_search_page.add_data_to_add_new_user(add_data)

            # 先搜索
            self.global_account_search_page.click_global_search_button()
            self.global_account_search_page.click_close_add_user_page()
            self.global_account_search_page.click_global_search_button()
            self.global_account_search_page.switch_to_search_user_frame()

            self.global_account_search_page.search_user_by_account_in_global_search(add_data['account'])
            get_user_account = self.global_account_search_page.get_user_account_after_search()
            self.assertEqual(get_user_account, add_data['account'])
            self.driver.default_frame()
            self.global_account_search_page.click_close_add_user_page()

            # 删除
            self.global_account_search_page.search_user_by_account_in_cust_manage(add_data['account'])

            # 打开全局搜索，搜索用户
            self.global_account_search_page.click_global_search_button()
            self.global_account_search_page.click_close_add_user_page()
            self.global_account_search_page.click_global_search_button()
            self.global_dev_search_page.swith_to_search_frame()

            self.global_account_search_page.search_user_by_account_in_global_search(add_data['account'])

            get_text = self.global_account_search_page.get_text_after_search()
            self.assertIn(self.assert_text.account_center_page_no_data_text(), get_text)
            self.driver.default_frame()
            self.global_account_search_page.click_close_add_user_page()
        csv_file.close()
