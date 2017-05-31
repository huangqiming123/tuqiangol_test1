import unittest
from time import sleep

from automate_driver.automate_driver import AutomateDriver
from pages.alarm_info.alarm_info_page import AlarmInfoPage
from pages.base.base_page import BasePage
from pages.base.base_paging_function import BasePagingFunction
from pages.command_management.command_management_page import CommandManagementPage
from pages.login.login_page import LoginPage


class TestCase142AlarmSetUp(unittest.TestCase):
    '''
    用例第142条，告警推送设置
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

    def test_case_142_alarm_set_up(self):
        # 断言url
        expect_url = self.base_url + '/alarmInfo/toAlarmInfo'
        self.assertEqual(expect_url, self.alarm_info_page.actual_url_click_alarm())
        # 断言文本
        expect_text = '告警'
        self.assertEqual(expect_text, self.alarm_info_page.actual_text_alick_alarm())

        # 点击告警总览
        self.alarm_info_page.click_lift_list('alarm_set_up')
        # 断言文本
        expect_text_after_click_alarm = '告警推送设置'
        self.assertEqual(expect_text_after_click_alarm, self.alarm_info_page.actual_text_click_alarm_set_up())

        # 点击APP推送全部
        self.alarm_info_page.click_menu("open_app")
        # 获取有多个
        total = self.alarm_info_page.get_total_number()
        for number in range(total + 1):
            if number == 0:
                pass
            else:
                self.assertEqual(True, self.driver.get_element(
                    'x,//*[@id="alarm_appSet_tbody"]/tr[%s]/td[4]/label[2]/div/input' % number).is_selected())

        # 点击关闭APP推送
        self.alarm_info_page.click_menu('close_app')
        for number in range(total + 1):
            if number == 0:
                pass
            else:
                self.assertEqual(False, self.driver.get_element(
                    'x,//*[@id="alarm_appSet_tbody"]/tr[%s]/td[4]/label[2]/div/input' % number).is_selected())

        # 点击查看全部告警
        self.alarm_info_page.click_menu('look_all')
        for number in range(total + 1):
            if number == 0:
                pass
            else:
                self.assertEqual(True, self.driver.get_element(
                    'x,//*[@id="alarm_appSet_tbody"]/tr[%s]/td[4]/label[1]/div/input' % number).is_selected())

        self.alarm_info_page.click_menu('close_all')
        for number in range(total + 1):
            if number == 0:
                pass
            else:
                self.assertEqual(False, self.driver.get_element(
                    'x,//*[@id="alarm_appSet_tbody"]/tr[%s]/td[4]/label[1]/div/input' % number).is_selected())

        # 全部设置邮件发送
        self.alarm_info_page.click_menu('email')
        # 断言
        expect_text = '设置邮件发送'
        self.assertEqual(expect_text, self.alarm_info_page.actual_text_ater_set_up_email())
        # 点击关闭
        self.alarm_info_page.set_up_email_operation('close')

        # 全部设置邮件发送
        self.alarm_info_page.click_menu('email')
        # 断言
        expect_text = '设置邮件发送'
        self.assertEqual(expect_text, self.alarm_info_page.actual_text_ater_set_up_email())
        # 点击取消
        self.alarm_info_page.set_up_email_operation('cancel')

        # 全部设置邮件发送
        self.alarm_info_page.click_menu('email')
        # 断言
        expect_text = '设置邮件发送'
        self.assertEqual(expect_text, self.alarm_info_page.actual_text_ater_set_up_email())
        self.alarm_info_page.add_email_to_set_up('123@abc.com')
        # 点击关闭
        self.alarm_info_page.set_up_email_operation('ensure')
        sleep(5)

        # 点击告警时间设置
        self.alarm_info_page.click_menu('time')
        # 断言
        expect_text = '告警时间设置'
        self.assertEqual(expect_text, self.alarm_info_page.actual_text_after_click_alarm_time())
        # 点击关闭
        self.alarm_info_page.set_up_alarm_time_operation('close')

        # 点击告警时间设置
        self.alarm_info_page.click_menu('time')
        # 断言
        expect_text = '告警时间设置'
        self.assertEqual(expect_text, self.alarm_info_page.actual_text_after_click_alarm_time())
        # 点击取消
        self.alarm_info_page.set_up_alarm_time_operation('cancel')

        # 点击告警时间设置
        self.alarm_info_page.click_menu('time')
        # 断言
        expect_text = '告警时间设置'
        self.assertEqual(expect_text, self.alarm_info_page.actual_text_after_click_alarm_time())
        self.alarm_info_page.add_data_to_set_up_alarm_time('100', '100')
        # 点击保存
        self.alarm_info_page.set_up_alarm_time_operation('ensure')

        # 点击列表中的元素
        self.alarm_info_page.circle_click_look_alarm()

        self.alarm_info_page.circle_click_app()

        self.alarm_info_page.circle_click_set_up_email()