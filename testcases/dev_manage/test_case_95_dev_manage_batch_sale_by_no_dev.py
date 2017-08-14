import unittest
from time import sleep

from automate_driver.automate_driver import AutomateDriver
from model.assert_text import AssertText
from model.connect_sql import ConnectSql
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.dev_manage.dev_manage_page_read_csv import DevManagePageReadCsv
from pages.dev_manage.dev_manage_pages import DevManagePages


class TestCase1116DevManageBatchSaleByNoDev(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.dev_manage_page = DevManagePages(self.driver, self.base_url)
        self.driver.set_window_max()
        self.log_in_base = LogInBase(self.driver, self.base_url)
        self.dev_manage_page_read_csv = DevManagePageReadCsv()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.assert_text = AssertText()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_case_1116_dev_manage_batch_sale_by_no_dev(self):
        # 打开途强在线首页-登录页
        self.base_page.open_page()
        self.log_in_base.log_in()
        # 点击进入设备管理
        self.dev_manage_page.enter_dev_manage()
        # 点击批量
        self.dev_manage_page.click_batch_sale_button()
        self.dev_manage_page.click_close_batch_sale_button()
        self.dev_manage_page.click_batch_sale_button()
        # 验证界面
        get_sale_title = self.dev_manage_page.get_sale_title_text_in_sale_dev()
        self.assertEqual(self.assert_text.batch_sale_text(), get_sale_title)

        # 搜索框输入多个设备IMEI，点击添加（设备之间用enter键、逗号隔开）
        self.dev_manage_page.add_imei_in_sale_dev_page('121201234567889,867597011453591')
        get_dev_in_list_number = self.dev_manage_page.get_dev_in_list_number()
        self.assertEqual(2, get_dev_in_list_number)

        # 搜索框输入多个设备IMEI，点击添加（设备之间不用enter键、逗号隔开，而用空格隔开）
        self.dev_manage_page.add_imei_in_sale_dev_page('121201234567889867597011453591')
        add_dev_state = self.dev_manage_page.add_dev_after_fail_state()
        self.assertEqual(self.assert_text.dev_page_fail_text(), add_dev_state)
        add_dev_reason = self.dev_manage_page.add_dev_after_fail_reason()
        self.assertEqual(self.assert_text.dev_page_inexistence_text(), add_dev_reason)
        self.dev_manage_page.click_close_fails()

        # 不选择销售对象进行销售
        self.dev_manage_page.click_sale_button()
        # text = self.dev_manage_page.get_error_text_after_ensure()
        # self.assertEqual(self.assert_text.glob_search_please_add_account_text(), text)

        # 点击重置的按钮
        self.dev_manage_page.click_clear_button_in_dev_sale()
        get_dev_in_list_number = self.dev_manage_page.get_dev_in_list_number()
        self.assertEqual(0, get_dev_in_list_number)
