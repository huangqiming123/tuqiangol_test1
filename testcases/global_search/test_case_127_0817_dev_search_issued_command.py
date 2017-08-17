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


class TestCase127DevSearchIssuedCommand(unittest.TestCase):
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

    def test_case_dev_search_issued_command(self):
        # 打开途强在线首页-登录页
        self.base_page.open_page()
        self.base_page.click_chinese_button()
        self.log_in_base.log_in()
        self.log_in_base.click_account_center_button()
        self.global_dev_search_page.click_easy_search()
        # 关闭
        self.global_dev_search_page.close_search()
        sleep(2)
        self.global_dev_search_page.click_easy_search()
        # 选择设备搜索
        self.global_dev_search_page.click_search_buttons()
        sleep(5)
        self.global_dev_search_page.swith_to_search_frame()
        sleep(5)
        # 点击详情
        self.global_dev_search_page.click_dev_detail_after_search_dev()

        get_imei = self.global_dev_search_page.get_imei_in_dev_detail()
        get_dev_name = self.global_dev_search_page.get_dev_types_in_dev_detail()

        # 点击设备指令
        self.global_dev_search_page.clcik_dev_command_button()

        get_imei_in_command_page = self.global_dev_search_page.get_dev_imei_in_command_page()
        get_dev_name_in_command_page = self.global_dev_search_page.get_dev_name_in_command_page()

        self.assertEqual(get_imei, get_imei_in_command_page)
        self.assertEqual(get_dev_name, get_dev_name_in_command_page)
