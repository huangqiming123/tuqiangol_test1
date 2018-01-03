import csv
import unittest
from time import sleep
from automate_driver.automate_driver import AutomateDriver
from model.assert_text import AssertText
from model.connect_sql import ConnectSql
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.statistical_form.obd_form_page import ObdFormPage
from pages.statistical_form.search_sql import SearchSql
from pages.statistical_form.statistical_form_page import StatisticalFormPage
from pages.statistical_form.statistical_form_page_read_csv import StatisticalFormPageReadCsv


class TestCase508FormSearchObdMileageSearch(unittest.TestCase):
    # 测试 报表搜索 - OBD里程报表搜索
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
        # 退出浏览器
        self.driver.quit_browser()

    def test_case_obd_mileage_search(self):
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
            dev_name = self.obd_form_page.get_dev_name_in_obd_mileage_statistical_form()
            dev_total_mile = self.obd_form_page.get_dev_total_mile_obd_mileage_statistical_form()
            dev_avg_oil = self.obd_form_page.get_dev_avg_oil_obd_mileage_statistical_form()
            dev_avg_speed = self.obd_form_page.get_avg_oil_obd_mileage_statistical_form()
            dev_total_oil = self.obd_form_page.get_dev_total_oil_obd_mileage_statistical_form()

            # 查询设备的名称
            sql_check_dev_name = self.obd_form_page.get_dev_name_in_sql(self.obd_form_page.search_imei())

            # 查询数据库的条数
            get_sql_total_number = self.obd_form_page.get_sql_total_number()
            get_web_total_number = self.obd_form_page.get_web_total_number()
            self.assertEqual(len(get_sql_total_number), get_web_total_number[1])

            # 获取查询出来的 页数
            if get_web_total_number[0] != 0 and get_web_total_number[0] != 1:
                self.obd_form_page.click_first_page()
            total_page = self.obd_form_page.get_obd_list_total_page_number()
            if total_page == 0:
                self.assertEqual('0', dev_total_mile)
                self.assertEqual('0', dev_avg_oil)
                self.assertEqual('0', dev_avg_speed)
                self.assertEqual('0', dev_total_oil)

            elif total_page == 1:
                # 断言平均油耗
                # 查询设备的名称
                self.assertEqual(dev_name, sql_check_dev_name)
                count_avg_oil = '%.2f' % ((float(dev_total_oil) / float(dev_total_mile)) * 100)
                self.assertEqual(count_avg_oil, dev_avg_oil)
                # 获取页面上的里程和耗油
                mile_and_oil_list = []
                per_page_total_number = self.obd_form_page.get_per_page_total_number()
                for n in range(per_page_total_number):
                    mile_and_oil_list.append({
                        'mile': float(self.obd_form_page.get_per_mile_in_obd_mileage_form(n)),
                        'oil': float(self.obd_form_page.get_per_oil_in_obd_mileage_form(n)),
                    })
                print(mile_and_oil_list)
                total_mile = 0
                total_oil = 0
                for data in mile_and_oil_list:
                    total_mile += data['mile']
                    total_oil += data['oil']
                self.assertAlmostEqual(float(dev_total_mile), total_mile)
                self.assertAlmostEqual(float(dev_total_oil), total_oil)

                # 计算总时间 然后断言平均速度
                total_time = sum(get_sql_total_number)
                print(total_time)
                avg_speed = '%.2f' % ((float(dev_total_mile)) / float((float(total_time) / 3600)))
                self.assertEqual(avg_speed, dev_avg_speed)

            else:
                # 断言平均油耗
                self.assertEqual(dev_name, sql_check_dev_name)
                count_avg_oil = '%.2f' % ((float(dev_total_oil) / float(dev_total_mile)) * 100)
                self.assertEqual(count_avg_oil, dev_avg_oil)
                mile_and_oil_list = []
                for i in range(total_page):
                    # 循环点击每一页
                    self.obd_form_page.click_per_page(i)
                    # 获取页面上的里程和耗油
                    per_page_total_number = self.obd_form_page.get_per_page_total_number()
                    for n in range(per_page_total_number):
                        mile_and_oil_list.append({
                            'mile': float(self.obd_form_page.get_per_mile_in_obd_mileage_form(n)),
                            'oil': float(self.obd_form_page.get_per_oil_in_obd_mileage_form(n)),
                        })
                total_mile = 0
                total_oil = 0
                for data in mile_and_oil_list:
                    total_mile += data['mile']
                    total_oil += data['oil']

                self.assertAlmostEqual(float(dev_total_mile), total_mile)
                self.assertAlmostEqual(float(dev_total_oil), total_oil)

                # 计算总时间 然后断言平均速度
                total_time = sum(get_sql_total_number)
                avg_speed = '%.2f' % ((float(dev_total_mile)) / float((float(total_time) / 3600)))
                self.assertEqual(avg_speed, dev_avg_speed)
        csv_file.close()
        self.driver.default_frame()
