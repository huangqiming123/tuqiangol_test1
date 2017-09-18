import csv
import unittest
from time import sleep

import requests

from automate_driver.automate_driver import AutomateDriver
from model.assert_text import AssertText
from model.connect_sql import ConnectSql
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.statistical_form.search_sql import SearchSql
from pages.statistical_form.statistic_form_page3 import StatisticFormPage3
from pages.statistical_form.statistic_form_page4 import StatisticFormPage4
from pages.statistical_form.statistical_form_page import StatisticalFormPage
from pages.statistical_form.statistical_form_page_read_csv import StatisticalFormPageReadCsv
from model.send_mail import request_base_url


class TestCase178SportStatisticalStayForm(unittest.TestCase):
    # 运动报表，停留报表


    def setUp(self):
        # 前置条件
        # 实例化对象
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.statistical_form_page = StatisticalFormPage(self.driver, self.base_url)
        self.statistical_form_page_read_csv = StatisticalFormPageReadCsv()
        self.seasrch_sql = SearchSql(self.driver, self.base_url)
        self.log_in_base = LogInBase(self.driver, self.base_url)
        self.connect_sql = ConnectSql()
        self.search_sql = SearchSql(self.driver, self.base_url)
        self.statistical_form_page3 = StatisticFormPage3(self.driver, self.base_url)
        self.statistical_form_page4 = StatisticFormPage4(self.driver, self.base_url)
        # 打开页面，填写用户名、密码、点击登录
        self.base_page.open_page()
        self.assert_text = AssertText()
        self.driver.set_window_max()
        self.driver.implicitly_wait(5)
        self.log_in_base.log_in_jimitest()

        # 登录之后点击统计报表
        self.statistical_form_page.click_control_after_click_statistical_form_page()
        sleep(3)

    def tearDown(self):
        # 退出浏览器
        self.driver.quit_browser()

    def test_case_sport_statistical_stay_form(self):
        # 断言url
        expect_url_after_click_statistical_form = self.base_url + '/deviceReport/statisticalReport'
        self.assertEqual(expect_url_after_click_statistical_form,
                         self.statistical_form_page.actual_url_after_statistical_form())

        # 点击停留报表
        self.statistical_form_page.click_stay_form_button()
        # 断言
        self.assertEqual(self.assert_text.statistical_form_stay_form(),
                         self.statistical_form_page.actual_text_after_click_stay_form_button())

        # 读取查询数据
        csv_file = self.statistical_form_page_read_csv.read_csv('sport_statistical_stay_search_data2.csv')
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
            # 搜索数据
            self.statistical_form_page.add_data_to_search_stay_form(search_data)
            self.statistical_form_page.switch_to_stay_report_form_frame()
            total_page = self.statistical_form_page4.get_total_page_in_over_stay_form()
            begin_time = self.statistical_form_page4.get_over_stay_report_form_begin_time()
            end_time = self.statistical_form_page4.get_over_stay_report_form_end_time()
            all_dev = self.seasrch_sql.search_current_account_equipment(search_data['search_user'])
            imeis = self.statistical_form_page3.change_dev_imei_format(all_dev)
            total_saty_time = self.statistical_form_page4.get_total_stay_time_in_over_stay_form()

            print(begin_time)
            print(end_time)
            print("总计", total_saty_time)
            print(type(total_saty_time))

            if total_page == 0:
                # 连接接口
                request_url = request_base_url()
                request_params = {
                    '_method_': 'getStopSegment',
                    'imeis': imeis,
                    'startTime': begin_time,
                    'endTime': end_time,
                    'acc': "off"

                }
                res = requests.post(request_url, data=request_params)
                sleep(30)
                response = res.json()
                self.assertEqual(400, response['code'])
                self.assertEqual('没有找到数据', response['msg'])

            elif total_page == 1:
                total_number_per_page = self.statistical_form_page4.get_total_number_per_page_in_over_stay_form()
                web_data = []
                for n in range(total_number_per_page):
                    web_data.append({
                        # 'addr': self.statistical_form_page4.get_addr_in_over_stay_form(n),
                        'endTime': self.statistical_form_page4.get_end_time_in_over_stay_form(n),
                        'imei': self.statistical_form_page4.get_imei_in_over_stay_form(n),
                        'lat': self.statistical_form_page4.get_lat_in_over_stay_form(n),
                        'lng': self.statistical_form_page4.get_lng_in_over_stay_form(n),
                        'startTime': self.statistical_form_page4.get_start_time_in_over_stay_form(n),
                    })
                print("页面数据", web_data)
                # 连接接口
                request_url = request_base_url()
                request_params = {
                    '_method_': 'getStopSegment',
                    'imeis': imeis,
                    'startTime': begin_time,
                    'endTime': end_time,
                    'acc': "off"
                }
                res = requests.post(request_url, data=request_params)
                sleep(30)
                response = res.json()
                res_data = response['data']
                for data in res_data:
                    del data['acc'], data['durSecond']
                print("接口数据", res_data)
                self.assertEqual(web_data, res_data)
            else:
                web_data = []
                for i in range(total_page):
                    # 循环点击每一页
                    self.statistical_form_page3.click_per_page_in_mile_report_form(i)
                    total_number_per_page = self.statistical_form_page4.get_total_number_per_page_in_over_stay_form()
                    for n in range(total_number_per_page):
                        web_data.append({
                            # 'addr': self.statistical_form_page4.get_addr_in_over_stay_form(n),
                            'endTime': self.statistical_form_page4.get_end_time_in_over_stay_form(n),
                            'imei': self.statistical_form_page4.get_imei_in_over_stay_form(n),
                            'lat': self.statistical_form_page4.get_lat_in_over_stay_form(n),
                            'lng': self.statistical_form_page4.get_lng_in_over_stay_form(n),
                            'startTime': self.statistical_form_page4.get_start_time_in_over_stay_form(n),

                        })
                print("页面数据", web_data)
                print(len(web_data))
                # 连接接口
                request_url = request_base_url()
                request_params = {
                    '_method_': 'getStopSegment',
                    'imeis': imeis,
                    'startTime': begin_time,
                    'endTime': end_time,
                    'acc': "off"

                }
                res = requests.post(request_url, data=request_params)
                sleep(30)
                response = res.json()
                res_data = response['data']
                for data in res_data:
                    del data['acc'], data['durSecond']
                print("接口数据", res_data)
                print(len(res_data))
                self.assertEqual(web_data, res_data)

            # 总计停留时间
            # 连接接口
            request_url = request_base_url()
            request_params = {
                '_method_': 'getStopSegmentSum',
                'imeis': imeis,
                'startTime': begin_time,
                'endTime': end_time,
                'acc': "off"

            }
            res = requests.post(request_url, data=request_params)
            sleep(20)
            response = res.json()
            res_data = response['data']

            if total_saty_time == "0":
                self.assertEqual(int(total_saty_time), res_data)
            else:
                time = total_saty_time.split("小时")
                print(time[0])
                time2 = time[1].split("分")
                print(time2[0])
                sec = time2[1].split("秒")[0]
                print(sec)

                web_total_time = (int(time[0]) * 60 * 60) + (int(time2[0]) * 60) + int(sec)
                print(web_total_time)
                self.assertEqual(web_total_time, res_data)

            self.driver.default_frame()
        csv_file.close()
