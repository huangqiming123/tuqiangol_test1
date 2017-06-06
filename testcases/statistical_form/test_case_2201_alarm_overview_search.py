import csv
import unittest
import time
from automate_driver.automate_driver import AutomateDriver
from model.connect_sql import ConnectSql
from pages.alarm_info.alarm_info_page import AlarmInfoPage
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.statistical_form.statistical_form_page import StatisticalFormPage
from pages.statistical_form.statistical_form_page_read_csv import StatisticalFormPageReadCsv


class TestCase138AlarmOverviewSearch(unittest.TestCase):
    '''
    用例第138条，告警总览页面搜索
    author：zhangAo
    '''

    def setUp(self):
        # 前置条件
        # 实例化对象
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.alarm_info_page = AlarmInfoPage(self.driver, self.base_url)
        self.statistical_form_page_read_csv = StatisticalFormPageReadCsv()
        self.log_in_base = LogInBase(self.driver, self.base_url)
        self.statistical_form_page = StatisticalFormPage(self.driver, self.base_url)
        self.connect_sql = ConnectSql()

        # 打开页面，填写用户名、密码、点击登录
        self.base_page.open_page()
        self.driver.set_window_max()
        self.driver.implicitly_wait(5)
        self.driver.clear_cookies()
        self.log_in_base.log_in_jimitest()

        # 登录之后点击控制台，然后点击指令管理
        self.statistical_form_page.click_control_after_click_statistical_form_page()
        time.sleep(3)

    def tearDown(self):
        self.driver.quit_browser()

    def test_case_138_alarm_overview_search(self):
        # 断言url
        expect_url = self.base_url + '/deviceReport/statisticalReport'
        self.assertEqual(expect_url, self.alarm_info_page.actual_url_click_alarm())

        # 点击告警总览
        self.alarm_info_page.click_alarm_overview_list()
        # 断言文本
        expect_text_after_click_alarm = '告警总览'
        self.driver.switch_to_frame('x,//*[@id="alarmOverviewFrame"]')
        self.assertEqual(expect_text_after_click_alarm, self.alarm_info_page.actual_text_click_alarm_info())
        self.driver.default_frame()
        # 输入数据搜索
        csv_file = self.statistical_form_page_read_csv.read_csv('alarm_overview_search_data.csv')
        csv_data = csv.reader(csv_file)
        is_header = True
        for row in csv_data:
            if is_header:
                is_header = False
                continue
            data = {
                'user_name': row[0],
                'choose_date': row[1],
                'began_time': row[2],
                'end_time': row[3]
            }
            self.alarm_info_page.add_data_to_search_in_alarm_overview(data)

            web_total = self.alarm_info_page.get_web_total_in_overview_search()
            if web_total == 0:
                self.assertIn('暂无数据', self.statistical_form_page.get_no_data_text_in_alarm_overview_page())
            else:
                self.driver.switch_to_frame('x,//*[@id="alarmOverviewFrame"]')
                sos_alarm_total = self.statistical_form_page.get_sos_total_alarm_number()
                list_sos_alarm_total = []
                for n in range(web_total):
                    number = self.statistical_form_page.get_list_sos_alarm_total_number(n)
                    list_sos_alarm_total.append(int(number))
                self.assertEqual(sos_alarm_total, str(sum(list_sos_alarm_total)))

                enter_satellite_dead_zone_alarm_total = self.statistical_form_page.get_enter_satellite_dead_zone_alarm_total()
                list_enter_satellite_dead_zone_alarm_total = []
                for n in range(web_total):
                    number = self.statistical_form_page.get_list_enter_satellite_dead_zone_alarm_total_number(n)
                    list_enter_satellite_dead_zone_alarm_total.append(int(number))
                self.assertEqual(enter_satellite_dead_zone_alarm_total,
                                 str(sum(list_enter_satellite_dead_zone_alarm_total)))

                self.driver.default_frame()

        csv_file.close()
