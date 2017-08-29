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


class TestCase129DevAdvancedSearchGetBack(unittest.TestCase):
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

    def test_case_dev_advanced_search_get_back(self):
        # 打开途强在线首页-登录页
        self.base_page.open_page()
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

        # 获取列表中首页设备的imei号
        # 获取首页有多少条记录
        first_page_total_number = self.global_dev_search_page.get_first_page_total_number_in_dev_search()
        imei_list_first = []
        for n in range(first_page_total_number):
            imei = self.global_dev_search_page.get_imei_in_dev_search(n)
            imei_list_first.append(imei)

        # 点击高级按钮
        self.global_dev_search_page.click_advanced_search_button()

        # 获取高级搜索页面设备列表的imei
        first_page_total_number_in_advanced_search = self.global_dev_search_page.get_first_total_number_in_advanced_search()
        self.assertEqual(first_page_total_number, first_page_total_number_in_advanced_search)
        imei_list_second = []
        for x in range(first_page_total_number_in_advanced_search):
            imei = self.global_dev_search_page.get_imei_in_dev_advanced_search(x)
            imei_list_second.append(imei)

        self.assertEqual(imei_list_first, imei_list_second)

        # 点击返回按钮
        self.global_dev_search_page.click_get_back_button_in_advanced_search()
        # 获取首页有多少条记录
        third_page_total_number = self.global_dev_search_page.get_first_page_total_number_in_dev_search()
        self.assertEqual(first_page_total_number, third_page_total_number)
        imei_list_thrid = []
        for n in range(third_page_total_number):
            imei = self.global_dev_search_page.get_imei_in_dev_search(n)
            imei_list_thrid.append(imei)

        self.assertEqual(imei_list_thrid, imei_list_first)
