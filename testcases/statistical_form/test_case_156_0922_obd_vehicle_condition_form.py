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


class TestCase156ObdVehicleConditionForm(unittest.TestCase):
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

        # 登录之后点击控制台，然后点击设置
        self.statistical_form_page.click_control_after_click_statistical_form_page()
        sleep(3)

    def tearDown(self):
        # 退出浏览器
        self.driver.quit_browser()

    def test_case_obd_vehicle_condition_form(self):
        # 断言url
        expect_url_after_click_statistical_form = self.base_url + '/deviceReport/statisticalReport'
        self.assertEqual(expect_url_after_click_statistical_form,
                         self.statistical_form_page.actual_url_after_statistical_form())

        # 点击obd统计的里程报表
        self.obd_form_page.click_obd_vehicle_condition_condition_form_button()
        # 切换到odb里程统计的frame里面
        self.obd_form_page.switch_to_obd_vehicle_condition_form_frame()

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
            self.obd_form_page.add_data_to_search_obd_vehicle_condition_form(search_data)

            # 获取页面上设备的信息
            dev_name = self.obd_form_page.get_dev_name_in_obd_vehicle_condition_form()
            dev_total_mile = self.obd_form_page.get_dev_total_mile_obd_vehicle_condition_form()
            dev_avg_oil = self.obd_form_page.get_dev_avg_oil_obd_vehicle_condition_form()
            dev_avg_speed = self.obd_form_page.get_avg_oil_obd_vehicle_condition_form()
            dev_total_oil = self.obd_form_page.get_dev_total_oil_obd_vehicle_condition_form()

            # 查询设备的名称
            sql_check_dev_name = self.obd_form_page.get_dev_name_in_sql(self.obd_form_page.search_imei())
            # 查询数据库的条数
            get_sql_total_number = self.obd_form_page.get_sql_total_number_in_tracel_form()
            get_web_total_number = self.obd_form_page.get_web_total_number_in_tracel_form()
            self.assertEqual(get_sql_total_number, get_web_total_number)

        self.driver.default_frame()
