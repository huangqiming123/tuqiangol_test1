import csv
import unittest
from time import sleep

import requests

from automate_driver.automate_driver import AutomateDriver
from model.assert_text import AssertText
from model.connect_sql import ConnectSql
from model.send_mail import request_base_url
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.statistical_form.search_sql import SearchSql
from pages.statistical_form.statistic_form_page3 import StatisticFormPage3
from pages.statistical_form.statistical_form_page import StatisticalFormPage
from pages.statistical_form.statistical_form_page_read_csv import StatisticalFormPageReadCsv


class TestCase174SportStatisticalOverview(unittest.TestCase):
    def setUp(self):
        # 前置条件
        # 实例化对象
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.statistical_form_page = StatisticalFormPage(self.driver, self.base_url)
        self.statistical_form_page_read_csv = StatisticalFormPageReadCsv()
        self.statistical_form_page3 = StatisticFormPage3(self.driver, self.base_url)
        self.log_in_base = LogInBase(self.driver, self.base_url)
        self.connect_sql = ConnectSql()
        self.search_sql = SearchSql(self.driver, self.base_url)
        self.assert_text = AssertText()
        # 打开页面，填写用户名、密码、点击登录
        self.base_page.open_page()
        self.driver.set_window_max()
        self.driver.implicitly_wait(5)
        self.driver.clear_cookies()
        self.log_in_base.log_in_jimitest()

        # 登录之后点击控制台，然后点击设置
        self.statistical_form_page.click_control_after_click_statistical_form_page()
        sleep(3)

    def tearDown(self):
        # 退出浏览器
        self.driver.quit_browser()

    def test_case_sport_statistical_sport_overview(self):
        # 断言url
        expect_url_after_click_statistical_form = self.base_url + '/deviceReport/statisticalReport'
        self.assertEqual(expect_url_after_click_statistical_form,
                         self.statistical_form_page.actual_url_after_statistical_form())
        # 断言
        self.assertEqual(self.assert_text.statistical_form_sport_overview_form(),
                         self.statistical_form_page.actual_text_after_click_sport_overview())
        # 读数据
        csv_file = self.statistical_form_page_read_csv.read_csv('sport_statistical_sport_overview_search_data.csv')
        csv_data = csv.reader(csv_file)
        is_header = True
        for row in csv_data:
            if is_header:
                is_header = False
                continue
            search_data = {
                'search_user': row[0],
                'choose_date': row[1],
                'begin_time': row[2],
                'end_time': row[3]
            }
            self.statistical_form_page.add_data_to_search_sport_overview(search_data)

            # 处理搜索出来的数据
            web_total_number = self.statistical_form_page3.get_web_search_total_number_sport_overview()
            data_web = []
            for n in range(web_total_number):
                data_web.append({
                    'imei': self.statistical_form_page3.get_imei_in_sport_overview(n),
                    'mileage': self.statistical_form_page3.get_mileage_in_sport_overview(n),
                    'overSpeedTimes': self.statistical_form_page3.get_over_speed_times_in_sport_overview(n),
                    'stopTimes': self.statistical_form_page3.get_stop_times_in_sport_overview(n)
                })
            print(data_web)
            # 连接数据库
            all_dev = self.search_sql.search_current_account_equipment(search_data['search_user'])
            imeis = self.statistical_form_page3.change_dev_imei_format(all_dev)
            begin_time = self.statistical_form_page3.get_sport_overview_form_begin_time()
            end_time = self.statistical_form_page3.get_sport_overview_form_end_time()
            get_current_userid = self.search_sql.search_current_account_user_id(search_data['search_user'])
            # 连接接口
            request_url = request_base_url()
            request_params = {
                '_method_': 'getRunSummary',
                'imeis': imeis,
                'startTime': begin_time,
                'endTime': end_time,
                'userIds': get_current_userid
            }
            res = requests.post(request_url, data=request_params)
            sleep(30)
            response = res.json()
            res_data = response['data']
            for data in res_data:
                if data['stopTimes'] != 0 or data['mileage'] != 0 or data['overSpeedTimes'] != 0:
                    del (data['atDay'])
            print(res_data)
            self.assertEqual(data_web, res_data)
            self.driver.default_frame()
        csv_file.close()
