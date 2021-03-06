import unittest
from automate_driver.automate_driver_server import AutomateDriverServer
from model.assert_text import AssertText
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer
from pages.safe_area.safe_area_page import SafeAreaPage


class TestCase133SafeAreaSwitch(unittest.TestCase):
    """ jimitest账号，区域预警----围栏、黑车地址库验证 """

    # author：邓肖斌

    def setUp(self):
        self.driver = AutomateDriverServer(choose='chrome')
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.log_in_base = LogInBaseServer(self.driver, self.base_url)
        self.safe_area_page = SafeAreaPage(self.driver, self.base_url)

        self.base_page.open_page()
        self.base_page.click_chinese_button()
        self.assert_text = AssertText()
        self.driver.set_window_max()
        self.log_in_base.log_in_jimitest()
        self.safe_area_page.click_control_after_click_safe_area()

    def tearDown(self):
        self.driver.quit_browser()

    def test_case_safe_area_switch(self):
        # 断言url
        expect_url = self.base_url + "/safearea/geozonemap?flag=0"
        self.assertEqual(expect_url, self.driver.get_current_url())

        # 选择围栏
        self.safe_area_page.click_select_fence_button()

        # 验证显示的是不是全是围栏
        # 获取总共有几页
        number = self.safe_area_page.get_total_page_num()
        if number == '0':
            numbers = self.safe_area_page.get_per_number()
            self.assertEqual(0, numbers)
            print('围栏无数据')
        else:
            for n in range(int(number)):
                # 获取这一页有多少条
                if number == '1':
                    numbers = self.safe_area_page.get_per_number()
                    for m in range(numbers):
                        text = self.safe_area_page.get_text_safe_area_type(m)
                        self.assertEqual(self.assert_text.safe_area_page_geo_fence(), text)
                else:
                    numbers = self.safe_area_page.get_per_number()
                    for m in range(numbers):
                        text = self.safe_area_page.get_text_safe_area_type(m)
                        self.assertEqual(self.assert_text.safe_area_page_geo_fence(), text)
                    self.safe_area_page.click_next_page()

        # 选择黑车地址库
        self.safe_area_page.click_select_black_address_button()
        number = self.safe_area_page.get_total_page_num()
        if number == '0':
            numbers = self.safe_area_page.get_per_number()
            self.assertEqual(0, numbers)
            print('黑车库无数据')
        else:
            for n in range(int(number)):
                # 获取这一页有多少条
                if number == '1':
                    numbers = self.safe_area_page.get_per_number()
                    for m in range(numbers):
                        text = self.safe_area_page.get_text_safe_area_type(m)
                        self.assertEqual(self.assert_text.safe_area_page_black_car_address_text(), text)
                else:
                    numbers = self.safe_area_page.get_per_number()
                    for m in range(numbers):
                        text = self.safe_area_page.get_text_safe_area_type(m)
                        self.assertEqual(self.assert_text.safe_area_page_black_car_address_text(), text)
                    self.safe_area_page.click_next_page()
