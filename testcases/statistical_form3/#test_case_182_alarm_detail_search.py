import csv
import unittest
from time import sleep, time

import requests

from automate_driver.automate_driver import AutomateDriver
from model.assert_text import AssertText
from model.connect_sql import ConnectSql
from model.send_mail import request_base_url
from pages.alarm_info.alarm_info_page import AlarmInfoPage
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.statistical_form.search_sql import SearchSql
from pages.statistical_form.statistic_form_page3 import StatisticFormPage3
from pages.statistical_form.statistical_form_page import StatisticalFormPage
from pages.statistical_form.statistical_form_page_read_csv import StatisticalFormPageReadCsv


class TestCase182AlarmDetailSearch(unittest.TestCase):
    # 告警详情页面搜索
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
        self.statistical_form_page3 = StatisticFormPage3(self.driver, self.base_url)
        self.seasrch_sql = SearchSql(self.driver, self.base_url)

        # 打开页面，填写用户名、密码、点击登录
        self.base_page.open_page()
        self.driver.set_window_max()
        self.driver.implicitly_wait(5)
        self.driver.clear_cookies()
        self.assert_text = AssertText()
        self.log_in_base.log_in_jimitest()
        # 登录之后点击控制台，然后点击指令管理
        self.statistical_form_page.click_control_after_click_statistical_form_page()
        sleep(3)

    def tearDown(self):
        self.driver.quit_browser()

    def test_case_alarm_detail_search(self):
        # 断言url
        expect_url = self.base_url + '/deviceReport/statisticalReport'
        self.assertEqual(expect_url, self.alarm_info_page.actual_url_click_alarm())
        # 点击告警详情
        self.alarm_info_page.click_alarm_detail_list()
        # 选择全部的告警类型查询
        self.statistical_form_page3.select_all_alarm_type_in_alarm_detail_search()
        # 读数据
        csv_file = self.statistical_form_page_read_csv.read_csv('alarm_detail_search_data.csv')
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
                'is_input_dev': row[7]
            }
            self.statistical_form_page3.add_data_to_search_alarm_detail(data)

            get_alarm_begin_time = self.statistical_form_page3.get_alarm_begin_time_in_alarm_detail_page()
            get_alarm_end_time = self.statistical_form_page3.get_alarm_end_time_in_alarm_detail_page()
            get_push_begin_time = self.statistical_form_page3.get_push_begin_time_in_alarm_detail_page()
            get_push_end_time = self.statistical_form_page3.get_push_end_time_in_alarm_detail_page()
            all_dev = self.seasrch_sql.search_current_account_equipment(data['user_name'])
            imeis = self.statistical_form_page3.change_dev_imei_format(all_dev)
            get_current_userid = self.seasrch_sql.search_current_account_user_id(data['user_name'])
            request_url = request_base_url()

            if data['is_input_dev'] == '0':
                request_params = {
                    '_method_': 'getAlarmDetailNoPaging',
                    'startTime': get_alarm_begin_time,
                    'endTime': get_alarm_end_time,
                    'userIds': get_current_userid,
                }
                res = requests.post(request_url, data=request_params)
                sleep(20)
                response = res.json()
                res_data = response['data']
                for data_1 in res_data:
                    del data_1['alarmType'], data_1['id'], data_1['lat'], data_1['lng'], data_1['speed'], data_1[
                        'status'], data_1['userId']
                print(res_data)

                web_total_number = self.statistical_form_page3.get_web_total_number_in_alarm_detail_page()
                web_data = []
                for n in range(web_total_number):
                    web_data.append({
                        'imei': self.statistical_form_page3.get_imei_in_alarm_detail(n),
                        'createTime': self.statistical_form_page3.get_creat_time_in_alarm_detail(n),
                        'pushTime': self.statistical_form_page3.get_push_time_in_alarm_detail(n),
                        'addr': self.statistical_form_page3.get_addr_in_alarm_detail(n),
                        'readStatus': self.statistical_form_page3.get_read_status_in_alarm_detail(n)
                    })
                print(web_data)
                self.assertEqual(web_data, res_data)

            elif data['is_input_dev'] == '1':
                request_params = {
                    '_method_': 'getAlarmDetailNoPaging',
                    'startCreateTime': get_push_begin_time,
                    'endCreateTime': get_push_end_time,
                    'userIds': get_current_userid,
                    'imeis': imeis
                }
                res = requests.post(request_url, data=request_params)
                sleep(20)
                response = res.json()
                res_data = response['data']
                for data_1 in res_data:
                    del data_1['alarmType'], data_1['id'], data_1['lat'], data_1['lng'], data_1['speed'], data_1[
                        'status'], data_1['userId']
                print(res_data)

                web_total_number = self.statistical_form_page3.get_web_total_number_in_alarm_detail_page()
                web_data = []
                for n in range(web_total_number):
                    web_data.append({
                        'imei': self.statistical_form_page3.get_imei_in_alarm_detail(n),
                        'createTime': self.statistical_form_page3.get_creat_time_in_alarm_detail(n),
                        'pushTime': self.statistical_form_page3.get_push_time_in_alarm_detail(n),
                        'addr': self.statistical_form_page3.get_addr_in_alarm_detail(n),
                        'readStatus': self.statistical_form_page3.get_read_status_in_alarm_detail(n)
                    })
                print(web_data)
                self.assertEqual(web_data, res_data)
            self.driver.default_frame()
        csv_file.close()
