import csv
import unittest
from time import sleep
from automate_driver.automate_driver import AutomateDriver
from model.assert_text import AssertText
from model.connect_sql import ConnectSql
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.statistical_form.search_sql import SearchSql
from pages.statistical_form.statistical_form_page import StatisticalFormPage
from pages.statistical_form.statistical_form_page_read_csv import StatisticalFormPageReadCsv


class TestCase154OilReport(unittest.TestCase):
    '''
    用例第154条，
    author ：zhangAo
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
        self.assert_text = AssertText()

        # 登录之后点击控制台，然后点击设置
        self.statistical_form_page.click_control_after_click_statistical_form_page()
        sleep(3)

    def tearDown(self):
        # 退出浏览器
        self.driver.quit_browser()

    def test_case_154_oil_report(self):
        # 断言url
        expect_url_after_click_statistical_form = self.base_url + '/deviceReport/statisticalReport'
        self.assertEqual(expect_url_after_click_statistical_form,
                         self.statistical_form_page.actual_url_after_statistical_form())

        # 点击停留报表
        self.statistical_form_page.click_oil_reoport()
        # 断言
        self.assertEqual(self.assert_text.statistical_form_oil_form(),
                         self.statistical_form_page.actual_text_after_click_oil_report_button())

        # # 读取查询数据
        csv_file = self.statistical_form_page_read_csv.read_csv('oil_report_search_data.csv')
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
            self.statistical_form_page.switch_to_oil_report()
            self.statistical_form_page.add_data_to_search_oil_report(search_data)
            all_dev = self.search_sql.search_current_account_equipment(search_data['search_user'])
            connect = self.connect_sql.connect_tuqiang_form()
            cursor = connect.cursor()
            get_total_sql = self.search_sql.get_oil_report_total_sql(all_dev)
            cursor.execute(get_total_sql)
            data = cursor.fetchall()
            total = len(data)
            web_total = self.statistical_form_page.get_total_in_oil_report()
            self.assertEqual(total, web_total)
            cursor.close()
            connect.close()
            self.driver.default_frame()
        csv_file.close()