import csv
import unittest
from time import sleep

from automate_driver.automate_driver import AutomateDriver
from model.assert_text import AssertText
from model.connect_sql import ConnectSql
from pages.account_center.account_center_navi_bar_pages import AccountCenterNaviBarPages
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.dev_manage.dev_manage_page_read_csv import DevManagePageReadCsv
from pages.dev_manage.dev_manage_pages import DevManagePages
from pages.dev_manage.search_sql import SearchSql


class TestCase79DevManageDevOperationActiveAndStart(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.dev_manage_page = DevManagePages(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPages(self.driver, self.base_url)
        self.log_in_base = LogInBase(self.driver, self.base_url)
        self.dev_manage_page_read_csv = DevManagePageReadCsv()
        self.connect_sql = ConnectSql()
        self.search_sql = SearchSql()
        self.assert_text = AssertText()
        self.driver.set_window_max()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_dev_manage_dev_operation_active_and_start(self):
        '''测试设备管理-设备搜索-by imei+设备名称+设备型号+车牌号+车架号+SIM'''

        # 打开途强在线首页-登录页
        self.base_page.open_page()
        # 登录
        self.log_in_base.log_in()

        self.dev_manage_page.enter_dev_manage()

        # 选择已激活和开机的设备
        self.dev_manage_page.choose_dev_active_and_statr()
        self.dev_manage_page.click_ensure()
        imei = self.dev_manage_page.get_imei_number()
        self.dev_manage_page.click_edit_button()
        self.dev_manage_page.click_close_edit_button()
        self.dev_manage_page.click_edit_button()

        csv_file = self.dev_manage_page_read_csv.read_csv('dev_operation_data.csv')
        csv_data = csv.reader(csv_file)

        for row in csv_data:
            self.data = {
                'dev_name': row[0],
                'sim': row[1],
                'mark': row[2],
                'd_name': row[3],
                'd_phone': row[4],
                'plate_numbers': row[5],
                'iccid': row[6],
                'sn': row[7],
                'vin': row[8],
                'engine_number': row[9],
                'install_time': row[10],
                'install_adress': row[11],
                'install_comp': row[12],
                'install_preson': row[13]
            }
            self.dev_manage_page.add_data_to_edit_dev_detila(self.data)
            # 验证是否修改成功
            sleep(3)
            text = self.dev_manage_page.get_dev_name()
            self.assertEqual(self.data['dev_name'], text)
        csv_file.close()

        # 点击查看位置
        current_handle = self.driver.get_current_window_handle()
        self.dev_manage_page.click_look_place_button()
        all_handles = self.driver.get_all_window_handles()
        for handle in all_handles:
            if handle != current_handle:
                self.driver.switch_to_window(handle)
                sleep(2)
                expect_url = self.base_url + "/console"
                self.assertEqual(expect_url, self.driver.get_current_url())

                # dev_name = self.dev_manage_page.get_dev_name_after_click_console()

                # self.assertEqual(self.data['dev_name'], dev_name)
                self.driver.close_current_page()

                self.driver.switch_to_window(current_handle)
                sleep(2)

        # 点击轨迹回放
        self.dev_manage_page.click_track_playback_button()
        all_handles = self.driver.get_all_window_handles()
        for handle in all_handles:
            if handle != current_handle:
                self.driver.switch_to_window(handle)
                sleep(2)
                expect_url = self.base_url + "/trackreplay/locus?imei=%s" % imei
                self.assertEqual(expect_url, self.driver.get_current_url())

                text = self.dev_manage_page.click_track_playback_get_text()
                self.assertEqual(self.assert_text.dev_page_track_replay_text(), text)
                self.driver.close_current_page()
                self.driver.switch_to_window(current_handle)
                sleep(2)

        # 点行车记录
        self.dev_manage_page.click_driving_recond_button()
        all_handles = self.driver.get_all_window_handles()
        for handle in all_handles:
            if handle != current_handle:
                self.driver.switch_to_window(handle)
                sleep(2)
                expect_url = self.base_url + "/drivingrecord/driving?imei=%s" % imei
                self.assertEqual(expect_url, self.driver.get_current_url())

                text = self.dev_manage_page.click_driving_recond_get_text()
                self.assertEqual(self.assert_text.dev_page_driving_record_text(), text)
                self.driver.close_current_page()
                self.driver.switch_to_window(current_handle)
                sleep(2)

        # 点街景
        self.dev_manage_page.click_street_scape_button()
        all_handles = self.driver.get_all_window_handles()
        for handle in all_handles:
            if handle != current_handle:
                self.driver.switch_to_window(handle)
                sleep(2)
                expect_url = self.base_url + "/trackpreset/tracking/%s?isTracking=1" % imei
                self.assertEqual(expect_url, self.driver.get_current_url())

                text = self.dev_manage_page.click_street_scape_get_text()
                self.assertIn(self.assert_text.dev_page_track_preset_text(), text)
                self.driver.close_current_page()
                self.driver.switch_to_window(current_handle)
                sleep(2)

        # 点查看告警
        self.dev_manage_page.click_look_alarm_button()
        all_handles = self.driver.get_all_window_handles()
        for handle in all_handles:
            if handle != current_handle:
                self.driver.switch_to_window(handle)
                sleep(2)
                expect_url = self.base_url + "/deviceReport/statisticalReport"
                self.assertEqual(expect_url, self.driver.get_current_url())

                text = self.dev_manage_page.click_look_alarm_get_text()
                self.assertEqual(self.assert_text.account_center_page_alarm_details_text(), text)
                self.driver.close_current_page()
                self.driver.switch_to_window(current_handle)
                sleep(2)
