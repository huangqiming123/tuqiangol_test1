import unittest
from time import sleep

from automate_driver.automate_driver import AutomateDriver
from model.assert_text import AssertText
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.dev_manage.dev_manage_page_read_csv import DevManagePageReadCsv
from pages.dev_manage.dev_manage_pages import DevManagePages


class TestCase80DevManageSearchCustomer(unittest.TestCase):
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

    def test_case_dev_manage_search_customer(self):
        # 打开途强在线首页-登录页
        self.base_page.open_page()
        self.base_page.click_chinese_button()
        # 登录
        self.log_in_base.log_in()
        # 点击进入设备管理
        self.dev_manage_page.enter_dev_manage()

        # 循环点击5次
        for n in range(5):
            self.driver.click_element('x,//*[@id="treeDemo_deviceManage_%s_span"]' % str(n + 2))
            sleep(2)
            # 判断数量
            get_account_dev_number = self.driver.get_text('x,//*[@id="treeDemo_deviceManage_%s_span"]' % str(n + 2))
            number = get_account_dev_number.split('(')[1].split('/')[0]

            dev_number = self.dev_manage_page.get_dev_number()
            self.assertEqual(number, str(dev_number))

        # 搜索无数据
        self.dev_manage_page.search_customer('无数据')
        get_text = self.dev_manage_page.get_search_customer_no_data_text()
        self.assertIn(self.assert_text.account_center_page_no_data_text(), get_text)
