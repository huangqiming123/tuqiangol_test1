import unittest
from time import sleep

from automate_driver.automate_driver import AutomateDriver
from pages.alarm_info.alarm_info_page import AlarmInfoPage
from pages.base.base_page import BasePage
from pages.base.base_paging_function import BasePagingFunction
from pages.command_management.command_management_page import CommandManagementPage
from pages.login.login_page import LoginPage


class TestTase143EnclosureSetUpAddEnclosure(unittest.TestCase):
    '''
    用例第143条，围栏设置，创建围栏
    author:zhangAo
    '''

    def setUp(self):
        # 前置条件
        # 实例化对象
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.log_in_page = LoginPage(self.driver, self.base_url)
        self.command_management_page = CommandManagementPage(self.driver, self.base_url)
        self.base_paging_function = BasePagingFunction(self.driver, self.base_url)
        self.alarm_info_page = AlarmInfoPage(self.driver, self.base_url)

        # 打开页面，填写用户名、密码、点击登录
        self.base_page.open_page()
        self.driver.set_window_max()
        self.driver.implicitly_wait(5)
        self.driver.clear_cookies()
        self.log_in_page.account_input('jimitest')
        self.log_in_page.password_input('jimi123')
        self.log_in_page.remember_me()
        self.log_in_page.login_button_click()
        self.driver.implicitly_wait(5)

        # 登录之后点击控制台，然后点击指令管理
        self.alarm_info_page.click_control_after_click_alarm_info()
        sleep(3)

    def tearDown(self):
        self.driver.quit_browser()

    def test_case_143_enclosure_set_up_add_enclosure(self):
        # 断言url
        expect_url = self.base_url + '/alarmInfo/toAlarmInfo'
        self.assertEqual(expect_url, self.alarm_info_page.actual_url_click_alarm())
        # 断言文本
        expect_text = '告警'
        self.assertEqual(expect_text, self.alarm_info_page.actual_text_alick_alarm())
        # 点击围栏设置
        self.alarm_info_page.click_lift_list('set_up_enclosure')
        # 断言文本
        expect_text = '围栏设置'
        self.assertEqual(expect_text, self.alarm_info_page.actual_text_after_click_set_up_enclosure())

        # 点击创建围栏
        self.alarm_info_page.click_add_enclosure()
        # 断言
        expect_text = '创建围栏'
        self.assertEqual(expect_text, self.alarm_info_page.actual_text_after_click_add_enclosure())
        # 点击关闭创建围栏
        self.alarm_info_page.click_close_add_enclosure()
