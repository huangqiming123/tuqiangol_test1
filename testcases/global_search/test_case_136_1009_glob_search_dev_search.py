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


class TestCase136GlobSearchDevSearch(unittest.TestCase):
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

    def test_case_glob_search_dev_search(self):
        # 打开途强在线首页-登录页
        self.base_page.open_page()
        self.log_in_base.log_in()
        self.log_in_base.click_account_center_button()
        self.global_dev_search_page.click_easy_search()
        # 关闭
        self.global_dev_search_page.close_search()
        sleep(2)
        self.global_dev_search_page.click_easy_search()
        self.global_dev_search_page.swith_to_search_frame()
        self.global_dev_search_page.click_advanced_search_button()

        # 点击搜索按钮
        self.global_dev_search_page.click_search_buttons_in_dev_advanced_search_page()
        sleep(4)
        # 点击详情
        self.global_dev_search_page.click_detail_button_in_dev_advanced_search_page()
        sleep(2)

        # 获取设备的imei和状态
        get_dev_imei = self.global_dev_search_page.get_dev_imei_in_details()
        get_dev_status = self.global_dev_search_page.get_dev_status_in_dev_detail()

        # 点击关闭高级搜索
        self.driver.default_frame()
        self.global_dev_search_page.click_close_button()

        # 点击控制台
        self.global_dev_search_page.click_cancel_page_button()

        # 输入imei然后搜索
        self.global_dev_search_page.add_dev_imei_to_search_in_console(get_dev_imei)

        # 获取设备的状态在控制台页面
        get_dev_status_in_console_page = self.global_dev_search_page.get_dev_status_in_console_page()
        self.assertEqual(get_dev_status, get_dev_status_in_console_page)
