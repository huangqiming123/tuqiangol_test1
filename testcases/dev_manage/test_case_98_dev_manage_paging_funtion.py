import unittest
from automate_driver.automate_driver import AutomateDriver
from model.assert_text import AssertText
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.dev_manage.dev_manage_page_read_csv import DevManagePageReadCsv
from pages.dev_manage.dev_manage_pages import DevManagePages


class TestCase98DevManagePagingFunction(unittest.TestCase):
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

    def test_dev_manager_paging_function(self):
        '''测试设备管理-设备搜索-by imei'''

        # 打开途强在线首页-登录页
        self.base_page.open_page()
        self.base_page.click_chinese_button()
        # 登录
        self.log_in_base.log_in_jimitest()
        # 点击进入设备管理
        self.dev_manage_page.enter_dev_manage()

        # 全部设备_分页默认显示每页20条
        # get_paging_text = self.dev_manage_page.get_paging_text()
        # self.assertEqual(self.assert_text.per_20_page(), get_paging_text)

        # 获取总共有多少页
        total_page_number = self.dev_manage_page.get_total_page_number_in_dev_manager()

        if total_page_number == 1:
            get_up_page_state = self.dev_manage_page.get_up_page_state()
            self.assertEqual('active', get_up_page_state)

            get_next_page_state = self.dev_manage_page.get_next_page_state()
            self.assertEqual('active', get_next_page_state)

        elif total_page_number == 0:
            text = self.dev_manage_page.get_search_no_dev_name_text()
            self.assertIn(self.assert_text.account_center_page_no_data_text(), text)

        else:
            for n in range(total_page_number):
                self.dev_manage_page.click_per_page(n + 1)

        if total_page_number != 0:
            self.dev_manage_page.click_per_number()
