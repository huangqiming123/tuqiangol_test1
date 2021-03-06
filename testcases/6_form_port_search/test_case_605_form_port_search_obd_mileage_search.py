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
from pages.statistical_form.obd_form_page import ObdFormPage
from pages.statistical_form.search_sql import SearchSql
from pages.statistical_form.statistical_form_page import StatisticalFormPage
from pages.statistical_form.statistical_form_page_read_csv import StatisticalFormPageReadCsv

__author__ = ''

class TestCase605FormPortSearchObdMileageSearch(unittest.TestCase):
    # 测试 报表 接口搜索 obd里程报表
    def setUp(self):
        # 前置条件
        # 实例化对象
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.statistical_form_page = StatisticalFormPage(self.driver, self.base_url)
        self.statistical_form_page_read_csv = StatisticalFormPageReadCsv()
        self.log_in_base = LogInBase(self.driver, self.base_url)
        self.connect_sql = ConnectSql()
        self.search_sql = SearchSql(self.driver, self.base_url)
        self.obd_form_page = ObdFormPage(self.driver, self.base_url)
        # 打开页面，填写用户名、密码、点击登录
        self.base_page.open_page()
        self.driver.set_window_max()
        self.driver.implicitly_wait(5)
        self.driver.clear_cookies()
        self.log_in_base.log_in_jimitest()
        self.assert_text = AssertText()

        current_handle = self.driver.get_current_window_handle()
        self.statistical_form_page.click_control_after_click_statistical_form_page()
        sleep(3)
        self.base_page.change_windows_handle(current_handle)

    def tearDown(self):
        self.driver.close_window()
        # 退出浏览器
        self.driver.quit_browser()

    def test_case_obd_mileage_search_port(self):
        # 断言url
        expect_url_after_click_statistical_form = self.base_url + '/deviceReport/statisticalReport'
        self.assertEqual(expect_url_after_click_statistical_form,
                         self.statistical_form_page.actual_url_after_statistical_form())

        # 点击obd统计的里程报表
        self.obd_form_page.click_obd_form_mileage_statistical_button()
        # 切换到odb里程统计的frame里面
        self.obd_form_page.switch_to_obd_mileage_statistical_frame()

        csv_file = self.statistical_form_page_read_csv.read_csv('obd_milage_report_search_data.csv')
        csv_data = csv.reader(csv_file)
        is_header = True
        for row in csv_data:
            if is_header:
                is_header = False
                continue
            search_data = {
                'user_name': row[0],
                'choose_date': row[2],
                'begin_time': row[3],
                'end_time': row[4]
            }
            self.obd_form_page.add_data_to_search_obd_mileage_statistical_form(search_data)

            # 获取页面上设备的信息
            dev_total_mile = self.obd_form_page.get_dev_total_mile_obd_mileage_statistical_form()
            dev_avg_oil = self.obd_form_page.get_dev_avg_oil_obd_mileage_statistical_form()
            dev_avg_speed = self.obd_form_page.get_avg_oil_obd_mileage_statistical_form()
            dev_total_oil = self.obd_form_page.get_dev_total_oil_obd_mileage_statistical_form()
            begin_time = self.obd_form_page.get_begin_times()
            end_time = self.obd_form_page.get_end_times()

            # 请求里程报表统计
            request_url = request_base_url()
            header = {
                '_method_': 'getObdTotalInfo',
                'imeis': self.obd_form_page.search_imei(),
                'startTime': begin_time,
                'endTime': end_time
            }
            print(header)
            req_json = requests.post(request_url, data=header).json()
            print(req_json)
            # 断言
            try:
                self.assertEqual(float(dev_total_mile), req_json['data'][0]['totalMileage'])
                self.assertEqual(float(dev_avg_oil), req_json['data'][0]['totalAvgFuelConsumption'])
                self.assertEqual(float(dev_avg_speed), req_json['data'][0]['totalAvgSpeed'])
                self.assertEqual(float(dev_total_oil), req_json['data'][0]['totalFuelConsumption'])
            except:
                self.assertEqual([None], req_json['data'])

            request_url = request_base_url()
            header = {
                '_method_': 'getObdTrip',
                'imeis': self.obd_form_page.search_imei(),
                'startTime': begin_time,
                'endTime': end_time,
                'type': 'day'
            }
            sleep(10)
            res_json = requests.post(request_url, data=header).json()

            total_page = self.obd_form_page.get_obd_list_total_page_number()
            if total_page == 0:
                self.assertEqual('0', dev_total_mile)
                self.assertEqual('0', dev_avg_oil)
                self.assertEqual('0', dev_avg_speed)
                self.assertEqual('0', dev_total_oil)

            elif total_page == 1:
                # 获取页面上的里程和耗油
                mile_and_oil_list = []
                per_page_total_number = self.obd_form_page.get_per_page_total_number()
                for n in range(per_page_total_number):
                    mile_and_oil_list.append({
                        'atDay': self.obd_form_page.get_at_day_in_odb_mileage_form(n),
                        'mileage': float(self.obd_form_page.get_per_mile_in_obd_mileage_form(n)),
                        'totalFuelConsumption': float(self.obd_form_page.get_per_oil_in_obd_mileage_form(n)),
                        'avgFuelConsumption': float(self.obd_form_page.get_avg_fuel_consumption_in_obd_mileage_form(n))
                    })

                res_data = res_json['data']
                for data in res_data:
                    del data['endLat'], data['endLng'], data['imei'], data['maxSpeed'], data[
                        'rapidAcceleration'], data['rapidDeceleration'], data['startLat'], data['startLng'], data[
                        'tripTime'], data['avgSpeed']
                self.assertEqual(mile_and_oil_list, res_data)
            else:
                mile_and_oil_list = []
                for i in range(total_page):
                    # 循环点击每一页
                    self.obd_form_page.click_per_page(i)
                    # 获取页面上的里程和耗油
                    per_page_total_number = self.obd_form_page.get_per_page_total_number()
                    for n in range(per_page_total_number):
                        mile_and_oil_list.append({
                            'atDay': self.obd_form_page.get_at_day_in_odb_mileage_form(n),
                            'mileage': float(self.obd_form_page.get_per_mile_in_obd_mileage_form(n)),
                            'totalFuelConsumption': float(self.obd_form_page.get_per_oil_in_obd_mileage_form(n)),
                            'avgFuelConsumption': float(
                                self.obd_form_page.get_avg_fuel_consumption_in_obd_mileage_form(n))
                        })

                res_data = res_json['data']
                for data in res_data:
                    del data['endLat'], data['endLng'], data['imei'], data['maxSpeed'], data[
                        'rapidAcceleration'], data['rapidDeceleration'], data['startLat'], data['startLng'], data[
                        'tripTime'], data['avgSpeed']
                self.assertEqual(mile_and_oil_list, res_data)
        csv_file.close()
        self.driver.default_frame()
