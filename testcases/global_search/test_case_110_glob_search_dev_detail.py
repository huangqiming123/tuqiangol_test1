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


class TestCase110GlobSearchDevDetail(unittest.TestCase):
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

    def test_case_1107_global_search_dev_detail(self):
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
        self.global_dev_search_page.click_dev_search_button()
        self.global_dev_search_page.click_detail_in_dev_search()
        dev_name_in_detail = self.global_dev_search_page.get_dev_name_in_detail()
        dev_imei_in_detail = self.global_dev_search_page.get_dev_imei_in_detail()
        dev_type_in_detail = self.global_dev_search_page.get_dev_type_in_detail()
        dev_active_time_in_detail = self.global_dev_search_page.get_dev_active_time_in_detail()
        dev_expire_time_in_detail = self.global_dev_search_page.get_dev_expire_time_in_detail()

        # 点击轨迹回放
        current_handle = self.driver.get_current_window_handle()
        self.global_dev_search_page.click_track_play_button_in_dev_detail()
        all_handles = self.driver.get_all_window_handles()
        for handle in all_handles:
            if handle != current_handle:
                self.driver.switch_to_window(handle)

                self.assertEqual(self.base_url + '/trackreplay/locus?imei=%s' % dev_imei_in_detail,
                                 self.driver.get_current_url())
                # 获取页面的抬头的文字
                text = self.global_dev_search_page.get_text_after_click_track_play()
                self.assertEqual(self.assert_text.dev_page_track_replay_text(), text)
                # 获取页面抬头的设备名称和imei
                dev_name_and_dev_imei = self.global_dev_search_page.get_dev_name_and_imei_after_click_track_play()
                self.assertIn(dev_imei_in_detail, dev_name_and_dev_imei)
                self.assertIn(dev_name_in_detail, dev_name_and_dev_imei)
                self.driver.close_current_page()
                sleep(2)
                self.driver.switch_to_window(current_handle)

        # 点击实时跟踪
        current_handle = self.driver.get_current_window_handle()
        self.global_dev_search_page.click_track_preset_button_in_dev_detail()
        all_handles = self.driver.get_all_window_handles()
        for handle in all_handles:
            if handle != current_handle:
                self.driver.switch_to_window(handle)

                self.assertEqual(self.base_url + '/trackpreset/tracking/%s?isTracking=0' % dev_imei_in_detail,
                                 self.driver.get_current_url())
                # 获取页面的抬头的文字
                text = self.global_dev_search_page.get_text_after_click_track_preset()
                self.assertIn(self.assert_text.dev_page_track_preset_text(), text)
                # 获取页面抬头的设备名称和imei
                dev_name_in_track_preset = self.global_dev_search_page.get_dev_name_in_track_preset()
                dev_imei_in_track_preset = self.global_dev_search_page.get_imei_in_track_preset()
                self.assertEqual(dev_imei_in_detail, dev_imei_in_track_preset)
                self.assertEqual(dev_name_in_detail, dev_name_in_track_preset)
                self.driver.close_current_page()
                sleep(2)
                self.driver.switch_to_window(current_handle)

        # 点击查看告警
        current_handle = self.driver.get_current_window_handle()
        self.global_dev_search_page.click_look_alarm_button_in_dev_detail()
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

        # 点击查看位置
        current_handle = self.driver.get_current_window_handle()
        self.global_dev_search_page.click_look_place_button_in_dev_detail()
        all_handles = self.driver.get_all_window_handles()
        for handle in all_handles:
            if handle != current_handle:
                self.driver.switch_to_window(handle)

                self.assertEqual(self.base_url + '/console', self.driver.get_current_url())
                # 获取页面的抬头的文字
                text = self.global_dev_search_page.get_text_after_click_look_place()
                # self.assertEqual(dev_imei_in_detail, text)
                # get_dev_name = self.global_dev_search_page.get_type_after_click_look_place()
                # self.assertEqual(dev_name_in_detail, get_dev_name)
                # 获取页面抬头的设备名称和ime
                self.driver.close_current_page()
                sleep(2)
                self.driver.switch_to_window(current_handle)

        # 点击设备信息
        sleep(1)
        self.global_dev_search_page.click_dev_info_button_in_dev_detail()
        sleep(2)
        # 验证设备的信息
        dev_imei_in_dev_info = self.global_dev_search_page.get_dev_imei_in_dev_info()
        self.assertEqual(dev_imei_in_detail, dev_imei_in_dev_info)

        dev_type_in_dev_info = self.global_dev_search_page.get_dev_type_in_dev_info()
        self.assertEqual(dev_type_in_detail, dev_type_in_dev_info)

        dev_name_in_dev_info = self.global_dev_search_page.get_dev_name_in_dev_info()
        self.assertEqual(dev_name_in_detail, dev_name_in_dev_info)

        # 点击设备转移
        self.global_dev_search_page.click_dev_tran_button_in_dev_detail()

        # 循环点击右侧客户树
        for n in range(5):
            self.global_dev_search_page.click_customer(n)
            get_customer_name_in_header = self.global_dev_search_page.get_customer_name_in_header()
            get_click_customer_name = self.global_dev_search_page.get_click_customer_name(n)
            self.assertEqual(get_customer_name_in_header, get_click_customer_name)

        # 搜索无数据的用户
        self.global_dev_search_page.search_user_in_dev_detail('无数据')
        text = self.global_dev_search_page.get_text_after_search_user_in_dev_detail()
        self.assertIn(self.assert_text.account_center_page_no_data_text(), text)

        # 添加已经添加的设备
        self.global_dev_search_page.add_dev_to_trans(dev_imei_in_detail)
        get_file_imei = self.global_dev_search_page.get_file_imei_after_add_imei()
        self.assertEqual(dev_imei_in_detail, get_file_imei)

        get_file_reason = self.global_dev_search_page.get_file_reason_add_imei()
        self.assertEqual(self.assert_text.dev_page_repetition_text(), get_file_reason)

        get_file_status = self.global_dev_search_page.get_file_status()
        self.assertEqual(self.assert_text.dev_page_fail_text(), get_file_status)

        # 点击关闭失败信息
        self.global_dev_search_page.close_file_info()

        # 添加不存在的
        self.global_dev_search_page.add_dev_to_trans(dev_imei_in_detail + '12345')
        get_file_imei = self.global_dev_search_page.get_file_imei_after_add_imei()
        self.assertEqual(dev_imei_in_detail + '12345', get_file_imei)

        get_file_reason = self.global_dev_search_page.get_file_reason_add_imei()
        self.assertEqual(self.assert_text.dev_page_inexistence_text(), get_file_reason)

        get_file_status = self.global_dev_search_page.get_file_status()
        self.assertEqual(self.assert_text.dev_page_fail_text(), get_file_status)

        self.global_dev_search_page.close_file_info()

        # 点击删除设备
        sleep(2)
        self.global_dev_search_page.click_detele_dev_in_dev_tran()
        # 点击转移
        self.global_dev_search_page.click_trans_dev_button()
        # 获取错误提示语
        get_text = self.global_dev_search_page.get_text_after_click_trans_dev()
        self.assertEqual(self.assert_text.glob_search_please_add_dev_text(), get_text)

        # 点击重置
        self.global_dev_search_page.click_reset_button()
        # 点击转移
        self.global_dev_search_page.click_trans_dev_button()
        # 获取错误提示语
        get_text = self.global_dev_search_page.get_text_after_click_trans_dev()
        self.assertEqual(self.assert_text.glob_search_please_add_account_text(), get_text)

        # 点击设备指令
        self.global_dev_search_page.click_dev_command_button()

        # 获取指令页面的设备名称和设备imei
        dev_imei_in_command = self.global_dev_search_page.get_dev_imei_in_command()
        dev_name_in_command = self.global_dev_search_page.get_dev_name_in_command()
        self.assertEqual(dev_imei_in_detail, dev_imei_in_command)
        self.assertEqual(dev_name_in_detail, dev_name_in_command)
