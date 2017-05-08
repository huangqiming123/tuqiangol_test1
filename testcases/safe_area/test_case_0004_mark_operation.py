import unittest
from time import sleep

from automate_driver.automate_driver import AutomateDriver
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.safe_area.safe_area_page import SafeAreaPage
from pages.safe_area.safe_area_page_read_csv import SafeAreaPageReadCsv


class TestCase0004MarkOperation(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.log_in_base = LogInBase(self.driver, self.base_url)
        self.safe_area_page = SafeAreaPage(self.driver, self.base_url)

        self.base_page.open_page()
        self.driver.set_window_max()
        self.log_in_base.log_in()
        self.current_account = self.log_in_base.get_log_in_account()
        self.safe_area_page.click_control_after_click_safe_area()
        self.safe_area_page_read_csv = SafeAreaPageReadCsv()

    def tearDown(self):
        self.driver.quit_browser()

    def test_case_0004_mark_operation(self):
        # 断言url
        expect_url = self.base_url + "/safearea/geozonemap?flag=0"
        self.assertEqual(expect_url, self.driver.get_current_url())

        self.safe_area_page.click_mark_button()
        sleep(2)

        self.safe_area_page.click_all_select_button_with_mark()
        # 点击删除
        self.safe_area_page.click_detele_button_with_mark()
        # 点击取消
        self.safe_area_page.click_cancel_detele_button()

        # 点击删除
        self.safe_area_page.click_detele_button_with_mark()
        # 点击取消
        self.safe_area_page.click_close_detele_button()

        # 点击列表的编辑
        self.safe_area_page.click_edit_button_in_list()
        # 点击保存
        self.safe_area_page.click_ensure_edit_in_list('名称','描述')

        # 点击列表的编辑
        self.safe_area_page.click_edit_button_in_list()
        # 点击保存
        self.safe_area_page.click_cancel_edit_in_list()

        # 点击列表的编辑
        self.safe_area_page.click_edit_button_in_list()
        # 点击保存
        self.safe_area_page.click_close_edit_in_list()

        # 点击列表中的删除
        self.safe_area_page.click_delete_button_in_list()
        self.safe_area_page.click_cancel_detele_button()

        self.safe_area_page.click_delete_button_in_list()
        self.safe_area_page.click_close_detele_button()