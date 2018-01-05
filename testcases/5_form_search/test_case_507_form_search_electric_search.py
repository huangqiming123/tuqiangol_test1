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


class TestCase507FormSearchElectricSearch(unittest.TestCase):
    # 测试 报表 电量报表查询
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
        self.assert_text = AssertText()
        self.search_sql = SearchSql(self.driver, self.base_url)
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
        self.driver.close_window()
        # 退出浏览器
        self.driver.quit_browser()

    def test_case_electric_search(self):
        # 断言url
        expect_url_after_click_statistical_form = self.base_url + '/deviceReport/statisticalReport'
        self.assertEqual(expect_url_after_click_statistical_form,
                         self.statistical_form_page.actual_url_after_statistical_form())
        # 点击里程报表
        self.statistical_form_page.click_electric_report_form_buttons()
        # 断言
        self.assertEqual(self.assert_text.statistical_form_electric_report(),
                         self.statistical_form_page.actual_text_after_click_electric_report_buttons())
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

            all_dev = self.search_sql.search_current_account_equipment(search_data['search_user'])
            all_user_dev = self.search_sql.search_current_account_equipment_and_next(search_data['search_user'])
            connect = self.connect_sql.connect_tuqiang_sql()
            cursor = connect.cursor()
            get_electric_total_sql = self.search_sql.get_total_electric_report_sql(all_user_dev, all_dev, search_data)
            print(get_electric_total_sql)
            cursor.execute(get_electric_total_sql)
            get_total_number = cursor.fetchall()
            total_list = []
            for range1 in get_total_number:
                for range2 in range1:
                    total_list.append(range2)
            cursor.close()
            connect.close()
            total = len(total_list)
            web_total = self.statistical_form_page.get_web_total_electric_report()
            self.assertEqual(total, web_total)
        csv_file.close()
