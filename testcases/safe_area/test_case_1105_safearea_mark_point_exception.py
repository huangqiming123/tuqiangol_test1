import unittest
from automate_driver.automate_driver_server import AutomateDriverServer
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer
from pages.safe_area.safe_area_page import SafeAreaPage


class TestCase1105SafeAreaMarkPointException(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriverServer()
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.log_in_base = LogInBaseServer(self.driver, self.base_url)
        self.safe_area_page = SafeAreaPage(self.driver, self.base_url)

        self.base_page.open_page()
        self.driver.set_window_max()
        self.log_in_base.log_in_jimitest()
        self.safe_area_page.click_control_after_click_safe_area()

    def tearDown(self):
        self.driver.quit_browser()

    def test_case_1105_safe_area_mark_point_exception(self):
        # 断言url
        expect_url = self.base_url + "/safearea/geozonemap?flag=0"
        self.assertEqual(expect_url, self.driver.get_current_url())
        # 点击标注点
        self.safe_area_page.click_mark_button()

        # 循环点击下一页
        page_number = self.safe_area_page.get_total_page_num_mark_page()
        if page_number == '0':
            text = self.safe_area_page.get_page_in_mark_page()
            self.assertEqual('0/0', text)
        elif page_number == '1':
            text = self.safe_area_page.get_page_in_mark_page()
            self.assertEqual('1/1', text)

            # 点击下一页
            self.safe_area_page.click_next_page_in_mark_page()
            # 获取最后一页数量
            number = self.safe_area_page.get_per_number_in_mark_page()
            self.assertNotEqual(0, number)

            # 点击上一页
            self.safe_area_page.click_ago_page_in_mark_page()
            number = self.safe_area_page.get_per_number_in_mark_page()
            self.assertNotEqual(0, number)
        else:
            for n in range(int(page_number)):
                text = self.safe_area_page.get_page_in_mark_page()
                self.assertEqual('%s/%s' % (str(n + 1), page_number), text)
                self.safe_area_page.click_next_page_in_mark_page()
            # 点击下一页
            self.safe_area_page.click_next_page_in_mark_page()
            # 获取最后一页数量
            number = self.safe_area_page.get_per_number_in_mark_page()
            self.assertNotEqual(0, number)

            for n in range(int(page_number)):
                text = self.safe_area_page.get_page_in_mark_page()
                self.assertEqual('%s/%s' % (str(int(page_number) - n), page_number), text)
                self.safe_area_page.click_ago_page_in_mark_page()

            # 点击上一页
            self.safe_area_page.click_ago_page_in_mark_page()
            number = self.safe_area_page.get_per_number_in_mark_page()
            self.assertNotEqual(0, number)
