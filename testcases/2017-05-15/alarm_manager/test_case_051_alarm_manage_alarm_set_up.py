import unittest
from time import sleep

from automate_driver.automate_driver import AutomateDriver
from pages.alarm_manager.alarm_manage_page import AlarmManagePage
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase


class TestCase051AlarmManageAlarmSetUp(unittest.TestCase):
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

    def test_case_alarm_manage_alarm_set_up(self):
        self.alarm_manage_page.click_alarm_icon()
        # 断言
        self.assertEqual(' 报警管理', self.alarm_manage_page.get_text_after_click_alarm_icon())

        # 点击告警设置
        self.alarm_manage_page.click_alarm_alarm_set_up()
        # 断言
        self.assertEqual('告警设置', self.alarm_manage_page.get_text_after_click_alarm_set_up())
        # 点击关闭
        self.alarm_manage_page.click_close_alarm_set_up()

        # 点击告警设置
        self.alarm_manage_page.click_alarm_alarm_set_up()
        # 断言
        self.assertEqual('告警设置', self.alarm_manage_page.get_text_after_click_alarm_set_up())
        # 点击取消
        self.alarm_manage_page.click_cancel_alarm_set_up()

        # 点击告警设置
        self.alarm_manage_page.click_alarm_alarm_set_up()
        # 断言
        self.assertEqual('告警设置', self.alarm_manage_page.get_text_after_click_alarm_set_up())
        # 点击保存
        self.alarm_manage_page.click_save_alarm_set_up()

        # 点击推送设置
        self.alarm_manage_page.click_push_setting_button()

        # 获取有多少个设置
        number = self.alarm_manage_page.get_number_alarm_set_up()
        print(number)

        for n in range(number):
            self.driver.switch_to_frame('x,//*[@id="alarmModalFrame"]')
            el = self.driver.get_element('x,//*[@id="alarm_appSet_tbody"]/tr[%s]/td[3]/label/div/input' % str(n + 1))
            if n < 22:
                self.driver.execute_script(el)
            a = el.is_selected()
            self.driver.click_element('x,//*[@id="alarm_appSet_tbody"]/tr[%s]/td[3]/label/div/ins' % str(n + 1))
            sleep(5)

            if a == True:
                self.assertEqual(False, el.is_selected())
            elif a == False:
                self.assertEqual(True, el.is_selected())

            self.driver.default_frame()

        # 点击全部设置邮件
        self.alarm_manage_page.click_all_set_up_email()
        # 断言
        self.assertEqual('全部设置邮件发送 - 设置邮件发送', self.alarm_manage_page.get_text_after_click_all_set_up_email())
        # 取消
        self.alarm_manage_page.click_cancel_all_set_up_email()
        sleep(5)

        # 点击全部设置邮件
        self.alarm_manage_page.click_all_set_up_email()
        # 断言
        self.assertEqual('全部设置邮件发送 - 设置邮件发送', self.alarm_manage_page.get_text_after_click_all_set_up_email())
        # 取消
        self.alarm_manage_page.click_close_all_set_up_email()
        sleep(5)

        # 点击全部设置邮件
        self.alarm_manage_page.click_all_set_up_email()
        # 断言
        self.assertEqual('全部设置邮件发送 - 设置邮件发送', self.alarm_manage_page.get_text_after_click_all_set_up_email())
        # 保存
        self.alarm_manage_page.click_save_all_set_up_email()
        sleep(5)

        for n in range(number):
            self.driver.switch_to_frame('x,//*[@id="alarmModalFrame"]')
            el = self.driver.get_element('x,//*[@id="alarm_appSet_tbody"]/tr[%s]/td[4]/a' % str(n + 1))
            self.driver.execute_script(el)
            el.click()
            sleep(2)
            self.alarm_manage_page.click_save_set_up_email()
            sleep(5)
            self.driver.default_frame()
