import csv
import unittest
import time

import requests

from automate_driver.automate_driver import AutomateDriver
from model.connect_sql import ConnectSql
from pages.alarm_info.alarm_info_page import AlarmInfoPage
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.statistical_form.search_sql import SearchSql
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
        self.search_sql = SearchSql(self.driver, self.base_url)

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

    def test_case_3103_alarm_overview_check_web_and_request(self):
        # 断言url
        expect_url = self.base_url + '/deviceReport/statisticalReport'
        self.assertEqual(expect_url, self.alarm_info_page.actual_url_click_alarm())

        # 点击告警总览
        self.alarm_info_page.click_alarm_overview_list()
        # 断言文本
        expect_text_after_click_alarm = '告警总览'
        self.assertEqual(expect_text_after_click_alarm, self.alarm_info_page.actual_text_click_alarm_info())
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
            self.alarm_info_page.switch_to_alarm_overview_frame()
            user_id = self.search_sql.search_current_account(data['user_name'])
            all_dev = self.search_sql.search_current_account_equipment(data['user_name'])
            start_time = self.statistical_form_page.get_start_time_in_alarm_overview()
            end_time = self.statistical_form_page.get_end_time_in_alarm_overview()
            playload = {
                'status': '1,10,11,12,128,13,14,15,16,17,18,19,192,194,195,2,22,23,3,4,5,6,9,90,ACC_OFF,ACC_ON,in,offline,out,sensitiveAreasFence,stayAlert,stayTimeIn,stayTimeOut',
                'imei': all_dev,
                'userId': user_id,
                'startTime': start_time,
                'endTime': end_time
            }
            headers = self.statistical_form_page.get_headers_for_post_request()

            r = requests.post('http://tuqiangol.com/alarmInfo/getAlarmReport', params=playload, headers=headers)
            response = r.text
            response_data = response
            print(response_data)
            if len(response_data) == 0:
                pass
            elif len(response_data) == 1:
                dev_data = eval(response_data.split('[')[1].split(']')[0])
                dev_name = dev_data['devName']
                dev_type = dev_data['mcType']
                dev_imei = dev_data['imei']
                dev_name_web = self.statistical_form_page.get_dev_name_in_alarm_overview()
                self.assertEqual(dev_name, dev_name_web)
                dev_type_web = self.statistical_form_page.get_dev_type_in_alarm_overview()
                self.assertEqual(dev_type, dev_type_web)
                dev_imei_web = self.statistical_form_page.get_dev_imei_in_alarm_overview()
                self.assertEqual(dev_imei, dev_imei_web)
            else:
                pass
            self.driver.default_frame()
        csv_file.close()
