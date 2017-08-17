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


class TestCase130DevSearchDetailUserRelation(unittest.TestCase):
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

    def test_case_dev_search_detail_user_relation(self):
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
        sleep(3)
        self.global_dev_search_page.swith_to_search_frame()
        self.global_dev_search_page.click_advanced_search_button()

        # 点击搜索按钮
        self.global_dev_search_page.click_search_buttons_in_dev_advanced_search_page()
        sleep(4)
        # 点击详情
        self.global_dev_search_page.click_detail_button_in_dev_advanced_search_page()
        get_imei_in_dev_advanced_detail_page = self.global_dev_search_page.get_imei_after_click_detail_button_in_dev_advanced()
        # 点击轨迹回放
        current_handle = self.driver.get_current_window_handle()
        self.global_dev_search_page.click_tracker_play_button_in_dev_advanced_page()
        all_handles = self.driver.get_all_window_handles()
        for handle in all_handles:
            if handle != current_handle:
                self.driver.switch_to_window(handle)
                expect_url = self.base_url + '/trackreplay/locus?imei=%s' % get_imei_in_dev_advanced_detail_page
                self.assertEqual(expect_url, self.driver.get_current_url())

                # 获取轨迹回放页面的imei
                get_imei_in_tracker_play = self.global_dev_search_page.get_imei_after_click_tracker_play_in_tracker_play()
                self.assertIn(get_imei_in_dev_advanced_detail_page, get_imei_in_tracker_play)

                self.driver.close_current_page()
                self.driver.switch_to_window(current_handle)

        # 点击实时跟踪(离线设备按钮灰暗显示不可选)
        current_handle = self.driver.get_current_window_handle()
        self.global_dev_search_page.swith_to_search_frame()
        self.global_dev_search_page.click_track_preset_button_in_dev_advanced_page()
        all_handles = self.driver.get_all_window_handles()
        for handle in all_handles:
            if handle != current_handle:
                self.driver.switch_to_window(handle)
                expect_url = self.base_url + '/trackpreset/tracking/%s?isTracking=0' % get_imei_in_dev_advanced_detail_page
                get_imei_in_track_preset = self.global_dev_search_page.get_imei_in_track_preset()
                self.assertEqual(expect_url, self.driver.get_current_url())
                self.assertEqual(get_imei_in_dev_advanced_detail_page, get_imei_in_track_preset)
                self.driver.close_current_page()
                self.driver.switch_to_window(current_handle)

        # 点击查看告警
        current_handle = self.driver.get_current_window_handle()
        self.global_dev_search_page.swith_to_search_frame()
        self.global_dev_search_page.click_alarm_detail_button_in_dev_advanced_page()
        all_handles = self.driver.get_all_window_handles()
        for handle in all_handles:
            if handle != current_handle:
                self.driver.switch_to_window(handle)
                expect_url = self.base_url + '/deviceReport/statisticalReport'
                self.assertEqual(expect_url, self.driver.get_current_url())
                self.driver.close_current_page()
                self.driver.switch_to_window(current_handle)

        # 点击查看位置
        current_handle = self.driver.get_current_window_handle()
        self.global_dev_search_page.swith_to_search_frame()
        self.global_dev_search_page.click_look_loacltion_button_in_dev_advanced_page()
        all_handles = self.driver.get_all_window_handles()
        for handle in all_handles:
            if handle != current_handle:
                self.driver.switch_to_window(handle)
                expect_url = self.base_url + '/console'
                self.assertEqual(expect_url, self.driver.get_current_url())
                self.driver.close_current_page()
                self.driver.switch_to_window(current_handle)

        # 点击控制台
        current_handle = self.driver.get_current_window_handle()
        self.global_dev_search_page.swith_to_search_frame()
        self.global_dev_search_page.click_console_button_in_dev_advanced()
        all_handles = self.driver.get_all_window_handles()
        for handle in all_handles:
            if handle != current_handle:
                self.driver.switch_to_window(handle)
                expect_url = self.base_url + '/console'
                self.assertEqual(self.driver.get_current_url(), expect_url)
                self.driver.close_current_page()
                self.driver.switch_to_window(current_handle)

        # 点击查看
        current_handle = self.driver.get_current_window_handle()
        self.global_dev_search_page.swith_to_search_frame()
        get_user_dev_number = self.global_dev_search_page.get_user_dev_number_in_dev_advanced()
        self.global_dev_search_page.click_look_button_in_dev_advanced()
        all_handles = self.driver.get_all_window_handles()
        for handle in all_handles:
            if handle != current_handle:
                self.driver.switch_to_window(handle)
                expect_url = self.base_url + '/device/toDeviceManage'
                self.assertEqual(self.driver.get_current_url(), expect_url)

                get_dev_total_in_dev_page = self.global_dev_search_page.get_user_dev_total_number_in_dev_page()
                self.assertEqual(get_user_dev_number, str(get_dev_total_in_dev_page))
                self.driver.close_current_page()
                self.driver.switch_to_window(current_handle)
