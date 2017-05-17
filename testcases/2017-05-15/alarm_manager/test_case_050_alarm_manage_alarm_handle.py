import unittest
from time import sleep

from automate_driver.automate_driver import AutomateDriver
from pages.alarm_manager.alarm_manage_page import AlarmManagePage
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase


class TestCase050AlarmManageAlarmHandle(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.log_in_base = LogInBase(self.driver, self.base_url)
        self.alarm_manage_page = AlarmManagePage(self.driver, self.base_url)

        self.base_page.open_page()
        self.driver.set_window_max()
        self.log_in_base.log_in()
        self.account = self.log_in_base.get_log_in_account()

    def tearDown(self):
        self.driver.quit_browser()

    def test_case_alarm_manage_alarm_handle(self):
        self.alarm_manage_page.click_alarm_icon()
        sleep(3)
        # 断言
        self.assertEqual(' 报警管理', self.alarm_manage_page.get_text_after_click_alarm_icon())

        # 点击全部标记为已读
        self.driver.click_element('x,/html/body/div[7]/div[1]/div/a')
        sleep(2)

        text = self.driver.get_text('x,/html/body/div[7]/div[2]/div[2]/table/tbody/tr[1]/td[8]/a')

        if text == '处理':

            # 点击告警处理
            self.alarm_manage_page.click_alarm_handle_button()
            # 断言
            self.assertEqual('告警处理', self.alarm_manage_page.get_text_after_click_alarm_handle())
            # 点击关闭
            self.alarm_manage_page.close_alarm_handle()
            sleep(2)

            # 点击告警处理
            self.alarm_manage_page.click_alarm_handle_button()
            # 断言
            self.assertEqual('告警处理', self.alarm_manage_page.get_text_after_click_alarm_handle())
            # 点击关闭
            self.alarm_manage_page.cancel_alarm_handle()
            sleep(2)

            # 点击告警处理
            self.alarm_manage_page.click_alarm_handle_button()
            # 断言
            self.assertEqual('告警处理', self.alarm_manage_page.get_text_after_click_alarm_handle())
            # 点击关闭
            self.alarm_manage_page.save_alarm_handle()
            sleep(2)

        elif text == '查看处理':
            self.alarm_manage_page.click_alarm_handle_button()

            # 断言
            self.assertEqual('查看处理', self.driver.get_text('x,/html/body/div[9]/div/div/div[1]/h4'))
            self.assertEqual(self.account,
                             self.driver.get_text('x,/html/body/div[9]/div/div/div[2]/div/form/div[2]/div/label'))
            self.driver.click_element('x,/html/body/div[9]/div/div/div[1]/button')
            sleep(2)
