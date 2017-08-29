import unittest

from automate_driver.automate_driver import AutomateDriver
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.dev_manage.dev_manage_page_read_csv import DevManagePageReadCsv
from pages.dev_manage.dev_manage_pages import DevManagePages


class TestCase84DevManageBatchIssuedCommand(unittest.TestCase):
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

    def test_case_dev_manage_batch_issued_command(self):
        # 打开途强在线首页-登录页
        self.base_page.open_page()
        # 登录
        self.log_in_base.log_in()
        # 点击进入设备管理
        self.dev_manage_page.enter_dev_manage()

        # 点击批量
        self.dev_manage_page.click_batch_issued_command_button()

        self.dev_manage_page.click_close_batch_batch_issued_command_button()

        self.dev_manage_page.click_batch_issued_command_button()

        # 获取选中的设备数量
        dev_number = self.dev_manage_page.get_dev_number_after_click_issued_command()
        dev_number_count = self.dev_manage_page.get_count_number_after_click_issued_command()
        self.assertEqual(str(dev_number), dev_number_count)
