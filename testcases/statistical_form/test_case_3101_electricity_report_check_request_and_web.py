import csv
import unittest
from time import sleep

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
    两种方案，第一获取请求的数据和页面上的元素进行对比
    页面上的数据就是http请求得到的数据
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

    def test_case_3101_electricity_report_check_request_and_web(self):
        # 断言url
        expect_url_after_click_statistical_form = self.base_url + '/deviceReport/statisticalReport'
        self.assertEqual(expect_url_after_click_statistical_form,
                         self.statistical_form_page.actual_url_after_statistical_form())
        # 点击里程报表
        self.statistical_form_page.click_electric_report_form_buttons()
        # 断言
        self.assertEqual('电量统计', self.statistical_form_page.actual_text_after_click_electric_report_buttons())
        # 读取查询数据
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
            self.statistical_form_page.add_data_to_search_electric_report(search_data)
            self.statistical_form_page.switch_to_electricity_report_frame()

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
            print(data)

            if data != '':
                # 将字符串类型的data转化成字典型的dev_list
                dev_list = eval(data)
                # 获取列表有多少页
                web_page = self.statistical_form_page.get_web_page_electric_report()
                # 分三种情况，0,1,其他
                if web_page == 0:
                    pass
                elif web_page == 1:
                    # 获取本页有多少条数据
                    web_page_list = self.statistical_form_page.get_web_page_list_electric_report()
                    # 循环
                    for x in range(web_page_list):
                        # 分别获取 设备名称，设备电量，imei，设备类型，所属用户
                        dev_name_web = self.statistical_form_page.get_dev_name_in_electric_report(x)
                        dev_electricity_web = self.statistical_form_page.get_dev_electricity_web_in_electric_report(x)
                        dev_imei_web = self.statistical_form_page.get_dev_imei_web_in_electric_report(x)
                        dev_type_web = self.statistical_form_page.get_dev_type_web_in_electric_report(x)
                        dev_user_name_web = self.statistical_form_page.get_dev_user_name_web_in_electric_report(x)
                        if web_page_list != 1:
                            self.assertEqual(dev_list[x]['deviceName'], dev_name_web)
                            self.assertEqual('%s' % str(dev_list[x]['electricity']) + '%', dev_electricity_web)
                            self.assertEqual(dev_list[x]['imei'], dev_imei_web)
                            self.assertEqual(dev_list[x]['mcType'].strip(), dev_type_web)
                            self.assertEqual(dev_list[x]['userName'], dev_user_name_web)
                        else:
                            # 特殊情况，当只有一条数据时，字典只有一个，无法获取到下标
                            self.assertEqual(dev_list['deviceName'], dev_name_web)
                            self.assertEqual('%s' % str(dev_list['electricity']) + '%', dev_electricity_web)
                            self.assertEqual(dev_list['imei'], dev_imei_web)
                            self.assertEqual(dev_list['mcType'].strip(), dev_type_web)
                            self.assertEqual(dev_list['userName'], dev_user_name_web)
                else:
                    # 当页面有多页时，使用两个for循环嵌套
                    for m in range(web_page):
                        self.statistical_form_page.click_per_page_in_electric_report_form(m)
                        web_page_list = self.statistical_form_page.get_web_page_list_electric_report()
                        for x in range(web_page_list):
                            dev_name_web = self.statistical_form_page.get_dev_name_in_electric_report(x)
                            dev_electricity_web = self.statistical_form_page.get_dev_electricity_web_in_electric_report(
                                x)
                            dev_imei_web = self.statistical_form_page.get_dev_imei_web_in_electric_report(x)
                            dev_type_web = self.statistical_form_page.get_dev_type_web_in_electric_report(x)
                            dev_user_name_web = self.statistical_form_page.get_dev_user_name_web_in_electric_report(x)
                            self.assertEqual(dev_list[10 * m + x]['deviceName'], dev_name_web)
                            self.assertEqual('%s' % str(dev_list[10 * m + x]['electricity']) + '%', dev_electricity_web)
                            self.assertEqual(dev_list[10 * m + x]['imei'], dev_imei_web)
                            self.assertEqual(dev_list[10 * m + x]['mcType'].strip(), dev_type_web)
                            self.assertEqual(dev_list[10 * m + x]['userName'], dev_user_name_web)
            self.driver.default_frame()

        csv_file.close()
