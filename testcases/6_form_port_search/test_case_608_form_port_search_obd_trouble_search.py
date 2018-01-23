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

class TestCase608FormPortSearchObdTroubleSearch(unittest.TestCase):
    # 测试 报表 接口搜索 obd车况报表
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

    def test_case_obd_trouble_port_search(self):
        # 断言url
        expect_url_after_click_statistical_form = self.base_url + '/deviceReport/statisticalReport'
        self.assertEqual(expect_url_after_click_statistical_form,
                         self.statistical_form_page.actual_url_after_statistical_form())

        # 点击obd统计的里程报表
        self.obd_form_page.click_obd_trouble_form_button()
        # 切换到odb里程统计的frame里面
        self.obd_form_page.switch_to_obd_trouble_form_frame()

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
            self.obd_form_page.add_data_to_search_obd_trouble_form(search_data)

            # 获取页面上设备的信息
            dev_total_mile = self.obd_form_page.get_dev_total_mile_obd_vehicle_condition_form()
            dev_avg_oil = self.obd_form_page.get_dev_avg_oil_obd_vehicle_condition_form()
            dev_avg_speed = self.obd_form_page.get_avg_oil_obd_vehicle_condition_form()
            dev_total_oil = self.obd_form_page.get_dev_total_oil_obd_vehicle_condition_form()
            begin_time = self.obd_form_page.get_begin_time()
            end_time = self.obd_form_page.get_end_time()

            request_url = request_base_url()
            header = {
                '_method_': 'getObdVehicleCondition',
                'imeis': self.obd_form_page.search_imei(),
                'startTime': begin_time,
                'endTime': end_time,
                'type': 'carfault'
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
                        'gpsTime': self.obd_form_page.get_gps_time_in_vehicle_condition_form(n),
                        'lng': float(self.obd_form_page.get_lot_in_trouble_form(n)),
                        'lat': float(self.obd_form_page.get_lat_in_trouble_form(n)),
                        'errorCode': self.obd_form_page.get_error_code_in_trouble_form(n)
                    })

                res_data = res_json['data']
                for data in res_data:
                    del data['acc'], data['addr'], data['batteryVoltage'], data['direction'], data[
                        'engineLoad'], data['fuelConsumption1'], data['fuelConsumption2'], data['gpsInfo'], data[
                        'gpsSpeed'], data['heatingTime'], \
                        data['idleTime'], data['imei'], data[
                        'maxSpeed'], data['oilPer'], data['rapidAcceleration'], data['rapidDeceleration'], data[
                        'rotatingSpeed'], data[
                        'speed'], data['throttlePosition'], data['totalMileage'], data['waterTemperature']
                print(mile_and_oil_list)
                print(res_data)
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
                            'gpsTime': self.obd_form_page.get_gps_time_in_vehicle_condition_form(n),
                            'lng': float(self.obd_form_page.get_lot_in_trouble_form(n)),
                            'lat': float(self.obd_form_page.get_lat_in_trouble_form(n)),
                            'errorCode': self.obd_form_page.get_error_code_in_trouble_form(n)
                        })

                res_data = res_json['data']
                for data in res_data:
                    del data['acc'], data['addr'], data['batteryVoltage'], data['direction'], data[
                        'engineLoad'], data['fuelConsumption1'], data['fuelConsumption2'], data['gpsInfo'], data[
                        'gpsSpeed'], data['heatingTime'], \
                        data['idleTime'], data['imei'], data[
                        'maxSpeed'], data['oilPer'], data['rapidAcceleration'], data['rapidDeceleration'], data[
                        'rotatingSpeed'], data[
                        'speed'], data['throttlePosition'], data['totalMileage'], data['waterTemperature']
                print(mile_and_oil_list)
                print(res_data)
                self.assertEqual(mile_and_oil_list, res_data)
        csv_file.close()
        self.driver.default_frame()
