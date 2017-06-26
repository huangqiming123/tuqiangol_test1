import unittest
from time import sleep

from automate_driver.automate_driver import AutomateDriver
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.dev_manage.dev_manage_page_read_csv import DevManagePageReadCsv
from pages.dev_manage.dev_manage_pages import DevManagePages


class TestCase1103DevManageBatchSale(unittest.TestCase):
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
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_case_1103_dev_manage_batch_sale(self):
        # 打开途强在线首页-登录页
        self.base_page.open_page()
        # 登录
        self.log_in_base.log_in()
        # 点击进入设备管理
        self.dev_manage_page.enter_dev_manage()

        # 点击批量
        self.dev_manage_page.click_batch_sale_button()

        self.dev_manage_page.click_close_batch_sale_button()

        self.dev_manage_page.click_batch_sale_button()

        # 搜索右侧客户树
        # 循环点击5次
        for n in range(5):
            self.driver.click_element('x,//*[@id="treeDemo_device_sale_id_%s_span"]' % str(n + 1))
            sleep(2)
            # 判断数量
            get_account_dev_number = self.driver.get_text('x,//*[@id="treeDemo_device_sale_id_%s_span"]' % str(n + 1))

            name = self.dev_manage_page.get_select_account_name()
            self.assertEqual(get_account_dev_number, name)

        # 搜索无数据
        self.dev_manage_page.search_customer_after_click_batch_sale_dev('无数据')
        get_text = self.dev_manage_page.get_search_customer_no_data_text_after_batch_sale_dev()
        self.assertEqual('  暂无数据 ', get_text)

        # 获取选中设备的数量
        dev_number = self.dev_manage_page.get_select_dev_number()

        # 获取抬头设备统计的数量
        dev_numbers_count = self.dev_manage_page.get_dev_numbers()
        self.assertEqual(str(dev_number), dev_numbers_count)
