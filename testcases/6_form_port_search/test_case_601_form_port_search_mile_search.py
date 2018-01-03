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


class TestCase601FormPortSearchMileSearch(unittest.TestCase):
    # 测试 报表 接口搜索 里程
    def setUp(self):
        # 前置条件
        # 实例化对象
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.statistical_form_page = StatisticalFormPage(self.driver, self.base_url)
        self.statistical_form_page_read_csv = StatisticalFormPageReadCsv()
        self.log_in_base = LogInBase(self.driver, self.base_url)
        self.statistical_form_page3 = StatisticFormPage3(self.driver, self.base_url)
        self.connect_sql = ConnectSql()
        self.seasrch_sql = SearchSql(self.driver, self.base_url)
        self.assert_text = AssertText()
        # 打开页面，填写用户名、密码、点击登录
        self.base_page.open_page()
        self.driver.set_window_max()
        self.driver.implicitly_wait(5)
        self.log_in_base.log_in_jimitest()

        current_handle = self.driver.get_current_window_handle()
        self.statistical_form_page.click_control_after_click_statistical_form_page()
        sleep(3)
        self.base_page.change_windows_handle(current_handle)

    def tearDown(self):
        # 退出浏览器
        self.driver.quit_browser()

    def test_case_mile_search_port(self):
        # 断言url
        expect_url_after_click_statistical_form = self.base_url + '/deviceReport/statisticalReport'
        self.assertEqual(expect_url_after_click_statistical_form,
                         self.statistical_form_page.actual_url_after_statistical_form())
        # 点击里程报表
        self.statistical_form_page.click_mileage_form_buttons()
        # 断言
        self.assertEqual(self.assert_text.statistical_form_mile_form(),
                         self.statistical_form_page.actual_text_after_click_mileage_form_buttons())

        # 读取查询数据
        csv_file = self.statistical_form_page_read_csv.read_csv('milage_report_search_datas.csv')
        csv_data = csv.reader(csv_file)
        is_header = True
        for row in csv_data:
            if is_header:
                is_header = False
                continue
            search_data = {
                'search_user': row[0],
                'type': row[1],
                'choose_date': row[2],
                'begin_time': row[3],
                'end_time': row[4]
            }
            self.statistical_form_page.add_datas_to_search_mileage_form(search_data)
            self.statistical_form_page.switch_to_mile_report_form_frame()
            all_dev = self.seasrch_sql.search_current_account_equipment(search_data['search_user'])
            print(all_dev)
            imeis = self.statistical_form_page3.change_dev_imei_format(all_dev)
            print(imeis)
            begin_time = self.statistical_form_page3.get_mile_report_form_begin_time()
            end_time = self.statistical_form_page3.get_mile_report_form_end_time()
            if search_data['type'] == 'mile':
                # 获取页面总共得到的总页数
                sleep(4)
                total_page = self.statistical_form_page3.get_total_page_in_mile_report_form()
                print(total_page)

                if total_page == 0:
                    # 连接数据库
                    all_dev = self.seasrch_sql.search_current_account_equipment(search_data['search_user'])
                    imeis = self.statistical_form_page3.change_dev_imei_format(all_dev)
                    req_type = ''
                    if search_data['type'] == 'mile':
                        req_type = 'segment'
                    elif search_data['type'] == 'day':
                        req_type = 'day'
                    begin_time = self.statistical_form_page3.get_mile_report_form_begin_time()
                    end_time = self.statistical_form_page3.get_mile_report_form_end_time()

                    # 连接接口
                    request_url = request_base_url()
                    request_params = {
                        '_method_': 'getMileage',
                        'imeis': imeis,
                        'type': req_type,
                        'startTime': begin_time,
                        'endTime': end_time,
                        'startRow': 0
                    }
                    res = requests.post(request_url, data=request_params)
                    sleep(30)
                    response = res.json()
                    print(response)
                    self.assertEqual(400, response['code'])
                    self.assertEqual('没有找到数据', response['msg'])

                elif total_page == 1:
                    # 获取这一个页有多少条记录
                    total_number_per_page = self.statistical_form_page3.get_total_number_per_page_in_mile_report_form()
                    web_data = []
                    for n in range(total_number_per_page):
                        web_data.append({
                            'imei': self.statistical_form_page3.get_imei_in_mile_report_form(n),
                            'distance': self.statistical_form_page3.get_distance_in_mile_report_form(n),
                            'startTime': self.statistical_form_page3.get_start_time_in_mile_report_form(n),
                            'endTime': self.statistical_form_page3.get_end_time_in_mile_report_form(n),
                        })
                    print('web', web_data)
                    # 连接数据库
                    all_dev = self.seasrch_sql.search_current_account_equipment(search_data['search_user'])
                    imeis = self.statistical_form_page3.change_dev_imei_format(all_dev)
                    req_type = ''
                    if search_data['type'] == 'mile':
                        req_type = 'segment'
                    elif search_data['type'] == 'day':
                        req_type = 'day'
                    begin_time = self.statistical_form_page3.get_mile_report_form_begin_time()
                    end_time = self.statistical_form_page3.get_mile_report_form_end_time()

                    # 连接接口
                    request_url = request_base_url()
                    request_params = {
                        '_method_': 'getMileage',
                        'imeis': imeis,
                        'type': req_type,
                        'startTime': begin_time,
                        'endTime': end_time,
                    }
                    res = requests.post(request_url, data=request_params)
                    sleep(30)
                    response = res.json()
                    res_data = response['data']
                    for data in res_data:
                        del data['avgSpeed'], data['startLat'], data['startLng'], data['endLat'], data['endLng'], data[
                            'runTimeSecond']
                    for data in res_data:
                        data['distance'] = float('%.3f' % (data['distance'] / 1000))
                    print('res', res_data)
                    self.assertEqual(web_data, res_data)
                else:
                    web_data = []
                    for i in range(total_page):
                        # 循环点击每一页
                        self.statistical_form_page3.click_per_page_in_mile_report_form(i)
                        total_number_per_page = self.statistical_form_page3.get_total_number_per_page_in_mile_report_form()
                        for n in range(total_number_per_page):
                            web_data.append({
                                'imei': self.statistical_form_page3.get_imei_in_mile_report_form(n),
                                'distance': self.statistical_form_page3.get_distance_in_mile_report_form(n),
                                'startTime': self.statistical_form_page3.get_start_time_in_mile_report_form(n),
                                'endTime': self.statistical_form_page3.get_end_time_in_mile_report_form(n),
                            })
                    print(web_data)
                    # 连接数据库
                    all_dev = self.seasrch_sql.search_current_account_equipment(search_data['search_user'])
                    imeis = self.statistical_form_page3.change_dev_imei_format(all_dev)
                    req_type = ''
                    if search_data['type'] == 'mile':
                        req_type = 'segment'
                    elif search_data['type'] == 'day':
                        req_type = 'day'
                    begin_time = self.statistical_form_page3.get_mile_report_form_begin_time()
                    end_time = self.statistical_form_page3.get_mile_report_form_end_time()

                    # 连接接口
                    request_url = request_base_url()
                    request_params = {
                        '_method_': 'getMileage',
                        'imeis': imeis,
                        'type': req_type,
                        'startTime': begin_time,
                        'endTime': end_time,
                        'startRow': 0
                    }
                    res = requests.post(request_url, data=request_params)
                    sleep(30)
                    response = res.json()
                    res_data = response['data']
                    for data in res_data:
                        del data['avgSpeed'], data['startLat'], data['startLng'], data['endLat'], data['endLng'], data[
                            'runTimeSecond']
                    for data in res_data:
                        data['distance'] = float('%.3f' % (data['distance'] / 1000))
                    print(res_data)
                    self.assertEqual(web_data, res_data)

            elif search_data['type'] == 'day':
                # 获取页面总共得到的总页数
                sleep(4)
                total_page = self.statistical_form_page3.get_total_page_in_mile_report_form_with_day()
                print(total_page)

                if total_page == 0:
                    # 连接数据库
                    all_dev = self.seasrch_sql.search_current_account_equipment(search_data['search_user'])
                    imeis = self.statistical_form_page3.change_dev_imei_format(all_dev)
                    req_type = ''
                    if search_data['type'] == 'mile':
                        req_type = 'segment'
                    elif search_data['type'] == 'day':
                        req_type = 'day'
                    begin_time = self.statistical_form_page3.get_mile_report_form_begin_time()
                    end_time = self.statistical_form_page3.get_mile_report_form_end_time()

                    # 连接接口
                    request_url = request_base_url()
                    request_params = {
                        '_method_': 'getMileage',
                        'imeis': imeis,
                        'type': req_type,
                        'startTime': begin_time,
                        'endTime': end_time,
                        'startRow': 0,
                    }
                    res = requests.post(request_url, data=request_params)
                    sleep(30)
                    response = res.json()
                    print(response)
                    self.assertEqual(400, response['code'])
                    self.assertEqual('没有找到数据', response['msg'])

                elif total_page == 1:
                    # 获取这一个页有多少条记录
                    total_number_per_page = self.statistical_form_page3.get_total_number_per_page_in_mile_report_form_with_day()
                    web_data = []
                    for n in range(total_number_per_page):
                        web_data.append({
                            'imei': self.statistical_form_page3.get_imei_in_mile_report_form_with_day(n),
                            'distance': self.statistical_form_page3.get_distance_in_mile_report_form_with_day(n),
                            'atDay': self.statistical_form_page3.get_at_day_time_in_mile_report_form_with_day(n)
                        })
                    print(web_data)
                    # 连接数据库
                    all_dev = self.seasrch_sql.search_current_account_equipment(search_data['search_user'])
                    imeis = self.statistical_form_page3.change_dev_imei_format(all_dev)
                    req_type = ''
                    if search_data['type'] == 'mile':
                        req_type = 'segment'
                    elif search_data['type'] == 'day':
                        req_type = 'day'
                    begin_time = self.statistical_form_page3.get_mile_report_form_begin_time()
                    end_time = self.statistical_form_page3.get_mile_report_form_end_time()

                    # 连接接口
                    request_url = request_base_url()
                    request_params = {
                        '_method_': 'getMileage',
                        'imeis': imeis,
                        'type': req_type,
                        'startTime': begin_time,
                        'endTime': end_time,
                        'startRow': 0
                    }
                    res = requests.post(request_url, data=request_params)
                    sleep(30)
                    response = res.json()
                    res_data = response['data']
                    for data in res_data:
                        del data['avgSpeed'], data['startLat'], data['startLng'], data['endLat'], data['endLng'], data[
                            'runTimeSecond']
                    for data in res_data:
                        data['distance'] = float('%.3f' % (data['distance'] / 1000))
                    for data in res_data:
                        data['atDay'] = data['atDay'].split(' ')[0]
                    print(res_data)
                    self.assertEqual(web_data, res_data)
                else:
                    web_data = []
                    for i in range(total_page):
                        # 循环点击每一页
                        self.statistical_form_page3.click_per_page_in_mile_report_form(i)
                        total_number_per_page = self.statistical_form_page3.get_total_number_per_page_in_mile_report_form_with_day()
                        for n in range(total_number_per_page):
                            web_data.append({
                                'imei': self.statistical_form_page3.get_imei_in_mile_report_form_with_day(n),
                                'distance': self.statistical_form_page3.get_distance_in_mile_report_form_with_day(n),
                                'atDay': self.statistical_form_page3.get_at_day_time_in_mile_report_form_with_day(n)
                            })
                    print(web_data)
                    # 连接数据库
                    all_dev = self.seasrch_sql.search_current_account_equipment(search_data['search_user'])
                    imeis = self.statistical_form_page3.change_dev_imei_format(all_dev)
                    req_type = ''
                    if search_data['type'] == 'mile':
                        req_type = 'segment'
                    elif search_data['type'] == 'day':
                        req_type = 'day'
                    begin_time = self.statistical_form_page3.get_mile_report_form_begin_time()
                    end_time = self.statistical_form_page3.get_mile_report_form_end_time()

                    # 连接接口
                    request_url = request_base_url()
                    request_params = {
                        '_method_': 'getMileage',
                        'imeis': imeis,
                        'type': req_type,
                        'startTime': begin_time,
                        'endTime': end_time,
                        'startRow': 0,
                    }
                    res = requests.post(request_url, data=request_params)
                    sleep(30)
                    response = res.json()
                    res_data = response['data']
                    for data in res_data:
                        del data['avgSpeed'], data['startLat'], data['startLng'], data['endLat'], data['endLng'], data[
                            'runTimeSecond']
                    for data in res_data:
                        data['distance'] = float('%.3f' % (data['distance'] / 1000))
                    for data in res_data:
                        data['atDay'] = data['atDay'].split(' ')[0]
                    print(res_data)
                    self.assertEqual(web_data, res_data)

            # 请求行程报表总计 - 总里程
            request_url = request_base_url()
            req_data = {
                '_method_': 'getMileage',
                'imeis': imeis,
                'startTime': begin_time,
                'endTime': end_time,
            }
            res = requests.post(request_url, data=req_data)
            response_data = res.json()
            if response_data['code'] == 0:
                data_total = '%.3f' % response_data['data'][0]['totalDistiance']
                web_total = ''
                if search_data['type'] == 'mile':
                    web_total = self.statistical_form_page3.get_web_total_in_mile_form_with_search_mile()
                elif search_data['type'] == 'day':
                    web_total = self.statistical_form_page3.get_web_total_in_mile_form_with_search_day()
                self.assertEqual(data_total, web_total)
            self.driver.default_frame()
        csv_file.close()
