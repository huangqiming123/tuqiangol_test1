import csv
import unittest
from time import sleep

from automate_driver.automate_driver import AutomateDriver
from pages.alarm_info.alarm_info_page import AlarmInfoPage
from pages.base.base_page import BasePage
from pages.base.base_paging_function import BasePagingFunction
from pages.command_management.command_management_page import CommandManagementPage
from pages.login.login_page import LoginPage


class TestCase144EnclosureSetUpOperation(unittest.TestCase):
    '''
    用例第144条，围栏设置页面的列表操作
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

    def test_case_144_enclosure_set_up_operation(self):
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

        # 点击查看
        self.alarm_info_page.set_up_enclosure_list_operation('look')
        # 断言
        expect_text = self.alarm_info_page.first_list_name_in_set_up_enclosure()
        self.assertEqual(expect_text, self.alarm_info_page.actaul_text_after_click_look())
        # 点击关闭
        self.alarm_info_page.close_look_enclosure()

        # 点击编辑围栏
        self.alarm_info_page.set_up_enclosure_list_operation('edit')
        # 断言
        expect_text = '编辑'
        self.assertEqual(expect_text, self.alarm_info_page.actual_text_after_click_edit())
        # 点击关闭
        self.alarm_info_page.click_edit_enclosure_operation('close')

        # 点击编辑围栏
        self.alarm_info_page.set_up_enclosure_list_operation('edit')
        # 断言
        expect_text = '编辑'
        self.assertEqual(expect_text, self.alarm_info_page.actual_text_after_click_edit())
        # 点击关闭
        self.alarm_info_page.click_edit_enclosure_operation('cancel')

        # 点击编辑围栏
        self.alarm_info_page.set_up_enclosure_list_operation('edit')
        # 断言
        expect_text = '编辑'
        self.assertEqual(expect_text, self.alarm_info_page.actual_text_after_click_edit())
        # 修改围栏的数据
        self.alarm_info_page.add_data_to_edit_enclosure('我的围栏', '这是我的地盘')
        # 点击关闭
        self.alarm_info_page.click_edit_enclosure_operation('ensure')

        # 点击删除围栏
        self.alarm_info_page.set_up_enclosure_list_operation('delete')
        # 断言
        sleep(2)
        self.assertEqual("确定", self.alarm_info_page.actual_text_after_click_delete_list())
        # 点击关闭
        self.alarm_info_page.click_detele_enclosure_operation('close')

        # 点击删除围栏
        self.alarm_info_page.set_up_enclosure_list_operation('delete')
        # 断言
        self.assertEqual("确定", self.alarm_info_page.actual_text_after_click_delete_list())
        # 点击取消
        self.alarm_info_page.click_detele_enclosure_operation('cancel')

        # 点击删除围栏
        self.alarm_info_page.set_up_enclosure_list_operation('delete')
        # 断言
        self.assertEqual("确定", self.alarm_info_page.actual_text_after_click_delete_list())
        # 点击确定
        self.alarm_info_page.click_detele_enclosure_operation('ensure')

        # 点击告警设置
        self.alarm_info_page.set_up_enclosure_list_operation('set_up')
        # 断言
        self.assertEqual('围栏设置', self.alarm_info_page.actual_text_after_click_set_up_alarm())
        # 点击关闭
        self.alarm_info_page.click_set_up_alarm_operation('close')

        # 点击告警设置
        self.alarm_info_page.set_up_enclosure_list_operation('set_up')
        # 断言
        self.assertEqual('围栏设置', self.alarm_info_page.actual_text_after_click_set_up_alarm())
        # 点击关闭
        self.alarm_info_page.click_set_up_alarm_operation('cancel')

        csv_file = open('E:\git\\tuqiangol_test\data\\alarm_info\set_up_alarm_data.csv', 'r', encoding='utf8')
        csv_data = csv.reader(csv_file)
        is_header = True
        for row in csv_data:
            if is_header:
                is_header = False
                continue
            set_up_alarm_data = {
                'search': row[0],
                'time_01': row[1],
                'time_02': row[2]
            }
            # 点击告警设置
            self.alarm_info_page.set_up_enclosure_list_operation('set_up')
            # 断言
            self.assertEqual('围栏设置', self.alarm_info_page.actual_text_after_click_set_up_alarm())

            # 增加数据去设置告警
            self.alarm_info_page.add_data_to_set_up_alarm(set_up_alarm_data)
            # 点击关闭
            self.alarm_info_page.click_set_up_alarm_operation('ensure')
