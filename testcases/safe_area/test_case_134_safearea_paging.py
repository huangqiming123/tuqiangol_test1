import unittest
from automate_driver.automate_driver_server import AutomateDriverServer
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer
from pages.safe_area.safe_area_page import SafeAreaPage


class TestCase134SafeAreaPaging(unittest.TestCase):
    """ web_autotest账号，区域预警----分页功能 """

    # author：邓肖斌

    def setUp(self):
        self.driver = AutomateDriverServer(choose='chrome')
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.log_in_base = LogInBaseServer(self.driver, self.base_url)
        self.safe_area_page = SafeAreaPage(self.driver, self.base_url)

        self.base_page.open_page()
        self.base_page.click_chinese_button()
        self.driver.set_window_max()
        self.log_in_base.log_in()
        self.safe_area_page.click_control_after_click_safe_area()

    def tearDown(self):
        self.driver.quit_browser()

    def test_case_safe_area_paging(self):
        # 断言url
        expect_url = self.base_url + "/safearea/geozonemap?flag=0"
        self.assertEqual(expect_url, self.driver.get_current_url())

        # 循环点击下一页
        page_number = self.safe_area_page.get_total_page_num()
        if page_number == '0':
            text = self.safe_area_page.get_page()
            self.assertEqual('0/0', text)
        elif page_number == '1':
            text = self.safe_area_page.get_page()
            self.assertEqual('1/1', text)

            # 点击下一页
            self.safe_area_page.click_next_page()
            # 获取最后一页数量
            number = self.safe_area_page.get_per_number()
            self.assertNotEqual(0, number)

            # 点击上一页
            self.safe_area_page.click_ago_page()
            number = self.safe_area_page.get_per_number()
            self.assertNotEqual(0, number)
        else:
            for n in range(int(page_number)):
                text = self.safe_area_page.get_page()
                self.assertEqual('%s/%s' % (str(n + 1), page_number), text)
                self.safe_area_page.click_next_page()
            # 点击下一页
            self.safe_area_page.click_next_page()
            # 获取最后一页数量
            number = self.safe_area_page.get_per_number()
            self.assertNotEqual(0, number)

            for n in range(int(page_number)):
                text = self.safe_area_page.get_page()
                self.assertEqual('%s/%s' % (str(int(page_number) - n), page_number), text)
                self.safe_area_page.click_ago_page()

            # 点击上一页
            self.safe_area_page.click_ago_page()
            number = self.safe_area_page.get_per_number()
            self.assertNotEqual(0, number)
