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


class TestCase133DevAdvancedSearchDevDetailTransferDevWithDev(unittest.TestCase):
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

    def test_case_dev_advanced_search_dev_detail_transfer_dev_with_dev(self):
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
        get_second_imei = self.global_dev_search_page.get_second_imei_in_dev_advanced_page()
        get_third_imei = self.global_dev_search_page.get_third_imei_in_dev_advanced_page()
        get_fourth_imei = self.global_dev_search_page.get_fourth_imei_in_dev_advanced_page()
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

        # 输入所搜索到设备的相同IMEI，点击添加
        self.global_dev_search_page.add_dev_to_trans_in_transfer_page(imei_in_transfer_dev_page)

        # 获取失败的状态
        get_failure_statue_after_click_add_button = self.global_dev_search_page.get_add_failure_status_after_click_add_button()
        self.assertEqual(self.assert_text.dev_page_fail_text(), get_failure_statue_after_click_add_button)

        get_failure_reason_after_click_add_button = self.global_dev_search_page.get_add_failure_reason_after_click_add_button()
        self.assertEqual(self.assert_text.dev_page_repetition_text(), get_failure_reason_after_click_add_button)

        self.global_dev_search_page.click_close_failure_windows()

        ##　输入存在的不相同IMEI，点击添加
        self.global_dev_search_page.add_dev_to_trans_in_transfer_page(get_second_imei)

        get_total_dev_number = self.global_dev_search_page.get_total_dev_number_in_transfer_page()
        self.assertEqual('2', get_total_dev_number)

        get_second_dev_user_account = self.global_dev_search_page.get_dev_user_account_by_sql(get_second_imei)
        get_second_dev_user_account_in_transfer_page = self.global_dev_search_page.get_second_dev_user_account_in_transfer_page()
        self.assertEqual(get_second_dev_user_account, get_second_dev_user_account_in_transfer_page)

        # 输入不存在的设备IMEI，点击添加
        self.global_dev_search_page.add_dev_to_trans_in_transfer_page(get_second_imei + '1245')

        # 获取失败的状态
        get_failure_statue_after_click_add_button = self.global_dev_search_page.get_add_failure_status_after_click_add_button()
        self.assertEqual(self.assert_text.dev_page_fail_text(), get_failure_statue_after_click_add_button)

        get_failure_reason_after_click_add_button = self.global_dev_search_page.get_add_failure_reason_after_click_add_button()
        self.assertEqual(self.assert_text.dev_page_inexistence_text(), get_failure_reason_after_click_add_button)

        self.global_dev_search_page.click_close_failure_windows()

        # 输入存在的部分相同部分不相同IMEI，点击添加
        self.global_dev_search_page.add_dev_to_trans_in_transfer_page(get_second_imei + ',' + get_third_imei)
        # 获取失败的状态
        get_failure_statue_after_click_add_button = self.global_dev_search_page.get_add_failure_status_after_click_add_button()
        self.assertEqual(self.assert_text.dev_page_fail_text(), get_failure_statue_after_click_add_button)

        get_failure_reason_after_click_add_button = self.global_dev_search_page.get_add_failure_reason_after_click_add_button()
        self.assertEqual(self.assert_text.dev_page_repetition_text(), get_failure_reason_after_click_add_button)

        self.global_dev_search_page.click_close_failure_windows()

        # 　点击重置
        self.global_dev_search_page.click_reset_button_in_transfer_page()

        # 获取统计的数量
        get_total_dev_number = self.global_dev_search_page.get_total_dev_number_in_transfer_page()
        self.assertEqual('0', get_total_dev_number)
