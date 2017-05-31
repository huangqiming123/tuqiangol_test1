import unittest
from time import sleep

from automate_driver.automate_driver import AutomateDriver
from model.connect_sql import ConnectSql
from pages.account_center.account_center_navi_bar_pages import AccountCenterNaviBarPages
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.global_search.global_account_search_page import GlobalAccountSearchPage
from pages.global_search.global_dev_search_page import GlobalDevSearchPage
from pages.global_search.global_search_page_read_csv import GlobleSearchPageReadCsv
from pages.global_search.search_sql import SearchSql


class TestCase1103GlobSearchAppDetailOperation(unittest.TestCase):
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
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_case_1103_global_search_app_detail_operation(self):
        # 打开途强在线首页-登录页
        self.base_page.open_page()
        self.log_in_base.log_in_jimitest()
        self.global_dev_search_page.click_easy_search()
        # 关闭
        self.global_dev_search_page.close_search()
        sleep(2)

        self.global_dev_search_page.click_easy_search()
        self.global_dev_search_page.select_search_app_user()

        # 点击搜索
        self.global_dev_search_page.click_search_button()
        # 点击详情
        self.global_dev_search_page.click_detail_in_app_user_search()

        # 点击控制台
        current_handle = self.driver.get_current_window_handle()
        self.global_dev_search_page.click_console_button_in_app_detail()
        all_handles = self.driver.get_all_window_handles()
        for handle in all_handles:
            if handle != current_handle:
                self.driver.switch_to_window(handle)

                self.assertEqual(self.base_url + '/console', self.driver.get_current_url())
                self.driver.close_current_page()
                sleep(2)
                self.driver.switch_to_window(current_handle)

        # 重置密码
        # 点击重置密码
        self.global_dev_search_page.click_reset_password_button_in_app_detail()
        # 点击关闭
        self.global_dev_search_page.close_button()

        # 点击重置密码
        self.global_dev_search_page.click_reset_password_button_in_app_detail()
        # 点击关闭
        self.global_dev_search_page.cancel_button()

        # 点击重置密码
        self.global_dev_search_page.click_reset_password_button_in_app_detail()
        # 点击关闭
        self.global_dev_search_page.ensure_button()

        get_text = self.global_dev_search_page.get_text_after_succeed()
        self.assertEqual('操作成功', get_text)

        # 获取app用户详情页面绑定的设备信息
        get_dev_name = self.global_dev_search_page.get_dev_name_in_app_detail()
        get_dev_imei = self.global_dev_search_page.get_dev_imei_in_app_detail()
        get_dev_type = self.global_dev_search_page.get_dev_type_in_app_detail()
        get_dev_active_time = self.global_dev_search_page.get_dev_active_time_in_app_detail()
        get_dev_expire_time = self.global_dev_search_page.get_dev_expire_time_in_app_detail()
        get_dev_bound_user = self.global_dev_search_page.get_dev_bound_user_in_app_detail()

        # 点击设备的操作
        # 详情
        self.global_dev_search_page.click_dev_operation_detail_in_app_detail()

        # 获取点击设备详情后页面的数据
        dev_name = self.global_dev_search_page.get_dev_name_in_dev_detail()
        self.assertEqual(get_dev_name, dev_name)

        dev_imei = self.global_dev_search_page.get_dev_imei_in_dev_detail()
        self.assertEqual(get_dev_imei, dev_imei)

        dev_type = self.global_dev_search_page.get_dev_type_in_dev_detail()
        self.assertEqual(get_dev_type, dev_type)

        dev_active_time = self.global_dev_search_page.get_dev_active_time_in_dev_detail()
        self.assertEqual(get_dev_active_time, dev_active_time)

        dev_expire_time = self.global_dev_search_page.get_dev_expire_time_in_dev_detail()
        self.assertEqual(get_dev_expire_time, dev_expire_time)

        dev_bound_user = self.global_dev_search_page.get_dev_bound_user_in_dev_detail()
        self.assertEqual(get_dev_bound_user, dev_bound_user)

        # 点击设备的轨迹回放、实时跟踪、查看告警
        self.global_dev_search_page.return_app_user_detail_list()

        # 点击轨迹回放
        current_handle = self.driver.get_current_window_handle()
        self.global_dev_search_page.click_track_replay_button_in_app_detail()
        all_handles = self.driver.get_all_window_handles()
        for handle in all_handles:
            if handle != current_handle:
                self.driver.switch_to_window(handle)
                self.assertEqual(self.base_url + '/trackreplay/locus?imei=%s' % dev_imei, self.driver.get_current_url())
                # 断言点击轨迹回放后的设备名称和 imei
                get_imei_in_replay = self.global_dev_search_page.get_imei_in_replay()
                self.assertEqual(dev_imei, get_imei_in_replay)
                get_dev_name_in_replay = self.global_dev_search_page.get_dev_name_in_replay()
                self.assertEqual(dev_name, get_dev_name_in_replay)
                self.driver.close_current_page()
                sleep(2)
                self.driver.switch_to_window(current_handle)

        # 点击实时跟踪
        current_handle = self.driver.get_current_window_handle()
        self.global_dev_search_page.click_track_preset_button_in_app_detail()
        all_handles = self.driver.get_all_window_handles()
        for handle in all_handles:
            if handle != current_handle:
                self.driver.switch_to_window(handle)
                self.assertEqual(self.base_url + '/trackpreset/tracking/%s?isTracking=0' % dev_imei,
                                 self.driver.get_current_url())
                # 断言点击轨迹回放后的设备名称和 imei
                get_imei_in_track_preset = self.global_dev_search_page.get_imei_in_track_preset()
                self.assertEqual(dev_imei, get_imei_in_track_preset)
                get_dev_name_in_track_preset = self.global_dev_search_page.get_dev_name_in_track_preset()
                self.assertIn(dev_name, get_dev_name_in_track_preset)
                self.driver.close_current_page()
                sleep(2)
                self.driver.switch_to_window(current_handle)

        # 点击查看告警
        current_handle = self.driver.get_current_window_handle()
        self.global_dev_search_page.click_alarm_detail_button_in_app_detail()
        all_handles = self.driver.get_all_window_handles()
        for handle in all_handles:
            if handle != current_handle:
                self.driver.switch_to_window(handle)
                self.assertEqual(self.base_url + '/deviceReport/statisticalReport', self.driver.get_current_url())
                # 断言
                text = self.global_dev_search_page.get_text_after_click_alarm_detail()
                self.assertEqual('告警详情', text)
                self.driver.close_current_page()
                sleep(2)
                self.driver.switch_to_window(current_handle)
