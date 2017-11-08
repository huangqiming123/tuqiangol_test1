import csv
import unittest
from time import sleep

from automate_driver.automate_driver_server import AutomateDriverServer
from model.assert_text import AssertText
from model.connect_sql import ConnectSql
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer
from pages.safe_area.safe_area_page import SafeAreaPage
from pages.safe_area.safe_area_page_read_csv import SafeAreaPageReadCsv
from pages.safe_area.safe_area_search_sql import SafeAreaSearchSql


class TestCase139RiskPointShare(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriverServer()
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.log_in_base = LogInBaseServer(self.driver, self.base_url)
        self.safe_area_page = SafeAreaPage(self.driver, self.base_url)

        self.base_page.open_page()
        self.base_page.click_chinese_button()
        self.driver.set_window_max()
        self.assert_text = AssertText()
        self.log_in_base.log_in_jimitest()
        self.connect_sql = ConnectSql()
        self.search_sql = SafeAreaSearchSql()
        self.safe_area_page_read_csv = SafeAreaPageReadCsv()

    def tearDown(self):
        self.driver.quit_browser()

    def test_case_139_risk_point_share(self):
        # 点击账号中心
        sleep(5)
        self.safe_area_page.click_account_center()
        # 获取登录账号
        account = self.safe_area_page.get_current_account_in_account_center()
        # 断言url
        self.safe_area_page.click_control_after_click_safe_area()
        expect_url = self.base_url + "/safearea/geozonemap?flag=0"
        self.assertEqual(expect_url, self.driver.get_current_url())

        self.safe_area_page.click_risk_point_share_button()
        csv_file = self.safe_area_page_read_csv.read_csv('risk_point_share.csv')
        csv_data = csv.reader(csv_file)

        is_header = True
        for row in csv_data:
            if is_header:
                is_header = False
                continue
            data = {
                'risk_name': row[0]
            }
            self.safe_area_page.add_data_to_search_risk_point_in_safe_area(data)
            # 获取查询出来的页面条数
            web_total = self.safe_area_page.get_web_total_after_click_search_risk_share()
            sql_total = self.safe_area_page.get_sql_total_after_click_search_risk_share(data)
            self.assertEqual(web_total, sql_total)
        csv_file.close()
