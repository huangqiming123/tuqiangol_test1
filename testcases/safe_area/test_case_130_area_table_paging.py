'''import unittest
from automate_driver.automate_driver_server import AutomateDriverServer
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer
from pages.safe_area.safe_area_page import SafeAreaPage
from pages.safe_area.safe_area_page_read_csv import SafeAreaPageReadCsv


class TestCase130AreaTablePaging(unittest.TestCase):
    """ web_autotest账号，区域告警--分页功能 """
    # author：邓肖斌

    def setUp(self):
        self.driver = AutomateDriverServer()
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.log_in_base = LogInBaseServer(self.driver, self.base_url)
        self.safe_area_page = SafeAreaPage(self.driver, self.base_url)

        self.base_page.open_page()
        self.base_page.click_chinese_button()
        self.driver.set_window_max()
        self.log_in_base.log_in()
        self.safe_area_page.click_control_after_click_safe_area()
        self.safe_area_page_read_csv = SafeAreaPageReadCsv()

    def tearDown(self):
        self.driver.quit_browser()

    def test_case_area_table_paging(self):
        # 断言url
        expect_url = self.base_url + "/safearea/geozonemap?flag=0"
        self.assertEqual(expect_url, self.driver.get_current_url())

        # 获取当前页面和总数
        total_page = self.safe_area_page.get_total_page_num()

        if total_page == '0':
            print('无数据！')
        elif total_page == '1':
            print('就一页！')
        else:
            # 下一页
            self.safe_area_page.click_next_page()
            self.assertEqual('2', self.safe_area_page.get_current_page_number())
            # 点击上一页
            self.safe_area_page.click_ago_page()
            self.assertEqual('1', self.safe_area_page.get_current_page_number())

            # 点击尾页
            self.safe_area_page.click_last_page()
            self.assertEqual(self.safe_area_page.get_current_page_number(), self.safe_area_page.get_total_page_num())
            # 点击首页
            self.safe_area_page.clcik_first_page()
            self.assertEqual('1', self.safe_area_page.get_current_page_number())
'''
