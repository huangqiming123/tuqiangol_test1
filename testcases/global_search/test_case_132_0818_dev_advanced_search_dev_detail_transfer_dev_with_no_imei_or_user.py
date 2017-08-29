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


class TestCase132DevAdvancedSearchDevDetailTransferDevWithNoImeiOrUser(unittest.TestCase):
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

    def test_case_dev_advanced_search_dev_detail_transfer_dev_with_no_imei_or_user(self):
        # 打开途强在线首页-登录页
        self.base_page.open_page()
        self.log_in_base.log_in()
        self.log_in_base.click_account_center_button()
        self.global_dev_search_page.click_easy_search()
        # 关闭
        self.global_dev_search_page.close_search()
        sleep(2)
        self.global_dev_search_page.click_easy_search()
        sleep(3)
        self.global_dev_search_page.swith_to_search_frame()
        self.global_dev_search_page.click_advanced_search_button()

        # 点击搜索按钮
        self.global_dev_search_page.click_search_buttons_in_dev_advanced_search_page()
        sleep(4)
        # 点击详情
        self.global_dev_search_page.click_detail_button_in_dev_advanced_search_page()
        sleep(2)
        get_imei_in_dev_advanced_detail_page = self.global_dev_search_page.get_imei_after_click_detail_button_in_dev_advanced()
        # 点击转移设备
        self.global_dev_search_page.click_transfer_dev_button_in_dev_detail()
        # 断言imei
        imei_in_transfer_dev_page = self.global_dev_search_page.get_dev_imei_in_transfer_dev_page()
        self.assertEqual(get_imei_in_dev_advanced_detail_page, imei_in_transfer_dev_page)

        dev_user_account_by_sql = self.global_dev_search_page.get_dev_user_account_by_sql(imei_in_transfer_dev_page)
        get_dev_user_account_in_transfer_page = self.global_dev_search_page.get_dev_user_account_in_transfer_page()
        self.assertEqual(dev_user_account_by_sql, get_dev_user_account_in_transfer_page)

        # 已选列表IMEI不为空，转移给用户为空，点击转移
        # 点击转移按钮
        self.global_dev_search_page.click_transfer_button_in_transfer_page()
        text = self.global_dev_search_page.get_text_after_click_transfer_button()
        self.assertEqual(self.assert_text.glob_search_please_add_account_text(), text)

        # 已选列表IMEI为空，选择转移给用户，点击转移
        # 删除设备  然后 选择一个用户
        self.global_dev_search_page.clcik_dev_imei_in_transfer_page()
        self.global_dev_search_page.click_user_to_transfer_dev_in_transfer_dev_page()

        self.global_dev_search_page.click_transfer_button_in_transfer_page()
        text = self.global_dev_search_page.get_text_after_click_transfer_button()
        self.assertEqual(self.assert_text.glob_search_please_add_dev_text(), text)

        ## 已选列表IMEI为空，转移给用户为空，点击转移
        # 点击重置的按钮
        self.global_dev_search_page.click_reset_button_in_transfer_page()
        self.global_dev_search_page.click_transfer_button_in_transfer_page()
        text = self.global_dev_search_page.get_text_after_click_transfer_button()
        self.assertEqual(self.assert_text.glob_search_please_add_account_text(), text)
