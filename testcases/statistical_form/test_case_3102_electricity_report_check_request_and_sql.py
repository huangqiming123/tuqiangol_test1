import csv
import unittest

import requests

from automate_driver.automate_driver import AutomateDriver
from model.connect_sql import ConnectSql
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.statistical_form.search_sql import SearchSql
from pages.statistical_form.statistical_form_page import StatisticalFormPage
from pages.statistical_form.statistical_form_page_read_csv import StatisticalFormPageReadCsv


class TestCase142SportStatisticalElectricReport(unittest.TestCase):
    '''
    方案2 获取请求的数据和数据库进行对比
    数据库查出来的数据和获取请求数据的数据序列不一致
    方法：验证查出来的数量，然后验证请求的数据必须在sql的列表里面
    author:zhangAo
    '''

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
        # 打开页面，填写用户名、密码、点击登录

    def tearDown(self):
        # 退出浏览器
        pass

    def test_case_3102_electricity_report_check_request_and_sql(self):
        csv_file = self.statistical_form_page_read_csv.read_csv('search_electric_report_data.csv')
        csv_data = csv.reader(csv_file)
        is_header = True
        for row in csv_data:
            if is_header:
                is_header = False
                continue
            search_data = {
                'search_user': row[0],
                'electric': row[1],
                'dev_type': row[2],
                'next': row[3]
            }
            all_dev = self.search_sql.search_current_account_equipment(search_data['search_user'])
            all_user_dev = self.search_sql.search_current_account_equipment_and_next(search_data['search_user'])
            connect = self.connect_sql.connect_tuqiang_sql()
            cursor = connect.cursor()
            get_electric_total_sql = self.search_sql.get_total_electric_report_sqls(all_user_dev, all_dev, search_data)
            cursor.execute(get_electric_total_sql)
            data = cursor.fetchall()
            sql_list = []
            for rang1 in data:
                for range2 in rang1:
                    sql_list.append(range2)
            web_dev_name = []
            web_dev_electricity = []
            web_dev_imei = []
            web_dev_user_name = []
            for n in range(len(sql_list)):
                if n % 4 == 0:
                    web_dev_name.append(sql_list[n])
                elif n % 4 == 1:
                    web_dev_electricity.append(sql_list[n])
                elif n % 4 == 2:
                    web_dev_imei.append(sql_list[n])
                elif n % 4 == 3:
                    web_dev_user_name.append(sql_list[n])
            print(web_dev_name)
            print(web_dev_electricity)
            print(web_dev_imei)
            print(web_dev_user_name)

            if search_data['next'] == '':
                self.next = 1
            if search_data['next'] == '1':
                self.next = 0
            user_id = self.search_sql.search_current_account(search_data['search_user'])
            playload = {
                'electricity': int(row[1]),
                'mcType': row[2],
                'containSubordinate': self.next,
                'userId': user_id
            }
            headers = self.statistical_form_page.get_headers_for_post_request()
            # headers = {
            #    'Cookie': 'JSESSIONID=0F3EDD7A72D86C3521C3F80F5719140B'
            # }
            # request库提交post请求，其中包含请求参数，请求头
            r = requests.post('http://tuqiangol.com/electricityReportController/list', params=playload, headers=headers)
            data = r.text.split('[')[1].split(']')[0]
            dev_list = eval(data)
            dev_name = []
            dev_electricity = []
            dev_imei = []
            dev_user_name = []
            if len(web_dev_name) == 1:
                dev_name.append(dev_list['deviceName'])
                dev_electricity.append(dev_list['electricity'])
                dev_imei.append(dev_list['imei'])
                dev_user_name.append(dev_list['userName'])
                print(dev_name)
                print(dev_electricity)
                print(dev_imei)
                print(dev_user_name)
                self.assertEqual(dev_name, web_dev_name)
                self.assertEqual(dev_electricity, web_dev_electricity)
                self.assertEqual(dev_imei, web_dev_imei)
                self.assertEqual(dev_user_name, web_dev_user_name)
            else:
                for n in range(len(dev_list)):
                    self.assertIn(dev_list[n]['deviceName'], web_dev_name)
                    self.assertIn(dev_list[n]['electricity'], web_dev_electricity)
                    self.assertIn(dev_list[n]['imei'], web_dev_imei)
                    self.assertIn(dev_list[n]['userName'], web_dev_user_name)
                    dev_name.append(dev_list[n]['deviceName'])
                    dev_electricity.append(dev_list[n]['electricity'])
                    dev_imei.append(dev_list[n]['imei'])
                    dev_user_name.append(dev_list[n]['userName'])
                print(dev_name)
                print(dev_electricity)
                print(dev_imei)
                print(dev_user_name)
                self.assertEqual(len(dev_name), len(web_dev_name))
                self.assertEqual(len(dev_electricity), len(web_dev_electricity))
                self.assertEqual(len(dev_imei), len(web_dev_imei))
                self.assertEqual(len(dev_user_name), len(web_dev_user_name))
            cursor.close()
            connect.close()
        csv_file.close()
