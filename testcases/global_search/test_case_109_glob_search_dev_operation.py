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


class TestCase109GlobSearchDevOperation(unittest.TestCase):
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

    def test_case_global_search_dev_operation(self):
        # 打开途强在线首页-登录页
        self.base_page.open_page()
        self.base_page.click_chinese_button()
        self.log_in_base.log_in_jimitest()
        self.log_in_base.click_account_center_button()
        self.global_dev_search_page.click_easy_search()
        # 关闭
        self.global_dev_search_page.close_search()
        sleep(2)

        self.global_dev_search_page.click_easy_search()

        # 选择用户搜索
        self.global_dev_search_page.click_search_buttons()

        # 获取设备信息
        dev_name = self.global_dev_search_page.get_dev_name_in_dev_search()
        dev_imei = self.global_dev_search_page.get_dev_imei_in_dev_search()
        dev_type = self.global_dev_search_page.get_dev_type_in_dev_search()
        dev_active_time = self.global_dev_search_page.get_dev_active_time_in_dev_search()
        dev_expire_time = self.global_dev_search_page.get_dev_expire_time_in_dev_search()

        # 点击轨迹回放
        current_handle = self.driver.get_current_window_handle()
        self.global_dev_search_page.click_track_play_button_in_dev_search()
        all_handles = self.driver.get_all_window_handles()
        for handle in all_handles:
            if handle != current_handle:
                self.driver.switch_to_window(handle)

                self.assertEqual(self.base_url + '/trackreplay/locus?imei=%s' % dev_imei, self.driver.get_current_url())
                # 获取页面的抬头的文字
                text = self.global_dev_search_page.get_text_after_click_track_play()
                self.assertEqual(self.assert_text.dev_page_track_replay_text(), text)
                # 获取页面抬头的设备名称和imei
                dev_name_and_dev_imei = self.global_dev_search_page.get_dev_name_and_imei_after_click_track_play()
                self.assertIn(dev_name, dev_name_and_dev_imei)
                self.assertIn(dev_imei, dev_name_and_dev_imei)
                self.driver.close_current_page()
                sleep(2)
                self.driver.switch_to_window(current_handle)

        # 点击实时跟踪
        current_handle = self.driver.get_current_window_handle()
        self.global_dev_search_page.click_track_preset_button_in_dev_search()
        all_handles = self.driver.get_all_window_handles()
        for handle in all_handles:
            if handle != current_handle:
                self.driver.switch_to_window(handle)

                self.assertEqual(self.base_url + '/trackpreset/tracking/%s?isTracking=0' % dev_imei,
                                 self.driver.get_current_url())
                # 获取页面的抬头的文字
                text = self.global_dev_search_page.get_text_after_click_track_preset()
                self.assertIn(self.assert_text.dev_page_track_preset_text(), text)
                # 获取页面抬头的设备名称和imei
                dev_name_in_track_preset = self.global_dev_search_page.get_dev_name_in_track_preset()
                dev_imei_in_track_preset = self.global_dev_search_page.get_imei_in_track_preset()
                self.assertEqual(dev_imei, dev_imei_in_track_preset)
                self.assertEqual(dev_name, dev_name_in_track_preset)
                self.driver.close_current_page()
                sleep(2)
                self.driver.switch_to_window(current_handle)

        # 点击查看告警
        current_handle = self.driver.get_current_window_handle()
        self.global_dev_search_page.click_look_alarm_button_in_dev_search()
        all_handles = self.driver.get_all_window_handles()
        for handle in all_handles:
            if handle != current_handle:
                self.driver.switch_to_window(handle)

                self.assertEqual(self.base_url + '/deviceReport/statisticalReport', self.driver.get_current_url())
                # 获取页面的抬头的文字
                text = self.global_dev_search_page.get_text_after_click_alarm_detail()
                self.assertEqual(self.assert_text.account_center_page_alarm_details_text(), text)
                # 获取页面抬头的设备名称和ime
                self.driver.close_current_page()
                sleep(2)
                self.driver.switch_to_window(current_handle)

        # 点击详情
        self.global_dev_search_page.click_detail_in_dev_search()
        # 获取设备的名称 imei、设备类型、激活时间、平台到期时间
        dev_name_in_detail = self.global_dev_search_page.get_dev_name_in_detail()
        self.assertEqual(dev_name, dev_name_in_detail)

        dev_imei_in_detail = self.global_dev_search_page.get_dev_imei_in_detail()
        self.assertEqual(dev_imei, dev_imei_in_detail)

        dev_type_in_detail = self.global_dev_search_page.get_dev_type_in_detail()
        self.assertEqual(dev_type, dev_type_in_detail)

        dev_active_time_in_detail = self.global_dev_search_page.get_dev_active_time_in_detail()
        self.assertEqual(dev_active_time, dev_active_time_in_detail)

        dev_expire_time_in_detail = self.global_dev_search_page.get_dev_expire_time_in_detail()
        self.assertEqual(dev_expire_time, dev_expire_time_in_detail)
