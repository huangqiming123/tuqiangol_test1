import csv
import unittest
from time import sleep

from automate_driver.automate_driver import AutomateDriver
from pages.alarm_info.alarm_info_page import AlarmInfoPage
from pages.base.base_page import BasePage
from pages.base.base_paging_function import BasePagingFunction
from pages.command_management.command_management_page import CommandManagementPage
from pages.login.login_page import LoginPage


class TestCase141AlarmDetailHandle(unittest.TestCase):
    '''
    用例第141条，告警详情页面处理
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

    def test_case_141_alarm_detail_handle(self):
        # 断言url
        expect_url = self.base_url + '/alarmInfo/toAlarmInfo'
        self.assertEqual(expect_url, self.alarm_info_page.actual_url_click_alarm())
        # 断言文本
        expect_text = '告警'
        self.assertEqual(expect_text, self.alarm_info_page.actual_text_alick_alarm())
        # 点击告警详情
        self.alarm_info_page.click_lift_list('alarm_detail')
        # 断言
        self.assertEqual('告警详情', self.alarm_info_page.actual_text_after_click_alarm_detail())
        sleep(3)

        # 读数据
        csv_file = open('E:\git\\tuqiangol_test\data\\alarm_info\\alarm_detail_search_data.csv', 'r', encoding='utf8')
        csv_data = csv.reader(csv_file)

        is_header = True
        for row in csv_data:
            if is_header:
                is_header = False
                continue
            data = {
                'user_name': row[0],
                'type': row[1],
                'status': row[2],
                'alarm_begin_time': row[3],
                'alarm_end_time': row[4],
                'push_begin_time': row[5],
                'push_end_time': row[6],
                'next_user': row[7]
            }
            self.alarm_info_page.add_data_to_search_alarm_detail(data)

            # 选中查询的第一个去处理
            self.alarm_info_page.choose_select_result_first()
            # 点击标记已读
            try:
                self.alarm_info_page.click_handle_meun('read')
                sleep(1)
                # 断言
                self.assertEqual('操作成功',self.base_page.reset_passwd_stat_cont())
            except:
                print('请选择告警信息')

            # 处理
            try:
                self.alarm_info_page.click_handle_meun('handle')
                # 断言
                self.assertEqual('告警处理', self.alarm_info_page.actual_text_after_click_handle())
                # 输入处理信息
                self.alarm_info_page.add_data_to_handle('处理人1', '这是我处理的，谢谢')
                sleep(5)
            except:
                print('选择的设备已经处理')

            # 点击全部标记为已读
            sleep(3)
            self.alarm_info_page.click_handle_meun('all_read')
            # 断言
            try:
                sleep(1)
                self.assertEqual('操作成功',self.base_page.reset_passwd_stat_cont())
            except:
                pass
            # 点击全部处理
            self.alarm_info_page.click_handle_meun('all_handle')
        csv_file.close()