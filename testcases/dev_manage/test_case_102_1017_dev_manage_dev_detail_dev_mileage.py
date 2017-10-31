import unittest

from automate_driver.automate_driver import AutomateDriver
from model.assert_text import AssertText
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.dev_manage.dev_manage_page_read_csv import DevManagePageReadCsv
from pages.dev_manage.dev_manage_pages import DevManagePages


class TestCase102DevManageDevDetailDevMileage(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.dev_manage_page = DevManagePages(self.driver, self.base_url)
        self.driver.set_window_max()
        self.log_in_base = LogInBase(self.driver, self.base_url)
        self.dev_manage_page_read_csv = DevManagePageReadCsv()
        self.assert_text = AssertText()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_case_dev_manage_dev_detail_dev_mileage(self):
        # 打开途强在线首页-登录页
        self.base_page.open_page()
        # 登录
        self.log_in_base.log_in()
        # 点击进入设备管理
        self.dev_manage_page.enter_dev_manage()
        self.dev_manage_page.click_edit_button()
        self.dev_manage_page.click_close_edit_button()
        self.dev_manage_page.click_edit_button()

        # 点击客户信息
        self.dev_manage_page.click_cust_info_button()

        # 获取总里程的最大长度
        dev_total_mileage_max_len = self.dev_manage_page.get_dev_total_mileage_max_len()
        self.assertEqual('10', dev_total_mileage_max_len)

        # 输入非数字
        self.dev_manage_page.input_dev_total_mileage_in_dev_detail('1we23')
        # 获取异常的文字
        text = self.assert_text.dev_total_mileage_text1()
        self.dev_manage_page.click_ensure()
        web_text = self.dev_manage_page.get_text_after_input_dev_total_mileage()
        self.assertEqual(text, web_text)

        # 输入大于999999
        self.dev_manage_page.input_dev_total_mileage_in_dev_detail('1000000000')
        # 获取异常的文字
        text = self.assert_text.dev_total_mileage_text2()
        self.dev_manage_page.click_ensure()
        web_text = self.dev_manage_page.get_text_after_input_dev_total_mileage()
        self.assertEqual(text, web_text)
