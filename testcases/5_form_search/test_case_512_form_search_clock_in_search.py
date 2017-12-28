import csv
import unittest
from time import sleep
from automate_driver.automate_driver import AutomateDriver
from model.assert_text import AssertText
from model.connect_sql import ConnectSql
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.statistical_form.clock_in_page import ClockInPage
from pages.statistical_form.obd_form_page import ObdFormPage
from pages.statistical_form.search_sql import SearchSql
from pages.statistical_form.statistical_form_page import StatisticalFormPage
from pages.statistical_form.statistical_form_page_read_csv import StatisticalFormPageReadCsv


class TestCase512FormSearchClockInSearch(unittest.TestCase):
    # 测试 报表搜索 打卡报表搜索
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
        self.clock_in_page = ClockInPage(self.driver, self.base_url)
        # 打开页面，填写用户名、密码、点击登录
        self.base_page.open_page()
        self.driver.set_window_max()
        self.driver.implicitly_wait(5)
        self.driver.clear_cookies()
        self.log_in_base.log_in_jimitest()
        self.assert_text = AssertText()

        # 登录之后点击控制台，然后点击设置
        self.statistical_form_page.click_control_after_click_statistical_form_page()
        sleep(3)

    def tearDown(self):
        # 退出浏览器
        self.driver.quit_browser()

    def test_case_clock_in_search(self):
        # 断言url
        expect_url_after_click_statistical_form = self.base_url + '/deviceReport/statisticalReport'
        self.assertEqual(expect_url_after_click_statistical_form,
                         self.statistical_form_page.actual_url_after_statistical_form())

        # 点击打卡记录
        self.clock_in_page.click_clock_in_form_button()
        # 切换到打开记录的frame里面
        self.clock_in_page.switch_to_click_in_form_frame()

        csv_file = self.statistical_form_page_read_csv.read_csv('clock_in_form_data.csv')
        csv_data = csv.reader(csv_file)
        is_header = True
        for row in csv_data:
            if is_header:
                is_header = False
                continue
            data = {
                'date_type': row[0],
                'begin_time': row[1],
                'end_time': row[2],
                'dev_type': row[3],
                'dev_imei': row[4],
                'clock_in_type': row[5]
            }
            self.clock_in_page.add_data_to_search_click_in_form(data)
            get_sql_data = self.clock_in_page.get_sql_data_in_clock_in_form(data)
            print(get_sql_data)
            web_list = []
            # 获取查询的页数
            number = self.clock_in_page.get_page_number_after_search_clock_in_form()
            if number == 0:
                text = self.clock_in_page.get_no_data_text_in_clock_form()
                self.assertIn(self.assert_text.account_center_page_no_data_text(), text)

            elif number == 1:
                # 获取每一页的条数
                per_page_number = self.clock_in_page.get_per_page_number_in_clock_in_form()
                for n in range(per_page_number):
                    web_list.append({
                        'imei': self.clock_in_page.get_imei_in_clock_in_form(n),
                        'time': self.clock_in_page.get_time_in_clock_form(n),
                        'on_off': self.clock_in_page.get_on_off_in_clock_form(n)
                    })
                print(web_list)
                self.assertEqual(get_sql_data, web_list)
            else:
                # 循环点击每一页
                for n in range(number):
                    self.clock_in_page.click_per_page(n)
                    per_page_number = self.clock_in_page.get_per_page_number_in_clock_in_form()
                    for n in range(per_page_number):
                        web_list.append({
                            'imei': self.clock_in_page.get_imei_in_clock_in_form(n),
                            'time': self.clock_in_page.get_time_in_clock_form(n),
                            'on_off': self.clock_in_page.get_on_off_in_clock_form(n)
                        })
                print(web_list)
                self.assertEqual(get_sql_data, web_list)
        self.driver.default_frame()
