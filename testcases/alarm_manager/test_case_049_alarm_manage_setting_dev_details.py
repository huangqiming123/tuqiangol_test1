import unittest
from time import sleep

from automate_driver.automate_driver import AutomateDriver
from pages.alarm_manager.alarm_manage_page import AlarmManagePage

from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase


class TestCase049AlarmManageSettingDevDetails(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.log_in_base = LogInBase(self.driver, self.base_url)
        self.alarm_manage_page = AlarmManagePage(self.driver, self.base_url)

        self.base_page.open_page()
        self.driver.set_window_max()
        self.log_in_base.log_in()

    def tearDown(self):
        self.driver.quit_browser()

    def test_case_alarm_manage_setting_dev_details(self):
        self.alarm_manage_page.click_alarm_icon()
        # 断言
        self.assertEqual(' 报警管理', self.alarm_manage_page.get_text_after_click_alarm_icon())
        # 获取第一个imei的值
        imei = self.alarm_manage_page.get_first_imei_value()

        # 断言
        sleep(2)
        self.assertEqual('设备编辑', self.alarm_manage_page.get_text_after_click_first_imei())
        get_imei = self.alarm_manage_page.get_imei_after_click_imei()
        self.assertEqual(imei, get_imei)

        # 点击关闭
        self.alarm_manage_page.close_edit_dev_details()

        # 获取第一个imei的值
        imei = self.alarm_manage_page.get_first_imei_value()

        # 断言
        sleep(2)
        self.assertEqual('设备编辑', self.alarm_manage_page.get_text_after_click_first_imei())
        get_imei = self.alarm_manage_page.get_imei_after_click_imei()
        self.assertEqual(imei, get_imei)

        # 点击取消
        self.alarm_manage_page.cancel_edit_dev_details()

        # 获取第一个imei的值
        imei = self.alarm_manage_page.get_first_imei_value()

        # 断言
        sleep(2)
        self.assertEqual('设备编辑', self.alarm_manage_page.get_text_after_click_first_imei())
        get_imei = self.alarm_manage_page.get_imei_after_click_imei()
        self.assertEqual(imei, get_imei)

        # 点击取消
        self.alarm_manage_page.cancel_save_dev_details()
